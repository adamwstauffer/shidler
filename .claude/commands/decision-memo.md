---
model: claude-fable-5
---

# `/decision-memo [<topic-or-path>]` — Author a decision memo (Fable-pinned)

Run when you need to capture a **decision** — a ratified choice, a course/project restructure, a trade-off resolution, a deprecation/supersession, a grading-policy call. Pinned to **Fable**: these memos are canonical and caught only at human review, so they get the strongest judgment model regardless of session model.

This command writes a memo under `docs/decisions/`. It does **not** write stage assignments, templates, or specs — a decision memo records *why* a choice was made; live materials implement it (CLAUDE.md working principle: "when records *document* a past change, update live materials, not the record").

## What this command does

You author a decision memo to house standard. Work in this order:

1. **Grep prior decisions FIRST.** Search `docs/decisions/` **and** `_archive/` for memos on the same topic before drafting. If one exists, decide: amend it, or write a new memo that explicitly **supersedes** it (and note the old one as superseded). Course-specific memos carry the `-<course-code>-` infix (e.g. `2026-05-07-bus629-stage2-restructure.md`); repo-wide ones don't.
2. **Verify load-bearing claims against ground truth** before asserting them — path/link claims via `Grep`/`Read` with `file:line` citations; spreadsheet claims via the `xlsx` skill / `recalc.py`; doc claims by opening the doc at HEAD. A memo that cites a moved path is worse than no memo.
3. **Draft to house format.** Match the existing memos exactly:
   - YAML frontmatter: `title`, `date`, `status: proposed`, `owner: Adam W. Stauffer`, `scope`, `related: [<prior memo filenames>]`.
   - Body: `## Executive Summary` (100–150 words, active voice — the CLAUDE.md writing convention), `## Background`/`## Context`, `## Decisions` (numbered, each with **Action** + **Rationale**), `## Alternatives considered` (rejected options *with reasons*), `## Consequences`, `## Status`.
   - Filename: `docs/decisions/YYYY-MM-DD-<slug>.md` (add the `-<course-code>-` infix for course-specific memos).
   - If Claude drafted it for review, open with the house callout: `> **Drafted by Claude for Adam's review — nothing here is adopted.**`
4. **Pause for ratification.** End by naming what ratifying unblocks. Do **not** flip `status:` to `accepted`/`implemented` until Adam ratifies — leave it `proposed`.

## Argument

`[<topic-or-path>]` — Optional. A topic to decide, or a path to a draft/notes to formalize. If nothing is given and nothing was pasted, ask what decision to capture before starting.

## Output

A memo file under `docs/decisions/`. End your run with one line:
`Drafted decision memo <slug> (status: <status>); <N> prior memos checked. Awaiting ratification.`
