# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Unified portfolio and course materials hub for Shidler College of Business (University of Hawaiʻi at Mānoa) courses taught by Adam W. Stauffer. Contains syllabi, assignment frameworks, project templates, branded materials, and professional portfolio documents — all managed via Git/Markdown.

## Repository Structure

- **Course directories** follow `[CODE]-[Descriptive-Title]` naming (e.g., `BUS-314-International-Corporate-Finance/`)
- **`docs/`** — Centralized documentation hub:
  - `_branding/` — UH Mānoa design tokens (`design.json`) and visual reference (`design-system.html`)
  - `templates/` — Reusable assignment templates (memo, spec, case brief, risk memo, prompt log)
  - `decisions/` — Strategic decision memos
  - `ai-usage-guidelines.md`, `writing-style-guide.md`, `reproducibility-playbook.md`
- **`BIO.md`** — Single source of truth for instructor biography; course READMEs link here
- **`_archive/`** — Deprecated/historical materials
- **`notes/`** — Personal research notes

### Within each course directory

- `README.md` — Standardized syllabus (overview, objectives, grading, AI policy, campus policies)
- `project-[name]/` or `[project-name]/` — Active project with stage assignments
- `_templates/excel/` — Skeleton Excel workbooks
- `_spreadsheets/` — Master financial models
- `archive/` — Past iterations (specs, prompts, analysis, deliverables)

## Five-Stage Project Workflow

Most projects follow this reusable pedagogical pattern:

1. **Memo** (Stage 1) — Executive summary and problem framing
2. **Specification** (Stage 2) — Technical planning, methodology, pseudocode
3. **Excel Build** (Stage 3) — Quantitative/financial model in Excel
4. **Prompt Engineering** (Stage 4) — AI integration and prompt documentation
5. **Final Recommendations** (Stage 5) — Synthesis and actionable insights

Stage files are named `stage[N]-[description]-assignment.md`. Templates for deliverables are `template-memo.md` and `template-spec.md`.

## Active Courses

| Code | Title | Level | Key Project |
|------|-------|-------|-------------|
| BUS 313 | Economic & Financial Environment of Global Business | Undergrad | Trade/geopolitics case studies |
| BUS 314 | International Business Finance | Undergrad | Accounting ratios (5-stage, 25+ ratios) |
| FIN 321 | International Finance & Securities | Upper undergrad | FX hedging (5-stage) |
| BUS 620 | Micro & Macro Economics | MBA | Team cases + individual research |
| BUS 122B | Intro Entrepreneurship/Sustainable Ag | Community college | Business plan + pitch |
| BUS 629 | International Corporate Finance | Vietnam EMBA | In development |

## UH Mānoa Brand System

Full design tokens live in `docs/_branding/design.json`. Key values:

- **Primary:** UH Green `#024731` — logos, headings, accents
- **Secondary:** Black `#000000` — body text, borders
- **Typography:** Open Sans (Bold headings, Regular body); Avenir for print
- **Accessibility:** ADA-compliant contrast ratios required; minimum 10pt body text

The `brand-guidelines` skill applies these standards automatically. Use it when creating any UH-branded materials.

## Writing and AI Conventions

- **Writing style:** Lead with 100–150 word executive summary; active voice; trim jargon; cite figures/tables in-text
- **AI use is optional, not required** for student projects
- **AI logging:** Meaningful prompts/outputs go in `deliverables/prompt-log.md`; AI-assisted sections marked in memos
- **Reproducibility:** Record dataset links + access dates; keep raw vs. clean data separate; tag releases for milestones

## Naming Conventions

- Course directories: `[CODE]-[Descriptive-Title]` with PascalCase hyphens
- `_`-prefixed directories (`_templates/`, `_archive/`, `_branding/`) denote system/organizational content
- Excel named ranges for BUS-314: `BAL_`, `INC_`, `CASH_`, `RATIO_` prefixes (see `BUS-314/.../CLAUDE.md` for full spec)

## Key Reference Paths

| Resource | Path |
|----------|------|
| Instructor Bio (SSOT) | `BIO.md` |
| Brand Design Tokens | `docs/_branding/design.json` |
| Reusable Templates | `docs/templates/` |
| Strategic Decisions | `docs/decisions/` |
| Repo Hierarchy Doc | `docs/decisions/2026-02-15-repo-hierarchy.md` |
| BUS-314 Ratios Context | `BUS-314-International-Corporate-Finance/accounting-ratios/CLAUDE.md` |
| Master Ratios Spreadsheet | `BUS-314-International-Corporate-Finance/_spreadsheets/BUS-314 Accounting & Performance Ratios - MASTER.xlsx` |

## Skills Available

This repo has custom Claude Code skills in `.claude/skills/`: `brand-guidelines`, `docx`, `internal-comms`, `pdf`, `pptx`, `skill-creator`, `xlsx`. Use the appropriate skill when creating or editing Office documents, applying UH branding, or writing internal communications.
