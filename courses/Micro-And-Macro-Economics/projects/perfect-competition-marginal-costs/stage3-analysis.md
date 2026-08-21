---
template: stage-brief
project: perfect-competition-marginal-costs
stage: 3
title: "Analysis + Prompt Log"
capability: marginal-analysis
deliverables:
  - path: analysis/perfect-competition-analysis.md
    format: markdown
    ai_boundary: human-first
  - path: analysis/figures/
    format: images
    ai_boundary: not-permitted
  - path: docs/decisions/perfect-competition-memo.md
    format: markdown
    ai_boundary: human-first
  - path: prompt-log.md
    format: markdown
    ai_boundary: human-first
prerequisites: [1, 2]
points: 9
estimated_time: "3-4 hrs"
---

# Case 1 · Stage 3 — Analysis + Prompt Log

**Deliverable:** the analysis with figures, the recommendation memo, and an updated prompt log
**Submission:** committed and pushed to your public repository; graded by inspection
**Estimated time:** 3–4 hours

---

## 1. Purpose

Stage 2 produced a number. This stage produces the reason: an explanation of *why* that is the
answer, in economics, using your own model's evidence — and then a recommendation written to the
person who has to act on it. A Solver output you cannot explain is a coincidence you happen to have
committed.

## 2. Prerequisites

- Stage 1: `docs/briefs/perfect-competition-brief.md` — the hypothesis you are now testing.
- Stage 2: `capabilities/marginal-analysis/model.xlsx` — the evidence source. Every number you cite comes
  from it.

Read before starting:

- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) — the memo structure and the prompt-log format.

## 3. Deliverables

| Artifact | Path | Format |
|---|---|---|
| The evidence — what the model shows and why, for someone checking your work | `analysis/perfect-competition-analysis.md` | markdown |
| At least two figures the analysis refers to | `analysis/figures/` | images |
| The answer — what the farmer should do, for the farmer | `docs/decisions/perfect-competition-memo.md` | markdown |
| The curated record of AI sessions, plus the reflection | `prompt-log.md` | markdown |

**Briefs ask; memos answer.** You wrote the question in Stage 1; this is where you close it. The
analysis is the file a reviewer audits; the memo is the file a decision-maker reads.

## 4. Background

Four things in this model are worth explaining, and together they are what the analysis has to
cover.

**Where marginal cost crosses price.** Tomatoes are the clean case — interior at 10 beds, MC $8,249
at bed 10 against a price of $8,800, with bed 11 costing $9,391.

**Which constraints bind, and what they are worth.** Carrots and mesclun stop at their bed caps with
MC still *below* price: the constraint ends production, not the economics. One more carrot bed would
add roughly **$352** of profit, one more mesclun bed roughly **$246**. Some constraints never bind at
all — 64 total beds and 4 temporary workers are both slack.

**The tomato MC dip at about 6 beds.** Marginal cost falls before it rises. The farmer's own field
hours at $34.72/hr run out, marginal labor switches to temporary labor at $17.36/hr, and then
diminishing returns push MC back up through the price line. This is the lesson that input prices bend
the marginal-cost curve, and it is the most interesting thing in the model.

**Why growing loss-making crops is correct.** Standalone, every crop loses money at every quantity,
because fixed costs dominate. The resolution is marginal cost against average *variable* cost: price
exceeds AVC everywhere, so every bed contributes above variable cost, and the *mix* — not any single
crop — is what turns a loss into $42,762. This is the short-run shutdown rule in farm clothes.

## 5. Procedure

1. **Write the analysis** at `analysis/perfect-competition-analysis.md`. One to two pages, covering
   all four questions above from your own workbook's numbers.
   *Confirm:* each claim points at a cell or a figure in your model, not at a textbook generalization.

2. **Export at least two figures** into `analysis/figures/` — the MC-versus-price charts are the
   obvious pair — and reference each one in the text.
   *Confirm:* the images render on the github.com page, not merely in your editor. Relative links
   are easy to get wrong.

3. **Close the analysis against your hypothesis.** One honest paragraph: what you predicted, what the
   model found, what your prior got right or wrong.
   *Confirm:* the paragraph names a specific difference. Being wrong in the brief and precise about
   why here is full-credit work.

4. **Write the memo** at `docs/decisions/perfect-competition-memo.md`. Half a page, addressed to
   whoever signs off on the plan — a partner, a lender, or you next February — with no jargon they
   did not ask for. Three things belong in it:
   - **The plan.** Plant 10 / 20 / 30, and one sentence of reasoning a non-economist would accept.
   - **The judgment call.** Both caps bind, and one is worth more to relax than the other. Which
     ground is worth spending money to expand first, and what is one more bed worth? That number came
     out of your shadow-price work; here it becomes advice.
   - **What would change your answer.** One line naming the variable the recommendation is most
     sensitive to.

   *Confirm:* it takes under twenty minutes to write. If it takes longer, the analysis has not
   finished its job — that is a signal, not a writing problem.

5. **Update `prompt-log.md`** at the repository root — a dated section for this engagement, not a new
   file. Log the sessions that *mattered*: where AI explained something, caught or introduced an
   error, or pushed your reasoning. Date, tool, what you asked, what you got, what you did with it.
   *Confirm:* it is a curated record, not a transcript dump.

