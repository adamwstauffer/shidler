## Stage 3 – Technical Specification (4 Points)

**Goal:**
Using `fin-321/stage3-spec-template.md`, produce a **2–3 page quantitative specification** that documents your Stage 2 Excel model and articulates a refined, improved version. Your spec should be detailed enough that a treasury analyst—or an AI assistant—could reconstruct and enhance the model from your written description alone.

---

### Scenario

You have now built a working hedge model. You know what the calculations look like in practice, where you made judgment calls, and what you would design differently with a clean slate.

Your task in Stage 3 is to turn that hands-on knowledge into a **professional technical document**: one that is simultaneously backward-looking (what you built) and forward-looking (how it should be improved). This is the document that will directly drive your Stage 4 AI prompt.

---

### Include

1. **Problem Statement** – Summarize the exposure, timing, and risk in precise, professional language. Be specific: currency, amount, settlement date, and business consequence of an adverse move.

2. **Inputs (Known Variables)** – List every variable used in your model with its name, value, unit, and data source. Use the standardized naming convention:

   | Named Range  | Description                    | Unit       |
   | ------------ | ------------------------------ | ---------- |
   | `FC_AMT`     | Foreign-currency receivable    | EUR / JPY  |
   | `S0_in`      | Spot rate at inception         | USD per FC |
   | `F0_in`      | Forward rate                   | USD per FC |
   | `R_USD`      | USD interest rate              | Annual %   |
   | `R_FC`       | Foreign-currency interest rate | Annual %   |
   | `K_PUT`      | Put option strike              | USD per FC |
   | `K_CALL`     | Call option strike             | USD per FC |
   | `PREM_PUT`   | Put premium per unit of FC     | USD        |
   | `PREM_CALL`  | Call premium per unit of FC    | USD        |
   | `T_DAYS`     | Days to settlement             | Days       |

3. **Assumptions & Constraints** – Clarify every simplification made in your model: rate basis (ACT/360 vs. ACT/365), treatment of transaction costs, parity assumption between forward and money market hedges, and any other conventions. Be explicit—the goal is full reproducibility.

4. **Calculation Flow** – Lay out the logical sequence for each hedge type. Describe formula logic and step order, not cell addresses:
   * Forward hedge: lock-in rate, compute USD proceeds
   * Money market hedge: borrow FC → convert at spot → invest USD; confirm parity
   * Option hedges: premium cost, net proceeds at various `S_T` values, payoff conditions

5. **Outputs** – Identify each specific result, table, and chart your model produces. Name them clearly (e.g., "Sensitivity Table: USD Proceeds by Strategy vs. S_T") so a reader knows exactly what to expect.

6. **Model Review — What Worked & What to Improve** – This section is unique to Stage 3's post-build approach. Reflect candidly on your Stage 2 model:
   * What was built correctly and operates as intended?
   * What simplifications or workarounds should be replaced in a more rigorous version?
   * What naming, layout, or formula improvements would make the model more auditable?
   * Are there additional scenarios or metrics worth including?

7. **Sensitivity Plan** – Describe how exchange-rate scenarios are constructed and what the sensitivity chart communicates. Explain the ±5% range, step size, and which strategy comparisons are most useful.

8. **Limitations & Next Steps** – Note what is excluded (e.g., dynamic hedging, credit risk, accounting treatment) and explain how this specification will feed directly into your Stage 4 AI prompt.

---

### Instructions

* **Use the template:** Start from `fin-321/stage3-spec-template.md`.
* **Be precise:** Every variable must have a name, value, and unit. Vague descriptions ("a reasonable interest rate") are not acceptable.
* **Write for an AI reader:** Your Stage 4 prompt will draw heavily from this document. If an instruction is ambiguous here, the AI will guess—and probably guess wrong.
* **Keep formulas conceptual:** Describe logic and sequence (e.g., "divide FC_AMT by (1 + R_FC × T_DAYS/360) to get the borrowing amount"), not cell equations.
* **Maintain professional tone:** You are advising the CFO or Director of Treasury, and documenting for a future model-builder.
* **Be concise:** Clear, complete, and no filler—2 to 3 pages maximum.

---

### Deliverable

* File name: `stage3-spec-LASTNAME.md`
* Length: 2–3 pages
* Tone: Professional, quantitative, and business-ready
* **Due Date:** **November 20**
* **Points:** 4 (graded on clarity, completeness, analytical logic, and reproducibility)

---

### Evaluation Highlights

| Criterion                 | Description                                                           | Points |
| ------------------------- | --------------------------------------------------------------------- | -----: |
| Clarity & Professionalism | Communicates risk, structure, and model logic effectively             |      1 |
| Analytical Logic          | Coherent, correctly ordered calculation flow for each hedge type      |      1 |
| Completeness              | All inputs (with named ranges), assumptions, outputs clearly defined  |      1 |
| Reproducibility           | Another analyst—or an AI—could build or rebuild the model from this spec |   1 |

---

### How This Leads to Stage 4

Your Stage 3 specification is the primary input to your Stage 4 AI prompt. A well-written spec means:

| What You Write in Stage 3            | What It Enables in Stage 4                                   |
| ------------------------------------- | ------------------------------------------------------------ |
| Named ranges with precise definitions | AI uses standardized variable names, no improvisation        |
| Step-by-step calculation flow         | AI generates correct, auditable formulas                     |
| Model review and improvement notes    | AI builds the *improved* version, not just a replica         |
| Explicit output requirements          | AI produces the exact tables, charts, and sections you need  |

> *By completing Stage 3, you create the machine-readable blueprint that transforms your prototype into a polished, AI-generated financial model—demonstrating the full analyst-to-automation workflow used by modern treasury and finance teams.*
