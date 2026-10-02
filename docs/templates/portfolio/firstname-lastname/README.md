# Firstname Lastname

> **Sample repo for in-class demo.** Every name, number, and engagement here is fictional. Copy the
> *shape*, not the content.

MBA candidate, Shidler College of Business (University of Hawaiʻi at Mānoa). I use spreadsheets,
written specs, and AI tools to turn messy operating questions into decisions a manager can act on.

- Résumé: [RESUME.md](RESUME.md)
- How I work with AI: [AGENTS.md](AGENTS.md) · [prompt-log.md](prompt-log.md)

## Engagements

Each engagement is one question, answered end to end: a **brief** written *before* the work, a
**decision** written *after* it, and the capability, data, and analysis that connect the two.

| # | Question | Brief (before) | Decision (after) | Capability |
|---|----------|----------------|------------------|------------|
| 1 | How many lunch plates should the food truck prep each day? | [brief](docs/briefs/2026-10-02-lunch-plate-volume.md) | [decision](docs/decisions/2026-10-09-lunch-plate-volume.md) | [marginal-analysis](capabilities/marginal-analysis/) |

## Capabilities

| Capability | What it does | Files |
|------------|--------------|-------|
| [marginal-analysis](capabilities/marginal-analysis/) | Finds the output level where marginal revenue stops covering marginal cost | README · spec · model.xlsx |

## Repo map

```text
firstname-lastname/
  README.md            who you are + the index of engagements   ← you are here
  RESUME.md
  AGENTS.md            your AI conventions — the canonical file
  CLAUDE.md            one line pointing to AGENTS.md
  prompt-log.md        the running record of AI sessions that mattered
  .gitignore           what must never enter the history
  .claude/skills/      personal sandbox
  capabilities/        one folder per capability
    marginal-analysis/
      README.md · spec.md · model.xlsx
  docs/
    briefs/            BEFORE the work: scope + hypothesis
    decisions/         AFTER the work: the recommendation
  data/                sourced inputs, with provenance
  analysis/figures/    the findings, and the charts they refer to
```
