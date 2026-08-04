---
template: stage-brief
project: imperfect-competition-marginal-revenue
stage: 1
title: "Brief, Spec, Build, Audit"
capability: pricing-power
deliverables:
  - path: docs/briefs/imperfect-competition-brief.md
    format: markdown
    ai_boundary: human-first
  - path: skills/pricing-power/spec.md
    format: markdown
    ai_boundary: human-first
  - path: skills/pricing-power/model.xlsx
    format: xlsx
    ai_boundary: ai-first-verified
  - path: skills/pricing-power/README.md
    format: markdown
    ai_boundary: human-first
prerequisites: []
points: 8
estimated_time: "3-4 hrs"
---

# Case 2 · Stage 1 — Brief, Spec, Build, Audit

**Deliverable:** the engagement brief, then `skills/pricing-power/spec.md`, `model.xlsx`, and `README.md`
**Submission:** committed and pushed to your public repository; graded by inspection
**Estimated time:** 3–4 hours

---

## 1. Purpose

One company, two market structures. This stage produces a model of both: a brief stating the
question and a hypothesis you can be wrong about, a specification precise enough to build from, the
workbook an AI builds from it, and your audit of what came back. What the numbers *mean* is Stage 2.

## 2. Prerequisites

Your portfolio repository already exists — it was stood up in Case 1, and this engagement adds to it
rather than restarting it. The capability folder is new: `skills/pricing-power/`.

Read before starting:

- The [case README](README.md) — the two-market setup, the parameterization, the check figures, and
  the sources. These are the facts your spec encodes. Do not invent numbers.
- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) — the brief and the spec.
- [AI Tools Lab](https://adamwstauffer.github.io/ai-lms/ailab.html#spec-to-artifact) — handing a spec to an AI tool.

## 3. Deliverables

| Artifact | Path | Format |
|---|---|---|
| The engagement brief, with a hypothesis committed before any modeling | `docs/briefs/imperfect-competition-brief.md` | markdown |
| The specification, written before the workbook exists, with audit findings appended | `skills/pricing-power/spec.md` | markdown |
| The workbook that satisfies it | `skills/pricing-power/model.xlsx` | xlsx |
| What the capability is, and where it was exercised | `skills/pricing-power/README.md` | markdown |

## 4. Background

Selling **commodity non-GMO corn seed**, the seed company is a price taker at $120 a bag: it produces
until **P = MC**, and free entry will erode the profit. Selling **the patented herbicide-tolerant GMO
seed**, the same firm faces the whole market's downward-sloping demand. One more bag sold lowers the price on
*every* bag, so marginal revenue falls at twice the slope of demand, and the rule becomes
**MR = MC**. Same crop, same $130M of fixed costs — and roughly an 83-fold difference in profit.

Both markets share the cost structure `TVC = a·Q + b·Q²`, so `MC = a + 2b·Q` with a = $1 per bag.
Non-GMO demand is flat at $120 with curvature b = 0.000015; GMO demand is
`P = 525 − 0.0000067·Q` with b = 0.000001, and `MR = 525 − 0.0000134·Q`.

Three things about that structure are where specifications go wrong, and each maps to a defect your
audit has to be able to catch:

**Variable cost is the area under marginal cost**, `aQ + bQ²` — not MC × Q. Specifying it as MC × Q
forces the non-GMO profit to exactly −$130M, because average cost then equals marginal cost and
profit collapses to minus fixed costs. That is an artifact, not economics, and the previous version
of this course's workbook shipped with exactly that bug.

**Price comes off the demand curve, never off marginal revenue.** MR = MC picks the *quantity*;
demand tells you the *price* buyers will pay for that quantity. A specification that is vague about
which curve supplies the price produces a model that prices at about $69 instead of $297 — the most
common error in this case, and one a generated workbook will make confidently.

**MR is a separate series from demand, with twice the slope.** A specification that describes "the
demand curve" without separately defining marginal revenue will produce a model where MR = P — which
is a model of Case 1, not of this one.

### Check figures — your acceptance criteria

| Figure | Non-GMO (price taker) | GMO (patent monopoly) |
|---|---|---|
| Q\* | **3,966,667 bags** | **34,025,974 bags** |
| P\* | $120 (given) | **$297.03** — off demand, not MR |
| Profit | **$106.0M** | **$8.785B** |
| Markup P/MC | 1.0× | **4.30×** (Lerner **0.768**) |

Write these into the spec as acceptance criteria before the build. They are the test suite, not the
answer you are graded on.

## 5. Procedure

### Brief

1. **Write `docs/briefs/imperfect-competition-brief.md` first**, before anything else. The two-market
   setup in your own words, and a hypothesis: *"I expect the GMO price and profit to be X because
   Y."* Real numbers and a mechanism.
   *Confirm:* the brief is committed before any spec or model work. The commit timestamp is what
   makes it a hypothesis rather than a summary, and it cannot be reconstructed later.

### Specify

2. **Write `skills/pricing-power/spec.md`** before opening Excel: named inputs with units and
   sources, structure, calculation logic in named-range notation, validation rules including the
   check figures above, and outputs. Both markets, side by side.
   *Confirm:* the spec defines demand and marginal revenue as separate series, states variable cost
   as the area under MC, and says explicitly which curve the price is read from.

3. **Commit the spec before generating anything.**
   *Confirm:* the commit order is brief, then spec, then workbook.

### Generate

4. **Hand the spec to an AI tool as-is** — chat, a CLI agent, or Claude for Excel. A manual build is
   permitted; the contract is graded, not the tool.
   *Confirm:* you did not re-explain the model in the chat. If you did, that explanation belongs in
   the spec — add it, commit, regenerate.

### Audit

5. **Run your validation rules and record the findings** at the end of `spec.md`: what you checked,
   what you found, what you did. At minimum, these four:
   - **The check figures**, both markets.
   - **A hand check at small Q.** Compute total variable cost at Q = 1,000,000 bags by hand from
     `aQ + bQ²` and compare it to the workbook. This is the check that catches VC = MC × Q, and it
     catches it in one line.
   - **The MR-versus-price structural check.** On the GMO sheet, MR must be strictly below price at
     every positive quantity. If MR = P anywhere, the model has rebuilt Case 1 — a price taker — and
     every downstream number is wrong.
   - **Formulas, not pasted values**, referencing your named inputs; no error cells.

   *Confirm:* each check names what it would have caught.

6. **Cross-check the welfare geometry.** Where the model computes the competitive benchmark and the
   deadweight loss, the [Econ Policy Lab](https://adamwstauffer.github.io/ai-lms/econlab.html) shows
   the same surplus areas interactively. Use it to confirm the shape of what your workbook reports
   before you trust the number.
   *Confirm:* you can point at the triangle your model is measuring.

7. **Write `skills/pricing-power/README.md`** — what the capability is, plus an "exercised in:" line
   pointing at this engagement's brief, and after Stage 2 its analysis and memo.

8. **Commit at least twice** with descriptive messages.

## 6. AI use

| Artifact | Draft order |
|---|---|
| `docs/briefs/imperfect-competition-brief.md` | Human-first |
| `skills/pricing-power/spec.md` | Human-first |
| `skills/pricing-power/model.xlsx` | AI-first, verified |
| `skills/pricing-power/README.md` | Human-first |

**If the artifact is evidence of your judgment, you draft it first and AI reviews; if the artifact is
a means to the work rather than the work itself, AI may draft it and you verify.** The two working
loops are described in [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html).

**For this stage specifically:** AI may explain MR and MC mechanics, critique your reasoning, and
debug what it built. It may not write your brief, and it may not hand you the optima before your
hypothesis is committed — asking a model "what is the profit-maximizing GMO quantity?" before the
brief exists defeats the stage. Asking it "why is my MR column falling twice as fast as my demand
column?" afterwards is exactly what it is for.

## 7. Verification

- [ ] `docs/briefs/imperfect-competition-brief.md` committed **before** any spec or model work
- [ ] The brief states the two-market setup in your own words and a hypothesis with real numbers and a mechanism
- [ ] `spec.md` committed before the workbook
- [ ] Demand and marginal revenue defined as **separate** series, MR with twice the slope
- [ ] Variable cost specified as the area under MC (`aQ + bQ²`), never MC × Q
- [ ] The spec states explicitly that price is read off demand, not off MR
- [ ] Check figures written into the spec as acceptance criteria before the build
- [ ] Both optima match: Q\* 3,966,667 and 34,025,974 bags; P\* $120 and $297.03; profit $106.0M and $8.785B
- [ ] Markup 4.30× and Lerner 0.768 reproduce
- [ ] Hand check at small Q confirms variable cost is the area under MC
- [ ] MR strictly below price at every positive quantity on the GMO sheet
- [ ] Decision tables complete for both markets and consistent with the optima
- [ ] D/MR/MC chart legible: MR twice as steep, the MR = MC crossing, and P\* up on demand
- [ ] Calculated cells contain formulas referencing named inputs; no `#REF!`, `#DIV/0!`, `#NAME?`
- [ ] Audit findings recorded in `spec.md` — at least three checks, each naming what it would have caught
- [ ] `README.md` in the capability folder, with an "exercised in:" line
- [ ] At least two descriptive commits for this stage

## 8. Rubric (8 pts)

| Criterion | Pts | What distinguishes strong work |
|---|---|---|
| Spec completeness — inputs, structure, calculation flow | 3 | Both markets specified; demand and MR as separate series with the twice-as-steep relationship stated; variable cost as the area under MC; the price-off-demand rule explicit rather than implied |
| Spec validation rules | 1 | Check figures written in as acceptance criteria before the build, alongside the small-Q hand check and the MR < P structural rule |
| Workbook satisfies the contract | 2 | Both optima correct — non-GMO via P = MC, GMO via MR = MC with P\* off demand; decision tables tracing to the marker rows; D/MR/MC chart legible; no error cells |
| Audit note | 1 | At least three concrete checks run, each named with what it would have caught, and any defects found documented with the fix |
| Brief before the build, and commit hygiene | 1 | The brief's commit predates every spec and model commit; at least two descriptive commits |

## 9. Common failure modes

| What goes wrong | The correction |
|---|---|
| P\* comes back around $69 | The model read the price off marginal revenue. MR picks the quantity; demand sets the price. Fix the spec's wording, commit, regenerate |
| Non-GMO profit is exactly −$130M | Variable cost was specified as MC × Q, so average cost equals marginal cost and profit collapses to minus fixed costs. It is the area under MC |
| MR and demand come back identical | The spec never defined MR as its own series. On linear demand it falls at twice the slope |
| The hypothesis is written after the model | There is no recovery — the commit history shows it, and Stage 2's verdict has nothing to compare against |
| The generated model matches the check figures but the formulas are pasted numbers | Matching figures with broken formulas fails inspection. The workbook is what is read, not the answer cell |
| The audit says "checked, correct" three times | A check is only worth recording if you can say what it would have caught |

## 10. References

- [Case README](README.md) — parameterization, check figures, discussion spine, sources
- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) · [AI Tools Lab](https://adamwstauffer.github.io/ai-lms/ailab.html#spec-to-artifact)
- [Econ Policy Lab](https://adamwstauffer.github.io/ai-lms/econlab.html) — surplus and deadweight-loss geometry, interactively
- [Portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html) · [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html)
- [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics), including [how work is submitted, with the post-deadline revision policy](https://adamwstauffer.github.io/ai-lms/onboarding.html#submitting)
