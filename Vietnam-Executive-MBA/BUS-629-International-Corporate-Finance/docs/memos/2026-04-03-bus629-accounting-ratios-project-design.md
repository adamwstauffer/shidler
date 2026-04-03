# BUS-629 Accounting Ratios Project — Design Decision Memo

**Created by:** Adam W. Stauffer
**Updated by:** Adam W. Stauffer
**Date Created:** 2026-04-03
**Date Updated:** 2026-04-03
**Version:** 0.2 — Revised draft
**LLM Used:** Claude Opus 4.6

---

## Executive Summary

This memo proposes a 5-stage accounting ratios project for BUS-629 International Corporate Finance (Vietnam EMBA), adapted from the proven BUS-314 undergraduate project. The central pedagogical innovation is **spec-driven design**: students build domain expertise through hands-on modeling (Stages 1–3), then distill that expertise into a formal technical specification (Stage 4) precise enough that an LLM can execute a complete ratio analysis from the spec alone (Stage 5). The spec is the capstone artifact — it proves the student understands the work deeply enough to specify it unambiguously. Students select their own companies (including non-U.S. and ASEAN-listed firms), build templates from scratch, self-audit their models, and critically evaluate LLM output against their own analysis. Total weight: 30 points.

---

## Background

### Source Project

BUS-314 (undergrad) runs a successful 4-stage accounting ratios pipeline:

| Stage | Deliverable | Points |
|-------|------------|--------|
| 1 | Executive Memo | 4 |
| 2 | Excel Model Build (from template) | 6 |
| 3 | Technical Specification (post-build) | 4 |
| 4 | Final Analysis + Prompt Engineering | 10 |
| | **Total** | **24 + 3 EC** |

The undergrad version provides Excel skeleton templates (progressive reveal), pre-selected company scenarios, and detailed step-by-step instructions. This works well for students encountering financial modeling for the first time.

### Why Adapt for EMBA?

EMBA students bring professional experience and should be challenged differently:

- **Self-directed learning** — Less hand-holding, more design thinking
- **Real-world framing** — They've seen (or built) models in the workplace; now formalize that intuition
- **Delegation through specification** — Senior professionals don't compute ratios; they write the spec for what should be computed, how, and why — then evaluate the output
- **Critical AI literacy** — Not just "use AI" but "evaluate AI output against your own expertise"
- **Company relevance** — Students analyze a company relevant to their own industry, employer, or career goals
- **International scope** — Vietnam EMBA students should be able to analyze HOSE/HNX-listed, ASEAN, or other non-U.S. companies

### Key Design Principles

1. **Build before you write** — Template architecture comes first; designing the model structure teaches ratio logic more deeply than filling in a pre-built template
2. **Choose your own company** — Intrinsic motivation; students analyze something they care about professionally
3. **Validate your own work** — Self-audit is a professional skill; catch your own errors before someone else does
4. **Spec-driven design** — The technical specification is the central artifact. If your spec is precise enough that an LLM (or a junior analyst, or a new hire) can execute it correctly, you've demonstrated mastery. If the output is wrong, the spec is wrong — and that's where the learning happens
5. **Evaluate, don't accept** — The final stage tests judgment: can you identify where AI output diverges from what a domain expert would produce?

---

## Method — Proposed 5-Stage Structure

### Stage 1: Template Architecture (6 pts)

**What:** Student builds a complete accounting ratios spreadsheet template from the ground up — no skeleton, no starter file. The template should be empty of company data but fully structured and ready to receive any company's financials.

**Why first:** Designing the container forces students to think about what data they need, how it flows between statements, and how ratios connect — before any numbers distract them. This is architectural thinking. It also builds the tacit knowledge that makes Stage 4's spec writing possible — you can't specify what you haven't built.

**Deliverable:** Blank `.xlsx` workbook with:
- Financial statement tabs (Balance Sheet, Income Statement, Cash Flow)
- Ratios tab with input section and all six ratio categories
- Named ranges defined (empty but named)
- Color coding system applied (Yellow/Blue/Green/Gray)
- Notes tab documenting layout decisions and named range conventions