6. **Write the reflection**, 300 words or fewer, at the end of the log: where AI helped, where it was
   wrong, and — graded hardest — *how you verified*.
   *Confirm:* the verification is concrete. "It seemed right" is not verification; "I checked its MC
   formula against the labor function at `q = 1` and it had dropped the exponent" is. If AI genuinely
   made no error you could catch, document the checks that convinced you.

7. **Update `capabilities/marginal-analysis/README.md`** so its "exercised in:" line points at the analysis
   and the memo as well as the brief.
   *Confirm:* the capability now links to all of its evidence.

8. **Commit at least twice** with descriptive messages.

## 6. AI use

| Artifact | Draft order |
|---|---|
| `analysis/perfect-competition-analysis.md` | Human-first |
| `docs/decisions/perfect-competition-memo.md` | Human-first |
| `prompt-log.md` and the reflection | Human-first |
| Figures | Exported from your own workbook — not generated |

**If the artifact is evidence of your judgment, you draft it first and AI reviews; if the artifact is
a means to the work rather than the work itself, AI may draft it and you verify.** The two working
loops are described in [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html).

**For this stage specifically:** AI may explain concepts, critique your reasoning, and help debug
formulas. It may not write the analysis, the memo, or the reflection. The line, concretely: asking AI
to critique your draft explanation of the MC dip is in bounds and worth logging. Pasting the case in
and asking for an analysis is out of bounds — and it shows, because AI-written analysis explains the
textbook rather than *your workbook's* numbers.

## 7. Verification

- [ ] P = MC evidence shown per crop, from your model's own numbers
- [ ] Binding caps identified, with shadow-price reasoning (~$352 carrots, ~$246 mesclun)
- [ ] Slack constraints named — 64 beds and 4 temporary workers
- [ ] The tomato MC dip explained by mechanism, not merely observed
- [ ] The "grow at a loss?" paradox resolved with MC versus AVC
- [ ] At least two figures in `analysis/figures/`, each referenced in the text
- [ ] Figures render on the GitHub page, not just in your editor
- [ ] Honest paragraph comparing the result against your Stage 1 hypothesis
- [ ] Memo written: the plan, the judgment call, and what would change your answer
- [ ] Prompt log updated with curated sessions and a reflection of 300 words or fewer
- [ ] Reflection names something concrete you verified, and how
- [ ] `capabilities/marginal-analysis/README.md` "exercised in:" line updated
- [ ] At least two descriptive commits for this stage

## 8. Rubric (9 pts)

| Criterion | Pts | What distinguishes strong work |
|---|---|---|
| P = MC evidence + binding constraints | 3 | Crossings shown from *your* model's numbers; carrot and mesclun caps identified as binding with ~$352 / ~$246 shadow-price reasoning; slack constraints named; the memo turns that into a recommendation the farmer could act on |
| MC dip + at-a-loss resolution | 2 | Dip mechanism (permanent-to-temporary wage switch) explained, not just observed; MC-versus-AVC shutdown logic resolves the loss-making crops correctly |
| Figures + hypothesis revisit | 1 | At least two figures referenced in text and rendering on GitHub; honest comparison against the Stage 1 hypothesis |
| Prompt log + reflection | 3 | Sessions curated, not dumped; reflection of 300 words or fewer with concrete instances of AI being wrong and *how you verified* — or, if nothing was caught, the checks that cleared it |

The memo carries no separate points. It is read together with the analysis under the P = MC evidence
and binding-constraints criterion, which already asks what a farmer should conclude from a binding
cap. What changes is where that conclusion lives, and that it is written to a person rather than to a
rubric.

## 9. Common failure modes

| What goes wrong | The correction |
|---|---|
| The analysis cites the textbook instead of the workbook | "MC rises due to diminishing returns" is a lecture note. "Carrot MC hits $1,742 at bed 20, still $352 under price — the cap binds" is analysis |
| Figures are decorative | Every figure earns its place by being referenced in the text. An unreferenced chart is worth nothing |
| Figures do not render on GitHub | Relative paths are case-sensitive and must be repository-relative. Check the rendered page |
| The MC dip is ignored | It is the one place this model surprises people. An analysis that skips it has skipped the most interesting result |
| The memo restates the analysis | A memo recommends. If it summarizes, the two documents have swapped jobs |
| The prompt log is reconstructed the night before | It produces generic mush that is obvious to a reader. Two lines per session, written at the time, is effortless |
| The reflection claims AI made no mistakes | Without evidence of checking, that reads as not having looked. Document the verification that cleared it |

## 10. References

- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) — the memo structure and prompt-log format
- [Farm Profit Lab](https://adamwstauffer.github.io/ai-lms/farmlab.html) — makes the MC dip visible in ten seconds of dragging
- [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html) · [Portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html)
- [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics), including [how work is submitted, with the post-deadline revision policy](https://adamwstauffer.github.io/ai-lms/onboarding.html#submitting)
- [Case README](README.md) — assumptions and check figures
