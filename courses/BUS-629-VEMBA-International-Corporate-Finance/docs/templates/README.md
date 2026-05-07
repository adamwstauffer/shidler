# Templates

This directory exists in the BUS-629 course tree as a **structural example** — it shows where templates live in a project repo so you can mirror the same layout in your own portfolio repo.

## The canonical templates live at the repo root

To avoid drift, BUS-629 does not maintain its own copies of the memo and spec templates. The single source of truth is at the repository root:

- **Memo template:** [`../../../../docs/templates/memo-template.md`](../../../../docs/templates/memo-template.md)
- **Spec template:** [`../../../../docs/templates/spec-template.md`](../../../../docs/templates/spec-template.md)
- **Prompt log:** [`../../../../docs/templates/prompt-log-template.md`](../../../../docs/templates/prompt-log-template.md)
- **Portfolio (bio + resume):** [`../../../../docs/templates/portfolio/`](../../../../docs/templates/portfolio/)
- **Templates README** (frontmatter schema, naming conventions): [`../../../../docs/templates/README.md`](../../../../docs/templates/README.md)

When the underlying templates evolve, every course inherits the change automatically.

## What this directory means for your own repo

When you build your own `Corporate Finance` portfolio repo (Stage 0), you should create a parallel structure:

```
your-repo/
└── docs/
    ├── decisions/      # Memos and decision documents (was docs/memos/)
    ├── specs/          # Technical specifications
    ├── plans/          # Project plans
    └── templates/      # Your personal copies of any templates you adapt
```

Inside *your* `docs/templates/`, keep:

- A copy of any template you have customized for your own workflow
- A `README.md` (this file is a model) noting which templates are personal vs. inherited from upstream

If you have not customized a template, you do not need a copy — link directly to the canonical version at the repo root.

## File naming convention

All memos and specs across this repo follow:

```
YYYY-MM-DD-{slug}.md
```

Lowercase slug, hyphen-separated, ISO date prefix so files sort chronologically. See the [repo-level templates README](../../../../docs/templates/README.md#file-naming-conventions) for the full table.

## YAML frontmatter

Every template has a YAML frontmatter block declaring `template`, `purpose`, `audience`, `fields_required`, and `naming_convention`. When you adapt a template, keep the frontmatter intact — tooling (and the LLM-spec workflow at Stage 4) reads it.
