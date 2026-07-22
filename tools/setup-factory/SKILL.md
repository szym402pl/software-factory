---
name: setup-factory
description: Bootstrap the Software Factory workflow into a new or existing project. Use when user says "setup factory", "bootstrap project", "new project", "initialize factory", or starts a fresh repo.
---

# Setup Factory

Installs the Software Factory workflow harness from `github.com/szym402pl/software-factory` into a target project.

## Step 1 — Verify GitHub auth

Run: `gh auth status`. If not authenticated, stop and tell user to run `gh auth login`.

## Step 2 — Choose mode

Ask user:

- **A: New project** — create GitHub repo + clone + install factory + commit + push
- **B: Existing repo** — clone from GitHub + install factory + commit + push
- **C: This folder** — install factory into current directory (user handles git)

## Step 3 — Execute

### Mode A — New project

1. Ask: project name? visibility (public/private, default private)?
2. `gh repo create <name> --<visibility> --clone`
3. `cd <name>`
4. Copy factory files (see "Copy procedure" below)
5. `git add -A && git commit -m "chore: install software-factory workflow" && git push`

### Mode B — Existing repo

1. Ask: repo URL (e.g. `owner/repo` or full URL)?
2. `gh repo clone <url>`
3. `cd <repo-dir>`
4. Copy factory files (see "Copy procedure" below)
5. `git add -A && git commit -m "chore: install software-factory workflow" && git push`

### Mode C — This folder

1. Verify: non-empty dir? Warn user if dir has code (will merge .gitignore).
2. Copy factory files.
3. Report: "Factory installed. Review changes and commit."

## Copy procedure

Clone factory repo to temp dir:

```bash
TEMP=$(mktemp -d)
git clone https://github.com/szym402pl/software-factory.git "$TEMP/factory"
```

Copy these files/dirs to the target project root, overwriting:

```
CLAUDE.md
PHILOSOPHY.md
skills/
tools/
docs/
.claude/
start.bat
```

IMPORTANT merge rules:
- **.gitignore**: Do NOT overwrite. Read both (factory + project). Append factory entries that don't already exist in project's .gitignore. If project has no .gitignore, copy factory's.
- **settings.local.json**: Skip — never copy. User-specific config.
- **router.md**: Copy factory template only if `docs/router.md` doesn't exist. If it does, skip (preserve user's codebase map).

Clean up: `rm -rf "$TEMP"`

## Step 4 — Report

List what was installed, where, and any files that were skipped/merged. Show the commit SHA if in mode A or B.

## Step 5 — Post-install offers

After reporting, offer these (if applicable):

### 5a. Domain modeling (existing code only)

If the target project has source files (>5), offer:

"Existing code detected. Want me to run `domain-modeling` to extract domain terms and build CONTEXT.md?"

If yes, invoke the `domain-modeling` skill.

### 5b. Wayfinder (new projects only)

If this is a new project (mode A), offer:

"Want to plan the project? I can run `wayfinder` to map out multi-session work as decision tickets."

If yes, invoke the `wayfinder` skill.
