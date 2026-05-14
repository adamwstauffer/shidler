# FIN-321 STAGE 4 SUBMISSION-FORMAT REVIEW & RECOMMENDATIONS

## Decision Memo

**Prepared by:** Adam W. Stauffer (draft by Claude Code)
**Date:** May 2, 2026
**Status:** Draft — Pending Review
**Scope:** FIN-321 International Finance & Securities, Spring 2026, FX Hedging Project, Stage 4 (Final Analysis & Structured AI Prompt)

---

## 1. SUMMARY

For Stage 4 of the FX Hedging Project, students were asked to submit *only a GitHub link* to their final analysis memo and structured AI prompt. The intent was twofold: (1) ensure students could maintain a public, version-controlled portfolio of their work, and (2) reinforce reproducibility as a finance-engineering competency.

After grading 33 submissions on a 6-point scale (with an 85% floor, a +0.25 bump for students who provided a GitHub link, and a -0.5 penalty for those who did not), the format **substantially worked**: 24 of 33 students (73%) earned a final score of 6.00, and 30 of 33 provided a usable GitHub link. However, four distinct failure modes emerged that cost grading time and produced unequal student experiences. This memo documents the findings, justifies the grades issued, and recommends concrete process changes for AY 2026–27.

---

## 2. GRADING APPROACH

| Criterion | Description | Points |
|-----------|-------------|------:|
| Hedge Interpretation (A + B) | Demonstrates understanding of forward, MM, put, call, and no-hedge outcomes | 1.5 |
| Sensitivity Analysis (C) | Meaningful EUR ±5% scenario discussion | 1.0 |
| Recommendation + Justification (D + E) | Actionable, data-supported, executive-ready | 1.5 |
| Structured AI Prompt (F) | Named ranges, color codes, verification, reproducible spec | 2.0 |
| **Subtotal** | | **6.0** |
| Curve floor | `Curved = MAX(Raw, 5.10)` (85% × 6 = 5.10) | — |
| GitHub bump | `+0.25` if a GitHub link was provided | +0.25 |
| GitHub deduction | `−0.5` if no link in submission | -0.5 |
| Ceiling | Final score capped at 6.0 | — |

The bump and deduction are applied **after** the floor and capped at 6.0:

```
Final = MIN( MAX(Raw, 5.10) + 0.25 [if link]  − 0.5 [if no link],  6.0 )
```

The bump rewards students who followed the GitHub-only protocol — even when their work hits the floor — and creates separation between students with the same raw score who differed in protocol compliance (e.g., Baik Sumin and Cherry Reagan both had raw 5.50 work, but Sumin provided a link and finished at 5.75 while Cherry pasted inline and finished at 5.50).

A custom Python pipeline (`_tools/fetch_stage4.py` + `_tools/grade_stage4.py`) was built to:
1. Parse each submission HTML for any `github.com` URL (in href or plain text — not just the link element).
2. Convert blob/tree/commit URLs to raw content URLs and download each deliverable (with recursive Git-tree fallback for bare repo URLs).
3. Score each deliverable against the rubric using textual signals (sections, hedge keywords, named-range tokens, color codes, verification mentions).
4. Apply curve and produce an Excel grading worksheet at `_grading/stage4-grading-worksheet.xlsx`.

Final grades and per-student notes live at `ignore-term/2026-Spring/stage4/_grading/stage4-grades-summary.md`.

---

## 3. FINDINGS

### 3.1 Distribution of final scores

| Final /6 | Count | Pct |
|---:|---:|---:|
| 6.00 | 24 | 73% |
| 5.75 | 3 | 9% |
| 5.50 | 2 | 6% |
| 5.35 | 4 | 12% |
| 4.60 | 1 | 3% |

No student fell below 4.60. The class-wide average raw score was approximately 5.55/6. The 85% floor lifted four submissions; the +0.25 GitHub bump applied to 30 students (and pushed 2 of them — Alton, Talioaga — from 5.75 up to the 6.0 cap); the -0.5 deduction applied to 3 (Cherry, Ferayorni, Shimao).

### 3.2 Four observed failure modes

The three students with **no GitHub link in any form** (Cherry, Ferayorni, Shimao) and the three students with a link that did not resolve to verifiable Stage 4 work (He, Haluber, Samson) revealed four distinct breakdowns of the GitHub-only submission policy:

