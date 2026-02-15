# Stage 2 – Technical Specification (6 Points)

**Goal:** Using `template-spec.md`, produce a **2–3 page quantitative specification** describing how you will build your accounting ratios model — including every input, formula, and output.

---

## Scenario

You will continue from the same company introduced in your Stage 1 memo. Your task now is to translate the ratio analysis plan into a **technical specification** that a fellow analyst — or an AI assistant — could follow to construct the spreadsheet model.

---

## Include

1. **Problem Statement** – Summarize the company, time period, and analytical objective in professional language.
2. **Inputs (Known Variables)** – Create a clean input table listing every data point you will pull from the financial statements. Group by source:
   - **Balance Sheet** items (current year and prior year)
   - **Income Statement** items
   - **Cash Flow Statement** items
   - **Market / Analyst inputs** (share price, shares outstanding, cost of capital, tax rate)
3. **Named Range Conventions** – Define standardized names for each input (e.g., `BAL_cash_marketable_securities_2024`, `INC_sales`, `CASH_operating`). These will become your Excel named ranges and AI prompt parameters.
4. **Assumptions & Constraints** – Clarify simplifications (e.g., "tax rate assumed at statutory 21%", "interest rates on simple annual basis", "no off-balance-sheet items included").
5. **Calculation Flow** – Lay out the logical sequence for computing ratios, organized by category:
   - Derived inputs (averages, daily figures, after-tax operating income, etc.)
   - Performance ratios (MVA, Market-to-Book, EVA)
   - Profitability ratios (ROA, ROC, ROE — both start-of-year and average-based)
   - Efficiency ratios (turnovers, collection period, days in inventory, margins)
   - Leverage ratios (debt ratios, coverage ratios, debt burden)
   - Liquidity ratios (current, quick, cash, NWC-to-assets)
   - Du Pont decomposition (ROA and ROE)
6. **Outputs** – Identify the specific results, tables, and visualizations your model should produce.
7. **Limitations & Next Steps** – Note what is excluded and how this sets up your Stage 3 Excel build.

---

## Instructions

- **Use the template:** Start from `template-spec.md`.
- **Keep formulas conceptual:** Describe logic and sequence, not cell references. Use named-range notation (e.g., `INC_net / startYear_equity`) so the spec reads like pseudocode.
- **Maintain professional tone:** You are advising the CFO or Director of FP&A.
- **Think ahead:** Design your spec so it can directly feed the spreadsheet, prompt, and final analysis stages.
- **Be concise:** Clear, complete, and no filler — 2 to 3 pages maximum.

---

## Deliverable

- File name: `stage2-spec-LASTNAME.md`
- Length: 2–3 pages
- Tone: Professional, quantitative, and business-ready
- **Due Date:** TBD
- **Points:** 6

---

## Evaluation

| Criterion | Description | Points |
|-----------|-------------|-------:|
| Clarity & Professionalism | Communicates structure effectively to management | 2 |
| Analytical Logic | Coherent, correctly ordered flow for each ratio category | 2 |
| Completeness | All inputs, named ranges, and outputs clearly defined | 1 |
| Reproducibility | Another analyst could build the model from your spec alone | 1 |

---

## How This Sets Up Later Stages

| Stage | What This Spec Enables |
|-------|------------------------|
| **Stage 3** | Each "Input" and "Output" becomes a spreadsheet cell or named range. |
| **Stage 4** | Your "Calculation Flow" becomes an AI prompt instruction block. |
| **Stage 5** | Your "Outputs" drive the interpretation and recommendation. |

> *Treat your specification as the bridge between business insight and technical execution — the CFO should be confident your plan is sound even before seeing the numbers.*
