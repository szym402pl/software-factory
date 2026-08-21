# `.out-of-scope/`

A repo directory storing persistent records of rejected feature requests. Two purposes:

- **Institutional memory** — preserves why a feature was rejected, so the reasoning survives beyond the issue being closed.
- **Deduplication** — surfaces prior decisions when similar requests arrive, preventing re-litigation.

## Structure

One file per **concept** (kebab-case, e.g. `dark-mode.md`), not per issue. Multiple related issues are grouped under one file.

## Format

Relaxed, design-doc style:

```markdown
# <Concept name>

## Why this is out of scope

<durable reason — scope/philosophy, technical constraint, or strategic decision. NOT temporary circumstances like "we're too busy right now.">

## Prior requests

- [#42](link) — <one-line gist>
- [#87](link) — <one-line gist>
```

## Checking during triage

1. Read all files in `.out-of-scope/`.
2. Match by **concept similarity** — "night theme" matches `dark-mode.md`, "dark color scheme" matches it too. Don't keyword-match; think about what the request is really asking for.
3. Surface any matches to the maintainer. They may:
   - **Confirm** — append to Prior requests, close the issue as `wontfix`.
   - **Reconsider** — delete or update the file, proceed with triage normally.
   - **Disagree** — treat as distinct, proceed normally.

## Writing

Only for rejected **enhancements**, never bugs. Never write for "closed as `wontfix` because it's already implemented" — that would poison dedup checks (a future similar request should NOT surface an already-built feature as a rejection).

Flow:
1. Maintainer decides to reject an enhancement.
2. Match an existing file or create a new one.
3. Append the issue to "Prior requests" with a one-line gist.
4. Comment on the issue linking to the file.
5. Close with `wontfix`.

## Updating

If the maintainer changes their mind:
- Delete the file from `.out-of-scope/`.
- Old issues are historical records — no need to reopen them.
