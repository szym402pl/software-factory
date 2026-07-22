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
"""

import sys
import subprocess
from pathlib import Path


DELIMITER = "### ═══ FILE:"
TEST_DELIMITER = "### ═══ TEST OUTPUT"
TEST_DELIMITER_END = "### ═══ END TEST OUTPUT"


def pack(file_paths: list[str]) -> str:
    """Read files and produce workstation.md content."""
    parts = []
    for path in file_paths:
        p = Path(path)
        try:
            content = p.read_text(encoding="utf-8")
        except FileNotFoundError:
            parts.append(f"{DELIMITER} {path} ═══\n")
            parts.append(f"(FILE NOT FOUND: {path})\n\n")
            continue
        except (UnicodeDecodeError, PermissionError) as e:
            parts.append(f"{DELIMITER} {path} ═══\n")
            parts.append(f"(ERROR reading {path}: {e})\n\n")
            continue

        parts.append(f"{DELIMITER} {path} ═══\n")
        parts.append(content)
        if not content.endswith("\n"):
            parts.append("\n")
        parts.append("\n")

    parts.append(f"{TEST_DELIMITER} (last run) ═══\n")
    parts.append("(no test output yet — run unpack --test)\n")
    parts.append(f"{TEST_DELIMITER_END} ═══\n")

    return "".join(parts)


def unpack(workstation_path: str, test_cmd: str | None = None, tail_lines: int = 0) -> None:
    """Parse workstation.md, write files back, optionally run tests.
    tail_lines: if > 0, keep only last N lines of test output.
    """
    text = Path(workstation_path).read_text(encoding="utf-8")

    # Split into sections by the DELIMITER
    sections = split_by_delimiter(text)

    written_files = []
    for file_path, content in sections:
        if not file_path:
            continue
        p = Path(file_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        written_files.append(file_path)
        print(f"  wrote: {file_path}")

    if not written_files:
        print("  WARNING: no files found in workstation.md")
        return

    if test_cmd:
        run_tests_and_append(workstation_path, test_cmd, tail_lines)


def run_tests_and_append(workstation_path: str, test_cmd: str, tail_lines: int = 0) -> None:
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

    # Smart truncate: keep failure-signaling lines + tail
    if tail_lines > 0:
        output = smart_truncate(output, tail_lines)

    # Read current workstation, strip old TEST OUTPUT section, append new
    text = Path(workstation_path).read_text(encoding="utf-8")
    text = strip_test_section(text)

    new_section = (
        f"{TEST_DELIMITER} (last run) ═══\n"
        f"Status: {status}\n"
        f"Command: {test_cmd}\n"
        f"{'─' * 60}\n"
        f"{output.strip()}\n"
        f"{TEST_DELIMITER_END} ═══\n"
    )

    Path(workstation_path).write_text(text.rstrip("\n") + "\n\n" + new_section, encoding="utf-8")
    print(f"  test: {status}")


def split_by_delimiter(text: str) -> list[tuple[str, str]]:
    """Parse workstation.md into list of (file_path, content)."""
    lines = text.splitlines(keepends=True)
    sections: list[tuple[str, str]] = []
    current_path: str | None = None
    current_lines: list[str] = []

    for line in lines:
        if line.startswith(DELIMITER) and not line.startswith(TEST_DELIMITER):
            # Save previous section
            if current_path is not None:
                sections.append((current_path, join_content(current_lines)))
            # Start new section
            current_path = parse_file_path(line)
            current_lines = []
        elif line.startswith(TEST_DELIMITER):
            # Stop collecting file content — any following sections after test
            # output would be re-split anyway, but stop here to avoid capturing
            # test output as file content.
            if current_path is not None:
                sections.append((current_path, join_content(current_lines)))
            current_path = None
            current_lines = []
        elif current_path is not None:
            current_lines.append(line)

    # Last section
    if current_path is not None:
        sections.append((current_path, join_content(current_lines)))

    return sections


def parse_file_path(line: str) -> str:
    """Extract file path from delimiter line.
    Format: ### ═══ FILE: src/foo.ts ═══
    """
    # Remove the prefix and suffix
    inner = line.removeprefix(DELIMITER).strip()
    # Remove trailing box chars
    inner = inner.removesuffix("═══").strip()
    return inner


def join_content(lines: list[str]) -> str:
    """Join content lines, stripping trailing newlines (exactly one at end)."""
    if not lines:
        return ""
    # Strip trailing empty lines (blank lines before next section or EOF)
    while lines and lines[-1].strip() == "":
        lines.pop()
    if not lines:
        return ""
    return "".join(lines)


def smart_truncate(output: str, max_lines: int) -> str:
    """Keep last N lines + any FAIL/Error lines from the dropped prefix.
    Ensures error messages are never lost even if they're above the tail window."""
    lines = output.splitlines()
    if len(lines) <= max_lines:
        return output

    tail = lines[-max_lines:]
    prefix = lines[:-max_lines]

    # Collect failure-signaling lines from prefix
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


def strip_test_section(text: str) -> str:
    """Remove everything from first TEST_DELIMITER to end."""
    idx = text.find(TEST_DELIMITER)
    if idx == -1:
        return text
    # Also look for the end delimiter to be safe
    end_idx = text.find(TEST_DELIMITER_END)
    if end_idx != -1:
        end_line_end = text.find("\n", end_idx)
        if end_line_end != -1:
            return text[:idx].rstrip("\n") + "\n"
    return text[:idx].rstrip("\n") + "\n"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "pack":
        # Parse: pack file1 file2 ... --output workstation.md
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
