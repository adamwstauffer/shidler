# Phase 2 — Model Specification

**FIN 321 · International Business Finance · Summer 2026 (Sec. 701)**

| | |
|---|---|
| **Points** | **4.2 / 20** (21% of the project) |
| **Due** | **Friday, July 31, 2026 · 11:59 PM HST** |
| **Full instructions** | <https://adamwstauffer.github.io/ai-lms/fx-hedging-stage2.html> |
| **Submit** | Commit & push the spec + prompt log; submit the file link via Lamaku |

## Goal

Using [`_templates/template-spec.md`](../../projects/fx-hedging/_templates/template-spec.md),
write a **2–3 page technical specification** for your FX hedging workbook — **before any Excel
exists**. It must be precise enough that an AI (or a colleague who never saw your memo) could
build the complete workbook from this document alone. In Phase 3, that is literally what happens:
**the spec is the prompt.**

Use your assigned scenario's parameters as **placeholder inputs**, clearly flagged as
*"indicative — replaced with live market data at Phase 4."*

## What to include

1. **Problem statement** — exposure, timing, risk, business consequence (currency, amount, date).
2. **Inputs (named-range contract)** — every input with name, placeholder value, unit, and
   Phase-4 data source. Use the standard names exactly: `FC_AMT`, `S0_in`, `F0_in`, `R_USD`,
   `R_FC`, `K_PUT`, `K_CALL`, `PREM_PUT`, `PREM_CALL`, `T_DAYS`.
3. **Tab architecture** — name every tab and its purpose (Cover, Legend/Key, Inputs, one area
   per hedge, Sensitivity, Notes & Assumptions).
4. **Assumptions & constraints** — rate basis (e.g., ACT/360), transaction costs, parity
   expectation, premium treatment.
5. **Calculation flow** — logic in named-range notation (never cell addresses) for forward,
   money-market (3 steps + parity check), and options (premium + payoff vs. ending spot `S_T`).
6. **Sensitivity plan** — `S_T` from 0.95×`S0_in` to 1.05×`S0_in` in 1% steps; one comparison chart.
7. **Validation rules (check figures)** — forward ≈ MM parity, continuous option proceeds,
   no error cells, every output a formula. These become your Phase 3 audit checklist.
8. **Outputs** — name each summary result and table exactly.

**LLM as drafter, you as editor.** Draft with an AI, then correct it. Log prompts in
`prompt-log.md` and show **at least one specific iteration** (a gap you found and how you fixed it).

## Deliverable

- File: `docs/specs/YYYY-MM-DD-{lastname}-{scenario-slug}-spec.md`
- Plus updated `prompt-log.md`. Committed and pushed.

## Rubric

| Criterion | Weight | Description |
|---|--:|---|
| Named-range contract & tab architecture | 30% | Complete inputs table w/ units, placeholders, Phase-4 sources; every tab named with purpose |
| Calculation flow | 30% | Correct, correctly ordered logic for all three hedge families in named-range notation |
| Validation & sensitivity plan | 20% | Concrete check figures; sensitivity design fully specified |
| Reproducibility & prompt log | 20% | Buildable by a context-free reader; human-in-the-loop iteration evidenced |

## Links

- Full instructions (website): <https://adamwstauffer.github.io/ai-lms/fx-hedging-stage2.html>
- Canonical stage doc: [`../../projects/fx-hedging/stage2-model-spec.md`](../../projects/fx-hedging/stage2-model-spec.md)
- Spec template: [`../../projects/fx-hedging/_templates/template-spec.md`](../../projects/fx-hedging/_templates/template-spec.md)