**Minimal instructions provided (by design).** Instead, supply:
- The list of 25+ ratios organized by category (Performance, Profitability, Efficiency, Leverage, Liquidity, Du Pont)
- Best practices one-pager covering:
  - **Layout:** One tab per financial statement; separate inputs from calculations from outputs
  - **Color coding:** Yellow = editable inputs, Blue = assumptions, Green = formulas, Gray = outputs
  - **Named ranges:** Use prefixed conventions (`BAL_`, `INC_`, `CASH_`, `RATIO_`, `startYear_`, `avg_`)
  - **Flow direction:** Inputs flow left-to-right or top-to-bottom; never circular
  - **Formatting:** Consistent number formats, thousands separators, percentage displays, right-aligned numbers, left-aligned labels
  - **Auditability:** Every formula should be traceable; no hardcoded numbers in formula cells
  - **Freeze panes:** Lock row/column headers for navigation
  - **Data validation:** Where appropriate, use dropdowns or input constraints

**Rubric:**

| Criterion | Points | What distinguishes strong work |
|-----------|--------|-------------------------------|
| Structure & Layout | 2 | Logical tab organization; clear separation of inputs, calculations, outputs |
| Named Ranges | 2 | Consistent naming convention; all key cells named; documented in Notes tab |
| Formatting & Professionalism | 1 | Color coding applied; number formats consistent; print-ready appearance |
| Completeness | 1 | All six ratio categories represented; all required inputs have designated cells |

---

### Stage 2: Company Selection Memo (4 pts)

**What:** Executive memo selecting and justifying the company the student will analyze. Frames the project scope, identifies data sources, and previews analytical approach.

**Why second:** With the template already built, the student knows exactly what data points they need. The memo becomes more precise — "I need prior-year total assets because my template computes start-of-year ROA" — rather than abstract hand-waving.

**Deliverable:** 400–600 word Markdown memo (`.md`) addressed to a CFO or VP of Finance.

**Company eligibility:**
- Publicly traded on a major exchange (NYSE, NASDAQ, HOSE, HNX, SGX, SET, IDX, PSE, Bursa Malaysia, or other recognized exchange)
- Annual report or 10-K equivalent available with sufficient detail for ratio computation
- Non-financial company (banks, insurance, and REITs have materially different ratio structures)
- Minimum 2 years of comparable data (current year + prior year)
- **Non-U.S. companies are encouraged**, especially firms listed on Vietnamese or ASEAN exchanges. If financial statements are in a language other than English, the ratio analysis and all deliverables must still be written in English. Students should note any IFRS vs. U.S. GAAP differences that affect ratio interpretation.

**Required sections:**

1. **Company Overview** — Name, ticker, exchange, industry, brief business description, market cap, reporting currency
2. **Selection Rationale** — Why this company? Relevance to student's industry, employer, career goals, or analytical interest. What makes it a compelling ratio analysis subject? (e.g., recent M&A, industry disruption, capital structure shift, cross-border operations)
3. **Data Availability & Sources** — Confirm access to 10-K / annual report / audited financials, identify specific data sources (SEC EDGAR, company IR page, HOSE disclosure portal, Yahoo Finance, etc.), note fiscal year end and reporting standards (U.S. GAAP, IFRS, VAS)
4. **Preliminary Observations** — 2–3 initial hypotheses about what the ratio analysis might reveal (e.g., "Given [Company]'s aggressive expansion into Indochina, I expect high leverage ratios but potentially declining efficiency metrics")
5. **Ratio Categories Preview** — Brief note on which ratio categories are most relevant for this company's industry and why
6. **Data Collection Plan** — Which financial statements are needed, what market/analyst assumptions must be sourced, any currency or accounting standard considerations

**Rubric:**

| Criterion | Points |
|-----------|--------|
| Company Selection & Rationale | 1 |
| Analytical Framing & Hypotheses | 1 |
| Data Source Identification | 1 |
| Professionalism & Communication | 1 |

---

### Stage 3: Model Population & Validation (8 pts)

**What:** Populate the Stage 1 template with real financial data for the chosen company. Compute all ratios. Self-audit the model for internal consistency.

**Why a dedicated stage:** In BUS-314, building and populating happen simultaneously (Stage 2). Separating them for EMBA forces deliberate validation — a skill that distinguishes senior analysts from juniors. The self-audit checklist mirrors what a Big 4 review process looks like. This stage also builds the deep model familiarity required for writing a credible spec in Stage 4.

**Deliverable:** Completed `.xlsx` workbook + brief validation report (`.md`, 200–300 words).

**Workbook requirements:**
- All financial statement data entered from 10-K / annual report / audited financials
- All 25+ ratios computed with working formulas
- Named ranges populated and functional
- Market/analyst assumptions sourced and documented (share price, shares outstanding, cost of capital, tax rate)
- For non-U.S. companies: note reporting currency and any IFRS/VAS adjustments in the Notes tab

