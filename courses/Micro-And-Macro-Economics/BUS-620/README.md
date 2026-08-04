# BUS 620: Micro- and Macro-Economic Foundations for Managers

**Shidler College of Business, University of Hawaiʻi at Mānoa**

**Course tutorials:** [Micro & Macro Economics on Kumu](https://adamwstauffer.github.io/ai-lms/micro-and-macro-economics.html) — the stage-by-stage tutorials, labs, and reference pages this course's projects assume. Kumu is organized by subject and carries no course codes; this README is the signpost from the code to the material.

## Course Overview

This MBA-level course provides a comprehensive exploration of microeconomic and macroeconomic theories and their application to real-world business and policy challenges. Emphasis is placed on the intersection of economics, geopolitics, and global stability.

## Instructor

**Adam W. Stauffer** | [adamstau@hawaii.edu](mailto:adamstau@hawaii.edu)

Please begin email subject lines with **BUS 620**. For more information about the instructor, see [BIO.md](../../../BIO.md).

---

## Learning Objectives

### Foundational Principles

* Elasticity, market structures, efficiency, externalities, and strategic behavior

### Global Environment

* Interconnectedness of economies, trade, fiscal/monetary policy, and financial markets

### Geopolitics

* How climate change, conflict, and resource control affect economic stability

### Managerial Application

* Team-based projects and case studies that apply economic reasoning to real business decisions

### Global Peace & Stability

* Explore how interdependence, trade, and cooperation can mitigate or exacerbate international conflict

By the end of the course, you will be able to integrate economic frameworks with geopolitical awareness to support effective managerial decision-making.

---

## Course Outline

The course opens with economic fundamentals (thinking like an economist, supply and demand). It progresses through microeconomic foundations (market structures, efficiency, strategic behavior, and externalities) while integrating geopolitical case studies. The latter half covers macroeconomics (national accounting, growth, labor markets, monetary and fiscal policy) with emphasis on how economic policies affect global stability, international trade, and resource conflicts. Throughout, case studies and team projects ground theory in real-world business and policy challenges.

---

## Skills Gained

Through the AI + GitHub project, you will also develop practical, workplace-ready skills:

* **AI Literacy & Prompt Engineering:** Design effective AI prompts for research, analysis, drafting, and critique, while evaluating limitations and biases
* **Reproducible Research Practices:** Maintain transparent AI Prompt Logs, ensuring accountability and reproducibility in analysis
* **GitHub Collaboration & Version Control:** Proficiency with GitHub for project management, version control, and collaborative workflows (branching, pull requests, peer review)
* **Data Analysis & Visualization:** Use AI and economic/finance models to generate tables, figures, and scenario analyses
* **Professional Report Writing:** Produce structured policy memos, case briefs, or risk management reports that integrate quantitative analysis with narrative clarity

---

## Grading (Fall 2026)

> **Status:** restructured 2026-07-31 for the Fall 2026 launch — three graded case-study projects
> added, project weights rebalanced. Revised 2026-08-02: the individual 30% is a **geopolitical
> research paper**, not the Policy Shock Analysis (deferred), and all case artifacts move to the
> portfolio-repo standard. Case 1 materials are released; Cases 2-3 remain Kumu-improved drafts
> pending instructor sign-off before release to students.

| Component | Weight |
|-----------|--------|
| Attendance & Participation | 10% |
| Case 1 — Perfect Competition: Decision Analysis (weeks 1–2) | 10% |
| Case 2 — Imperfect Competition: Pricing Power Analysis (weeks 3–4) | 10% |
| Case 3 — Economic Profit & Rent: Earnings Analysis (weeks 5–6) | 10% |
| Individual Project — Geopolitical Research Paper | 30% |
| Team Case Study Presentation | 30% |
| **Total** | **100%** |

### Attendance & Participation (10%)

Essential for maximizing learning outcomes. Each case opens with an in-class working session —
showing up and committing is participating.

### Case-Study Projects (3 × 10%)

Three 2-week Excel + AI engagements, each worth 20 points split across 2–3 graded stages. One
**personal public GitHub portfolio repo**, created in Case 1's first stage, accretes all term. It is
structured by **capability** and **engagement**, not by course — the full standard is in
`ai-lms/docs/decisions/2026-08-02-website-simplification-and-portfolio-repo-standard.md` § 6. Each
case adds a capability folder plus its evidence:

| Stage | Deliverable path in the student repo |
|---|---|
| 1 — Brief | `docs/briefs/<case-slug>-brief.md` (+ Case 1 only: repo skeleton, `AGENTS.md`, `CLAUDE.md`, `RESUME.md`, `prompt-log.md`, collaborator `adamwstauffer`) |
| 2 — Build | `skills/<capability>/spec.md` + `skills/<capability>/model.xlsx` + skill `README.md` |
| 3 — Report | `analysis/<case-slug>-analysis.md` + `analysis/figures/` + `docs/decisions/<case-slug>-memo.md` + prompt-log update |

Check figures are published so students can self-verify before submitting. The three cases trace one
arc — competition → market power → where the profits hide:

1. **Perfect Competition — Decision Analysis** (market-garden scenario): P = MC, Excel Solver.
   Capability `marginal-analysis`, engagement `perfect-competition`
   ([case + stage briefs](../projects/in-progress/perfect-competition-marginal-costs/))
2. **Imperfect Competition — Pricing Power Analysis** (Monsanto GMO seed scenario): monopoly,
   MR = MC, Lerner, deadweight loss. Capability `pricing-power`, engagement `imperfect-competition`
   ([case + stage briefs](../projects/in-progress/imperfect-competition-marginal-revenue/))
3. **Economic Profit & Rent — Earnings Analysis** (ride-share scenario): accounting vs economic
   profit, economic rent, medallion capitalization. Capability `economic-profit`, engagement
   `economic-profit` ([case + stage briefs](../projects/in-progress/accounting-profit-economic-profit-economic-rent/))

> **Sync rule.** These paths are mirrored by the Kumu website's stage pages and by its progression
> gates (`ai-lms/website/assets/js/gates.js`). One path table, three consumers — change one, change
> all three. Any future `grade_stage*.py` scanners read from the same table.

### Individual Project — Geopolitical Research Paper (30%)

An individual research paper on a geopolitical question with real economic stakes — resource
control, trade restriction, conflict, sanctions, climate policy — of your own choosing. Analyze who
wins, who loses, by how much, and what the economics predicts about stability. Structure,
formatting, length, and submission are on the course syllabus and Lamaku; this project is **not**
run through the Kumu website or the portfolio repo.

Peer evaluation accounts for 50% of the grade. The Case 2 pricing-power analysis is the deliberate
on-ramp: its welfare-loss and policy framing is the muscle this paper uses at full scale.

> **Deferred:** the *Policy Shock Analysis* previously occupying this 30% is parked, not cancelled —
> its materials remain in [`../projects/individual-research/`](../projects/individual-research/) and
> its Kumu page is retained but delinked. Restoring it in a future term is a one-line change.

### Team Case Study Presentation (30%)

Teams are assigned by the instructor and present applied cases on geopolitical challenges — AI and
labour markets, climate policy, trade and supply chains, global markets. The engagement is
**presentation-first: there is no team workbook and no separate memo.** The deck carries the
recommendation on its closing slide(s), and it is built spec-driven like every other artifact in
this course — the team commits a ten-slide content map and a `design.json` visual spec, hands both
to AI, and audits the result. The stated learning objective is **collaborative work in a shared
repository**: branches and pull requests, not email attachments. The team repo is named for the
team, hosted on one member's account with all members plus the instructor as collaborators, and
uses the same hierarchy as the personal portfolio repo. Presentation runs about 10–15 minutes plus
a 10-minute moderated discussion the team leads; peer review is collected through a structured
survey.
Presentations are peer-reviewed, with 50% of the grade based on peer evaluation.

> **Relocated here 2026-08-03** from `../projects/team-research/README.md` under the standing rule
> that calendars live only in offering-level artifacts. The prior (Fall 2025) offering ran
> presentations on 2025-12-10 with peer-review feedback due 2025-12-12; the Fall 2026 equivalents
> slot into weeks 12–15 on the calendar below. The older evaluation split that brief carried
> (peer 32.5% / instructor 32.5% / timing 25% / peer participation 10%) was **stale and has been
> removed** from the project brief — the 50/50 peer/instructor split stated above governs, and
> percentage splits are offering-owned in any case.

> **Also relocated here 2026-08-03:** the individual research paper's prior (Fall 2025) deadlines —
> paper due 2025-12-03, peer review due 2025-12-17. Fall 2026 equivalents slot into weeks 7–11 on
> the calendar below.

---

## Fall 2026 Term Calendar (draft)

Instruction runs **2026-08-24 → 2026-12-10**; finals week 2026-12-14–18. Stage due dates below say
"end of week" — exact dates will be slotted to class meeting days on the syllabus.

| Weeks | Dates | What's running |
|---|---|---|
| 1–2 | Aug 24 – Sep 4 | **Case 1 — Perfect Competition** (stage 1 repo + brief, 2 build, 3 analysis) |
| 3–4 | Sep 8 – Sep 18 | **Case 2 — Imperfect Competition** (stage 1 build, 2 analysis) · Labor Day Sep 7 |
| 5–6 | Sep 21 – Oct 2 | **Case 3 — Economic Profit & Rent** (stage 1 build, 2 analysis) |
| 7–11 | Oct 5 – Nov 6 | **Geopolitical research paper** (proposal → draft → final) · macro units |
| 12–15 | Nov 9 – Dec 10 | **Team case studies** (repo build → presentations) · Thanksgiving Nov 26–27 |
| 16 | Dec 14–18 | Finals week — peer-review wrap-up |

---

## AI Use Policy

MBA students are encouraged to explore AI tools to enhance learning and professional decision-making. Acceptable uses include:

* Knowledge Enhancement: Use AI to clarify theory or extend readings
* Research Support: Gather data, statistics, and examples for assignments
* Critical Thinking: Test your arguments against counterarguments generated by AI
* Problem-Solving: Simulate case scenarios and brainstorm managerial responses
* Professional Skills: Practice clear, concise communication in prompts and outputs

Requirements:
* Log all AI use in the Prompt Log
* Verify outputs against trusted sources
* Treat AI as a supplement — not a substitute — for your own analysis

---

## Campus Policies

**Students with Disabilities:** Contact the KOKUA Program (Student Services Center, Room 13; 956-7511; http://www.hawaii.edu/kokua/).

**Academic Honesty:** UH Mānoa enforces strict rules on plagiarism and cheating. See: http://www.hawaii.edu/student/conduct.

---

## Directory Contents

```
BUS-620/
└── README.md   this file
```

Shared curriculum (individual research, team research, in-development case studies) lives in [`../projects/`](../projects/).
