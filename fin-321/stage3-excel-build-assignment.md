## Stage 3 – Excel Model Build (4 Points)

**Goal:**
Transform your Stage 2 technical specification into a **working Excel model** that implements your hedge analysis. The model should clearly show how each hedging strategy affects your firm’s USD proceeds and risk exposure.

---

### Scenario

You are continuing in your role as the **Financial Analyst or Treasury Analyst** supporting your CFO.
Your Stage 1 memo defined the problem.
Your Stage 2 specification outlined your analytical plan.
Now, in Stage 3, you’ll bring it to life—turning your plan into a functioning spreadsheet that computes and compares hedge outcomes.

---

### Include in Your Model

1. **Inputs (Yellow Section)**

   * All variables defined in your Stage 2 spec.
   * Use clear labeling, consistent units, and defined names for key cells (e.g., `FC_AMT`, `R_USD`, `F0_in`).
   * Highlight all editable cells in yellow.

2. **Forward Hedge**

   * Calculate locked-in USD proceeds.
   * Clearly show where this hedge sits in your comparison table.

3. **Money Market Hedge**

   * Show each sub-step: borrow → convert → invest.
   * Confirm your parity logic by comparing to the forward result.

4. **Option Hedges (Put and Call)**

   * Compute total premium cost.
   * Show how USD proceeds vary with different ending spot rates (`S_T`).
   * You’ll use this logic later for the sensitivity chart.

5. **Sensitivity Table (±5 % in EURUSD)**

   * Vary the ending spot rate from 0.95×S₀ to 1.05×S₀ in 1 % increments.
   * Calculate USD proceeds for each hedge strategy at every rate.
   * (Optional but encouraged) Add a chart comparing hedging outcomes.

6. **Outputs**

   * A clean summary section showing:

     * Forward hedge result (USD)
     * Money Market hedge result (USD)
     * Option results across scenarios
     * Recommendation placeholder (will be finalized in Stage 5).

---

### Instructions & Hints

* **Start from the provided Stage 3 Skeleton or Partial Template.**
  Use the file corresponding to your progress (Skeleton → Forward Partial → Forward + MM Partial).

* **Follow your Stage 2 spec closely.**
  Every variable and step in your plan should appear in your spreadsheet.

* **Keep formulas transparent.**
  Use readable cell references or named ranges. Annotate with brief comments where logic may not be obvious.

* **Check reasonableness.**

  * Forward and MM hedges should yield very similar results (within rounding).
  * Option proceeds should vary logically with `S_T`.

* **Document your work.**
  Add a “Notes” section in your sheet with any assumptions, simplifications, or references.

* **Avoid over-engineering.**
  Focus on clarity and auditability over advanced Excel tricks.

* **Optional Stretch Goal:**
  Add a small macro or data table to automate your sensitivity grid.

---

### Deliverable

* File name: `stage3-model-LASTNAME.xlsx`
* Tabs: Main model + optional “Notes” sheet
* Due: **November 20, 2025**
* **Points:** 4 (graded on structure, accuracy, and professional presentation)

---

### Evaluation Highlights

| Criterion              | Description                                           | Points |
| ---------------------- | ----------------------------------------------------- | -----: |
| Structure & Clarity    | Logical layout, consistent formatting, labeled inputs |      1 |
| Accuracy               | Correct hedge calculations and relationships          |      1 |
| Sensitivity & Analysis | Sensitivity table and (optional) chart implemented    |      1 |
| Professionalism        | Clear presentation, readability, business-ready       |      1 |

---

### How This Leads to Next Stages

| Stage                            | What You’ll Use                                                                               |
| -------------------------------- | --------------------------------------------------------------------------------------------- |
| **Stage 4 – Prompt Engineering** | You’ll use your model logic to design a prompt that generates this spreadsheet automatically. |
| **Stage 5 – Final Analysis**     | You’ll interpret results and recommend the best hedge to your CFO.                            |

> *By completing Stage 3, you bridge the gap between your written specification and a functioning decision tool—exactly what financial analysts do before presenting to senior management.*

