# Stage 3 – AI-Assisted Build + Audit (17% of project)

## Goal

Generate a working workbook **from your own Stage 2 specification** — using any AI tool or by
hand — and **audit the result**. The workbook must satisfy the build contract below regardless
of how it was produced. Your graded skill in this stage is not typing formulas; it is
**specifying precisely and auditing ruthlessly** — the two things an analyst still owns when AI
does the assembly.

There is no starter template. Your spec *is* the template.

---

## The Build Contract

The finished workbook must have, verifiable by inspection (and by the grading script):

1. **All ten named ranges** from the contract (`FC_AMT`, `S0_in`, `F0_in`, `R_USD`, `R_FC`,
   `K_PUT`, `K_CALL`, `PREM_PUT`, `PREM_CALL`, `T_DAYS`), each attached to the right cell.
2. **Formulas, never hard-coded values.** Every calculated cell contains a formula referencing
   named ranges. A pasted number where a formula belongs scores zero for that element — this is
   checked mechanically.
3. **Cover page** — scenario, author, date, and a data-provenance block (placeholder values
   noted as indicative, per your spec).
4. **Legend/Key tab** — the color convention, applied throughout:
   Yellow = inputs · Blue = assumptions · Green = formulas · Gray = outputs.
5. **All three hedge families** — forward; money market shown in its three explicit steps;
   put and call with premium cost in USD and proceeds as a function of `S_T`.
6. **Sensitivity table + chart** — ±5% in 1% steps, formula-driven (no hand-typed rows).
7. **Validation checks live in the workbook** — the parity check and any other check figures
   from your spec §7, computed, visible, and passing.

## Tool guidance

Use whatever produces the best result — the contract, not the tool, is graded:

- **Claude for Excel** (if you have access — availability varies; don't buy anything),
- **Claude / ChatGPT on the web**: paste or link your spec (GitHub URL is cleanest), ask for the
  workbook or for the structure + formulas to assemble,
- **Copilot in Excel**, or
- **manual build** directly from your spec.

Whichever route: your spec goes in **as-is**. If you find yourself re-explaining the model in
the chat, that's a spec defect — fix the spec (commit the change), then regenerate. Log every
prompt in `prompt-log.md`.

---

## The Audit Note (required)

AI output is a draft, not a deliverable. Audit the generated workbook against your spec's
validation rules and document **at least 3 findings** — things you checked and confirmed, or
found broken and fixed. Real examples: a hardcoded value where a formula belongs, a named range
attached to the wrong cell, a sign error in the put payoff, a sensitivity row that doesn't
recalculate, parity check failing due to rate-basis mismatch. For each finding: what you
checked, what you found, what you did.

An audit note claiming "everything was perfect" is a red flag, not a good sign — the grader
will be auditing the same workbook.

## Deliverables

- Workbook: `models/builds/YYYY-MM-DD-{lastname}-{scenario-slug}-model.xlsx`
- Audit note: `analysis/YYYY-MM-DD-{lastname}-build-audit.md` (≥3 findings)
- Updated `prompt-log.md`. Commit incrementally — generation, then each audit fix.

## Evaluation

| Criterion | Description | Weight |
| --------- | ----------- | -----: |
| Contract compliance | Named ranges complete and correct; formulas-only (mechanically checked); all hedges + sensitivity present and computing correctly | 50% |
| Structure & presentation | Cover, legend/key, color convention, auditable layout | 25% |
| Audit note | ≥3 substantive findings with evidence; fixes committed | 25% |

---

## How this leads to Stage 4

Your workbook currently runs on placeholder inputs. Stage 4 loads **live market data** — and if
the model only worked because of the numbers it was built around, it will break. A clean build
contract (formulas + named ranges everywhere) is what makes Stage 4 a ten-minute task instead
of a rebuild.
