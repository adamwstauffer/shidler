---
template: stage-brief
project: imperfect-competition-marginal-revenue
stage: 2
title: "Analysis, Memo, Prompt Log"
capability: pricing-power
deliverables:
  - path: analysis/imperfect-competition-analysis.md
    format: markdown
    ai_boundary: human-first
  - path: analysis/figures/
    format: images
    ai_boundary: not-permitted
  - path: docs/decisions/imperfect-competition-memo.md
    format: markdown
    ai_boundary: human-first
  - path: prompt-log.md
    format: markdown
    ai_boundary: human-first
prerequisites: [1]
points: 12
estimated_time: "3-4 hrs"
---

# Case 2 · Stage 2 — Analysis, Memo, Prompt Log

**Deliverable:** the analysis with figures, the recommendation memo, and an updated prompt log
**Submission:** committed and pushed to your public repository; graded by inspection
**Estimated time:** 3–4 hours

---

## 1. Purpose

Stage 1 built the machine; this stage says what it means. Your model shows the same company earning
$106.0M in one market and $8.785B in the other, from the same crop and the same fixed costs. The
analysis explains why, puts a dollar figure on what society pays for it, and takes a position on
whether that price is worth paying. The memo turns the position into advice somebody could act on.

## 2. Prerequisites

- Stage 1: `docs/briefs/imperfect-competition-brief.md` — the hypothesis you are now testing.
- Stage 1: `skills/pricing-power/model.xlsx` — the evidence source. Every number you cite comes from it.

Read before starting:

- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) — the memo structure and the prompt-log format.

## 3. Deliverables

| Artifact | Path | Format |
|---|---|---|
| The evidence — what the model shows and why, for someone checking your work | `analysis/imperfect-competition-analysis.md` | markdown |
| At least two figures the analysis refers to | `analysis/figures/` | images |
| The answer — what a decision-maker should do about it | `docs/decisions/imperfect-competition-memo.md` | markdown |
| The curated record of AI sessions, plus the reflection | `prompt-log.md` | markdown |

**Briefs ask; specs define; memos answer.**

## 4. Background

Five things the analysis has to cover, and what strong coverage looks like.

**Why MR < P for the price maker, and MR = P for the price taker.** The twice-as-steep rule for
linear demand, stated mechanically: one more bag sold lowers the price on *every* bag, so marginal
revenue falls at twice the slope of demand. The price taker's extra bag changes nothing, so
MR = P = $120.

**Why P\* comes off demand, not MR.** MR = MC picks the *quantity* — 34,025,974 bags. Demand tells
you the *price* buyers will pay for that quantity — $297.03. Explain it as if to a classmate who
just priced at $69.05.

**What markup and the Lerner index measure.** 4.30× and 0.768 as gauges of market power: price at
4.3 times marginal cost, roughly 77% of the price being margin over cost. Contrast the non-GMO row
at 1.0× and 0.

**What the deadweight loss means.** Roughly **$2.99B a year**, and not a transfer — surplus that
simply vanishes. The monopoly withholds about 26M bags to hold price at $297, and the competitive
benchmark price is about **$121.46**, almost exactly the $120 non-GMO price. Strip the patent and
GMO seed is just seed. That near-coincidence is the case's best result and the one most students
walk past.

**Whether the patent's innovation incentive justifies it.** A position, defended, engaging the
discussion spine: complement lock-in, where the herbicide sells the seed and the seed sells the
herbicide; patent enforcement, which is what *keeps* demand downward-sloping, because without it
farmers' saved seed is competing supply; glyphosate-resistant weeds as a negative externality the
private optimum ignores; and the 2018 acquisition, where the price of approval was the largest
negotiated merger divestiture in U.S. history. Either side is defensible. A fence-sit is not.

## 5. Procedure

1. **Write the analysis** at `analysis/imperfect-competition-analysis.md`, covering all five
   questions above from your own model's numbers, in whatever structure reads best.
   *Confirm:* each claim points at a cell or a figure in your model rather than at the case README.

2. **Export at least two figures** into `analysis/figures/` and reference each in the text. The
   D/MR/MC chart is the obvious first; a profit or decision-table figure is a natural second.
   *Confirm:* the images render on the github.com page, not only in your editor.

3. **Open with your hypothesis and a verdict.** Reproduce the hypothesis from your Stage 1 brief
   unedited, then one or two sentences on where it landed against the model and what you misjudged.
   *Confirm:* the hypothesis text matches what was committed. A prediction that missed by ten times,
   with a sharp account of why, beats a lucky guess with no account.

4. **Write the memo** at `docs/decisions/imperfect-competition-memo.md`. Half a page, addressed to
   someone who has to act — a regulator weighing the patent, or an executive deciding what the
   pricing power is worth defending. The recommendation, the reasoning that drives it, the judgment
   call where the evidence ran out, and what would change your answer.
   *Confirm:* it recommends rather than summarizes.

5. **Update `prompt-log.md`** at the repository root — a dated section for this engagement, covering
   both stages. Sessions from Stage 1, including formula debugging and the generation session,
   belong here too.
   *Confirm:* it is a curated record, not a transcript dump.

