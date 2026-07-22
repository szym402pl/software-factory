---
name: cheat
description: Find the laziest path. Dissolve requirements that don't hold, then find the shortest path for what survives.
disable-model-invocation: true
user-invokable: true
---

# cheat

Two-phase skill. Fire after `/grilling`, before `/to-spec`.

**Phase 1:** Question inversion — dissolve the requirement if it doesn't hold. → [[inversion]]

**Phase 2:** Lazy path — for what survives, find the shortest route. Pick depth:
- CRUD, boilerplate, stdlib answers → [[quick-scan]]
- New feature, dependency, "how to X" → [[standard]]
- Architecture, wayfinder, "does this exist?" → [[deep]]

Override: `/cheat --quick` or `/cheat --deep`.

## Output

Feed into `/to-spec`. Your output becomes a `## Cheat check` section in the spec:

```
- Verdict: survived | dissolved | qol | external
- Root problem: <if survived>
- Lazy path: <what to use, what to build, what to skip>
```

## The ladder

Regardless of depth, stop at the first rung:
1. Does this need to exist? → skip
2. Stdlib? → use
3. Native platform? → use
4. Already-installed dep? → use
5. Library exists? → adapt
6. One line? → one line
7. Minimum code that works.

**Rules:** User decides. PFE, not NIH. Delete before building. Boring over clever.
