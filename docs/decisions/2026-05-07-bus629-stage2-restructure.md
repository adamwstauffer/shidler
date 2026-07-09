---
title: "BUS-629 Restructure — Stage 2: Course-Specific Changes"
date: 2026-05-07
status: accepted
owner: Adam W. Stauffer
course: BUS-629-VEMBA-International-Corporate-Finance
scope: course
depends_on:
  - ../2026-05-07-repo-cleanup-stage1-generic.md
related:
  - 2026-04-03-bus629-accounting-ratios-project-design.md  # currently in courses/.../docs/memos/, will move
refined_by:
  - 2026-05-12-bus629-stage2-5-followup-revisions.md  # Spring 2026 cohort overlay (Stage 2 memo-only this cohort; Stage 4 HIL requirement; Stage 5 verification + retrospective + feedback-incorporation lines)
---

> **Status note (added 2026-05-13):** This memo is the durable structural blueprint for BUS-629 stages 0–5 and is in effect. The Spring 2026 cohort runs against a narrower scope captured in [`2026-05-12-bus629-stage2-5-followup-revisions.md`](2026-05-12-bus629-stage2-5-followup-revisions.md) — most notably, Stage 2 is memo-only for this cohort (the 70/30 deliverable/presentation split documented in §3 below resumes in AY 2026–27). See the May 12 memo for the full Spring 2026 deviations.

# BUS-629 Restructure — Stage 2: Course-Specific Changes

## Summary

After the Stage 1 generic cleanup lands (templates consolidated, naming convention adopted, decision-memo language standardized), restructure BUS-629 to: (1) make Stage 0 a true *infrastructure* stage where students stand up their own GitHub repo, (2) provide a generic Excel template at Stage 1 instead of asking each student to design one, (3) defer full ratio analysis from Stage 3 to Stage 5 so Stage 3 is a clean financials-upload, (4) make the Stage 4 spec an LLM-drafted artifact (with both desktop and CLI workflows documented), (5) bump Stage 5 weight and add a GitHub-structure rubric component, (6) align internal directory names (`memos` → `decisions`) with the rest of the repo, and (7) revise the project presentation to match.

## Context

Current BUS-629 stage layout (from `courses/BUS-629-VEMBA-International-Corporate-Finance/README.md`):

| Stage | Deliverable | Weight |
|------:|-------------|-------:|
| 0 | Repository Setup & Infrastructure | 5% |
| 1 | Template Architecture | 20% |
| 2 | Company Selection Memo | 10% |
| 3 | Model Population & Validation | 25% |
| 4 | Technical Specification | 20% |
| 5 | LLM Analysis & Executive Evaluation | 20% |

Issues observed in pilot design:

- Stage 1 asks every student to design a ratios template from scratch before they have built one. High variance in output quality; not the skill we are trying to assess in this course.
- Stage 3 conflates *getting financials in* with *analyzing them*, leaving Stage 5 thin.
- Stage 4 spec writing is taught generically, not tied to the LLM workflow that motivates the course.
- Course-internal directory names (`docs/memos`, `docs/templates`) diverge from the repo-level convention (`docs/decisions`, `docs/templates` at root).
- The presentation deck (`BUS629_AI_Ratios_Project.pptx`) shows the current stage layout and will be out-of-date after the restructure.

## Decisions

### 1. Rename `courses/BUS-629-.../docs/memos/` → `docs/decisions/`

- **Action:** `git mv` the directory; update internal links in BUS-629 README, stage docs, and `2026-04-03-bus629-accounting-ratios-project-design.md`.
- **Rationale:** Aligns with repo-level `docs/decisions/`. "Memo" is the artifact *type*; "decisions" is the *purpose*. Decision memos and design memos both live here; non-decision memos (none currently) would need a different home, but there are none.

### 2. Restructure stages

The stage names below intentionally use the existing "Stage" terminology rather than "Phase" used in the brainstorm — the course README, all stage filenames, and the presentation already say "Stage." If a global Stage→Phase rename is desired, treat that as a separate decision.

