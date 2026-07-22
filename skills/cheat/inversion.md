# Phase 1 — Question inversion

Ask the user. Sharp, not hostile:

> "What actually breaks if we don't build this?"

Categorize:

| Category | Signal | Action |
|----------|--------|--------|
| **Problem** | Something breaks. Real pain. | Trace the pain. Is the proposed solution the actual fix, or is there a root-cause fix that's cheaper? |
| **QoL / preference** | Nothing breaks. User just wants it. | Don't question further. "OK — this is about making things nicer." |
| **External requirement** | Compliance, contract, audit, "must have." | Don't question further. "External constraint — no gatekeeping." |

## For Problem

Dig one step deeper:
- "If the root problem is X, why is building Y the solution? What would a zero-code fix look like?"
- If the problem dissolves under scrutiny → propose dissolution. User decides, not you.
- Example: "We need a traffic sign web app" → "What problem?" → 10 people avoiding merge conflicts on Access DB, used 2x/year. Solution: Citrix. Free.

## Exit

| Outcome | Next |
|---------|------|
| Dissolved — user agrees | Stop. Record: `cheat: dissolved` |
| QoL | Proceed to Phase 2 |
| External | Proceed to Phase 2 |
| Survived | Proceed to Phase 2. Record: `cheat: survived — <root problem>` |
