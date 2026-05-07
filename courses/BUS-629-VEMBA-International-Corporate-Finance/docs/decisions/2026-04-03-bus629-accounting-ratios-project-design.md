# BUS-629 Accounting Ratios Project — Design Decision Memo

**Created by:** Adam W. Stauffer
**Updated by:** Adam W. Stauffer
**Date Created:** 2026-04-03
**Date Updated:** 2026-04-03
**Version:** 0.4 — Revised draft
**LLM Used:** Claude Opus 4.6

---

## Executive Summary

This memo proposes a 6-stage accounting ratios project for BUS-629 International Corporate Finance (Vietnam EMBA), adapted from the proven BUS-314 undergraduate project. The central pedagogical innovation is **spec-driven design**: students build domain expertise through hands-on modeling (Stages 1–3), then distill that expertise into a formal technical specification (Stage 4) precise enough that an LLM can execute a complete ratio analysis from the spec alone (Stage 5). The project begins with a foundational Stage 0 where teams establish professional-grade GitHub repositories with investment-bank-style directory structures, learning version control, Markdown documentation, and collaborative workflows before any analytical work begins. All analytical stages (1–5) are completed individually. Students select their own companies (including non-U.S. and ASEAN-listed firms), build templates from scratch, self-audit their models, and critically evaluate LLM output against their own analysis. Point values are set per class; this memo defines stage weights and rubric proportions.

---

## Background

### Source Project

BUS-314 (undergrad) runs a successful 4-stage accounting ratios pipeline:

| Stage | Deliverable |
|-------|------------|
| 1 | Executive Memo |
| 2 | Excel Model Build (from template) |
| 3 | Technical Specification (post-build) |
| 4 | Final Analysis + Prompt Engineering |

The undergrad version provides Excel skeleton templates (progressive reveal), pre-selected company scenarios, and detailed step-by-step instructions. This works well for students encountering financial modeling for the first time.

### Why Adapt for EMBA?

EMBA students bring professional experience and should be challenged differently:

- **Self-directed learning** — Less hand-holding, more design thinking
- **Real-world framing** — They've seen (or built) models in the workplace; now formalize that intuition
- **Delegation through specification** — Senior professionals don't compute ratios; they write the spec for what should be computed, how, and why — then evaluate the output
- **Critical AI literacy** — Not just "use AI" but "evaluate AI output against your own expertise"
- **Company relevance** — Students analyze a company relevant to their own industry, employer, or career goals
- **International scope** — Vietnam EMBA students should be able to analyze HOSE/HNX-listed, ASEAN, or other non-U.S. companies
- **Professional tooling** — Modern finance teams use version control, structured documentation, and collaborative platforms; the project should too

### Key Design Principles

1. **Professional infrastructure first** — Set up the workspace like a real analytical team before doing any analysis
2. **Build before you write** — Template architecture comes first; designing the model structure teaches ratio logic more deeply than filling in a pre-built template
3. **Choose your own company** — Intrinsic motivation; students analyze something they care about professionally
4. **Validate your own work** — Self-audit is a professional skill; catch your own errors before someone else does
5. **Spec-driven design** — The technical specification is the central artifact. It must be precise enough to fully define the Excel ratio model (structure, named ranges, formulas, validation rules) AND the analysis (interpretation, benchmarking, recommendations). If an LLM — or a junior analyst, or a new hire — can execute it correctly, you've demonstrated mastery. If the output is wrong, the spec is wrong — and that's where the learning happens.
6. **Evaluate, don't accept** — The final stage tests judgment: can you identify where AI output diverges from what a domain expert would produce?

---

## Method — Proposed 6-Stage Structure

### Stage Weight Allocation

Point values are set per class. The following weights define each stage's proportion of the total project score.

| Stage | Deliverable | Weight |
|-------|------------|--------|
| 0 | Repository Setup & Team Infrastructure | 5% |
| 1 | Template Architecture | 20% |
| 2 | Company Selection Memo | 10% |
| 3 | Model Population & Validation | 25% |
| 4 | Technical Specification (Spec-Driven Design) | 20% |
| 5 | LLM Analysis & Executive Evaluation | 20% |
| | **Total** | **100%** |

---

