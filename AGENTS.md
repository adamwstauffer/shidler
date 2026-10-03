# AGENTS.md

Instructions for AI coding agents (Claude Code, Codex CLI, and any other tool that reads this
convention) working in this repository. `CLAUDE.md` is a one-line pointer here — the same
AGENTS.md-canonical convention students follow in their portfolio repos.

## Working Principles

Adapted from [Andrej Karpathy's coding guidelines](https://github.com/multica-ai/andrej-karpathy-skills) for this docs/Markdown repository:

- **Think before editing** — state assumptions and surface ambiguity instead of guessing silently; offer the simpler option when one exists.
- **Simplicity first** — do the task that was asked; no speculative restructuring of courses, templates, or decision memos.
- **Surgical changes** — touch only what the request needs, and preserve each file's existing style and formatting (existing template conventions always win). Flag stray issues you notice rather than fixing them unasked; when records *document* a past change (e.g. a decision memo), update live materials, not the record.
- **Goal-driven** — define what "done" looks like, then verify it: `recalc.py` returns 0 errors, generated Office files validate, referenced paths resolve, no broken links.

## Repository Purpose

Unified portfolio and course materials hub for Shidler College of Business (University of Hawaiʻi at Mānoa) courses taught by Adam W. Stauffer. Contains syllabi, assignment frameworks, project templates, branded materials, and professional portfolio documents — all managed via Git/Markdown.

Student-facing tutorials live on the companion **Kumu site**, <https://adamwstauffer.github.io/ai-lms/>. This repo's stage briefs and the site's stage pages are kept in sync — a change to one usually implies a change to the other.

## Repository Structure

- **`courses/`** — Subject-first directories (e.g., `courses/International-Corporate-Finance/`), not course-code-first. See `courses/README.md` for the Shidler-code-to-directory map. Each subject directory shares one shape: `projects/<slug>/` (shared curriculum) + one `<CODE[-POPULATION]>/` subfolder per offering (e.g., `BUS-629-VEMBA/`, `FIN-321/`). See `docs/decisions/2026-07-08-generic-course-directory-naming.md` for the full rationale.
- **`docs/`** — Centralized documentation hub:
  - `_branding/` — Adam's personal slide and color kit: design tokens (`design.json`), visual reference (`design-system.html`), `.potx` templates. Not an official UH or Shidler asset.
  - `decisions/` — One public memo, `2026-07-08-generic-course-directory-naming.md`; other memos are kept privately, see `CHANGELOG.md`
  - `ai-usage-guidelines.md`, `writing-style-guide.md`, `reproducibility-playbook.md`, `grading-scale.md`, `financial-model-assumptions.md`
- **`templates/`** (repo root) — Deliverable templates students copy (memo, spec, case brief, stage brief, prompt log, `portfolio/`, `spreadsheets/`)
- **`guides/`** (repo root) — How-to guides for students
- **`CHANGELOG.md`** — Notable changes to how the repo is organized
- The instructor bio, resume and CV live on the site, never in this repo: <https://adamwstauffer.github.io/bio.html>

## Local-only trees — PII and history (hard rules)

Several root directories exist on Adam's machine but are **fully gitignored — they must never
appear on the public tree**, not even as placeholder READMEs:

- **`/rosters/`** — rosters, attendance sheets, approved-access lists (incl. the Kumu-site access list `rosters/approved/kumu-approved.xlsx`). Student PII: names, emails, IDs. FERPA — never commit anything from this tree, never add whitelist exceptions.
- **`/recommendations/`** — recommendation letters and the résumés, statements, and correspondence supporting them. One folder per student, `recommendations/<YYYY-MM>-<lastname>-<firstname>/`. Same rule: nothing here is ever committed.
- **`<CODE[-POPULATION]>/ignore/`** — per-offering student submissions and grading records.

Each local tree carries its own untracked `README.md` describing its layout — read it before
filing anything there. When work touches these trees, reference them by path in commits/memos but
never `git add` their contents.

### Within each subject directory

- `README.md` — Subject hub: overview, course-code table, links to `projects/` and offering folders
- `projects/<slug>/` — Shared curriculum: stage assignment docs, `_templates/`, analysis/deliverables/models as applicable
- `<CODE[-POPULATION]>/README.md` — Per-offering syllabus (overview, objectives, grading, AI policy, campus policies)
- `<CODE[-POPULATION]>/ignore/` — Gitignored student submissions and grading records for that offering

## Grading

Grading tooling is kept outside this public repo. Grade records and rosters stay local, under the
gitignored `ignore/` and `rosters/` trees — never committed.

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

Stage files are named `stage[N]-[description].md`, numbered **per case** (Stage 0 is repo setup where a project has one; content stages start at 1) — the containing
folder already scopes the case, so the filename does not encode it again (decided 2026-08-02; the
BUS 620 `stage1a/1b/1c` scheme was renamed to `stage1/stage2/stage3`). Templates for deliverables
live in [`templates/`](templates/).

Student portfolio repos are organized by capability: the top-level `capabilities/` directory
(renamed from `skills/` 2026-08-06 to avoid colliding with Claude Code's `.claude/skills/`) holds one folder per
capability (`capabilities/<capability>/{README.md,spec.md,model.xlsx}`).

## Release Workflow

**Never push `main` directly.** Work lands on a feature branch, goes to `main` via pull request,
and Adam's merge is the release. This is a deploy airlock, not code review: this repo's briefs are
what students read, and the Kumu site's stage pages mirror them. The PR is the moment to see exactly what is about to go live.

Branch naming: `launch/<term>`, `feat/<slug>`, `fix/<slug>`, `docs/<slug>`.

## Active Courses

| Code | Subject | Level | Key Project |
|------|-------|-------|-------------|
| BUS 313 | International Economics and Trade | Undergrad | Trade/geopolitics case studies |
| BUS 314 | International Corporate Finance | Undergrad (archived) | Performance ratios — superseded by BUS 629's project; not on the public tree |
| FIN 321 | International Finance and Securities | Upper undergrad | FX hedging (6-stage, Stage 0–5) |
| BUS 620 | Micro- and Macro-Economics | MBA | Team cases + individual research |
| BUS 620 DLEMBA | Micro- and Macro-Economics | Distance EMBA | Cases + individual research (no team case) |
| BUS 122B | Intro Entrepreneurship/Sustainable Ag | Community college | Business plan + pitch |
| BUS 629 | International Corporate Finance | Vietnam EMBA | Performance ratios (6-stage, spec-driven) |

Note: there is no separate "DCF" project — confirmed via repo-wide search, no such materials exist. The GAAP-conversion methodology (the accounting-standards conversion framework decision of 2026-05-24, kept privately) is implemented as one supporting artifact (`courses/International-Corporate-Finance/projects/performance-ratios/models/templates/gaap-bridge-template.xlsx`) inside the Performance Ratios project, not a standalone project.

## Slide and Color Kit

Adam's personal kit, inspired by UH Mānoa's public brand guide; not an official UH or Shidler asset. Full design tokens live in `docs/_branding/design.json`. Key values:

- **Primary:** UH Green `#024731` — logos, headings, accents
- **Secondary:** Black `#000000` — body text, borders
- **Typography:** Open Sans (Bold headings, Regular body); Avenir for print
- **Accessibility:** ADA-compliant contrast ratios required; minimum 10pt body text

Apply these values when creating course slides or documents.

## Writing and AI Conventions

- **Writing style:** Lead with 100–150 word executive summary; active voice; trim jargon; cite figures/tables in-text
- **AI use is expected and disclosed;** disclosed AI is never deducted
- **AI logging:** Meaningful prompts/outputs go in `deliverables/prompt-log.md`; AI-assisted sections marked in memos
- **Reproducibility:** Record dataset links + access dates; keep raw vs. clean data separate; tag releases for milestones

## Naming Conventions

- Subject directories: `courses/[Descriptive-Subject-Name]` with PascalCase hyphens (no course code in the name)
- Offering subfolders: `courses/<Subject>/[CODE[-POPULATION]]/` (e.g., `BUS-629-VEMBA/`, `FIN-321/`)
- `_`-prefixed directories (`_templates/`, `_branding/`) denote system/organizational content
- Excel named ranges for the Performance Ratios project: `BAL_`, `INC_`, `CASH_`, `RATIO_` prefixes (see the Performance Ratios project README)

## Key Reference Paths

| Resource | Path |
|----------|------|
| Instructor Bio (SSOT) | <https://adamwstauffer.github.io/bio.html> |
| How-to Guides | `guides/` |
| Changelog | `CHANGELOG.md` |
| Brand Design Tokens | `docs/_branding/design.json` |
| Reusable Templates | `templates/` |
| Repo Hierarchy Doc | `docs/decisions/2026-07-08-generic-course-directory-naming.md` (the one public decision memo) |
| Appendix Presentations | `docs/presentations/` |
| **Financial Model Assumptions (SSOT)** | **`docs/financial-model-assumptions.md`** |
| Grading Scale | `docs/grading-scale.md` |
| Kumu tutorial site | <https://adamwstauffer.github.io/ai-lms/> |

## Financial Model Assumptions (mandatory for valuation work)

Whenever building or modifying a financial model — DCF, comparable companies, LBO, merger model, three-statement build, or any valuation exercise — the agent **must read [`docs/financial-model-assumptions.md`](docs/financial-model-assumptions.md) first** and use the values stored there for any cross-company assumption (risk-free rate, equity risk premium, US tax rate default, terminal growth rate convention, color palette, number formats, etc.).

These values are institutional house-view assumptions and must be identical across every model regardless of which company is being analyzed. Company-specific inputs (beta, revenue, margins, capital structure) are still derived per company, but the **methodology and shared inputs** come from this file.

- If a value in the spec is older than its update cadence, refresh it in the file and add an Update Log entry — do not quietly use a fresher value.
- If the analysis requires deviating from the spec (e.g., a non-USD DCF), document the deviation in the model's notes section.
- Every hardcoded cell drawing from this spec should cite it in the cell comment: `Source: docs/financial-model-assumptions.md §[section]`.

This applies to the `financial-analysis:*`, `investment-banking:*`, `equity-research:*`, `pitch-agent:*`, and `market-researcher:*` plugin skills as well — they live in the plugin cache and shouldn't be edited directly, so this AGENTS.md directive is the binding override.

## Excel Conventions

When building or editing any `.xlsx` workbook, **always use formulas instead of hardcoded values** for calculated cells. Only raw source data (e.g., a company's reported revenue typed from a filing) may be entered as a literal number. Every intermediate calculation, subtotal, ratio, and output cell must be a formula referencing its inputs. This applies to all spreadsheet-producing skills (`xlsx`, `financial-analysis:*`, `investment-banking:*`, `equity-research:*`, `pitch-agent:*`, `gl-reconciler:*`, `market-researcher:*`).

## Agent tooling

Adam's personal Claude Code configuration (`.claude/`) is local-only and gitignored in this repo;
nothing in it is needed to take a course. Office-document work uses the standard Claude `docx` /
`xlsx` / `pptx` / `pdf` skills from your own Claude Code install.
