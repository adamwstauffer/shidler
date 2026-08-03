---
template: stage-brief
project: perfect-competition-marginal-costs
stage: 2
title: "Model Build"
capability: marginal-analysis
deliverables:
  - path: skills/marginal-analysis/model.xlsx
    format: xlsx
    ai_boundary: human-first
  - path: skills/marginal-analysis/spec.md
    format: markdown
    ai_boundary: human-first
  - path: skills/marginal-analysis/README.md
    format: markdown
    ai_boundary: human-first
prerequisites: [1]
points: 8
estimated_time: "3-4 hrs"
---

# Case 1 · Stage 2 — Model Build

**Deliverable:** `skills/marginal-analysis/model.xlsx`, `spec.md`, and `README.md`
**Submission:** committed and pushed to your public repository; graded by inspection
**Estimated time:** 3–4 hours

---

## 1. Purpose

This stage produces the model: the cost structure, each crop's marginal-cost schedule, the P = MC
read per crop, and a documented Solver run that finds the profit-maximizing mix under the real
constraints. It also produces the spec that makes the run reproducible by somebody else. Getting the
machinery right is the whole job here — *why* the answer looks the way it does is Stage 3.

## 2. Prerequisites

- Stage 1 complete: the repository exists, and `docs/briefs/perfect-competition-brief.md` is
  committed with your hypothesis in it, before this stage's work begins.
- `farm-profit-optimizer-template.xlsx`, in this folder, copied into your repository as
  `skills/marginal-analysis/model.xlsx`.

Read before starting:

- The [case README](README.md) — all scenario assumptions: prices, wages, bed caps, the labor
  function. Do not invent numbers; the workbook's blue input cells and the README's assumptions table
  are the same set.
- The template's own README sheet — the authoritative walkthrough of conventions, the color key, and
  the Solver steps.
- [The portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html) — why the spec and the model live together in the capability folder.

## 3. Deliverables

| Artifact | Path | Format |
|---|---|---|
| The completed workbook | `skills/marginal-analysis/model.xlsx` | xlsx |
| The model spec, including the documented Solver run | `skills/marginal-analysis/spec.md` | markdown |
| What the capability is, and where it was exercised | `skills/marginal-analysis/README.md` | markdown |

## 4. Background

`marginal-analysis` is a **capability** — take a decision with a rising cost curve and find where the
next unit stops paying for itself. It is not "the farm assignment." That is why the folder is named
for the method, and why the spec and the workbook sit in it together: a method and the model that
implements it are one object, and filing them apart creates structure with no payoff.

The farm is the **engagement** that exercises the capability, and its evidence lives elsewhere — the
brief in `docs/briefs/`, the analysis in `analysis/`. The capability's `README.md` is the join
between the two. The same structure carries into the later engagements, and it is what a reader
follows from a claim on your resume to the work that proves it.

Economically, this is the supply side of perfect competition made mechanical. The farm is a price
taker, every additional bed of a crop costs more labor than the last, and the question is where
rising marginal cost meets a flat price line.

## 5. Procedure

1. **Build the cost structure** — fixed costs, fertilizer per bed, and the labor function: hours for
   `q` beds = `q × hrs/wk/bed × 36 × (1 + dim%)^q`. The exponential term is the diminishing-returns
   engine.
   *Confirm:* test at `q = 1`. One bed of tomatoes should cost `1 × 2.5 × 36 × 1.10` hours. If your
   MC schedules come out flat, this is where it broke.

2. **Build the MC schedules** — bed-by-bed marginal cost for tomatoes, carrots, and mesclun on the
   MC Schedules sheet.
   *Confirm:* the MC-versus-price charts populate for all three crops.

3. **Read P = MC per crop** — find where each crop's standalone marginal cost crosses its price.
   *Confirm:* roughly **tomatoes ~10, carrots ~10, mesclun ~6 beds**. Note what tomato MC does around
   bed 6; you explain it in Stage 3.

4. **Run Solver** — objective: maximize profit. Changing cells: the three bed-count decisions.
   Method: **GRG Nonlinear** with **integer** decisions. Constraints exactly as listed on the
   workbook's README sheet — bed caps, 64 total beds, temp workers ≤ 4.
   *Confirm:* every constraint-check cell is green, and the run reproduces the check figures below.

5. **Write `spec.md`** — half a page, no more, covering three things:
   - **What the model computes and how** — the labor function, the permanent-then-temporary costing
     convention, the blended-rate allocation. Name the input cells and any named ranges you rely on.
   - **The Solver run, reproducibly** — objective cell, changing cells, every constraint, method, and
     the starting point you used. A Solver run that is not documented is not reproducible, and
     something unreproducible is not a model.
   - **How the model is validated** — which check figures you matched, and any hand calculation you
     used to prove a formula. The `q = 1` test is the classic.

   *Confirm:* somebody who has never seen your workbook could rerun the optimization from this file
   alone.

6. **Write `skills/marginal-analysis/README.md`** — three or four lines. What the capability is, and
   an "exercised in:" line pointing at this engagement's brief, and after Stage 3 its analysis and
   memo.
   *Confirm:* the links resolve on github.com, not just locally.

