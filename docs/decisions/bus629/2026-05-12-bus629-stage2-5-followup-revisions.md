---
title: "BUS-629 Stages 2–5 — follow-up revisions for AY 2026-27"
date: 2026-05-12
status: proposed
owner: Adam W. Stauffer
course: BUS-629-VEMBA-International-Corporate-Finance
scope: course
applies_to: future semesters (current Spring 2026 cohort already in flight)
related:
  - 2026-05-07-bus629-stage2-restructure.md
  - 2026-05-12-bus629-stage1-excel-literacy-gap.md
  - ../2026-05-10-claude-plugins-student-rollout.md
---

# BUS-629 Stages 2–5 — follow-up revisions for AY 2026-27

## Summary

The 2026-05-07 restructure memo settled the broad shape of BUS-629's project pipeline: Stage 2 frames, Stage 3 populates, Stage 4 specs, Stage 5 executes-and-evaluates. After reading the current state of `stage2-*.md` through `stage5-*.md`, four refinements are worth proposing for AY 2026-27 — none of them re-litigate the restructure, all of them tighten enforcement of behaviors the rubrics already aspire to. Cross-stage, three threads emerge: (1) the **peer set** is implicitly required at Stage 5 but never produced upstream; (2) **manual verification** of LLM output is called for in the rubric language at Stage 5 but never enforced as an artifact; (3) the **plugin rollout** (memo 2026-05-10) creates new options at Stage 4 that are currently unaddressed. The current Spring 2026 cohort is out of scope.

## Context

This memo builds on:

- **`2026-05-07-bus629-stage2-restructure.md`** — settled stage weights, the financials-only / LLM-spec / synthesis split, and the 70/30 deliverable/presentation rubric for Stages 2, 4, 5.
- **`2026-05-12-bus629-stage1-excel-literacy-gap.md`** — proposed adding active-demonstration tasks to Stage 1 for future semesters.
- **`2026-05-10-claude-plugins-student-rollout.md`** — identified BUS-629 as a Tier 2 opt-in pilot for the `financial-services` plugins.

Reading each stage doc end-to-end surfaces refinement opportunities the broad restructure didn't address.

---

## Stage 2 — Company Selection Memo (10%)

**Current state:** 400–600 word memo + 3–5 minute presentation. Required sections cover company overview, rationale, data sources, preliminary hypotheses, ratio categories, data plan. Rubric is 70/30 deliverable/presentation.

### Observations

1. **The memo is addressed to a boss, but there's no formal feedback cycle.** Stage 5 explicitly mentions "your Stage 2 memo with any comments I have" as an input to the final analysis. The student is supposed to incorporate instructor feedback between Stage 2 and Stage 5 — but Stage 2's deliverable terminates at submission, and Stage 5's deliverable doesn't reward demonstrably incorporating feedback. The feedback loop is implicit, not graded.
2. **No peer set is identified at selection time.** Real analysts pick a peer comparison set at the moment they pick a company; deferring this to Stage 5 means the synthesis stage starts without a benchmark. The Data Collection Plan section could absorb this.
3. **Hypothesis quality is in the presentation rubric but not the deliverable rubric.** The Tips section emphasizes falsifiable hypotheses ("I expect X because Y"), but the 4-line deliverable rubric weights "Analytical Framing & Hypotheses" without specifying falsifiability as a quality criterion.

### Proposed revisions

| # | Change | Mechanism |
|---|--------|-----------|
| 2A | Add a required **peer-set table** to the memo's Data Collection Plan section: 3–5 comparable companies with ticker, exchange, market cap, fiscal year end. | New section line item; ~50 words. |
| 2B | Make hypothesis falsifiability an explicit rubric criterion ("Each hypothesis states a directional expectation and a reason"). | Replace "Analytical Framing & Hypotheses" criterion text. |
| 2C | Reserve 5% of Stage 5's deliverable rubric for "demonstrably incorporated Stage 2 feedback" (track changes, reply-to-comments commit, or revised memo committed alongside the final analysis). | Stage 5 rubric line item; described under Stage 5 below. |

---

## Stage 3 — Populated Financials (20%)

**Current state:** Upload of populated workbook. Self-check items listed but not graded as artifacts. Rubric is 40% accuracy + 25% completeness + 20% source docs + 15% formula-error-free.

