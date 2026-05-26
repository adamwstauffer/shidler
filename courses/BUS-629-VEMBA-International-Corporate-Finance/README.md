# BUS 629: International Corporate Finance

**Vietnam Executive MBA Program** | Shidler College of Business, University of Hawai'i at Manoa

## Course Overview

This course develops students' understanding of corporate finance. It introduces financing and investment decision-making considerations and the securities available to financial managers. The course relies heavily on developing models using Microsoft Excel and applies a **spec-driven design** approach where students build financial models, write technical specifications, and critically evaluate LLM-generated analysis.

---

## Instructor

**Adam W. Stauffer** | [adamstau@hawaii.edu](mailto:adamstau@hawaii.edu)

Please begin email subject lines with **BUS 629**. Before sending an email, check to see if your question is answered in this syllabus. For more information about the instructor, see [BIO.md](../BIO.md).

**Office Hours:** Please email to schedule appointments.

---

## Textbook

Brealey, Myers, and Marcus, *Fundamentals of Corporate Finance*, 11th ed., McGraw-Hill

- Access to **McGraw-Hill (MH) Connect** web-based course companion system.

You can register for MH Connect on **Lamaku** by selecting the **"MH Campus"** option from the left menu.

**Slides:** Slides will be available on Lamaku.

---

## Topics Covered

- Goals & Governance of the Corporation
- Financial Markets & Institutions
- Accounting & Finance
- Measuring Corporate Performance
- The Time Value of Money
- Valuing Bonds
- Valuing Stocks
- Net Present Value & Other Investment Criteria
- Using DCF Analysis to Make Investment Decisions
- Risk, Return & the Opportunity Cost of Capital & Capital Budgeting
- WACC & Company Valuation
- Introduction to Corporate Financing
- How Companies Raise Venture Capital & Issue Securities
- Long-term & Short-term Financial Planning
- Options

---

## Course Outline

The course progresses through foundational concepts of corporate finance, starting with accounting and financial analysis, moving through valuation methods (bonds and stocks), and concluding with capital budgeting, cost of capital, and advanced topics in financing and risk management. Throughout, emphasis is placed on real-world applications using spreadsheet modeling and case studies.

---

## AI + GitHub Course Project

Through the AI + GitHub project, students gain practical, workplace-ready skills:

| Skill | Description |
|-------|-------------|
| **AI Literacy & Prompt Engineering** | Design effective AI prompts for research, analysis, drafting, and critique while evaluating limitations |
| **Spec-Driven Design** | Write technical specifications precise enough for any competent executor (human or AI) to produce correct output |
| **GitHub & Version Control** | Proficiency with GitHub for project management, version control, and collaborative workflows |
| **Data Analysis & Modeling** | Use AI and finance models to generate tables, figures, and scenario analyses |
| **Professional Report Writing** | Structured memos, specs, and executive evaluations integrating quantitative analysis with narrative clarity |

**Resume/LinkedIn Keywords:** AI-assisted analysis, Prompt engineering, Spec-driven design, GitHub workflow, Reproducible research

### Project: Accounting Ratios Analysis

A 6-stage spec-driven design project. Students stand up their own public GitHub portfolio repo, populate the provided ratios template with financials for a company of their choice (non-U.S. and ASEAN-listed firms encouraged), and use an LLM to draft technical specifications and produce the final analysis — which they then critically evaluate.

| Stage | Deliverable | Weight | Format |
|-------|-------------|-------:|--------|
| 0 | Personal GitHub repo with README, RESUME, BIO | 5% | Repo URL |
| 1 | Provided ratios Excel template uploaded to your repo | 20% | `.xlsx` |
| 2 | Company selection memo | 10% | `.md` |
| 3 | Populated financials spreadsheet for selected company | 20% | `.xlsx` |
| 4 | LLM-drafted technical specification | 20% | `.md` |
| 5 | Full analysis + LLM evaluation + repo polish | 25% | Repo URL |

**Format:** All stages are **deliverable-only** — no in-class presentations this semester. Total project weight: 100%.

**Submission paths.** GitHub is the required submission channel — your Stage 5 deliverable is the public repo URL itself. Stages 2, 3, and 4 carry a **Lamaku-upload fallback** for students who hit hard blockers with Git setup; see the top of each stage doc for details. The fallback is a safety valve, not an alternate track — by Stage 5, all prior-stage artifacts must be consolidated into your GitHub repo.