**Self-audit checklist (must address each item in validation report):**

| Check | What to verify |
|-------|---------------|
| Balance Sheet balances | Assets = Liabilities + Equity (both years) |
| Du Pont ROA consistency | Du Pont ROA (Margin x Turnover) ≈ Direct ROA |
| Du Pont ROE consistency | Du Pont ROE ≈ Direct ROE |
| Sign checks | No negative ratios where impossible (e.g., negative current ratio) |
| Reasonableness | Ratios fall within plausible industry ranges |
| Named range audit | Spot-check 5 named ranges to confirm they point to correct cells |
| Formula audit | Spot-check 5 formulas to confirm they reference correct inputs |
| Start-of-year vs. average | Compare start-of-year and average-based profitability ratios; explain any divergence |

**Rubric:**

| Criterion | Points |
|-----------|--------|
| Data Accuracy | 2 |
| Formula Correctness | 2 |
| Internal Consistency (Du Pont checks) | 2 |
| Validation Report & Self-Audit | 2 |

---

### Stage 4: Technical Specification — Spec-Driven Design (6 pts)

**What:** Write a formal technical specification that fully defines the accounting ratio analysis for the student's company. The spec must be precise and complete enough that an LLM — with no prior context — can take the spec as its sole input and produce a correct, comprehensive ratio analysis with strategic recommendations.

**This is the central artifact of the project.** It is not a "prompt" in the casual sense. It is a technical specification — the same kind of document a finance director would hand to a new analyst, an offshore team, or an automation system. The fact that the executor happens to be an LLM is incidental; the spec should work for any competent executor.

**Why spec-driven design matters:** In professional practice, the ability to specify analytical work precisely is more valuable than the ability to execute it. Execution scales (via teams, tools, AI); specification requires domain expertise that cannot be delegated. A spec that produces wrong output reveals a gap in the author's understanding — and that feedback loop is where the deepest learning happens.

**Pedagogical connection to earlier stages:**
- **Stage 1** (template architecture) taught the student *what* a ratio model needs
- **Stage 2** (company memo) taught the student *why* this company and *what* to look for
- **Stage 3** (population & validation) taught the student *how* the numbers behave and where errors hide
- **Stage 4** synthesizes all of this into a specification that proves mastery: "I understand this well enough to specify it unambiguously for someone (or something) that has never seen it before"

**Deliverable:** Technical specification document (`.md`, 3–5 pages).

**Required specification components:**

**Part A — Model Specification** (defines the ratio model)

1. **Scope & Objective** — Company name, fiscal period, reporting standard (GAAP/IFRS/VAS), analytical objective, intended audience
2. **Data Inputs** — Complete, explicit table of every financial data point required. Organized by source:
   - Balance Sheet items (current year and prior year)
   - Income Statement items
   - Cash Flow Statement items
   - Market/Analyst inputs (share price, shares outstanding, cost of capital, tax rate)
   - All values stated numerically — the executor does not look up, infer, or estimate any data
3. **Named Range Conventions** — Full map of named ranges to values. Each named range includes: name, source, value, and unit. Example: `BAL_assets_total_2025 | Balance Sheet | 394,328 | USD millions`
4. **Derived Inputs** — Computed intermediate values (averages, start-of-year figures, daily rates, after-tax operating income) with explicit formulas in named-range notation
5. **Ratio Definitions & Formulas** — Every ratio, organized by category (Performance, Profitability, Efficiency, Leverage, Liquidity, Du Pont), with:
   - Formula in named-range notation (e.g., `RATIO_ROA = INC_net / startYear_assets_total`)
   - Expected unit (%, x, days, currency)
   - Brief interpretation guide (what does "high" or "low" mean for this ratio?)
6. **Validation Rules** — Internal consistency checks the executor must verify:
   - Du Pont ROA ≈ Direct ROA
   - Du Pont ROE ≈ Direct ROE
   - Balance Sheet balance (both years)
   - Any company-specific checks

**Part B — Analysis Specification** (defines what to do with the computed ratios)

7. **Analysis Requirements** — For each ratio category, specify:
   - What to interpret and why it matters for this company
   - Benchmarks or comparison targets (industry averages, competitor values, or general expectations — provide actual numbers where available, or instruct the executor to apply general knowledge)
   - Cross-category connections to examine (e.g., "Assess whether leverage is amplifying ROE sustainably by examining debt ratios alongside profitability trends")