### Stage 0: Repository Setup & Team Infrastructure (5% of project)

**What:** Teams of 3–4 students create a shared GitHub repository with a professional directory structure modeled on how analytical teams at investment banks, Big 4 firms, and corporate finance departments organize their work. Students learn Git fundamentals, Markdown documentation, and collaborative file management.

**Why first:** Every subsequent stage depends on having a well-organized workspace. In professional finance, analysts who can't find files, version documents, or maintain a clean project structure waste enormous time. This stage also removes the "I don't know how to use GitHub" barrier before any graded analytical work begins. It's a low-stakes, high-learning-density introduction.

**Collaboration model:** Individual. Each student creates their own GitHub repository. The course repository (`courses/BUS-629-VEMBA-International-Corporate-Finance/`) serves as a **living example** — students replicate this structure in their own repos.

**Deliverable:** A GitHub repository (named `[username]`, e.g., `adamwstauffer/`) with the following structure (or well-justified variation):

```
[username]/
├── README.md                          # Project charter: name, company, timeline, status
│
├── docs/
│   ├── memos/                         # Executive memos (Stage 2, decision memos)
│   │   └── README.md
│   ├── specs/                         # Technical specifications (Stage 4)
│   │   └── README.md
│   ├── plans/                         # Project plans, timelines, status updates
│   │   └── README.md
│   └── templates/                     # Reusable templates
│       ├── README.md
│       ├── memo-template.md           # Starting point for Stage 2
│       └── spec-template.md           # Starting point for Stage 4
│
├── models/                            # Financial models (Excel workbooks)
│   ├── templates/                     # Stage 1: blank ratio templates
│   │   └── README.md
│   └── builds/                        # Stage 3: populated, working models
│       └── README.md
│
├── data/                              # Source data and financial statements
│   └── README.md                      # Data provenance: sources, access dates, notes
│
├── analysis/                          # Analytical outputs
│   └── validation/                    # Stage 3 validation reports
│       └── README.md
│
└── deliverables/                      # Final, presentation-ready outputs
    └── README.md                      # What constitutes a "final" deliverable
```

**A living example of this structure** — with populated READMEs in every directory — is available in the course repository at [`courses/BUS-629-VEMBA-International-Corporate-Finance/`](../../).

**Why this structure:**

| Directory | IB/Professional Analogue | Purpose |
|-----------|-------------------------|---------|
| `docs/decisions/` | Deal memos, investment committee briefs | Analytical framing and decision documentation |
| `docs/specs/` | Model specification documents, methodology papers | Technical blueprints that define analytical work |
| `docs/plans/` | Project plans, pitch timelines | Coordination and scheduling |
| `docs/templates/` | Firm-wide memo and spec formats | Standardized starting points that ensure consistency |
| `models/templates/` | Blank model frameworks (e.g., LBO template, DCF skeleton) | Reusable analytical infrastructure — separate from populated builds |
| `models/builds/` | Working models with live data | Where the actual analysis lives |
| `data/` | Data room, source documents | Raw inputs kept separate from derived analysis — auditability |
| `analysis/validation/` | Working papers, model review | Self-audit and validation documentation |
| `deliverables/` | Client-ready pitchbooks, final reports | Only polished, reviewed outputs land here |

**Key learning objectives for Stage 0:**

1. **README.md files** — Each directory gets a README explaining what belongs there, naming conventions, and any relevant context. Students learn that a README is the "front door" to any directory — if someone new joins the team, they should be able to navigate the repo from READMEs alone. The top-level README serves as a team charter.

2. **Markdown fundamentals** — Through writing READMEs, students practice headings, lists, tables, links, and code blocks. These are the same formatting tools they'll use for memos (Stage 2), validation reports (Stage 3), specs (Stage 4), and final analysis (Stage 5).

3. **Git basics** — Clone, branch, commit, push, pull. Each team member must make at least one commit. Commit messages should be descriptive (not "update" or "fix").

4. **Naming conventions** — Files follow a consistent pattern: `[stage]-[description].[ext]` (e.g., `stage1-ratio-template.xlsx`, `stage2-company-memo.md`). Since each student has their own repo, names don't need a lastname prefix.