| Stage | Deliverable | Weight | Change |
|------:|-------------|-------:|--------|
| 0 | Personal GitHub repo with README, RESUME, BIO + intro to commit/push/pull | 5% | **Reframed** — student creates their own public `Corporate Finance` repo |
| 1 | Provided generic Excel template (IS / BS / CF / Ratios + cover + legend) — student uploads their copy | 20% | **Reframed** — instructor provides skeleton; student demonstrates they can use it |
| 2 | Company selection memo (`.md`) | 10% | Process change — uses repo memo template, `YYYY-MM-DD-` naming, lives in their `docs/decisions/` |
| 3 | Populated financials spreadsheet for selected company | **20%** | **Scope reduced** — financials only, no full analysis. Drops 5 pts to fund Stage 5. |
| 4 | LLM-drafted technical spec (`.md`) | 20% | Process change — student uses an LLM (Claude desktop *or* CLI) to draft the spec from project instructions + Stage 1 template |
| 5 | Pull-it-all-together: full analysis + LLM evaluation + repo polish | **25%** | Bumped from 20%; adds GitHub-structure rubric component |

Total still 100%.

#### Stage 0 — student repo creation

- **Deliverable:** GitHub repo URL submitted via Lamaku.
- **Required contents at submission:** root `README.md`, `RESUME.md`, `BIO.md`. (Templates for these come from the repo-level `docs/templates/portfolio/` after the Stage 1 generic cleanup.)
- **Instructions cover:**
  - Creating directories and READMEs manually in the GitHub web UI.
  - Same actions via Claude Code CLI / Claude desktop app.
  - High-level explanation of `commit`, `push`, `pull`.
- **Rationale:** Course goal includes GitHub fluency; the existing Stage 0 already gestures at this but treats infrastructure as a checklist. Making the deliverable an actual hosted repo URL forces the workflow.

#### Stage 1 — provided Excel template

- **Deliverable:** Student uploads their copy of the template to their repo (no modifications required at this stage).
- **Template contents (instructor-built, lives in repo):**
  - Cover / instructions page
  - Legend & key (color coding, named-range conventions)
  - Income Statement skeleton
  - Balance Sheet skeleton
  - Cash Flow skeleton
  - Ratios tab — **formulas pre-filled** against the named-range references on the IS / BS / CF tabs, so ratios auto-populate once Stage 3 financials are entered
- **Storage:** `docs/templates/spreadsheets/performance-ratios-template.xlsx` at the **repo level** (per Stage 1 generic cleanup principle: shared assets live at repo root). Cross-link from BUS-629 README and Stage 1 instructions.
- **Rationale:** Eliminates "design a template" as an upstream gate on the analytical work that actually develops the course's learning objectives.

#### Stage 2 — company selection memo

- **Deliverable:** `.md` file in student's `docs/decisions/` named `YYYY-MM-DD-{slug}.md`.
- **Template:** repo-level `docs/templates/memo-template.md` (post Stage 1 cleanup).
- **No weight change.**

#### Stage 3 — financials only

- **Deliverable:** populated `.xlsx` named `YYYY-MM-DD-{company-slug}-financials.xlsx`.
- **Scope:** Income Statement, Balance Sheet, Cash Flow populated for selected company. Ratios tab will auto-populate from the pre-filled formulas (Stage 1 decision) — students are not asked to interpret ratios yet, only to verify the numbers tie to the source 10-K.
- **Weight: 20%** (down from 25%).
- **Rationale:** Full analysis is deferred to Stage 5. This:
  1. Forces students to actually use the LLM-drafted spec (Stage 4) to drive the Stage 5 analysis, instead of pre-baking conclusions.
  2. Keeps Stage 3 grading objective (the numbers tie to the source 10-K or not).
  3. Makes Stage 5 substantive enough to justify the weight bump.

#### Stage 4 — LLM-drafted spec

- **Deliverable:** `.md` spec in student's `docs/specs/`, named `YYYY-MM-DD-{slug}.md`.
- **Template:** repo-level `docs/templates/spec-template.md`.
- **Process change:** Student uses an LLM to *draft* the spec, conditioned on:
  - The project instructions (this README + Stage 4 brief)
  - Their Stage 1 Excel template (or a shared link to it)
- **Two workflows documented in stage instructions:**
  - **Desktop (Claude / ChatGPT web):** upload the project instructions PDF/MD and the Excel file, then prompt with the spec template structure.
  - **CLI (Claude Code):** point at GitHub raw URLs for the project instructions and template, then prompt to draft against the spec template in the student's repo.