6. **Write the reflection**, 300 words or fewer, including **one AI error you caught** — a wrong
   formula, a confidently wrong explanation, a price read off the wrong curve. If you genuinely
   caught none, say what you checked and how you would have known.
   *Confirm:* the verification is concrete. "The AI was great and made no mistakes" reads as not
   having looked.

7. **Update `skills/pricing-power/README.md`** so its "exercised in:" line points at the analysis and
   the memo as well as the brief.

8. **Commit at least twice** with descriptive messages.

## 6. AI use

| Artifact | Draft order |
|---|---|
| `analysis/imperfect-competition-analysis.md` | Human-first |
| `docs/decisions/imperfect-competition-memo.md` | Human-first |
| `prompt-log.md` and the reflection | Human-first |
| Figures | Exported from your own workbook — not generated |

**If the artifact is evidence of your judgment, you draft it first and AI reviews; if the artifact is
a means to the work rather than the work itself, AI may draft it and you verify.** The two working
loops are described in [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html).

**For this stage specifically:** AI may explain MR and MC mechanics and critique your reasoning; it
may not write the analysis, the memo, or the reflection. A useful line to hold: paste your *draft*
and ask the model to attack the argument. Do not paste the questions and ask for prose — the
reflection is where the difference shows, and so is the analysis, because a model that has not seen
your workbook writes about the textbook instead of your numbers.

## 7. Verification

- [ ] Hypothesis reproduced unedited at the top, with an honest verdict against the model
- [ ] Setup paragraph in your own words: why the firm is a price taker in one market and a price maker in the other, and what the patent has to do with it
- [ ] The twice-as-steep rule explained mechanically, not asserted
- [ ] P\*-off-demand explained well enough to fix someone who priced at $69.05
- [ ] Markup 4.30× and Lerner 0.768 interpreted as market power, not recited
- [ ] Deadweight loss framed as vanished surplus, with the ~$121.46 benchmark against the $120 non-GMO price
- [ ] The patent paragraph takes and defends a position using the discussion spine
- [ ] At least two figures in `analysis/figures/`, each referenced in the text
- [ ] Figures render on the GitHub page
- [ ] Memo written: recommendation, reasoning, the judgment call, what would change your answer
- [ ] `prompt-log.md` updated across both stages, with a reflection of 300 words or fewer
- [ ] The reflection names a concrete AI error caught, or the checks that cleared it
- [ ] `skills/pricing-power/README.md` "exercised in:" line updated
- [ ] At least two descriptive commits for this stage

## 8. Rubric (12 pts)

| Criterion | Pts | What distinguishes strong work |
|---|---|---|
| Hypothesis + setup | 3 | Hypothesis committed before the model work and left unedited; setup in your own words; honest verdict on the miss |
| Perfect versus imperfect mechanics | 3 | Twice-as-steep rule stated correctly; P\*-off-demand explained rather than asserted; markup and Lerner interpreted as market power |
| Deadweight loss + the patent tradeoff | 3 | The ~$2.99B a year framed as vanished surplus; the ~$121 against $120 benchmark landed; the patent paragraph takes and defends a position using the spine |
| Prompt log + reflection | 3 | Complete log across both stages; reflection of 300 words or fewer, specific, including a genuinely caught AI error or the checks that cleared it |

The memo carries no separate points. It is read together with the analysis under the deadweight-loss
and patent-tradeoff criterion, which already asks what a decision-maker should conclude. What changes
is where that conclusion lives, and that it is written to a person rather than to a rubric.

## 9. Common failure modes

| What goes wrong | The correction |
|---|---|
| Q1 and Q2 restate definitions | The test: would your paragraph fix somebody who priced at MR = MC? If not, it is a definition, not an explanation |
| The hypothesis was edited after the model ran | The commit history shows it, and the verdict becomes worthless. A wrong hypothesis costs nothing; a rewritten one costs the criterion |
| The patent paragraph concludes "there are arguments on both sides" | That is the one answer that earns nothing. The paragraph exists to make you weigh vanished surplus against the incentive that produced the trait at all |
| Deadweight loss is described as a transfer to the firm | It is neither consumer surplus nor profit — it is the surplus from trades that never happen. The firm does not receive it |
| The memo summarizes the analysis | A memo recommends. If it restates findings, the two documents have swapped jobs |
| Outside statistics appear without a source | Cite them or drop them. The case README's figures are already sourced |
| The prompt log is reconstructed at the end | It produces generic mush a reader can smell. Two lines per session, written at the time |

## 10. References

- [Case README](README.md) — check figures, discussion spine, validated facts and sources
- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) — the memo structure and prompt-log format
- [Econ Policy Lab](https://adamwstauffer.github.io/ai-lms/econlab.html) — surplus and deadweight-loss geometry, interactively
- [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html) · [Portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html)
- [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics), including [how work is submitted, with the post-deadline revision policy](https://adamwstauffer.github.io/ai-lms/onboarding.html#submitting)
