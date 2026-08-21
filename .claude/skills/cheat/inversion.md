# Phase 1 — Question inversion

Comes after Phase 0 (internal check, [[internal]]) — if the org already solved this, you shouldn't reach here.

Ask two questions. Sharp, not hostile:

> "What actually breaks if we don't build this?"
> "Who checks? And what happens if it's not perfect?"

Categorize:

| Category | Signal | Action |
|----------|--------|--------|
| **Problem** | Something breaks. Real pain. | Trace the pain. Is the proposed solution the actual fix, or is there a root-cause fix that's cheaper? |
| **QoL / preference** | Nothing breaks. User wants it. | Don't question further. "OK — this is about making things nicer." |
| **External requirement** | Compliance, contract, audit, "must have." | Don't question further. "External constraint — no gatekeeping." |

## For Problem

Dig one step deeper:
- "If the root problem is X, why is building Y the solution? What would a zero-code fix look like?"
- If the problem dissolves under scrutiny → propose dissolution. User decides, not you.
- Example: "We need a traffic sign web app" → "What problem?" → 10 people avoiding merge conflicts on Access DB, used 2x/year. Solution: Citrix. Free.

## Who checks?

Operationalize the "stick exists — use it" reflex:

- **Nobody checks** → cheat ceiling is high. What's the laziest thing that works? An HTML file on Netlify? A Google Doc? A cron job on a spare machine? Propose it.
- **Someone checks, but casually** (boss glances at it, client sees demo) → cheat on everything invisible. Polish only the surface they see.
- **Formal gate** (PR review, compliance audit, security scan) → cheat on approach/design. Code must pass the gate.

Record the gate level in the cheat check output.

## Exit

| Outcome | Next |
|---------|------|
| Dissolved — user agrees | Stop. Record: `cheat: dissolved` |
| QoL | Proceed to Phase 2 |
| External | Proceed to Phase 2 |
| Survived | Proceed to Phase 2. Record: `cheat: survived — <root problem>` |
