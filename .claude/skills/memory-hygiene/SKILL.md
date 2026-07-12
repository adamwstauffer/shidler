---
name: memory-hygiene
description: Audit and maintain the Claude auto-memory store (MEMORY.md index + single-fact *.md files under ~/.claude/projects/C--GitHub-shidler/memory/). Use periodically, before a /compact, after a session that wrote new memories, or when MEMORY.md grows past ~25 entries. Runs validate_memory.py to find broken index links (errors), dangling [[name]] cross-refs and orphan files (warnings), and missing frontmatter. Auto-activates on `/memory-hygiene`.
tools: [Bash, Read, Edit, Write, Grep, Glob]
---

# Memory Hygiene Skill

Keeps this project's Claude memory store coherent as it grows. The store is the **external** per-project memory dir — `MEMORY.md` (the index loaded each session) plus the single-fact `*.md` files under `C:/Users/adamw/.claude/projects/C--GitHub-shidler/memory/`. It is **not** a repo directory; the validator lives in the repo and operates on it.

## When to invoke

- **Periodically** (every ~10 sessions) or when `MEMORY.md` passes ~25 index lines.
- **Before a `/compact`** — a clean index survives summarization better.
- **After a session wrote memories** — confirm new entries are indexed and cross-refs resolve.
- **When you notice drift** — a `[[link]]` that 404s, an entry describing a deleted/moved file.

## Step 1 — run the validator

```bash
python .claude/skills/memory-hygiene/validate_memory.py \
  --memory-dir "$HOME/.claude/projects/C--GitHub-shidler/memory"
# add --strict to exit non-zero on warnings; --json for a machine-readable report
```

On Windows PowerShell:

```powershell
python .claude/skills/memory-hygiene/validate_memory.py `
  --memory-dir "$env:USERPROFILE\.claude\projects\C--GitHub-shidler\memory"
```

## Step 2 — triage findings

| Finding | Severity | Fix |
|---|---|---|
| `MEMORY.md links to missing file: X` | **ERROR** | The index points at a deleted/renamed file. Update or remove the index line. |
| `missing required frontmatter key 'name'` | **ERROR** | Add a `name:` slug to the file's frontmatter. |
| `dangling [[slug]]` | warning | Either a typo (usually a missing `feedback_`/`project_` prefix — fix it) or a deliberate forward-ref to a memory not yet written (leave it). If it points at a **decision memo / spec**, that's a misuse of `[[ ]]` — convert to a plain path reference. |
| `not referenced in MEMORY.md (orphan)` | warning | Add a one-line index pointer, or delete if the fact is obsolete/wrong. |
| `missing description` / `missing type` | warning | Backfill the frontmatter opportunistically when you touch the file. |

**A `[[name]]` that doesn't resolve is not automatically a bug** — the memory convention allows forward-refs. Only fix the ones that are *typos* (wrong/missing prefix) or *mis-targeted* (pointing at a non-memory doc).

## Step 3 — organize (optional, when the index is crowded)

If `MEMORY.md` is past ~25 lines, group by type so recall stays cheap: keep the `feedback_*` (grading/house rules) together and the `project_*` (ongoing work) together. Don't rewrite content — this is index organization, not fact editing. Delete memories that turn out to be wrong (per the memory rules) rather than letting them accumulate.

## Guardrails

- **Never put fact content in MEMORY.md** — it's an index; one line per memory, no frontmatter, pointer only.
- **One fact per file** — if a fact file has grown to cover two things, that's a split candidate, not a hygiene error.
- **Don't store what the repo already records** — code structure, past fixes, git history, CLAUDE.md content. If you find such a memory, flag it for deletion.
