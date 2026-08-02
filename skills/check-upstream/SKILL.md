---
name: check-upstream
description: Diff local skills against Matt Pocock's upstream skills repo and report divergence.
disable-model-invocation: true
---

# Check Upstream

Diff every skill in `skills/` against [mattpocock/skills](https://github.com/mattpocock/skills). Report divergence so the user decides what to pull.

## Process

### 1. Fetch upstream manifest

Matt's skills live under two directories:

- `https://github.com/mattpocock/skills/tree/main/skills/engineering`
- `https://github.com/mattpocock/skills/tree/main/skills/productivity`

WebFetch both pages. Extract every skill directory name (skip `README.md` and other files). Build a flat map: `{ skill_name: "engineering" | "productivity" }`.

Done when: every directory name from both pages is captured in the map.

### 2. Index local skills

List every subdirectory of `skills/` that contains a `SKILL.md`. That's the local set.

Done when: the local set is complete — every `skills/*/SKILL.md` accounted for.

### 3. Cross-reference

Three sets:

| Set | Meaning |
|-----|---------|
| **Overlap** | in both local and upstream |
| **Only local** | in `skills/` but not in Matt's repo |
| **Only upstream** | in Matt's repo but not in `skills/` |

Report only-local and only-upstream as simple lists — no diff needed.

### 4. Diff each overlapping skill

For **every** skill in the overlap set — no sampling, no skipping — fetch Matt's version from:

`https://raw.githubusercontent.com/mattpocock/skills/main/skills/{category}/{name}/SKILL.md`

Read the local `skills/{name}/SKILL.md`. Compare. Categorize:

- **Identical** — byte-for-byte same.
- **Minor diff** — small wording changes, formatting, or a few lines different. Summarize the delta in one sentence.
- **Customized** — local has deliberate additions/rewrites beyond upstream. List what was added/changed. Cross-check against the preservation registry below.
- **Major divergence** — upstream significantly restructured or expanded. Flag for manual review.

Done when: every overlapping skill has been fetched, diffed, and categorized — the count matches the overlap set size.

### 5. Report

```
## Upstream diff — mattpocock/skills

### Only upstream (N)
<list — skills Matt has that we don't>

### Only local (N)
<list — our custom skills>

### Overlap (N)
<one table row per skill: name | status | delta summary>

### Preservation required
<for each customized skill: what to preserve and how>
```

End with: "To update a skill: `WebFetch` its upstream raw URL, apply custom preservation if listed in the registry, write to `skills/<name>/SKILL.md`."

## Preservation registry

Some skills carry local customizations that must survive any upstream update. Before reporting, check each customized skill against this registry:

| Skill | Custom additions | How to preserve on update |
|-------|-----------------|--------------------------|
| `code-review` | 4 extra code smells: **Tight Coupling**, **Long Parameter List**, **Temporal Coupling**, **Leaky Abstraction** (lines after "Refused Bequest" in the smell baseline) | Fetch upstream, then reinsert the 4 custom smells into the list before writing |
| `codebase-design` | 5 extra principles under `## Principles`: **Organize by feature**, **Tests live with the code**, **Shared never imports from a feature**, **A file has one reason to change**, **Import from the defining module** (first 5 bullets under `## Principles`) | Fetch upstream, then reinsert the 5 principles as the first bullets under `## Principles` |

If other skills have accrued customizations, append to this registry — it grows over time.
