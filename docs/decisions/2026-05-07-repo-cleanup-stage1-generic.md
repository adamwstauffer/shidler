---
title: "Repo Cleanup — Stage 1: Generic / Cross-Course Changes"
date: 2026-05-07
status: proposed
owner: Adam W. Stauffer
scope: repo-wide
related:
  - 2026-02-15-repo-hierarchy.md
  - bus629/2026-05-07-bus629-stage2-restructure.md
---

# Repo Cleanup — Stage 1: Generic Changes

## Summary

Before making BUS-629–specific changes (Stage 2), tighten and standardize the repo-wide foundation: consolidate templates at the repo level, fix the public-facing README, remove broken/legacy template files, flatten over-nested directories, and adopt a single date-prefixed naming convention for all memos and specs. These are mechanical, low-risk changes that course-level work can safely build on.

## Context

The repo currently has:

- **Duplicate templates** — `docs/templates/memo-template.md` and `docs/templates/spec-template.md` exist at the repo level *and* are duplicated inside `courses/BUS-629-VEMBA-International-Corporate-Finance/docs/templates/`. Future courses will repeat this drift.
- **A broken/orphan template README** — `docs/templates/README-broken.md` (legacy) sits alongside `docs/templates/README.md` (active).
- **Two stale example files** in `docs/templates/` — interest-rate-parity spec/prompt examples that pre-date the current spec convention.
- **An over-nested portfolio directory** — `docs/templates/bio-and-resume/{bio,resume}/`, where `resume/` contains only a `RESUME.md` and `README.md`. The intermediate `bio-and-resume/` and `resume/` levels add navigation cost without payoff.
- **A public README** that calls strategic decisions "Decision Records," lists a clone command students don't need, omits the Vietnam EMBA campus addresses, and has no on-ramp for students who want to extend project work into their own portfolio.
- **A CV** missing LinkedIn and GitHub identifiers — the two primary links a recruiter or student looks for first.
- **No machine-readable frontmatter on Markdown templates**, so an LLM has to read the body to figure out what each template is for.

## Decisions

### 1. Verify `.claude/` is the only Claude Code directory in root

`.claude/` already exists at the repo root with skills and settings. A check confirmed there is **no** `claude/` (un-dotted) directory in the working tree — only a `claude` git **branch** in `.git/refs/`. No file move is needed.

- **Action:** No-op. If the original intent was to move a `claude/` *branch* of work into `.claude/`, that needs separate clarification.
- **Rationale:** `CLAUDE.md` must stay in repo root so Claude Code auto-loads it; do not move it.

### 2. Consolidate course-level templates to the repo level

- **Action:** Move `courses/BUS-629-VEMBA-International-Corporate-Finance/docs/templates/{memo-template.md, spec-template.md, README.md}` up to `docs/templates/`. Delete the now-empty `courses/.../docs/templates/` directory.
- **Action:** Update the BUS-629 course README's "Memo Template" / "Spec Template" links to point to `../../docs/templates/memo-template.md` and `../../docs/templates/spec-template.md`.
- **Action:** Audit other courses (BUS-313, BUS-314, FIN-321, BUS-620, BUS-122B) for any course-local copies of repo-level templates. Replace with relative links to `docs/templates/`.
- **Rationale:** Single source of truth. When the memo template evolves, every course inherits the change.

### 3. Add YAML frontmatter to all Markdown templates

Every file in `docs/templates/*.md` gets a frontmatter block:

```yaml
---
template: memo            # one of: memo, spec, case-brief, prompt-log, ...
purpose: "Stage 1 executive memo — problem framing and recommendation"
audience: student
fields_required: [title, author, date, summary, recommendation]
naming_convention: "YYYY-MM-DD-{slug}.md"
---
```

- **Action:** Add frontmatter to `memo-template.md`, `spec-template.md`, `case-brief-template.md`, `prompt-log-template.md`, and any newly imported templates.
- **Action:** Document the frontmatter schema in `docs/templates/README.md` so students and LLMs both know what to expect.
- **Rationale:** Discoverability for LLM-assisted workflows (Stage 4 of the BUS-629 project explicitly uses an LLM to draft specs against templates) and lower onboarding cost for students.

### 4. Add a "File Naming Conventions" section to template README

Document, in one place, the convention used across the repo:

- Memos & specs: `YYYY-MM-DD-{slug}.md` (lowercase slug, hyphen-separated)
- Student spreadsheet deliverables: `YYYY-MM-DD-{company-slug}-financials.xlsx`
- Stage assignment files: `stageN-{slug}-assignment.md` (or `stageN-{slug}.md` where already established)

- **Action:** Add the section to `docs/templates/README.md` and cross-link from each course-level template README that remains.
- **Rationale:** Today the convention is implicit. Making it explicit prevents drift and gives students a single rule to follow.

### 5. Archive legacy template content

Move the following from `docs/templates/` into `_archive/templates/` (preserving git history via `git mv`):

- `prompt-example-interest-rate-parity.md`
- `risk-memo-template.md`
- `spec-example-interest-rate-parity.md`

- **Rationale:** These pre-date the current spec convention. They are useful as historical reference but should not be discoverable from the live templates index.

### 6. Delete `docs/templates/README-broken.md`

