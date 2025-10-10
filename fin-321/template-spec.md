# [Spec Title] – Technical Specification Template

**Created by:** [name]  
**Updated by:** [name]  
**Date Created:** [date]  
**Date Updated:** [date]  
**Version:** [0.0]
**LLM Used:"" [LLM] (optional if LLm used)

**Role:** Financial Analyst / Treasury Analyst  
**Audience:** CFO or Director of Treasury  

**Purpose:** Provide a professional, quantitative specification outlining the analytical structure for evaluating FX hedging alternatives.

---

## 1. Problem Statement

Briefly restate the exposure and objective in professional terms.

Example phrasing:
> Our company expects to receive EUR-denominated revenue in 12 months, exposing us to potential FX risk from fluctuations in the EURUSD rate. This specification outlines the analytical framework for quantifying, comparing, and evaluating alternative hedging strategies to mitigate that risk.

Include:
- Exposure type (receivable or payable)  
- Foreign currency amount and time horizon  
- Objective (e.g., protect USD value, preserve upside)  
- Decision context (corporate treasury or business unit)

> *A strong statement demonstrates clear understanding of both financial context and business implications.*

---

## 2. Inputs (Known Variables)

Create a clean, professional input table. This will become the foundation for your spreadsheet and future AI prompts.

| Variable | Description | Unit | Example | Source |
|-----------|-------------|------|----------|--------|
| `FC_AMT` | Foreign-currency receivable | EUR | 1,200,000 | Company data |
| `S₀` | Current EURUSD spot rate | USD/EUR | [Look up] | Market data |
| `F₀` | 1-year EURUSD forward rate | USD/EUR | 1.0890 | Provided |
| `r_USD` | USD 1-year interest rate | % | [Look up] | Market data |
| `r_EUR` | EUR 1-year interest rate | % | [Look up] | Market data |
| `t` | Time to maturity | Years | 1 | Derived |
| `K_put` | EUR Put strike | USD/EUR | [Set at spot] | Analyst choice |
| `K_call` | EUR Call strike | USD/EUR | [Set at spot] | Analyst choice |
| `Premium_put` | Put premium | USD per contract | 0.017 | Scenario |
| `Premium_call` | Call premium | USD per contract | 0.022 | Scenario |

> *Tip:* Keep labels short and standardized. Think like a financial modeler — these names should become variable names, spreadsheet inputs, or prompt parameters later.

---

## 3. Assumptions & Constraints

State all conventions used. Clarity here ensures reproducibility.

Example list:
- Interest rates are quoted on a simple annual basis.  
- Forward rate provided represents a 1-year maturity.  
- Transaction and credit costs are excluded.  
- Option premiums are paid upfront in USD.  
- Exchange rates expressed as USD per EUR.  

> *Write assumptions so another treasury analyst could replicate your results exactly.*

---

## 4. Calculation Flow

Describe the logic and sequencing of your analysis — as if briefing a junior analyst or AI model builder. Focus on **order of operations**, not formulas.

Example flow:
1. Compute USD proceeds under the forward hedge.  
2. Recreate a synthetic forward using money market parity to validate rates.  
3. Compute option hedge outcomes for both the EUR put and EUR call under varying spot outcomes \(S_T\).  
4. Compare USD results across hedges at the base case and across sensitivity scenarios.  
5. Summarize the trade-offs (certainty vs. optionality vs. cost).  

> *Your goal: anyone reading this section should know exactly how to implement your logic in Excel or code — without you explaining formulas.*

---

## 5. Outputs

List expected results from the model. These become your **spreadsheet outputs**, **AI prompt targets**, and **Stage 5 discussion points**.

| Output | Description | Format | Purpose |
|---------|--------------|---------|----------|
| `USD_forward` | USD proceeds from forward hedge | Numeric | Certainty benchmark |
| `USD_mm` | USD proceeds from money market hedge | Numeric | Cross-check against forward |
| `USD_put` | USD proceeds from EUR put hedge | Table | Sensitivity & protection |
| `USD_call` | USD proceeds from EUR call hedge | Table | Optional upside case |
| `Chart_1` | Hedge outcomes vs. S_T | Line chart | Visual comparison |
| `Summary` | Written conclusion | 1–2 paragraphs | Executive-ready takeaway |

> *Outputs should read like a professional financial dashboard — clear, repeatable, and decision-focused.*

---

## 6. Sensitivity Plan

Define how you will test and visualize FX outcomes.

Example:
> Vary EURUSD spot at maturity \(S_T\) from 0.95×S₀ to 1.05×S₀ in increments of 0.01.  
> For each value, compute USD proceeds under all hedge strategies.  
> Present results as a comparison table and line chart.

> *Professional analysts always test sensitivity — it shows how robust their recommendations are.*

---

## 7. Limitations & Next Steps

Briefly note any analytical limits (e.g., volatility ignored, credit risk excluded) and outline your immediate next step (e.g., model build in Stage 3).

Example phrasing:
> This specification does not incorporate implied volatility or transaction costs. The next phase will involve constructing an Excel model implementing this logic to quantify results under each hedge structure.

---

# 🧭 Writing a Strong Specification

**Your spec should:**
- **Communicate like a professional:** clear, structured, and jargon-free.  
- **Think one stage ahead:** your spec should feed directly into your Excel build or AI prompt.  
- **Be internally consistent:** variables, labels, and steps must align.  
- **Be reproducible:** a new analyst should be able to implement your plan without your help.  
- **Be executive-relevant:** the CFO should understand *what you’re doing* and *why it matters*.

---

## 🔗 How This Sets You Up for Later Stages

| Stage | What This Spec Enables |
|-------|------------------------|
| **Stage 3** | Each “Input” and “Output” becomes a spreadsheet cell or named range. |
| **Stage 4** | Your “Calculation Flow” becomes an AI prompt instruction block. |
| **Stage 5** | Your “Outputs” drive the interpretation and recommendation. |

> *Treat your specification as the bridge between business insight and technical execution — the CFO should be confident your plan is sound even before seeing the numbers.*
