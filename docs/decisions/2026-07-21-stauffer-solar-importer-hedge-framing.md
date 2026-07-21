# FX Exposure Framing: EUR Receivable Hedge Strategy for U.S. Solar Equipment Importer

**Created by:** Adam W. Stauffer  
**Updated by:** Adam W. Stauffer  
**Date Created:** 2026-07-21  
**Date Updated:** 2026-07-21  
**Version:** 1.0  
**LLM Used:** None

---

## Executive Summary (≤150 words)

Our firm — a U.S.-based solar equipment importer — expects to collect **€4,500,000** from a European counterparty in approximately one year. At today's EURUSD spot rate, that receivable converts to roughly $4,894,650 USD; however, if the euro weakens materially before settlement, our realized USD proceeds could fall well short of that figure. This memo frames the currency risk, introduces three hedging families that can protect the position, and outlines the analytical work planned for Stages 2–5. The recommended path is to evaluate all three strategies — a forward contract, a money-market hedge, and a EUR put option — against the 1-year forward rate of **1.0875** before committing to a single approach. No capital is deployed until the Stage 5 recommendation is ratified by leadership.

---

## Background & Objectives

**Exposure.** As a U.S.-domiciled importer selling solar equipment to European distributors, we invoice in EUR. The receivable of **€4,500,000** is due in one year (settlement date: approximately 2027-07-21). Our functional currency is USD; until that EUR is converted, we bear full EURUSD translation risk.

**Risk.** If EURUSD depreciates from the current spot toward, say, 1.00, our USD realization drops by roughly $390,000 relative to today's spot-implied value — a meaningful impact on operating cash flow and FY-27 budget assumptions. Conversely, euro appreciation is upside we may choose to preserve through an options-based strategy.

**Objectives.**
1. Quantify the worst-case and base-case USD outcomes under the three hedge families.
2. Select the hedge that best balances cost, downside protection, and upside optionality.
3. Document the methodology rigorously so the decision is reproducible and auditable.

---

## Methods

Three hedge families will be modeled side-by-side:

| Hedge | Mechanism | Pro | Con |
|-------|-----------|-----|-----|
| **Forward Contract** | Lock in the 1-year forward rate of **1.0875** today | Certainty; zero premium | Gives up any euro appreciation; counterparty credit risk |
| **Money-Market Hedge** | Borrow EUR today, convert to USD, invest at USD rate; repay with receivable | Mirrors forward economics; uses balance-sheet levers | Requires credit facility; ties up borrowing capacity |
| **EUR Put Option** | Buy a put (K ≈ spot, premium $0.015/contract) giving the right to sell EUR at strike | Retains upside if EUR strengthens | Upfront premium cost; requires option market access |

**Data inputs to be sourced at Stage 2 start (market close, date of work):**
- EURUSD spot rate (Bloomberg / Yahoo Finance; record date and source)
- 1-year USD risk-free rate (U.S. Treasury)
- 1-year EUR risk-free rate (ECB benchmark or EURIBOR equivalent)
- Put and call premiums as given: $0.015 and $0.018 per contract (no multiplier)
- 1-year forward rate (given): **1.0875**

The quantitative model will be built in Excel (Stage 3) from a formal specification (Stage 2), populated with live market data (Stage 4), and validated via an independent LLM run before a final recommendation is issued (Stage 5).

---

## Limitations & Next Steps

**Limitations.**
- Interest rates and spot FX are placeholders until Stage 2 market-data pull; all Stage 1 figures are illustrative.
- The scenario provides a single forward rate (1.0875) rather than a full yield curve; basis risk from curve shape is not modeled.
- Option premiums are simplified (no multiplier, single strike); real-market premiums and Greeks will differ.
- Credit quality of the European counterparty and settlement risk are outside scope.

**Next Steps.**

| Stage | Deliverable | Responsible |
|-------|-------------|-------------|
| **Stage 2 – Model Specification** | Design the Excel workbook: named input ranges (`BAL_`, `INC_`, `CASH_`, `RATIO_` conventions), calculation flow, and output tables for all three hedge payoffs | Adam W. Stauffer |
| **Stage 3 – AI-Assisted Build** | Generate workbook from spec using LLM assistance; audit every formula for accuracy | Adam W. Stauffer |
| **Stage 4 – Market Data Population** | Pull live EURUSD spot, USD/EUR rates; populate model and confirm hedge payoffs reconcile | Adam W. Stauffer |
| **Stage 5 – Validation & Recommendation** | Run independent LLM validation; deliver final hedge recommendation with sensitivity analysis | Adam W. Stauffer |

CFO approval is requested to proceed to Stage 2.

---

## References

- Scenarios file: `courses/International-Finance-And-Securities/projects/fx-hedging/scenarios.md`
- FX Hedging Project overview: `courses/International-Finance-And-Securities/projects/fx-hedging/README.md`
- 1-year EURUSD forward rate (given): 1.0875
- EUR put premium (given): $0.015/contract; EUR call premium (given): $0.018/contract
- EURUSD spot and interest rates: to be recorded from Bloomberg / Yahoo Finance at Stage 2 market-data pull
