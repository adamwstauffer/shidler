---
title: "BUS-629 post-deadline revision sweep — policy and mechanics"
date: 2026-05-15
status: accepted
owner: Adam W. Stauffer
course: BUS-629-VEMBA-International-Corporate-Finance
scope: course
applies_to: Spring 2026 cohort and forward unless revised
related:
  - 2026-05-12-bus629-stage2-5-followup-revisions.md
  - 2026-05-07-bus629-stage2-restructure.md
revision_history:
  - 2026-05-15 morning — draft locked in conversation: half-gap cap, unlimited student-initiated re-grades, no instructor scans
  - 2026-05-15 afternoon — revised after instructor pushback: time-triggered batch sweep (not student-initiated), 1 attempt per stage with grace clause, cap removed
---

# BUS-629 — post-deadline revision sweep

## Summary

After each stage's due date, the instructor runs **one batch revision sweep** across every student's repo. The sweep re-runs the stage's rubric against the current repo state and updates the score if it improved. The full rubric applies — there is **no cap** on the bump; a student who revises to raw 100 ends at 100. Each student gets **one sweep per stage**; once that stage's sweep runs, the stage is locked. Students do not need to email or request the sweep — they just revise files in their repo before the stage's due date and the sweep picks up whatever is there. Score numbers are **always private** — kept to the internal gitignored `STAGE{N}_GRADES.md` reports and instructor-to-student communication — never published to the student's public GitHub artifacts. Re-grade entries in the internal report are **append-only**: original grade and comments stay intact; an `### Updated YYYY-MM-DD (post-deadline sweep)` block is added underneath, listing items addressed, items still open, the per-criterion delta, and the new score.

Why time-triggered batch rather than ad-hoc re-grade-on-request: **22 students × 5 stages × N re-grades per student** does not scale for a solo instructor. Batching to one sweep per stage caps the work at 22 × 5 = 110 review events for the whole semester, which is tractable; per-student per-iteration handling would scale as `N × students`.

---

## Context

After Stage 0 and Stage 2 grading rounds for the Spring 2026 cohort, multiple students started incorporating feedback and committing improvements within days. The first student to email saying *"I've addressed Stage 0 and Stage 2 feedback"* was Luong Duy Phuong on 2026-05-15. Without a re-grade policy, that effort is invisible to the gradebook — and the implicit message is *"first draft locks your score."* That is the opposite of the pedagogical claim Stage 2's tracked-feedback workflow makes (revision is professional norm; an auditor or supervising analyst marks up a draft, the analyst revises, the reviewer signs off).

This memo locks the policy choices we settled in conversation so we can return to delivery automation without re-litigating the underlying rules.

## Decisions

### D1. Post-deadline sweep replaces ad-hoc re-grade requests.

- **Trigger:** time-based. The instructor runs the sweep once per stage, within ~24 hours after that stage's due date.
- **Student action:** revise files in your repo before the stage's due date. No email or issue required. The sweep picks up whatever is in the repo at the cutoff.
- **No instructor-initiated mid-cycle scans.** The sweep happens **once** per stage, at the post-deadline window. Before that, the original grade and feedback stand.
- **Stage due dates** (Spring 2026 cohort): S0 May 16; S1/S2/S3 May 23; S4/S5 May 30 — all 11:59 PM local.
- **Sweep dates** (Spring 2026 cohort): S0 sweep May 17; S1/S2/S3 sweep May 24; S4/S5 sweep May 31.

### D2. One sweep per student per stage. Stage locks after sweep runs.

- After the sweep, the score for that stage is **final**. No further re-grades, even if additional commits land. This is what makes "one attempt" structural rather than honor-based.
- **Grace clause for the Spring 2026 cohort:** any student who already received an ad-hoc re-grade under the prior policy (in effect 2026-05-15 morning) gets **one additional sweep event** under the new system. In practice this is a no-op for the cohort, because every student gets exactly one sweep per stage anyway — the grace clause just removes any ambiguity about whether the prior re-grade "used up" the new entitlement.
- Why one sweep, not unlimited: **22 students × 5 stages × N revisions** does not scale for a solo instructor. One sweep per stage caps the semester's review workload at 22 × 5 = 110 events and concentrates them at five well-defined cutoffs.