**Student guides** (read as needed — none are required cover-to-cover):

- [`docs/guides/github-mba-guide.md`](../../docs/guides/github-mba-guide.md) — GitHub fundamentals, first commit, instructor write access, PR mechanics. **Read Sections 4–7 before Stage 2.**
- [`docs/guides/responding-to-pr-feedback.md`](../../docs/guides/responding-to-pr-feedback.md) — Rubric-shaped checklist for the Stage 5 PR-feedback line (5% of project). **Read the week before Stage 5.**
- [`docs/guides/vas-ifrs-gaap-ratio-quickref.md`](../../docs/guides/vas-ifrs-gaap-ratio-quickref.md) — Cross-standard reference for ratio interpretation (lease accounting, LIFO, goodwill amortization, R&D capitalization). **Read during Stage 3 if your company reports under VAS or IFRS; revisit at Stage 5 when interpreting ratios.**
- [`docs/guides/claude-code-install-for-non-technical-users.md`](../../docs/guides/claude-code-install-for-non-technical-users.md) — Optional. Windows/Mac walkthrough if you want to try Claude Code in a terminal.
- [`docs/guides/student-ai-enhancements.md`](../../docs/guides/student-ai-enhancements.md) — Optional / ungraded. Above-and-beyond paths (author a Claude Skill, try a Claude-for-Financial-Services plugin).

**Stage assignments:**
[Stage 0](stage0-repo-setup.md) |
[Stage 1](stage1-template-architecture.md) |
[Stage 2](stage2-company-selection-memo.md) |
[Stage 3](stage3-model-population-validation.md) |
[Stage 4](stage4-technical-specification.md) |
[Stage 5](stage5-llm-analysis-evaluation.md)

See [project design memo](docs/decisions/2026-04-03-bus629-accounting-ratios-project-design.md) for full rationale and pedagogical design.

### Project flow at a glance

Each stage produces a named artifact that the next stage consumes. The chain looks like this:

```
Stage 0 — Set up your portfolio repo (Stage 0 README)
              ↓
Stage 1 — Upload the ratios Excel template to your repo
              ↓
Stage 2 — Write a memo selecting your company → docs/decisions/
              ↓   (instructor reviews via pull request; you grant Write access)
Stage 3 — Populate the template with that company's financials → models/builds/
              ↓
Stage 4 — Use an LLM to draft a technical spec of the analysis → docs/specs/
              ↓   (one human-in-the-loop iteration recorded → in prompt log or analysis/validation/)
Stage 5 — Feed your spec to an LLM; verify, evaluate, and write the final analysis → deliverables/
          Polish the whole repo; submit the repo URL on Lamaku.
```

The repo at Stage 5 is your portfolio — the URL is shareable on LinkedIn and is the artifact the rubric grades.

### Project filename convention

Every project artifact uses the same naming pattern across all stages:

```
YYYY-MM-DD-{lastname}-{company-slug}-{kind}.{ext}
```

- **`YYYY-MM-DD`** — date you created the file (always lowercase, hyphen-separated, e.g., `2026-05-21`)
- **`{lastname}`** — your family name, all lowercase, no spaces (e.g., `nguyen`, `tran`, `pham`)
- **`{company-slug}`** — the company you're analyzing, all lowercase, hyphens for spaces (e.g., `vinamilk`, `fpt-corp`, `vingroup`)
- **`{kind}`** — what stage / what artifact (e.g., `selection`, `financials`, `spec`, `final-analysis`)
- **`{ext}`** — `md` for memos and analyses, `xlsx` for spreadsheets

Examples for a student named Nguyen analyzing Vinamilk:

| Stage | File |
|---|---|
| 2 | `docs/decisions/2026-05-21-nguyen-vinamilk-selection.md` |
| 3 | `models/builds/2026-06-04-nguyen-vinamilk-financials.xlsx` |
| 4 | `docs/specs/2026-06-18-nguyen-vinamilk-spec.md` |
| 4 (HIL note) | `analysis/validation/2026-06-19-nguyen-vinamilk-stage4-iteration.md` |
| 5 (raw LLM) | `deliverables/2026-07-02-nguyen-vinamilk-llm-raw.md` |
| 5 (verification) | `analysis/validation/2026-07-03-nguyen-vinamilk-stage5-verification.md` |
| 5 (final analysis) | `deliverables/2026-07-03-nguyen-vinamilk-final-analysis.md` |
| 5 (retrospective) | `deliverables/2026-07-03-nguyen-vinamilk-spec-retrospective.md` |

