# marginal-analysis

Finds the output level where one more unit stops paying for itself: keep producing while
**marginal revenue (MR) ≥ marginal cost (MC)**, and stop at the first unit where MC > MR.

## When to use it

Any "how much / how many" decision with rising costs: prep volume, staffing hours, ad spend,
inventory orders.

## Files

| File | Purpose |
|------|---------|
| [spec.md](spec.md) | Method, inputs, outputs, and checks — enough for someone else to rebuild it |
| `model.xlsx` | The working model: `Inputs` → `Data` → `Model` |

## Used in

- [Engagement 1: lunch-plate volume](../../docs/decisions/2026-10-09-lunch-plate-volume.md)
