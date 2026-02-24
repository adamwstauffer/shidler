## Stage 2 – Excel Model Build (6 Points)

**Goal:**
Using the provided Stage 2 Skeleton template, build a **working Excel model** that implements your firm's FX hedge analysis. Your model should clearly show how each hedging strategy affects your USD proceeds and risk exposure—turning the business problem from your Stage 1 memo into a functioning analytical tool.

---

### Scenario

You are the **Financial Analyst or Treasury Analyst** supporting your CFO.
Your Stage 1 memo defined the problem—a foreign-currency receivable exposed to exchange-rate risk.
Now, in Stage 2, you'll convert that business scenario into a spreadsheet that computes and compares hedge outcomes side-by-side.

Work from your Stage 1 scenario. If anything is ambiguous (e.g., interest-rate basis, exact option strikes), make a reasonable assumption and note it in your model.

---

### Include in Your Model

1. **Inputs Section (Yellow Cells)**

   * All scenario variables from your Stage 1 memo: FC amount, spot rate, forward rate, interest rates, option strikes, premiums, and time horizon.
   * Use clear labels, consistent units, and **named ranges** for key cells (e.g., `FC_AMT`, `S0_in`, `F0_in`, `R_USD`, `R_FC`, `K_PUT`, `K_CALL`, `PREM_PUT`, `PREM_CALL`, `T_DAYS`).
   * Highlight all editable inputs in **yellow**.

2. **Forward Hedge**

   * Calculate locked-in USD proceeds using the forward rate.
   * Show the result clearly in your comparison summary.

3. **Money Market Hedge**

   * Show each sub-step explicitly: **borrow in foreign currency → convert at spot → invest in USD**.
   * Confirm parity by comparing your MM result to the forward hedge result (they should be very close).

4. **Option Hedges (Put and Call)**

   * Compute total premium cost in USD.
   * Show how USD proceeds vary with different ending spot rates (`S_T`).
   * Use this logic as the basis for your sensitivity section.

5. **Sensitivity Table (±5% range)**

   * Vary the ending spot rate from 0.95×S₀ to 1.05×S₀ in 1% increments.
   * Calculate USD proceeds for each hedging strategy at every rate.
   * Include a chart comparing hedging outcomes across the scenario range.

6. **Summary Output Section (Gray Cells)**

   * Forward hedge result (USD)
   * Money Market hedge result (USD)
   * Option results across key scenarios
   * A placeholder row for your hedge recommendation (to be completed in Stage 5)

---

### Instructions & Hints

* **Start from the provided Stage 2 Skeleton.**
  Use the skeleton file corresponding to your level of progress. Work through it section by section rather than all at once.

* **Let your Stage 1 memo guide you.**
  Every variable you identified in the memo should appear as a labeled input in your spreadsheet.

* **Keep formulas transparent.**
  Use readable cell references or named ranges throughout. Avoid burying logic in deeply nested expressions. Add brief inline comments where the calculation may not be obvious.

* **Check reasonableness as you go.**
  * Forward and MM hedges should produce very similar USD proceeds (within rounding).
  * Option proceeds should vary logically and continuously with `S_T`.
  * No result should look wildly different without a clear reason.

* **Document your assumptions.**
  Add a "Notes & Assumptions" section or a dedicated tab listing any simplifications you made (e.g., rate basis, ignoring bid-ask spreads, transaction costs).

* **Color coding convention:**

  | Color  | Meaning                        |
  | ------ | ------------------------------ |
  | Yellow | Inputs / editable variables    |
  | Blue   | Assumptions                    |
  | Green  | Formulas / intermediate steps  |
  | Gray   | Outputs / summary KPIs         |

* **Avoid over-engineering.**
  Focus on clarity and auditability over advanced Excel tricks. A model a colleague can audit in five minutes is worth more than one with elaborate macros no one can follow.

* **Optional Stretch Goal:**
  Add a data table or short macro to automate your sensitivity grid.

---

### Deliverable

* File name: `stage2-model-LASTNAME.xlsx`
* Tabs: Main model + "Notes & Assumptions" tab
* **Due Date:** **November 7**
* **Points:** 6 (graded on structure, accuracy, and professional presentation)

---

### Evaluation Highlights

| Criterion              | Description                                              | Points |
| ---------------------- | -------------------------------------------------------- | -----: |
| Structure & Clarity    | Logical layout, consistent formatting, labeled inputs    |      2 |
| Accuracy               | Correct hedge calculations; forward ≈ MM parity holds   |      2 |
| Sensitivity & Analysis | Sensitivity table and chart implemented and readable     |      1 |
| Professionalism        | Color coding, named ranges, notes tab, business-ready    |      1 |

---

### How This Leads to Stage 3

Building the model before writing a formal specification is intentional. Once you have worked through the actual calculations, you will have first-hand knowledge of:

* Which inputs are most sensitive and why
* Where the model logic is straightforward vs. where judgment calls were required
* What you would improve if building the model again from scratch

You will carry all of that experience into **Stage 3**, where you will write a formal technical specification that documents what you built *and* articulates a more polished version—one precise enough to instruct an AI assistant to regenerate it in Stage 4.

> *By completing Stage 2, you bridge the gap between a business problem and a functioning decision tool—exactly what financial analysts do before presenting to senior management.*
