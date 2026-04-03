# Shidler College of Business — Course & Portfolio Hub

Unified repository for course materials, project frameworks, branded assets, and professional portfolio documents for courses taught by **Adam W. Stauffer** at the University of Hawai&#x02BB;i at M&#x0101;noa Shidler College of Business.

Everything lives in one Git-tracked repo so students, collaborators, and reviewers can find syllabi, assignment specs, templates, and decision records in a single place.

---

## Repository Structure

```
shidler/
├── BIO.md                        # Instructor biography (single source of truth)
├── CV.md                         # Curriculum vitae
├── RESUME.md                     # One-page resume
├── CLAUDE.md                     # AI assistant configuration for this repo
│
├── GitHub_AI_Appendix.pptx       # Generic appendix: GitHub & AI setup guide
├── Claude_Appendix.pptx          # Generic appendix: Using Claude (web, app, CLI)
│
├── BUS-313-Economic-And-Financial-Environment-Global-Business/
├── BUS-314-International-Corporate-Finance/
├── BUS-620-Micro-And-Macro-Economics/
├── BUS-629-VEMBA-International-Corporate-Finance/
├── FIN-321-International-Finance-And-Securities/
├── Windward-Community-College/
│   └── BUS-122B-Intro-Entrepreneurship-Sustainable-Agriculture/
│
├── docs/
│   ├── _branding/                # UH Manoa design system & templates
│   ├── decisions/                # Strategic decision memos
│   ├── templates/                # Reusable deliverable templates
│   ├── ai-usage-guidelines.md
│   ├── writing-style-guide.md
│   └── reproducibility-playbook.md
│
├── _archive/                     # Deprecated/historical materials
├── notes/                        # Personal research notes
└── scripts/                      # Utility scripts
```

---

## Active Courses

| Code | Title | Level | Key Project |
|------|-------|-------|-------------|
| BUS 313 | Economic & Financial Environment of Global Business | Undergrad | Trade/geopolitics case studies |
| BUS 314 | International Business Finance | Undergrad | Accounting ratios (4-stage, 25+ ratios) |
| FIN 321 | International Finance & Securities | Upper undergrad | FX hedging (5-stage) |
| BUS 620 | Micro & Macro Economics | MBA | Team cases + individual research |
| BUS 122B | Intro Entrepreneurship / Sustainable Ag | Community college | Business plan + pitch |
| BUS 629 | International Corporate Finance | Vietnam EMBA | Accounting ratios (5-stage, living example) |

Each course directory contains a `README.md` syllabus, project folders with staged assignments, and any course-specific templates or decision records.

---

## Generic Appendix Presentations

Two course-agnostic slide decks live at the repo root. Attach them to any course project:

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

### Decision Records (`docs/decisions/`)

Lightweight memos capturing strategic decisions about repo structure, course design, and project architecture.

---

## Project Workflow

Most projects follow a staged pedagogical pattern:

1. **Memo** — Executive summary and problem framing
2. **Specification** — Technical planning, methodology, pseudocode
3. **Excel Build** — Quantitative/financial model
4. **Prompt Engineering** — AI integration and prompt documentation
5. **Final Recommendations** — Synthesis and actionable insights

BUS-314 uses a 4-stage variant (build-first, prompt merged into final). See each course README for details.

---

## AI Tools & Claude Code

AI use is **optional, not required** for student projects. When used, meaningful interactions should be logged in a prompt log.

This repo includes [Claude Code](https://claude.ai/code) configuration:

- **`CLAUDE.md`** — Project-level instructions that Claude reads automatically
- **`.claude/skills/`** — Custom skills that extend Claude's capabilities: `brand-guidelines`, `bus314-accounting-ratios`, `docx`, `xlsx`, `pptx`, `pdf`, `internal-comms`, `skill-creator`
- Skills activate via `/commands` (e.g., `/pptx`, `/brand-guidelines`) and require no separate installation — clone the repo and they're ready

See the **Claude_Appendix.pptx** for a complete walkthrough.

---

## Getting Started

1. **Clone the repo**: `git clone https://github.com/adamwstauffer/shidler.git`
2. **Navigate to your course**: Open the appropriate `BUS-*` or `FIN-*` directory
3. **Read the syllabus**: Each course has a `README.md` with objectives, grading, and policies
4. **Work on deliverables**: Follow the staged assignment files in each project folder
5. **Commit your work**: `git add . && git commit -m "Stage 1 memo" && git push`

For a visual walkthrough, see **GitHub_AI_Appendix.pptx**.

---

## Key Reference Paths

| Resource | Path |
|----------|------|
| Instructor Bio | `BIO.md` |
| Brand Design Tokens | `docs/_branding/design.json` |
| Visual Design Reference | `docs/_branding/design-system.html` |
| Reusable Templates | `docs/templates/` |
| Strategic Decisions | `docs/decisions/` |
| AI Usage Guidelines | `docs/ai-usage-guidelines.md` |
| Writing Style Guide | `docs/writing-style-guide.md` |
