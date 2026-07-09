---
title: "BUS-629 Stage 1 — Excel-literacy gap and future-semester revisions"
date: 2026-05-12
status: proposed
owner: Adam W. Stauffer
course: BUS-629-VEMBA-International-Corporate-Finance
scope: course
applies_to: future semesters (current Spring 2026 cohort already in flight)
related:
  - 2026-05-07-bus629-stage2-restructure.md
---

# BUS-629 Stage 1 — Excel-literacy gap and future-semester revisions

## Summary

The instructor's stated intent for Stage 1 is to give VEMBA students a discrete checkpoint where they demonstrate Excel competency — formulas, named ranges, structured workbooks — before the analysis pipeline diverts the rest of the course toward LLM-driven work at Stages 3–5. The current `stage1-template-architecture.md` asks students to download a pre-built template, upload it unmodified, and stand up a directory skeleton; the rubric weights are 30% upload / 40% directory / 20% README / 10% commits. None of these line items require the student to open the spreadsheet. The course locks Stage 1 for the current cohort; this memo proposes three options to close the gap for AY 2026–27 onward.

## Context

The Stage 2 restructure memo (`2026-05-07-bus629-stage2-restructure.md`) deliberately moved Stage 1 *away* from "design your own template from scratch" toward "use a provided template" — a sound call for VEMBA students whose course value sits at Stages 3–5, not in template engineering. The unintended side effect is that Stage 1's *demonstration component* was removed without a replacement, leaving Stage 1 as essentially a Git/filesystem exercise rebranded as Excel.

The rest of the pipeline assumes Stage 1 fluency:

- **Stage 3** asks students to populate `INC_*`, `BAL_*`, `CASH_*` named ranges with company financials. A student who never inspected the template at Stage 1 will treat this as a data-entry task and may miss structural mistakes (overwriting a formula cell, breaking a named-range scope, entering data in the wrong column).
- **Stage 4** asks students to write a spec precise enough for an LLM to execute. Naming conventions matter — a spec that references `RATIO_CurrentRatio` is only meaningful if the student understands what the named range computes.

So the cost of a passive Stage 1 isn't just "we didn't grade Excel"; it's that downstream stages silently inherit shaky foundations.

## Options for revision

### Option A — Named-range catalog (passive comprehension test)

Students produce a 1-page table (markdown in their repo at `models/templates/README.md`) listing every named range in the template, the formula behind it, and a one-sentence description of what it computes. No template modification required.

- **Pros:** Forces students to read every formula in the template. Low instructor maintenance — answer key is the template itself. Produces a useful reference artifact students reuse at Stages 3–4.
- **Cons:** Comprehension, not skill. A student could copy the formulas into a table without understanding them.
- **Rubric shift:** Add a 30% "named-range catalog" line; reduce "README quality" to 10% and "directory structure" to 30%.

### Option B — Find-the-bug audit (active demonstration)

Distribute the template in a "broken" variant with 3 deliberate flaws — e.g., a `RATIO_` formula referencing the wrong named range, an `INC_` total that doesn't sum its components, a sheet-scoped name where workbook-scoped is required. Students must identify, document, and fix the bugs, committing the corrected file plus a short `analysis/validation/stage1-audit.md` note.

- **Pros:** Genuinely tests Excel proficiency. Mirrors the "audit the LLM" stance the course wants at Stage 5 — same muscle, easier target. Produces a clear pass/fail signal.
- **Cons:** Requires instructor to maintain a broken-template variant alongside the clean one (or generate it per semester). Risk of frustration for students with weak Excel skills — fallback needed (TA hints, partial credit for finding 1 of 3).

### Option C — Extend the template (active construction)

Students must add at least three of their own ratios beyond what the template provides — pick from a list (e.g., DuPont decomposition, working-capital cycle days, interest-coverage variations) and implement using the existing named-range conventions. Document in `models/templates/README.md`.

- **Pros:** Active construction. Students must understand the template's conventions well enough to extend them consistently. Outputs feed Stage 4 naturally — their custom ratios become candidates for the LLM spec.
- **Cons:** Highest variance in output quality. Risk of students copying ratios they don't understand. Most instructor grading time of the three options.

## Recommendation

Adopt **A + B** for AY 2026–27: the catalog (Option A) tests comprehension at modest cost; the audit (Option B) provides the active demonstration the original intent calls for. Defer Option C until A+B are battle-tested — extension work is better placed at Stage 4, where the student is already specifying ratios for analysis.

Proposed revised Stage 1 rubric:

| Criterion | Weight | Notes |
|-----------|--------|-------|
| Template uploaded correctly | 15% | Down from 30% — table stakes |
| Directory structure | 25% | Down from 40% |
| Named-range catalog (Option A) | 25% | New |
| Bug-audit completed + documented (Option B) | 25% | New |
| README quality + commit hygiene | 10% | Consolidated |

Stage 1 weight remains 20% of total project score.

## Risks and tradeoffs

- **Maintenance burden:** The broken-template variant must be regenerated each semester so bugs aren't memorized across cohorts. Mitigate by parameterizing the bug-injection (a small script that picks N out of M known flaws).
- **VEMBA Excel variance:** Some students are CFOs who haven't touched Excel personally in years; others are operations leads who live in it. The audit task may feel unevenly demanding. Mitigate with a "minimum viable" floor (find 1 of 3 = 60% on that line item).
- **Pipeline coherence:** If Stage 1 grows in active workload, watch that it doesn't crowd Stage 2 (the memo). Total stage hours should stay within the EMBA workload budget.
- **Bilingual considerations:** Stage 1 instructions and the audit note may need a Vietnamese-language companion if the cohort skews that way. Out of scope for this memo but flag for the broader translation conversation.

## Out of scope

- **Current Spring 2026 cohort.** Stage 1 has already been assigned; no mid-course rubric change. Any feedback collected from this cohort about template friction should inform the AY 2026–27 revision.
- **Stage 5 verification component.** The parallel question — should Stage 5 require students to manually verify N ratios against LLM output? — is a separate concern and warrants its own memo. Captured here as a forward link only.
- **Cross-course alignment.** BUS-314 has a structurally similar 4-stage flow; whether to backport a Stage-1-style demonstration there is out of scope.

## Open questions

1. Does the broken-template variant get checked in to the public course directory, or distributed only via the LMS to prevent it leaking forward into the next cohort?
2. Should the named-range catalog be a fillable template (rows pre-listed, students complete columns) or free-form (students discover the list themselves)? Fillable is gentler; free-form tests more.
3. Is there appetite to formally retire the "students design their own template" path that BUS-314 still uses, or keep it as the undergraduate-level variant?
