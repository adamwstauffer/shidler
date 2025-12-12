# EUR Receivable Hedge Model – Technical Specification

**Created by:** Kimberly McMoore  
**Updated by:** Kimberly McMoore  
**Date Created:** November 7  
**Date Updated:** November 7  
**Version:** 1

**Role:** Financial Analyst / Treasury Analyst  
**Audience:** CFO or Director of Treasury  

**Purpose:** Provide a complete, quantitative specification describing how the FX hedging model will be structured, the inputs required, the assumptions applied, and the sequence of calculations for evaluating hedging alternatives for our EUR receivable.

---

## 1. Problem Statement

Our firm, a U.S.-based technology services company, expects to receive €12,500,000 in 12 months from a European customer. Because our financial reporting currency is USD, the USD value of this receivable is exposed to changes in the EURUSD exchange rate over the next year. A depreciation of the euro would reduce the dollar value of the inflow, directly impacting revenue recognition, project profitability, and cash-flow planning.

The objective of this analysis is to design a replicable quantitative framework for evaluating three FX hedging strategies—forward contracts, money-market hedges, and EUR options. This specification provides the analytical structure a treasury analyst or AI assistant can use to build the Stage 3 Excel model and support a data-driven hedge recommendation for management.

---

## 2. Inputs (Known Variables)

| Variable | Description | Unit | Example | Source |
|---------|-------------|-------|---------|--------|
| **FC_AMT** | EUR receivable amount | EUR | 12,500,000 | Internal |
| **S₀** | Current EURUSD spot rate | USD per EUR | [lookup] | Market (Yahoo Finance, Bloomberg) |
| **F₀** | 1-year EURUSD forward rate | USD per EUR | 1.0910 | Provided |
| **r_USD** | USD 1-year interest rate | % | [lookup] | Market |
| **r_EUR** | EUR 1-year interest rate | % | [lookup] | Market |
| **t** | Time to maturity | Years | 1 | Derived |
| **K_put** | Strike price for EUR put | USD per EUR | = spot | Analyst |
| **K_call** | Strike price for EUR call | USD per EUR | = spot | Analyst |
| **Premium_put** | Premium on EUR put | USD per contract | 0.017 | Scenario |
| **Premium_call** | Premium on EUR call | USD per contract | 0.022 | Scenario |
| **S_T** | Spot at maturity | USD per EUR | Scenario range | Model |

**Note:** Options have **no multiplier** — premiums apply per euro.

---

## 3. Assumptions & Constraints

1. Interest rates are annual and simple.  
2. Exchange rates quoted as USD per EUR (EURUSD).  
3. Option premiums are paid upfront in USD at t = 0.  
4. Strike prices (K) are set equal to the current FX spot rate.  
5. Receivable is certain and paid exactly at 1-year maturity.  
6. No counterparty credit risk included.  
7. No transaction costs, spreads, or margin requirements.  
8. Money market hedge follows interest rate parity logic.  
9. All payoffs are linear with no exotic features.  
10. Units and sign conventions remain consistent across hedges.

These assumptions allow the model to remain transparent, reproducible, and aligned with standard classroom hedging frameworks.

---

## 4. Calculation Flow

This section outlines the exact sequence the Excel model will follow.

### **Step 1 — Initialize Inputs**  
Load all variables: FC_AMT, S₀, F₀, r_USD, r_EUR, option strikes, and premiums.

### **Step 2 — Unhedged USD Exposure**  
1. Compute USD proceeds at maturity:  
   **USD_unhedged = FC_AMT × S_T**  
2. This is the baseline scenario.

### **Step 3 — Forward Hedge**  
1. Lock in forward rate: **F₀**  
2. Compute:  
   **USD_forward = FC_AMT × F₀**  
3. Value stays constant across S_T scenarios.

### **Step 4 — Money-Market Hedge (Synthetic Forward)**

**At t = 0:**  
1. Discount EUR receivable:  
   **EUR_present = FC_AMT / (1 + r_EUR)**  
2. Convert to USD and borrow:  
   **USD_borrowed = EUR_present × S₀**

**At t = 1:**  
3. EUR received repays EUR loan exactly.  
4. Repay USD borrowing with interest:  
   **USD_mm = USD_borrowed × (1 + r_USD)**  

This provides the synthetic forward payoff.

### **Step 5 — Option Hedge Outcomes**

#### **EUR Put**
Protects against euro depreciation.

- If **S_T < K_put** (exercise):  
  **USD_put = FC_AMT × K_put − (Premium_put × FC_AMT)**  
- If **S_T ≥ K_put** (expires):  
  **USD_put = FC_AMT × S_T − (Premium_put × FC_AMT)**

#### **EUR Call**
Provides upside participation.

- If **S_T > K_call** (exercise):  
  **USD_call = FC_AMT × K_call − (Premium_call × FC_AMT)**  
- If **S_T ≤ K_call** (expires):  
  **USD_call = FC_AMT × S_T − (Premium_call × FC_AMT)**

### **Step 6 — Scenario Table**  
For a range of S_T values (e.g., **0.90 to 1.10 × S₀**, increments of 0.01):  
- Compute USD_unhedged  
- Compute USD_forward  
- Compute USD_mm  
- Compute USD_put  
- Compute USD_call  

### **Step 7 — Visualization**  
Produce a **line chart** showing hedge payoffs vs. S_T across all strategies.

---

## 5. Outputs

| Output | Description | Format | Purpose |
|--------|-------------|---------|---------|
| **USD_unhedged** | Baseline USD value | Table | Benchmark |
| **USD_forward** | Forward hedge value | Numeric | Certainty benchmark |
| **USD_mm** | Synthetic forward value | Numeric | IRP check |
| **USD_put** | Put hedge USD outcome | Table/Curve | Downside protection |
| **USD_call** | Call hedge USD outcome | Table/Curve | Upside participation |
| **Chart_1** | Hedge payoffs vs. S_T | Line chart | Executive-friendly comparison |
| **Summary** | 1–2 paragraph conclusion | Text | Prepares Stage 5 deliverable |

---

## 6. Sensitivity Plan

To evaluate hedge robustness:

- Vary **S_T from 0.90×S₀ to 1.10×S₀**, step = 0.01  
- For each S_T scenario, compute all hedge outcomes  
- Present results in a table and a line chart  
- Identify:  
  - Option breakeven points  
  - Regions where each hedge dominates  
  - Range of USD outcomes (risk bands)

This ensures management sees both downside protection and upside participation differences.

---

## 7. Limitations & Next Steps

### **Limitations**
- No option pricing/volatility modeling included  
- No bid-ask spreads, margin requirements, or credit risk  
- Assumes perfect borrowing and lending at market rates  
- No FX forecast probabilities or stochastic modeling  

### **Next Steps (Stage 3)**
- Build Excel model implementing all calculations  
- Assign named ranges for inputs  
- Generate tables and charts  
- Prepare the structure for Stage 4 and Stage 5
