# Shidler College of Business — Course & Portfolio Hub

Unified repository for course materials, project frameworks, branded assets, and professional portfolio documents for courses taught by **Adam W. Stauffer** at the University of Hawai&#x02BB;i at M&#x0101;noa Shidler College of Business.

Everything lives in one Git-tracked repo so students, collaborators, and reviewers can find syllabi, assignment specs, templates, and decision memos in a single place.

---

## Repository Structure

```
shidler/
├── BIO.md                          # Instructor biography (single source of truth)
├── CV.md                           # Curriculum vitae
├── RESUME.md                       # One-page resume
├── CLAUDE.md                       # AI assistant configuration for this repo
│
├── courses/                        # Subject-first directories (see courses/README.md for the code map)
│   ├── International-Corporate-Finance/    # BUS 314 (inactive), BUS 629
│   ├── International-Finance-And-Securities/  # FIN 321
│   ├── International-Economics-And-Trade/  # BUS 313
│   ├── Micro-And-Macro-Economics/          # BUS 620, BUS 620 DLEMBA
│   └── Sustainable-Agriculture-Entrepreneurship/  # BUS 122B
│       └── BUS-122B/
│
├── docs/
│   ├── _branding/                  # UH Manoa design system & templates
│   ├── decisions/                  # Strategic decision memos
│   ├── presentations/              # Course-agnostic appendix slide decks
│   ├── templates/                  # Reusable deliverable templates
│   ├── ai-usage-guidelines.md
│   ├── writing-style-guide.md
│   └── reproducibility-playbook.md
│
├── _archive/                       # Deprecated/historical materials (incl. bus314/, the archived BUS-314 project)
├── notes/                          # Personal research notes
└── scripts/                        # Utility scripts
```

---

## Active Courses

| Code | Subject | Level | Key Project |
|------|-------|-------|-------------|
| BUS 313 | International Economics and Trade | Undergrad | Trade/geopolitics case studies |
| BUS 314 | International Corporate Finance | Undergrad (inactive) | Performance ratios — superseded by BUS 629's project design; see `courses/International-Corporate-Finance/BUS-314/` |
| FIN 321 | International Finance and Securities | Upper undergrad | FX hedging (5-stage) |
| BUS 620 | Micro- and Macro-Economics | Masters — MBA | Team cases + individual research |
| BUS 620 DLEMBA | Micro- and Macro-Economics | Masters — DLEMBA | In setup |
| BUS 122B | Sustainable Agriculture Entrepreneurship | Community college | Business plan + pitch |
| BUS 629 | International Corporate Finance | Masters — VEMBA | Performance ratios (6-stage, spec-driven) |

See [`courses/README.md`](courses/README.md) for the full code-to-directory map. Each subject directory contains a `projects/` folder with shared curriculum and one subfolder per offering with its syllabus, roster, and course-specific decision memos.

### Vietnam EMBA Campus Locations

BUS 629 is delivered in person at two locations as part of the Shidler Vietnam Executive MBA program:

| City | Venue | Address |
|------|-------|---------|
| **Ho Chi Minh City** | Van Lang University, Building I, Level 2, Room I2.01 | 69/68 Đặng Thùy Trâm, Ward 13, Bình Thạnh District, HCMC |
| **Hanoi** | FPT Headquarters | 10 Phạm Văn Bạch street, Cầu Giấy District, Hanoi |

---

## Appendix Presentations

Two course-agnostic slide decks live in `docs/presentations/`. Attach them to any course project:

| File | What It Covers |
|------|---------------|
| **GitHub_AI_Appendix.pptx** | Creating a GitHub account, installing Git, the add-commit-push workflow, GitHub Desktop, using ChatGPT and Claude for projects, prompt patterns, and a cheat sheet |
| **Claude_Appendix.pptx** | Claude on the web and desktop, file uploads, artifacts, Projects, Claude Code (CLI) installation and workflow, skills & /commands, and the UH design system |

---

## Documentation Hub (`docs/`)

### Branding (`docs/_branding/`)

The UH M&#x0101;noa design system is stored as two complementary files:

- **`design.json`** — Machine-readable design tokens (colors, typography, spacing, components). Claude and other tools read this file to apply institutional branding automatically.
- **`design-system.html`** — Human-readable visual reference. Open in a browser to review the full color palette, typography scale, and component examples.

PowerPoint templates (`.potx`, `.pptx`) live in `docs/_branding/templates/`.

### Templates (`docs/templates/`)

