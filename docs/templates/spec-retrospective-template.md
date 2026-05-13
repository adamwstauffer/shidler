---
template: spec-retrospective
purpose: "Structured self-evaluation of a Stage 4 technical specification after seeing how an LLM executed it at Stage 5 — surfaces spec gaps with evidence, not impressions"
audience: student
fields_required: [date, author, company, spec_file, stage5_output, section_verdicts, top_gaps, revisions, effectiveness_rating, forward_link, process_feedback]
naming_convention: "YYYY-MM-DD-{lastname}-{company-slug}-spec-retrospective.md (lives in deliverables/)"
courses: [BUS-629, FIN-321, BUS-314]
---

# Stage 4 Spec — Retrospective

**Author:** [Your Name]
**Date:** [YYYY-MM-DD]
**Company:** [Company name + ticker]
**Spec being evaluated:** `docs/specs/YYYY-MM-DD-{slug}-spec.md`
**Stage 5 LLM output:** `deliverables/YYYY-MM-DD-{slug}-llm-raw.md`

---

## 1. Section-by-section verdict

> For each section of your Stage 4 spec, rate **Clear / Vague / Missing** and explain in one line. Vague or Missing rows must cite the symptom that revealed the gap in your Stage 5 LLM output (a specific line, claim, or omission). "I just feel like it was vague" does not earn the verdict.

| Spec section | Verdict | Symptom in Stage 5 output |
|---|---|---|
| Part A.1 — Scope & Objective | | |
| Part A.2 — Model Architecture | | |
| Part A.3 — Data Inputs | | |
| Part A.4 — Named Range Conventions | | |
| Part A.5 — Derived Inputs | | |
| Part A.6 — Ratio Definitions & Formulas | | |
| Part A.7 — Validation Rules | | |
| Part B.8 — Analysis Requirements | | |
| Part B.9 — Du Pont Decomposition | | |
| Part B.10 — Strategic Recommendation Requirements | | |
| Part B.11 — Output Format | | |

---

## 2. Top three gaps with evidence

> Pick the three most consequential gaps from Section 1. For each, describe where it surfaced in the LLM output, why your spec caused it, and the exact spec language you would add or change to prevent it.

### Gap 1: [one-line title]

- **Where it surfaced:** [specific section, line, or claim in your Stage 5 LLM output]
- **Spec cause:** [what your spec was missing, ambiguous about, or assumed]
- **Fix (exact language):** [the sentence or table row you would add to your spec]

### Gap 2: [one-line title]

- **Where it surfaced:**
- **Spec cause:**
- **Fix (exact language):**

### Gap 3: [one-line title]

- **Where it surfaced:**
- **Spec cause:**
- **Fix (exact language):**

---

## 3. Revisions

> If you re-ran with a revised spec, what three changes would you make? Each change must reference the gap it addresses (Gap 1, 2, or 3 above). Vague items ("add more detail") do not count.

1. [Revision] — addresses Gap [N]
2. [Revision] — addresses Gap [N]
3. [Revision] — addresses Gap [N]

---

## 4. Effectiveness rating

> Pick the row that best describes your spec. The anchors are deliberately specific — choose the one your evidence supports, not the one that feels generous.

| Rating | Anchor |
|:---:|---|
| **5** | I would hand this spec to a junior analyst and trust their output without re-checking. |
| **4** | Solid overall; one section needs sharpening before I'd ship it. |
| **3** | Workable with revisions; spec has gaps the LLM had to guess around. |
| **2** | Substantial rework needed; LLM output diverged in meaningful ways traceable to the spec. |
| **1** | Spec is not yet usable as a standalone artifact. |

**My rating: [1–5]**

**Justification (100–200 words):**

> Cite at least one concrete piece of evidence per anchor point you claim. For example, if you rate **4**, identify the section that needs sharpening and one specific symptom in your Stage 5 output that supports the rating. If you rate **3**, identify two or more sections the LLM had to guess around, with examples.

[Your justification here.]

---

## 5. Forward link

> One sentence: what changes in how you'd approach the *next* spec you write — for this company in a year, a different company, or a non-finance domain?

[Your sentence here.]

---

## 6. Retrospective process feedback (≤150 words)

> Step back from your spec for a moment and evaluate this retrospective template itself.
>
> - **What did filling this out surface that you wouldn't have noticed in a free-form "what I'd change" write-up?** Specific examples, not "it was helpful."
> - **One structural change you'd make to this template** — add a section, remove a section, reword a prompt — and the reason it would produce better self-knowledge.
>
> This section is graded for thoughtfulness, not for praising or critiquing the assignment. "More space for X" is a structural suggestion. "Make it shorter" without saying what to cut is not.

[Your feedback here.]

---

## Notes for graders

This retrospective is part of the Stage 5 deliverable rubric. Strong submissions are:

- **Evidence-tied.** Every verdict, gap, and rating points at a specific symptom in the Stage 5 LLM output.
- **Specific in revisions.** "Add more detail" earns less than "Add a Derived Inputs row defining `avgAssets_2025 = (BAL_assets_total_2025 + BAL_assets_total_2024) / 2`."
- **Honest in rating.** A self-rated **5** with weak Stage 5 output and no specific evidence is a flag, not a flex.
- **Thoughtful in Section 6.** Cohort-level patterns in Section 6 inform next semester's template — this section is read with that in mind.
