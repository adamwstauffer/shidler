# Stage 5 – LLM Analysis & Validation (25% of project — capstone)

## Goal

The capstone. Feed your Stage 2 spec and Stage 4 market-data memo — **and nothing else** — to a
fresh LLM session and have it produce the complete hedge analysis independently. Then do what a
professional does with any model output, human or machine: **verify it by hand, reconcile the
differences, and only then make the recommendation.** Finish by polishing the repo into the
portfolio piece it's been becoming all term.

---

## Part 1 — Independent LLM execution

Open a **fresh** LLM conversation (no history). Provide exactly two documents: your spec and
your market-data memo (GitHub links or file uploads). Ask it to compute all hedge outcomes and
recommend a strategy. Do not coach it, correct it mid-run, or paste your workbook results — this
is a production test of your documents. Log the prompt.

## Part 2 — Comparison & hand verification

1. **Comparison table** — LLM's result vs. your workbook's result for each strategy (forward,
   MM, put, call, unhedged at 2–3 `S_T` points). Flag every discrepancy and diagnose it: LLM
   error, workbook error, or spec ambiguity?
2. **Hand-verification table (≥3 outcomes, arithmetic shown).** Recompute by hand — calculator
   and named-range notation, no Excel:
   - forward proceeds (`FC_AMT × F0_in`),
   - the money-market hedge, all three steps,
   - one option outcome (e.g., put floor net of premium at a chosen `S_T`).
   Show the numbers at each step. This table is the single strongest evidence in the project
   that you understand the model.

## Part 3 — Executive recommendation memo

2–4 pages, to the CFO, insight over computation:

- **A. Exposure summary** — brief restatement.
- **B. Hedge outcomes** — key findings per strategy, including unhedged baseline.
- **C. Sensitivity interpretation** — behavior under EUR depreciation/appreciation; certainty
  vs. flexibility vs. cost.
- **D. Recommendation** — one strategy (or combination), supported by *your live-data* numbers.
- **E. Executive justification** — cash-flow stability, budget certainty, liquidity, optionality,
  premium cost; accounting implications optional.

## Part 4 — Spec retrospective & repo polish

- **Retrospective (½–1 page, in the validation doc):** what did the LLM get wrong or have to
  guess, and what does that reveal about your spec? What would v2 of the spec say differently?
  Candor is graded; "the spec was perfect" is not a retrospective.
- **Repo polish checklist:** top-level README current (bio + a project section linking every
  stage artifact), one-line repo description set, all files in canonical locations with
  convention-compliant names, stub READMEs still accurate, `prompt-log.md` complete through
  stage 5, clean commit history, repo public.

## Deliverables

- Validation doc (Parts 1–2 + retrospective):
  `analysis/YYYY-MM-DD-{lastname}-{scenario-slug}-validation.md` — include the raw LLM output
  as an appendix or linked file.
- Recommendation memo (Part 3):
  `docs/decisions/YYYY-MM-DD-{lastname}-{scenario-slug}-hedge-recommendation.md`
- Polished repo + final `prompt-log.md`.

## Evaluation

| Criterion | Description | Weight |
| --------- | ----------- | -----: |
| LLM execution & comparison | Clean two-document run; complete comparison table; discrepancies diagnosed, not just listed | 25% |
| Hand verification | ≥3 outcomes recomputed with arithmetic shown; reconciled to the workbook | 25% |
| Recommendation & executive voice | Data-supported, decision-ready, CFO-appropriate | 25% |
| Spec retrospective | Specific, honest, ties LLM failures to spec gaps | 17% |
| Repo polish | Checklist complete; repo is genuinely portfolio-ready | 8% |

## Further study (optional — not graded)

Optional enrichment, no points attached. In 1–2 paragraphs each, discuss **2–3** of: AI skills & automation (live data pulls, on-demand
regeneration, Monte Carlo); multi-file reasoning across spec/model/log; GitHub as audit
evidence and reproducibility infrastructure; hedge-accounting integration (OCI vs. P&L,
documentation requirements). Tie each to *your* project, not the abstract idea.

---

## Why this matters

You specified a model, had an AI build it, audited the build, loaded live data, validated the
whole chain by hand, and shipped an executive recommendation — version-controlled end to end.
That is the analyst-to-automation workflow as it actually runs in treasury, banking, FP&A, and
audit. The repository you just polished is the proof.