### Observations

1. **Validation is described, not enforced.** The self-check table tells students what to verify ("BS balances, no `#REF!`, sign sanity, source documentation") but doesn't ask for evidence that they did. A student who skipped the self-check is graded the same as one who didn't — until errors are caught by the instructor at grading time.
2. **Currency and units traps are real for VEMBA cohorts.** Vietnamese companies report in VND (often in millions); the cover-tab unit field is a single point of failure for the entire ratios computation. Currently this is buried in tips.
3. **Source documentation is asked for but not date-stamped.** Companies amend filings; the "as-accessed-on" date matters for reproducibility.
4. **No structured connection to Stage 2's peer set (if adopted).** If 2A lands, Stage 3 should optionally accept lightweight peer-financial entries (top-level totals only) to give Stage 5 something to compare against.

### Proposed revisions

| # | Change | Mechanism |
|---|--------|-----------|
| 3A | Require a **validation note** at `analysis/validation/stage3-validation.md` — short markdown checking off each self-check item with a one-line "verified by" note (e.g., "BS balanced: 1,234,567 = 1,234,567, both years"). | New deliverable; ~150 words; ~10% rubric weight (carved from accuracy). |
| 3B | Promote the **units/currency** line from tip to rubric: rename "Source documentation" criterion to "Source documentation + units/currency consistency" with explicit weighting. | Rubric text change. |
| 3C | Require a **filing access date** in the Cover & Instructions tab, separate from the filing's own publication date. | One-line addition to workbook requirements. |
| 3D | (Conditional on 2A) Allow a `data/peers/` directory with one-row-per-peer top-level financials (Total Revenue, Total Assets, Total Equity, Net Income). Lightweight; not required for Stage 3 grade, but rewarded at Stage 5. | New optional directory in repo structure. |

---

## Stage 4 — LLM-Drafted Spec (20%)

**Current state:** Heaviest stage. Two workflows (desktop / CLI). Part A (model spec, 7 items) + Part B (analysis spec, 4 items). Rubric: 25%/25%/25%/25%. Quality test is described as "feed the spec to a fresh LLM and see if Stage 5 succeeds" — but this is described, not executed at Stage 4.

### Observations

1. **The self-contained quality test is aspirational, not enforced.** Stage 4 says "if the LLM at Stage 5 can't reconstruct the analysis from this spec alone, the spec has gaps." But the test is only really run at Stage 5 — by which point Stage 4 is already graded. Students don't get the feedback signal in time to revise.
2. **The "Stage 4 = precursor to a Claude Code skill" framing is informal.** The instructor's stated framing (per design conversations) is that the spec resembles a `SKILL.md` file. Stage 4 doesn't make this concrete — there's no template structured as a skill, and no encouragement to produce a portable artifact.
3. **The plugin rollout opens new Stage 4 options.** Per the 2026-05-10 memo, `audit-xls` and `financial-analysis` plugins are now available in this repo. Students using the CLI workflow could lean on these constructively (e.g., audit-xls verifying their Stage 3 workbook before specifying the analysis). Stage 4 currently doesn't address plugin use.
4. **Prompt-log standards are loose.** "Spec craft + prompt log quality" is 25% of the deliverable, but the prompt-log-template is generic and not tuned to spec-drafting. What constitutes a "meaningful iteration" is left to grader judgment.

### Proposed revisions

