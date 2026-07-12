---
name: grill-me
description: Use when the user types "/grill-me", says "grill me", "stress-test this", or "interrogate the plan" — a sequential, one-question-at-a-time interrogation that converges decisions BEFORE they calcify in a decision memo, a course/stage restructure, a rubric, or a template. Augments (does not replace) brainstorming: brainstorming expands the option space, grill-me converges it. Includes a mandatory Auto-Pushback Pass and a Repo Convergence Check that enforces this repo's "no speculative restructuring" principle.
tools: [Read, Grep, Glob, Bash, Edit, Write]
---

# Grill-Me Skill

**Authority:** This skill augments `superpowers:brainstorming`; it does NOT replace it. Brainstorming expands the option space — grill-me **converges** decisions before they calcify in a memo, a restructure, a rubric, or a template. Adapted from `mattpocock/skills/grill-me`, retargeted from a software/database domain onto this docs/Markdown/Excel repo.

## When to invoke

Ad-hoc, user-triggered. Invoke manually **before**:

- Opening a `docs/decisions/` memo on a non-trivial call (a restructure, a grading-policy change, a supersession).
- A course/subject-directory restructure or a stage-doc redesign.
- A rubric or weight change (e.g. re-weighting stages, changing a curve floor).
- A new template or a change to an existing one.
- **Any brainstorming session** the user wants pre-aligned (typed `/grill-me` or "grill me on X").

## When NOT to invoke

- Mid-way through a mechanical batch (e.g. grading student N of 20) — pre-align *before* the batch, not during.
- For obvious, no-ambiguity edits (fix a typo, add one bullet).
- Pure conversational tasks (status, summaries, lookups).
- After the user has already explicitly entered `superpowers:brainstorming` — grill-me runs **before**, not in parallel.

## Core loop

**One question at a time. Recommend an answer. Pause for the human.**

```
1. Read the artifact (memo draft, stage doc, rubric, template, restructure proposal)
2. Identify the next unresolved decision branch
3. Ask ONE question with:
   - The specific decision being made
   - A recommended answer (with reasoning)
4. Pause. Wait for the human to confirm / redirect / dig deeper.
5. If a term or convention crystallizes → propose capturing it inline (glossary line, or a decision-memo row)
6. If a hard-to-reverse decision settles → propose a `docs/decisions/` memo inline (hand to /decision-memo)
7. Loop until exit criteria met
```

Never batch-dump questions. Never advance the tree until the current branch resolves.

## Auto-Pushback Pass (MANDATORY before presenting any structural recommendation)

Human pushback at every grill iteration consistently surfaces improvements the skill should have caught itself. Making the human run that pass is a skill failure. This institutionalizes it.

**A "structural recommendation" here means:** a new course/subject directory, a new project or stage, a new template, a rubric/weight change, a supersession/archive move, or a restructure of `courses/` — anything hard to reverse once materials propagate. It does **not** mean a typo fix, a one-line addition, or a pure lookup.

### The recipe

After drafting a structural recommendation and BEFORE presenting it to the human:

1. **Run Pass 1 — MANDATORY.** Explicitly review the draft for improvements, missed cases, and simpler alternatives. Surface findings in a structured table (never a silent self-correction):

   ```markdown
   | R | Finding | Resolution |
   |---|---|---|
   | R1 | <specific issue caught> | <how it changed the recommendation> |
   | R2 | ... | ... |
   ```

2. **Decide if Pass 2 fires.** Pass 2 triggers IF Pass 1 found **≥3 substantive improvements** OR a **P0 issue** (would break a referenced path, duplicate an existing artifact, violate a grading memory, or leak a score). Objective threshold — not subjective "significant."
3. **Hard cap = 2 passes.** Never run Pass 3 yourself — **human pushback IS Pass 3.** (Exception: the human explicitly says "do another pass.")
4. **Scope filter.** Auto-pass fires only on structural recommendations (above). Skip it on pure edits, lookups, and decision-log appends with no new structural content.

The forcing function is the table: silent "looks good!" rubber-stamping is forbidden. The human reads the table to see what the pass caught vs. what they still catch.

## Repo Convergence Check (MANDATORY before any "new course / project / stage / template / spreadsheet" recommendation)

This repo's CLAUDE.md is explicit: **"no speculative restructuring," "surgical changes," "do the task that was asked."** Before recommending a *new* anything, prove it isn't already there — grill-me does the convergence work so the human doesn't have to.

Before recommending a new course directory, project, stage, template, spreadsheet, or decision-memo pattern, execute these checks AND surface the results in the grill response:

