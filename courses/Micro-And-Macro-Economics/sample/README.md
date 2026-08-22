# firstname-lastname

> **This is a sample, not a student repository.** It is a working copy of the
> [portfolio repo standard](https://adamwstauffer.github.io/ai-lms/portfolio-repo.html) — the
> skeleton [Stage 0, part 2](https://adamwstauffer.github.io/ai-lms/github-stage0.html) asks you to
> stand up under your **own** GitHub account, named for you. Browse it to see what the structure
> looks like once it exists. Do not fork it, and do not copy the placeholder prose: the bio is the
> first thing any reader sees, and generic filler is obvious.
>
> Everything below this line is what *your* `README.md` would hold.

---

<!-- PLACEHOLDER — replace with three to six sentences on who you are, what you have done,
     and what you are working toward. Write it in your own voice; an LLM may draft it, but
     ship nothing you would not want read aloud. -->

*Three to six sentences on who you are and what you are working toward go here.*

## Engagements

The index is the by-subject view of this repository — it lives here, never in the folder paths.
Each row links a piece of work to its brief, its analysis, and its memo.

| Engagement | Capability | Brief | Analysis | Memo |
|---|---|---|---|---|
| *(engagement name)* | [`marginal-analysis`](capabilities/marginal-analysis/) | `docs/briefs/` | `analysis/` | `docs/decisions/` |

## Structure

```
firstname-lastname/
├── README.md            who you are + the index of engagements
├── RESUME.md            Markdown resume
├── AGENTS.md            your AI conventions — the canonical file
├── CLAUDE.md            one line pointing to AGENTS.md
├── prompt-log.md        the running record of AI sessions that mattered
├── .gitignore           what must never enter the history
├── .claude/skills/      personal sandbox — yours to experiment with, ungraded
├── capabilities/        one folder per capability
│   └── marginal-analysis/
│       ├── README.md    what the capability is + which engagements exercised it
│       ├── spec.md      the method: model design, named ranges, formula logic
│       └── model.xlsx   starts as a template, becomes your model
├── docs/
│   ├── briefs/          BEFORE the work: scope + hypothesis
│   └── decisions/       AFTER the work: the recommendation, to an audience
├── data/                sourced inputs, with provenance
└── analysis/            the findings
    └── figures/         charts the findings refer to
```

Three distinctions carry the whole structure:

- **Briefs ask; memos answer.** A brief is written *before* the work and commits you to a
  hypothesis you can be wrong about. A brief written afterwards is a summary of the answer.
- **Capabilities are what you can do; engagements are evidence.** `capabilities/` holds the
  method; `docs/`, `data/`, and `analysis/` hold the proof you exercised it.
- **The spec and the model live together.** A method and the workbook implementing it are one
  object — splitting them into a `specs/` folder creates two places to look and no payoff.

## Two mechanical facts

**Git tracks files, not folders.** An empty directory does not survive a push. Every directory
here holds a one-line `README.md` for exactly that reason — which is more useful to a reader
than an empty folder anyway.

**History is permanent.** A file committed once stays in the history after it is deleted. That
is why `.gitignore` goes in *before* the first workbook, and why credentials never get committed
even briefly.

## Naming

- Repository named for the person — `firstname-lastname`, or `firstname-lastname-portfolio` if
  taken. Never for a course, a semester, or a week.
- Files named for the engagement: `perfect-competition-brief.md` still makes sense to a stranger
  in three years; `week1.md` does not.
- Slugs lowercase and hyphen-separated, three to six words. No spaces, no underscores.
- Dated documents lead with the ISO date — `YYYY-MM-DD-slug.md` — so a listing sorts itself.