**(a) Format rebellion — Cherry Reagan and Tate Shimao.** Both pasted their full memo content directly into the Lamaku comment box rather than push to GitHub and link. The work itself was strong (both would have earned 6.00 with a link), but they took the -0.5 GitHub penalty and forfeited the +0.25 bump (final 5.50 each). The pattern suggests these students did not trust the link-only flow or did not have a working repo at the moment of submission.

**(b) Wrong-file links — Christian Josh Haluber.** Haluber linked to `scenario4-fx-memo.md` in his repo, but inspection showed the file was actually a Stage 1 memo (background, methods, next steps), not a Stage 4 final analysis. Auto-grader scored 3.75/6 raw; the floor lifted him to 5.10, the link bump added 0.25 → final 5.35. This is a sanity-check failure that the LMS could have caught with a glance at the linked file's content.

**(c) Private or deleted repos — Nizhen He.** He's submission linked to `Ni-2026/Nizhen-portfolio` at a specific commit SHA; both the repo and the user's repo list returned 404 from the GitHub API. The work may exist privately, but the grader has no way to verify. Because a link was provided in good faith, the bump applied (5.10 + 0.25 = 5.35).

**(d) Bare-repo links with no Stage 4 deliverable — Jersey Kianne Samson.** Samson submitted a bare repo URL (`jksamson-debug/shidler`). The repo exists publicly and contains FIN-321 Stage 1 work, but no Stage 4 file. The recursive tree search resolved to a *template* file (the BUS-314 Stage 4 assignment markdown that lives in the same multi-course portfolio repo), which scored poorly. Floor + bump → 5.35.

**(e) Comment-only "everything's on GitHub" — Alexander Ferayorni.** Ferayorni's submission was a one-sentence note that his work was on GitHub, but no link was provided. The user `aferayorni` has zero public repos. Final score 4.60 (raw 2.5 → floor 5.10 → no bump → -0.5 deduction).

### 3.3 Operational cost to grader

The link-only format added meaningful grading workflow cost: roughly **two hours of tooling work** to build the fetch pipeline (HTML parse → URL normalize → raw fetch → recursive tree fallback → text extraction across .md/.pdf/.docx/.html). For 33 students this is amortized; for 100+ students this scales linearly only because the tools are now reusable. Manual review of the four edge cases above also took longer than reading inline content would have.

---

## 4. ASSESSMENT OF THE GITHUB-ONLY POLICY

**The pedagogical goal is correct.** The Stage 4 deliverable explicitly tests reproducibility — a structured prompt that could regenerate the Stage 2 spreadsheet from documented inputs. A submission format that accepts inline pastes contradicts the lesson; one that requires GitHub artifacts reinforces it. The 67% perfect-score rate and the 30/33 link-provision rate both indicate that the policy worked for most students.

**However, the policy under-specified four edge cases that quietly degraded the experience for ~12% of the cohort.** Each failure mode was preventable with stronger pre-submission checks:

| Failure mode | Frequency | Underlying cause |
|---|---:|---|
| Inline paste, no link | 2 (6%) | Students did not trust or could not complete the link flow |
| Wrong-file link | 1 (3%) | No automated check that the linked file is the *Stage 4* file |
| Private/deleted repo | 1 (3%) | No requirement that repos be public or grader-accessible |
| Bare-repo link, no deliverable | 1 (3%) | URL allowed pointing at the repo root, not the file |
| Comment-only, no link | 1 (3%) | No syntactic validation that submission text contains a link |

Net assessment: **the policy should be retained but tightened**. Without changes, this rate of edge cases will scale up on larger sections (BUS-313, BUS-314).

---

## 5. RECOMMENDATIONS

**5.1 Add a submission-time link validator.** Before submission is accepted, parse the comment text for a `github.com/<user>/<repo>/blob/<branch>/...stage4*.md` (or `.pdf`) pattern. If absent, show the student a warning: "We could not detect a Stage 4 file link — submission accepted but you may receive a -0.5 GitHub penalty." This converts the late-discovery deduction into a real-time decision point.

*Owner:* Stauffer + LMS support. *Effort:* low (Lamaku/Sakai may already support text-pattern validators on submission comments).

