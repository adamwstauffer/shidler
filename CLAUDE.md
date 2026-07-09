# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Working Principles

Adapted from [Andrej Karpathy's coding guidelines](https://github.com/multica-ai/andrej-karpathy-skills) for this docs/Markdown repository:

- **Think before editing** — state assumptions and surface ambiguity instead of guessing silently; offer the simpler option when one exists.
- **Simplicity first** — do the task that was asked; no speculative restructuring of courses, templates, or decision memos.
- **Surgical changes** — touch only what the request needs, and preserve each file's existing style and formatting (existing template conventions always win). Flag stray issues you notice rather than fixing them unasked; when records *document* a past change (e.g. a decision memo), update live materials, not the record.
- **Goal-driven** — define what "done" looks like, then verify it: `recalc.py` returns 0 errors, generated Office files validate, referenced paths resolve, no broken links.

## Repository Purpose

Unified portfolio and course materials hub for Shidler College of Business (University of Hawaiʻi at Mānoa) courses taught by Adam W. Stauffer. Contains syllabi, assignment frameworks, project templates, branded materials, and professional portfolio documents — all managed via Git/Markdown.

## Repository Structure

- **`courses/`** — Subject-first directories (e.g., `courses/International-Corporate-Finance/`), not course-code-first. See `courses/README.md` for the Shidler-code-to-directory map. Each subject directory shares one shape: `projects/<slug>/` (shared curriculum) + one `<CODE[-POPULATION]>/` subfolder per offering (e.g., `BUS-629-VEMBA/`, `FIN-321/`). See `docs/decisions/2026-07-08-generic-course-directory-naming.md` for the full rationale.
- **`docs/`** — Centralized documentation hub:
  - `_branding/` — UH Mānoa design tokens (`design.json`) and visual reference (`design-system.html`)
  - `templates/` — Reusable assignment templates (memo, spec, case brief, risk memo, prompt log)
  - `decisions/` — Strategic decision memos, flat (`YYYY-MM-DD-<slug>.md`; course-specific ones are `YYYY-MM-DD-<course-code>-<slug>.md`, e.g. `2026-05-07-bus629-stage2-restructure.md`)
  - `ai-usage-guidelines.md`, `writing-style-guide.md`, `reproducibility-playbook.md`
- **`BIO.md`** — Single source of truth for instructor biography; course READMEs link here
- **`_archive/`** — Deprecated/historical materials; course-specific archives live in `_archive/<course-code>/` subdirs (e.g., `_archive/fin321/`, `_archive/bus314/` — the archived BUS-314 project, superseded by the shared `performance-ratios` project under `courses/International-Corporate-Finance/projects/`)
- **`scripts/`** — Repo-level tooling scripts; spreadsheet cleanup pipelines live in `scripts/spreadsheets/`

### Within each subject directory

- `README.md` — Subject hub: overview, course-code table, links to `projects/` and offering folders
- `projects/<slug>/` — Shared curriculum: stage assignment docs, `_templates/`, `_tools/` (grading scripts), analysis/deliverables/models as applicable
- `<CODE[-POPULATION]>/README.md` — Per-offering syllabus (overview, objectives, grading, AI policy, campus policies)
- `<CODE[-POPULATION]>/ignore/` — Gitignored student submissions and grading records for that offering

## Project Workflow

Most projects follow a reusable pedagogical pattern. The default is five stages:

1. **Memo** (Stage 1) — Executive summary and problem framing
2. **Specification** (Stage 2) — Technical planning, methodology, pseudocode
3. **Excel Build** (Stage 3) — Quantitative/financial model in Excel
4. **Prompt Engineering** (Stage 4) — AI integration and prompt documentation
5. **Final Recommendations** (Stage 5) — Synthesis and actionable insights

**The archived BUS-314 project used a 4-stage variant** (build-first, prompt merged into final):
1. Memo → 2. Excel Build → 3. Spec (post-build) → 4. Final Analysis + Prompt

**The current Performance Ratios project (BUS 629) uses a 6-stage variant** (Stage 0–5: repo setup, template architecture, company selection, model population/validation, technical specification, LLM analysis evaluation).

Stage files are named `stage[N]-[description]-assignment.md`. Templates for deliverables are `template-memo.md` and `template-spec.md`.

## Active Courses

| Code | Subject | Level | Key Project |
|------|-------|-------|-------------|
| BUS 313 | International Economics and Trade | Undergrad | Trade/geopolitics case studies |
| BUS 314 | International Corporate Finance | Undergrad (archived) | Performance ratios — superseded, see `_archive/bus314/` |
| FIN 321 | International Finance and Securities | Upper undergrad | FX hedging (5-stage) |
| BUS 620 | Micro- and Macro-Economics | MBA | Team cases + individual research |
| BUS 620 DLEMBA | Micro- and Macro-Economics | Distance EMBA | In setup |
| BUS 122B | Intro Entrepreneurship/Sustainable Ag | Community college | Business plan + pitch |
| BUS 629 | International Corporate Finance | Vietnam EMBA | Performance ratios (6-stage, spec-driven) |

Note: there is no separate "DCF" project — confirmed via repo-wide search, no such materials exist. The GAAP-conversion methodology (`docs/decisions/2026-05-24-accounting-standards-conversion-framework.md`) is implemented as one supporting artifact (`models/templates/gaap-bridge-template.xlsx`) inside the Performance Ratios project, not a standalone project.

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

- Subject directories: `courses/[Descriptive-Subject-Name]` with PascalCase hyphens (no course code in the name)
- Offering subfolders: `courses/<Subject>/[CODE[-POPULATION]]/` (e.g., `BUS-629-VEMBA/`, `FIN-321/`)
- `_`-prefixed directories (`_templates/`, `_archive/`, `_branding/`) denote system/organizational content
- Excel named ranges for the Performance Ratios project: `BAL_`, `INC_`, `CASH_`, `RATIO_` prefixes (see `accounting-ratios` skill for full spec)

## Key Reference Paths

| Resource | Path |
|----------|------|
| Instructor Bio (SSOT) | `BIO.md` |
| Brand Design Tokens | `docs/_branding/design.json` |
| Reusable Templates | `docs/templates/` |
| Strategic Decisions | `docs/decisions/` |
| Repo Hierarchy Doc | `docs/decisions/2026-02-15-repo-hierarchy.md` (historical; superseded by `docs/decisions/2026-07-08-generic-course-directory-naming.md`) |
| Accounting Ratios Skill | `.claude/skills/accounting-ratios/SKILL.md` |
| Master Ratios Spreadsheet | `docs/spreadsheets/Corporate Finance Master Spreadsheets.xlsx` (supersedes the archived `_archive/bus314/_spreadsheets/BUS-314 Accounting & Performance Ratios - MASTER.xlsx`) |
| Appendix Presentations | `docs/presentations/` |
| **Financial Model Assumptions (SSOT)** | **`docs/financial-model-assumptions.md`** |

## Financial Model Assumptions (mandatory for valuation work)

Whenever building or modifying a financial model — DCF, comparable companies, LBO, merger model, three-statement build, or any valuation exercise — Claude **must read [`docs/financial-model-assumptions.md`](docs/financial-model-assumptions.md) first** and use the values stored there for any cross-company assumption (risk-free rate, equity risk premium, US tax rate default, terminal growth rate convention, color palette, number formats, etc.).

These values are institutional house-view assumptions and must be identical across every model regardless of which company is being analyzed. Company-specific inputs (beta, revenue, margins, capital structure) are still derived per company, but the **methodology and shared inputs** come from this file.

- If a value in the spec is older than its update cadence, refresh it in the file and add an Update Log entry — do not quietly use a fresher value.
- If the analysis requires deviating from the spec (e.g., a non-USD DCF), document the deviation in the model's notes section.
- Every hardcoded cell drawing from this spec should cite it in the cell comment: `Source: docs/financial-model-assumptions.md §[section]`.

This applies to the `financial-analysis:*`, `investment-banking:*`, `equity-research:*`, `pitch-agent:*`, and `market-researcher:*` plugin skills as well — they live in the plugin cache and shouldn't be edited directly, so this CLAUDE.md directive is the binding override.

## Excel Conventions

When building or editing any `.xlsx` workbook, **always use formulas instead of hardcoded values** for calculated cells. Only raw source data (e.g., a company's reported revenue typed from a filing) may be entered as a literal number. Every intermediate calculation, subtotal, ratio, and output cell must be a formula referencing its inputs. This applies to all spreadsheet-producing skills (`xlsx`, `financial-analysis:*`, `investment-banking:*`, `equity-research:*`, `pitch-agent:*`, `gl-reconciler:*`, `market-researcher:*`).

## Skills Available

This repo has custom Claude Code skills in `.claude/skills/`: `brand-guidelines`, `accounting-ratios`, `docx`, `internal-comms`, `pdf`, `pptx`, `skill-creator`, `xlsx`. Use the appropriate skill when creating or editing Office documents, applying UH branding, helping with the Performance Ratios project, or writing internal communications.