| # | Change | Mechanism |
|---|--------|-----------|
| 4A | Add a required **dry-run quality test** to the Stage 4 deliverable: student feeds their spec to a fresh LLM session (no prior context), saves the output as `analysis/validation/stage4-dryrun.md`, and writes a 100-word note on what gaps the dry-run exposed and how the spec was revised. | New artifact; ~10% rubric weight (carved from "Spec craft"). Closes the feedback loop inside Stage 4. |
| 4B | Provide a `SKILL.md`-formatted spec template alongside the existing markdown spec template, and document that strong specs map 1:1 to a skill file (frontmatter `name`/`description`, body = the spec). Optional adoption. | New template at `docs/templates/skill-spec-template.md`; cross-link from Stage 4. |
| 4C | Add a third workflow option ("Workflow C — Claude Code CLI with plugins") referencing `audit-xls` (verify Stage 3 workbook) and `financial-analysis` (used constructively to populate Part A's Data Inputs table). Stage 4 deliverable rubric does not require plugin use; it just documents the option. | New section in Stage 4 doc; coordinates with the plugin rollout pilot. |
| 4D | Tighten the prompt-log rubric: at least one iteration must show "spec gap identified → prompt revised → improved output." Generic prompt logs ("I asked Claude to write the spec") do not earn the credit. | Rubric criterion text revision. |

---

## Stage 5 — Synthesis + Repo Polish (25%)

**Current state:** Capstone. Three things at once: execute spec, evaluate LLM output, polish repo. Required artifacts: raw LLM output + evaluated analysis + spec retrospective + prompt log. Rubric: 30% correctness + 25% LLM eval/retro + 20% recommendations/voice + 25% repo polish.

### Observations

1. **"LLM errors caught and corrected" is in the rubric language but not in the required artifacts.** The student can claim they caught errors without producing the verification table that proves it. This is the single biggest gap — it's the "did the student actually engage critically with the AI" test.
2. **Spec retrospective rigor varies widely.** The Tips section gives a strong example ("Part B section 9 was vague because…"); the rubric rewards specificity. But there's no structural prompt — students can submit a vague retrospective and the grader has to push back individually.
3. **Peer benchmarking is implicit.** Strategic Recommendations are required to be "actionable" and "backed by ratio evidence" but the rubric doesn't say "vs. what." Recommendations without a comparison set are weak.
4. **Repo polish is well-specified but recruiter-blind on a few details.** Missing from the checklist: a 1-line repo description (top-right of GitHub page), a top-of-README "what you'll find here" / project status block, a `LICENSE` file (relevant for public portfolio repos), a `.gitignore` excluding `.DS_Store`, `~$*.xlsx`, etc. These are the things a hiring manager sees first.
5. **Stage 2 feedback incorporation is not graded** (see Stage 2 observation 1).

### Proposed revisions

| # | Change | Mechanism |
|---|--------|-----------|
| 5A | Require a **manual verification table** at `analysis/validation/stage5-verification.md`: pick at least 5 ratios, recompute manually from Stage 3 financials, compare to the LLM's stated values, mark match/discrepancy, write a 1-line note on each discrepancy. | New required artifact; ~10% rubric weight (carved from "Analytical correctness"). |
| 5B | Add a **structured spec retrospective template** at `docs/templates/spec-retrospective-template.md` — required sections: section-by-section verdict, top-3 spec gaps with evidence from the dry-run (4A) and final output, what you'd change, effectiveness rating (1–5). | New template; cross-link from Stage 5 doc. Tightens 25% retrospective criterion. |
| 5C | Require **peer benchmarking** for at least 2 of the 3–5 strategic recommendations. Peer comparison numbers may come from the Stage 3 peer-set table (3D) or from secondary research at Stage 5. | New rubric criterion under "Strategic Recommendations." |
| 5D | Expand the **repo polish checklist** with: 1-line repo description, top-of-README project status / "what you'll find" block, `LICENSE` (Apache-2.0 or MIT recommended), `.gitignore` excluding common scratch files. | Stage 5 polish checklist additions. |
| 5E | (From 2C) Reserve **5% of Stage 5 deliverable rubric for incorporating Stage 2 feedback**: visible in repo as a revised memo committed alongside the final analysis, or as commits replying to instructor feedback. | New rubric line item. |

Proposed Stage 5 deliverable rubric reshuffle:

| Criterion | Current | Proposed |
|-----------|--------:|---------:|
| Analytical correctness (incl. 5A manual verification) | 30% | 25% |
| Manual verification artifact (5A) | — | 10% |
| LLM evaluation + spec retrospective (template 5B) | 25% | 25% |
| Strategic recommendations + peer benchmarking (5C) | 20% | 20% |
| Stage 2 feedback incorporation (5E) | — | 5% |
| Repo polish (with 5D expansions) | 25% | 15% |
| **Total** | **100%** | **100%** |

Repo polish drops from 25% → 15%; manual verification carves 10% of its own; Stage 2 feedback gets 5%. Polish remains substantive but no longer dominates the rubric over analytical engagement.

---

## Cross-stage threads

### Peer set as a first-class artifact (Stages 2 → 3 → 5)

The single most useful structural change across stages. Currently each stage assumes the student has a peer comparison without ever producing one. Adopting 2A + 3D + 5C threads a peer set through the entire pipeline; declining all three keeps peer comparison as a Stage-5 ad-hoc exercise. Recommend all-or-nothing.

### Manual verification as the audit muscle (Stage 1 → Stage 5)

If the Stage 1 audit task (`2026-05-12-bus629-stage1-excel-literacy-gap.md`) is adopted, students arrive at Stage 5 having already practiced "find the bug in a spreadsheet." Stage 5's verification table (5A) is the production-scale version of that exercise — same skill, real stakes. Conceptually clean.

### Plugin integration as Stage 4 pilot

The 2026-05-10 memo identifies BUS-629 as Tier 2 (opt-in pilot) for the `financial-services` plugins. Proposal 4C operationalizes that pilot at exactly the right stage. Recommend keeping it strictly optional for the first cohort that sees these revisions — promote to recommended only after watching how a self-selected subset uses it.

### Bilingual cohort considerations (all stages)

Out of scope for this memo, but a parallel decision is warranted: should any stage allow Vietnamese-language deliverables with English summaries, or English with Vietnamese visual aids? The current "all deliverables in English" policy is workable but worth revisiting at the cohort-feedback stage. Flag for separate memo.

---

## Recommendation summary

**Adopt for AY 2026-27** (high confidence, low friction):

- 2B (hypothesis falsifiability in rubric), 2C/5E (feedback incorporation)
- 3A (validation note), 3B (units/currency rubric line), 3C (filing access date)
- 4A (Stage 4 dry-run), 4D (prompt-log standards)
- 5A (manual verification table), 5B (retrospective template), 5D (repo polish expansions)

**Adopt as a coordinated set** (peer-set thread — adopt all or none):

- 2A, 3D, 5C

**Pilot optional**:

- 4B (skill-format spec template) — provide; don't require
- 4C (plugin workflow) — coordinate with 2026-05-10 rollout

## Risks and tradeoffs

- **Workload creep.** Adding artifacts (3A, 4A, 5A) increases student deliverable count. Total weight is unchanged, but cognitive load rises. Mitigate by making each new artifact small (≤200 words / one short table) and providing templates.
- **Rubric complexity.** Adding rubric lines makes grading more deterministic but also more bureaucratic. The proposed Stage 5 rubric has 6 lines vs. 4 today. Watch grading time per submission as the test.
- **Plugin pilot dependency.** 4C only makes sense if the plugin rollout pilot is actually run. If the AY 2026-27 cohort skips plugins, drop 4C.
- **Peer-set thread is all-or-nothing.** Adopting 2A without 3D and 5C creates an orphan artifact at Stage 2. Cleanest to commit to the full thread or none of it.
- **Bilingual question deferred.** Not addressing language at all may be wrong for VEMBA — but addressing it inside this memo would expand scope. Recommend a separate decision before AY 2026-27 launch.

## Out of scope

- **Current Spring 2026 cohort.** All revisions apply to AY 2026-27 onward. No mid-course rubric changes.
- **BUS-314 / FIN-321 parallels.** Several proposals (manual verification, peer set, validation notes) could backport to the undergrad courses. Separate decision.
- **Bilingual language policy.** Flagged here, addressed elsewhere.
- **Implementation order.** This memo proposes *what* to adopt; sequencing and template/skill construction are an implementation-plan concern.

## Open questions

1. Is the AY 2026-27 cohort timing fixed enough to lock these revisions before semester start, or will revisions land iteratively?
2. Should the peer-set thread (2A + 3D + 5C) be required or optional for the first revised cohort? Optional gives a control group; required gives uniform data.
3. Does adopting 4B (skill-format spec template) align with the broader student skill-building arc, or is it premature for VEMBA students who may not be using Claude Code at all?
4. If plugin pilot proceeds (4C), does the instructor want telemetry on which students used which plugins (via commit-log inspection of any `.claude/` artifacts they produce), or is opt-in opt-in?
5. Should "Stage 2 feedback incorporation" (2C/5E) be a hard gate (cannot submit Stage 5 without it) or a rubric criterion (graded but not blocking)?