5. **Separation of concerns** — Raw data is not mixed with analysis. Templates are not mixed with populated models. Working drafts are not mixed with final deliverables. This mirrors how professional teams prevent errors and maintain auditability.

**What students submit:** A link to their GitHub repository. The repository must contain the full directory structure with README.md files in every directory.

**Rubric (% of Stage 0 score):**

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Directory Structure | 30% | All required directories present; logical organization; no orphan files |
| README Quality | 30% | Every directory has a README; READMEs explain purpose, conventions, and what belongs; top-level README serves as team charter with member names and project scope |
| Markdown & Formatting | 20% | Correct use of headings, lists, tables, links; consistent formatting across READMEs |
| Git Fundamentals | 20% | At least one meaningful commit per member; descriptive commit messages; no broken files |

**Instructor note:** This stage is intentionally low-weight (5%) and low-stakes. The goal is familiarity, not mastery. Students who struggle with Git here have time to improve before graded analytical work begins. Consider a brief in-class walkthrough or lab session to accompany this stage.

---

### Stage 1: Template Architecture (20% of project)

**What:** Student builds a complete accounting ratios spreadsheet template from the ground up — no skeleton, no starter file. The template should be empty of company data but fully structured and ready to receive any company's financials.

**Why Stage 1:** Designing the container forces students to think about what data they need, how it flows between statements, and how ratios connect — before any numbers distract them. This is architectural thinking. It also builds the tacit knowledge that makes Stage 4's spec writing possible — you can't specify what you haven't built.

**Collaboration model:** Individual. Each student builds their own template. Templates are saved to the team repository under `models/templates/`.

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

**Rubric (% of Stage 1 score):**

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Structure & Layout | 30% | Logical tab organization; clear separation of inputs, calculations, outputs |
| Named Ranges | 30% | Consistent naming convention; all key cells named; documented in Notes tab |
| Formatting & Professionalism | 20% | Color coding applied; number formats consistent; print-ready appearance |
| Completeness | 20% | All six ratio categories represented; all required inputs have designated cells |

---

### Stage 2: Company Selection Memo (10% of project)

**What:** Executive memo selecting and justifying the company the student will analyze. Frames the project scope, identifies data sources, and previews analytical approach.

**Why Stage 2:** With the template already built, the student knows exactly what data points they need. The memo becomes more precise — "I need prior-year total assets because my template computes start-of-year ROA" — rather than abstract hand-waving.

**Collaboration model:** Individual. Each student selects a different company. Memos are saved to `docs/decisions/`.

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

**Rubric (% of Stage 2 score):**

| Criterion | % |
|-----------|---|
| Company Selection & Rationale | 25% |
| Analytical Framing & Hypotheses | 25% |
| Data Source Identification | 25% |
| Professionalism & Communication | 25% |

---

### Stage 3: Model Population & Validation (25% of project)

**What:** Populate the Stage 1 template with real financial data for the chosen company. Compute all ratios. Self-audit the model for internal consistency.

**Why a dedicated stage:** In BUS-314, building and populating happen simultaneously. Separating them for EMBA forces deliberate validation — a skill that distinguishes senior analysts from juniors. The self-audit checklist mirrors what a Big 4 review process looks like. This stage also builds the deep model familiarity required for writing a credible spec in Stage 4.

**Collaboration model:** Individual. Each student populates their own model. Completed workbooks are saved to `models/builds/`; validation reports to `analysis/validation/`.

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

**Rubric (% of Stage 3 score):**

| Criterion | % |
|-----------|---|
| Data Accuracy | 25% |
| Formula Correctness | 25% |
| Internal Consistency (Du Pont checks) | 25% |
| Validation Report & Self-Audit | 25% |

---

### Stage 4: Technical Specification — Spec-Driven Design (20% of project)

**What:** Write a formal technical specification that fully defines both the Excel ratio model and the accounting ratio analysis for the student's company. The spec must be precise and complete enough that an LLM — with no prior context — can take the spec as its sole input and produce (a) a correct, working ratio model and (b) a comprehensive analysis with strategic recommendations.

**This is the central artifact of the project.** It is not a "prompt" in the casual sense. It is a technical specification — the same kind of document a finance director would hand to a new analyst, an offshore team, or an automation system. The fact that the executor happens to be an LLM is incidental; the spec should work for any competent executor.