- **Action:** `git rm docs/templates/README-broken.md`.
- **Rationale:** Superseded by `docs/templates/README.md`. Keeping the broken copy in the live tree is a footgun for anyone (or any LLM) browsing the directory.

### 7. Flatten `docs/templates/bio-and-resume/`

Current:

```
docs/templates/bio-and-resume/
├── README.md
├── bio/
│   └── README.md
└── resume/
    ├── README.md
    └── RESUME.md
```

Proposed:

```
docs/templates/portfolio/
├── README.md          # merged: bio + resume guidance
├── bio-template.md    # extracted from bio/README.md
├── resume-template.md # renamed from resume/RESUME.md (template form, not Adam's CV)
```

- **Action:** Flatten to `docs/templates/portfolio/`. Eliminate the two intermediate directories.
- **Rationale:** Two extra clicks for one file each is unjustified. A flat folder of templates is easier to scan. `portfolio/` chosen over `bio-and-resume/` because it's a single word, scopes naturally to additional artifacts (cover letters, LinkedIn copy, etc.) without further renames, and matches the recruiter-facing framing students are building toward.

### 8. README.md (root) updates

Apply these edits to `README.md`:

**a. Rename "Decision Records" → "Decision Memos"** (line ~29 and ~84). The directory is `decisions/`, the artifacts are *memos*. "Records" implies after-the-fact log; "memos" reflects the proposal-and-discussion flow already documented in `docs/decisions/README.md`.

**b. Add Vietnam EMBA campus information.** Extend the BUS-629 row (or add a "Campus Locations" subsection under Active Courses) with:

- **Ho Chi Minh City** — Building I, Level 2, Room I2.01, Van Lang University, 69/68 Đặng Thùy Trâm, Ward 13, Bình Thạnh District, HCMC
- **Hanoi** — FPT Headquarters, 10 Phạm Văn Bạch street, Cầu Giấy District, Hanoi

**c. Rewrite "Getting Started"** to drop the clone step (too much for first-time students) and reflect a browser-first GitHub workflow:

```markdown
## Getting Started

1. **Navigate to your course**: Open the appropriate directory under `courses/`
2. **Read the syllabus**: Each course has a `README.md` with objectives, grading, and policies
3. **Work on deliverables**: Follow the staged assignment files in each project folder
4. **Commit your work**: `git add . && git commit -m "Stage 1 memo" && git push`

For a visual walkthrough, see **`docs/presentations/GitHub_AI_Appendix.pptx`**.
```

**d. Add a new "Extending This Work" (or "Further Tools & Templates") section** that, for each course, points students at the additional templates they could create to advance their career:

- Sketch: a small table — `Course → Project → Career-aligned extensions`. E.g., FIN-321 FX hedging students could add: corporate treasury policy memo, exposure dashboard spec, hedging-effectiveness backtest spec; BUS-314 ratios students could add: industry comparison brief, credit-analysis spec, equity-research initiation note template.
- **Open question:** This is a meaningful authoring task on its own. Recommend implementing as a follow-up commit, not bundled into the README rename.

### 9. Single naming convention everywhere: `YYYY-MM-DD-{slug}.md`

- **Action:** Audit `docs/decisions/`, `docs/decisions/bus314/`, `docs/decisions/fin321/`, and (post-rename) `courses/BUS-629-.../docs/decisions/` for files not following the convention. Rename via `git mv` to preserve history.
- **Known offender:** `docs/decisions/fin321/fin321-scenario2-fx-hedging-memo.md` — needs a date prefix.
- **Rationale:** Sortable by date, predictable for tooling, already the norm in most directories.

## Implementation Order

These can ship as discrete PRs / commits in any order, but the suggested sequence minimizes broken links:

1. Add frontmatter to existing `docs/templates/*.md` (additive, breaks nothing).
2. Document naming convention in `docs/templates/README.md`.
3. Delete `README-broken.md`; archive the three legacy files.
4. Flatten `bio-and-resume/`.
5. Move BUS-629 course-level templates → repo level; update BUS-629 README links.
6. Rename `Decision Records` → `Decision Memos` in root README.
7. Rewrite Getting Started; add Vietnam EMBA campus locations.
8. Add "Extending This Work" section (separate commit — content authoring).
9. Rename non-conforming decision memos to `YYYY-MM-DD-` convention.
10. CV: append LinkedIn (`linkedin.com/in/adamwstauffer`) and GitHub (`@adamwstauffer`) under contact line in `CV.md`.

## Out of Scope (deferred)

- BUS-629 stage restructure, `docs/memos` → `docs/decisions` rename, presentation slide updates — covered in [Stage 2 memo](bus629/2026-05-07-bus629-stage2-restructure.md).
- Updating `CLAUDE.md` to reflect any path changes — do this last, after the moves settle.
- Any course-level README updates beyond BUS-629 link-target swaps.

## Resolved (was open)

- **"Extending This Work" content:** drafted by Claude for review. **Not** per-course — centralized and **categorized by career objective** (corporate finance, investment banking, equity research, treasury, FP&A, etc.) so students can find extensions aligned with their target roles regardless of which course they took. ✓
- **`CV.md` vs `RESUME.md`:** LinkedIn/GitHub line on **both**. Already done. ✓
