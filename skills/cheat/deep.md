# Phase 3 — Deep

For: architecture decisions, wayfinder-scale, novel ideas, "this might not exist anywhere."

## Strategy

Full who-built-this-before-me approach:

1. **Generate vocabulary** — 6-10 framings from distinct vantage points (builder, user, academic, infrastructure, adjacent-community)
2. **Search** — 3-6 queries across GitHub, npm, PyPI, ProductHunt, HN Show HN, arXiv
3. **Trace one layer down** — every direct match → check its dependencies. "The larger referenced project is often the real incumbent."
4. **Cluster** — Direct / Adjacent / Partial / Abandoned (with last commit date)
5. **Vet supply chain** — for anything headed toward "adapt": license type (flag copyleft), maintainer count, release cadence, known CVEs. A small, single-maintainer package with a recent CVE is a worse bet than an older, boring, widely-used one — "abandoned" isn't the only red flag.
6. **Extract patterns** — common architecture, libraries, naming, pricing
7. **Benchmark** — one honest paragraph: does the user's angle genuinely differ?
8. **Verdict** — Build it / Fork & extend / Contribute / Use existing / Investigate first / Killed by market

## Budget

≤10 total queries. Stop earlier if landscape is clear after 3-4 queries and at least one dependency trace.

## Example

"Need a local-first sync engine for a notes app." Vocabulary: "CRDT library," "offline-first sync," "local-first database," "conflict-free replicated data type." Search surfaces Yjs, Automerge, and three abandoned side projects with the same pitch, all stalled at the same wall (conflict resolution UX, not the CRDT math). Trace one layer down: Automerge is used inside three larger local-first frameworks — the real incumbents, not Automerge itself. Pattern: nobody builds the CRDT layer from scratch anymore; the differentiation is always in the sync transport and UI, not the algorithm. Verdict: `Use Automerge, build the transport layer`.

## Killed by market

If deep research turns up several independent attempts at the same idea, all abandoned, with a consistent reason (not just "ran out of time") — that's a distinct signal from "nothing exists" (proceed to build) or "something exists" (use it). Surface it as its own verdict rather than quietly filing it under "genuine gap." The user should see that pattern before committing.

## Output

Short markdown report:

```
## Prior art: <title ≤8 words>

### Landscape
| Name | Link | Status | Relevance | Bucket |
|------|------|--------|-----------|--------|
| ... | ... | ... | ... | Direct/Adjacent/Partial/Abandoned |

### Supply-chain notes
- <license flags, maintainer/CVE concerns for anything headed toward "adapt">

### Patterns
- <3-6 bullets on what the standard approach looks like>

### Differentiator
<one paragraph — honest comparison. Don't manufacture novelty.>

### Verdict
<one line: Build it | Fork X | Contribute to Y | Use Z | Investigate first | Killed by market — <why others stalled>>
```
