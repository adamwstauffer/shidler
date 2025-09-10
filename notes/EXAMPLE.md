### A.1 Workflow Example (README ➜ Prompts ➜ Spec)

* **README (student-facing brief)**

  * Problem choices (pick one):
    1. Rent control in a metro market; 2) Sugar tax; 3) Expansionary monetary policy with sticky prices.
     * Required analyses: equilibrium shifts, elasticity, DWL, incidence, short-run vs long-run.
     * Deliverables + due dates, grading rubric, collaboration rules.

* **Prompts (AI use, reproducible)**
  * “Explain the causal chain from policy → incentives → market outcomes using supply/demand.”
  * “Check my DWL calculation with step-by-step reasoning; flag any missing elasticity assumptions.”
  * “Generate a clean diagram description I can recreate (axes, intercepts, shifts, labels).”
 
* **Spec (scope + criteria)**

  * **Models:** Partial equilibrium S/D, tax incidence, simple AS-AD, Phillips tradeoff (optional).
  * **Data:** 1 public dataset or simulated data (justify).
  * **Outputs:** 2–3 page memo (no identity info), 1-page technical appendix (math + chart), prompt log.

### A.2 Phases & Deliverables

* **Phase 1 – Scoping (Weeks 1-4):** 1-page proposal + baseline diagram.
* **Phase 2 – Analysis (Weeks 4–7):** Calculations (incidence, DWL), short-run vs long-run narrative.
* **Phase 3 – Robustness (Weeks 7-10):** Elasticity sensitivity table; alternate assumptions.
* **Phase 4 – Memo & Appendix (Weeks 10-13):** Final memo + reproducible steps + prompt log.

---

# GitHub Starter Repository (students fork this)

```text
bus-620-projects/
├─ README.md                          # Master overview: how to use repo, AI policy, honor code
├─ .gitignore                         # Node, Python, OS cruft, notebooks checkpoints
├─ .gitattributes                     # Normalize line endings; optional LFS hooks
├─ LICENSE
├─ docs/
│  ├─ ai-usage-guidelines.md          # Allowed uses, prompt logging, citation rules
│  ├─ writing-style-guide.md          # Memo format, charts, footnotes, figures
│  ├─ data-sourcing-checklist.md      # How to find, cite, and sanity-check data
│  └─ reproducibility-playbook.md     # “Run it again” rules (versions, seeds, exports)
├─ .github/
│  ├─ ISSUE_TEMPLATE.md               # Use for peer review comments
│  └─ PULL_REQUEST_TEMPLATE.md        # Checklist: rubric, prompt log, reproducibility
├─ _templates/
│  ├─ report-memo-template.md         # 2–3 page memo skeleton (cover, exec summary, findings)
│  ├─ prompt-log-template.md          # Table: goal | prompt | tool | output link | notes
│  ├─ spec-template.md                # Scope, models, data, acceptance criteria
│  ├─ figure-caption-template.md
│  └─ spreadsheet-starter.xlsx        # Basic calc tabs + example formulas
├─ common/
│  ├─ prompts/
│  │  ├─ diagram-prompts.md
│  │  ├─ critique-prompts.md
│  │  └─ data-cleaning-prompts.md
│  └─ utils/
│     └─ README.md                    # (optional) Python/Colab tips; no code required
├─ micro-macro/
│  ├─ README.md                       # Project A brief (student-facing)
│  ├─ prompts.md                      # Curated prompts for Micro/Macro
│  ├─ spec.md                         # Formal acceptance criteria
│  ├─ data/                           # Put datasets here (or links)
│  ├─ figures/                        # Export final charts here (PNG/SVG)
│  ├─ analysis/                       # XLS/CSV or notebook; formulas documented
│  └─ deliverables/
│     ├─ memo.md
│     └─ prompt-log.md
├─ intl-econ/
│  ├─ README.md
│  ├─ prompts.md
│  ├─ spec.md
│  ├─ data/
│  ├─ figures/
│  ├─ analysis/
│  └─ deliverables/
│     ├─ case-brief.md
│     └─ prompt-log.md
└─ intl-finance/
   ├─ README.md
   ├─ prompts.md
   ├─ spec.md
   ├─ data/
   ├─ figures/
   ├─ analysis/
   │  └─ fx-hedge.xlsx                # Forward calc + scenarios (students edit/duplicate)
   └─ deliverables/
      ├─ risk-memo.md
      └─ prompt-log.md
```

