# BUS-629 Pop-Quiz Extension — Design Decision Memo

**Created by:** Adam W. Stauffer
**Date:** 2026-05-16
**Status:** Draft for instructor review
**Audience:** Full VEMBA cohort with completed Stage 5
**Format:** Surprise extension assignment ("pop quiz"); time-boxed, individual, deliverable-only
**Calibration target:** ~50% pass rate on first attempt

---

## Executive Summary

The VEMBA cohort has completed the BUS-629 spec-driven ratios pipeline through Stage 5. Across the cohort, Stage 4 specs and Stage 5 final analyses showed strong analytical writing and executive voice but uneven discipline on the two artifacts that test *whether each student's spec actually works in production*: manual verification (the cross-check on LLM hallucination) and the spec retrospective (the closed-loop critique). A surprise extension is the right instrument to harden those exact muscles without rewriting the rubric or re-opening Stage 5 grades.

This memo proposes a **single-sitting, 6-hour pop-quiz extension** that takes each student's own Stage 4 spec and stress-tests it along two axes most of the cohort did not exercise: **spec portability** (does the spec generalize from the student's focal company to a self-selected international peer?) and **FX translation sensitivity** (do the ratios hold up under realistic ±15% home-currency scenarios?). The deliverable is a 350-word CFO-style memo, a structured spec-failure log, a manually-verified FX sensitivity grid, a peer-selection rationale, and the raw LLM session. Pass/fail is judgment-graded against a fixed 7-point rubric; the existing Stage 5 score is unaffected.

The assignment is deliberately calibrated so that **roughly half the cohort will clear the pass bar on first attempt.** Spec portability is a senior skill, and the FX work surfaces translation-vs-transaction issues most MBA finance courses skip. Students who pass have demonstrated something most peer programs do not certify; students who fail get one round of written feedback and a revision window.

---

## Background

### What the cohort has shown

- **Stage 4 specs** — executable LLM specs across a range of multinationals chosen by each student
- **Stage 5 final analyses** — full reports with executive summaries, ratio interpretation, and strategic recommendations
- **Repo discipline** — clean structure and reproducibility consistent across most submissions

### Where the existing work was thin (cohort-wide pattern)

Without quoting the rubric line-by-line, two artifacts came in lightest across the cohort:

1. **Manual verification** — the artifact that proves the student can catch LLM hallucinations
2. **Spec retrospective** — the structured "what would I change about my own spec" file

These are precisely the spec-driven-design failure modes the project exists to teach. A surprise extension targeted at those gaps is more useful than a cohort-wide re-grade.

### Why "pop quiz" framing

- **Surprise** removes the option to re-scope or hedge — replicates real exec-briefing pressure
- **Time-boxed** (6 hours, single sitting) forces prioritization, the EMBA-level skill
- **Builds on existing artifacts** — zero new setup cost; each student reuses their own spec and workbook
- **Off-rubric** — no impact on Stage 5 grade; framed as a stretch challenge, not a punishment

---

## Proposed Assignment

### Title
**"CFO Briefing: Does Your Spec Survive Contact With Reality?"**

### Scenario (prompt to student)

> Your CFO has read your Stage 5 analysis and has two follow-up questions. Both are due as a single one-page memo (≤350 words). You have your existing Stage 4 spec, your Stage 3 workbook, and one LLM session. No re-doing the spec from scratch — you have to *use what you built*.
>
> 1. **"Pick the strongest international peer to your Stage 5 company, run your spec on them, and tell me which of your Stage 5 conclusions still apply and which break."** Choose the peer yourself and defend the choice in one paragraph. If your framework is sound it should generalize; if it doesn't, I want to know exactly where it fails.
>
> 2. **"Re-run your Stage 5 ratios under three FX scenarios — spot, home currency +15%, home currency −15% — and tell me which ratios are FX-sensitive and which are not. Then tell me what you'd do differently as CFO under the adverse scenario. Be explicit about whether each FX effect is translation, transaction, or both."**

### Required deliverables (single repo PR, branch `pop-quiz-extension`)

| # | File | Length / requirement |
|--:|------|----------------------|
| 1 | `analysis/pop-quiz/cfo-briefing.md` | ≤350 words, hard cap; self-contained (no "see appendix" hand-offs) |
| 2 | `analysis/pop-quiz/spec-failure-log.md` | ≥5 entries; each entry must quote the original spec line and propose a concrete fix |
| 3 | `analysis/pop-quiz/fx-sensitivity-table.md` | Ratio × {Spot, +15%, −15%} grid; ≥5 rows manually recomputed against the LLM output with the recomputation shown step-by-step |
| 4 | `analysis/pop-quiz/peer-selection-rationale.md` | ≤150 words; must address sector overlap, geography, size band, and accounting regime |
| 5 | `analysis/pop-quiz/raw-llm-output.md` | Unedited LLM session(s); ≥1 caught hallucination annotated inline |

### Constraints

- **6-hour wall-clock budget**, single sitting, self-reported at the top of the CFO memo
- **One LLM session** — model and version logged; multiple sessions = automatic fail
- **Manual recomputation required** for ≥5 FX-sensitive ratios, shown step-by-step
- **No revisions to the original Stage 4 spec file** — the failure log is *about* the original spec, not a rewrite of it
- **Audience framing:** senior CFO who has read the student's Stage 5 memo; no re-explanation of basics
- **Peer selection is part of the test.** A poorly chosen peer (no real sector overlap, opaque disclosures, no English-language statements, mismatched fiscal year) will torpedo the rest of the analysis and is not the instructor's problem
- **No instructor-provided peer list.** Asking for one is itself a signal

### Pass rubric — must hit ≥5 of 7

