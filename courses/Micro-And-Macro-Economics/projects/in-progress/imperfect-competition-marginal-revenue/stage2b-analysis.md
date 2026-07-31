# Mini 2 · Stage 2b — Analysis + Prompt Log

> **Status:** Kumu-authored draft (2026-07-31) — pending Adam's review before students see it.

**Mini weight:** 10% of course grade — this stage: 12 of 20 pts (hypothesis/setup 3 · analysis 6 · prompt log + reflection 3)
**Format:** upload-only — no presentation component
**Deliverable:** `projects/monsanto/analysis.md` (with ≥2 figures) and `projects/monsanto/prompt-log.md` in your portfolio repo
**Due:** end of Week 4 — exact dates on the course calendar

---

## Overview

Stage 2a built the machine; this stage is where you say what it means. Your completed `monsanto-model.xlsx` shows the same company earning $106.0M in one market and $8.785B in the other — same crop, same fixed costs. The analysis explains *why*, puts a dollar figure on what society pays for it, and takes a position on whether that price is worth paying.

One structural note: in Mini 1 the setup narrative was a standalone `brief.md`. Your repo already exists and the two-market setup is short, so the brief is **folded into this stage** — your hypothesis (already committed, top of `analysis.md`, per Stage 2a Step 0) plus a setup paragraph replace it. Same points, one fewer file.

This analysis is also the deliberate on-ramp to your individual **Policy Shock project (30% of the course)**: markup, Lerner, deadweight loss, and the patent-tradeoff argument are exactly the toolkit you'll aim at a policy of your own choosing. Write this one well and you've drafted your own reference material.

The Week 4 in-class session is a working discussion of the case's four spine questions — come with your model done. **DLEMBA students:** screencast instead of the live session; deliverables identical.

---

## Part 1 — Hypothesis + setup (3 pts)

At the top of `analysis.md` (already committed in Stage 2a):

1. **Your 3-sentence hypothesis**, unedited — leave it as committed, wrong is fine.
2. **A setup paragraph in your own words:** the two-market structure — why Monsanto is a price taker in non-GMO seed and a price maker in GMO seed, and what the patent has to do with it. Your words, not the README's.
3. **A hypothesis verdict:** one or two sentences on where your prediction landed vs the model, and what you misjudged. A prediction that missed by 10× and a sharp account of why beats a lucky guess with no account.

## Part 2 — The analysis (6 pts)

`analysis.md` continues with the comparison, supported by **at least 2 figures** exported from your workbook (the D/MR/MC chart is the obvious first; a profit or decision-table figure is a natural second). Cover all five, in whatever structure reads best:

| # | Question | What strong coverage looks like |
|---|---|---|
| 1 | **Why is MR < P for the price maker — and equal to P for the price taker?** | The twice-as-steep rule for linear demand, stated mechanically: one more bag sold lowers the price on *every* bag, so marginal revenue falls at twice the slope of demand. The price taker's extra bag changes nothing — MR = P = $120. |
| 2 | **Why does P\* come off the demand curve, not MR?** | MR = MC picks the *quantity* (34,025,974 bags); demand tells you the *price* buyers will pay for that quantity ($297.03). Explain it as if to a classmate who just charged $69.05. |
| 3 | **What do markup and Lerner measure?** | 4.30× and 0.768 as market-power gauges: price 4.3× marginal cost, ~77% of the price being margin over cost. Contrast with the non-GMO row (1.0×, 0). |
| 4 | **What does the DWL ≈ $2.99B/yr mean?** | Not a transfer — surplus that *vanishes*. Monopoly withholds ~26M bags to hold price at $297; the competitive benchmark price is ~$121.46 — almost exactly the $120 non-GMO price. Strip the patent and GMO seed is just… seed. |
| 5 | **Does the patent's innovation incentive justify the ~$3B/yr?** (one paragraph, a position, defended) | Engage the case's discussion spine: complement lock-in (Roundup sells the seed and vice versa), patent enforcement (no replanting) as what *keeps* demand downward-sloping, superweeds as a negative externality the private optimum ignores, and Bayer 2018 — where the DOJ's answer was the largest negotiated merger divestiture in U.S. history. Either side is defensible; a fence-sit is not. |

Use the check figures from the [case README](README.md) — don't invent numbers, and don't cite outside statistics without a source.

## Part 3 — Prompt log + reflection (3 pts)

`projects/monsanto/prompt-log.md`:

- **The log:** one row or entry per meaningful AI session across the whole mini — date, tool, what you asked, what you did with the answer. Sessions from Stage 2a (formula debugging, MR mechanics) belong here too.
- **The reflection (≤300 words):** how you used AI on this mini, where it helped, and — required — **one AI error you caught**: a wrong formula, a confidently wrong explanation, a P\* read off the wrong curve. If you genuinely caught none, say what you *checked* and how you'd have known. "The AI was great and made no mistakes" scores as not having looked.

**AI-use boundary (course standard):** AI may explain MR/MC mechanics, critique your reasoning, and debug formulas — not write your analysis. A useful line to hold: paste the AI your *draft* and ask it to attack the argument; don't paste it the questions and ask for prose. Your reflection is where the difference shows.

---

## What to submit

Graded by inspection of your repo — nothing to upload beyond your repo URL.

- [ ] `projects/monsanto/analysis.md` — hypothesis (unedited) + setup + verdict, the five-question analysis, ≥2 figures embedded and referenced in the text
- [ ] `projects/monsanto/prompt-log.md` — session log + ≤300-word reflection with the caught AI error
- [ ] Figures live in the repo (e.g., `projects/monsanto/figures/`) and render on GitHub — no broken image links
- [ ] At least **2 descriptive commits** for this stage's work

---

> **Post-deadline revision sweep.** After this stage's due date, I'll re-run the rubric against your repo state. Improvements you commit before the deadline — tightening the DWL explanation, replacing a generic patent paragraph with a real position, fixing broken figure links — can move your score up; the full rubric applies, no cap on the bump. No email or issue needed; just revise the files. One sweep per stage; the score locks once the sweep runs.

---

## Rubric (12 pts)

| Criterion | Pts | What distinguishes strong work |
|-----------|-----|-------------------------------|
| Hypothesis + setup | 3 | Hypothesis committed before model work (Stage 2a timestamp), left unedited; setup in own words; honest verdict on the miss |
| Perfect vs imperfect mechanics (Q1–Q3) | 3 | Twice-as-steep rule stated correctly; P\*-off-demand explained, not just asserted; markup/Lerner interpreted as market power, not recited |
| DWL + patent tradeoff (Q4–Q5) | 3 | $2.99B/yr framed as vanished surplus; the $121 ≈ $120 benchmark "aha" landed; patent paragraph takes and defends a position using the spine |
| Prompt log + reflection | 3 | Complete log across both stages; reflection ≤300 words, specific, includes a genuinely caught AI error |

---

## Tips

- **Write for the classmate who got it wrong.** The best test of Q1–Q2 prose: would it fix someone who priced at MR = MC? If it only restates definitions, it wouldn't.
- **The verdict is the interesting part.** Nobody grades you down for a wrong hypothesis — only for pretending you didn't have one, or editing it after the fact (the commit history shows both).
- **Take a side on the patent.** The paragraph exists to make you weigh $2.99B/yr of vanished surplus against the incentive that produced the trait at all. "There are arguments on both sides" is the one answer that earns nothing.
- **Bank the toolkit.** Markup, Lerner, DWL, benchmark-vs-actual — your Policy Shock project will ask you to run this exact play on a policy you choose. Keep this analysis close; you'll reuse its bones.