8. **Du Pont Decomposition** — Specific instructions for ROE breakdown: which component is the primary driver? Is the balance sustainable?
9. **Strategic Recommendation Requirements** — Number of recommendations (3–5), evidence standard (each must cite specific ratio values), actionable specificity (who does what by when)
10. **Output Format Specification** — Exact structure of the deliverable:
    - Document format (executive memo)
    - Required sections and their order
    - Length targets per section
    - Tone and audience (e.g., "addressed to the Board of Directors; executive-level language; no unexplained jargon")
    - How to present ratio results (tables, narrative, or both)

**Quality test:** A well-written spec should be self-contained. If you hand Part A + Part B to an LLM with zero additional context, it should produce output that is substantially correct. If it doesn't, the spec has gaps — and identifying those gaps is the learning.

**Rubric:**

| Criterion | Points | What distinguishes strong work |
|-----------|--------|-------------------------------|
| Data Completeness (Part A, items 1–4) | 1.5 | Every input value present; no gaps the executor must fill |
| Ratio Definitions & Formulas (Part A, items 5–6) | 1.5 | All 25+ ratios specified with correct formulas and validation rules |
| Analysis Specification (Part B, items 7–10) | 1.5 | Clear interpretive guidance; meaningful benchmarks; actionable recommendation criteria |
| Spec Craft & Clarity | 1.5 | Unambiguous language; logical organization; a competent executor could follow this without asking questions |

---

### Stage 5: LLM Analysis & Executive Evaluation (6 pts)

**What:** Execute the Stage 4 specification with an LLM. Receive the AI-generated analysis. Then — critically — evaluate, correct, and annotate the output. Submit the raw LLM output, the student's evaluated final version, and a reflection on what the spec got right and wrong.

**Why this is the capstone:** The future of finance work is not "do the analysis" or "make the AI do the analysis." It's "specify the work, evaluate the output, and take responsibility for the final product." This stage tests judgment — and closes the spec-driven design feedback loop. Where the LLM output diverges from the student's own Stage 3 analysis, either the spec had a gap or the student's manual work had an error. Either way, the student learns.

**Deliverables:**
1. **Raw LLM output** (`.md`) — Unedited response from the LLM, produced by pasting the Stage 4 spec
2. **Evaluated final analysis** (`.md`, 3–5 pages) — Student-edited version with annotations
3. **Spec retrospective** (included in final analysis or as separate section, 300–500 words)

**Required sections in the evaluated final analysis:**

1. **Company & Data Summary** — Verified company context, assumptions, and any accounting standard notes
2. **Ratio Results & Interpretation** — All six categories, with student corrections and additions to LLM output where needed
3. **Du Pont Analysis** — ROE decomposition with student commentary on whether the LLM's interpretation is sound
4. **Strategic Recommendations** — 3–5 actionable recommendations, each with:
   - Data support from the model (cite specific ratio values)
   - Student assessment: Did the LLM get this right? What nuance did it miss?
5. **LLM Evaluation & Annotations** — Critical assessment:
   - What did the LLM execute correctly from the spec?
   - Where did it deviate, hallucinate, or oversimplify?
   - What context did it miss that a human analyst with industry knowledge would catch?
   - Were any errors caused by spec gaps vs. LLM limitations?
6. **Spec Retrospective** — The feedback loop:
   - What would you change in your Stage 4 spec to produce better output?
   - Which spec sections were sufficient? Which were ambiguous?
   - If you re-ran the spec with revisions, what would improve?
   - Rate the spec's effectiveness (1–5) with justification
7. **Executive Justification** — Final investment or strategic thesis in the student's own voice — not the LLM's. This is the "so what?" that only a human with judgment can provide.

**Rubric:**

| Criterion | Points |
|-----------|--------|
| Quality of LLM Output (reflects spec quality) | 1.5 |
| Ratio Interpretation & Accuracy | 1.5 |
| Critical Evaluation & Spec Retrospective | 1.5 |
| Strategic Recommendations & Executive Voice | 1.5 |

---

## Findings — Stage Comparison

### BUS-314 (Undergrad) vs. BUS-629 (EMBA)

