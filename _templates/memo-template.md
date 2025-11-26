# [Memo Title]
**Created by:** Kimberly McMoore 
**Updated by:**  Kimberly McMoore
**Date Created:**  October 24
**Date Updated:**  November 13
**Version:**  1


---
## Executive Summary (≤150 words)
Our firm at U.S. Tech Services expects to receive €12,500,000 on October 24, 2026 from our European client. Because we report in USD, exchange rate volatility could affect how much we ultimately receive, and so the final value of this receivable will depend on the EURUSD exchange rate at settlement. If the euro depreciates, our USD proceeds could fall significantly.

This memo outlines our FX exposure, explains why hedging should be considered, and evaluates three hedging strategies: a forward contract, a money-market hedge, and options. Each approach provides different levels of protection, cost, and flexibility. Finally, this memo concludes with the next steps, including how we will build a spreadsheet model to quantify USD outcomes under each hedge and determine the optimal risk-management approach.

---
## Background
We are scheduled to receive €12.5 million in one year, and the final amount we recognize in USD will depend on the EURUSD exchange rate at that time. If the euro weakens, our revenue will decline. The current 1-year forward rate of 1.0910 gives us a baseline, but the actual outcome is still uncertain. 

---
## Method (models & assumptions)
Here are our three hedge families relevant to our EUR receivable: a forward contract, a money-market hedge, and EUR options. 

Forward hedge:
- Pros: Locks in a known USD amount at maturity; simple to implement; no upfront payment.
- Cons: Removes any upside benefit if the EUR appreciates.

Money-market hedge:
- Pros: Uses borrowing/lending based on interest rate parity; eliminates FX uncertainty without paying a premium.
- Cons: Requires borrowing or lending in USD and EUR; sensitivity to interest rate assumptions.

Options hedge (EUR put or call depending on structure):
- Pros: Provides downside protection while allowing upside participation if EUR strengthens.
- Cons: Requires paying an option premium (given in the scenario: $0.017 for put, $0.022 for call).

Assumptions include: determining the current EURUSD spot rate to set the strike price; applying market USD and EUR interest rates for the money-market hedge; using one-year compounding; and modeling payoffs under a range of potential EURUSD levels at maturity. These assumptions will be implemented in the spreadsheet model for Stage 2 and expanded in Stage 3.

---
## Findings (figures/tables referenced)
(Spreadsheet in Stages 2–3 will compute:)

- USD proceeds unhedged under various EURUSD scenarios.
- Locked-in USD via forward.
- Synthetic proceeds via money-market hedge.
- Option payoffs net of premium.

---
## Implications (policy/managerial)
Hedging stabilizes USD revenue, improves planning accuracy, and protects against a weakening euro—critical given the scale of the receivable.

---
## Limitations & Next Steps
Next, I will:

1. Pull real-time spot FX and interest rates.
2. Build the Excel model per spec (payoff tables, IRP calculations, scenario analysis).
3. Provide a final hedge recommendation based on expected values and risk tolerance.

---
## References

