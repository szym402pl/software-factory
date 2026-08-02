# Phase 2 — Prior-art ladder

Comes after Phase 0 (internal check) and Phase 1 (inversion) — only run this if the requirement survived and nothing internal covers it.

Before writing our own code: has someone already solved something close (worth reading, not copying), and does the project already depend on something that quietly covers this?

## Rung 1: Study prior art

Someone already built something close. Find it and read it — for architecture, data model, and approach. This is research, not sourcing. **We do not fork, vendor, or copy-paste any of it into our codebase.** We build our own implementation, informed by what we learned.

Sources:
- **GitHub** — `[project name] clone`, `[tech stack] [project type]`, `[project type] open source`, `awesome-[domain]`
- **"Built with X" showcases** — Next.js, Tailwind, Laravel, etc. have showcase pages, filterable by category
- **Alternative lists** — `X alternative open source`, opensourcealternative.to, alternativeto.net
- **Starter kits / boilerplates** — `[stack] boilerplate`, `[stack] starter` (read for structure, don't clone it in)

What to extract: how they modeled the domain, what they got wrong (issues/PRs are often more instructive than the code), what tradeoffs they made and why.

Verdict options:
- **Close reference found** → note the pattern, proceed to build our own version of it
- **Nothing close** → proceed to Rung 2 with no prior art to lean on, that's fine

## Rung 2: Check existing stack

Before looking for anything new — does the project already depend on something that quietly does this? An auth library that already supports SSO, an ORM feature that already handles soft-deletes, a queue that already supports delayed jobs. This is genuine reuse — it's infrastructure we already chose, not our product's own logic. Turn on a feature before adding a dependency; add a dependency before writing custom code for something that's a fixed mechanism (see [[routing]] for that distinction).

## Exit

| Rung outcome | Next |
|-------------|------|
| Prior art found — pattern to build from | Build our own version informed by it. → Phase 3 |
| Existing dependency covers it | Verdict: `found in stack`. Use it. |
| Nothing found | "Genuine gap, no prior art to lean on. Proceed to code cheat." → Phase 3 |
| User says "just build it" | Respect it. → Phase 3 |

Every rung that finds something → surface it to the user before proceeding. Don't grind forward silently.