| Dimension | BUS-314 (Undergrad) | BUS-629 (EMBA) |
|-----------|---------|---------|
| Template | Provided (progressive reveal) | Built from scratch |
| Company | Pre-selected scenarios | Student's choice (incl. non-U.S.) |
| Stage order | Memo → Build → Spec → Final | Build → Memo → Populate → Spec → LLM Eval |
| Spec role | Post-build reflection | Central artifact; drives LLM execution |
| Validation | Instructor-side checks | Student self-audit (dedicated stage) |
| AI role | Student writes prompt as component of final | LLM executes the spec; student evaluates |
| Capstone skill | Prompt engineering | Spec-driven design + critical evaluation |
| Feedback loop | None (prompt not tested) | Spec → LLM → Retrospective (closed loop) |
| International scope | U.S. companies only | U.S., Vietnamese, and ASEAN companies |
| Points | 24 + 3 EC | 30 |

### Point Allocation

| Stage | Deliverable | Points | % of Total |
|-------|------------|--------|-----------|
| 1 | Template Architecture | 6 | 20% |
| 2 | Company Selection Memo | 4 | 13% |
| 3 | Model Population & Validation | 8 | 27% |
| 4 | Technical Specification (Spec-Driven Design) | 6 | 20% |
| 5 | LLM Analysis & Executive Evaluation | 6 | 20% |
| | **Total** | **30** | **100%** |

### The Spec-Driven Design Arc

```
Stage 1          Stage 2         Stage 3              Stage 4            Stage 5
Build the     →  Frame the    →  Populate &        →  Write the       →  Execute & Evaluate
container        analysis         validate              specification

TACIT KNOWLEDGE ACQUISITION                          KNOWLEDGE EXTERNALIZATION
(learn by doing)                                     (prove you understand by specifying)

"I built it"    "I chose why"   "I verified it"      "I can specify    "I can judge
                                                      it precisely"     the output"
```

The spec (Stage 4) is the **bridge** between domain expertise and delegation. Everything before it builds the knowledge; everything after it tests whether that knowledge was captured precisely enough to be actionable.

---

## Implications

### Pedagogical

- **Stages 1–3** build tacit knowledge through hands-on modeling, company selection, and self-audit
- **Stage 4** externalizes that knowledge into a formal specification — the hardest cognitive step
- **Stage 5** closes the feedback loop: spec quality is tested empirically, not just graded abstractly
- **The 60/40 split** (traditional modeling / spec+AI) reflects where corporate finance is heading
- **Self-audit in Stage 3** is deliberately positioned before spec writing to ensure students have deep model familiarity before they attempt to specify the work for someone else

### Operational

- **No Excel templates to maintain** — Students build from scratch, reducing instructor prep
- **Company diversity** — Each student analyzes a different company, reducing plagiarism risk and enriching class discussion
- **LLM-agnostic** — Students can use any capable LLM (Claude, ChatGPT, Gemini, Copilot, etc.)
- **Grading efficiency** — The spec (Stage 4) is the highest-signal artifact for assessing understanding; instructors can focus grading effort there

### Vietnam EMBA Context

- **Non-U.S. companies explicitly welcomed.** Many EMBA students work at Vietnamese or ASEAN-listed companies. Analyzing their own employer or a regional competitor increases engagement and career relevance.
- **Minimum data requirements for non-SEC filers:** Audited annual report with Balance Sheet, Income Statement, and Cash Flow Statement. English-language financials preferred; if financials are in Vietnamese, all deliverables and the spec must be in English. Students should note the reporting standard (IFRS, VAS, local GAAP) and flag any material differences from U.S. GAAP that affect ratio interpretation (e.g., VAS treatment of revaluation reserves, IFRS 16 lease capitalization).
- **Currency:** All ratio inputs should be in the company's reporting currency. If the student's company reports in VND, ratios are computed in VND. The spec should note the currency and any exchange rate context relevant to interpretation.
- **Time zone and schedule:** Stages should have sufficient buffer between deadlines to accommodate working professionals.

---

## Collaboration Model

### Default: Individual Work

All stages are completed individually. This ensures each student builds personal mastery of the full analytical pipeline — from template design through spec writing and LLM evaluation. The individual model is the recommended default for the first offering of BUS-629.

### Exploration: Team Variant

A team-based variant could work for future offerings or as an instructor option. Here is how it might be structured:

**Team composition:** 2–3 students per team. Larger teams dilute individual learning.

**Stages with team potential:**

