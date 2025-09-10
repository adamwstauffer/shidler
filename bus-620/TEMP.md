# BUS-620 Micro/Macro Economics

**Theme:** Policy shock analysis (price controls, tax/subsidy, or monetary/ fiscal impulse)
**Output style:** Executive policy memo + reproducible appendix

### A.1 Workflow (README ➜ Prompts ➜ Spec)

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

* **Phase 1 – Scoping (Week 1):** 1-page proposal + baseline diagram.
* **Phase 2 – Analysis (Weeks 2–3):** Calculations (incidence, DWL), short-run vs long-run narrative.
* **Phase 3 – Robustness (Week 4):** Elasticity sensitivity table; alternate assumptions.
* **Phase 4 – Memo & Appendix (Week 5):** Final memo + reproducible steps + prompt log.

### A.3 Rubric (10 pts)

* Correct use of theory (3), clarity & structure (2), quantitative accuracy (2), diagrams (1), reproducibility + prompts (2).

---

# 2) Project B — International Economics (Trade & Tariffs)

**Theme:** Real dispute or policy (tariff, quota, VER, TBT/SPS) and general-equilibrium intuition
**Output style:** Trade case brief with model-backed winner/loser analysis

### B.1 Workflow (README ➜ Prompts ➜ Spec)

* **README**

  * Pick a case (e.g., steel tariffs, USMCA rule-of-origin, Airbus-Boeing dispute).
  * Map factors → comparative advantage → expected trade pattern → policy shock.
  * Deliverables + rubric + citation format.
* **Prompts**

  * “Summarize case X in 200 words with neutral language and cite primary sources.”
  * “Given factor endowments, infer HO predictions and who gains/loses under a tariff.”
  * “Draft a pxp trade-flow diagram narrative I can recreate.”
* **Spec**

  * **Models:** Ricardian (unit labor req), Heckscher-Ohlin (factor abundance), Specific-Factors for distribution.
  * **Empirics:** Use at least one trade flow or tariff dataset; document sources.
  * **Outputs:** 2–3 page brief, graphic of trade-flow shift, distributional table (consumers, producers, govt).

### B.2 Phases & Deliverables

* **Phase 1 – Case Selection & Background:** 1-page summary + citations.
* **Phase 2 – Model Fit:** Which model explains the case and why?
* **Phase 3 – Distribution & Welfare:** Winners/losers table; deadweight loss + tariff revenue bounds.
* **Phase 4 – Policy Recommendation:** Memo with alternatives (e.g., wage insurance, phasedown).

### B.3 Rubric (10 pts)

* Model selection/justification (3), data use & citations (2), distribution analysis (2), clarity (2), AI prompts (1).

---

# 3) Project C — International Finance (FX & Derivatives)

**Theme:** FX risk management for a small multinational (exporter or importer)
**Output style:** Risk memo + hedge playbook + calculation sheet

### C.1 Workflow (README ➜ Prompts ➜ Spec)

* **README**

  * Choose a currency pair (e.g., USD/EUR). Define exposure (AR/AP, timing, size).
  * Required: spot/forward parity check, scenario analysis, hedge alternatives (forward, option collar).
* **Prompts**

  * “Compute forward rate via CIP given S, r\_d, r\_f (show formula path).”
  * “Stress scenarios: ±5%, ±10% FX; tabulate P\&L unhedged vs forward vs collar.”
  * “Draft hedge rationale in manager-friendly prose; add risks & monitoring checklist.”
* **Spec**

  * **Methods:** Interest parity, forward pricing, option payoff tables (if chosen).
  * **Artifacts:** Spreadsheet/notebook with formulas, memo, prompt log.
  * **Governance:** Hedge objective, limits, rebalancing triggers, reporting cadence.

### C.2 Phases & Deliverables

* **Phase 1 – Exposure Map:** Cash-flow timing, currency, sizing (timeline).
* **Phase 2 – Valuation & Parity:** Forward calc; sanity-check with market quotes (document date).
* **Phase 3 – Strategy Set:** Compare hedge P\&L across scenarios; choose & justify.
* **Phase 4 – Memo + Playbook:** Final memo + XLS/CSV + prompt log.

### C.3 Rubric (10 pts)

* Correct finance math (3), scenario quality (2), hedge selection logic (3), clarity (1), AI prompts (1).

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

* **`intl-econ/README.md`**

```md
# Project B — International Trade & Tariffs
Select a real dispute/policy and analyze using Ricardian/HO/Specific-Factors.
**Deliverables:** case brief + winners/losers table + figures + prompt log.
```

* **`intl-finance/README.md`**

```md
# Project C — International Finance (FX & Derivatives)
Map your firm’s FX exposure, compute forward via parity, compare hedges.
**Deliverables:** risk memo, `analysis/fx-hedge.xlsx`, prompt log, figures.
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

