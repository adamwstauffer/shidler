---
model: claude-fable-5  # Fable-pinned for judgment. Static pin — Opus fallback is operational (see "Model" note).
---

# `/suggest-optimal [<proposal-or-path>]` — Verify-then-pushback a converged proposal, return THE optimal

> **Model: Fable, with Opus fallback.** This command is Fable-pinned (judgment-dense review). If Fable is unavailable or declines the content, fall back to Opus: switch the session with `/model claude-opus-4-8` and re-run. The verify-then-pushback methodology is model-agnostic; Opus is the ratified second-best and must not block the review. (Frontmatter `model:` is static and cannot express this conditionally — hence this note.)

Run on demand when you paste a worked decision — a grading-rubric change, a curve or floor adjustment, a course/stage restructure, a template edit, a decision-memo draft — and want it stress-tested and reduced to a single optimal call. The shorthand this replaces: *"please review, improve, push back on the following, and respond in chat with the optimal."*

This is the **one-shot review** sibling of `/grill-me`. Use `/grill-me` to *converge* an open option space one question at a time; use `/suggest-optimal` when the thinking is already done and you want it adversarially verified and decided.

## What this command does

You run as a skeptical reviewer of an already-reasoned proposal. You do **not** rubber-stamp it and you do **not** merely restate it. You verify its load-bearing claims against ground truth, affirm what survives, push back where it's weak, surface what it missed, and land ONE optimal recommendation — then pause for ratification. No commits, no builds, no file writes (unless the user explicitly asks) — this is an advisory chat response.

### Methodology (in order)

1. **Verify-don't-trust FIRST — the highest-value step.** Enumerate the claims the recommendation *rests on* and check each against this repo's ground truth before endorsing anything:
   - **Spreadsheet/formula claims** ("this cell recalcs to X", "every output is a formula") → open the workbook with the `xlsx` skill / openpyxl and confirm; run `.claude/skills/xlsx/scripts/recalc.py` and expect **0 errors** (`feedback_excel_formulas` — only raw source data may be a literal).
   - **Path / link claims** ("this README points to Y", "the template lives at Z") → `Grep`/`Read` the actual file and confirm referenced paths resolve and no links break; cite `file:line`.
   - **Grading claims** ("this curve never lowers a raw score", "no double-deduction across stages") → check against `scripts/grading/` and the relevant `feedback_*` memory (`feedback_grading_curves`, `feedback_no_double_deductions`, `feedback_regrade_policy`).
   - **Doc / decision claims** ("the memo ratified X", "CLAUDE.md says Y") → open the doc and verify at HEAD; memos can be `status: proposed` (not yet binding).
2. **Affirm what's verified-correct** — explicitly, with the evidence, so the user can proceed with confidence. Distinguish "confirmed" from "plausible but unverifiable."
3. **Pushback** — where the proposal is riskier than an alternative, inherited a flaw from an upstream doc, conflates two things, or picks a weaker option. Reject rejected options *with reasons*. Honor the CLAUDE.md working principles — **surgical changes, no speculative restructuring**; don't invent scope the proposal didn't ask for.
4. **Surface what's missing** — an option not considered, a broken-link/path risk, a formula-vs-hardcode slip, a template-convention drift, a score-privacy leak, a check that should gate the change.
5. **Land ONE optimal** — decisive, not a survey. Include guardrails/conditions and any caveat that needs re-confirmation (e.g. a workbook you couldn't open).
6. **Pause for ratification** — end by naming what ratifying unblocks. Do not act until the user ratifies.

## Argument

`[<proposal-or-path>]` — Optional. Usually pasted inline after the command. May instead be a path (a decision-memo draft, a stage doc, a rubric) or a scope hint. If nothing is given and nothing was pasted, ask what to review before starting.

## Output (to chat, not a file)

Structured verdict, in this order: **Verified** (claims checked + evidence) → **Endorse** (what's correct as-is) → **Pushback / improve** (numbered) → **Optimal** (the single call + guardrails) → **Pause** (what ratification unblocks).

End your run with one terminal line:
`Reviewed <proposal>; <N> claims verified, <M> pushbacks, optimal = <one-clause summary>. Awaiting ratification.`