**Why spec-driven design matters:** In professional practice, the ability to specify analytical work precisely is more valuable than the ability to execute it. Execution scales (via teams, tools, AI); specification requires domain expertise that cannot be delegated. A spec that produces wrong output reveals a gap in the author's understanding — and that feedback loop is where the deepest learning happens.

**Pedagogical connection to earlier stages:**
- **Stage 0** (repo setup) taught the student how to organize professional workspaces
- **Stage 1** (template architecture) taught the student *what* a ratio model needs — structure, tabs, named ranges, color coding, formula flow
- **Stage 2** (company memo) taught the student *why* this company and *what* to look for
- **Stage 3** (population & validation) taught the student *how* the numbers behave and where errors hide
- **Stage 4** synthesizes all of this into a specification that proves mastery: "I understand this well enough to specify it unambiguously for someone (or something) that has never seen it before"

**Collaboration model:** Individual. Each student writes a spec for their own company. Specs are saved to `docs/specs/` (and cross-referenced in `ai/specs/`).

**Deliverable:** Technical specification document (`.md`, 3–5 pages).

**Required specification components:**

**Part A — Model Specification** (defines the Excel ratio model — structure, data, formulas)

The model specification must be detailed enough that the executor could reconstruct the student's Stage 1 template and Stage 3 populated model from this document alone.

1. **Scope & Objective** — Company name, fiscal period, reporting standard (GAAP/IFRS/VAS), reporting currency, analytical objective, intended audience

2. **Model Architecture** — Specify the spreadsheet structure:
   - Tab layout (which tabs, what each contains, how data flows between them)
   - Color coding conventions and their meaning
   - Input/calculation/output separation
   - Any formatting requirements (number formats, decimal places, header styles)

3. **Data Inputs** — Complete, explicit table of every financial data point required. Organized by source:
   - Balance Sheet items (current year and prior year)
   - Income Statement items
   - Cash Flow Statement items
   - Market/Analyst inputs (share price, shares outstanding, cost of capital, tax rate)
   - All values stated numerically — the executor does not look up, infer, or estimate any data

4. **Named Range Conventions** — Full map of named ranges to values. Each named range includes: name, source, value, and unit. Example: `BAL_assets_total_2025 | Balance Sheet | 394,328 | USD millions`

5. **Derived Inputs** — Computed intermediate values (averages, start-of-year figures, daily rates, after-tax operating income) with explicit formulas in named-range notation

6. **Ratio Definitions & Formulas** — Every ratio, organized by category (Performance, Profitability, Efficiency, Leverage, Liquidity, Du Pont), with:
   - Formula in named-range notation (e.g., `RATIO_ROA = INC_net / startYear_assets_total`)
   - Expected unit (%, x, days, currency)
   - Brief interpretation guide (what does "high" or "low" mean for this ratio?)

7. **Validation Rules** — Internal consistency checks the executor must verify:
   - Du Pont ROA ≈ Direct ROA
   - Du Pont ROE ≈ Direct ROE
   - Balance Sheet balance (both years)
   - Any company-specific checks

**Part B — Analysis Specification** (defines what to do with the computed ratios)

8. **Analysis Requirements** — For each ratio category, specify:
   - What to interpret and why it matters for this company
   - Benchmarks or comparison targets (industry averages, competitor values, or general expectations — provide actual numbers where available, or instruct the executor to apply general knowledge)
   - Cross-category connections to examine (e.g., "Assess whether leverage is amplifying ROE sustainably by examining debt ratios alongside profitability trends")

9. **Du Pont Decomposition** — Specific instructions for ROE breakdown: which component is the primary driver? Is the balance sustainable?

10. **Strategic Recommendation Requirements** — Number of recommendations (3–5), evidence standard (each must cite specific ratio values), actionable specificity (who does what by when)

11. **Output Format Specification** — Exact structure of the deliverable:
    - Document format (executive memo)
    - Required sections and their order
    - Length targets per section
    - Tone and audience (e.g., "addressed to the Board of Directors; executive-level language; no unexplained jargon")
    - How to present ratio results (tables, narrative, or both)

