# Phase 2 — Deep

For: architecture decisions, wayfinder-scale, novel ideas, "this might not exist anywhere."

## Strategy

Full who-built-this-before-me approach:

1. **Generate vocabulary** — 6-10 framings from distinct vantage points (builder, user, academic, infrastructure, adjacent-community)
2. **Search** — 3-6 queries across GitHub, npm, PyPI, ProductHunt, HN Show HN, arXiv
3. **Trace one layer down** — every direct match → check its dependencies. "The larger referenced project is often the real incumbent."
4. **Cluster** — Direct / Adjacent / Partial / Abandoned (with last commit date)
5. **Extract patterns** — common architecture, libraries, naming, pricing
6. **Benchmark** — one honest paragraph: does the user's angle genuinely differ?
7. **Verdict** — Build it / Fork & extend / Contribute / Use existing / Investigate first

## Budget

≤10 total queries. Stop earlier if landscape is clear after 3-4 queries and at least one dependency trace.

## Output

Short markdown report:

```
## Prior art: <title ≤8 words>

### Landscape
| Name | Link | Status | Relevance | Bucket |
|------|------|--------|-----------|--------|
| ... | ... | ... | ... | Direct/Adjacent/Partial/Abandoned |

### Patterns
- <3-6 bullets on what the standard approach looks like>

### Differentiator
<one paragraph — honest comparison. Don't manufacture novelty.>

### Verdict
<one line: Build it | Fork X | Contribute to Y | Use Z | Investigate first>
```
