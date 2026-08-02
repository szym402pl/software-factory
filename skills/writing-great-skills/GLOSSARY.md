# Glossary

Disclosed reference for `writing-great-skills`. Every term is a lever on **Predictability** — "the degree to which a skill makes the agent behave the same _way_ on every run."

## Invocation — how a skill is reached

**Model-Invoked** — skill keeps a **description** (the machine-readable trigger), so the agent can fire it autonomously _and_ the human can still type the name. Trade: permanent **context load** (tokens + attention) every turn. Mechanics: omit `disable-model-invocation`.

**User-Invoked** — skill strips the description, invisible to the agent, reachable only by the human. Zero context load, but the human becomes the index — that's **cognitive load**, the price of human agency. Mechanics: set `disable-model-invocation: true`.

**Context Load** — tokens + attention a model-invoked skill's description costs every turn. Aggregate across all model-invoked skills.

**Cognitive Load** — the human's burden of remembering which user-invoked skills exist and when to reach for them. Grows with every user-invoked skill.

**Router Skill** — a user-invoked skill that names the other user-invoked skills and when to reach for each. Cures cognitive load. Can only hint, never fire them.

**Granularity** — how finely skills are divided. Each split spends one of the two loads (context or cognitive), so split only when the cut earns it.

## Information hierarchy — how content is arranged

**Step** — an ordered action in `SKILL.md`. Primary tier of the ladder. Each step ends on a **completion criterion**.

**Reference** — a definition, rule, or fact, consulted on demand. Can live in-skill (secondary tier) or behind a **context pointer** (disclosed tier).

**Information Hierarchy** — the ladder ranking material by how immediately the agent needs it: in-skill steps → in-skill reference → disclosed reference behind a context pointer.

**Progressive Disclosure** — moving reference down the ladder (out of `SKILL.md` into a linked file) to keep the top legible. Licensed by **branching**: disclose what only some branches need, inline what every path needs.

**Context Pointer** — a named reference encoding the condition for when the agent should reach the linked material. Its _wording_, not its target, decides reach reliability.

**Branch** — a distinct path through a skill. Different runs take different branches. The cleanest disclosure test: inline what every branch needs; push behind a pointer what only some branches reach.

**Co-location** — the within-file companion to the ladder: keep a concept's definition, rules, and caveats under one heading rather than scattered, so reading one part brings its neighbours with it.

**External Reference** — a plain file outside the skill system that any skill can point at. The only shared home two user-invoked skills can use.

**Sprawl** — a skill simply too long, even when every line is live and unique. Cure: the ladder — disclose reference behind pointers, split by branch or sequence.

## Steering — shaping runtime behavior

**Leading Word** — a compact concept from the model's pretraining (e.g. _lesson_, _fog of war_, _tracer bullets_) that anchors behavior in few tokens. Repeats as a token, never a sentence. Serves predictability twice: anchors execution in the body, anchors invocation in the description.

**Completion Criterion** — the condition telling the agent a unit of work is done. Its **clarity** resists **premature completion**; its **demand** sets **legwork**.

**Premature Completion** — ending a step before it's genuinely done, attention slipping to _being done_ because **post-completion steps** are visible ahead. Defence: sharpen the criterion first (cheap, local); only split by sequence when the criterion is irreducibly fuzzy _and_ you observe the rush.

**Post-Completion Steps** — the steps still ahead that tempt the agent to rush the current one. Visible in-skill; hiding them (splitting by sequence) encourages more legwork.

**Legwork** — the behind-the-scenes digging the agent does within a step. Driven by a demanding completion criterion, whether the skill has steps or not.

**Negation** — steering by prohibition. Backfires: _don't think of an elephant_ names the elephant. Cure: prompt the **positive** — state the target behaviour so the banned one is never spoken.

**No-Op** — an instruction that changes nothing because the model already does it by default. Model-relative; settled by running the skill, not debate. A weak leading word (_be thorough_ when the agent is already thorough-ish) is a no-op; fix with a stronger word (_relentless_).

## Pruning — keeping it lean

**Single Source of Truth** — each meaning in exactly one authoritative place. **Duplication** violates it.

**Duplication** — the same meaning in more than one place. Costs maintenance and tokens, inflates a meaning's prominence past its real rank.

**Relevance** — does a line still bear on what the skill does? The primary pruning test.

**Sediment** — stale accumulation never cleared. The default fate of any skill without a pruning discipline. Distinct from sprawl: sediment is stale; sprawl can be live but too long.