**Quality test:** A well-written spec should be self-contained. If you hand Part A + Part B to an LLM with zero additional context, it should be able to:
1. Reconstruct the ratio model (or verify the provided ratios against the formulas)
2. Produce a substantially correct analysis with meaningful strategic recommendations

If it can't, the spec has gaps — and identifying those gaps is the learning.

**Rubric (% of Stage 4 score):**

| Criterion | % | What distinguishes strong work |
|-----------|---|-------------------------------|
| Model Specification — Data & Structure (Part A, items 1–5) | 25% | Every input value present; model architecture fully defined; no gaps the executor must fill |
| Model Specification — Ratios & Validation (Part A, items 6–7) | 25% | All 25+ ratios specified with correct formulas in named-range notation; validation rules complete |
| Analysis Specification (Part B, items 8–11) | 25% | Clear interpretive guidance; meaningful benchmarks; actionable recommendation criteria; output format fully defined |
| Spec Craft & Clarity | 25% | Unambiguous language; logical organization; a competent executor could follow this without asking questions |

---

### Stage 5: LLM Analysis & Executive Evaluation (20% of project)

**What:** Execute the Stage 4 specification with an LLM. Receive the AI-generated analysis. Then — critically — evaluate, correct, and annotate the output. Submit the raw LLM output, the student's evaluated final version, and a reflection on what the spec got right and wrong.

**Why this is the capstone:** The future of finance work is not "do the analysis" or "make the AI do the analysis." It's "specify the work, evaluate the output, and take responsibility for the final product." This stage tests judgment — and closes the spec-driven design feedback loop. Where the LLM output diverges from the student's own Stage 3 analysis, either the spec had a gap or the student's manual work had an error. Either way, the student learns.

**Collaboration model:** Individual. Each student runs their own spec and writes their own evaluation. All Stage 5 outputs go to `deliverables/`.

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

**Rubric (% of Stage 5 score):**

| Criterion | % |
|-----------|---|
| Quality of LLM Output (reflects spec quality) | 25% |
| Ratio Interpretation & Accuracy | 25% |
| Critical Evaluation & Spec Retrospective | 25% |
| Strategic Recommendations & Executive Voice | 25% |

---

## Findings — Stage Comparison

### BUS-314 (Undergrad) vs. BUS-629 (EMBA)

| Dimension | BUS-314 (Undergrad) | BUS-629 (EMBA) |
|-----------|---------|---------|
| Infrastructure | Instructor-managed repo | Students build their own repos (Stage 0) |
| Template | Provided (progressive reveal) | Built from scratch |
| Company | Pre-selected scenarios | Student's choice (incl. non-U.S./ASEAN) |
| Stage order | Memo → Build → Spec → Final | Setup → Build → Memo → Populate → Spec → LLM Eval |
| Spec role | Post-build reflection | Central artifact; fully defines model + analysis |
| Spec scope | Analysis and prompt only | Model architecture + data + formulas + analysis + output format |
| Validation | Instructor-side checks | Student self-audit (dedicated stage) |
| AI role | Student writes prompt as component of final | LLM executes the spec; student evaluates |
| Capstone skill | Prompt engineering | Spec-driven design + critical evaluation |
| Feedback loop | None (prompt not tested) | Spec → LLM → Retrospective (closed loop) |
| International scope | U.S. companies only | U.S., Vietnamese, and ASEAN companies |

### The Spec-Driven Design Arc

```
Stage 0         Stage 1          Stage 2         Stage 3              Stage 4                Stage 5
Set up the   →  Build the     →  Frame the    →  Populate &        →  Write the           →  Execute &
workspace       container        analysis         validate              specification          Evaluate

INFRASTRUCTURE   TACIT KNOWLEDGE ACQUISITION                         KNOWLEDGE EXTERNALIZATION
                 (learn by doing)                                    (prove mastery by specifying)

"We organized   "I built it"    "I chose why"   "I verified it"      "I can specify        "I can judge
 the workspace"                                                       the model AND          the output"
                                                                      the analysis"
```

