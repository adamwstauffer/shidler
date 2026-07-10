# Stage 1 – Executive Memo (17% of project)

> Content unchanged from v1 (`../stage1-memo-assignment.md`) — this stage is typically already
> in flight when the v2 docs go live. v2 adds the rubric table (grading transparency) and the
> canonical save location/filename.

## Goal

Using `_templates/template-decision-memo.md`, write a **300–400 word memo to your CFO**
explaining your firm's **FX receivable exposure** and why hedging is worth considering.

## Instructions

**Scenario:** Your firm expects to receive a foreign-currency payment (see your assigned
scenario in `scenarios.md`) on a specific future date. Exchange-rate volatility could affect
how much your company ultimately receives in USD.

**Include:**

1. **What the exposure is** — currency, amount, timing.
2. **Why it's risky** — what could go wrong for USD proceeds.
3. **Three hedge families** — forward, money market, options — with quick pros/cons for each.
4. **Next steps** — what you'll build in Stages 2–5:
   - *Model Specification (Stage 2):* design the workbook — inputs, named ranges, calculation
     flow — before building.
   - *AI-Assisted Build (Stage 3):* generate the workbook from your spec and audit the output.
   - *Market Data (Stage 4):* load live market data and confirm the model holds up.
   - *Validation & Recommendation (Stage 5):* validate against an independent LLM run and
     deliver the hedge recommendation.

**Tone:** executive-friendly and clear. The CFO has 90 seconds.

## Deliverable

- File: `docs/decisions/YYYY-MM-DD-{lastname}-{scenario-slug}-hedge-framing.md`
- One page, from the decision-memo template, YAML frontmatter intact.
- Committed and pushed (after Stage 0, restructure the location if you saved it elsewhere).

## Evaluation

| Criterion | Description | Weight |
| --------- | ----------- | -----: |
| Exposure framing | Currency, amount, timing, and business consequence stated precisely | 25% |
| Hedge families & trade-offs | All three families, with honest pros/cons, not boilerplate | 25% |
| Next steps | Correctly frames the Stage 2–5 arc as a plan the CFO can approve | 25% |
| Professionalism | Executive tone, template used, correct location and filename, committed | 25% |

---

## How this leads to Stage 2

Every variable you name in this memo — the receivable amount, the timing, the rates that matter —
becomes a **named input** in your Stage 2 specification. If the memo is vague about the exposure,
the spec will be vague about the model. Write the memo like the model depends on it, because it
does.
