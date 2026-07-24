# Phase 3 — Quick scan

For: CRUD, known patterns, obvious stdlib answers, boilerplate, "I could write this in 5 lines."

Check mental inventory. No web search, with one exception below. Answer from knowledge.

- Does stdlib do this?
- Does a native platform feature cover it?
- Is there an already-installed dependency that handles it?
- Is there a well-known library (no need to verify — model knows it exists)? Check its license before adding it, even at this depth.

## Stale-knowledge exception

Fast-moving domains — JS frameworks, AI/LLM tooling, anything with a recent major version bump — get one confirmation search even at this depth. "Well-known" from training data can mean "well-known and already deprecated or superseded." Everything else: answer from knowledge, no search.

Output: one-line verdict. "Use `structuredClone`. Done." or "Nothing does this. 3 lines. Build."
