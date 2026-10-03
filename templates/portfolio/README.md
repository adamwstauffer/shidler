# Portfolio Templates

Professional bio and resume templates for student GitHub portfolios. These are the foundation for the public repos students build in BUS-629 (Stage 0) and any other course that asks for a portfolio artifact.

## Why a GitHub portfolio?

- **Version control:** Track changes as your bio and resume evolve.
- **Portfolio showcase:** Your resume sits alongside your projects.
- **Public or private:** Share with a link or keep private until ready.
- **Easy export:** Print or save to PDF anytime.

A public repo named `firstname-lastname` (your own first and last name) puts your bio, resume, and project work behind one link.

---

## Files in this directory

| File | Purpose |
|------|---------|
| [`bio-template.md`](./bio-template.md) | Bio assignment + iterative-revision prompt library |
| [`resume-template.md`](./resume-template.md) | Resume skeleton (Penn-style format) |
| [`firstname-lastname/`](./firstname-lastname/) | The one sample student repository, filled in with fictional work |

---

## Suggested student repo structure

```markdown
firstname-lastname/
├─ README.md            # Your bio (what visitors see first)
├─ RESUME.md            # Your resume in Markdown
├─ AGENTS.md            # Conventions for any AI agent working in the repo
├─ CLAUDE.md            # One line pointing to AGENTS.md
├─ prompt-log.md        # Your AI prompt log
├─ capabilities/        # What you can do, one folder per capability
├─ docs/                # Briefs and decision memos
├─ data/                # Source data, with provenance in data/README.md
└─ analysis/            # Findings and figures
```

The [`firstname-lastname/`](./firstname-lastname/) sample shows each of these filled in.

---

## Workflow

### Part 1 — Create your bio

1. Create a public GitHub repo named `firstname-lastname` (your own first and last name).
2. The default `README.md` is your **bio** — the first thing a visitor sees.
3. Use [`bio-template.md`](./bio-template.md) as the structural starting point. It gives a 200–400 word structure. You write the draft yourself; AI may then review it for clarity and flag claims you cannot back.
4. Aim for at least **two iterations** before submitting — this is where the writing skill develops.

### Part 2 — Add your resume

1. In the same repo, create a `RESUME.md` file.
2. Use [`resume-template.md`](./resume-template.md) — fill in education, professional experience, leadership, honors, skills.
3. Keep bullets **short, action-oriented, and quantifiable**:
   - ✅ "Developed Excel tool to model $50,000 in cost savings"
   - ❌ "Worked on Excel project"

### Part 3 — Export to PDF

1. Open `RESUME.md` in GitHub and click **Raw**.
2. Browser print → Save as PDF.
   - **Mac:** ⌘ + P → Destination → Save as PDF
   - **Windows:** Ctrl + P → Destination → Save as PDF
3. Save as `firstname-lastname-resume.pdf`.

---

## Best practices

- **Keep it updated:** Commit changes whenever you gain experience.
- **Use branches:** A `job-specific` branch lets you tailor for a specific application without losing the master copy.
- **Link to it:** Add the GitHub URL to your LinkedIn and email signature.
- **One page** if possible.
- **Quantify results** when possible.
- Delete sections that don't apply — don't leave them blank.

---

## Resources

- [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)
- [GitHub Pages](https://pages.github.com/) — turn your portfolio into a website
- [Penn Career Services Resume Guide](https://careerservices.upenn.edu/channels/resume/)
- [Penn Sample Resumes](https://careerservices.upenn.edu/preparing-effective-resumes/undergraduates-student-resume-samples/)
- [Sample Consulting Resume (PDF)](https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2021/09/SampleConsultingResume.pdf)
