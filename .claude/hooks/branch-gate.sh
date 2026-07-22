#!/usr/bin/env bash
# PreToolUse hook — blocks edits on main/master branch
set -euo pipefail

# Parse the tool input from stdin
input=$(cat)
command=$(echo "$input" | jq -r '.tool_input.command // ""')

# Only block write operations (Edit, Write, Bash that writes files)
# Read-only operations pass through
is_write_op=false
case "$command" in
  *">"*|*">>"*|*"git commit"*|*"git merge"*|*"git rebase"*)
    is_write_op=true
    ;;
esac

if [ "$is_write_op" = false ]; then
  exit 0
fi

# Check current branch
branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "no-git")

if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
  echo "BRANCH GATE: You are on '$branch'. Create a feature branch first." >&2
  echo "  git checkout -b <feature-name>" >&2
  exit 2
fi

exit 0
