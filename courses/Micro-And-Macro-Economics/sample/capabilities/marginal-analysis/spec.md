---
type: spec
capability: marginal-analysis
artifact: model.xlsx
updated: YYYY-MM-DD
---

# Spec — marginal-analysis model

<!-- SAMPLE. The spec defines the artifact precisely enough that somebody else could rebuild it
     without asking you a question. Headings below are the shape; the content is yours. -->

## Purpose

*What decision the model supports, and for whom.*

## Inputs

| Input | Cell / named range | Units | Source |
|---|---|---|---|
| *(input)* | `Inputs!B4` | *(units)* | [`data/`](../../data/) |

Every input is a literal typed once, in one place. Nothing downstream is hardcoded.

## Calculations

| Output | Formula logic | Depends on |
|---|---|---|
| Total cost | *(stated in words, then the formula)* | inputs above |
| Marginal cost | change in total cost ÷ change in quantity | total cost column |
| Profit-maximizing quantity | the last unit where MR ≥ MC | MC, MR columns |

**Every calculated cell is a formula.** Only raw source data is a literal — a typed-in number
where a formula belongs is the single most common defect in a submitted workbook, and it breaks
the moment an input changes.

## Named ranges

| Name | Refers to | Why it is named |
|---|---|---|

## Assumptions and limits

*What the model takes as given, and the conditions under which its answer stops holding.*

## How to verify it

*The checks that show the model is right — a total that must tie, a value you can compute by
hand, a sensitivity that must move in a known direction.*
