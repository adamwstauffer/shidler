<!--
FIN-321 fx-hedging — student feedback / grade template.

This is the canonical shape of the per-student feedback block the graders emit
(see _report.build_pr_feedback). It is the copy a STUDENT receives, so it omits
internal machinery: no "floor applied" tag on the header, no flag codes. The
floor / round-up / instructor adjustments still appear, but as neutral,
self-explaining rows so the student sees exactly how the final number was
reached. Placeholders are in {curly braces}.
-->

## {Student Name} — **{final} / 100** ({letter})

**Repo:** {https://github.com/…}
**Memo:** `{docs/decisions/…-hedge-framing.md}`   <!-- stage-dependent; Stage 0 shows Repo only -->

| Criterion | Earned | Notes |
|-----------|--------|-------|
| {Criterion 1} | {earned} / {max} | {brief but descriptive — name what's there and what's missing; the suggestions below expand it} |
| {Criterion 2} | {earned} / {max} | {…} |
| {…} | {…} | {…} |
| **Raw total** | **{raw} / 100** | — |
| **Floor adjustment** | **+{n}** | lifted to {floor}% floor, rounded up |     <!-- only when the floor lifted the score -->
| **Instructor adjustment** | **+{n}** | {one-line reason} |                    <!-- only when the instructor overrode -->
| **Final** | **{final} / 100** | {earned on merit / floor applied / instructor-adjusted} |

### Improvement Suggestions (due before deliverable deadline for grade improvement)

**Stage {N} rubric notes**
- {One actionable fix per gap, tied to a criterion note above. For the early
  phases and undergrads, spell it out step by step — exact file paths, exact
  GitHub menu clicks, numbered steps — so the student knows precisely *what* to
  do and *how*. Example: "Add `prompt-log.md` at the repo root: (1) create the
  file; (2) paste the prompts you used; (3) commit."}
- {…}

**Looking ahead to Stage {N+1}**
- {Short pointer to the next stage's deliverable and where it lives in the repo.}

<!--
STYLE NOTES
- Header: name + final grade + letter only. Never surface "floor applied" or
  flag codes here — those live in the internal STAGE{N}_GRADES.md.
- Notes column: brief, but descriptive and helpful (not detector shorthand like
  "frontmatter N, location off"). The detail goes in the suggestions.
- Suggestions: detailed and step-by-step while feedback is delivered as this
  file, especially for undergrads and Stages 0–1. When we move to PR-based
  feedback, keep the specificity but drop the hand-holding (fewer numbered
  micro-steps, assume more Git fluency).
- Every block ends forward-looking ("Looking ahead"), never on what's broken.
-->
