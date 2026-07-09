# BUS-314 ACCOUNTING RATIOS PROJECT — STAGE RESTRUCTURE
## Decision Memo

**Prepared by:** Adam W. Stauffer (draft by Claude Code)
**Date:** February 24, 2026
**Status:** Draft — Pending Review
**Scope:** BUS-314 International Business Finance, Accounting Ratios Project

---

## 1. SUMMARY

This memo evaluates three proposed changes to the BUS-314 accounting ratios project:

1. **Reorder Stages 2 and 3** — Move Excel Build before Technical Specification
2. **Merge Stage 4 into Stage 5** — Combine Prompt Engineering with Final Analysis & Recommendation
3. **Consolidate the project-level CLAUDE.md** — Reduce redundancy with README.md

These changes would reduce the project from five stages to four, align BUS-314 with the FIN-321 stage order established in PR #16, and simplify the student deliverable pipeline without sacrificing learning objectives.

---

## 2. CURRENT STATE

### BUS-314 Stage Sequence (5 stages, 24 points + 3 EC)

| Stage | Deliverable | Points | Purpose |
|-------|------------|--------|---------|
| 1 | Executive Memo | 4 | Frame the problem and company choice |
| 2 | Technical Specification | 6 | Plan the model in pseudocode |
| 3 | Excel Model Build | 4 | Construct the working spreadsheet |
| 4 | Prompt Engineering | 4 | Translate model into AI-executable prompt |
| 5 | Final Analysis & Recommendation | 6 | Interpret ratios, recommend to CFO |

### FIN-321 Stage Sequence (already reordered via PR #16)

| Stage | Deliverable | Points |
|-------|------------|--------|
| 1 | Executive Memo | 4 |
| 2 | **Excel Model Build** | **6** |
| 3 | **Technical Specification** | **4** |
| 4 | Prompt Engineering | 4 |
| 5 | Final Analysis & Recommendation | 6 |

FIN-321 swapped Excel and Spec and adjusted points to weight the build higher.

---

## 3. PROPOSED CHANGES

### 3A. Reorder: Excel Build Before Technical Specification

**Current:** Memo → Spec → Excel → Prompt → Final
**Proposed:** Memo → **Excel** → **Spec** → ...

**Rationale:**

- **Build-first pedagogy.** Students learn by doing. Writing a specification for a model they haven't built is abstract; writing one after building is reflective. The FIN-321 post-build spec explicitly includes a "Model Review — What Worked & What to Improve" section that only exists because students have hands-on experience to draw from.
- **Reduces the abstraction barrier.** BUS-314 students are undergraduates encountering financial modeling for the first time. Asking them to plan 25+ ratio formulas in pseudocode before touching Excel creates a high cognitive barrier. Building first gives them concrete experience to articulate.
- **Cross-course consistency.** FIN-321 already uses this order. Students who take both courses (FIN-321 requires BUS-314 as a prerequisite) will encounter a consistent workflow.
- **Spec quality improves.** Post-build specs are more precise because students know which inputs are tricky, where judgment calls are needed, and what they'd do differently — exactly the reflective thinking we want to develop.

**Risks:**

- Students may build poorly structured models without a plan. **Mitigation:** The Stage 1 memo already identifies ratio categories, data sources, and next steps, providing enough framing. The Excel template (`_templates/excel/`) provides structural scaffolding.
- Breaks the "plan before build" paradigm common in software engineering. **Counterpoint:** This is a finance course, not a software engineering course. The goal is financial literacy and analytical judgment, not waterfall methodology.

### 3B. Merge: Prompt Engineering Into Final Analysis

**Current:** Stages 4 (Prompt, 4 pts) and 5 (Final Analysis, 6 pts) are separate.
**Proposed:** Combine into a single **Stage 4: Final Analysis, Prompt Engineering & Recommendation**.

**Rationale:**

- **Natural integration.** Stage 5 already tells students: "Have your LLM generate a draft based on your Stage 3/4 spreadsheet output, then refine it." The prompt engineering is already positioned as a tool for the final analysis — separating them creates an artificial boundary.
- **Reduces deliverable fatigue.** Five stages for one project is a lot for an undergraduate course. Four stages (memo → build → spec → final) is a tighter, more manageable pipeline.
- **Prompt engineering is a skill, not a standalone deliverable.** The prompt matters insofar as it produces useful output. Evaluating the prompt alongside its output (the final analysis) is more authentic than grading the prompt in isolation.
- **Mirrors real-world workflow.** Analysts don't submit a prompt and then separately submit the analysis. They use AI as part of the analytical process and deliver the result.

**What gets preserved:**

- The structured prompt deliverable (Deliverable 1 from current Stage 4) becomes a required component of the merged stage — students still write the prompt as a `.md` file.
- Prompt engineering best practices (hierarchical structure, explicit variables, named ranges) remain in the assignment instructions.
- The AI-generated spreadsheet (Deliverable 2 from current Stage 4) becomes optional or extra credit — the human-built Stage 2 model is the primary spreadsheet artifact.

**What changes:**

- The prompt is evaluated as part of the final deliverable, not independently.
- Students who don't use AI simply write the final analysis from their Stage 2 model, as already permitted in the current Stage 5 instructions.

**Risks:**

