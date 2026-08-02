# Agent Briefs

A structured comment that serves as the authoritative spec an AFK agent works from when an issue or PR moves to `ready-for-agent`.

## Principles

- **Durability over precision** — briefs must stay useful as the codebase evolves. Describe interfaces, types, and behavioral contracts. Name specific types, signatures, and config shapes. Never reference file paths or line numbers.
- **Behavioral, not procedural** — describe what the system should do, not how to implement it. The agent explores the codebase fresh and makes its own implementation decisions.
- **Complete acceptance criteria** — every brief needs concrete, testable, independently verifiable criteria so the agent knows when it's done.
- **Explicit scope boundaries** — state what's out of scope to prevent gold-plating or assumptions about adjacent features.

## Template

```markdown
## Agent Brief

**Category:** bug | enhancement

**Summary:** one sentence — what needs to happen.

**Current behavior:** what the system currently does.

**Desired behavior:** what the system should do instead.

**Key interfaces:** types, signatures, config shapes, behavioral contracts the agent should know about. No file paths or line numbers.

**Acceptance criteria:**
- [ ] Criterion 1
- [ ] Criterion 2

**Out of scope:** what the agent should NOT touch.
```

## Examples

### Bug brief

```markdown
## Agent Brief

**Category:** bug

**Summary:** skill descriptions in the `/skills` listing truncate mid-word instead of breaking at word boundaries.

**Current behavior:** descriptions over 80 characters are cut at character 80, even if that's in the middle of a word.

**Desired behavior:** descriptions truncate at the last word boundary before 80 characters, appending "…" only when truncated.

**Key interfaces:** the `formatSkillList()` function consumes `Skill.description: string` and produces display text. The truncation logic lives there.

**Acceptance criteria:**
- [ ] A description of exactly 75 chars displays in full, no "…"
- [ ] A description of 85 chars whose 80th char is mid-word truncates at the last space before 80, with "…"
- [ ] A description with no spaces before 80 chars truncates at 80 with "…"

**Out of scope:** changing the 80-char limit itself, or modifying any other part of the `/skills` output.
```

### Enhancement brief

```markdown
## Agent Brief

**Category:** enhancement

**Summary:** add `.out-of-scope/` directory support for tracking rejected feature requests.

**Current behavior:** rejected feature requests are closed with a comment. When a similar request arrives later, there's no structured way to surface the prior decision.

**Desired behavior:** a `.out-of-scope/` directory holds one markdown file per rejected concept. During triage of new enhancement requests, the triage agent reads this directory and surfaces matches.

**Key interfaces:** the triage skill reads `.out-of-scope/*.md` files. Each file follows a loose design-doc format with a "Why this is out of scope" section and a "Prior requests" list.

**Acceptance criteria:**
- [ ] `.out-of-scope/` directory exists and is documented in the triage skill's reference docs
- [ ] Rejected enhancements produce a new or updated file in `.out-of-scope/`
- [ ] Triage runs a dedup check against `.out-of-scope/` before recommending action

**Out of scope:** migrating existing closed-wontfix issues into `.out-of-scope/`, or modifying the issue tracker's native label system.
```

### PR brief

```markdown
## Agent Brief

**Category:** enhancement (PR)

**Summary:** finish the `--json` flag on the CLI — the contributor added the flag and default output, but errors still emit plain text and there's no test coverage.

**Current behavior (in the diff):** `--json` flag is parsed, success output is JSON. Error paths still write human-readable text to stderr. No tests exercise the JSON output path.

**Desired behavior:** all output (success and error) is valid JSON when `--json` is set. Test coverage confirms both paths.

**Key interfaces:** `cli.parseArgs()` returns `{json: boolean, ...}`. The `handleError()` function writes to `process.stderr` directly — it needs to accept a format parameter or check the flag.

**Acceptance criteria:**
- [ ] `--json` makes error output valid JSON (parseable, with `error` and `message` keys)
- [ ] Default output (no `--json`) is unchanged
- [ ] Tests cover both success-JSON and error-JSON paths

**Out of scope:** changing the JSON schema for success output, or adding `--json` to subcommands that don't yet support it.
```

### Bad brief (don't do this)

```markdown
Fix the triage bug. It's in `src/triage.ts` around line 150.
```

No category, no acceptance criteria, no scope, references a file path that will rot.
