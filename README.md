# Shidler College of Business — Course & Portfolio Hub

Unified repository for course materials, project frameworks, branded assets, and professional portfolio documents for courses taught by **Adam W. Stauffer** at the University of Hawai&#x02BB;i at M&#x0101;noa Shidler College of Business.

Everything lives in one Git-tracked repo so students, collaborators, and reviewers can find syllabi, assignment specs, templates, and decision memos in a single place.

## About Me

**Adam W. Stauffer** is a Faculty Lecturer in finance and economics at the Shidler College of Business, University of Hawaiʻi at Mānoa, and teaches sustainable agriculture entrepreneurship at Windward Community College. Before teaching, he was a trader and market-maker in U.S.-listed ETFs at Barclays Capital and Lehman Brothers, was founder and Chief Investment Officer of Springline Capital in the British Virgin Islands, and founded Greenshoot.org, a disaster-recovery platform built after Hurricane Irma. He builds his courses around AI: students frame, specify, build with AI, audit and decide, in the open on GitHub. He holds an MBA in Finance from Wharton and a BA in Biology from Trinity College, and was a CFA charterholder from 2004 to 2011.

- [Bio](https://adamwstauffer.github.io/bio.html) · [Resume](https://adamwstauffer.github.io/resume.html) ([PDF](https://adamwstauffer.github.io/resume.pdf)) · [CV](https://adamwstauffer.github.io/cv.html), all on [adamwstauffer.github.io](https://adamwstauffer.github.io/)
- [LinkedIn](https://linkedin.com/in/adamwstauffer) · [GitHub](https://github.com/adamwstauffer)

---

## 📘 Start here: the Kumu tutorial site

**<https://adamwstauffer.github.io/ai-lms/>** — the companion tutorial site for these courses.
This repo holds the *source materials* (syllabi, stage briefs, templates); **Kumu is
where you actually work through a project**: stage-by-stage tutorials with checklists and
self-quizzes, hands-on labs, and an AI tutor. Organized by subject, no course codes:

| Subject | Kumu page | Courses |
|---------|-----------|---------|
| Getting set up (GitHub + AI, start here) | [Onboarding](https://adamwstauffer.github.io/ai-lms/onboarding.html) | all |
| International Corporate Finance | [Performance ratios](https://adamwstauffer.github.io/ai-lms/international-corporate-finance.html) | BUS 629 |
| International Finance & Securities | [FX hedging](https://adamwstauffer.github.io/ai-lms/international-finance-and-securities.html) | FIN 321 |
| International Economics & Trade | [Trade cases](https://adamwstauffer.github.io/ai-lms/international-economics-and-trade.html) | BUS 313 |
| Micro- & Macro-Economics | [Econ cases](https://adamwstauffer.github.io/ai-lms/micro-and-macro-economics.html) | BUS 620 / DLEMBA |

Each offering's `README.md` under `courses/` signposts its own Kumu pages, point values, and due
dates — the course README is the schedule, Kumu is the instruction.

---

## Why the projects work this way: doers → reviewers

Entry-level analysts used to learn judgment by building models that seniors reviewed. AI now drafts
that first pass, so the work that trained reviewers is the work AI does first. Every project here
makes you do both jobs: you frame and specify, AI builds, you audit and decide. Full argument:
[The doer–reviewer dilemma](https://adamwstauffer.github.io/writing/doer-reviewer-dilemma.html).

---

## Repository Structure

```
shidler/
├── BIO.md                          # Short instructor bio; full bio, resume and CV on adamwstauffer.github.io
├── AGENTS.md                       # AI agent instructions for this repo (canonical)
├── CLAUDE.md                       # One-line pointer to AGENTS.md
│
├── courses/                        # Subject-first directories (see courses/README.md for the code map)
│   ├── International-Corporate-Finance/    # BUS 314 (archived), BUS 629
│   ├── International-Finance-And-Securities/  # FIN 321
│   ├── International-Economics-And-Trade/  # BUS 313
│   ├── Micro-And-Macro-Economics/          # BUS 620, BUS 620 DLEMBA
│   └── Windward-Community-College/
│       └── BUS-122B-Intro-Entrepreneurship-Sustainable-Agriculture/
│
├── guides/                         # Student guides: GitHub, PR feedback, Claude Code, VAS/IFRS/GAAP ratios
├── templates/                      # Reusable deliverable templates (memo, spec, brief, prompt log)
│
├── docs/
│   ├── _branding/                  # UH Manoa design system & templates
│   ├── decisions/                  # Strategic decision memos
│   ├── presentations/              # Course-agnostic appendix slide decks
│   ├── ai-usage-guidelines.md
│   ├── writing-style-guide.md
│   └── reproducibility-playbook.md
```

Answer keys, grading scripts and `.claude/` tooling are deliberately kept out of this public repo.

---

## Active Courses

| Code | Subject | Level | Key Project |
|------|-------|-------|-------------|
| BUS 313 | International Economics and Trade | Undergrad | Trade/geopolitics case studies |
| BUS 314 | International Corporate Finance | Undergrad (archived) | Performance ratios — superseded by BUS 629's project design |
| FIN 321 | International Finance and Securities | Upper undergrad | FX hedging (6-stage) |
| BUS 620 | Micro- and Macro-Economics | MBA | Team cases + individual research |
| BUS 620 DLEMBA | Micro- and Macro-Economics | Distance EMBA | Team cases + individual research |
| BUS 122B | Intro Entrepreneurship / Sustainable Ag | Community college | Business plan + pitch |
| BUS 629 | International Corporate Finance | Vietnam EMBA | Performance ratios (6-stage, spec-driven) |

See [`courses/README.md`](courses/README.md) for the full code-to-directory map. Each subject directory contains a `projects/` folder with shared curriculum and one subfolder per offering with its syllabus, roster, and course-specific decision memos.

## Documentation Hub (`docs/`)

### Branding (`docs/_branding/`)

The UH M&#x0101;noa design system is stored as two complementary files:

- **`design.json`** — Machine-readable design tokens (colors, typography, spacing, components). Claude and other tools read this file to apply institutional branding automatically.
- **`design-system.html`** — Human-readable visual reference. Open in a browser to review the full color palette, typography scale, and component examples.

PowerPoint templates (`.potx`, `.pptx`) live in `docs/_branding/templates/`.

### Templates (`templates/`)

Reusable Markdown templates for common deliverables: executive memo, technical spec, case brief, risk memo, prompt log, and bio/resume formats.

### Decision Memos (`docs/decisions/`)

Lightweight memos capturing strategic decisions about repo structure, course design, and project architecture.

---

## AI Tools & Claude Code

AI is **expected** and must be **disclosed**; log meaningful interactions in a prompt log. Disclosed AI
work is never penalized. The grade follows the journey, not the destination: the framing, spec,
audit and decision are yours, and they carry the weight.

This repo includes AI agent configuration — and models the same convention your portfolio repo
should follow:

- **`AGENTS.md`** — The canonical agent-instructions file, read by Claude Code, Codex, and other tools
- **`CLAUDE.md`** — A one-line pointer to `AGENTS.md` (kept for tools that look for it by name)

See **`docs/presentations/Claude_Appendix.pptx`** for a complete walkthrough.

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

## Key Reference Paths

| Resource | Path |
|----------|------|
| Instructor Bio | `BIO.md` |
| Brand Design Tokens | `docs/_branding/design.json` |
| Visual Design Reference | `docs/_branding/design-system.html` |
| Appendix Presentations | `docs/presentations/` |
| Reusable Templates | `templates/` |
| Decision Memos | `docs/decisions/` |
| AI Usage Guidelines | `docs/ai-usage-guidelines.md` |
| Writing Style Guide | `docs/writing-style-guide.md` |