## Starter file contents (copy/paste)

**`README.md` (root)**

```md
# Economics + AI Course Projects

This repo hosts three separate projects for three courses:
- `micro-macro/` — Policy shock analysis (memo + appendix)
- `intl-econ/` — Trade/tariff case brief (welfare + distribution)
- `intl-finance/` — FX risk & hedging memo

## Workflow
1) Read the course folder `README.md`  
2) Draft your `spec.md` from `_templates/spec-template.md`  
3) Use `prompts.md` to guide AI assistance; record every prompt in `deliverables/prompt-log.md`  
4) Build your analysis in `analysis/` and export final figures to `figures/`  
5) Write the final memo in `deliverables/`

### Reproducibility & AI Policy
- Log prompts, cite data, and keep a clear chain from assumptions → results.
- AI may help draft, critique, and check math; **you** are responsible for correctness.
```

**`_templates/spec-template.md`**

```md
# Project Spec
- **Problem / Case:** 
- **Models to apply (micro/macro or trade or FX):**
- **Data sources (links + access date):**
- **Key calculations / diagrams:**
- **Success criteria (acceptance tests):**
  - [ ] Theory is correctly applied
  - [ ] Quant methods are transparent and reproducible
  - [ ] Figures match text; units & labels clear
  - [ ] Limitations & robustness discussed
- **Deliverables & deadlines:**
```

**`_templates/prompt-log-template.md`**

```md
| Date | Goal | Exact Prompt | Tool (LLM/Sheet/Code) | Output Link/Location | Notes & Actions |
|------|------|--------------|------------------------|----------------------|-----------------|
```

**`_templates/report-memo-template.md`**

```md
# Title
**Executive Summary (≤150 words)**

## Background
## Method (models, assumptions)
## Findings (tables/figures referenced)
## Policy/Managerial Implications
## Limitations & Next Steps
## References (data & sources)
```

**Course-specific `README.md` stubs**

* **`micro-macro/README.md`**

```md
# Project A — Micro/Macro Policy Shock
Choose one: rent control, sugar tax, or expansionary monetary policy.
**Deliverables:** `deliverables/memo.md`, `deliverables/prompt-log.md`, figures, analysis file.

Use `prompts.md` for suggested AI queries; log them all.
Rubric: theory (3), clarity (2), quant (2), diagrams (1), reproducibility (2).
```


**Course `prompts.md` seeds** (one example each)

* **Micro/Macro**

```md
- Check DWL: “Given P*, Q*, tax t, and elasticities (Es, Ed), verify DWL triangle area and who bears incidence.”
- Robustness: “Vary demand elasticity from 0.5 to 2.0 and summarize incidence/DWL shifts in a 6-row table.”
```

* **International Econ**

```md
- Model fit: “Given country A (K-abundant) and B (L-abundant), predict sectoral winners/losers under tariff τ on capital-intensive good.”
- Evidence: “List 3 credible sources for trade flows and applied tariffs for case X with access instructions.”
```

* **International Finance**

```md
- Forward pricing: “Compute 3-month F = S*(1+r_d*T)/(1+r_f*T). Show steps and round to 4 decimals.”
- Hedge compare: “Make a table of unhedged vs forward vs collar P&L for ±5/±10% spot moves.”
```

---

## How students use it (quick start)

```bash
# 1) Fork → Clone
git clone <their fork>

# 2) Pick course folder; copy templates
cp _templates/spec-template.md micro-macro/spec.md
cp _templates/prompt-log-template.md micro-macro/deliverables/prompt-log.md
cp _templates/report-memo-template.md micro-macro/deliverables/memo.md

# 3) Create a new branch for each milestone
git checkout -b phase-1-scoping
git add .
git commit -m "Phase 1 spec + initial diagram plan"
git push -u origin phase-1-scoping
# Open PR for instructor/peer feedback
```

---

## Instructor knobs (easy modifications)

* **Tight/loose AI policy:** Edit `docs/ai-usage-guidelines.md` to allow/exclude drafting vs only critique.
* **Rubrics:** Keep short in `README.md` but include detailed version in each `spec.md`.
* **Milestones:** Add dates at the top of each course `README.md`.
* **Peer review:** Require one PR review & one issue filed per student.
* **Repro:** Require “Run Sheet” at the end of each memo describing exactly how to recreate figures.

