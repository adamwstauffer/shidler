# FX Hedging Decision Memo – EUR Receivable Exposure

**Created by:** Adam W. Stauffer
**Updated by:** Adam W. Stauffer
**Date Created:** 2026-03-25
**Date Updated:** 2026-03-25
**Version:** 1.0
**LLM Used:** Claude Opus 4.6

---

## Executive Summary (≤150 words)

Our pharmaceutical export division expects to receive EUR 8,000,000,000 from a European distributor in one year. At today's spot rate, this receivable converts to approximately $8.7 billion in USD proceeds — but that figure is entirely dependent on where EURUSD trades at maturity. A 5% depreciation of the euro would reduce our USD proceeds by roughly $435 million, directly impacting operating margins on an already-negotiated contract. This memo outlines the exposure, explains why it warrants active risk management, and introduces three hedging strategies — forward contracts, currency options, and a money market hedge — for the CFO's consideration. Subsequent stages will build a quantitative model, document the methodology, and deliver a final recommendation on the optimal hedge.

---

## Background & Objectives

Our firm has contracted to supply pharmaceutical products to a European distributor with payment of EUR 8,000,000,000 due in 12 months. Because our cost base is denominated in USD, any weakening of the euro against the dollar between now and the payment date directly erodes profit margins. Recent EURUSD volatility — driven by diverging Fed and ECB monetary policy, geopolitical uncertainty, and shifting trade dynamics — makes this exposure material.

**Primary objective:** Protect the USD value of the EUR 8B receivable against adverse currency movements.
**Secondary objective:** Preserve upside participation if the euro appreciates, where cost-effective.

---

## Methods

Three hedging families will be evaluated in Stages 2–4:

| Strategy | Mechanism | Pros | Cons |
|----------|-----------|------|------|
| **Forward Contract** | Lock in a sale of EUR 8B at the 1-year forward rate of 1.0890 | Eliminates uncertainty; no upfront cost; simple execution | Sacrifices all upside if EUR appreciates beyond 1.0890 |
| **Currency Options** | Purchase a EUR put option (strike at-the-money, premium ~$0.021/EUR) to set a floor on USD proceeds | Preserves upside; defines a worst-case floor | Premium cost (~$168 million on notional) reduces net proceeds |
| **Money Market Hedge** | Borrow EUR today at the EUR interest rate, convert to USD at spot, invest at the USD rate; repay EUR loan with the receivable | Locks in an effective rate using existing credit facilities; no derivative required | Ties up balance sheet capacity; effective rate depends on interest rate differential |

Each strategy will be modeled across a range of EURUSD outcomes (0.95–1.20) to compare net USD proceeds, breakeven points, and risk-adjusted returns.

---

## Limitations & Next Steps

**Limitations:** Option premiums and forward rates are indicative and will be confirmed with market data at Stage 2 initiation. Interest rates for the money market hedge are TBD based on current SOFR and EURIBOR benchmarks. Transaction costs, credit risk, and basis risk are not yet modeled.

**Next Steps:**

1. **Excel Model Build (Stage 2):** Construct a working spreadsheet that computes and compares hedge outcomes for all three strategies across multiple EURUSD scenarios.
2. **Technical Specification (Stage 3):** Document the model's architecture, assumptions, and formulas — precise enough for an AI or analyst to reconstruct independently.
3. **Final Analysis & Recommendation (Stage 4):** Select the optimal hedge strategy using model results, draft a structured AI prompt for sensitivity analysis, and present the final recommendation to the CFO.

---

## References

- EURUSD spot and forward rates: to be sourced from Bloomberg/Yahoo Finance at Stage 2 initiation.
- Hull, J.C. *Options, Futures, and Other Derivatives*, 11th ed. Pearson.
- Eun, C.S. & Resnick, B.G. *International Financial Management*, 9th ed. McGraw-Hill.