### D3. No cap on the bump. The full rubric applies on the post-deadline sweep.

- If a student revises to raw 100, the final is 100. The rubric is the cap.
- **Supersedes the earlier half-gap cap** (50% of the original-to-100 distance), which was in effect for the morning 2026-05-15 draft of this memo. That cap is removed because (a) the post-deadline sweep happens only once per stage, so the structural attempt-cap already prevents grade inflation through repeated iteration, and (b) pedagogically, the cap was sending a mixed signal — "we want you to iterate, but we'll keep some of the deduction even after you fix it." With time-bounded one-shot sweeps, full recovery is appropriate.
- **Retroactive application:** any re-grade already entered under the half-gap cap is updated in place to remove the cap. For the Spring 2026 cohort, the only affected entry is Luong Duy Phuong's Stage 2 (re-graded 90 under the cap → 100 after cap removal, same day). The original 80/floor entry is preserved; the cap-removal note is added to the existing `### Updated 2026-05-15` block.

### D4. Score numbers are always private.

- `STAGE{N}_GRADES.md` lives under `ignore/` — already gitignored, never pushed.
- Email replies to students mention the new score number.
- **Public-facing artifacts** (PRs, GitHub issues, repo files) describe *items addressed / items open / pedagogical framing* but never include the score number itself.
- Rationale: the student's repo is a portfolio artifact visible to managers, peers, and reviewers indefinitely. Score history doesn't belong there. The feedback substance does.

### D5. Sweep entries are append-only. Stage locks after the sweep runs.

- Original entry (header, rubric table, suggestions) stays untouched.
- Sweep entry added underneath as `### Updated YYYY-MM-DD (post-deadline sweep)` with:
  - Items addressed (per the original suggestion list)
  - Items still open (forward-looking, not punitive — per `feedback_no_double_deductions`)
  - Per-criterion delta (e.g., `Analytical Framing: 15 → 25`)
  - New raw + new final
  - Closing line: `**Re-graded final:** NN / 100 (effective YYYY-MM-DD)` — this canonical marker is what `build_roster.py` parses to surface the updated score in the master roster.
- Class summary table gets a **second line** for the student showing `Original 80 → Re-graded 100 (2026-05-17)`. The original line stays.
- The roster's `Current stage` and per-stage columns read the latest re-graded final via the canonical marker, so sweep updates flow through automatically without manual roster edits.
- **Stage lock:** after the sweep entry lands, the stage is final. No further re-grades, even if the student commits more work to the repo afterward.

### D6. Sweep policy is communicated to students up front.

