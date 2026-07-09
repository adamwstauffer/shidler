# BUS-314 ACCOUNTING RATIOS PROJECT — DIRECTORY CLEANUP & ALIGNMENT

## Decision Memo

**Prepared by:** Adam W. Stauffer (draft by Claude Code)
**Date:** March 25, 2026
**Status:** Draft — Pending Review
**Scope:** BUS-314 International Business Finance, Accounting Ratios Project

---

## 1. SUMMARY

This memo documents housekeeping and structural changes to the BUS-314 accounting ratios project, aligning it with the conventions established in the FIN-321 reorganization (`FIN-321/_decisions/2026-03-25-fin321-project-reorganization.md`):

1. **Move templates** from `accounting-ratios/` to course-level `_templates/` and rename memo template
2. **Remove stale due dates** ("TBD" placeholders) from stage assignment files
3. **Update file references** across stage assignments to new template locations
4. **Add student guidance** on deliverable save locations and GitHub commit workflow
5. **Fix Laulima references** to Lamaku throughout course README
6. **Update deliverable formats** to Markdown committed to GitHub (remove PDF option)
7. **Standardize filename convention** to `lastname-first-stageN-deliverable`
8. **Add Lamaku reference** for spreadsheet template sourcing in Stage 2
9. **Populate empty** `_spreadsheets/README.md`

---

## 2. CHANGES MADE

### Templates Moved
- `accounting-ratios/template-memo.md` → `_templates/template-decision-memo.md`
- `accounting-ratios/template-spec.md` → `_templates/template-spec.md`

### Stage File Updates
- Stage 1: template reference updated, deliverable format to `.md` on GitHub, filename convention, save location guidance, removed TBD date
- Stage 2: filename convention, Lamaku spreadsheet template reference, save location guidance, removed TBD date
- Stage 3: template reference updated, removed TBD date
- Stage 4: removed TBD due date
- Extra credit: removed TBD due date

### Project README Updates
- Removed due date column from deliverables table
- Updated directory tree (templates moved, scenarios added)
- Updated Getting Started instructions (scenario assignment, template paths, Lamaku, commit guidance)
- Added "Committing Your Work" section with recommended save locations

### Course README
- All "Laulima" references → "Lamaku"
- Laulima URL → Lamaku URL

---

## 3. CROSS-COURSE ALIGNMENT

Both BUS-314 and FIN-321 now follow identical conventions:

| Convention | BUS-314 | FIN-321 |
|-----------|---------|---------|
| Template location | `_templates/` | `_templates/` |
| Memo template name | `template-decision-memo.md` | `template-decision-memo.md` |
| Decision memo location | `_decisions/` | `_decisions/` |
| Stage count | 4 | 4 |
| Filename convention | `lastname-first-stageN-*` | `lastname-first-stageN-*` |
| Deliverable format | `.md` on GitHub | `.md` on GitHub |
| LMS reference | Lamaku | Lamaku |

---

**Document Version:** 1.0
**Last Updated:** March 25, 2026
**Author:** Adam W. Stauffer (draft by Claude Code)
