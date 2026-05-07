# Stage 4: LLM-Drafted Technical Specification

**Weight:** 20% of project score (70% deliverable / 30% presentation)
**Deliverable:** Technical specification (`.md`) drafted with an LLM, plus a prompt log entry

---

## Overview

Use an LLM (Claude or another capable model) to draft a formal technical specification that fully defines both the Excel ratio model and the analytical work to be done on your selected company. The spec must be precise enough that an LLM with no prior context — given only the spec as input — can produce a correct, comprehensive ratio analysis with strategic recommendations.

You are not writing the spec from a blank page. You are using an LLM to **draft** it, conditioned on the project instructions and your Stage 1 template. Your job is to direct the drafting, evaluate the output, and ship a spec that *you* would sign your name to.

**This is the central artifact of the project.**

## Why spec-driven design + LLM drafting

Two pedagogical moves stack here:

1. **Spec-driven design.** The ability to specify analytical work precisely is more valuable than the ability to execute it. Execution scales (via teams, tools, AI); specification requires domain expertise that cannot be delegated.
2. **LLM as drafter, you as editor.** The future of finance work is not "write everything from scratch" or "let AI write everything." It's specify the work, evaluate the output, and take responsibility for the final product.

A spec that produces wrong output at Stage 5 reveals a gap in your spec — and that feedback loop is where the deepest learning happens.

---

## Deliverable

A technical specification (`.md`, 3–5 pages) saved to `docs/specs/` in your repository, plus a corresponding prompt log entry.

**Spec filename:** `YYYY-MM-DD-{lastname}-{company-slug}-spec.md`
Example: `2026-06-18-nguyen-vinamilk-spec.md`

**Spec template:** [`../../docs/templates/spec-template.md`](../../docs/templates/spec-template.md) — copy, rename per the convention above, fill in the sections, keep the YAML frontmatter intact.

**Prompt log:** Add a row to your `deliverables/prompt-log.md` for each meaningful prompt session used to draft the spec. Use [`../../docs/templates/prompt-log-template.md`](../../docs/templates/prompt-log-template.md) if you don't already have one.

---

## Two LLM workflows — pick one

### Workflow A — Claude desktop / ChatGPT (file uploads)

Best if you don't yet have a CLI workflow. Works in any browser.