- A single cohort email at policy adoption (2026-05-15) explains the mechanics, the rationale, and what students need to do (nothing — just revise files in the repo). Draft at `docs/emails/BUS-629/2026-05-15-regrade-policy.md`.
- A one-line note is added to each `stage{N}-*.md` assignment doc so students who re-read the assignment between policy email and the sweep see the rules in context.
- Suggested wording (to add to each stage's "Submission" section):
  > **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Any improvements you make before the deadline — addressing prior feedback, expanding sections, fixing data — can move your score up. The full rubric applies (no cap on the bump). You don't need to email or open an issue; just revise the files in your repo. One sweep per stage; the score locks once the sweep runs.

---

## Deferred — to be settled in a follow-up memo

### Tracked-feedback delivery mechanics

Three primitives, each appropriate to a different situation. Picking among them, automating them, and standardizing the PR/issue template is **out of scope for this memo** — captured here so we can return cleanly.

**Option A: PR with mechanical commits.**
Best when the open item is a mechanical fix (drop tracked `.DS_Store`, rename a file to canonical pattern, fix frontmatter casing). Push a branch on the student's repo (e.g., `feedback/stage0-cleanup-2026-05-15`), single-purpose commit, open a PR titled `Stage 0 carry-forward: stop tracking .DS_Store files`. Student merges → fix lands. Demonstrates the auditor-markup workflow concretely.

**Option B: PR with review-only line comments.**
Best when the memo has content-level wording suggestions but nothing to mechanically edit. Tiny diff anchor on the relevant file, then line-anchored review comments via `gh pr review` / GitHub API on specific lines. Student responds in threads, makes the change herself, instructor approves. Closest to the supervising-analyst marking up a draft memo.

**Option C: GitHub issue.**
Best when there is no diff to propose (re-grade summary on an already-on-spec memo). Issue title `BUS-629 Stage N — re-grade (revisions reviewed YYYY-MM-DD)`, body lists items addressed + still-open + carry-forward tips. Student closes when read.

**Edit-vs-don't-edit boundary.**
- *Mechanical / convention-driven* (file removal, rename, frontmatter additions, casing): OK to push as commits in a PR. Demonstrates the workflow.
- *Content / voice* (bio length, memo wording, hypothesis claims): never push as commits. Always offered as suggestions in PR comments or issue text. The student's voice is non-negotiable.

**Branch and PR etiquette (proposed defaults, not locked):**
- Branch naming: `feedback/stage{N}-{short-slug}-{date}` (e.g., `feedback/stage0-dsstore-cleanup-2026-05-15`).
- Single-purpose PRs — never bundle S0 cleanup with S2 review on one branch.
- Never push to student's `main` directly; always go through PR.
- Student may decline the merge; she owns the repo.

**Tooling implications (also deferred):**
A `regrade_stage{N}.py` helper could re-fetch repo state, compute the rubric delta, print a proposed PR body + proposed issue body to console for instructor review. Separate flags `--push-pr` and `--open-issue` would actually fire after review. Internal `STAGE{N}_GRADES.md` append happens only after explicit confirmation. Nothing happens silently. **Not built yet** — the first few re-grades will be done manually so we can refine the format before automating.

---

## Open questions for the follow-up memo

1. **When delivery is by PR, where does the PR description's text come from?** The internal grade-report's "suggestions" section is privately-framed (often references "the rubric" or "−5 deduction"). The PR body needs to be re-rendered in student-facing professional voice. Is that a manual rewrite each time, or a templated transformation?
2. **Repeat re-grades — same PR/issue updated, or new one?** Probably new, with cross-references in the body. Locks in the audit trail.
3. **What happens when a student misses the stage due date but the project is still open?** Probably: no re-grade; the next stage's revisions still receive feedback but don't roll back into the prior stage's score. Worth explicit confirmation.
4. **Are re-grades counted in cohort-level statistics (mean, median)?** Probably yes — the re-graded score is the canonical final. Worth re-stating in the report header.

## Implementation status

| Element | Status | Owner |
|---|---|---|
| D1–D6 (policy mechanics, time-triggered version) | Accepted 2026-05-15 afternoon | Adam Stauffer |
| Cohort email | Drafted at `docs/emails/BUS-629/2026-05-15-regrade-policy.md` | Adam Stauffer to send |
| One-line policy note in each stage assignment doc (S0–S5) | Applied 2026-05-15 | Adam Stauffer |
| First test case (Phuong S0 + S2 manual re-grade under prior policy) | Re-grade entries logged; S2 cap removed retroactively (90 → 100) per D3 | Done |
| Tracked-feedback delivery mechanics (PR vs. issue vs. inline) | **Deferred** — sweep model reduces the urgency since one batch event per stage is operationally simpler than per-student PR/issue handling | Adam Stauffer |
| `sweep_stage{N}.py` tooling (was `regrade_stage{N}.py`) | **Deferred** — first sweep (S0 on 2026-05-17) will be run manually so we can refine the format before automating | Adam Stauffer |