7. **Commit at least twice** with descriptive messages — one when the cost structure and MC schedules
   work, one after the documented Solver run. Not `update xlsx`.
   *Confirm:* if `~$model.xlsx` appears in your Changes panel, your `.gitignore` is broken; fix it
   before committing.

### Check figures — verify before submitting

The answers are published so you can self-verify. The grade is for the model that produces them, not
for the numbers.

| Check | Value |
|---|---|
| Optimal mix | Tomatoes **10** / Carrots **20** / Mesclun **30** (60 beds) |
| Season profit | **$42,762** |
| Standalone P ≈ MC points | Tomatoes ~10 · Carrots ~10 · Mesclun ~6 beds |

If Solver lands elsewhere, the model has a bug — trace it. Matching the numbers with broken formulas
will not survive inspection either; the rubric reads the workbook, not the answer cell.

**Companion oracle:** the interactive [Farm Profit Lab](https://adamwstauffer.github.io/ai-lms/farmlab.html)
is this same model made touchable. Drag the bed counts, watch MC cross price, sanity-check any
intermediate value. If your spreadsheet and the lab disagree, believe the lab and find your formula
error.

## 6. AI use

| Artifact | Draft order |
|---|---|
| `skills/marginal-analysis/model.xlsx` | Human-first |
| `skills/marginal-analysis/spec.md` | Human-first |
| `skills/marginal-analysis/README.md` | Human-first |

**If the artifact is evidence of your judgment, you draft it first and AI reviews; if the artifact is
a means to the work rather than the work itself, AI may draft it and you verify.** The two working
loops are described in [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html).

**For this stage specifically:** AI may explain concepts, critique your reasoning, and help debug
formulas — "why is my MR column falling twice as fast as my demand column?" is exactly what it is
for. Having AI hand you completed formulas you cannot explain is self-sabotage, because Stage 3
requires you to explain what every piece of this model does. Log the sessions that mattered; the
prompt log is graded in Stage 3, and this stage's debugging sessions are precisely what belongs in
it.

## 7. Verification

- [ ] Workbook committed to `skills/marginal-analysis/model.xlsx`
- [ ] Labor function verified by hand at `q = 1`
- [ ] MC schedules and charts populated for all three crops
- [ ] P ≈ MC located per crop and noted
- [ ] Solver run: GRG Nonlinear, integer decisions, every constraint entered
- [ ] All constraint-check cells green; no `#REF!`, `#DIV/0!`, or `#NAME?` anywhere
- [ ] Check figures matched: 10/20/30 beds, $42,762
- [ ] The MC dip located and noted for Stage 3 — do not explain it yet
- [ ] `spec.md` covers model logic, the full Solver run, and how you validated it
- [ ] `README.md` in the capability folder, with an "exercised in:" line
- [ ] No hardcoded overrides of formulas anywhere in the workbook
- [ ] At least two descriptive commits for this stage

## 8. Rubric (8 pts)

| Criterion | Pts | What distinguishes strong work |
|---|---|---|
| Cost structure + labor function correct | 2 | Blue inputs match the case assumptions; diminishing-returns exponent working; blended-wage convention followed |
| MC schedules + P = MC per crop | 2 | Bed-by-bed MC correct for all three crops; standalone crossings identified (~10/~10/~6); charts populated |
| Solver run correct + documented | 3 | GRG Nonlinear, integer decisions, all constraints from the README sheet; finds 10/20/30 at $42,762; objective, cells, constraints, method, and start point written down in `spec.md` |
| Workbook hygiene + commit hygiene | 1 | Checks green, no error cells, no hardcoded overrides of formulas; skill `README.md` present; at least two descriptive commits |

## 9. Common failure modes

| What goes wrong | The correction |
|---|---|
| MC schedules come out flat | The diminishing-returns exponent is missing or misapplied. Test the labor function at `q = 1` before anything else |
| Labor costs are wrong by a consistent margin | Permanent hours are consumed before any temporary hours, and the P&L allocates labor at the *blended* rate. Mixing the two conventions is the most common structural bug |
| Tomato MC falls around bed 6 and you "fix" it | The model is right — marginal cost is not guaranteed to be monotonic. Note it and explain it in Stage 3 |
| Solver lands on a different mix | Try two starting points. 0/0/0 finds the optimum; 20/0/0 may not, and that path-dependence is worth one sentence in the spec |
| The spec is written at the end | Every time you settle a convention, that is a line of `spec.md`. Reconstructing it afterwards is how details get lost |
| `~$model.xlsx` appears in Changes | `.gitignore` is missing, misnamed, or in the wrong folder |

## 10. References

- [Case README](README.md) — assumptions, constraints, instructor notes
- [Farm Profit Lab](https://adamwstauffer.github.io/ai-lms/farmlab.html) — the same model, interactive
- [Portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html) · [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html)
- [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics), including [how work is submitted, with the post-deadline revision policy](https://adamwstauffer.github.io/ai-lms/onboarding.html#submitting)
