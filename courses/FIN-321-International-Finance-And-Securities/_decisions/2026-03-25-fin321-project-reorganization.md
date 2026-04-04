# FIN-321 FX HEDGING PROJECT — DIRECTORY REORGANIZATION & STAGE CLEANUP

## Decision Memo

**Prepared by:** Adam W. Stauffer (draft by Claude Code)
**Date:** March 25, 2026
**Status:** Draft — Pending Review
**Scope:** FIN-321 International Finance & Securities, FX Hedging Project

---

## 1. SUMMARY

This memo documents several housekeeping and structural changes to the FIN-321 FX hedging project:

1. **Move templates** from `project-fx-hedging/` to `_templates/` and rename the memo template to `template-decision-memo.md`
2. **Archive Stage 4 (Prompt Engineering)** — fold prompt engineering into Stage 5 rather than maintaining it as a standalone deliverable
3. **Remove stale due dates** from all stage assignment files (e.g., "October 24", "November 7")
4. **Update file references** across stage assignments to reflect new template and directory locations
5. **Add student guidance** on where to save deliverables (`.md` memos to `docs/decisions/`, `.xlsx` templates to `docs/templates/excel/`)
6. **Update spreadsheet template sourcing** to reference Lamaku instead of a specific skeleton file

---

## 2. CURRENT STATE (Pre-Change)

### Directory Structure

```
courses/FIN-321-International-Finance-And-Securities/
├── _templates/
│   └── excel/
│       └── README-v2.md
├── archive/
│   └── (historical materials)
└── project-fx-hedging/
    ├── README.md
    ├── scenarios.md
    ├── stage1-memo-assignment.md
    ├── stage2-excel-build-assignment.md
    ├── stage3-spec-assignment.md
    ├── stage4-prompt-engineering.md    ← standalone stage
    ├── stage5-final-rec.md
    ├── template-memo.md               ← in project directory
    └── template-spec.md               ← in project directory
```

### Issues

- Templates lived inside `project-fx-hedging/` instead of `_templates/`, inconsistent with the repo convention where `_`-prefixed directories hold reusable/system content
- `template-memo.md` was generically named; the memo template serves a decision-memo purpose and should be labeled accordingly
- Stage 4 (Prompt Engineering) existed as a standalone 4-point deliverable, creating an artificial boundary between the prompt and the analysis it supports
- All stage files contained hardcoded due dates from a prior semester (Fall 2025), which would confuse students in future semesters
- Stage files referenced stale template paths (`fin-321/memo-template.md`, `fin-321/stage3-spec-template.md`)
- No guidance on where students should save deliverables within their own repositories

---

## 3. PROPOSED CHANGES

### 3A. Move Templates to `_templates/`

**Before:**
- `project-fx-hedging/template-memo.md`
- `project-fx-hedging/template-spec.md`

**After:**
- `_templates/template-decision-memo.md`
- `_templates/template-spec.md`

**Rationale:** Aligns with the repo convention established in `docs/decisions/2026-02-15-repo-hierarchy.md` where `_`-prefixed directories hold reusable organizational content. Templates are not project-specific artifacts — they serve multiple stages and could be reused across projects or semesters.

**Risks:** Existing links or student bookmarks to old paths will break. **Mitigation:** Stage assignment files updated with new paths; old paths no longer exist so any stale reference will produce a clear "file not found" rather than a silent mismatch.

### 3B. Archive Stage 4 (Prompt Engineering)

**Before:** Stage 4 was a standalone 4-point deliverable requiring a structured AI prompt and an AI-generated spreadsheet.

**After:** `stage4-prompt-engineering.md` moved to `archive/`. Prompt engineering skills are integrated into Stage 5 (Final Analysis & Recommendation). Students who use AI document their prompt as part of the final deliverable.

**Rationale:**
- **Mirrors BUS-314 precedent.** The BUS-314 restructure (see `docs/decisions/2026-02-24-bus314-stage-restructure.md`) merged prompt engineering into the final stage for the same reasons.
- **Prompt engineering is a skill, not a standalone deliverable.** Evaluating the prompt alongside the analysis it produces is more authentic than grading it in isolation.
- **Reduces deliverable fatigue.** Five stages is heavy for one project; four active stages (1, 2, 3, 5) is a tighter pipeline.
- **AI use remains optional.** Students who do not use AI simply write the final analysis from their Stage 2 model, as already permitted.

**What is preserved:** Prompt engineering best practices, rubric criteria for AI-readiness, and the expectation of structured prompts all remain accessible in the archived file and can be referenced in Stage 5 instructions.

**Risks:** Prompt engineering may receive less explicit attention. **Mitigation:** Stage 5 already includes extra credit for AI-related discussion (Claude Skills, Code Interpreter, multi-file reasoning).

### 3C. Remove Stale Due Dates