- Prompt engineering skills may receive less attention if bundled. **Mitigation:** Weight the prompt component explicitly in the rubric (e.g., 2 of 8 points).
- Grading complexity increases for one stage. **Mitigation:** Use a clear rubric with separate line items for analysis, prompt quality, and recommendations.

### 3C. Consolidate CLAUDE.md Into README.md

The project currently has both `README.md` (student-facing) and `CLAUDE.md` (AI-context) with overlapping content (ratio categories, project structure, stage descriptions).

**Options:**

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| A — Keep separate, trim CLAUDE.md | Remove overlapping content from CLAUDE.md; keep only formula pseudocode, named ranges, and "How to Help Students" | Clean separation of audiences | Two files to maintain |
| B — Merge into README.md | Add a collapsed `<details>` section or appendix to README with AI-specific context | Single source of truth | README gets longer; students see AI instructions |
| C — Keep as-is | No changes | No work | Ongoing redundancy and drift risk |

**Recommendation:** Option A. The formula pseudocode and named-range conventions in CLAUDE.md are genuinely useful for AI assistants and would clutter the student-facing README. But the ratio categories list, project overview, and directory structure should only live in the README. Trim CLAUDE.md to ~40 lines: formulas, named ranges, and scaffolding guidance.

---

## 4. PROPOSED NEW STRUCTURE

### Stage Sequence (4 stages, 24 points + 3 EC)

| Stage | Deliverable | Points | Change |
|-------|------------|--------|--------|
| 1 | Executive Memo | 4 | Unchanged |
| 2 | Excel Model Build | 6 | Promoted from Stage 3; points increased from 4 to 6 |
| 3 | Technical Specification | 4 | Demoted from Stage 2; points decreased from 6 to 4; gains post-build reflection section |
| 4 | Final Analysis, Prompt Engineering & Recommendation | 10 | Merged Stages 4+5; prompt is a required component |

**Point redistribution:** 4 + 6 + 4 + 10 = 24 (unchanged total).

The Excel Build receives more weight because it is now the primary construction stage rather than a specification follow-through. The Spec receives less weight because it shifts from a planning document to a reflective/documentation artifact. The merged final stage carries the combined weight and evaluates the full analytical pipeline.

### Proposed Stage 4 Rubric

| Criterion | Description | Points |
|-----------|-------------|-------:|
| Ratio Interpretation | Demonstrates understanding of what ratios reveal | 2 |
| Strategic Recommendations | Actionable, data-supported recommendations | 2 |
| Du Pont Analysis | Meaningful decomposition and discussion | 1 |
| Structured AI Prompt | Clear, complete, reproducible prompt with all financial data | 2 |
| Professionalism & Communication | Executive-ready, well-structured deliverable | 1 |
| AI-Generated Output OR Manual Analysis | Working spreadsheet from prompt, or equivalent manual work | 2 |

### File Renaming

| Current | Proposed |
|---------|----------|
| `stage2-spec-assignment.md` | `stage3-spec-assignment.md` |
| `stage3-excel-build-assignment.md` | `stage2-excel-build-assignment.md` |
| `stage4-prompt-engineering.md` | Merged into `stage4-final-analysis-assignment.md` |
| `stage5-final-rec.md` | Merged into `stage4-final-analysis-assignment.md` |

---

## 5. CROSS-COURSE ALIGNMENT

After this change, BUS-314 and FIN-321 would share a common 4-stage pattern:

| Stage | BUS-314 | FIN-321 |
|-------|---------|---------|
| 1 | Memo | Memo |
| 2 | Excel Build | Excel Build |
| 3 | Spec (post-build) | Spec (post-build) |
| 4 | Final Analysis + Prompt | Final Analysis + Prompt* |

*FIN-321 currently retains a separate Stage 4 (Prompt) and Stage 5 (Final). If the BUS-314 merge works well, the same consolidation could be applied to FIN-321 in a future semester.

---

## 6. IMPACT ON SUPPORTING FILES

| File | Action Required |
|------|-----------------|
| `README.md` (project) | Update stage table, deliverable timeline, "Getting Started" section |
| `CLAUDE.md` (project) | Trim to formulas, named ranges, and AI scaffolding guidance only |
| `template-memo.md` | No change |
| `template-spec.md` | Add "Model Review" section for post-build reflection |
| `_templates/excel/` | No change |
| `extra-credit.md` | Review point alignment |
| Root `CLAUDE.md` | Update five-stage references to four-stage |
| `docs/decisions/2026-02-15-repo-hierarchy.md` | Update stage workflow description |

---

## 7. RECOMMENDATION

Proceed with all three changes:

1. **Reorder** Stages 2 and 3 (Excel before Spec) — aligns with FIN-321 precedent and build-first pedagogy
2. **Merge** Stages 4 and 5 (Prompt into Final) — reduces deliverable count, integrates AI as tool rather than isolated exercise
3. **Trim** CLAUDE.md — remove redundancy with README, keep only AI-specific context

These changes simplify the student experience, improve spec quality through post-build reflection, and treat AI tools as integrated analytical instruments rather than standalone deliverables.

---

**Document Version:** 1.0
**Last Updated:** February 24, 2026
**Author:** Adam W. Stauffer (draft by Claude Code)
