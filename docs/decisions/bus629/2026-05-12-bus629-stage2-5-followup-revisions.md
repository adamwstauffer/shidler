---
title: "BUS-629 Stages 2–5 — Spring 2026 cohort decisions"
date: 2026-05-12
status: accepted
owner: Adam W. Stauffer
course: BUS-629-VEMBA-International-Corporate-Finance
scope: course
applies_to: Spring 2026 cohort (starting 2026-05-14) and forward unless revised
related:
  - 2026-05-07-bus629-stage2-restructure.md
  - 2026-05-12-bus629-stage1-excel-literacy-gap.md
  - ../2026-05-10-claude-plugins-student-rollout.md
supersedes_draft: this file previously held a longer set of speculative proposals; the decisions below are the simplified actual scope
---

# BUS-629 Stages 2–5 — Spring 2026 cohort decisions

## Summary

Stages 2–5 land in the current Spring 2026 cohort with a deliberately tight scope: Stage 2 is a memo addressed to the instructor for review and approval (no in-class pitch this semester); Stage 3 is the populated-financials upload as currently specified; Stage 4 is the LLM-drafted spec with at least one human-in-the-loop review iteration documented; Stage 5 keeps the current restructure with three additions — a manual ratio verification table, a structured spec retrospective, and a small rubric line for incorporating instructor feedback from Stage 2. Items that came up in the earlier draft but did not survive scoping — in-class pitches, peer-set tables, SKILL.md as a graded artifact, plugin-workflow requirements — are parked as **Future Considerations** for AY 2026-27.

## Context

An earlier draft of this memo proposed 14 changes across the four stages. After review, the instructor (Adam Stauffer) trimmed scope significantly to fit the current cohort's runway and the VEMBA workload budget. This memo captures the decisions actually adopted; the longer brainstorm is preserved in git history (commit `d1f4d06`).

The Stage 1 follow-up memo (`2026-05-12-bus629-stage1-excel-literacy-gap.md`) remains future-semester-only — Stage 1 submissions for the current cohort have been accepted and the rubric is not changing mid-cycle.

---

## Stage 2 — Company Selection Memo (10%)

### Decisions

- **Memo only this semester.** No in-class presentation / pitch for the current cohort. The 70/30 deliverable/presentation split from the 2026-05-07 restructure is suspended for Stage 2 in Spring 2026; the memo carries the full 10%.
- **Audience: Adam Stauffer (course instructor) for review and approval.** Not a hypothetical CFO; not other students. Memo framing should match how a junior analyst writes to a managing director — concise, decision-oriented, evidence-tight.
- **No peer-review component.** The memo is reviewed only by the instructor.
- **Instructor write access to the student's portfolio repo is required at Stage 2.** Each student must add Adam Stauffer's GitHub handle as a collaborator with write (push) permission on their personal portfolio repository. This enables feedback as **pull requests opened against the student's repo** — concrete suggested edits the student reviews, comments on, and merges — rather than markdown comments on an external document. The PR-driven feedback loop mirrors real code-review workflows and is the operational complement to the "review and approval" framing above.
- **Instructor feedback is expected and will be returned.** Students should anticipate revising the memo (or carrying revisions forward into later stages) based on that feedback. See Stage 5 below for how feedback incorporation is graded.

### Rubric implication

| Criterion | % of Stage 2 |
|-----------|-------------:|
| Company Selection & Rationale | 25% |
| Analytical Framing & Hypotheses (falsifiable; directional) | 25% |
| Data Source Identification | 25% |
| Professionalism & Communication | 25% |

Falsifiability moves into the rubric criterion text — a hypothesis must state a direction and a reason ("I expect X because Y"); open-ended framings ("we'll see what the ratios show") do not earn full credit.

### Implementation TODO before cohort start