All hardcoded due dates removed from stage files:
- Stage 1: "October 24" removed
- Stage 2: "November 7" removed
- Stage 3: "November 20" removed
- Stage 4: "December 12, 2025" (archived)
- Stage 5: "December 12, 2025" removed

**Rationale:** Dates are semester-specific and belong in the course syllabus (README.md) or LMS, not baked into reusable assignment files.

### 3D. Update Template References in Stage Files

| Stage File | Old Reference | New Reference |
|-----------|---------------|---------------|
| `stage1-memo-assignment.md` | `fin-321/memo-template.md` | `_templates/template-decision-memo.md` |
| `stage3-spec-assignment.md` | `fin-321/stage3-spec-template.md` | `_templates/template-spec.md` |

### 3E. Add Deliverable Save Location Guidance

New guidance added to stage files directing students on repository organization:

| Stage | Guidance Added |
|-------|---------------|
| Stage 1 (Memo) | Save `.md` memo to `shidler/docs/decisions/` |
| Stage 2 (Excel) | Save `.xlsx` template to `shidler/docs/templates/excel/` |

### 3F. Update Spreadsheet Template Sourcing

Stage 2 previously referenced "the provided Stage 2 Skeleton." Updated to: "the Spreadsheet template provided in class and available in Lamaku."

**Rationale:** The skeleton files are distributed via the LMS, not the repo. The instruction should point students to the authoritative source.

---

## 4. POST-CHANGE STRUCTURE

```
courses/FIN-321-International-Finance-And-Securities/
├── _decisions/
│   └── 2026-03-25-fin321-project-reorganization.md   ← this memo
├── _templates/
│   ├── excel/
│   │   └── README-v2.md
│   ├── template-decision-memo.md                      ← moved & renamed
│   └── template-spec.md                               ← moved
├── archive/
│   ├── stage4-prompt-engineering.md                    ← archived
│   └── (historical materials)
└── project-fx-hedging/
    ├── README.md                                       ← updated
    ├── scenarios.md
    ├── stage1-memo-assignment.md                       ← updated
    ├── stage2-excel-build-assignment.md                ← updated
    ├── stage3-spec-assignment.md                       ← updated
    └── stage4-final-analysis-assignment.md               ← renamed from stage5, rewritten
```

### Active Stage Sequence

| Stage | Deliverable | Points |
|-------|------------|--------|
| 1 | Executive Memo | 4 |
| 2 | Excel Model Build | 6 |
| 3 | Technical Specification | 4 |
| 4 | Final Analysis, Prompt Engineering & Recommendation | 10 |
| **Total** | | **24** |

---

## 5. CROSS-COURSE ALIGNMENT

| Stage | BUS-314 | FIN-321 |
|-------|---------|---------|
| 1 | Memo | Memo |
| 2 | Excel Build | Excel Build |
| 3 | Spec (post-build) | Spec (post-build) |
| 4 | Final Analysis + Prompt | Final Analysis + Prompt |

Both courses now follow the same **Build → Document → Analyze** workflow with identical 4-stage structure.

---

## 6. ADDITIONAL CLEANUP ITEMS IDENTIFIED

| Item | Location | Issue | Recommended Action |
|------|----------|-------|--------------------|
| ~~Stale `2025` year references~~ | ~~`stage5-final-rec.md`~~ | Resolved — file renamed to `stage4-final-analysis-assignment.md` and fully rewritten | Complete |
| `README-v2.md` in `_templates/excel/` | `_templates/excel/README-v2.md` | Versioned filename suggests an earlier README exists or the naming is inconsistent | Rename to `README.md` or archive the v1 |
| Archive directory structure | `archive/` | Contains subdirectories (`analysis/`, `assignments/`, `deliverables/`, `figures/`, `prompts/`, `specs/`) with mostly placeholder READMEs | Consider consolidating or removing empty placeholder READMEs |
| `scenarios.md` placeholder values | `project-fx-hedging/scenarios.md` | Market data fields contain placeholders ("look up current spot") | Clarify whether placeholders are intentional (students fill in) or need updating |
| Course README stage count | `README.md` (root) | May still reference 5-stage project | Verify and update to reflect 4 active stages |
| Root `CLAUDE.md` stage description | `CLAUDE.md` | References FIN-321 as a 5-stage project | Update to reflect archived Stage 4 |

---

## 7. RECOMMENDATION

Proceed with all changes as documented. The reorganization:

- Aligns FIN-321 with the repo's `_`-prefixed directory convention for reusable content
- Follows the BUS-314 precedent for merging prompt engineering into the final stage
- Eliminates semester-specific dates from reusable assignment files
- Gives students clear guidance on where to save deliverables in their repositories
- Points students to the correct template source (Lamaku) for spreadsheet work

---

**Document Version:** 1.0
**Last Updated:** March 25, 2026
**Author:** Adam W. Stauffer (draft by Claude Code)
