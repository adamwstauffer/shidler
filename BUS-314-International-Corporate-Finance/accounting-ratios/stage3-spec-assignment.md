# Stage 3 – Technical Specification (4 Points)

**Goal:** Using `template-spec.md`, produce a **2–3 page quantitative specification** that documents your Stage 2 Excel model and articulates a refined, improved version. Your spec should be detailed enough that a fellow analyst — or an AI assistant — could reconstruct the model from your written description alone.

---

## Scenario

You have now built a working ratio model. You know what the calculations look like in practice, where you made judgment calls, and what you would design differently with a clean slate.

Your task in Stage 3 is to turn that hands-on knowledge into a **professional technical document**: one that is simultaneously backward-looking (what you built) and forward-looking (how it should be improved). This is the document that will directly drive your Stage 4 AI prompt.

---

## Include

1. **Problem Statement** – Summarize the company, time period, and analytical objective in professional language.
2. **Inputs (Known Variables)** – Create a clean input table listing every data point you pulled from the financial statements. Group by source:
   - **Balance Sheet** items (current year and prior year)
   - **Income Statement** items
   - **Cash Flow Statement** items
   - **Market / Analyst inputs** (share price, shares outstanding, cost of capital, tax rate)
3. **Named Range Conventions** – Define standardized names for each input (e.g., `BAL_cash_marketable_securities_2024`, `INC_sales`, `CASH_operating`). These are your Excel named ranges and AI prompt parameters.
4. **Assumptions & Constraints** – Clarify simplifications (e.g., "tax rate assumed at statutory 21%", "interest rates on simple annual basis", "no off-balance-sheet items included").
5. **Calculation Flow** – Lay out the logical sequence for computing ratios, organized by category:
   - Derived inputs (averages, daily figures, after-tax operating income, etc.)
   - Performance ratios (MVA, Market-to-Book, EVA)
   - Profitability ratios (ROA, ROC, ROE — both start-of-year and average-based)
   - Efficiency ratios (turnovers, collection period, days in inventory, margins)
   - Leverage ratios (debt ratios, coverage ratios, debt burden)
   - Liquidity ratios (current, quick, cash, NWC-to-assets)
   - Du Pont decomposition (ROA and ROE)
6. **Outputs** – Identify the specific results, tables, and visualizations your model produces.
7. **Model Review — What Worked & What to Improve** – Reflect candidly on your Stage 2 model:
   - What was built correctly and operates as intended?
   - What simplifications or workarounds should be replaced in a more rigorous version?
   - What naming, layout, or formula improvements would make the model more auditable?
   - Are there additional scenarios or metrics worth including?
8. **Limitations & Next Steps** – Note what is excluded and how this sets up your Stage 4 final analysis and AI prompt.

---

## Instructions

- **Use the template:** Start from `template-spec.md`.
- **Keep formulas conceptual:** Describe logic and sequence, not cell references. Use named-range notation (e.g., `INC_net / startYear_equity`) so the spec reads like pseudocode.
- **Maintain professional tone:** You are advising the CFO or Director of FP&A.
- **Reflect on your build:** The "Model Review" section is where the real learning happens. Be honest about what worked and what didn't — this is the kind of reflective documentation that distinguishes strong analysts.
- **Think ahead:** Design your spec so it can directly feed the AI prompt and final analysis in Stage 4.
- **Be concise:** Clear, complete, and no filler — 2 to 3 pages maximum.

---

## Deliverable

- File name: `stage3-spec-LASTNAME.md`
- Length: 2–3 pages
- Tone: Professional, quantitative, and business-ready
- **Due Date:** TBD
- **Points:** 4

---

## Evaluation

| Criterion | Description | Points |
|-----------|-------------|-------:|
| Clarity & Professionalism | Communicates structure effectively to management | 1 |
| Analytical Logic | Coherent, correctly ordered flow for each ratio category | 1 |
| Completeness & Model Review | All inputs, named ranges, outputs defined; candid reflection on what worked and what to improve | 1 |
| Reproducibility | Another analyst could rebuild the model from your spec alone | 1 |

---

## How This Sets Up Later Stages

| Stage | What This Spec Enables |
|-------|------------------------|
| **Stage 4** | Your "Calculation Flow" becomes the AI prompt instruction block. Your "Model Review" tells the AI what to improve. Your "Outputs" drive the interpretation and recommendation. |

> *By completing Stage 3, you create the machine-readable blueprint that transforms your prototype into a polished, documented model — demonstrating the reflective documentation skills valued by finance teams and auditors alike.*
