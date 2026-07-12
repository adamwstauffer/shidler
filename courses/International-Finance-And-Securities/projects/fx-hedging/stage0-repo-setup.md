# Stage 0 – Portfolio Repository (8% of project)

## Goal

Stand up (or restructure) your **public GitHub portfolio repository** before analytical work
begins. Every deliverable in this project is committed here; by the end of the term the repo is
a portfolio piece you can put on a resume. This stage removes all tooling friction now, so later
stages are about finance, not Git.

**Already have a portfolio repo from BUS 313/314?** You don't start over — your task is to
restructure it to the canonical skeleton below and add anything missing. Same rubric applies.

---

## Steps

1. **GitHub account** — use your `hawaii.edu` email (unlocks GitHub Education benefits). If you
   have a personal account, add the .edu email to it instead of creating a second account.
2. **Install GitHub Desktop** — no command line required for this course.
3. **Create the repository** — public, named professionally after *you*, not a course:
   `firstname-lastname` (or `firstname-lastname-portfolio` if the plain name is taken). Resist a
   course- or finance-scoped name: this repo outlives any one class — it collects your BUS 313/314,
   FIN 321, and career docs — and its name is the first thing an employer reads, so name it for the
   person, not the subject.
4. **Build the canonical skeleton** — every folder gets a stub `README.md` (one or two lines
   saying what belongs there):

   ```
   [repo-name]/
   ├── README.md                  # Bio — first thing visitors see
   ├── RESUME.md                  # Resume
   ├── BIO.md                     # Optional longer-form bio
   ├── prompt-log.md              # Running log of AI prompts used, updated every stage
   ├── docs/
   │   ├── README.md
   │   ├── decisions/             # Memos and decision documents (Stages 1, 5)
   │   ├── specs/                 # Technical specifications (Stage 2)
   │   ├── plans/                 # Optional project plans / timelines
   │   └── templates/             # Stub README pointing at canonical course templates
   ├── models/
   │   ├── README.md              # Explains templates/ vs. builds/
   │   ├── templates/             # Blank model frameworks
   │   └── builds/                # Populated, working models (Stages 3–4)
   ├── data/                      # Market data + provenance notes (Stage 4)
   │   └── README.md
   └── analysis/                  # Audit and validation work (Stages 3, 5)
       └── README.md
   ```

   Do **not** copy course templates into `docs/templates/` — its README links to the canonical
   templates in the course repo. One source of truth; no stale copies.
5. **Draft your bio and resume** — use an LLM as the drafter and yourself as the editor; log the
   prompts in `prompt-log.md`. The bio `README.md` is what a recruiter sees first.
6. **Commit and push** — at least **2 meaningful commits** with descriptive messages
   (e.g., `Add repo skeleton with directory READMEs`, `Add bio and resume`), not `update`.

---

## Deliverable

Your repository URL, submitted via Lamaku. Graded by direct repo inspection.

## Evaluation

| Criterion | Description | Weight |
| --------- | ----------- | -----: |
| Public & accessible | Repo is public, professionally named, URL submitted | 25% |
| Skeleton & READMEs | Canonical structure complete; stub README in every folder; `prompt-log.md` present | 25% |
| Bio & resume | Clear, professional, recruiter-ready; evidence of editing beyond raw LLM output | 25% |
| Commit hygiene | ≥2 meaningful commits with descriptive messages | 25% |

---

## How this leads to Stage 2

Your stage 1 memo (already written) gets committed to `docs/decisions/`. Stage 2's specification
lands in `docs/specs/`. From here on, "submit" means "commit and push" — version control is a
professional skill you practice by default, not a submission mechanism.
