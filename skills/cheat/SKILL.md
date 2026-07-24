---
name: cheat
description: Find the laziest path. Dissolve, steal, then build the minimum.
disable-model-invocation: true
user-invocable: true
---

# cheat

Four-phase skill. Fire after `/grilling`, before `/to-spec`.

**Phase 0: Internal check** — has this team already built it? → [[internal]]

**Phase 1: Inversion** — dissolve the requirement if it doesn't hold. Add "who checks?" reflex. → [[inversion]]

**Phase 2: Creative cheat** — steal design, structure, or approach before writing code. → [[creative-ladder]]

**Phase 3: Code cheat** — for what survives, find the shortest path. → [[routing]]
Route by project type to the right cheat surfaces, then go only as deep as necessary:

| Depth | When | File |
|-------|------|------|
| Quick-scan | Obvious stdlib/known answer | [[quick-scan]] |
| Standard | Common problem, "someone built this" | [[standard]] |
| Deep | Genuinely novel territory | [[deep]] |

Override: `/cheat --quick` or `/cheat --deep`.

## The cheat ladder

Stop at the first rung that holds. User decides at each rung.

**Internal (check yourself first):**
0. **Ask the org** — existing codebase/monorepo, internal wiki, Slack/issue-tracker history. Cheapest possible source, zero license risk. → [[internal]]

**Creative (don't build):**
1. **Steal design** — Dribbble, Awwwards, ThemeForest, landing-page galleries
2. **Steal structure** — open-source clones, "X built with Y", awesome lists
3. **Steal approach** — competitor sites, adjacent industries, "how X does Y"
4. **Check existing stack** — do you already pay for a tool (Stripe, Auth0, CMS, analytics) that quietly does this?
5. **No-code / low-code** — Zapier/Make/n8n, Retool/Appsmith/Airtable, Bubble/Glide. Often the real answer for internal tools.
6. **Buy** — only if <$50 one-time. "This exists for $29. Cheaper than customizing."

**Code (build minimum):**
7. Stdlib? → use
8. Native platform? → use
9. Already-installed dep? → use
10. Library exists? → adapt (check license + maintenance health first, see [[routing]])
11. One line? → one line
12. Minimum code that works.

Numbers are ordering, not a contract — treat this as one continuous spectrum, cheapest first, not a checklist to march through regardless of fit.

## License & legal gate

Before anything from rungs 1–10 gets *adopted* (not just referenced for inspiration), check its license:
- **Design (Dribbble, ThemeForest, etc.)** — inspiration only unless the license explicitly permits implementation. Copying a shot pixel-for-pixel is infringement, not a cheat.
- **Code (GitHub, npm, etc.)** — check the license file. Copyleft (GPL, AGPL) can force your project's license. Confirm compatibility before forking or vendoring.
- **Templates (ThemeForest, WordPress themes)** — check redistribution/resale terms, not just the price.

If license is unclear or restrictive → downgrade to "steal the approach, not the artifact" and rebuild the specific part that's actually novel.

## Rules

User decides. PFE (Proudly Found Elsewhere), not NIH (Not Invented Here). Delete before building. Boring over clever.

Ask **"Who checks?"** — if nobody, the cheat ceiling is way higher. If something breaks, what actually happens?

Before every depth escalation: **"Found something. Need deeper?"** — respect the user's time.

Fast-moving domains (JS frameworks, AI/LLM tooling, anything with a recent major version) — one confirmation search even at quick-scan depth. "Well-known" can mean "well-known and already deprecated."

## Output

Feed into `/to-spec`. Output becomes `## Cheat check` in the spec:

```
- Verdict: dissolved | found internally | stolen | adapted | built | killed by market
- What we stole: internal asset | design | structure | approach | code
- From: <sources used>
- License check: <clear | flagged — see note>
- Lazy path: <what to use, build, skip>
- User taste check: <which direction user picked from options>
```
