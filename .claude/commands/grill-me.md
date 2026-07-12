---
model: claude-fable-5
---

# `/grill-me [<artifact-or-scope>]` — Ad-hoc pre-alignment grill

Run on demand **before** opening a brainstorming session, a `docs/decisions/` memo, a course/stage restructure, or a rubric/template change. Converges decisions one branch at a time so the downstream brainstorm/memo/plan starts pre-aligned.

## What this command does

You run as a sequential, one-question-at-a-time interrogator. You augment (do NOT replace) `superpowers:brainstorming` — your job is to **converge** decisions, not expand the option space.

Follow the methodology in `.claude/skills/grill-me/SKILL.md` end-to-end:

- One question at a time, with a recommended answer; pause for the human after every question.
- Before any **structural recommendation** (new course/project/stage/template, rubric/weight change, restructure, supersession), run the **Auto-Pushback Pass** (mandatory Pass 1 in an R-table; Pass 2 on the objective threshold; 2-pass cap — human pushback is Pass 3).
- Before any **"new X"** recommendation, run the **Repo Convergence Check** (grep `courses/`, `docs/templates/`, `docs/decisions/`, `_archive/` — prefer extending an existing artifact; this repo's "no speculative restructuring" rule).
- Force grading decisions through the grading-domain guardrails (generosity-only curve, no double-deductions, score privacy, GAAP/IFRS neutrality, Excel-formulas).
- When a hard-to-reverse call settles → propose a `docs/decisions/` memo inline (hand to `/decision-memo`).

## Argument

`[<artifact-or-scope>]` — Optional. Examples:

- A decision-memo draft: `docs/decisions/2026-07-12-foo.md`
- A stage doc or rubric: `courses/.../projects/fx-hedging/stage3-ai-build-audit.md`
- A restructure proposal pasted inline
- A free-form scope: `whether to split BUS-620 DLEMBA into its own subject dir`

If no argument is given, ask what artifact or scope to grill before starting the core loop.

## Exit

Stop and hand off when all in-scope decisions are resolved or deferred, the human says "good, let's brainstorm now" / "ship it", or three consecutive "defer" answers fire (recommend upstream research, then exit).

## Output to terminal

End your run with one line: `Grilled <artifact>; <N> decisions converged, <M> deferred, <K> memo/glossary captures proposed.`