- **Required artifact:** the spec, plus a brief prompt log entry showing the prompt(s) used.
- **Rationale:** This is the course's signature pedagogical move — make the LLM's role in spec writing explicit, observable, and graded.

#### Stage 5 — synthesis + repo polish

- **Deliverable:** Link to GitHub repo (no upload — final state of the repo *is* the deliverable).
- **Contents:** Full ratio analysis (deferred from Stage 3), LLM-generated executive evaluation against the Stage 4 spec, and a polished repo (READMEs in every directory, decision memos, naming conventions followed).
- **Weight: 25%** (up from 20%).
- **Rubric addition:** explicit % allocation for GitHub directory structure, READMEs, and naming convention compliance. Suggested split (within the 25%):
  - Analytical correctness: 12%
  - Executive evaluation quality: 8%
  - Repo polish (structure, READMEs, naming): 5%
- **Rationale:** The portfolio artifact is the long-tail value of this course — students leave with a public repo to point employers at. Grading the repo as a deliverable (not just the contents) reinforces that.

### 3. Add presentation-scoring component to Stages 2, 4, 5 only

Stages 0, 1, 3 are upload-only deliverables (repo URL, template upload, financials upload) — they have no in-class presentation moment, so a presentation rubric line for those stages would be rubric theatre. Stages 2, 4, 5 do involve student presentation of the work.

- **Decision:** **70% deliverable / 30% presentation** split within Stages 2, 4, 5. No total math change; redistribution stays inside each stage's existing weight.
- **Action:** Update `stage2-company-selection-memo.md`, `stage4-technical-specification.md`, `stage5-llm-analysis-evaluation.md` with the 70/30 sub-rubric.
- **Action:** Stage docs 0, 1, 3 explicitly note "Upload-only deliverable — no presentation component" so the asymmetry is intentional and visible.
- **Rationale:** Aligns rubric with what actually happens in class. 30% is enough to make presentation matter; 70% keeps analytical substance dominant.

### 4. Revise `BUS629_AI_Ratios_Project.pptx`

- **Action:** Update the project deck to reflect the revised stage layout (titles, deliverables, weights, the LLM-spec workflow at Stage 4, the repo-as-deliverable framing at Stages 0 and 5).
- **Trigger via:** `/pptx` skill once decisions in this memo are accepted.
- **Out of scope here:** the actual slide edits (this is a decision memo, not an implementation plan).

### 5. Update BUS-629 README

After the above lands:

- Update the stage table with new weights.
- Replace `docs/memos/...` paths with `docs/decisions/...`.
- Repoint Memo / Spec template links to the repo-level `docs/templates/`.
- Update the Repository Structure tree (the `docs/memos/` line becomes `docs/decisions/`).
- Add a "Provided Templates" subsection pointing students at the repo-level Excel template introduced in Stage 1.

## Resolved (was open)

- **Excel template location:** `docs/templates/spreadsheets/` — new subdirectory. ✓
- **Excel template filename:** `performance-ratios-template.xlsx`. ✓
- **Presentation rubric math:** 70/30 deliverable/presentation split, applied only to Stages 2, 4, 5. No total weight rebalancing. ✓
- **Cohort timing:** next VEMBA cohort starts **2026-05-14** (one week from this memo). Implementation must complete before then. The minimum viable cut for Day 1 is: BUS-629 README accurate, Stage 0 instructions ready, Stage 1 instructions + Excel template available. Stages 2–5 can land iteratively in the first weeks of the cohort. ✓

## Implementation Order

Sequence to minimize broken links and ensure templates exist before they are referenced:

1. Confirm Stage 1 generic cleanup PR has merged (templates at repo level, frontmatter present, naming convention documented).
2. Build and commit the repo-level Excel template (Stage 1 provided template).
3. `git mv courses/BUS-629-.../docs/memos courses/BUS-629-.../docs/decisions`; update inbound links.
4. Rewrite each `stageN-*.md` file to reflect the new deliverables, weights, and presentation rubric.
5. Update BUS-629 README (stage table, structure tree, link targets).
6. Update `BUS629_AI_Ratios_Project.pptx` via `/pptx`.
7. Update `CLAUDE.md` references to the BUS-629 directory layout if any.
