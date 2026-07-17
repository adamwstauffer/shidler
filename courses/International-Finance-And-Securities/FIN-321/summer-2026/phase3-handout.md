# Phase 3 — AI-Assisted Build + Audit

**FIN 321 · International Business Finance · Summer 2026 (Sec. 701)**

| | |
|---|---|
| **Points** | **3.4 / 20** (17% of the project) |
| **Due** | **Friday, July 31, 2026 · 11:59 PM HST** |
| **Full instructions** | <https://adamwstauffer.github.io/ai-lms/fx-hedging-stage3.html> |
| **Submit** | Commit & push the workbook + audit note + prompt log; submit links via Lamaku |

## Goal

Generate a working workbook **from your own Phase 2 specification** — using any AI tool or by
hand — and **audit the result**. Your graded skill here is not typing formulas; it is
**specifying precisely and auditing ruthlessly**. There is no starter template — your spec *is*
the template.

## The build contract (verifiable by inspection and by the grading script)

1. **All ten named ranges** attached to the right cells (`FC_AMT`, `S0_in`, `F0_in`, `R_USD`,
   `R_FC`, `K_PUT`, `K_CALL`, `PREM_PUT`, `PREM_CALL`, `T_DAYS`).
2. **Formulas, never hard-coded values.** Every calculated cell is a formula referencing named
   ranges — a pasted number where a formula belongs scores **zero** for that element (checked
   mechanically).
3. **Cover page** — scenario, author, date, data-provenance block (placeholders noted as indicative).
4. **Legend/Key tab** — color convention applied throughout: Yellow = inputs · Blue =
   assumptions · Green = formulas · Gray = outputs.
5. **All three hedge families** — forward; money market in three explicit steps; put and call
   with premium in USD and proceeds as a function of `S_T`.
6. **Sensitivity table + chart** — ±5% in 1% steps, formula-driven (no hand-typed rows).
7. **Validation checks live in the workbook** — parity check and any other check figures from
   your spec §7, computed, visible, and passing.

**Tool guidance:** use whatever produces the best result (Claude for Excel, Claude/ChatGPT on
the web with your spec pasted or linked, Copilot in Excel, or a manual build). Your spec goes in
**as-is** — if you're re-explaining the model in chat, that's a spec defect: fix the spec, commit,
regenerate. Log every prompt in `prompt-log.md`.

## The audit note (required)

Audit the generated workbook against your spec's validation rules and document **≥3 findings** —
things you checked and confirmed, or found broken and fixed. For each: what you checked, what you
found, what you did. "Everything was perfect" is a red flag, not a good sign.

## Deliverables

- Workbook: `models/builds/YYYY-MM-DD-{lastname}-{scenario-slug}-model.xlsx`
- Audit note: `analysis/YYYY-MM-DD-{lastname}-build-audit.md` (≥3 findings)
- Updated `prompt-log.md`. Commit incrementally — generation, then each audit fix.

## Rubric

| Criterion | Weight | Description |
|---|--:|---|
| Contract compliance | 50% | Named ranges complete/correct; formulas-only (mechanically checked); all hedges + sensitivity present and computing |
| Structure & presentation | 25% | Cover, legend/key, color convention, auditable layout |
| Audit note | 25% | ≥3 substantive findings with evidence; fixes committed |

## Links

- Full instructions (website): <https://adamwstauffer.github.io/ai-lms/fx-hedging-stage3.html>
- Canonical stage doc: [`../../projects/fx-hedging/stage3-ai-build-audit.md`](../../projects/fx-hedging/stage3-ai-build-audit.md)
