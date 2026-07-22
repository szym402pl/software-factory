# Software Factory

## Rules

- **Research-first.** Before building anything new: WebSearch → GitHub → npm. Someone already built it. Adapt, don't invent.
- **Branch gate.** Never edit `main` directly. Branch per feature/fix. Hook blocks it physically.
- **Concision.** When reporting to the user, be extremely concise. Sacrifice grammar for concision.
- **No Explore subagent.** Never use `Agent(subagent_type="Explore")`. Each spawn eats ~50K tokens (cold cache miss). Use Grep/Glob tools directly.
- **Only factory skills.** Never invoke skills outside `skills/` directory. No caveman, no ponytail, no external plugins.

## Navigation

| File/Dir | What it is | When to read |
|----------|-----------|-------------|
| `skills/` | 13 agent skills | Invoked on demand, never pre-loaded |
| `.claude/domain.md` | How domain docs work | Auto-read by skills when exploring code |
| `.claude/issue-tracker.md` | Where issues live | Auto-read by `to-tickets`, `to-spec` |
| `.claude/settings.json` | Hooks + permissions | Never — config, not context |
| `CONTEXT.md` | Project glossary (if exists) | Auto-read by skills when exploring code |
| `docs/router.md` | What lives where (file→purpose map) | Before Grep/Glob — consult first |
| `docs/adr/` | Architecture decisions (if exists) | Auto-read by skills when touching that area |

## Skills

**Vocabulary layer — runs beneath every other skill:**
- `codebase-design` — deep modules, seams, interfaces, depth, leverage, locality. Design every module through this lens. Without it, code goes shallow and sloppy.
- `domain-modeling` — CONTEXT.md glossary, ADRs. Keeps terminology precise across the whole project.

**Build loop (user-invoked):**
`grilling` sharpens ideas → `cheat` (research existing solutions) → `to-spec` crystallizes → `to-tickets` splits into tracer bullets. Prefer larger tickets (~1 session each) — workstation amortizes per-ticket overhead.

**Implementation loop (model-invoked):**
`tdd` (red-green at pre-agreed seams) + `code-review` (2 sub-agents after every ticket. 2-axis: Standards + Spec).
After each ticket: update `docs/router.md` — add new modules, update changed responsibilities, remove deleted files. One line per file.

**Emergency & support:**
`diagnosing-bugs` (6-phase, Phase 1 = tight pass/fail signal before any hypothesis), `research` (background agent, primary sources), `prototype` (throwaway code for design questions), `resolving-merge-conflicts`.

**Session management (user-invoked):**
`handoff` — compact conversation to markdown, reference artifacts, fresh agent picks up.

**Setup (user-invoked, one-time):**
`setup-pre-commit`, `git-guardrails-claude-code`.

All skills in `skills/`. Invoked on demand, never pre-loaded.

## Commands

Check `package.json` scripts. Default: `npm test` (typecheck + suite).

## Workstation (edit loop)

When editing 2+ files, use workstation.md instead of per-file Read/Edit cycle:

1. `pack file1 file2 ... --output workstation.md` → read workstation.md ONCE
2. Edit workstation.md with **MultiEdit** (one call, many changes). No re-reads.
3. `unpack workstation.md --test "npm test" --tail 40` → read **TEST OUTPUT tail only**
   This REPLACES separate `npm test` — do NOT run both. One test run, in unpack.
   Use --tail for suites with many tests (keeps failures + last N lines).
4. Fix → unpack → test → repeat until PASS

Skip workstation for single-file edits — TDD + direct Edit is faster.