1. **Peer defensibly chosen.** Sector, geography, size band, and accounting regime all addressed in the rationale
2. **Spec failures named honestly.** ≥5 entries, each quoting the original spec line and proposing a concrete fix; defensive entries ("the spec was fine, the data was bad") do not count
3. **FX-sensitive ratios manually recomputed.** ≥5 ratios shown step-by-step, tied to the LLM output cell-by-cell
4. **Translation-vs-transaction distinction made correctly.** At least one ratio explained on each side, with an explicit reason
5. **CFO memo ≤350 words and self-contained.** No appendix hand-offs to dodge the cap
6. **At least one Stage 5 conclusion confirmed and one broken** by the peer test, each with explicit evidence (specific ratio + specific delta)
7. **At least one LLM hallucination caught and annotated.** Silent acceptance of clean LLM output is a fail signal, not a pass signal

**Outcomes:** Strong Pass (7/7) · Pass (5–6/7) · Fail (≤4/7). Failed attempts receive one round of written narrative feedback and a 72-hour revision window. Calibration target: ~50% of the cohort clears the pass bar on first attempt.

---

## Rationale

### Why this is "super hard"

- **Spec portability is a senior skill.** Junior analysts run specs; senior people *design specs that survive being run on the wrong company*. Most MBAs have never been asked to do this.
- **Peer selection is itself the trap.** Choose a peer with local-GAAP-only disclosures, segment reporting that doesn't tie out, or a misaligned fiscal year, and the rest of the analysis collapses. Choosing well requires real industry knowledge, not a Google search.
- **The 350-word cap is brutal.** Five stages of long-form writing have trained the cohort in the opposite direction. CFO compression is a different skill, and it's the one most likely to fail under time pressure.
- **The translation-vs-transaction line is the technical content most MBA finance courses skip.** Getting it right separates the half that passes from the half that doesn't.
- **One LLM session with ≥1 caught hallucination required.** Students who treated the LLM as an oracle through Stage 5 cannot pass without changing how they work.

### Why a 50% pass rate is the right target

- A 90% pass rate signals the bar is rubric-checking, not skill-testing
- A 20% pass rate signals an unfair surprise
- A 50% pass rate is consistent with how real promotion-level decisions are evaluated in industry: the work is hard, the criteria are explicit and published, and "good enough at this stage" is genuinely not good enough at the next one
- Failure here is recoverable — one revision cycle, no grade impact — so the calibration cost to students is low and the signal to those who pass is high

### Why it's still fair

- Reuses artifacts each student already built; no new data acquisition required
- Plausible international peers across the cohort's focal sectors all have English-language IR disclosures
- 6 hours is enough if the student trusts their own spec; not enough if they were secretly relying on extra LLM hand-holding through earlier stages
- Pass/fail framing means a strong analytical attempt is rewarded even when peer specifics are imperfect
- **The rubric is published with the prompt** — no hidden criteria, no moving targets

### Why now

VEMBA Stage 5 just closed (yesterday). This is the moment when the spec-driven-design ideas are freshest — and when the gap between "I wrote a spec" and "my spec is portable" is most teachable.

---

## Risks and Open Questions

| Risk | Mitigation |
|------|------------|
| Students read "pop quiz" as punishment | Cover email frames it as an opt-in stretch challenge; explicit no-grade-impact line; emphasize the published rubric and the revision window |
| 6 hours is too little for unfamiliar peer research | The peer is self-selected — choosing a research-heavy peer is on the student. The rubric explicitly rewards judicious peer choice. |
| Some students don't accept | Optional. No follow-up if declined. Acceptance rate is itself a cohort signal worth reading. |
| Peer disclosures rely on local-GAAP quirks the spec can't anticipate | That's the point — the spec-failure log is *supposed* to be long. Length and specificity of the log are positive signals. |
| FX scenario produces an apples-to-oranges issue for USD-reporting companies | Acceptable for the student to argue scenarios apply to *segment-level translated revenue and EBIT*. Catching that distinction is itself a pass signal. |
| ~50% fail rate produces complaints | The rubric is explicit, published with the prompt, and failure is recoverable via the 72-hour revision window. Calibration is the point, not the cost. |
| Students collude or share peer choices | The CFO memo is individual; identical peer rationale across two PRs is investigable. Spec-failure logs are anchored to each student's own Stage 4 spec, which differs across the cohort. |

### Open questions for instructor

1. **Channel:** Email-only cohort announcement, or a brief synchronous notice? *Recommend: email-only, one shot, no preamble — preserves the surprise.*
2. **Deadline:** Sunday EOD (Vietnam time) gives ~24+ hours of elapsed wall-clock for a 6-hour sitting. *Recommend: Sunday EOD; the wall-clock budget enforces the discipline, not the deadline.*
3. **Public artifact:** Does each pop-quiz PR get merged into the student's public portfolio repo, or kept in a draft branch? *Recommend: student's call after seeing feedback — strong-pass usually merges, fail usually stays in draft.*
4. **Revision window for failed attempts:** Confirm 72 hours and a single revision pass. *Recommend: yes — preserves the difficulty signal without making failure terminal.*

---

## Recommendation

Approve the assignment as drafted, with the four open questions resolved as recommended above. If approved, next step is a short cover email to the cohort and the actual assignment markdown file (`pop-quiz-extension-assignment.md`) committed to the course repo for reproducibility.

Total instructor effort to launch: ~30 minutes (cover email + assignment file). Grading effort: ~30 minutes of written narrative feedback per returned attempt; cohort total scales with acceptance rate. At the calibration target, expect roughly half the returned attempts to require a feedback-and-revision cycle.