**Why lowercase?** GitHub on Linux servers treats `Nguyen-` and `nguyen-` as different files. Sticking to lowercase prevents broken links later.

### Project glossary

Terms used across the stage assignments. Skim once now; refer back as needed.

| Term | Plain-English meaning |
|---|---|
| **Repository (repo)** | A folder of files tracked by Git and hosted on GitHub. Your portfolio repo holds everything you produce in this project. |
| **Commit** | A saved snapshot of your repo at a moment in time, with a short message describing what changed. You will commit dozens of times across the semester. |
| **Commit history** | The chronological list of all commits in your repo. Reviewers (the instructor, managers, audit reviewers) can see it. |
| **Commit hash** | The unique ID (e.g., `ec8fa60`) of one commit. Used to point at a specific saved state. |
| **Pull request (PR)** | A proposed change to your repo, opened by you or a collaborator (the instructor). You read the suggested edits, comment on them, and either merge or reject. The instructor uses PRs to give you feedback on your memo, spec, and final analysis. |
| **YAML frontmatter** | The block of metadata at the top of a Markdown file, between two `---` lines. Looks like `title:`, `date:`, `author:`. The repo's templates use frontmatter to encode required fields — leave it intact when you customize a template. |
| **Named range** | A label assigned to a cell or group of cells in Excel (e.g., `BAL_assets_total_2025`) so formulas can refer to the label instead of the cell address. The ratios template uses named ranges so the formulas survive when you copy the workbook. |
| **Named-range notation** | The way we write formulas in the spec — using the named-range label instead of a cell address (e.g., `INC_net_income_2025 / BAL_assets_total_2025` rather than `B12 / D14`). |
| **Spec / specification** | The Stage 4 document that defines exactly what the analysis must do — precise enough that an LLM with no other context can execute it. |
| **LLM** | Large Language Model — Claude, ChatGPT, Gemini, etc. The AI that drafts your Stage 4 spec and produces the Stage 5 first-draft analysis. |
| **HIL (human-in-the-loop)** | A workflow where you review an LLM's output, identify what's wrong, and revise either the prompt or the spec to improve the next run. Required at Stage 4. |
| **Diff** | A side-by-side comparison showing what changed between two versions of a file (the "before" and the "after"). Used in PRs and HIL iteration notes. |
| **Annotated diff** | A diff with one-line notes added next to each change explaining *why* you made it. |
| **10-K** | The U.S. SEC's annual report form for public companies. We use "10-K" loosely to mean "audited annual report" — for Vietnamese companies, the equivalent is the annual report filed under VAS (Vietnamese Accounting Standards) or IFRS. |
| **Prompt log** | A `deliverables/prompt-log.md` file in your repo where you record meaningful AI sessions (what you asked, what you kept, what you changed). |
| **Lamaku** | The University of Hawai'i at Mānoa's course management system, where you submit final URLs and access course resources. |

### Repository Structure

This repository serves as a **living example** of the directory structure students should replicate in their own repos. Each directory contains a `README.md` explaining its purpose and conventions.

```
courses/BUS-629-VEMBA-International-Corporate-Finance/
├── README.md                  <- You are here
├── docs/
│   ├── decisions/             # Executive memos and decision documents
│   ├── specs/                 # Technical specifications
│   ├── plans/                 # Project plans and timelines
│   └── templates/             # Stub README pointing at canonical repo-level templates
├── models/
│   ├── templates/             # Blank model frameworks (Stage 1)
│   └── builds/                # Populated, working models (Stage 3)
├── data/                      # Source financial data and provenance
├── analysis/
│   └── validation/            # Self-audit and validation reports (Stage 3)
└── deliverables/              # Final, presentation-ready outputs (Stage 5)
```

---

# Administration

## Textbook / IDAP Program

This course participates in the Bookstore's **Interactive Digital Access Program (IDAP)**.

