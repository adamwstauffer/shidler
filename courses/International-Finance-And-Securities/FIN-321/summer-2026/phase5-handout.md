# Phase 5 — LLM Analysis & Validation (Capstone)

**FIN 321 · International Business Finance · Summer 2026 (Sec. 701)**

| | |
|---|---|
| **Points** | **5.0 / 20** (25% of the project) |
| **Due** | **Friday, August 14, 2026 · 11:59 PM HST** |
| **Full instructions** | <https://adamwstauffer.github.io/ai-lms/fx-hedging-stage5.html> |
| **Submit** | Commit & push the validation doc + recommendation memo + polished repo; submit links via Lamaku |

## Goal

The capstone. Feed your **Phase 2 spec and Phase 4 market-data memo — and nothing else** — to a
**fresh** LLM session and have it produce the complete hedge analysis independently. Then do what
a professional does with any model output: **verify it by hand, reconcile the differences, and
only then make the recommendation.** Finish by polishing the repo into a portfolio piece.

## Part 1 — Independent LLM execution

Open a fresh LLM conversation (no history). Provide exactly two documents: your spec and your
market-data memo (GitHub links or uploads). Ask it to compute all hedge outcomes and recommend a
strategy. **Do not coach it, correct it mid-run, or paste your workbook results** — this is a
production test of your documents. Log the prompt.

## Part 2 — Comparison & hand verification

1. **Comparison table** — LLM result vs. your workbook for each strategy (forward, MM, put, call,
   unhedged) at 2–3 `S_T` points. Flag every discrepancy and diagnose it: LLM error, workbook
   error, or spec ambiguity?
2. **Hand-verification table (≥3 outcomes, arithmetic shown)** — recompute by hand (calculator +
   named-range notation, no Excel): forward proceeds, the money-market hedge (all three steps),
   and one option outcome. Show the numbers at each step. This is the strongest evidence that you
   understand the model.

## Part 3 — Executive recommendation memo (2–4 pages, to the CFO)

- **A. Exposure summary** — brief restatement.
- **B. Hedge outcomes** — key findings per strategy, including the unhedged baseline.
- **C. Sensitivity interpretation** — behavior under EUR depreciation/appreciation; certainty vs.
  flexibility vs. cost.
- **D. Recommendation** — one strategy (or combination), supported by *your live-data* numbers.
- **E. Executive justification** — cash-flow stability, budget certainty, liquidity, optionality,
  premium cost.

## Part 4 — Spec retrospective & repo polish

- **Retrospective (½–1 page):** what did the LLM get wrong or have to guess, and what does that
  reveal about your spec? What would v2 say differently? "The spec was perfect" is not a retrospective.
- **Repo polish:** top-level README current (bio + a project section linking every stage
  artifact), repo description set, canonical file locations/names, stub READMEs accurate,
  `prompt-log.md` complete through Phase 5, clean commit history, repo public.

## Deliverables

- Validation doc (Parts 1–2 + retrospective):
  `analysis/YYYY-MM-DD-{lastname}-{scenario-slug}-validation.md` (include raw LLM output as an appendix/linked file)
- Recommendation memo (Part 3):
  `docs/decisions/YYYY-MM-DD-{lastname}-{scenario-slug}-hedge-recommendation.md`
- Polished repo + final `prompt-log.md`.

## Rubric

| Criterion | Weight | Description |
|---|--:|---|
| LLM execution & comparison | 25% | Clean two-document run; complete comparison table; discrepancies diagnosed |
| Hand verification | 25% | ≥3 outcomes recomputed with arithmetic shown; reconciled to the workbook |
| Recommendation & executive voice | 25% | Data-supported, decision-ready, CFO-appropriate |
| Spec retrospective | 17% | Specific, honest, ties LLM failures to spec gaps |
| Repo polish | 8% | Checklist complete; repo is genuinely portfolio-ready |

*Optional (not graded): a short "further study" note — see the canonical stage doc.*

## Links

- Full instructions (website): <https://adamwstauffer.github.io/ai-lms/fx-hedging-stage5.html>
- Canonical stage doc: [`../../projects/fx-hedging/stage5-llm-analysis-validation.md`](../../projects/fx-hedging/stage5-llm-analysis-validation.md)
