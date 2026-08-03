---
template: stage-brief
project: perfect-competition-marginal-costs
stage: 2
title: "Spec, Build, Audit"
capability: marginal-analysis
deliverables:
  - path: skills/marginal-analysis/spec.md
    format: markdown
    ai_boundary: human-first
  - path: skills/marginal-analysis/model.xlsx
    format: xlsx
    ai_boundary: ai-first-verified
  - path: skills/marginal-analysis/README.md
    format: markdown
    ai_boundary: human-first
prerequisites: [1]
points: 8
estimated_time: "3-4 hrs"
---

# Case 1 · Stage 2 — Spec, Build, Audit

**Deliverable:** `skills/marginal-analysis/spec.md`, `model.xlsx`, and `README.md`
**Submission:** committed and pushed to your public repository; graded by inspection
**Estimated time:** 3–4 hours

---

## 1. Purpose

This stage produces a working model of the farm's decision — and it produces it in the order a
working analyst does. You write the **specification first**, before the workbook exists: every input
with a name and a unit, the calculation logic, and the validation rules the finished model must
pass. Then you hand that specification to an AI tool and it builds the workbook. Then you **audit**
what came back against the rules you wrote.

There is no starter workbook to fill in. Your spec is the template.

## 2. Prerequisites

- Stage 1 complete: the repository exists, and `docs/briefs/perfect-competition-brief.md` is
  committed with your hypothesis in it.

Read before starting:

- The [case README](README.md) — every scenario assumption: prices, wages, bed caps, the labor
  function, the constraints. These are the facts your spec has to encode. Do not invent numbers.
- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) — the
  spec template, beside the brief and the memo.
