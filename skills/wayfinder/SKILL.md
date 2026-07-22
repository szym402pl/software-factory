---
name: wayfinder
description: Plan work too big for one agent session. Create a shared map of decision tickets, resolve one per session until the route is clear.
disable-model-invocation: true
user-invokable: true
---

# wayfinder

You plan work too big for one agent session. You chart a map of **decision** tickets — not deliverables — and resolve them one at a time until the route to the goal is clear. You don't do the work itself; you clear the fog so someone (or a later session) can.

## Rules

- **Map is one issue** labeled `wayfinder:map`. Tickets are **child issues** with `wayfinder:<type>` labels.
- **Refer by name.** Every map and ticket is referenced by title, never bare ID. Names read at a glance; numbers don't.
- **Block with native dependencies.** Use the tracker's blocking edges.
- **One ticket per session.** Never resolve more than one in a single session (research tickets are the exception).
- **Plan, don't do.** The urge to "just build it" is the signal you've reached the map's edge — hand off.

## The Map

A single issue labeled `wayfinder:map`:

```
## Destination
<one-or-two-line description of what "done" looks like>

## Notes
<domain context, skills to consult, preferences>

## Decisions so far
- <one-line gist> → <link to closed ticket>
- ...

## Not yet specified
<fog of war — in-scope work you sense but can't yet phrase sharply>

## Out of scope
<work consciously ruled beyond the destination>
```

## Ticket types

| Type | Mode | Purpose |
|------|------|---------|
| **Research** | AFK | Docs, APIs, knowledge bases — resolved by the `/research` skill |
| **Prototype** | HITL | Cheap throwaway artifact to react to — resolved by `/prototype` |
| **Grilling** | HITL | One-question-at-a-time — resolved by `/grilling` and `/domain-modeling` |
| **Task** | HITL or AFK | Manual work blocking a decision. The only type that *does* rather than decides |

Each ticket body has a `## Question` section — the sharp question it answers.

## Frontier

The frontier = open, unblocked, unclaimed child tickets. This is the edge of what's known. Pick from the frontier to advance.

## Fog of war

The map is deliberately incomplete. The test: can you state the question **precisely** now? (Not *answer* it — just *phrase* it sharply.)

- Sharp question → ticket (even if blocked)
- Fuzzy shape → "Not yet specified"

Resolving a ticket clears fog ahead. What was fuzzy graduates to fresh tickets.

## Two modes

### 1. Chart the map

1. Name the destination via `/grilling` + `/domain-modeling`
2. Map the frontier breadth-first — what must be decided?
3. Create the `wayfinder:map` issue
4. Create specifiable tickets as children
5. Wire blocking edges
6. Fire research tickets in parallel subagents
7. **Stop.** Charting is one session's work.

### 2. Work through the map

1. Load the map from the issue URL/number
2. Pick a ticket from the frontier (first one if not specified)
3. Claim it (assign yourself)
4. Resolve the decision via the appropriate skill
5. Record resolution as a comment on the ticket
6. Close the ticket, append to "Decisions so far"
7. Graduate fog — anything newly specifiable → fresh tickets
8. Handle out-of-scope: decisions that turned out beyond scope get a line in "Out of scope", not "Decisions so far"
9. **Never resolve more than one ticket per session** (research tickets excepted)