- `stage2-company-selection-memo.md`: remove the "In-class presentation" section, remove the presentation rubric block, restore full 100% to the deliverable rubric, change "Audience: A CFO or VP of Finance" → "Audience: Adam Stauffer (course instructor) for review and approval," update the hypothesis criterion text, **add a "Grant instructor write access" subsection** with step-by-step GitHub instructions (Settings → Collaborators → Add people → Adam's GitHub handle → Write role) and call out that the access grant is part of the Stage 2 submission checklist.
- README stage table: note that Stage 2 is memo-only for Spring 2026.
- `stage0-repo-setup.md` (or wherever onboarding lives): forward-flag the upcoming write-access requirement so students aren't surprised at Stage 2.

---

## Stage 3 — Populated Financials (20%)

### Decisions

- **No scope additions for this semester.** Stage 3 remains the populated-financials upload as currently specified in `stage3-model-population-validation.md`. The validation-note artifact, units/currency rubric promotion, filing-access-date field, and optional peer financials are all **parked for future semesters** (see Future Considerations).
- **Existing rubric stays:** 40% accuracy / 25% completeness / 20% source documentation / 15% auto-computed ratios resolve cleanly.

### Implementation TODO before cohort start

None. Stage 3 doc is current.

---

## Stage 4 — LLM-Drafted Spec (20%)

### Decisions

- **Spec deliverable as currently specified, plus a required human-in-the-loop (HIL) review iteration.** Students must submit evidence of at least one HIL review pass: an annotated diff, a "round 2" prompt that addressed gaps from round 1, or a short before/after note showing what they revised. A single-shot LLM dump with no visible iteration is below standard.
- **Claude Code skill format is aspirational, not graded.** The instructor encourages — but does not require — students to consider whether their spec could be tailored as a Claude-for-financial-services skill (`SKILL.md` format). Framing: "this is how you'd reshape your spec to direct Claude for your unique problem." This belongs in the tips, not the rubric.
- **Two workflows (desktop / CLI) as currently documented.** No third "plugin" workflow added this semester; plugin pilot stays parked for a future cohort.

### Rubric implication

Existing 25/25/25/25 stays. The "Spec craft + prompt log quality" criterion's rubric text gains an explicit HIL-iteration requirement:

> Strong work shows at least one iteration where the student identified a gap in the LLM's draft and revised either the prompt or the spec. A prompt log of a single one-shot dump does not earn this credit.

### Implementation TODO before cohort start

- `stage4-technical-specification.md`: add an "HIL review requirement" subsection clarifying what counts as evidence of iteration; revise the "Spec craft + prompt log" rubric criterion text.
- Add a short "If you're curious" sidebar pointing students toward the Claude-for-financial-services plugin family as an enhancement path — explicitly note it is **not** graded.

---

## Stage 5 — Synthesis + Repo Polish (25%)

### Decisions

- **Three additions adopted:**
  - **Manual ratio verification table** (`analysis/validation/stage5-verification.md`) — pick at least 5 ratios, recompute manually from Stage 3 financials, compare to the LLM's stated values, mark match/discrepancy with a 1-line note. Carves 10% of the deliverable rubric from "Analytical correctness."
  - **Structured spec retrospective template** at `docs/templates/spec-retrospective-template.md` — required sections: section-by-section verdict on the Stage 4 spec, top-3 gaps with evidence, what you'd change, effectiveness rating (1–5).
  - **Stage 2 feedback incorporation** worth 5% of deliverable rubric — visible in repo as a revised memo committed alongside the final analysis, or as commits demonstrably responding to instructor feedback. Not a hard gate; graded as a rubric line.
- **Repo polish checklist expanded** with: 1-line repo description (GitHub page header), top-of-README project status / "what you'll find here" block, `LICENSE` file (MIT or Apache-2.0 recommended), `.gitignore` excluding common scratch files.
- **Peer benchmarking: recommended, not required.** With no peer-set thread upstream, peer comparisons at Stage 5 are an "above and beyond" element. Students who source peer data at Stage 5 may use it to strengthen their strategic recommendations; absence does not penalize.

### Revised Stage 5 deliverable rubric

| Criterion | Weight |
|-----------|-------:|
| Analytical correctness (ratios, Du Pont, interpretation) | 25% |
| Manual verification artifact (new) | 10% |
| LLM evaluation + spec retrospective (template-backed) | 25% |
| Strategic recommendations + executive voice | 20% |
| Stage 2 feedback incorporation (new) | 5% |
| Repo polish (expanded checklist) | 15% |
| **Total deliverable** | **100%** |

Polish drops 25% → 15%; the freed 10% funds the manual verification artifact. Stage 2 feedback line is 5%, carved evenly from analytical correctness and retrospective. 70/30 deliverable/presentation split is unchanged.

### Implementation TODO before cohort start

- `stage5-llm-analysis-evaluation.md`: add the manual verification artifact requirement, link the new retrospective template, expand the repo polish checklist, add the Stage 2 feedback incorporation rubric line, swap in the revised rubric table.
- Create `docs/templates/spec-retrospective-template.md` at the repo level.

---

## Future Considerations (parked for AY 2026-27)

Items raised in the earlier draft that are not adopted this semester but worth revisiting:

| Item | Stage | Why parked |
|------|------:|------------|
| In-class pitch / presentation | 2 | Instructor likes the idea; not ready for this cohort. Reintroducing the 70/30 split is straightforward for AY 2026-27. |
| Peer-set table at memo time | 2 | Couples to Stage 3 and Stage 5 (all-or-nothing thread); adding three artifacts mid-runway is too much. |
| Validation note artifact | 3 | Low-cost addition once the cohort settles into the new structure. |
| Units/currency promoted to rubric | 3 | Add after observing how often this fails in Spring 2026 grading. |
| Filing access date field | 3 | Trivial future-add. |
| Peer financials in `data/peers/` | 3 | Coupled to Stage 2 peer-set decision. |
| SKILL.md format as a graded artifact | 4 | Aspirational this semester; if observed adoption is high, promote to a rubric criterion next cohort. |
| Plugin workflow as a third option | 4 | Coordinate with the 2026-05-10 plugin rollout pilot; depends on whether VEMBA cohort proves a willing pilot group. |
| Peer benchmarking required (not optional) | 5 | Couples to Stage 2 peer-set thread. |
| Tightened prompt-log standards | 4 | Watch what gets submitted this cohort; tighten next cycle. |

## Risks and tradeoffs

- **Asymmetric stage rubrics.** Stages 0, 1, 3 are upload-only and have no presentation; Stage 2 this semester is also memo-only (no presentation); Stages 4 and 5 carry the 70/30 split. The README needs to make this asymmetry clear so students don't assume a Stage 2 pitch obligation that doesn't exist.
- **Repo polish weight drop.** Polish moves from 25% → 15% of Stage 5. Students may interpret this as "polish matters less" — but it's still the most heavily weighted single non-analytical line. Mitigate by retaining the explicit checklist and the language that the repo is the long-tail portfolio artifact.
- **HIL iteration enforcement.** The rubric language for Stage 4 will need to be concrete enough that "one iteration" is gradable. The included rubric text ("identified a gap → revised prompt or spec → improved output") is the working definition; refine after first cohort.
- **Feedback-incorporation timing.** Adam's review of Stage 2 memos needs to land before Stage 5 begins (ideally before Stage 4) so students have time to revise. Operational, not pedagogical, but worth tracking on the instructor side.

## Out of scope

- **Stage 0 and Stage 1.** Already in flight; not changing.
- **BUS-314 / FIN-321 parallels.** Several adopted ideas (manual verification table, structured retrospective) could backport. Separate decision.
- **Bilingual / Vietnamese-language deliverables.** Flagged for separate memo before AY 2026-27 cohort recruitment.

## Open questions

1. Should Stage 4's HIL-review evidence be submitted as a separate file (e.g., `analysis/validation/stage4-iteration.md`) or embedded inside the prompt log? Cleaner-as-separate; lower-friction-as-embedded.
2. Stage 2 feedback turnaround — what's the instructor commitment? "Feedback within X days of submission" lets students plan; no commitment risks Stage 5 starting without it.
3. Is the Stage 2 audience change from "CFO/VP Finance" → "Adam Stauffer" purely framing, or does the memo's *tone* also shift (e.g., shorter, less formal preamble)? Worth one line of guidance in the stage doc.
4. Write-access scope: collaborator with Write role (push to any branch, merge PRs) vs. Triage role (review, label, comment but not push). Write is the cleaner default for the PR-feedback workflow; Triage is the safer fallback if students worry about direct-push surprises. Recommend Write.
5. Privacy: students' portfolio repos are public by Stage 5. While their work is in progress between Stage 2 and Stage 5, who else can see the instructor's PR comments? Consider whether early stages should be on a private branch with the repo flipped to public at Stage 5 polish time.
