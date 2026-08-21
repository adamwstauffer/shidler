---
template: stage-brief
project: accounting-profit-economic-profit-economic-rent
stage: 2
title: "Analysis, Memo, Prompt Log"
capability: economic-profit
deliverables:
  - path: analysis/economic-profit-analysis.md
    format: markdown
    ai_boundary: human-first
  - path: analysis/figures/
    format: images
    ai_boundary: not-permitted
  - path: docs/decisions/economic-profit-memo.md
    format: markdown
    ai_boundary: human-first
  - path: prompt-log.md
    format: markdown
    ai_boundary: human-first
prerequisites: [1]
points: 12
estimated_time: "3-4 hrs"
---

# Case 3 · Stage 2 — Analysis, Memo, Prompt Log

**Deliverable:** the analysis with figures, the recommendation memo, and an updated prompt log
**Submission:** committed and pushed to your public repository; graded by inspection
**Estimated time:** 3–4 hours

---

## 1. Purpose

Stage 1 established who is making money. This stage explains why the verdicts land where they do,
follows the money to the asset that was capturing it, and shows what happened when entry arrived.
Then it recommends something to somebody who has to act.

## 2. Prerequisites

- Stage 1: `docs/briefs/economic-profit-brief.md` — the hypothesis you are now testing.
- Stage 1: `capabilities/economic-profit/model.xlsx` — the evidence source, including your documented
  sensitivity run.

Read before starting:

- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) — the memo structure and the prompt-log format.

## 3. Deliverables

| Artifact | Path | Format |
|---|---|---|
| The evidence — what the model shows and why, for someone checking your work | `analysis/economic-profit-analysis.md` | markdown |
| At least two figures the analysis refers to | `analysis/figures/` | images |
| The answer — what a decision-maker should do about it | `docs/decisions/economic-profit-memo.md` | markdown |
| The curated record of AI sessions, plus the reflection | `prompt-log.md` | markdown |

**Briefs ask; specs define; memos answer.**

## 4. Background

Five things the analysis has to establish.

**The four verdicts, by mechanism.** Not a restatement of the table — an explanation. The part-timer
is hit hardest because the car's costs do not scale: full payment and insurance sit on half the
revenue. The office worker turns out to have positive economic profit, which is the same statement in
reverse. And the cab driver "wins" at the driver level while handing $36,000 a year to somebody who
never drives.

**Net-to-net discipline.** Show that you understand why opportunity cost uses the alternative's *net*
earnings — $52,200, not the $57,600 gross — and why a part-timer forgoes a part-time alternative.
If your Stage 1 figures matched the check figures you already applied this; here you articulate it.

**Where the money went.** The cab driver's lease is the hook. The medallion is a factor in fixed
supply — 13,587 of them — so the payment is **economic rent**, and an asset earning rent indefinitely
is worth `rent ÷ required return`. $36,000 ÷ 3.5% = $1,028,571 against an observed peak above $1M.
$18,000 ÷ 6.0% = $300,000 against roughly $335,000 observed. One division, both eras, within about
10% each time.

**Why the rent collapsed.** App vehicles went from about 40,000 to more than 120,000. Fares fell,
so the lease fell; the income stream also got riskier, so the required return rose. Both moves shrink
the same fraction, which is why the asset lost 70–85% of its value. The medallion cap blocked entry
into *yellow cabs* — it never blocked entry into *rides*. Rent survives only as long as the moat
actually surrounds the market. Be honest about the second cause too: predatory medallion lending
inflated the peak, so entry was not the only villain.

**Supply and demand, and the cross-case link.** Supply shifted right, massively; demand also shifted
right, but the supply shock dominates — price down, quantity up, consumers better off, incumbent
rent-holders worse off. Then connect it: the medallion's rent behind a moat is the seed patent in
miniature. Same moat → rent → entry logic, a different legal wrapper.

## 5. Procedure

1. **Write the analysis** at `analysis/economic-profit-analysis.md`, covering the five things above
   from your own model's numbers.
   *Confirm:* each claim points at a cell or a figure in your model rather than at the case README.

2. **Open with your hypothesis and a verdict.** Reproduce the Stage 1 hypothesis unedited, then one
   or two sentences on where it landed and what you misjudged.
   *Confirm:* the text matches what was committed. Wrong but well-reasoned scores as well as right.

3. **Use the sensitivity run.** Your 30 → 22 days-per-month result is the gig-economy fragility point
   in one number: every driver verdict goes deep negative one input away from the base case.
   *Confirm:* the numbers in the analysis come from your run, not from the case notes.

4. **Export at least two figures** into `analysis/figures/` and reference each in the text. Natural
   candidates: accounting against economic profit across the four workers; the medallion's capitalized
   value against observed prices in both eras; the sensitivity result.
   *Confirm:* the figures render on the github.com page, and each carries analytical weight — a
   screenshot of the raw sheet is not a figure.

5. **Write the memo** at `docs/decisions/economic-profit-memo.md`. Half a page to somebody who has to
   act — a regulator deciding whether to cap app vehicles, a lender deciding what a medallion is worth
   as collateral, or a driver deciding whether to lease one. Recommendation, the reasoning that drives
   it, the judgment call where the evidence ran out, and what would change your answer.
   *Confirm:* it recommends rather than summarizes.

