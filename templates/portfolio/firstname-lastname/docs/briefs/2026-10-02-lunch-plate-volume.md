# Brief: How many lunch plates should the food truck prep each day?

*Written 2026-10-02, BEFORE the analysis.*

## Client and question

The owner of a (fictional) Kakaʻako food truck preps in 20-plate batches and wants to know how many
batches to prep for a weekday lunch.

## Scope

- **In:** weekday lunch, one menu item, current price ($14).
- **Out:** menu changes, catering orders, weekend demand.

## Hypothesis

More is better until the second cook's overtime kicks in. My guess: **about 120 plates** (6
batches).

## What would change my mind

If batch costs keep rising slowly past batch 6, the right answer is higher than 120.

## Data needed

| Need | Source | Status |
|------|--------|--------|
| Cost of each successive batch | Owner interview | → `data/prep-batch-costs.csv` |
| Price | Menu | $14 |
| Fixed daily cost | Owner's lease and permit | $300 |

## Capability

[marginal-analysis](../../capabilities/marginal-analysis/)