1. Open [Claude](https://claude.ai) (or ChatGPT, or another capable model).
2. Upload these files into the chat:
   - The Stage 4 brief (this document, exported as PDF or pasted as text)
   - Your Stage 1 template: `models/templates/performance-ratios-template.xlsx`
   - The repo-level [`spec-template.md`](../../docs/templates/spec-template.md)
   - Your Stage 3 populated workbook (gives the LLM real numbers to populate the Data Inputs section)
3. Prompt: *"Using the spec template structure, draft a technical specification for [company] ratios analysis. Populate every section. Use named-range notation throughout. Where data values appear in my Stage 3 workbook, include them numerically in the Data Inputs table."*
4. Iterate. Ask the LLM to expand sparse sections, tighten verbose ones, and verify formulas tie to your template's named ranges.
5. Copy the final output into `docs/specs/YYYY-MM-DD-{lastname}-{company-slug}-spec.md` in your repo.

### Workflow B — Claude Code CLI (terminal)

Best if you already cloned your repo locally and want the LLM to read repo files directly.

1. Install [Claude Code](https://claude.ai/code) and `cd` into your portfolio repo.
2. Launch `claude`.
3. Prompt:
   ```
   Read these files:
   - https://raw.githubusercontent.com/adamwstauffer/shidler/main/courses/BUS-629-VEMBA-International-Corporate-Finance/stage4-technical-specification.md
   - https://raw.githubusercontent.com/adamwstauffer/shidler/main/docs/templates/spec-template.md
   - models/templates/performance-ratios-template.xlsx (in this repo)
   - models/builds/<your Stage 3 file>.xlsx (in this repo)

   Draft a technical specification for {company} accounting ratios analysis,
   following the spec-template structure. Save it to
   docs/specs/<YYYY-MM-DD>-<lastname>-<company-slug>-spec.md.
   ```
4. Iterate inside Claude Code, asking it to refine specific sections.
5. Commit and push when done.

---

## Required spec components

### Part A — Model Specification

Defines the Excel ratio model: structure, data, formulas, and validation. Detailed enough that the executor could reconstruct your Stage 1 template and Stage 3 populated model from this document alone.

1. **Scope & Objective** — Company, fiscal period, reporting standard (GAAP/IFRS/VAS), reporting currency, analytical objective, intended audience.
2. **Model Architecture** — Tab layout, color coding, input/calculation/output separation, formatting requirements.
3. **Data Inputs** — Complete table of every financial data point required, with values stated numerically (sourced from your Stage 3 workbook).
4. **Named Range Conventions** — Full map of named ranges (`BAL_*`, `INC_*`, `CASH_*`, `RATIO_*`) to values.
5. **Derived Inputs** — Computed intermediate values (averages, start-of-year figures, after-tax operating income) with explicit formulas in named-range notation.
6. **Ratio Definitions & Formulas** — Every ratio organized by category (Performance, Profitability, Efficiency, Leverage, Liquidity, Du Pont) with formula in named-range notation, expected unit, and brief interpretation guide.
7. **Validation Rules** — Internal consistency checks (Du Pont vs. direct, Balance Sheet balance, etc.).

### Part B — Analysis Specification

Defines what to do with the computed ratios.

8. **Analysis Requirements** — For each ratio category: what to interpret, benchmarks or comparison targets, cross-category connections to examine.
9. **Du Pont Decomposition** — Specific instructions for ROE breakdown analysis.
10. **Strategic Recommendation Requirements** — Number of recommendations (3–5), evidence standard, actionable specificity.
11. **Output Format** — Exact structure of the deliverable: sections, order, length targets, tone, audience.

---

## Quality test

A well-written spec is **self-contained**. If you hand Part A + Part B to an LLM with zero additional context (which is exactly what Stage 5 will do), it should be able to:

1. Reconstruct the ratio model — or verify the provided ratios against the formulas
2. Produce a substantially correct analysis with meaningful strategic recommendations

If it can't, the spec has gaps. Identifying those gaps is the learning.

---

## In-class presentation (30% of stage grade)

A 5–7 minute presentation walking through your spec.

**Suggested structure:**
- Which workflow you used (desktop vs. CLI) and why (1 minute)
- One section of your spec that took the most iteration to get right (2–3 minutes)
- One section the LLM drafted well on the first pass (1 minute)
- The "spec quality test": what would you change if you re-ran (1 minute)
- Q&A (1–2 minutes)

---

## Rubric (Stage 4 = 20% of project)

### Deliverable — 70% of stage grade

| Criterion | % of deliverable | What distinguishes strong work |
|-----------|-----------------:|--------------------------------|
| Model spec — Data & Structure (Part A, items 1–5) | 25% | Every input value present numerically; architecture fully defined |
| Model spec — Ratios & Validation (Part A, items 6–7) | 25% | All 25+ ratios specified with correct formulas in named-range notation |
| Analysis spec (Part B, items 8–11) | 25% | Clear interpretive guidance; meaningful benchmarks; actionable recommendation criteria |
| Spec craft + prompt log quality | 25% | Unambiguous spec language; prompt log captures meaningful iterations, not single-shot copy-paste |

### Presentation — 30% of stage grade

| Criterion | % of presentation |
|-----------|------------------:|
| Walkthrough clarity | 40% |
| Quality of self-critique (what to change) | 30% |
| Response to Q&A | 20% |
| Professionalism (timing, presence) | 10% |

---

## Tips

- **Spec the model, not just the analysis.** The most common failure mode is jumping to Part B before Part A is airtight. The LLM at Stage 5 needs both.
- **Cite numerically.** "Total assets" is not a spec. "`BAL_assets_total_2025` = 394,328 USD millions" is.
- **Iterate the prompt, not just the output.** If the LLM keeps producing weak Part A sections, your prompt is the problem — fix the prompt and re-run, rather than hand-editing the output.
- **Log meaningfully.** "Asked Claude to write the spec" is not a useful log entry. "Iterated three times on the Du Pont section because the first two drafts confused decomposition with attribution" is.
