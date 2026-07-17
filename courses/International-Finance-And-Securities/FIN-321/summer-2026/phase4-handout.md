# Phase 4 — Market Data + Population

**FIN 321 · International Business Finance · Summer 2026 (Sec. 701)**

| | |
|---|---|
| **Points** | **2.4 / 20** (12% of the project) |
| **Due** | **Friday, August 7, 2026 · 11:59 PM HST** |
| **Full instructions** | <https://adamwstauffer.github.io/ai-lms/fx-hedging-stage4.html> |
| **FX Hedging Lab** | <https://adamwstauffer.github.io/ai-lms/fxlab.html> |
| **Submit** | Commit & push the market-data memo + repopulated workbook; submit links via Lamaku |

## Goal

Replace your placeholder inputs with **live market data**, document exactly where every number
came from, and confirm the model survives contact with reality. Because everyone retrieves data
on their own date, **every student's numbers are unique** — and that's intended.

## Retrieve (as of market close on the day you begin this phase)

- `S0_in` — EURUSD spot (Yahoo Finance, ECB reference rate, Bloomberg, etc.). Record source + timestamp.
- `R_USD`, `R_FC` — 1-year interest rates (a government yield or deposit/reference rate per
  currency). **Document which rate you chose and why** — the choice matters more than the decimals.
- `F0_in` — 1-year forward: a live quote if you can find one, otherwise **compute the CIP-implied
  forward** `F0 = S0 × (1 + R_USD×T/360) / (1 + R_FC×T/360)` and say so. Compare to your scenario's
  indicative forward and comment on the gap.
- `K_PUT`, `K_CALL` — strikes at/near your live spot, per the scenario convention.
- `PREM_PUT`, `PREM_CALL` — keep the scenario-given premiums (note this as an assumption).
- `FC_AMT`, `T_DAYS` — from your scenario.

## Then

1. **Write the market-data memo** — `data/YYYY-MM-DD-{lastname}-market-data.md`: a table of every
   input with value, source, retrieval timestamp, and any proxy/computation. An auditor should be
   able to re-pull every number.
2. **Populate the workbook** — enter live values into the named-range input cells; nothing else
   should need to change. If a formula breaks, the structure was wrong — fix it and record what
   you fixed (finding it *is* the exercise, not a penalty).
3. **Re-run the checks** — parity check passes with live data; sensitivity table and chart
   recalculate around the new spot.
4. **Cross-check against the FX Hedging Lab** — enter your live inputs into the lab and compare
   its forward / money-market / option outputs to your workbook. If they disagree, find out which
   is wrong before submitting and record the resolution in the memo.

## Deliverables

- Market-data memo: `data/YYYY-MM-DD-{lastname}-market-data.md`
- Re-committed workbook (same file, new commit noting the population + any structural fixes)
- Updated `prompt-log.md` if AI assisted the data hunt.

> **Feedback may arrive as a pull request** from here on — a proposed change shown as a
> line-by-line diff. Read it, merge it, edit on top, hand it to an LLM, or **push back with
> reasons**. Reasoned disagreement is a professional skill and is explicitly welcome.

## Rubric

| Criterion | Weight | Description |
|---|--:|---|
| Data quality & provenance | 50% | Every input sourced, timestamped, proxies documented; sensible rate choices |
| Model resolves cleanly | 33% | Live data loads through named ranges; checks pass; fixes documented honestly |
| Lab cross-check | 17% | Comparison performed and documented; discrepancies resolved |

## Links

- Full instructions (website): <https://adamwstauffer.github.io/ai-lms/fx-hedging-stage4.html>
- FX Hedging Lab: <https://adamwstauffer.github.io/ai-lms/fxlab.html>
- Canonical stage doc: [`../../projects/fx-hedging/stage4-market-data-population.md`](../../projects/fx-hedging/stage4-market-data-population.md)
