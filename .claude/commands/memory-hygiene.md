# `/memory-hygiene` — Validate + organize the memory store

Run periodically (every ~10 sessions), before a `/compact`, or after a session that wrote new memories. Keeps the Claude auto-memory store (`MEMORY.md` index + single-fact `*.md` files) coherent as it grows.

## What this command does

Follow the methodology in `.claude/skills/memory-hygiene/SKILL.md` end-to-end:

1. Run `.claude/skills/memory-hygiene/validate_memory.py` against `~/.claude/projects/C--GitHub-shidler/memory`.
2. Triage findings — **errors** (broken index links, missing `name:` frontmatter) get fixed; **warnings** (orphans, dangling `[[refs]]`, missing description/type) get fixed opportunistically or explained.
3. If `MEMORY.md` is crowded (>~25 lines), group the index by type (`feedback_*` together, `project_*` together) without editing fact content.

## Guardrails

- MEMORY.md is an **index** — one line per memory, pointer only, never fact content.
- A dangling `[[ref]]` is only a bug if it's a typo or points at a non-memory doc; deliberate forward-refs are allowed.
- Delete memories that are wrong; don't store what the repo already records.

## Output

The validator's findings, triaged, ending with:
`Memory hygiene: <N> memories / <E> errors / <W> warnings — <fixed / routed>.`