1. **Existing-artifact grep.** Grep the natural home for the concept before proposing a new one:
   | Proposing… | Check first… |
   |---|---|
   | A new course / subject dir | `courses/` + `courses/README.md` (the Shidler-code→directory map) |
   | A new project or stage | the subject's `projects/<slug>/` — is it an extension of an existing stage arc? |
   | A new template | `docs/templates/` + the project's `_templates/` |
   | A new spreadsheet | `docs/spreadsheets/` (the master workbooks) before building a one-off |
   | A new decision pattern | `docs/decisions/` + `_archive/` for a prior/superseding memo |
   | A grading rule | the `feedback_*` memories + `scripts/grading/` |
2. **Archive check.** Grep `_archive/<course-code>/` — the concept may be a *retired* artifact, not a missing one (e.g. the archived BUS-314 project superseded by the shared `performance-ratios` project).
3. **Extend-vs-create.** If an adjacent artifact exists, default to **extending** it and say so; only recommend a new artifact if extension would force NULL-pollution or semantic conflation. Prefer the existing template's conventions (CLAUDE.md: "existing template conventions always win").

For each check, document in the grill response: what was searched (show the grep/glob), what was found (or confirmed absent), and whether it changes the recommendation. **If a check surfaces existing infrastructure → redirect the recommendation BEFORE presenting to the human.** Making the human do convergence work is a skill failure.

### When the Convergence Check can be skipped

- Editing an artifact that already exists and is in scope (e.g. re-weighting an existing rubric).
- Pure documentation / link fixes with no new artifact.

Otherwise: don't skip.

## Grading-domain guardrails

When the grill touches grading, force the recommendation through this repo's settled rules — surface the relevant one as a check, not an afterthought:

- **Curves are generosity-only** — `Curved = MAX(raw, floor)`, never lower a raw score (`feedback_grading_curves`).
- **No double-deductions across stages** — don't re-deduct for an issue already flagged in a prior stage; repeat it as a forward-looking tip (`feedback_no_double_deductions`).
- **Score privacy** — score numbers live only in internal `STAGE{N}_GRADES.md` and instructor email, never in PRs/issues/student-facing files (`feedback_score_privacy`).
- **Accounting standards** — don't penalize non-US-GAAP line items; grade on disclosure quality (`feedback_accounting_standards_grading`).
- **Excel** — every calculated cell is a formula; only raw source data is a literal (`feedback_excel_formulas`).

If a proposal violates one, flag it as a P0 in the Auto-Pushback table.

## Crystallization triggers

Propose capturing a decision inline when **any** of these fire:

- The human disambiguates an overloaded term or convention (e.g. "stage" numbering doesn't map v1→v2).
- An edge case forces a definition ("what if a student enhances the provided template?" → `feedback_template_enhancements_welcome`).
- A hard-to-reverse call settles (a restructure, a supersession, a weight change) → propose a `docs/decisions/` memo (hand to `/decision-memo`).

Format the proposed capture, ask for confirmation, then act. Don't write speculatively.

## Exit criteria

Stop grilling and hand back (or to `superpowers:brainstorming`) when:

- All decision branches in the artifact's scope are resolved OR explicitly deferred with rationale.
- The human says "good, let's brainstorm now" / "that's enough" / "ship it."
- Three consecutive questions get "I don't know yet, defer" — the artifact isn't ready for grilling; back off and recommend more upstream research first.

## Quick reference

| Situation | Action |
|---|---|
| User types `/grill-me` or "grill me" | Invoke, read the named artifact, start the core loop |
| Structural recommendation forming | Run the Auto-Pushback Pass (R-table) before presenting |
| "New course/project/stage/template" forming | Run the Repo Convergence Check first |
| Grading decision | Force it through the grading-domain guardrails |
| Hard-to-reverse decision settles | Propose a `docs/decisions/` memo → hand to `/decision-memo` |
| Three "I don't know" in a row | Stop; recommend upstream research |
| Human says "let's brainstorm" | Hand off to `superpowers:brainstorming` |

## Common mistakes

| Mistake | Fix |
|---|---|
| Asking multiple questions at once | One question. Pause. Wait. |
| Skipping the recommended answer | Always include one — the human's job is confirm/redirect, not generate from scratch |
| Skipping the Auto-Pushback Pass on a structural rec | Mandatory. Surface findings in the R-table; silent self-corrections forbidden |
| Recommending a "new X" without the Convergence Check | Mandatory — this repo restructures often; the artifact may already exist or be archived |
| Batching decisions under a "no pause" directive | "No pause" applies to lookups, NOT structural decisions — those always pause |

## References

- Upstream: <https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me>
- Companion: `superpowers:brainstorming` (converge → then expand), `/decision-memo` (capture the settled call).
