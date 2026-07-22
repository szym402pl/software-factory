#!/usr/bin/env bash
# Stop hook — warns if tests haven't passed this session
set -euo pipefail

# Check if package.json has a test script
if [ -f "package.json" ]; then
  has_test=$(jq -r '.scripts.test // ""' package.json)
  if [ -n "$has_test" ]; then
    echo "STOP CHECK: Run 'npm test' before ending session if you changed code." >&2
    echo "  Last test run status unknown — verify manually." >&2
  fi
fi

exit 0