- Course materials will be available digitally via Lamaku by the first day of class.
- A charge for digital materials will be added to your MyUH account.
- You may opt out via the Inclusive Access Student Portal (linked in your IDAP welcome email).
- If you opt out, access will be removed and charges refunded.
- Unpaid charges may result in a hold on your account.

More information: [https://www.bookstore.hawaii.edu/manoa/site_IDAP.asp](https://www.bookstore.hawaii.edu/manoa/site_IDAP.asp)

## Accessing McGraw-Hill Connect

Register via Lamaku by selecting **"MH Campus."** You should not need to enter payment details.

An optional discounted loose-leaf version of the textbook is available at the bookstore.

## Communication

- Email is the preferred method in emergencies.
- Check the Lamaku course website one day before each class session.

---

# Grading

| Description | Percent |
|-------------|---------|
| Attendance & Participation | 10% |
| Individual Project | 45% |
| Exam | 45% |
| **Total** | **100%** |

## Attendance and Participation

Attendance will be taken and factored into your participation score.

## Examinations

- Final exam held online via MH Connect, open-book.
- Make-up exams are rare and only given under legitimate, unavoidable circumstances.
- Prior approval and documentation required.
- Make-up exams may be more rigorous than the original.
- If you believe there is a grading error, notify the instructor within one week of posting. If regrading is requested, the entire exam will be regraded.

---

# AI Use Policy

Students are encouraged to explore AI tools to enhance learning and professional decision-making. Acceptable uses include:

- **Knowledge Enhancement:** Use AI to clarify theory or extend readings.
- **Research Support:** Gather data, statistics, and examples for assignments.
- **Critical Thinking:** Test your arguments against counterarguments generated by AI.
- **Problem-Solving:** Simulate case scenarios and brainstorm managerial responses.
- **Professional Skills:** Practice clear, concise communication in prompts and outputs.

**Requirements:**
- Log all AI use in the Prompt Log.
- Verify outputs against trusted sources.
- Treat AI as a supplement — not a substitute — for your own analysis.

---

# Course Compliance with Campus Policies

Students must follow all rules and policies of the University of Hawai'i at Manoa and the Shidler College of Business.

## Students with Disabilities

Students with documented disabilities should contact the instructor or the **KOKUA Program** (Student Services Center, Room 13, 956-7511). Website: [http://www.hawaii.edu/kokua/](http://www.hawaii.edu/kokua/)

## Academic Honesty

Cheating and plagiarism will not be tolerated and will be handled under the UH Student Code of Conduct. Full code: [http://www.hawaii.edu/student/conduct](http://www.hawaii.edu/student/conduct)

### Cheating Includes:

- Unauthorized assistance during exams
- Obtaining exam information beforehand
- Submitting another's work as your own
- Using prohibited materials
- Fabricating or falsifying data
- Altering grades or exam answers
- Falsifying University records
- Misrepresenting facts for exemptions

### Plagiarism Includes:

- Copying work without attribution
- Improper paraphrasing or quotation
- Submitting the same work in multiple courses without permission
- "Drylabbing" (using others' experimental data or write-ups)

---

## Key Links

| Resource | Location |
|----------|----------|
| Project Design Memo | [`docs/decisions/2026-04-03-bus629-accounting-ratios-project-design.md`](docs/decisions/2026-04-03-bus629-accounting-ratios-project-design.md) |
| Project Presentation | [`BUS629_AI_Ratios_Project.pptx`](BUS629_AI_Ratios_Project.pptx) |
| Provided Excel Template (Stage 1) | [`../../docs/templates/spreadsheets/performance-ratios-template.xlsx`](../../docs/templates/spreadsheets/performance-ratios-template.xlsx) |
| Memo Template | [`../../docs/templates/memo-template.md`](../../docs/templates/memo-template.md) |
| Spec Template | [`../../docs/templates/spec-template.md`](../../docs/templates/spec-template.md) |
| Templates README (frontmatter, naming) | [`../../docs/templates/README.md`](../../docs/templates/README.md) |
| Brand Guidelines | [`../../docs/_branding/design.json`](../../docs/_branding/design.json) |
| Financial Model Assumptions (Student) | [`../../docs/financial-model-assumptions-student.md`](../../docs/financial-model-assumptions-student.md) |
| Financial Model Assumptions (Full Spec) | [`../../docs/financial-model-assumptions.md`](../../docs/financial-model-assumptions.md) |
