---
name: claude-md-audit
description: Audit CLAUDE.md and the memory store (MEMORY.md + fact files) for drift — stale path citations, cross-file contradictions, duplicated facts, and bloat. Use periodically (monthly, or after a big restructure), not on every change. Read-only by default; reports findings by severity with file:line + suggested fix, and routes anything not fixed this session to a follow-up note. Auto-activates on `/claude-md-audit`.
tools: [Bash, Read, Grep, Glob, Edit]
---

# CLAUDE.md + Memory Audit Skill

This repo restructures `courses/` often (subject-first renames, archive moves, supersessions). Every restructure risks leaving CLAUDE.md or a memory citing a path that no longer exists. This skill catches that drift on a **periodic** scan rather than trying to check every commit (the most-skipped kind of rule).

## Scope

The canonical instruction + memory surface:

- **`CLAUDE.md`** (repo root) — the single project instruction file.
- **`MEMORY.md`** — the memory index loaded each session (at `~/.claude/projects/C--GitHub-shidler/memory/MEMORY.md`).
- **The memory fact files** — `feedback_*.md`, `project_*.md`, etc. in the same dir.

## The four checks (run all, in order)

### 1. Stale references (highest value here)

Extract every path CLAUDE.md and MEMORY.md cite (backtick-quoted paths, links, table "Path" columns) and confirm each resolves in the live tree:

```bash
# pull backtick-quoted paths from CLAUDE.md, test each
grep -oE '`[^`]+`' CLAUDE.md | tr -d '`' | grep -E '/|\.md|\.json|\.xlsx|\.py' | sort -u \
  | while read p; do [ -e "$p" ] || echo "MISSING: $p"; done
```

Do the same for MEMORY.md and for any path a fact file names in its body. Flag each miss with the citing `file:line` and the likely correct path (grep the tree for the basename — a restructure usually *moved* it, didn't delete it).

### 2. Cross-file contradictions

Compare claims that appear in more than one place — CLAUDE.md vs. a memory, or two CLAUDE.md sections. Common drift: a stage count, a weight table, a "current vs. archived" status, a naming convention. Quote both sides with `file:line`. (Example class: CLAUDE.md's "Active Courses" table vs. a `project_*` memory's description of the same course.)

### 3. Duplication + bloat

Facts stated in full in two places should live in one home with a pointer from the other (single-sourcing). Flag: a fact duplicated between CLAUDE.md and a memory; a memory that just restates code/git history (which the memory rules say not to store); a CLAUDE.md section that has grown past its usefulness.

### 4. Structural hygiene

- **Broken index links** — a `MEMORY.md` line pointing at a memory file that doesn't exist (run `/memory-hygiene`'s validator if present, or grep the linked filenames).
- **Orphan memories** — a fact file not referenced in `MEMORY.md`.
- **Dangling `[[refs]]`** — a `[[name]]` in a memory body with no matching file (may be a deliberate forward-ref — flag, don't auto-fix).

## Output

You are **read-only by default** — report and *offer* fixes; don't rewrite without approval. Group findings by severity:

```
CLAUDE.md + memory audit — <date>

ERRORS (broken references / contradictions)
- CLAUDE.md:NN — cites `path/that/moved.md`; now at `new/path.md`. Fix: update the citation.

WARNINGS (duplication / bloat / orphans)
- MEMORY.md — `feedback_foo.md` orphaned (not indexed). Fix: add index line or rotate.

HYGIENE (minor)
- feedback_bar.md — dangling [[baz]] (likely forward-ref; leave unless typo).
```

End with one terminal line:
`CLAUDE.md audit: <N> stale refs / <N> contradictions / <N> dup-or-bloat / <N> hygiene. <recommendation>.`

Route anything you don't fix this session into a short follow-up note in the audit output so it isn't lost. Fold in `npm run docs:validate` or an equivalent link-checker if one exists in the repo.

## Why a ritual, not a per-change rule

Drift is better *prevented* by single-sourcing each fact (one home + pointers) and *caught* by this periodic scan. Run it monthly or right after a `courses/` restructure — not on every edit.
