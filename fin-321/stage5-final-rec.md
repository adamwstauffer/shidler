# Stage 5 – Final FX Hedge Analysis & Recommendation

**Created by:** Kimberly McMoore  
**Date:** December 12, 2025  
**Version:** 1.0  

---

## A. Exposure Summary
Our firm expects to receive a **€12,500,000** payment in **1 year**. This foreign-currency receivable exposes us to **EUR/USD exchange rate fluctuations**, which could significantly affect the USD cash flows. A depreciation of the EUR relative to the USD would reduce the USD proceeds, while an appreciation could increase proceeds. Effective hedging is therefore crucial to protect cash flow certainty and support financial planning.

---

## B. Summary of Hedge Outcomes

| Hedge Type       | USD Proceeds (Base Case, S₀) | Notes                                    |
|-----------------|------------------------------|-----------------------------------------|
| Unhedged        | 13,625,000                   | Fully exposed to FX risk                 |
| Forward         | 13,637,500                   | Locked-in USD, certainty, parity with MM|
| Money Market    | 13,889,563                   | Synthetic forward, validates parity logic|
| Put Option      | 13,412,500                   | Protects downside below strike, limited upside |
| Call Option     | 13,350,000                   | Upside participation above strike, premium paid |

- Forward and Money Market hedges provide **certainty in USD cash flows**.  
- Option hedges offer **flexibility**: puts protect against EUR depreciation, calls allow upside participation but require premium payment.  

---

## C. Sensitivity Interpretation
- **EUR Depreciation:**  
  - Put option mitigates downside; forward/MM lock in value and fully avoid losses.  
- **EUR Appreciation:**  
  - Call option allows upside, but forward/MM limit gains to fixed amounts.  
  - Unhedged exposure captures full appreciation but carries full downside risk.  

**Insight:** Forward and MM hedges provide stability; options introduce optionality at a cost.

---

## D. Strategic Recommendation
**Recommended Hedge: Forward Hedge**  
- Locks in USD proceeds at **$13,637,500**, ensuring **budget certainty** and **cash flow stability**.  
- Validated by money market hedge parity.  
- Avoids premium costs and complexity of options.  
- Supports treasury and operational planning without speculative risk.

**Alternative Consideration:** A **put option overlay** could be considered if slight downside protection beyond the forward is desired, but at the expense of paying the premium.

---

## E. Executive Justification
- **Cash Flow Stability:** Forward hedge guarantees USD proceeds, reducing volatility in financial statements.  
- **Budget Certainty:** Facilitates operational and capital planning.  
- **Liquidity:** No upfront premiums required (unlike options).  
- **Optionality:** Forward hedge foregoes upside potential, but this is acceptable given risk-averse treasury policy.  
- **Accounting Implications:** Straightforward hedge accounting; simple documentation for audit purposes.

---

## Extra Credit – Areas for Further Study

### 1. Claude Skills (Automation & Live Data)
- Pull live EUR/USD rates and interest rates.  
- Auto-update model and regenerate sensitivity tables.  
- Reduce manual errors and speed reporting.

### 2. OpenAI Codex / Code Interpreter
- Convert Stage 3 pseudocode into a Python-based model.  
- Automate large-scale scenario testing (Monte Carlo).  
- Ensure formula correctness and reproducibility.

### 3. GitHub Automation & Version Control
- Track versions of specs, prompts, and spreadsheet templates.  
- Branching and pull requests allow parallel model development.  
- Enables audit trails and rollback of changes, supporting internal controls.

---

**Conclusion:** The forward hedge is the recommended strategy for protecting USD cash flows, balancing certainty, risk, and operational simplicity. Combined with GitHub-based version control and optional automation via AI, this approach is robust, auditable, and executive-ready.
