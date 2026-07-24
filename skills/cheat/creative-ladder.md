# Phase 2 — Creative cheat

Comes after Phase 0 (internal check) — only run this if the org hasn't already solved it.

Before writing a single line of code. Steal what professionals already made.

## Rung 1: Steal design

Don't design. Find designs made by people better at it.

Sources:
- **Dribbble** — search `[project type] design`, `[project type] landing page`, `[project type] UI`
- **Awwwards** — browse by category. Winners have annotated case studies.
- **Behance** — search `[project type] UI`, full case studies with process
- **Landing page galleries** — landingfolio.com, land-book.com, onepagelove.com, saaslandingpage.com
- **ThemeForest / Creative Market** — search `[project type] template`. Screenshot previews. Steal layout, don't buy yet.
- **WordPress theme demos** — search `[project type] WordPress theme`. View live demo. Steal structure.
- **Tailwind UI / shadcn/ui blocks** — pre-built sections. Copy-pasteable.

Output to user: 2-3 design approaches found. "Any of these catch your eye?"

License note: Dribbble/Behance/Awwwards shots are inspiration, not implementation rights — copying one pixel-for-pixel is infringement. ThemeForest/theme purchases carry redistribution/resale terms that matter more than the price; check those, not just the $ tag.

## Example

"Need a pricing page." Search `saas pricing page design` on Dribbble and `pricing page` on landingfolio.com. Find three strong directions: tiered-cards, comparison-table, and slider-based. Surface all three with one-line notes on who each style suits, rather than picking one — user's taste is the filter, not the agent's.

## Rung 2: Steal structure

Someone already built something close. Find the repo, not the design.

Sources:
- **GitHub** — `[project name] clone`, `[tech stack] [project type]`, `[project type] open source`, `awesome-[domain]`
- **"Built with X" showcases** — Next.js, Tailwind, Laravel all have showcase pages. Filter by category.
- **ProductHunt / BetaList** — what launched recently in this space? Often open-source.
- **Alternative lists** — `X alternative open source`, opensourcealternative.to, alternativeto.net
- **Starter kits / boilerplates** — `[stack] boilerplate`, `[stack] starter`, `[stack] saas template`

Verdict options:
- **Clone exists, direction matches** → fork it
- **Structure exists, wrong domain** → steal architecture, rebuild content
- **Nothing close** → proceed to Rung 3

## Rung 3: Steal approach

Not code. Not design. The approach. How others think about this problem.

Sources:
- **Competitor sites** — how do they onboard? What's their information architecture? What's their pricing model?
- **Adjacent industries** — how does a totally different domain solve the same UX pattern?
- **YouTube** — `how to build X`, `X tutorial` at 2x. Steal the approach, not the code.
- **Technical blogs** — `how we built X at Y`, engineering blogs. Architecture decisions, not implementation.
- **HN / Reddit** — `Show HN: X`, `I built X`. Read comments. Users tell you exactly what works and what doesn't.
- **Conference talks** — `building X at scale`, `lessons from Y`. YouTube, filter >20min.

Output: "Here's how 2-3 others approach this. Pick the direction that feels right."

## Rung 4: Check existing stack

Before looking for anything new — do you already pay for a tool that quietly does this? Stripe, Auth0, your CMS, your analytics/email/search vendor all ship features that go unused. "We already have Stripe Radar, we don't need to build fraud scoring" beats any external cheat.

Output: "We already pay for X, which does this via <feature>. Turn it on before building anything."

## Rung 5: No-code / low-code

For internal tools especially, this is often the actual answer, not a fallback:
- **Automation** — Zapier, Make, n8n
- **Internal-tool builders** — Retool, Appsmith, Budibase
- **App builders** — Bubble, Glide, Airtable (+ its automations)

Output: "This is a Retool app, not a codebase." Sizing check: if it's used by <20 people or run infrequently, no-code usually wins even if it's less elegant.

## Rung 6: Buy (only if cheap)

If Rungs 1-3 found a close match AND it's <$50 one-time → propose buying.

"This exists for $29. We'd spend more than $29 of time customizing it."

Never propose: subscriptions, enterprise plans, marketplaces with per-sale cuts, anything >$50.

## Exit

| Rung outcome | Next |
|-------------|------|
| Design stolen — user likes a direction | Proceed to Phase 3 with design reference |
| Structure found — fork candidate | Propose fork. User decides. |
| Approach stolen — direction clear | Proceed to Phase 3 with approach reference |
| All rungs empty | "Genuine gap. Proceed to code cheat." → Phase 3 |
| User says "just build it" | Respect it. → Phase 3 |

Every rung that finds something → surface options to user. Don't grind forward silently. User's taste IS the filter.
