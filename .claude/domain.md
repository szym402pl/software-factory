# Domain Docs

How skills should consume this project's domain documentation when exploring the codebase.

## Before exploring, read these

- **`CONTEXT.md`** at the repo root — project glossary. Read it first.
- **`docs/adr/`** — architecture decisions touching the area you're about to work in.

If these files don't exist, proceed silently. `domain-modeling` skill creates them lazily when terms or decisions get resolved.

## File structure

Single-context (most projects):

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0001-event-sourced-orders.md
│   └── 0002-postgres-for-write-model.md
└── src/
```

## Use the glossary's vocabulary

When naming a domain concept (issue title, refactor, test name), use the term from `CONTEXT.md`. Don't drift to synonyms the glossary avoids.

If the concept you need isn't there, note it for `domain-modeling`.

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it:

> _Contradicts ADR-0007 (event-sourced orders) — but worth reopening because…_