6. **Update `prompt-log.md`** at the repository root — a dated section covering both stages,
   including the generation session — and close with a reflection of 300 words or fewer naming **one
   AI error you caught** and how you verified it. Economic versus normal profit is a reliable place
   for a model to stumble.
   *Confirm:* the verification is concrete.

7. **Update `capabilities/economic-profit/README.md`** so its "exercised in:" line points at the analysis
   and the memo as well as the brief.

8. **Commit at least twice** with descriptive messages.

## 6. AI use

| Artifact | Draft order |
|---|---|
| `analysis/economic-profit-analysis.md` | Human-first |
| `docs/decisions/economic-profit-memo.md` | Human-first |
| `prompt-log.md` and the reflection | Human-first |
| Figures | Exported from your own workbook — not generated |

**If the artifact is evidence of your judgment, you draft it first and AI reviews; if the artifact is
a means to the work rather than the work itself, AI may draft it and you verify.** The two working
loops are described in [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html).

**For this stage specifically:** AI may explain the profit concepts and attack your draft argument;
it may not write the analysis, the memo, or the reflection. Paste your draft and ask it to find the
weakest claim — that is the use that improves the work.

## 7. Verification

- [ ] Hypothesis reproduced unedited at the top, with an honest verdict against the model
- [ ] The four verdicts explained by mechanism — the part-timer's non-scaling car costs named explicitly
- [ ] Net-to-net discipline articulated: why $52,200 and not $57,600, and why the part-timer's alternative is halved
- [ ] The medallion story told **with** the capitalization arithmetic, both eras
- [ ] Both capitalized values tied to their observed prices, and the ~10% agreement noted
- [ ] The collapse explained by both moves — lease down *and* required return up — plus the honest note that lending inflated the peak
- [ ] The moat point landed: the cap blocked entry into yellow cabs, never into rides
- [ ] Supply and demand: correct curve, correct direction, price, quantity, and whose surplus
- [ ] Cross-case link drawn on the moat → rent → entry logic, not name-dropped
- [ ] The 30 → 22 sensitivity used as the fragility argument, with your own numbers
- [ ] At least two figures in `analysis/figures/`, each referenced and analytically load-bearing
- [ ] Figures render on the GitHub page
- [ ] Memo written: recommendation, reasoning, the judgment call, what would change your answer
- [ ] `prompt-log.md` updated across both stages, with a reflection of 300 words or fewer
- [ ] The reflection names a concrete AI error caught, or the checks that cleared it
- [ ] `capabilities/economic-profit/README.md` "exercised in:" line updated
- [ ] At least two descriptive commits for this stage

## 8. Rubric (12 pts)

| Criterion | Pts | What distinguishes strong work |
|---|---|---|
| Hypothesis + setup | 3 | Hypothesis committed before the model work and left unedited; honest revisit — wrong but well-reasoned scores as well as right |
| The four verdicts | 2 | Mechanism, not restatement — the part-timer's non-scaling car costs and the net-to-net discipline explicitly articulated |
| Medallion story with the math | 2 | Capitalization arithmetic drives the narrative; entry → lease down → riskier perpetuity → 70–85% collapse, tied to observed prices |
| Supply/demand + cross-case link | 2 | Correct curve and direction; price, quantity, and surplus all addressed; the pricing-power parallel drawn on the moat → rent → entry logic rather than name-dropped |
| Figures | — | At least two, analytically load-bearing — graded within the rows above; a missing or decorative figure costs the row it should have served |
| Prompt log + reflection | 3 | Sessions logged with substance; reflection of 300 words or fewer centered on a concrete AI error caught and how it was verified |

The memo carries no separate points. It is read together with the analysis under the medallion and
supply/demand criteria, which already ask what somebody should conclude. What changes is where that
conclusion lives, and that it is written to a person rather than to a rubric.

## 9. Common failure modes

| What goes wrong | The correction |
|---|---|
| The verdicts are restated rather than explained | Name the mechanism. "The part-timer earns less" is the table; "the car's fixed costs sit on half the revenue" is the analysis |
| The medallion section tells the story without the arithmetic | The capitalization is the story. Rent ÷ required return, both eras, against the observed prices |
| The collapse is attributed to entry alone | Two things moved: the rent fell and the required return rose. And lending practices inflated the peak — say so |
| "The cap protected the taxi industry" | It protected entry into *yellow cabs*. Rides were never capped, which is exactly why the rent evaporated |
| The cross-case link is a sentence naming the other case | Draw the logic: a legal moat creates rent, rent capitalizes into an asset price, entry that bypasses the moat destroys both |
| Figures are decorative | A figure earns its place by carrying evidence the text uses. Here it costs the rubric row it should have served |
| The reflection claims the AI made no mistakes | Without evidence of checking, that reads as not having looked |

## 10. References

- [Case README](README.md) — check figures, industry prompts, validated facts and sources
- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) — the memo structure and prompt-log format
- [Econ Policy Lab](https://adamwstauffer.github.io/ai-lms/econlab.html) — surplus areas, for the supply-and-demand section
- [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html) · [Portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html)
- [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics), including [how work is submitted, with the post-deadline revision policy](https://adamwstauffer.github.io/ai-lms/onboarding.html#submitting)
