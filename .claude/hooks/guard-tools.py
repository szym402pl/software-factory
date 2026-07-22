#!/usr/bin/env python3
"""
PreToolUse hook — one file, five gates.

1. Banned bash patterns  — blocks recursive/wildcard searches, forces Grep/Glob tools
2. Bash write escape     — blocks cat/echo redirects to source files, forces Write/Edit
3. Forbidden directories — blocks Read/Write/Edit inside .git, node_modules, dist, etc.
4. Forbidden extensions  — blocks binary/log/archive files
5. Branch gate           — blocks source file edits on main/master
"""
import json
import os
import re
import sys

# ── Config ──────────────────────────────────────────────────────────

FORBIDDEN_DIRS = {
    ".git", ".claude", ".idea", ".vscode", "node_modules",
    "build", "dist", "out", "output", "target", "bin", "obj",
    "vendor", "venv", ".venv", "__pycache__", "logs", ".next",
    "coverage", ".nyc_output",
}

FORBIDDEN_EXTS = {
    ".zip", ".7z", ".tar", ".tar.gz", ".iso", ".img",
    ".bin", ".elf", ".o", ".a", ".so", ".dll", ".exe",
    ".pt", ".ckpt", ".log",
}

BANNED_BASH_PATTERNS = [
    r"grep\s+-R\b", r"grep\s+-r\b",
    r"find\s+\.\s", r"find\s+/",
    r"ls\s+-R\b", r"\btree\s",
]

SOURCE_EXTS = {
    ".js", ".jsx", ".ts", ".tsx", ".py", ".go", ".rb", ".php",
    ".c", ".h", ".cc", ".cpp", ".cxx", ".hpp", ".hh",
    ".rs", ".java", ".cs", ".css", ".scss", ".html", ".vue", ".svelte",
    ".json", ".yaml", ".yml", ".toml", ".xml", ".md", ".sql",
}

# ── Bash write-escape detection ──────────────────────────────────────

def extract_bash_write_targets(command: str) -> list:
    """Find heredoc/redirect writes to source files."""
    targets = []
    # heredoc: cat > file.ts <<EOF ... EOF, tee file.ts <<EOF ... EOF
    heredoc_re = re.compile(
        r"""(?:cat|tee)\s+(?:-a\s+)?>{1,2}\s*(?P<path>[^\s<>|;&]+\.(?:ts|tsx|js|jsx|py|rs|go|java|cs|css|html|vue|svelte|json|yaml|yml|toml|xml|md|sql))\s*<<-?\s*['"]?(?P<delim>\w+)['"]?\s*\n(?P<body>.*?)\n\s*(?P=delim)\b""",
        re.VERBOSE | re.DOTALL,
    )
    for m in heredoc_re.finditer(command):
        targets.append((m.group("path"), m.group("body")))

    # simple redirect: echo "x" > file.ts, printf "x" >> file.ts
    redirect_re = re.compile(
        r"""[^<>|]>{1,2}\s*(?P<path>[^\s<>|;&]+\.(?:ts|tsx|js|jsx|py|rs|go|java|cs|css|html|vue|svelte|json|yaml|yml|toml|xml|md|sql))\b""",
    )
    for m in redirect_re.finditer(command):
        path = m.group("path")
        if path not in {t[0] for t in targets}:
            targets.append((path, command))

    return targets


# ── Main ────────────────────────────────────────────────────────────

def block(reason: str):
    print(reason, file=sys.stderr)
    sys.exit(2)


try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

tool_name = data.get("tool_name", "")
tool_input = data.get("tool_input", {})
file_path = tool_input.get("file_path", "") or ""

# Gate 1: Banned bash patterns
if tool_name == "Bash":
    command = tool_input.get("command", "")
    for pattern in BANNED_BASH_PATTERNS:
        if re.search(pattern, command):
            block(
                f"BLOCKED: '{pattern}' is a broad-search pattern. "
                f"Use the Grep or Glob tool instead — they have built-in "
                f"head_limit and don't blow up context."
            )

    # Gate 2: Bash write escape
    for target_path, _body in extract_bash_write_targets(command):
        norm = target_path.replace("\\", "/")
        block(
            f"BLOCKED: bash redirect to '{target_path}' detected. "
            f"Use the Write or Edit tool instead of cat/tee/echo redirects."
        )

# Gate 3 & 4: Forbidden dirs + extensions
# Block via directory component check AND direct path check
def hits_forbidden(path: str) -> tuple[bool, str]:
    """Returns (blocked, reason)."""
    norm = path.replace("\\", "/")
    parts = set(norm.split("/"))

    for d in FORBIDDEN_DIRS:
        if d in parts:
            return True, f"'{path}' is inside forbidden directory '{d}'"

    for ext in FORBIDDEN_EXTS:
        if norm.endswith(ext):
            return True, f"'{path}' has forbidden extension '{ext}'"

    return False, ""


if tool_name in ("Read", "Edit", "Write", "MultiEdit", "Grep", "Glob"):
    # Check file_path
    blocked, reason = hits_forbidden(file_path)
    if blocked:
        block(f"BLOCKED: {reason}")

    # Grep/Glob: also check the 'path' param
    if tool_name in ("Grep", "Glob"):
        search_path = tool_input.get("path", "")
        if search_path:
            blocked2, reason2 = hits_forbidden(search_path)
            if blocked2:
                block(f"BLOCKED: {reason2}")

    # Gate 5: Branch gate (only for Write/Edit/MultiEdit on source files)
    if tool_name in ("Write", "Edit", "MultiEdit"):
        ext = os.path.splitext(file_path)[1].lower()
        if ext in SOURCE_EXTS:
            try:
                import subprocess
                branch = subprocess.run(
                    ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                    capture_output=True, text=True, timeout=5,
                ).stdout.strip()
                if branch in ("main", "master"):
                    block(
                        f"BLOCKED: editing '{file_path}' on '{branch}'. "
                        f"Never edit main directly. Create a feature branch: "
                        f"git checkout -b <feature-name>"
                    )
            except Exception:
                pass  # Not a git repo — allow

sys.exit(0)
