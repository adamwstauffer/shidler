# FIN-321 — Transaction Hedging Project (Receivable)

**Due Date:** See syllabus  
**Submission Platform:** Lamaku (single PDF)  
**Peer Review Weight:** 33% (Instructor 67%, Peer average 33%)

---

## 🎯 Objective
Determine the **optimal transaction hedge** for a foreign-currency **receivable** due in the short run. Compare a **forward**, **money market**, **option**, and **no-hedge** strategy; justify your recommendation with quantitative analysis and clear reasoning.

---

## 📦 Deliverables (single PDF, in order)
1. **Cover Page** (only page with your name): Title, Name, Date, Topic, LLM(s) Used  
2. **Executive Summary** (≤ ½ page): key recommendation + why  
3. **Main Memo** (≤ 2 pages): analysis, formulas, sensitivity, risks, and governance  
4. **Addendum** (not in page limit):  
   - `specs/hedging-spec.md` (or a screenshot)  
   - Initial and revised **prompts** (verbatim)  
   - References and any appendix figures/tables

> Also push your source files to GitHub (optional but recommended for versioning): spreadsheet, spec, prompt log, and memo markdown.
> Lamaku submission remains the official submission of record.
 
---

## 🧪 Scenario (Base Case)
You may use the base case or design your own (clearly document deviations in your spec).

- Receivable: **€5,000,000** in **90 days**  
- Spot (USD/EUR): **1.1000**  
- 90-day Forward (USD/EUR): **1.1050**  
- USD rate (annual): **5.00%**  
- EUR rate (annual): **3.00%**  
- Option: **EUR put** with strike **K** (USD/EUR), premium **c** (USD per EUR); choose reasonable values or market quotes

**Time fraction**: use **t = 90/360** unless you document an alternative.

---

## 🧰 Required Strategies
- **Forward:** lock F; USD proceeds = € * F  
- **Money Market (MM):** borrow € PV today, convert at spot, invest USD → USD proceeds = S * ( € / (1+ r_EUR·t) ) * (1 + r_USD·t )  
- **Option:** buy **EUR put** (protects USD from EUR depreciation) → USD proceeds at T = € * MAX(S_T, K) − (premium in USD)  
- **No Hedge:** USD proceeds = € * S_T (expose to FX)

Add a **parity check**: implied forward **F_IRP = S·(1 + r_USD·t)/(1 + r_EUR·t)** vs quoted F.

---

## 🧮 Analysis Requirements
- Build your model in `analysis/hedging-model.xlsx` (starter template provided).  
- Include a **sensitivity table** of USD proceeds for S_T at −10%, −5%, 0%, +5%, +10% vs spot.  
- Identify the **breakeven** for the option.  
- State your **decision rule** (e.g., maximize expected USD proceeds given a distribution; or minimize downside risk subject to floor).  
- Recommend a strategy; discuss **trade-offs** (certainty, upside participation, premium cost, credit/operational risks).

---

## 🧠 Spec & Prompts
- Create `specs/hedging-spec.md` to define scenario, inputs, formulas, decision rule, and acceptance criteria.  
- Maintain `prompts/prompt-log.md` with the initial and revised prompts (+ any model-check prompts).

---

## 📝 Memo (≤ 2 pages) — Suggested Sections
- Background & Exposure
- Alternatives & Core Math (forward, MM, option)
- Sensitivity & Risk
- Recommendation & Governance (limits, triggers, reporting)

> Executive Summary (≤ ½ page) appears before the memo and does not count toward the 2-page limit.

---

## 🧾 Grading (10 points total)
- **Spec quality & completeness** — 2 pts  
- **Prompt evolution & transparency** — 2 pts  
- **Quant accuracy & sensitivity** — 3 pts  
- **Clarity & structure (incl. exec summary)** — 2 pts  
- **Peer review participation (x2)** — 1 pt  
> Final score = 67% instructor rubric + 33% peer-review average.