The spec (Stage 4) is the **bridge** between domain expertise and delegation. Everything before it builds the knowledge; everything after it tests whether that knowledge was captured precisely enough to be actionable. The spec must define the complete model (not just the analysis) because specifying a model's architecture, data flow, and formula logic is a fundamentally different skill than specifying what to do with the results.

---

## Implications

### Pedagogical

- **Stage 0** builds professional infrastructure skills and removes tooling barriers before analytical work begins
- **Stages 1–3** build tacit knowledge through hands-on modeling, company selection, and self-audit
- **Stage 4** externalizes that knowledge into a formal specification — the hardest cognitive step, now encompassing both the model and the analysis
- **Stage 5** closes the feedback loop: spec quality is tested empirically, not just graded abstractly
- **Self-audit in Stage 3** is deliberately positioned before spec writing to ensure students have deep model familiarity before they attempt to specify the work for someone else

### Operational

- **No Excel templates to maintain** — Students build from scratch, reducing instructor prep
- **Company diversity** — Each student analyzes a different company, reducing plagiarism risk and enriching class discussion
- **LLM-agnostic** — Students can use any capable LLM (Claude, ChatGPT, Gemini, Copilot, etc.)
- **Grading efficiency** — The spec (Stage 4) is the highest-signal artifact for assessing understanding; instructors can focus grading effort there
- **Repo structure carries forward** — Students can reuse the Stage 0 repository structure for other course projects
- **Living example** — The course repo itself uses the same structure, so students always have a reference

### Vietnam EMBA Context

- **Non-U.S. companies explicitly welcomed.** Many EMBA students work at Vietnamese or ASEAN-listed companies. Analyzing their own employer or a regional competitor increases engagement and career relevance.
- **Minimum data requirements for non-SEC filers:** Audited annual report with Balance Sheet, Income Statement, and Cash Flow Statement. English-language financials preferred; if financials are in Vietnamese, all deliverables and the spec must be in English. Students should note the reporting standard (IFRS, VAS, local GAAP) and flag any material differences from U.S. GAAP that affect ratio interpretation (e.g., VAS treatment of revaluation reserves, IFRS 16 lease capitalization).
- **Currency:** All ratio inputs should be in the company's reporting currency. If the student's company reports in VND, ratios are computed in VND. The spec should note the currency and any exchange rate context relevant to interpretation.
- **Time zone and schedule:** Stages should have sufficient buffer between deadlines to accommodate working professionals.

---

## Collaboration Model

### Default: Individual

All stages are completed individually. Each student creates their own GitHub repository (Stage 0) and completes all analytical stages (1–5) independently. This ensures every student builds personal mastery of the full pipeline — from infrastructure setup through spec writing and LLM evaluation.

### Exploration: Team Variant

For future offerings, a team-based variant could add value. Here is how it might work:

**Team composition:** 2–3 students per team. Larger teams dilute individual learning.

