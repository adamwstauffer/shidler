---
template: stage-brief
project: perfect-competition-marginal-costs
stage: 1
title: "Engagement Brief"
capability: marginal-analysis
deliverables:
  - path: docs/briefs/perfect-competition-brief.md
    format: markdown
    ai_boundary: human-first
prerequisites: [0]
points: 1
estimated_time: "25-35 min"
---

# Case 1 · Stage 1 — Engagement Brief

**Deliverable:** `docs/briefs/perfect-competition-brief.md`
**Submission:** committed and pushed to your public repository; graded by inspection
**Estimated time:** 25–35 minutes

---

## 1. Purpose

One page stating the farm's problem in your own words and ending in a hypothesis you can be shown
wrong about. It is not analysis. It is the condition that makes the analysis worth anything — the
brief has to exist before the model does, because Stage 3 compares what you predicted against what
the model found, and that comparison cannot be reconstructed afterwards.

## 2. Prerequisites

- Stage 0: the portfolio repository, with `docs/briefs/` in place.

Read before starting:

- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) — the shape of a brief
- The [case README](README.md) — scenario, assumptions table, constraints

## 3. Deliverables

| Artifact | Path | Format |
|---|---|---|
| The engagement brief | `docs/briefs/perfect-competition-brief.md` | markdown |

## 4. Background

A prediction written *before* the model runs is falsifiable. The same sentence written afterwards is
a summary of the output, and it teaches you nothing, because you can no longer distinguish "I
understood the economics" from "I read the answer cell."

This is not a classroom convention. It is why a consultant writes an engagement brief before opening
the data, and why "we always thought so" is the least trustworthy sentence in business. A wrong
hypothesis, precisely reasoned, is worth as much as a correct one and considerably more than a lucky
one.

What makes a hypothesis genuine is that some outcome would refute it. *"I expect roughly 15 tomato
beds, 20 carrot, 25 mesclun, because tomatoes earn about four times what carrots do per bed and I
doubt the labor penalty closes that gap"* names quantities and a mechanism, and the model can
contradict it. *"I expect a balanced mix because diversification reduces risk"* would survive any
result, which is what disqualifies it.

## 5. Procedure

1. **Read the [case README](README.md)** — the scenario, the assumptions table, and the constraints.
   These are the facts your brief restates. Do not invent numbers.
   *Confirm:* you can state what the farm is deciding without looking back at the page.

2. **Write the brief** at `docs/briefs/perfect-competition-brief.md`, using the structure on the
   deliverable-templates page. **Before opening the workbook or Solver**, write half a page to a page
   covering two things:
   - **The problem in your own words.** What the farm is deciding, what is fixed, what is chosen,
     what limits the choice. If you cannot state it without re-reading the case, you do not have it
     yet, and that is useful information about where the next hour goes.
   - **Your hypothesis.** *"I expect the optimal mix to be X because Y."* Real quantities — beds of
     tomatoes, carrots, mesclun — and real reasoning: prices per bed, labor intensity, the
     diminishing-returns percentages, the caps. Name the mechanism you think decides it.

   *Confirm:* some outcome of the model would show your hypothesis wrong. If none would, it is not a
   hypothesis yet.

3. **Have it criticized, then answer the criticism yourself.** Ask a model to name your implicit
   assumptions, your unsupported claims, and whether your hypothesis is falsifiable — and to
   *not rewrite anything*. Then make the changes in your own words.
   *Confirm:* the prompt is logged, and the words in the brief are yours.

4. **Commit and push.** The message says what changed:
   `Add perfect-competition brief with mix hypothesis`.
   *Confirm:* the brief is committed **before any modeling begins**. The commit timestamp is what
   makes it a hypothesis rather than a summary, and there is no way to add it later.

## 6. AI use

| Artifact | Draft order |
|---|---|
| `docs/briefs/perfect-competition-brief.md` | Human-first |

**If the artifact is evidence of your judgment, you draft it first and AI reviews; if the artifact is
a means to the work rather than the work itself, AI may draft it and you verify.** The two working
loops are described in [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html).

**For this stage specifically:** AI may explain the case's economics and argue against your
reasoning; it may not write the brief. A hypothesis you did not generate cannot be honestly compared
against results in Stage 3, and that comparison is the point. Criticism of a draft you have already
written is in bounds and worth logging — the instruction that keeps it in bounds is *do not rewrite
it*.

## 7. Verification

- [ ] `docs/briefs/perfect-competition-brief.md` restates the problem in your voice
- [ ] The hypothesis names a specific mix **and** the mechanism behind it
- [ ] Some model outcome would show the hypothesis wrong
- [ ] The brief was committed **before** any modeling work started
- [ ] Any AI critique session is logged in `prompt-log.md`

## 8. Rubric (1 pt)

| Criterion | Pts | What distinguishes strong work |
|---|---|---|
| Brief quality — genuine hypothesis | 1 | Problem restated accurately in your own voice; hypothesis names a specific mix with economic reasoning, written before any Solver work |

## 9. Common failure modes

| What goes wrong | The correction |
|---|---|
| The hypothesis is hedged: "a balanced mix, because diversification" | Name quantities and a mechanism; a prediction that survives every outcome is not a prediction |
| The brief is written after the workbook | There is no recovery — the Stage 3 comparison is gone. Write it first, even badly |
| The problem statement paraphrases the case README sentence by sentence | Restating is not copying. If you cannot say it differently, you do not have it yet |
| The AI critique came back as a rewritten brief | You asked the wrong question. Ask it to name gaps and stop, then fix them yourself |
| Commit messages read `update` | Say what changed: `Add brief: predicting tomato-heavy mix on price per bed` |

## 10. References

- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) · [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html)
- [Case README](README.md) — scenario, assumptions, constraints
