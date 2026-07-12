# Stage 2 – Model Specification (21% of project)

## Goal

Using `_templates/template-spec.md`, write a **2–3 page technical specification** for your FX
hedging workbook — **before any Excel exists**. The spec must be precise enough that an AI (or a
colleague who has never seen your memo) could build the complete workbook from this document
alone. In Stage 3, that is literally what happens.

This is the design stage. Professionals spec models before building them; the discipline of
writing down every input, name, formula, and check *first* is where most of the learning in this
project lives.

---

## Scenario

You are the treasury analyst who wrote the Stage 1 memo. The CFO said "yes, build it." Before
you (or your AI) open Excel, Treasury wants a design document it can review — because a model
built without a spec is a model nobody else can audit.

Use your assigned scenario's parameters (`scenarios.md`) as **placeholder inputs**, clearly
flagged as *"indicative — replaced with live market data at Stage 4."* Where the scenario says
you set the value (strikes at/near spot, interest rates), state the placeholder you chose and
how Stage 4 will source the real one.

---

## Include

1. **Problem Statement** — exposure, timing, risk, business consequence. Precise: currency,
   amount, settlement date.

2. **Inputs (Named-Range Contract)** — every input with name, placeholder value, unit, and
   Stage-4 data source. Use the standardized convention exactly:

   | Named Range | Description | Unit |
   | ----------- | ----------- | ---- |
   | `FC_AMT`    | Foreign-currency receivable | EUR |
   | `S0_in`     | Spot rate at inception | USD per EUR |
   | `F0_in`     | Forward rate | USD per EUR |
   | `R_USD`     | USD interest rate | Annual % |
   | `R_FC`      | Foreign-currency interest rate | Annual % |
   | `K_PUT`     | Put option strike | USD per EUR |
   | `K_CALL`    | Call option strike | USD per EUR |
   | `PREM_PUT`  | Put premium per unit of FC | USD |
   | `PREM_CALL` | Call premium per unit of FC | USD |
   | `T_DAYS`    | Days to settlement | Days |

3. **Tab Architecture** — name every tab and its purpose. Minimum: Cover (scenario, author,
   data-source documentation), Legend/Key (color convention), Inputs, one calculation area per
   hedge (forward, money market, options), Sensitivity, Notes & Assumptions.

4. **Assumptions & Constraints** — rate basis (e.g., ACT/360), transaction costs ignored or
   not, forward/MM parity expectation, premium treatment. Explicit enough for full
   reproducibility.

5. **Calculation Flow** — formula logic in named-range notation, never cell addresses:
   - Forward hedge: `FC_AMT × F0_in` → locked USD proceeds.
   - Money market hedge, 3 steps: borrow `FC_AMT / (1 + R_FC × T_DAYS/360)` → convert at
     `S0_in` → invest at `R_USD`; state the parity check vs. the forward.
   - Options: total premium in USD; net proceeds as a function of ending spot `S_T`; payoff
     conditions for put floor and call participation.

6. **Sensitivity Plan** — `S_T` from 0.95×`S0_in` to 1.05×`S0_in` in 1% steps; USD proceeds per
   strategy at each rate; one comparison chart. State what the chart should let the CFO see.

7. **Validation Rules (Check Figures)** — the self-checks the finished workbook must pass:
   forward ≈ MM parity (within rounding), option proceeds vary continuously with `S_T`, no
   error cells, every output cell a formula. These become your Stage 3 audit checklist.

8. **Outputs** — name each summary result and table (gray cells) exactly.

---

## Instructions

- **Write for an AI reader.** Ambiguity here becomes a wrong workbook in Stage 3 — the AI will
  guess, and guess wrong. Every variable: name, value, unit. "A reasonable interest rate" is
  not acceptable.
- **LLM as drafter, you as editor.** Have an AI draft the spec from your memo + scenario, then
  correct it. Log prompts in `prompt-log.md` and show **at least one specific iteration** — a
  gap you identified in the draft and how you fixed it (before/after note or annotated diff).
- Keep formulas conceptual (named-range notation), professional tone, 2–3 pages, no filler.

## Deliverable

- File: `docs/specs/YYYY-MM-DD-{lastname}-{scenario-slug}-spec.md`
- Plus updated `prompt-log.md`. Committed and pushed.

## Evaluation

| Criterion | Description | Weight |
| --------- | ----------- | -----: |
| Named-range contract & tab architecture | Complete inputs table with units/placeholders/Stage-4 sources; every tab named with purpose | 30% |
| Calculation flow | Correct, correctly ordered logic for all three hedge families in named-range notation | 30% |
| Validation & sensitivity plan | Concrete check figures; sensitivity design fully specified | 20% |
| Reproducibility & prompt log | Buildable by a context-free reader; HIL iteration evidenced in the log | 20% |

---

## How this leads to Stage 3

In Stage 3 you hand this document to an AI and it builds your workbook. Every weakness in the
spec becomes a defect in the build — which you will then have to find and fix in the audit. The
better the spec, the shorter the audit.

And the sharper, AI-era reason to get it right: you don't describe the workbook to the AI and
hope — **the spec is the prompt.** A precise spec tells the model exactly what to build and exactly
what each result must equal, so the first build comes back close and the audit is *verification,
not archaeology.* A vague spec does the reverse: the AI confidently builds the wrong thing, and you
discover your real requirements one frustrating tweak at a time. Every minute spent making this
document unambiguous is a round of corrective back-and-forth you don't pay for later.
