# Capabilities

One folder per capability — `marginal-analysis`, `pricing-power`, `fx-hedging`, whatever you turn
out to be able to do. Never a folder named for a course, a semester, or a week.

A capability folder holds three things:

| File | What it is |
|---|---|
| `README.md` | what the capability is, and which engagements exercised it |
| `spec.md` | the method: model design, named ranges, formula logic |
| the model file | starts as a template, becomes your model |

The spec and the model live together because a method and the workbook implementing it are one
object. Splitting them into a `specs/` folder creates two places to look and no payoff.

Capabilities are what you can do; the engagements in `docs/`, `data/`, and `analysis/` are the
evidence that you did. Each README's link from claim to proof is the line a reader follows.