Reusable Markdown templates for common deliverables: executive memo, technical spec, case brief, risk memo, prompt log, and bio/resume formats.

### Decision Memos (`docs/decisions/`)

Lightweight memos capturing strategic decisions about repo structure, course design, and project architecture.

---

## Project Workflow

Most projects follow a staged pedagogical pattern:

1. **Memo** — Executive summary and problem framing
2. **Specification** — Technical planning, methodology, pseudocode
3. **Excel Build** — Quantitative/financial model
4. **Prompt Engineering** — AI integration and prompt documentation
5. **Final Recommendations** — Synthesis and actionable insights

The archived BUS-314 project used a 4-stage variant (build-first, prompt merged into final); the current Performance Ratios project (BUS 629) uses a 6-stage variant (Stage 0–5). See each subject's `projects/` folder for exact stage docs.

---

## AI Tools & Claude Code

AI use is **optional, not required** for student projects. When used, meaningful interactions should be logged in a prompt log.

This repo includes [Claude Code](https://claude.ai/code) configuration:

- **`CLAUDE.md`** — Project-level instructions that Claude reads automatically
- **`.claude/skills/`** — Custom skills that extend Claude's capabilities: `brand-guidelines`, `accounting-ratios`, `docx`, `xlsx`, `pptx`, `pdf`, `internal-comms`, `skill-creator`
- Skills activate via `/commands` (e.g., `/pptx`, `/brand-guidelines`) and require no separate installation — clone the repo and they're ready

See **`docs/presentations/Claude_Appendix.pptx`** for a complete walkthrough.

---

## Getting Started

1. **Navigate to your course**: Look up your course code in [`courses/README.md`](courses/README.md), then open your offering's subfolder (e.g., `courses/International-Corporate-Finance/BUS-629-VEMBA/`)
2. **Read the syllabus**: Each offering has a `README.md` with objectives, grading, and policies
3. **Work on deliverables**: Follow the staged assignment files in the subject's `projects/` folder
4. **Commit your work**: `git add . && git commit -m "Stage 1 memo" && git push`

For a visual walkthrough, see **`docs/presentations/GitHub_AI_Appendix.pptx`**.

---

## Extending This Work — Templates by Career Objective

The course projects in this repo are starting points, not endpoints. The same skills you used to build a ratios model, write a memo, or draft a spec can be repointed at almost any analytical task in finance and business. Below are templates and specs you could create from this foundation, organized by career objective.

These are **suggestions, not assignments.** Pick one or two that align with where you want your career to go, build them in your portfolio repo, and you'll have a public, version-controlled body of work that demonstrates initiative beyond what was required for class.

Each row notes which course project most naturally leads into the extension.

### Corporate Finance & FP&A

| Extension | What it is | Builds on |
|-----------|------------|-----------|
| **Three-statement model template** | Linked IS/BS/CF skeleton with driver-based forecasting | BUS-314, BUS-629 ratios template |
| **Budget-vs-actual variance memo** | Monthly variance analysis with commentary template | Any memo project |
| **Capital allocation framework spec** | Decision framework for ranking investment projects (NPV, IRR, payback, strategic fit) | BUS-314 / BUS-629 |
| **Working capital optimization brief** | DSO/DIO/DPO benchmarking with action recommendations | BUS-314 / BUS-629 ratios |
| **Earnings call prep template** | Q&A prep doc structuring expected questions, talking points, ratio movements | BUS-314 / BUS-629 |

### Investment Banking

| Extension | What it is | Builds on |
|-----------|------------|-----------|
| **DCF valuation spec + model** | Full discounted cash flow with WACC sensitivity, terminal value scenarios | BUS-314 / BUS-629 |
| **Comparable companies analysis (CCA)** | Trading comps template with multiple selection rationale | BUS-314 / BUS-629 |
| **Precedent transactions analysis** | Deal comps with adjustments for control premium, synergies | BUS-314 / BUS-629 |
| **LBO model template** | Sources & uses, debt schedule, returns waterfall | BUS-314 / BUS-629 |
| **Pitchbook narrative template** | Executive summary, situation, recommendation structure for client decks | Any memo project |

### Equity Research / Buy-side Analyst

| Extension | What it is | Builds on |
|-----------|------------|-----------|
| **Initiation of coverage report template** | Long-form research report: business model, financials, valuation, risks, rating | BUS-314 / BUS-629 |
| **Earnings preview / recap memo** | Pre- and post-earnings notes with consensus vs. actual | BUS-314 / BUS-629 |
| **Sector primer template** | Industry structure, key players, KPIs, regulatory landscape | BUS-313 case studies |
| **Stock pitch one-pager** | Single-page thesis: catalyst, valuation, risk/reward | BUS-314 / BUS-629 |
| **Quarterly model update memo** | Standardized quarterly review for a covered name | BUS-314 / BUS-629 |

### Credit Analysis & Debt Capital Markets

| Extension | What it is | Builds on |
|-----------|------------|-----------|
| **Credit memo template** | Issuer analysis, recovery analysis, ratings rationale | BUS-314 / BUS-629 ratios |
| **Covenant compliance check** | Spec for testing financial covenants against quarterly financials | BUS-314 / BUS-629 |
| **Bond indenture summary** | Structured summary of key terms (covenants, calls, ranking) | Any memo project |
| **Default scenario stress test** | Spec for stressing financials under recession/rate-shock scenarios | BUS-314 / BUS-629 |

### Treasury, FX & Risk Management

| Extension | What it is | Builds on |
|-----------|------------|-----------|
| **FX exposure dashboard spec** | Multi-currency exposure aggregation with hedge ratios | FIN-321 hedging |
| **Hedge effectiveness backtest** | Spec for evaluating realized hedge performance vs. plan | FIN-321 hedging |
| **Treasury policy document** | Counterparty limits, hedging mandates, cash investment policy | FIN-321 / BUS-629 |
| **Cash forecast model** | Rolling 13-week cash flow forecast template | BUS-629 cash flow |
| **Counterparty risk memo** | Methodology for sizing exposure to a single bank/dealer | FIN-321 |

### Private Equity & Venture Capital

| Extension | What it is | Builds on |
|-----------|------------|-----------|
| **Investment committee memo template** | IC deck/memo: thesis, deal terms, financials, risks, ask | Any memo project |
| **Portfolio company quarterly review** | Standardized PortCo monitoring template | BUS-314 / BUS-629 |
| **Cap table model spec** | Pre/post-money cap table with conversion mechanics | BUS-122B startup model |
| **Term sheet summary template** | Structured summary of key economic and control terms | BUS-122B / any memo |

### Sustainability, ESG & Impact

| Extension | What it is | Builds on |
|-----------|------------|-----------|
| **ESG ratio framework spec** | Carbon intensity, water use, governance metrics alongside financial ratios | BUS-314 / BUS-629 |
| **Sustainable agriculture P&L template** | Multi-year P&L with regenerative ag cost structures | BUS-122B |
| **Impact reporting memo** | Standardized impact disclosure (avoided emissions, jobs, etc.) | BUS-122B / BUS-313 |
| **Climate scenario analysis spec** | Spec for stressing financials under physical/transition risk scenarios | BUS-314 / FIN-321 |

### Strategy, Consulting & Policy

| Extension | What it is | Builds on |
|-----------|------------|-----------|
| **Industry primer / market sizing** | Top-down + bottom-up market sizing with sources | BUS-313 / BUS-620 |
| **Strategic options memo** | "Three options + recommendation" framework for any decision | Any memo project |
| **Policy impact case brief** | Trade/regulatory case applied to a specific firm or sector | BUS-313 / BUS-620 |
| **Competitor teardown** | Structured analysis of a single competitor's strategy and financials | BUS-314 / BUS-629 |

### How to add an extension to your portfolio

1. **Copy the relevant repo-level template** as your starting point — `memo-template.md`, `spec-template.md`, or the `performance-ratios-template.xlsx` skeleton.
2. **Adapt it** to the specific extension (e.g., add an LBO debt schedule tab, or restructure the memo for an IC audience).
3. **Use it on a real example.** A blank template is worth less than a populated one. Pick a real company or scenario and run it end-to-end.
4. **Commit it to your portfolio repo** with a clear README explaining what the template is for and when to use it.
5. **Link it from your bio.** A manager, peer, or reviewer who lands on your repo should be able to find your extensions in two clicks.

A portfolio with three thoughtful, well-executed extensions beats one with twenty half-finished templates. Pick deliberately, build well.

---

## Key Reference Paths

| Resource | Path |
|----------|------|
| Instructor Bio | `BIO.md` |
| Brand Design Tokens | `docs/_branding/design.json` |
| Visual Design Reference | `docs/_branding/design-system.html` |
| Appendix Presentations | `docs/presentations/` |
| Reusable Templates | `docs/templates/` |
| Decision Memos | `docs/decisions/` |
| AI Usage Guidelines | `docs/ai-usage-guidelines.md` |
| Writing Style Guide | `docs/writing-style-guide.md` |
