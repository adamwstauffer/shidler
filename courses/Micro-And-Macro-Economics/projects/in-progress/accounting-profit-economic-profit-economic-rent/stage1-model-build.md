---
template: stage-brief
project: accounting-profit-economic-profit-economic-rent
stage: 1
title: "Brief, Spec, Build, Audit"
capability: economic-profit
deliverables:
  - path: docs/briefs/economic-profit-brief.md
    format: markdown
    ai_boundary: human-first
  - path: skills/economic-profit/spec.md
    format: markdown
    ai_boundary: human-first
  - path: skills/economic-profit/model.xlsx
    format: xlsx
    ai_boundary: ai-first-verified
  - path: skills/economic-profit/README.md
    format: markdown
    ai_boundary: human-first
prerequisites: []
points: 8
estimated_time: "3-4 hrs"
---

# Case 3 · Stage 1 — Brief, Spec, Build, Audit

**Deliverable:** the engagement brief, then `skills/economic-profit/spec.md`, `model.xlsx`, and `README.md`
**Submission:** committed and pushed to your public repository; graded by inspection
**Estimated time:** 3–4 hours

---

## 1. Purpose

Four people in one city, one question: who is actually making money? This stage produces the model
that can answer it — a brief with a hypothesis you can be wrong about, a specification precise
enough to build from, the workbook an AI builds from it, and your audit of what came back. What the
verdicts *mean*, and where the money actually went, is Stage 2.

## 2. Prerequisites

Your portfolio repository already exists. This engagement adds one capability folder:
`skills/economic-profit/`.

Read before starting:

- The [case README](README.md) — the four workers' figures, the medallion parameters, the check
  figures, and the sources. These are the facts your spec encodes. Do not invent numbers.
- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) — the brief and the spec.
- [AI Tools Lab](https://adamwstauffer.github.io/ai-lms/ailab.html#spec-to-artifact) — handing a spec to an AI tool.

## 3. Deliverables

| Artifact | Path | Format |
|---|---|---|
| The engagement brief, with a hypothesis committed before any modeling | `docs/briefs/economic-profit-brief.md` | markdown |
| The specification, written before the workbook exists, with audit findings appended | `skills/economic-profit/spec.md` | markdown |
| The workbook that satisfies it | `skills/economic-profit/model.xlsx` | xlsx |
| What the capability is, and where it was exercised | `skills/economic-profit/README.md` | markdown |

## 4. Background

A full-time app driver, a part-time app driver, a full-time yellow-cab driver, and an office worker
each get a full profit-and-loss statement: gross earnings down to **accounting profit**, and then
past it to **economic profit** by charging each person what their next-best alternative would have
paid them. The verdicts flip. A healthy $50,520 of accounting profit turns *negative* once the
forgone office job is counted.

Then the second question: if the drivers are not making economic profit, where did the money go? The
answer is bolted to the hood of the yellow cab. The **medallion** is a factor in fixed supply, the
lease payment is **economic rent**, and an asset earning rent indefinitely is worth
`rent ÷ required return`. One division reproduces both the peak price and the collapse.

Three specification failures produce three recognizable defects here, and each maps to a check your
audit has to run.

**Opportunity cost is the alternative's *net* earnings, not its gross.** The office job pays $57,600
gross and $52,200 after its own costs. Charging the driver $57,600 compares gross to net and
overstates every implicit cost in the model. The previous version of this course's template shipped
with exactly that error.

**Opportunity cost has to match scale.** A part-time driver forgoes a *part-time* alternative —
$26,100, not $52,200. Specify "the traditional job's earnings" without qualification and a model will
charge the part-timer a full-time opportunity cost, which makes the part-timer look far worse than
they are for a reason that is arithmetic rather than economic.

**Capitalization has two moving parts.** Between the two eras the annual rent falls *and* the
required return rises, because the income stream got riskier as well as smaller. A specification that
changes only the rent reproduces neither observed price. Both inputs belong in the named contract.

One structural requirement: the **days-per-month** figure is an explicit named input, not a constant
buried inside formulas. The whole sensitivity exercise depends on being able to change it.

### Check figures — your acceptance criteria

| | Uber FT | Uber PT | Yellow Cab FT | Traditional job |
|---|---|---|---|---|
| **Accounting profit** | **$50,520** | **$22,860** | **$59,580** | **$52,200** |
| **Economic profit** | **−$1,680** | **−$3,240** | **+$7,380** | **+$1,680** |

| Medallion | Pre-entry | Post-entry |
|---|---|---|
| Lease | $36,000/yr | $18,000/yr |
| Required return | 3.5% | 6.0% |
| **Capitalized value** | **$1,028,571** | **$300,000** |
| Observed price | >$1M peak | ≈$335K |

Write these into the spec as acceptance criteria before the build. They are the test suite, not the
answer you are graded on.

## 5. Procedure

### Brief

1. **Write `docs/briefs/economic-profit-brief.md` first.** The four-person setup in your own words,
   and a hypothesis: *"I expect X to have the highest economic profit because Y."* Name the person and
   the mechanism.
   *Confirm:* committed before any spec or model work. The commit timestamp is what makes it a
   hypothesis rather than a summary.

### Specify

2. **Write `skills/economic-profit/spec.md`** before opening Excel: named inputs with units and
   sources, structure for both sheets, calculation logic in named-range notation, validation rules,
   and outputs.
   *Confirm:* the spec states the net-to-net rule, the scale-matching rule, days-per-month as an
   input, and both capitalization inputs as separate named values per era.

3. **Commit the spec before generating anything.**
   *Confirm:* the commit order is brief, then spec, then workbook.

### Generate

4. **Hand the spec to an AI tool as-is** — chat, a CLI agent, or Claude for Excel. A manual build is
   permitted; the contract is graded, not the tool.
   *Confirm:* you did not re-explain the model in chat. If you did, that explanation belongs in the
   spec — add it, commit, regenerate.

### Audit

5. **Run your validation rules and record the findings** at the end of `spec.md`: what you checked,
   what you found, what you did. At minimum, these four:
   - **The check figures** — all eight profit numbers and both medallion values.
   - **A hand calculation of one opportunity cost.** Take the part-time driver's implicit cost and
     compute it yourself from the traditional job's *net* earnings, halved. If the workbook says
     $52,200 or $28,800, the spec's net-to-net or scale rule did not survive the build.
   - **The two capitalization inputs.** Confirm that the rent *and* the required return both differ
     between eras, and that the value is `rent ÷ required return` rather than a hard-coded number.
   - **Formulas, not pasted values**, referencing your named inputs; no error cells.

   *Confirm:* each check names what it would have caught.

6. **Run the sensitivity and document it.** Change days per month from 30 to 22, record what happens
   to each worker's economic profit, then restore the input before your final commit.
   *Confirm:* the numbers moved, which means the input is genuinely wired through rather than
   duplicated as a constant somewhere.

7. **Write `skills/economic-profit/README.md`** — what the capability is, plus an "exercised in:" line
   pointing at this engagement's brief, and after Stage 2 its analysis and memo.

8. **Commit at least twice** with descriptive messages.

## 6. AI use

| Artifact | Draft order |
|---|---|
| `docs/briefs/economic-profit-brief.md` | Human-first |
| `skills/economic-profit/spec.md` | Human-first |
| `skills/economic-profit/model.xlsx` | AI-first, verified |
| `skills/economic-profit/README.md` | Human-first |

**If the artifact is evidence of your judgment, you draft it first and AI reviews; if the artifact is
a means to the work rather than the work itself, AI may draft it and you verify.** The two working
loops are described in [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html).

**For this stage specifically:** AI may explain the profit concepts, quiz you, critique your
reasoning, and debug what it built. It may not write your brief, and it may not hand you the verdicts
before your hypothesis is committed. Asking "walk me through why opportunity cost uses net earnings"
is exactly right; asking "which of the four has the highest economic profit?" before the brief exists
defeats the stage.

## 7. Verification

- [ ] `docs/briefs/economic-profit-brief.md` committed **before** any spec or model work
- [ ] The brief names a person and a mechanism, not a hedge
- [ ] `spec.md` committed before the workbook
- [ ] Opportunity cost specified as the alternative's **net** earnings, never gross
- [ ] Opportunity cost **scale-matched** — the part-timer forgoes a part-time alternative
- [ ] Days per month is a named input, not a constant inside formulas
- [ ] Both capitalization inputs — rent and required return — named separately for each era
- [ ] Check figures written into the spec as acceptance criteria before the build
- [ ] All four accounting profits match: $50,520 · $22,860 · $59,580 · $52,200
- [ ] All four economic profits match: −$1,680 · −$3,240 · +$7,380 · +$1,680
- [ ] Medallion values match: $1,028,571 and $300,000, each as rent ÷ required return
- [ ] Hand calculation of one opportunity cost confirms the net-to-net and scale rules survived the build
- [ ] Sensitivity run documented: 30 → 22 days per month, verdicts recorded, input restored
- [ ] Calculated cells contain formulas referencing named inputs; no `#REF!`, `#DIV/0!`, `#NAME?`
- [ ] Audit findings recorded in `spec.md` — at least three checks, each naming what it would have caught
- [ ] `README.md` in the capability folder, with an "exercised in:" line
- [ ] At least two descriptive commits for this stage

## 8. Rubric (8 pts)

| Criterion | Pts | What distinguishes strong work |
|---|---|---|
| Spec completeness — inputs, structure, calculation flow | 3 | Both sheets specified; the net-to-net rule and the scale-matching rule stated explicitly rather than implied; days per month as a named input; both capitalization inputs named per era |
| Spec validation rules | 1 | Check figures written in as acceptance criteria before the build, alongside the hand calculation of an opportunity cost and the structural rules |
| Workbook satisfies the contract | 2 | All eight profit figures and both medallion values reproduce; capitalization computed as rent ÷ required return rather than hard-coded; sensitivity run documented with the input restored; no error cells |
| Audit note | 1 | At least three concrete checks run, each named with what it would have caught, and any defects found documented with the fix |
| Brief before the build, and commit hygiene | 1 | The brief's commit predates every spec and model commit; at least two descriptive commits |

## 9. Common failure modes

| What goes wrong | The correction |
|---|---|
| Implicit costs use the office job's $57,600 | That is its gross. Opportunity cost is what the alternative pays *after its own costs* — $52,200. Comparing gross to net overstates every implicit cost in the model |
| The part-timer is charged $52,200 | Scale mismatch. A part-time driver forgoes a part-time alternative — $26,100 |
| Both medallion values come from the same required return | The stream got riskier as well as smaller. Rent falls from $36,000 to $18,000 *and* the required return rises from 3.5% to 6.0%. Change one and neither observed price is reproduced |
| The medallion values are typed in | Capitalization is a division the model performs, not a fact it stores. If the rent changes, the value must move |
| Changing days per month does nothing | The figure is hard-coded somewhere inside the formulas. Fix the spec, commit, regenerate |
| The sensitivity run is left in the workbook | Record the result, then restore the input to 30 before the final commit |

## 10. References

- [Case README](README.md) — the four workers' figures, medallion parameters, check figures, sources
- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) · [AI Tools Lab](https://adamwstauffer.github.io/ai-lms/ailab.html#spec-to-artifact)
- [Portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html) · [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html)
- [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics), including [how work is submitted, with the post-deadline revision policy](https://adamwstauffer.github.io/ai-lms/onboarding.html#submitting)
