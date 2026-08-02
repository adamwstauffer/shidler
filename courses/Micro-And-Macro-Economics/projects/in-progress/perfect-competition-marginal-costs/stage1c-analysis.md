# Case 1 · Stage 1c — Analysis + Prompt Log

**Case weight:** 10% of course grade — this stage: 9 of 20 pts (analysis 6 + prompt log 3)
**Format:** Upload-only — no presentation component
**Deliverable:** `analysis/perfect-competition-analysis.md` (≥2 figures in `analysis/figures/`) + `docs/decisions/perfect-competition-memo.md` + an updated root `prompt-log.md`, all committed to your repo
**Due:** end of Week 2 — exact dates on the course calendar (Case 1 spans Weeks 1–2, Aug 24–Sep 4)

> **Status:** Kumu-authored draft (2026-07-31; paths + framing rewritten 2026-08-02 to the portfolio-repo standard) — pending Adam's review before students see it.

> **Where this fits in the engagement.**
> **Input:** your Stage 1a `docs/briefs/perfect-competition-brief.md` (the hypothesis you're now testing) + your Stage 1b `skills/marginal-analysis/model.xlsx` (the evidence source — every number you cite comes from it).
> **Output (this stage):** the analysis, the client memo, and an updated prompt log — closing out Case 1.
> **Used by:** the in-class debrief, and Cases 2–3 — the analysis-over-a-model-you-built pattern repeats all semester, as does the prompt-log habit.

---

## Overview

Stage 1b produced a number — 10/20/30, $42,762. Stage 1c is where the points actually live: explain *why* that's the answer, in economics, with your model's own evidence, and then tell the farmer what to do about it. A Solver output you can't explain is a coincidence you happen to have committed.

Three files, and the split between the first two is the point:

| File | What it is |
|---|---|
| `analysis/perfect-competition-analysis.md` | **The evidence.** What the model shows and why, with figures. Written for someone checking your work. |
| `docs/decisions/perfect-competition-memo.md` | **The answer.** What the farmer should do, in half a page, written for the farmer. |
| `prompt-log.md` (repo root) | The curated record of AI sessions + your reflection. |

Briefs ask; memos answer. You wrote the question in Stage 1a — this is where you close it.

## `analysis/perfect-competition-analysis.md` — the optimal mix and *why* (6 pts)

Aim for 1–2 pages plus **at least 2 figures** — charts exported or screenshotted from your workbook into `analysis/figures/` (MC-vs-price per crop is the obvious pair). Every figure earns its place by being *referenced in the text*; a decorative chart is worth nothing. Cover four things:

1. **P = MC evidence per crop.** Where does each crop's marginal cost cross its price, and how does that show up in the optimal mix? Tomatoes are the clean case — interior at 10 beds, MC $8,249 at bed 10 vs price $8,800, bed 11 would cost $9,391. Show the reader the crossing, don't just assert it.
2. **Which constraints bind — and what they're worth.** Carrots and mesclun stop at their bed caps with MC still *below* price — the constraint, not economics, ends production. Use the shadow-price intuition: one more carrot bed would add roughly **$352** of profit (mesclun ~$246). Note which constraints are *slack* too — 64 beds and 4 temp workers never bind.
3. **The tomato MC dip at ~6 beds.** MC falls before it rises — explain the mechanism: the farmer's expensive field hours ($34.72/hr) run out and marginal labor switches to cheaper temp labor ($17.36/hr), then diminishing returns push MC back up through the price line. This is the "input prices bend the MC curve" lesson; an analysis that ignores the dip has ignored the most interesting thing in the model.
4. **"Grow carrots and mesclun at a loss?"** Standalone, every crop loses money at every quantity — fixed costs dominate. So why is growing them optimal? Resolve it with MC vs AVC: price exceeds average *variable* cost everywhere, so every bed contributes over variable cost, and the *mix* — not any single crop — is what turns a loss into $42,762. This is the short-run shutdown rule wearing farm clothes.

Close with one honest paragraph against your Stage 1a hypothesis: what you predicted, what the model found, what your prior got wrong or right. Being wrong in the brief and precise about *why* here is full-credit work.

## `docs/decisions/perfect-competition-memo.md` — the planting recommendation

Half a page, written to whoever has to sign off on the plan — a partner, a lender, or you next February — with no jargon they didn't ask for. The recommendation that used to close the analysis lives here instead, because that's the shape of the work: the analysis is the file a reviewer audits, the memo is the file a decision-maker reads.

Three things belong in it:

- **The plan.** Plant 10 / 20 / 30 — and one sentence of reasoning a non-economist would accept.
- **The judgment call.** Both the carrot and mesclun caps bind, and one is worth more to relax than the other. Which ground is worth spending money to expand first, and what is one more bed worth? That number came out of your shadow-price work in the analysis — this is where it turns into advice.
- **What would change your answer.** One line. If tomato prices fell 20%, if a fifth temp worker were available, if the caps lifted — name the variable your recommendation is most sensitive to.

This memo carries no separate points; it is read together with the analysis under the "P = MC evidence + binding constraints" criterion, which already asks what a farmer should conclude from a binding cap. What changes is where that conclusion lives — and that it's written to a person, not to a rubric.

## `prompt-log.md` — sessions + reflection (3 pts)

Log the AI sessions that **mattered** — the ones where AI explained a concept, caught (or introduced) an error, or pushed your reasoning. Not a transcript dump; a curated record. For each session: date, tool, what you asked, what you got, what you did with it.

The log lives at the repo root and accretes across all three engagements — add a dated section for this one rather than starting a new file.

Then a **reflection, ≤300 words**: where AI helped, where it was wrong, and — the part that's graded hardest — *how you verified*. "It seemed right" is not verification; "I checked its MC formula against the labor function at q = 1 and it had dropped the exponent" is. If AI genuinely made no error you could catch, document the verification that convinced you it hadn't — "the AI was flawless" without evidence of checking reads as "I didn't look."

## AI-use boundary (course standard)

AI may explain concepts, critique your reasoning, and help debug formulas. It may not write your brief, analysis, memo, or reflection. Log the sessions that mattered.

The line for this stage, concretely: asking AI to critique your draft explanation of the MC dip is in-bounds and worth logging. Pasting the case in and asking for an analysis is out-of-bounds — and it shows, because AI-written analysis explains the textbook, not *your workbook's* numbers.

---

## What to submit

Commit all three files to your repo — Stage 1c is graded by inspection. Nothing separate goes to Lamaku unless announced.

- [ ] `analysis/perfect-competition-analysis.md` — ≥2 figures, all four questions addressed, hypothesis revisited
- [ ] Figure image files in `analysis/figures/` (relative links that render on GitHub — check the rendered page, not just your editor)
- [ ] `docs/decisions/perfect-competition-memo.md` — the plan, the judgment call on which cap to relax, what would change your answer
- [ ] `prompt-log.md` updated — meaningful sessions + ≤300-word reflection
- [ ] `skills/marginal-analysis/README.md` "exercised in:" line updated to point at the analysis and memo
- [ ] ≥2 descriptive commits for this stage

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit — a figure that actually shows the P = MC crossing, a sharper shutdown-rule paragraph, a reflection with real verification steps — can move your score up; the full rubric applies, no cap on the bump. No email needed; just revise and push. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (9 pts)

| Criterion | Pts | What distinguishes strong work |
|-----------|-----|-------------------------------|
| P = MC evidence + binding constraints | 3 | Crossings shown from *your* model's numbers; carrot/mesclun caps identified as binding with ~$352/~$246 shadow-price reasoning; slack constraints named; the memo turns that into a recommendation the farmer could act on |
| MC dip + at-a-loss resolution | 2 | Dip mechanism (perm→temp wage switch) explained, not just observed; MC-vs-AVC shutdown logic resolves the "loss-making" crops correctly |
| Figures + hypothesis revisit | 1 | ≥2 figures referenced in text and rendering on GitHub; honest comparison against the Stage 1a hypothesis |
| Prompt log + reflection | 3 | Sessions curated, not dumped; reflection ≤300 words with concrete instances of AI being wrong and *how you verified* (or, if nothing was caught, the checks that cleared it) |

---

## Tips

- **Write from your cells, not from the textbook.** "MC rises due to diminishing returns" is a lecture note; "carrot MC hits $1,742 at bed 20, still $352 under price — the cap binds" is analysis. Cite your own numbers.
- **Write the memo last and write it fast.** If it takes more than twenty minutes, the analysis hasn't finished its job. A memo you struggle to write is a signal, not a writing problem.
- **The dip is a gift.** It's the one place this model surprises people — the [Farm Profit Lab](https://adamwstauffer.github.io/ai-lms/farmlab.html) makes it visible in ten seconds of dragging the tomato slider. Watch it happen, then explain it.
- **Screenshot figures are fine.** Nobody is grading chart aesthetics; they're grading whether the figure carries evidence your text uses.
- **Log as you go.** Reconstructing the prompt log the night before produces exactly the generic mush the rubric can smell. A two-line entry per session, written at the time, is effortless.
