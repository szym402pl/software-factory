---
name: cheat
description: Find the laziest path. Dissolve, steal, then build the minimum.
disable-model-invocation: true
user-invocable: true
---

# cheat

Four-phase skill. Fire after `/grilling`, before `/to-spec`.

**Phase 0: Internal check** — has this repo/project already solved it? → [[internal]]

**Phase 1: Inversion** — dissolve the requirement if it doesn't hold. Add "who checks?" reflex. → [[inversion]]

**Phase 2: Prior-art cheat** — research how others solved it (never fork/vendor), and use what's already in the stack. → [[prior-art-ladder]]

**Phase 3: Code cheat** — for what survives, find the shortest path. → [[routing]]
Route by project type to the right cheat surfaces, then go only as deep as necessary:

| Depth | When | File |
|-------|------|------|
| Quick-scan | Obvious stdlib/known answer | [[quick-scan]] |
| Standard | Common problem, "someone built this" | [[standard]] |
| Deep | novel territory | [[deep]] |

Override: `/cheat --quick` or `/cheat --deep`.

## The cheat ladder

Stop at the first rung that holds. User decides at each rung.

**Internal (check yourself first):**
0. **Check the repo** — existing codebase/monorepo, repo docs/ADRs, issue-tracker history. Cheapest possible source, zero license risk. → [[internal]]

**Prior art (research, never reuse):**
1. **Study prior art** — open-source clones, "X built with Y", awesome lists, starter kits. This is for architecture and approach only — never fork, vendor, or copy-paste someone's implementation into ours. Extract the pattern; we still build our own version.
2. **Check existing stack** — does a dependency or service already in the project quietly do this? This is reuse (it's infrastructure, not our product's own logic) — use it.

**Code — ours from scratch, except fixed mechanisms:**
3. **Fixed-mechanism check** — is this a solved, interchangeable problem (an algorithm, a protocol implementation, a crypto primitive, a stdlib-level utility) where we have no meaningful room to do it differently or better? Or is it our product's own logic/structure?
   - **Fixed mechanism** → stdlib? → native platform? → already-installed dep? → established library (check license + maintenance health, see [[routing]])? Use it, don't hand-roll it.
   - **Our own logic** → no shortcut. Code it from scratch, informed by rung 1's research. One line if one line does it; otherwise the minimum code that works.

Numbers are ordering, not a contract — treat this as one continuous spectrum, cheapest first, not a checklist to march through regardless of fit.

## License & legal gate

Applies to fixed mechanisms pulled in as dependencies (rung 3) — our own product code has no external license to worry about, since it's written from scratch.

- **Code (GitHub, npm, etc.)** — check the license file before adding a dependency. Copyleft (GPL, AGPL) can force your project's license. Confirm compatibility before installing.

If a candidate library's license is unclear or restrictive → don't vendor its code as a workaround. Either find an alternative library, or confirm this is our own logic and build it from scratch.

## Rules

User decides. PFE (Proudly Found Elsewhere) *as inspiration*, not as a fork — our own product logic is always coded from scratch, informed by what we found. NIH avoidance applies only to fixed mechanisms (algorithms, protocols, stdlib-level utilities): don't hand-roll those, pull them in as a dependency. Delete before building. Boring over clever.

Ask **"Who checks?"** — if nobody, the cheat ceiling is way higher. If something breaks, what actually happens?

Before every depth escalation: **"Found something. Need deeper?"** — respect the user's time.

Fast-moving domains (JS frameworks, AI/LLM tooling, anything with a recent major version) — one confirmation search even at quick-scan depth. "Well-known" can mean "well-known and already deprecated."

## Output

Feed into `/to-spec`. Output becomes `## Cheat check` in the spec:

```
- Verdict: dissolved | found internally | dependency used | built from scratch | killed by market
- Prior art studied: <what we looked at for inspiration, if anything>
- What we used as a dependency (fixed mechanisms only): <libs/stdlib, or none>
- From: <sources used>
- License check: <clear | flagged — see note | n/a, no dependency>
- Lazy path: <what to use as a dep, what to build ourselves, what to skip>
- User taste check: <which direction user picked from options>
```
