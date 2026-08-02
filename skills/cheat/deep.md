# Phase 3 — Deep

For: architecture decisions, wayfinder-scale, novel ideas, "this might not exist anywhere as a library."

## Strategy

Full who-solved-this-before-me approach, aimed at fixed mechanisms (see PHILOSOPHY.md #5/#6) — our own product logic still gets built from scratch, but informed by what this turns up.

1. **Generate vocabulary** — 6-10 framings from distinct vantage points (builder, user, academic, infrastructure, adjacent-community)
2. **Search** — 3-6 queries across GitHub (code/library search), npm, PyPI, crates.io, arXiv
3. **Trace one layer down** — every direct match → check its dependencies. "The larger referenced library is often the real incumbent."
4. **Cluster** — Direct / Adjacent / Partial / Abandoned (with last commit date)
5. **Vet supply chain** — for anything headed toward "use as a dependency": license type (flag copyleft), maintainer count, release cadence, known CVEs. A small, single-maintainer package with a recent CVE is a worse bet than an older, boring, widely-used one — "abandoned" isn't the only red flag.
6. **Extract patterns** — common architecture, libraries, naming — for our own build, not to copy
7. **Benchmark** — one honest paragraph: is this genuinely a fixed mechanism, or does our product's angle mean we should build it ourselves?
8. **Verdict** — Build it ourselves / Use existing library (dependency) / Contribute upstream instead of duplicating / Investigate first / Killed by market

## Budget

≤10 total queries. Stop earlier if landscape is clear after 3-4 queries and at least one dependency trace.

## Example

"Need a local-first sync engine for a notes app." Vocabulary: "CRDT library," "offline-first sync," "local-first database," "conflict-free replicated data type." Search surfaces Yjs, Automerge, and three abandoned side projects with the same pitch, all stalled at the same wall (conflict resolution UX, not the CRDT math). Trace one layer down: Automerge is used inside three larger local-first frameworks — the real incumbents, not Automerge itself. Pattern: nobody hand-rolls the CRDT algorithm from scratch anymore, it's a fixed mechanism; the differentiation is always in the sync transport and UI, which is our own product logic. Verdict: `Use Automerge as a dependency, build the transport layer and UI ourselves`.

## Killed by market

If deep research turns up several independent attempts at the same idea, all abandoned, with a consistent reason (not just "ran out of time") — that's a distinct signal from "nothing exists" (proceed to build) or "a library exists" (use it). Surface it as its own verdict rather than quietly filing it under "genuine gap." The user should see that pattern before committing.

## Output

Short markdown report:

```
## Prior art: <title ≤8 words>

### Landscape
| Name | Link | Status | Relevance | Bucket |
|------|------|--------|-----------|--------|
| ... | ... | ... | ... | Direct/Adjacent/Partial/Abandoned |

### Supply-chain notes
- <license flags, maintainer/CVE concerns for anything headed toward "use as dependency">

### Patterns
- <3-6 bullets on what the standard approach looks like — input to our own build>

### Differentiator
<one paragraph — honest comparison. Don't manufacture novelty.>

### Verdict
<one line: Build it ourselves | Use library Z as a dependency | Contribute to Y instead | Investigate first | Killed by market — <why others stalled>>
```
