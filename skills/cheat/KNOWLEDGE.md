# Cheat — operational patterns

Non-obvious techniques for Phase 2 deep research.

## Vocabulary generation

Before searching, reframe the idea 6-10 ways:
- Builder's words ("state machine library", "FSM implementation")
- User's words ("form wizard", "multi-step form")
- Academic ("finite automaton", "statecharts")
- Infrastructure ("event-driven workflow engine")
- Adjacent community ("game AI behavior trees")

Different framings surface different project clusters. One framing = one lens only.

## Trace one layer down

On every direct match → check its dependencies, "built with X" mentions, "inspired by Y" notes. The larger referenced project is often the real incumbent. Most skills fail here — they stop at the first match.

## Cluster

| Bucket | Signal |
|--------|--------|
| Direct | Same problem, same approach |
| Adjacent | Same problem, different approach |
| Partial | Subset of the problem |
| Abandoned | Last commit >1yr, archived, no maintainers |

If all queries return the same project, you haven't reached different clusters. Reword.

## Verdict

Pick one. No "it depends":
- **Build it** — genuine gap
- **Fork X** — close but wrong direction
- **Contribute to Y** — missing feature, project healthy
- **Use Z** — already solved
- **Investigate first** — something exists but unclear if it fits (read issue tracker)
