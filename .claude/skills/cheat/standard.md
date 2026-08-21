# Phase 3 — Standard

For: fixed-mechanism decisions — is there an established library for this well-defined sub-problem? "Someone definitely already published a package for this."

## Strategy

- 2-3 WebSearch queries
- Check npm / PyPI / crates.io first, GitHub only to read a library's source when docs are thin
- Different vocabulary per query (builder's words, user's words, adjacent-community framing)

## Checkpoint

Before escalating to deep, ask:

> "Found [N] options. Best: [one-line summary]. Use this as a dependency? Or is this actually specific enough to our product that we build it ourselves?"

User decides. Don't escalate without asking.

## Output

Short verdict with links:

```
Verdict: Use library X (dependency) | Build ourselves, no fixed mechanism fits
- [X](link) — what it does, why it fits
- [Y](link) — alternative considered, why not
- License/health check: <license type, maintainer count, last release — flag if copyleft or single-maintainer>
- If building ourselves: <1-2 lines on approach, informed by any prior art from Phase 2>
- Depth checkpoint: [user chose to stop | user wants deeper]
```
