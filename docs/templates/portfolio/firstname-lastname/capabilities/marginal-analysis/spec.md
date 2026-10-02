# Spec: marginal-analysis

## Question it answers

At what quantity Q\* does profit peak, given a price and a schedule of rising batch costs?

## Inputs

| Input | Where | Type |
|-------|-------|------|
| Price per unit (P) | `Inputs!B3` | typed (blue) |
| Fixed cost per period (FC) | `Inputs!B4` | typed (blue) |
| Batch size, batch variable cost | `Data!A:C` | typed, from `data/prep-batch-costs.csv` |

## Method (per batch row *i*)

```text
Q_i      = Q_(i-1) + batch size
TVC_i    = TVC_(i-1) + batch variable cost
TC_i     = FC + TVC_i
TR_i     = P × Q_i
Profit_i = TR_i − TC_i
MC_i     = batch variable cost ÷ batch size        (cost of each plate in this batch)
MR_i     = P                                       (price-taker: each plate sells at P)
Signal_i = "Produce" if MR_i ≥ MC_i, else "Stop"
```

Q\* = the Q with the highest profit. It must match the last row whose signal is "Produce."

## Outputs

`Model!` summary block: Q\*, profit at Q\*, MC of the last batch produced, MC of the first batch
skipped.

## Checks

- Every cell on `Model` is a formula; recalculation shows zero errors.
- Q\* from max-profit equals Q\* from the MR ≥ MC rule.
- Change the price in `Inputs!B3` and Q\* moves in the expected direction.

## Limits

- Assumes every plate prepped sells. Leftovers are a cost the model doesn't capture.
- Constant price: no discount for volume, no demand curve. For that, MR falls with Q and the spec
  needs a demand input.