| Stage | Individual or Team | Rationale |
|-------|-------------------|-----------|
| 0 — Repo Setup | **Team** | Shared infrastructure; collaborative setup mirrors how IB teams organize shared workspaces. Each member still makes commits. |
| 1 — Template Architecture | **Individual** | Every student must build model intuition. This cannot be delegated within a team without loss. |
| 2 — Company Selection Memo | **Team** | Team selects one company together. Each member writes a section of the memo. Joint accountability for company choice. |
| 3 — Model Population & Validation | **Team with individual accountability** | Team populates one shared workbook, but each member owns specific ratio categories and must sign off on their section's validation. Peer cross-check replaces solo self-audit. |
| 4 — Technical Specification | **Team** | Collaborative spec writing mirrors real-world delegation briefs written by teams. Assign sections by expertise. Enforce internal review (each section reviewed by a member who didn't write it). |
| 5 — LLM Evaluation | **Individual** | Each team member independently evaluates the LLM output and writes their own executive evaluation. This prevents free-riding and ensures every student demonstrates judgment. |

**Key risk:** Stage 1 must remain individual — otherwise some students never internalize the model architecture. Stage 5 must also remain individual — otherwise the evaluation section becomes groupthink.

**Peer review add-on (works with either model):** After Stage 3, students swap workbooks with a classmate for a blind peer review. The reviewer completes a structured checklist (similar to Stage 3's self-audit) and writes a 150-word review note. This teaches model review skills and could be implemented as a lightweight sub-stage (Stage 3b) without adding a full new stage.

### Recommendation

Start with **individual work** for the first cohort. Introduce the **peer review add-on** (Stage 3b) if class size and schedule permit. Consider the **team variant** for subsequent cohorts after evaluating how the individual model performs.

---

## Future Considerations — Extra Credit & Extensions

No formal extra credit structure for v1. The following ideas are worth developing for future iterations or as instructor-optional additions:

### EMBA-Relevant Extensions

1. **IFRS vs. U.S. GAAP Reconciliation** — For students analyzing non-U.S. companies: identify 3–5 material differences in accounting treatment and quantify the impact on key ratios. High relevance for Vietnamese students working with VAS/IFRS.

2. **Cross-Border Competitor Comparison** — Compare the student's company against a competitor in a different country/reporting jurisdiction. Requires normalizing for accounting standard differences. Teaches what's comparable and what isn't.

3. **Multi-Year Trend Analysis** — Extend the model to 3–5 years. Identify inflection points. More meaningful for companies that have undergone strategic shifts (M&A, market entry, restructuring).

4. **Industry Panel Presentation** — Teams of 3–4 students who analyzed companies in the same industry present a panel discussion. Each presents their company's ratios, then the panel discusses industry-level patterns. Builds presentation and synthesis skills.

5. **Spec Iteration** — After Stage 5, revise the Stage 4 spec based on retrospective findings. Re-run with the LLM. Compare output quality between v1 and v2. Demonstrates iterative improvement — the core of spec-driven design.

6. **Automated Model Generation** — Use the spec to have an LLM generate the Excel workbook itself (via Claude Code, Python + openpyxl, or similar). Compare the auto-generated model to the student's Stage 3 model. Tests whether the spec is precise enough to produce not just analysis but the model itself.

7. **Peer Spec Exchange** — Two students swap Stage 4 specs (without swapping Stage 3 models). Each runs the other's spec through an LLM and evaluates the output. Provides an external test of spec clarity — if a classmate's LLM can't execute your spec correctly, the spec needs work.

---

## Limitations & Next Steps

### Remaining Decisions

1. **Timeline** — Define stage deadlines relative to the Vietnam EMBA course schedule
2. **LLM guidance** — Provide tips for Claude, ChatGPT, and Gemini? Or keep LLM-agnostic with general best practices?
3. **Peer review implementation** — If Stage 3b peer review is adopted, define the matching process and checklist
4. **Presentation component** — Should Stage 5 include a live defense or presentation of findings? Consider time constraints for working EMBA professionals.
5. **Ratio list adjustments** — Are all 25+ BUS-314 ratios appropriate at the MBA level, or should the list be expanded (e.g., ROIC, free cash flow yield, Altman Z-score)?
6. **Stage 0 logistics** — In-class lab session vs. asynchronous setup? Git GUI (GitHub Desktop) vs. command line?

### Next Steps

- [ ] Finalize this memo (incorporate feedback)
- [ ] Create Stage 1 best-practices one-pager and ratio category reference sheet
- [ ] Write stage assignment files (`stage0-repo-setup.md` through `stage5-llm-evaluation.md`)
- [ ] Adapt company selection guide for international / non-U.S. / ASEAN companies
- [ ] Update BUS-629 course `README.md` with project overview and timeline
- [ ] Update `CLAUDE.md` to reflect BUS-629 project structure and conventions

---

## References

- BUS-314 Accounting Ratios Project — `courses/BUS-314-International-Corporate-Finance/accounting-ratios/`
- BUS-314 Stage Restructure Decision — `docs/decisions/2026-02-24-bus314-stage-restructure.md`
- BUS-314 Accounting Ratios Skill — `.claude/skills/bus314-accounting-ratios/SKILL.md`
- BUS-629 Memo Template — `courses/BUS-629-VEMBA-International-Corporate-Finance/docs/templates/memo-template.md`
- BUS-629 Spec Template — `courses/BUS-629-VEMBA-International-Corporate-Finance/docs/templates/spec-template.md`
- BUS-629 Living Example (directory structure) — `courses/BUS-629-VEMBA-International-Corporate-Finance/`
