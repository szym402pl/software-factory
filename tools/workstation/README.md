# Workstation — single-file edit loop

Eliminates Read→Edit→Read cycling. Pack changed files into one workstation.md,
edit freely (no re-reads), unpack→test→iterate.

## Commands

```bash
# 1. Pack files for current ticket
python tools/workstation/workstation.py pack src/foo.ts src/bar.ts --output workstation.md

# 2. Model reads workstation.md ONCE, then edits freely

# 3. Unpack + test feedback
python tools/workstation/workstation.py unpack workstation.md --test "npm test"

# 4. Model reads TEST OUTPUT section at bottom (cheap, ~200 tokens)
#    Fixes in same workstation.md → unpack → test → repeat until pass
```


## Workstation.md format

```
### ═══ FILE: src/foo.ts ═══
[content]

### ═══ FILE: src/bar.ts ═══
[content]

### ═══ TEST OUTPUT (last run) ═══
Status: FAIL (exit 1)
Command: npm test
────────────────────────────────────────────────────────────
test output here...
### ═══ END TEST OUTPUT ═══
```

## Token savings

| Approach | Files | Rounds | Reads | Cost |
|----------|-------|--------|-------|------|
| No workstation | 3 | 2 edits each | 6x Read (full files) | ~9000 tokens |
| With workstation | 3 | 2 edits each | 1x Read (workstation) + 3x test tail | ~2500 tokens |

~72% reduction on file reading.

## Integration

Add to CLAUDE.md under a "Workstation" section:

```
 ## Workstation (edit loop)
 When editing 2+ files, use workstation.md:
  1. pack <files> --output workstation.md → read once
  2. Edit within workstation.md (no re-reads)
  3. unpack workstation.md --test "npm test" → read TEST OUTPUT tail
  4. Fix → unpack → test → repeat until pass
```