- [AI Tools Lab](https://adamwstauffer.github.io/ai-lms/ailab.html) — the three routes for handing a
  spec to an AI tool, and what each one can and cannot do.
- [Portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html) — why the
  spec and the model live together in the capability folder.

## 3. Deliverables

| Artifact | Path | Format |
|---|---|---|
| The specification, written first, with the audit findings added at the end | `skills/marginal-analysis/spec.md` | markdown |
| The workbook that satisfies it | `skills/marginal-analysis/model.xlsx` | xlsx |
| What the capability is, and where it was exercised | `skills/marginal-analysis/README.md` | markdown |

## 4. Background

### Why the specification comes first

Building a spreadsheet from scratch used to be the scarce skill. It is not any more. What is scarce
is the ability to state a requirement precisely enough that a capable system produces the right
artifact — and then to determine whether it did.

**The spec is the prompt.** A precise specification tells the model exactly what to build and exactly
what each result must equal, so the first build comes back close and your review is *verification
rather than archaeology*. A vague one does the reverse: the model confidently builds the wrong thing,
and you discover your own requirements one frustrating correction at a time.

There is a second effect, and it is the one that teaches you the economics. When you build by hand,
every assumption you never stated gets quietly resolved as you type, and nobody — including you —
finds out which assumptions were missing. Hand a half-formed spec to a model and the gaps come back
as defects you can point at. The failure becomes diagnostic instead of invisible.

This is not AI doing your work. The standard is higher, not lower: someone who cannot specify the
model cannot produce a correct one by any route, and someone who cannot audit it cannot tell that
they have not.

### What the specification has to get right

This is the supply side of perfect competition made mechanical. The farm is a price taker, every
additional bed of a crop takes more labor than the last, and the question is where rising marginal
cost meets a flat price line. Four things in that sentence are where specs go wrong:

**The labor function.** Hours for `q` beds = `q × hrs/wk/bed × 36 × (1 + dim%)^q`. The exponential
term is the diminishing-returns engine — each additional bed makes *every* bed slightly more
labor-hungry. A spec that describes labor as linear produces a model with flat marginal costs and no
economics in it at all.

**The costing convention.** The farmer's own field hours are consumed before any temporary hours are
purchased, and the profit-and-loss allocates labor at the *blended* rate. These are two separate
rules and stating only one of them is the most common structural defect in this model.

**Marginal cost is not monotonic here.** It falls before it rises. A spec that asserts "marginal cost
increases with quantity" is specifying a different model than the one the case describes, and the
build will be wrong in an interesting way. State the mechanism you expect instead of the shape you
expect.

**Validation rules are part of the specification, not an afterthought.** The check figures below are
published precisely so you can write them into the spec *as acceptance criteria* — the conditions
the finished workbook must satisfy — before a single formula exists.

### Check figures — your acceptance criteria

| Check | Value |
|---|---|
| Optimal mix | Tomatoes **10** / Carrots **20** / Mesclun **30** (60 beds) |
| Season profit | **$42,762** |
| Standalone P ≈ MC points | Tomatoes ~10 · Carrots ~10 · Mesclun ~6 beds |

These are not the answer you are being graded on. They are the test suite. A model that reproduces
them with broken formulas fails inspection just as surely as one that misses them.

## 5. Procedure

### Specify

1. **Write `skills/marginal-analysis/spec.md` before opening Excel.** Half a page to a page, covering
   five things:
   - **Inputs, as a named contract.** Every input with a name, its value, its unit, and its source in
     the case README. You choose the names; the requirement is that they exist and are used
     consistently.
   - **Structure.** Every sheet or region and what it is for — inputs, cost structure, the
     marginal-cost schedules, the optimization, the checks.
   - **Calculation logic in named-range notation, never cell addresses.** `LABOR_HRS(q) = q ×
     HRS_PER_BED × WEEKS × (1 + DIM_PCT)^q` is specifiable. "Column D times column E" is not — it
     describes a spreadsheet that does not exist yet.
   - **Validation rules.** The check figures above as acceptance criteria, plus the `q = 1` hand
     calculation, plus "no error cells" and "every calculated cell contains a formula."
   - **Outputs.** Name each result the model has to report.

   *Confirm:* someone who has never seen the case could build the workbook from this document alone.
   That is the actual test, and it is worth reading your spec once with that reader in mind.

2. **Write for an AI reader.** Ambiguity here becomes a defective workbook in the next step. "A
   reasonable labor rate" is not a specification. Every variable gets a name, a value, and a unit.
   *Confirm:* no sentence in the spec requires the reader to already know the case.

3. **Commit the spec before generating anything.** The commit order is part of the deliverable.
   *Confirm:* `git log` shows the spec landing before the workbook.

### Generate

4. **Hand the spec to an AI tool as-is.** Any of the three routes in the
   [AI Tools Lab](https://adamwstauffer.github.io/ai-lms/ailab.html) — a chat surface, a CLI agent
   pointed at your repository, or Claude for Excel if you have access. A manual build directly from
   your spec is also permitted; the contract is graded, not the tool.
   *Confirm:* you pasted or linked the spec without rewriting it in the chat.

5. **Treat re-explanation as a defect report.** If you find yourself explaining the model in the chat
   window, the explanation belongs in the spec. Stop, add it to `spec.md`, commit the change, and
   regenerate.
   *Confirm:* every clarification you had to give verbally now exists in the committed spec.

6. **Run the optimization.** Objective: maximize profit. Changing cells: the three bed-count
   decisions. Method: **GRG Nonlinear** with **integer** decisions. Constraints as the case README
   states them — bed caps, 64 total beds, temporary workers ≤ 4.
   *Confirm:* every constraint-check cell is green.

### Audit

7. **Run your validation rules against what came back**, and record the findings in a short section
   at the end of `spec.md`. For each check: what you checked, what you found, what you did. At
   minimum, run these five:
   - **The `q = 1` hand check.** One bed of tomatoes should cost `1 × 2.5 × 36 × 1.10` hours. This
     one line catches a dropped exponent, the most common structural defect.
   - **An independent cross-check.** Take at least one intermediate value — a marginal cost at a
     given bed count — and compare it against the
     [Farm Profit Lab](https://adamwstauffer.github.io/ai-lms/farmlab.html), which is a separate
     implementation of this same model. If they disagree, believe the lab and find your formula error.
   - **Two Solver starting points.** Run from 0/0/0 and from 20/0/0. They may not agree; note the
     path-dependence and which one you trust.
   - **The check figures.** 10/20/30 beds, $42,762, standalone crossings near 10 / 10 / 6.
   - **Formulas, not values.** Spot-check that calculated cells contain formulas referencing your
     named inputs. A pasted number where a formula belongs is a defect even when the number is right.

   *Confirm:* each check names what it would have caught, not just that it passed.

8. **Note the tomato marginal-cost dip** at around 6 beds, without explaining it — that is Stage 3's
   work.
   *Confirm:* the observation is recorded somewhere you will find it again.

9. **Write `skills/marginal-analysis/README.md`** — three or four lines. What the capability is, and
   an "exercised in:" line pointing at this engagement's brief, and after Stage 3 its analysis and
   memo.
   *Confirm:* the links resolve on github.com.

10. **Commit at least twice** with descriptive messages — the spec, then the audited workbook. Not
    `update xlsx`.
    *Confirm:* if `~$model.xlsx` appears in your Changes panel, your `.gitignore` is broken; fix it
    before committing.

## 6. AI use

| Artifact | Draft order |
|---|---|
| `skills/marginal-analysis/spec.md` | Human-first |
| `skills/marginal-analysis/model.xlsx` | AI-first, verified |
| `skills/marginal-analysis/README.md` | Human-first |

**If the artifact is evidence of your judgment, you draft it first and AI reviews; if the artifact is
a means to the work rather than the work itself, AI may draft it and you verify.** The two working
loops are described in [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html).

**For this stage specifically:** the workbook is a means, and AI generating it from your spec is the
assignment rather than a shortcut. The spec is not — it is the artifact your judgment is being read
in, so AI may critique it, find the ambiguity in it, and argue with your conventions, but you write
it. The audit is yours as well: a model can help you run a check, and it cannot tell you its own
output is correct.

Log the sessions that mattered. The prompt log is graded in Stage 3, and a generation-and-repair
session is exactly what belongs in it.

## 7. Verification

- [ ] `spec.md` committed **before** the workbook — check the commit order
- [ ] Every input named, with a unit and a source in the case README
- [ ] Calculation logic written in named-range notation, no cell addresses
- [ ] Validation rules stated as acceptance criteria, including the published check figures
- [ ] Any clarification given verbally during generation now lives in the committed spec
- [ ] `model.xlsx` committed to `skills/marginal-analysis/`
- [ ] Labor function verified by hand at `q = 1`
- [ ] At least one intermediate value cross-checked against the Farm Profit Lab
- [ ] Solver run from two starting points (0/0/0 and 20/0/0), path-dependence noted
- [ ] Check figures matched: 10/20/30 beds, $42,762, standalone crossings ~10 / ~10 / ~6
- [ ] Calculated cells contain formulas, not pasted values; no `#REF!`, `#DIV/0!`, or `#NAME?`
- [ ] All constraint-check cells green
- [ ] Audit findings recorded in `spec.md` — at least three checks, each naming what it would have caught
- [ ] The tomato MC dip located and noted for Stage 3 — do not explain it yet
- [ ] `README.md` in the capability folder, with an "exercised in:" line
- [ ] At least two descriptive commits for this stage

## 8. Rubric (8 pts)

| Criterion | Pts | What distinguishes strong work |
|---|---|---|
| Spec completeness — inputs, structure, calculation flow | 3 | Every input named with units and source; the labor function, the permanent-then-temporary costing convention, and the blended-rate allocation all stated in named-range notation, unambiguously enough to build from without knowing the case |
| Spec validation rules | 2 | Check figures stated as acceptance criteria *before* the build, alongside the `q = 1` hand check and the structural rules (formulas not values, no error cells) |
| Workbook satisfies the contract | 2 | Formulas referencing named inputs rather than pasted values; Solver reproduces 10/20/30 at $42,762; constraint checks green; no error cells |
| Audit note | 1 | At least three concrete checks run, each named with what it would have caught, and any defects found documented with the fix |

## 9. Common failure modes

| What goes wrong | The correction |
|---|---|
| The spec is written after the workbook | It is then a description, not a specification, and the commit order shows it. Write it first, even roughly |
| The spec describes a spreadsheet rather than a model — "column D times column E" | The spreadsheet does not exist yet. Name the quantities and state the relationships between them |
| The model comes back with flat marginal costs | The diminishing-returns exponent is missing from the spec. Fix the spec, commit, regenerate — do not patch the workbook by hand |
| Labor costs are wrong by a consistent margin | The spec stated one of the two costing rules. Permanent hours are consumed before temporary hours, *and* the P&L allocates at the blended rate |
| The chat transcript is full of clarifications | Each one is a spec defect that was never written down. Move them into `spec.md` and regenerate |
| Marginal cost falls around bed 6 and it looks like a bug | The model is right — marginal cost is not guaranteed to increase. Note it for Stage 3 |
| The two Solver starting points disagree and one is ignored | That is a finding, not a nuisance. Record which you trust and why |
| The audit says "checked, correct" three times | A check is only worth recording if you can say what it would have caught |
| `~$model.xlsx` appears in Changes | `.gitignore` is missing, misnamed, or in the wrong folder |

## 10. References

- [Case README](README.md) — assumptions, constraints, instructor notes
- [Deliverable templates](https://adamwstauffer.github.io/ai-lms/deliverable-templates.html) — the spec template
- [AI Tools Lab](https://adamwstauffer.github.io/ai-lms/ailab.html) — handing a spec to chat, a CLI agent, or Claude for Excel
- [Farm Profit Lab](https://adamwstauffer.github.io/ai-lms/farmlab.html) — an independent implementation of this model, for cross-checking
- [Portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html) · [AI conventions](https://adamwstauffer.github.io/ai-lms/ai-conventions.html)
- [Git mechanics](https://adamwstauffer.github.io/ai-lms/onboarding.html#git-mechanics), including [how work is submitted, with the post-deadline revision policy](https://adamwstauffer.github.io/ai-lms/onboarding.html#submitting)