**5.2 Require deep links, not repo roots.** Update the Stage 4 assignment to specify: *"Link must be to a `/blob/<branch>/.../stage4*` file, not a repo root or folder."* Reject `tree/` or bare-repo URLs in spec language. This eliminates failure mode (d) entirely.

*Owner:* Stauffer. *Effort:* trivial (one paragraph in `stage4-final-analysis-assignment.md`).

**5.3 Require public or grader-accessible repos.** Add to the Stage 0 / project setup: *"Your portfolio repo must be public, OR you must add `@stauffer-grader` as a collaborator before Stage 4 submission."* Distribute a single grader GitHub identity for collaborator invites. This eliminates failure mode (c).

*Owner:* Stauffer + IT. *Effort:* low (one sentence in setup; one GitHub account).

**5.4 Accept inline content as a fallback, but still require the link.** For students who paste full content (Cherry, Shimao), the deduction stings them harder than students who linked sloppily. Recommend keeping the -0.5 deduction (it preserves the policy signal) but explicitly grading the inline content when present, rather than treating absent-link as absent-work. This is what the current grading already does and should be codified.

*Owner:* Stauffer. *Effort:* none — already in practice.

**5.4a Add an explicit GitHub-compliance bump.** Adopted this term: students who provided a usable GitHub link receive a +0.25 bump on top of their curved score (capped at the 6.0 ceiling). This creates positive separation between students who followed the protocol and students who pasted inline, even when both produced equivalent underlying work. The bump is small enough to never overwhelm the rubric but large enough to preserve a meaningful gap (e.g., Baik 5.75 vs. Cherry 5.50 at the same raw score).

*Owner:* Stauffer. *Effort:* none — already implemented in `grade_stage4.py`.

**5.5 Build a one-pass grading harness for AY 2026–27.** The fetch + grade scripts produced this term should be moved from `_tools/` (per-course) to `scripts/grading/` (repo-level) and parameterized by course/stage. This pays for itself the first time it's reused on BUS-314.

*Owner:* Stauffer (low priority — already functional in current location). *Effort:* medium.

**5.6 Pre-flight email two weeks before due date.** Send a short reminder to FIN-321 students roughly two weeks before Stage 4 due, including: (1) "your repo must be public," (2) "link to the Stage 4 file, not the repo root," (3) a one-line example. This addresses Cherry/Shimao/Ferayorni "didn't trust the flow" failures by making the flow explicit.

*Owner:* Stauffer. *Effort:* low. Can be scheduled as a recurring agent.

---

## 6. DECISION

| Recommendation | Action |
|---|---|
| 5.1 Submission-time link validator | **Adopt for AY 2026–27** if LMS supports it |
| 5.2 Require deep links | **Adopt** — update `stage4-final-analysis-assignment.md` |
| 5.3 Require public / grader-accessible repos | **Adopt** — update Stage 0 / project setup |
| 5.4 Accept inline content as fallback | **Codify existing practice** in rubric language |
| 5.4a +0.25 bump for GitHub link | **Adopted this term** — keep for AY 2026–27 |
| 5.5 Lift grading harness to repo level | **Defer** — revisit if reused on BUS-314 |
| 5.6 Pre-flight email | **Adopt** — schedule recurring agent for Spring 2027 |

Final grades are posted at `ignore-term/2026-Spring/stage4/_grading/stage4-grades-summary.md`. No grade reversals are recommended at this time; the floor and -0.5 penalty applied uniformly per the policy stated to students.

---

## 7. REFERENCES

- `courses/FIN-321-International-Finance-And-Securities/project-fx-hedging/stage4-final-analysis-assignment.md` — Stage 4 assignment spec (10-point rubric; this term graded out of 6 with 85% floor)
- `courses/FIN-321-International-Finance-And-Securities/_tools/fetch_stage4.py` — submission-fetching pipeline
- `courses/FIN-321-International-Finance-And-Securities/_tools/grade_stage4.py` — auto-grading pipeline
- `ignore-term/2026-Spring/stage4/_grading/stage4-grading-worksheet.xlsx` — full per-student worksheet
- `ignore-term/2026-Spring/stage4/_grading/stage4-grades-summary.md` — narrative grade summary
- `docs/decisions/fin321/2026-03-25-fin321-project-reorganization.md` — earlier decision to fold prompt engineering into final stage
