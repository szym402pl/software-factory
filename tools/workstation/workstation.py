"""
workstation.py — pack files into single workstation.md, unpack back after edits.

Usage:
  pack:   python tools/workstation/workstation.py pack file1.ts file2.ts --output workstation.md
          writes workstation.md to specified path (no shell redirect — guard-safe).

  unpack: python tools/workstation/workstation.py unpack workstation.md [--test "npm test"]
          splits files back, overwriting originals.
          runs test command if provided, appends ### TEST OUTPUT section.

Workflow:
  pack --output workstation.md → Read once → Edit freely → unpack --test → repeat.
  Single Read replaces N Reads across the edit loop.

Safety:
  Each pack run stamps a random nonce into its delimiters and writes a MANIFEST
  header listing the exact files packed. unpack() re-parses the file using that
  same nonce, then validates the parsed sections against the manifest — same
  paths, same count, same order — BEFORE writing anything back to disk. If a
  delimiter line got mangled by an edit, or file content happens to contain
  literal delimiter-shaped text, the mismatch is caught and unpack aborts with
  no files written, instead of silently corrupting or merging file contents.
"""

import sys
import subprocess
import secrets
from pathlib import Path


MANIFEST_PREFIX = "### ═══ MANIFEST"
TEST_MARKER = "TEST OUTPUT"


def make_nonce() -> str:
    return secrets.token_hex(4)


def file_delimiter(nonce: str) -> str:
    return f"### ═══ FILE[{nonce}]:"


def test_delimiter(nonce: str) -> str:
    return f"### ═══ {TEST_MARKER}[{nonce}]"


def test_delimiter_end(nonce: str) -> str:
    return f"### ═══ END {TEST_MARKER}[{nonce}]"


def pack(file_paths: list[str]) -> str:
    """Read files and produce workstation.md content, stamped with a nonce
    and a manifest so unpack() can validate before writing anything back."""
    nonce = make_nonce()
    fdelim = file_delimiter(nonce)
    tdelim = test_delimiter(nonce)
    tdelim_end = test_delimiter_end(nonce)

    parts = []
    manifest_paths = []
    warnings = []

    for path in file_paths:
        p = Path(path)
        try:
            content = p.read_text(encoding="utf-8")
        except FileNotFoundError:
            parts.append(f"{fdelim} {path} ═══\n")
            parts.append(f"(FILE NOT FOUND: {path})\n\n")
            manifest_paths.append(path)
            continue
        except (UnicodeDecodeError, PermissionError) as e:
            parts.append(f"{fdelim} {path} ═══\n")
            parts.append(f"(ERROR reading {path}: {e})\n\n")
            manifest_paths.append(path)
            continue

        # Guard: warn (don't silently corrupt) if content already contains
        # something delimiter-shaped. The nonce makes an exact collision
        # astronomically unlikely, but a near-miss is worth flagging.
        if "### ═══ FILE" in content or "### ═══ MANIFEST" in content:
            warnings.append(path)

        parts.append(f"{fdelim} {path} ═══\n")
        parts.append(content)
        if not content.endswith("\n"):
            parts.append("\n")
        parts.append("\n")
        manifest_paths.append(path)

    manifest_lines = "\n".join(f"  - {mp}" for mp in manifest_paths)
    manifest = (
        f"{MANIFEST_PREFIX}[{nonce}] ═══\n"
        f"files: {len(manifest_paths)}\n"
        f"{manifest_lines}\n"
        f"{MANIFEST_PREFIX}-END ═══\n\n"
    )

    body = "".join(parts)
    body += f"{tdelim} (last run) ═══\n"
    body += "(no test output yet — run unpack --test)\n"
    body += f"{tdelim_end} ═══\n"

    if warnings:
        print(
            "  WARNING: possible delimiter-shaped text found in: "
            + ", ".join(warnings)
            + " — nonce should still keep sections separated correctly, "
              "but double-check the unpack validation output."
        )

    return manifest + body


