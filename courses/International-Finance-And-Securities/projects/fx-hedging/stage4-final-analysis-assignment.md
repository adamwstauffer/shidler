# Stage 4 – Final Analysis, Prompt Engineering & Recommendation (10 Points)

## Goal

Deliver a polished, executive-ready memo summarizing your FX hedge analysis and recommending the best strategy. As part of this deliverable, you will also write a **structured AI prompt** that could regenerate your spreadsheet model — demonstrating your ability to convert domain knowledge into machine-readable instructions.

This stage combines quantitative rigor, interpretation, communication, and AI fluency — exactly what senior finance leaders expect from modern analysts.

**Hint:** Have your LLM generate a draft based on your Stage 2 spreadsheet output and Stage 3 specification, then refine it with your own analysis and judgment. If you don't have AI access, write the analysis directly from your spreadsheet results and submit the prompt as a standalone document.

---

## Deliverable Requirements (2–4 page `.md` file committed to GitHub)

Must include:

---

### A. Exposure Summary

Brief restatement:
- Currency, amount, and timing of the receivable
- FX risk and consequences for USD cash flows
- Business context for the hedging decision

---

### B. Summary of Hedge Outcomes

Present your key findings by strategy:

| Strategy | What to Highlight | What to Discuss |
|----------|------------------|-----------------|
| **Forward Hedge** | Locked-in USD proceeds | Certainty vs. opportunity cost |
| **Money Market Hedge** | Synthetic forward via borrow/convert/invest | Parity with forward; liquidity implications |
| **Put Option** | Floor protection with upside | Premium cost vs. downside protection |
| **Call Option** | Upside participation | When and why this applies |
| **No Hedge** | Unhedged USD proceeds at various S_T | Risk exposure baseline |

Focus on **insight rather than computation** — the CFO already has the numbers.

---

### C. Sensitivity Interpretation

Explain hedge behavior under:
- EUR depreciation scenarios
- EUR appreciation scenarios

Highlight differences in certainty, flexibility, and cost across strategies. Reference your Stage 2 sensitivity table (±5% range).

---

### D. Strategic Recommendation

Choose one strategy (or combination):
- Forward
- Money Market
- Put
- Call
- Combination

Support with data from your model, risk profile, and business strategy.

---

### E. Executive Justification

Use management-level reasoning:
- Cash flow stability
- Budget certainty
- Liquidity impact
- Optionality value
- Premium costs
- Accounting implications (optional)

---

### F. Structured AI Prompt (Required Component)

Write a **1–2 page structured prompt** (as a separate section or appendix) that could instruct an AI to generate your complete FX hedging spreadsheet. Your prompt must include:

1. **Scenario-Specific Variables** — All values explicitly stated: FC_AMT, spot rate, forward rate, interest rates, option strikes, premiums, T_DAYS. AI does not infer missing data.

2. **Named Range Conventions** — Use standardized names matching your Stage 3 spec (e.g., `FC_AMT`, `S0_in`, `F0_in`, `R_USD`, `R_FC`, `K_PUT`, `K_CALL`, `PREM_PUT`, `PREM_CALL`, `T_DAYS`).

3. **Spreadsheet Requirements** — Instruct the AI to produce:
   - Input section with named ranges
   - Color coding: **Yellow** = Inputs, **Blue** = Assumptions, **Green** = Formulas, **Gray** = Outputs
   - Forward hedge, Money Market hedge (3-step), Option hedges (put and call)
   - Sensitivity table (±5% range)
   - Verification checks (forward vs. MM parity, formula consistency)

4. **Hierarchical Structure** — Use clear section headers (e.g., `# GOAL`, `# INPUT VARIABLES`, `# MODEL LOGIC`, `# VERIFICATION`, `# EXPORT`).

---

## Prompt Engineering Best Practices

### 1. Avoid Vague Prompts

Example of a bad prompt:
> "Make me an FX hedging spreadsheet."

Example of a good prompt:
> "Create an Excel workbook modeling forward, money market, and option hedges for a EUR 4,500,000 receivable using the following market data. Use named ranges matching the convention FC_AMT, S0_in, F0_in..."

### 2. Provide All Variable Values

AI does not infer values. Include every scenario variable explicitly.

### 3. Use Named Ranges Consistently

Never allow the AI to invent its own naming system. Define names in your prompt.

### 4. Specify Formatting Explicitly

Color codes, sections, layout — be explicit.

### 5. Include Context Files from GitHub

This is the most efficient way to use AI for models.

**Options for providing context:**
1. **Best:** GitHub links to your spec and template files
2. **Medium:** Upload `.md` or `.xlsx` files directly
3. **Least:** Copy/paste text manually

---

## Note on AI Access

If you do not have access to an AI tool capable of generating Excel files, you may:
1. Submit your structured prompt (Section F) as written.
2. Submit your Stage 2 model as the primary spreadsheet artifact with a brief note explaining that you would use the prompt to regenerate it.

The prompt itself is the primary deliverable — it demonstrates your ability to convert domain knowledge into machine-readable instructions.

---

## Extra Credit (2 points): Areas for Further Study & Improvement

In 1–2 paragraphs each, discuss **2–3** of the following topics and how they connect to your project:

1. **AI Skills & Automation** — How could AI tools (e.g., Claude Skills, Code Interpreter) pull live market data, regenerate your model on demand, or run Monte Carlo simulations?
2. **Multi-File Reasoning** — How could AI read your spec, model, and prompt together to maintain consistency, automate rebuilds, or create dashboards?
3. **GitHub & Version Control** — How does committing specs, models, and prompts to GitHub enable auditable, reproducible model regeneration? Tie this to your Stages 1–3.
4. **Accounting & Audit Integration** — How do hedge accounting flows (OCI vs. P&L), documentation requirements, and reproducibility connect to this project? How could GitHub serve as audit evidence?

---

## Evaluation

| Criterion | Description | Points |
|-----------|-------------|-------:|
| Hedge Interpretation | Demonstrates understanding of what each strategy achieves | 2 |
| Strategic Recommendation | Actionable, data-supported recommendation | 2 |
| Sensitivity Analysis | Meaningful discussion of outcomes under different scenarios | 1 |
| Structured AI Prompt | Clear, complete, reproducible prompt with all scenario data | 2 |
| Professionalism & Communication | Executive-ready, well-structured deliverable | 1 |
| AI-Generated Output OR Manual Analysis | Working spreadsheet from prompt, or equivalent manual work | 2 |

---

## Career Relevance

This project builds skills used in:

### Corporate Treasury
- Exposure management and hedge design
- Hedge performance testing
- AI-augmented scenario analysis

### Investment Banking
- Cross-border deal modeling
- FX-sensitive valuation adjustments

### FP&A
- Cash flow forecasting under FX uncertainty
- Scenario building and budget risk assessment

### Accounting & Audit
- OCI vs. P&L hedge accounting documentation
- Hedge effectiveness proof
- Version-controlled models and audit trails

### Data, Analytics & AI Roles
- Spec-to-model-to-prompt automation pipeline
- GitHub collaboration and version control
- AI-assisted financial modeling and reporting

---

## Why This Matters

This multi-stage journey reflects workflows used at Big 4 accounting firms, corporate treasury teams, investment banks, and consulting firms. You are demonstrating analytical reasoning, automation fluency, model governance, financial decision leadership, and technical communication.

**This is a portfolio-ready artifact for internships, jobs, and graduate programs.**
