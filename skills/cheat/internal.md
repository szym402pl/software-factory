# Phase 0 — Internal check

Before any external source: has this repo/project already solved it? Cheapest possible source — no search cost, no license risk, no vetting needed.

## Check in order

1. **Codebase** — grep for similar function names, similar domain terms, similar file structure. A half-finished attempt still saves time.
2. **Repo docs** — CONTEXT.md, docs/adr/, docs/router.md, README. "We decided against X because Y" is as valuable as code.
3. **Issue tracker** — search for the feature name, the pain point, adjacent tickets. Someone may have scoped this already, or explicitly decided not to build it (and why).
4. **Ask the user** — if search comes up empty, ask before building from scratch. Still cheaper than a from-scratch build.

## Verdict

- **Found working code/asset** → use or adapt it. Skip to Phase 3 output only if adaptation is nontrivial.
- **Found an abandoned attempt** → read it before dismissing it. Why did it stall — technical dead end, or just deprioritized?
- **Found a prior explicit decision not to build this** → surface it to the user before proceeding. Circumstances may have changed, but don't silently ignore it.
- **Nothing found** → proceed to Phase 1.

## Exit

| Outcome | Next |
|---------|------|
| Reusable asset found | Verdict: `found internally`. Stop, or adapt with reference to it. |
| Prior decision found | Surface to user. User decides whether to proceed. |
| Nothing found | Proceed to Phase 1 → [[inversion]] |