def read_manifest(text: str) -> tuple[str, list[str]]:
    """Extract (nonce, expected_paths) from the MANIFEST header.
    Raises ValueError if no manifest is found (e.g. hand-edited or
    pre-guard workstation.md) — caller should treat this as unsafe to unpack."""
    lines = text.splitlines()
    nonce = None
    expected: list[str] = []
    in_manifest = False

    for line in lines:
        if line.startswith(MANIFEST_PREFIX) and line.endswith("-END ═══"):
            break
        if line.startswith(MANIFEST_PREFIX):
            # ### ═══ MANIFEST[abcd1234] ═══
            inner = line[len(MANIFEST_PREFIX):]
            if "[" in inner and "]" in inner:
                nonce = inner[inner.index("[") + 1: inner.index("]")]
            in_manifest = True
            continue
        if in_manifest and line.strip().startswith("- "):
            expected.append(line.strip()[2:])

    if nonce is None:
        raise ValueError(
            "No MANIFEST header found — this workstation.md wasn't produced "
            "by the current pack(), or the header was edited/removed. "
            "Refusing to unpack: cannot safely validate section boundaries."
        )
    return nonce, expected


def unpack(workstation_path: str, test_cmd: str | None = None, tail_lines: int = 0) -> None:
    """Parse workstation.md, VALIDATE against its manifest, and only then
    write files back. Runs tests afterward if requested."""
    text = Path(workstation_path).read_text(encoding="utf-8")

    try:
        nonce, expected_paths = read_manifest(text)
    except ValueError as e:
        print(f"  ABORTED: {e}")
        sys.exit(1)

    fdelim = file_delimiter(nonce)
    tdelim = test_delimiter(nonce)

    sections = split_by_delimiter(text, fdelim, tdelim)
    parsed_paths = [path for path, _ in sections]

    # Validate before writing anything: same set, same count, same order.
    # A mismatch means a delimiter line was mangled, duplicated, or content
    # collided with delimiter-shaped text — don't guess, abort.
    mismatches = diff_manifest(expected_paths, parsed_paths)
    if mismatches:
        print("  ABORTED: parsed sections don't match the manifest — nothing was written.")
        for m in mismatches:
            print(f"    {m}")
        print(
            "  This usually means a FILE delimiter line was edited/deleted, "
            "or file content collided with delimiter-shaped text. "
            "Re-pack from the original files and redo the edit."
        )
        sys.exit(1)

    written_files = []
    for file_path, content in sections:
        p = Path(file_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        written_files.append(file_path)
        print(f"  wrote: {file_path}")

    if not written_files:
        print("  WARNING: no files found in workstation.md")
        return

    if test_cmd:
        run_tests_and_append(workstation_path, test_cmd, nonce, tail_lines)


def diff_manifest(expected: list[str], parsed: list[str]) -> list[str]:
    """Return a list of human-readable mismatch descriptions, empty if clean."""
    issues = []
    if expected == parsed:
        return issues

    expected_set, parsed_set = set(expected), set(parsed)
    missing = [p for p in expected if p not in parsed_set]
    extra = [p for p in parsed if p not in expected_set]
    dupes = [p for p in parsed if parsed.count(p) > 1]

    if missing:
        issues.append(f"missing sections (in manifest, not found in body): {missing}")
    if extra:
        issues.append(f"unexpected sections (found in body, not in manifest): {extra}")
    if dupes:
        issues.append(f"duplicate sections (likely a merged/split file): {sorted(set(dupes))}")
    if not issues and expected != parsed:
        issues.append(f"same files but different order: expected {expected}, got {parsed}")

    return issues


def run_tests_and_append(workstation_path: str, test_cmd: str, nonce: str, tail_lines: int = 0) -> None:
    """Run test command and append output to workstation.md.
    tail_lines: if > 0, keep only last N lines + preserve any line containing 'FAIL' or 'Error:'.
    """
    print(f"\n  running: {test_cmd}")
    try:
        result = subprocess.run(
            test_cmd,
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
            cwd=Path.cwd(),
        )
        output = (result.stdout or "") + (result.stderr or "")
        exit_code = result.returncode
    except subprocess.TimeoutExpired:
        output = "TEST TIMEOUT (>120s)"
        exit_code = -1

    status = "PASS" if exit_code == 0 else f"FAIL (exit {exit_code})"

    if tail_lines > 0:
        output = smart_truncate(output, tail_lines)

    tdelim = test_delimiter(nonce)
    tdelim_end = test_delimiter_end(nonce)

    text = Path(workstation_path).read_text(encoding="utf-8")
    text = strip_test_section(text, tdelim)

    new_section = (
        f"{tdelim} (last run) ═══\n"
        f"Status: {status}\n"
        f"Command: {test_cmd}\n"
        f"{'─' * 60}\n"
        f"{output.strip()}\n"
        f"{tdelim_end} ═══\n"
    )

    Path(workstation_path).write_text(text.rstrip("\n") + "\n\n" + new_section, encoding="utf-8")
    print(f"  test: {status}")


def split_by_delimiter(text: str, fdelim: str, tdelim: str) -> list[tuple[str, str]]:
    """Parse workstation.md into list of (file_path, content), using this
    pack's nonce-stamped delimiters. Content between MANIFEST-END and the
    first FILE delimiter (or stray text outside any section) is ignored."""
    lines = text.splitlines(keepends=True)
    sections: list[tuple[str, str]] = []
    current_path: str | None = None
    current_lines: list[str] = []

    for line in lines:
        if line.startswith(fdelim):
            if current_path is not None:
                sections.append((current_path, join_content(current_lines)))
            current_path = parse_file_path(line, fdelim)
            current_lines = []
        elif line.startswith(tdelim):
            if current_path is not None:
                sections.append((current_path, join_content(current_lines)))
            current_path = None
            current_lines = []
        elif current_path is not None:
            current_lines.append(line)

    if current_path is not None:
        sections.append((current_path, join_content(current_lines)))

    return sections


def parse_file_path(line: str, fdelim: str) -> str:
    """Extract file path from a delimiter line: '<fdelim> src/foo.ts ═══'."""
    inner = line[len(fdelim):].strip()
    inner = inner.removesuffix("═══").strip()
    return inner


def join_content(lines: list[str]) -> str:
    """Join content lines, stripping trailing blank lines (exactly one at end)."""
    if not lines:
        return ""
    while lines and lines[-1].strip() == "":
        lines.pop()
    if not lines:
        return ""
    return "".join(lines)


def smart_truncate(output: str, max_lines: int) -> str:
    """Keep last N lines + any FAIL/Error lines from the dropped prefix."""
    lines = output.splitlines()
    if len(lines) <= max_lines:
        return output

    tail = lines[-max_lines:]
    prefix = lines[:-max_lines]

    signals = []
    for line in prefix:
        stripped = line.strip()
        if any(
            keyword in stripped
            for keyword in ("FAIL ", "Error:", "error:", "PASS ", "Tests:", "assert")
        ):
            signals.append(line)

    if signals:
        return "\n".join(signals) + "\n... (" + str(len(lines) - max_lines) + " lines truncated) ...\n" + "\n".join(tail)
    else:
        return "... (" + str(len(lines) - max_lines) + " lines truncated) ...\n" + "\n".join(tail)


def strip_test_section(text: str, tdelim: str) -> str:
    """Remove everything from the first test delimiter to end."""
    idx = text.find(tdelim)
    if idx == -1:
        return text
    return text[:idx].rstrip("\n") + "\n"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "pack":
        args = sys.argv[2:]
        output_path = None
        files = []
        i = 0
        while i < len(args):
            if args[i] == "--output" and i + 1 < len(args):
                output_path = args[i + 1]
                i += 2
            else:
                files.append(args[i])
                i += 1

        if not files:
            print("Usage: workstation.py pack file1 file2 ... --output workstation.md")
            sys.exit(1)
        if not output_path:
            print("ERROR: --output <path> is required")
            sys.exit(1)

        content = pack(files)
        Path(output_path).write_text(content, encoding="utf-8")
        print(f"  packed {len(files)} files -> {output_path}")

    elif cmd == "unpack":
        if len(sys.argv) < 3:
            print("Usage: workstation.py unpack <workstation.md> [--test \"npm test\"] [--tail N]")
            sys.exit(1)

        workstation_path = sys.argv[2]
        test_cmd = None
        tail_lines = 0
        args = sys.argv[3:]
        i = 0
        while i < len(args):
            if args[i] == "--test" and i + 1 < len(args):
                test_cmd = args[i + 1]
                i += 2
            elif args[i] == "--tail" and i + 1 < len(args):
                tail_lines = int(args[i + 1])
                i += 2
            else:
                i += 1

        if not Path(workstation_path).exists():
            print(f"ERROR: {workstation_path} not found")
            sys.exit(1)

        unpack(workstation_path, test_cmd, tail_lines)

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