| Stage | Individual or Team | Rationale |
|-------|-------------------|-----------|
| 1 — Template Architecture | **Individual** | Every student must build model intuition. This cannot be delegated within a team without loss. |
| 2 — Company Selection Memo | **Team** | Team selects one company together. Each member writes a section of the memo (e.g., one writes rationale, another writes data plan). Joint accountability for company choice. |
| 3 — Model Population & Validation | **Team with individual accountability** | Team populates one shared workbook, but each member owns specific ratio categories and must sign off on their section's validation. Peer cross-check replaces solo self-audit. |
| 4 — Technical Specification | **Team** | Collaborative spec writing mirrors real-world delegation briefs written by teams. Assign sections by expertise. Enforce internal review (each section reviewed by a member who didn't write it). |
| 5 — LLM Evaluation | **Individual** | Each team member independently evaluates the LLM output and writes their own executive evaluation. This prevents free-riding and ensures every student demonstrates judgment. |

**Key risk:** In teams, Stage 1 must remain individual — otherwise some students never internalize the model architecture. Stage 5 must also remain individual — otherwise the evaluation section becomes groupthink.

**Peer review add-on (works with either model):** After Stage 3, students swap workbooks with a classmate for a blind peer review. The reviewer completes a structured checklist (similar to Stage 3's self-audit) and writes a 150-word review note. This adds ~1–2 points and teaches code/model review skills. Could be implemented as a lightweight sub-stage (Stage 3b) without adding a full new stage.

### Recommendation

Start with **individual work** for the first cohort. Introduce the **peer review add-on** (Stage 3b) if class size and schedule permit. Consider the **team variant** for subsequent cohorts after evaluating how the individual model performs.

---

## Future Considerations — Extra Credit & Extensions

No formal extra credit structure for v1, but the following ideas are worth developing for future iterations:

### EMBA-Relevant Extensions

1. **IFRS vs. U.S. GAAP Reconciliation** — For students analyzing non-U.S. companies: identify 3–5 material differences in accounting treatment and quantify the impact on key ratios. High relevance for Vietnamese students working with VAS/IFRS.

2. **Cross-Border Competitor Comparison** — Compare the student's company against a competitor in a different country/reporting jurisdiction. Requires normalizing for accounting standard differences. Teaches what's comparable and what isn't.

3. **Multi-Year Trend Analysis** — Extend the model to 3–5 years. Identify inflection points. More meaningful for companies that have undergone strategic shifts (M&A, market entry, restructuring).

4. **Industry Panel Presentation** — Teams of 3–4 students who analyzed companies in the same industry present a panel discussion. Each presents their company's ratios, then the panel discusses industry-level patterns. Builds presentation and synthesis skills.

5. **Spec Iteration** — After Stage 5, revise the Stage 4 spec based on retrospective findings. Re-run with the LLM. Compare output quality between v1 and v2. Demonstrates iterative improvement — the core of spec-driven design.

6. **Automated Model Generation** — Use the spec to have an LLM generate the Excel workbook itself (via Claude Code, Python + openpyxl, or similar). Compare the auto-generated model to the student's Stage 3 model. Tests whether the spec is precise enough to produce not just analysis but the model itself.

---

## Limitations & Next Steps

### Remaining Decisions

1. **Timeline** — Define stage deadlines relative to the Vietnam EMBA course schedule
2. **LLM guidance** — Provide tips for Claude, ChatGPT, and Gemini? Or keep LLM-agnostic with general best practices?
3. **Peer review implementation** — If Stage 3b peer review is adopted, define the matching process and checklist
4. **Presentation component** — Should Stage 5 include a live defense or presentation of findings? Consider time constraints for working EMBA professionals.
5. **Ratio list adjustments** — Are all 25+ BUS-314 ratios appropriate at the MBA level, or should the list be expanded (e.g., ROIC, free cash flow yield, Altman Z-score)?

### Next Steps

- [ ] Finalize this memo (incorporate feedback)
- [ ] Create Stage 1 best-practices one-pager and ratio category reference sheet
- [ ] Write stage assignment files (`stage1-template-architecture.md` through `stage5-llm-evaluation.md`)
- [ ] Adapt company selection guide for international / non-U.S. / ASEAN companies
- [ ] Update BUS-629 course `README.md` with project overview and timeline
- [ ] Update `CLAUDE.md` to reflect BUS-629 project structure and conventions

---

## References

- BUS-314 Accounting Ratios Project — `BUS-314-International-Corporate-Finance/accounting-ratios/`
- BUS-314 Stage Restructure Decision — `docs/decisions/2026-02-24-bus314-stage-restructure.md`
- BUS-314 Accounting Ratios Skill — `.claude/skills/bus314-accounting-ratios/SKILL.md`
- Memo Template — `docs/templates/memo-template.md`
- Spec Template — `docs/templates/spec-template.md`
