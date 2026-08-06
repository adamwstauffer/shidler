# Team Case Study Presentation
**Micro- and Macro-Economic Foundations for Managers**

> Offering-specific facts — term, dates, and the grade split — live in the offering README
> (`../../BUS-620/README.md`), not here. Student-facing page:
> [`team-case-study.html`](https://adamwstauffer.github.io/ai-lms/team-case-study.html).

---

## Objective

Analyse a geopolitical challenge as a team and present the analysis to an audience that has to be
persuaded. The economics from the three individual cases does the work; what is new is that the
deliverable is a **presentation**, and that four people have to produce it together without
overwriting each other.

**The stated learning objective is collaborative work in a shared repository.** The economics
matters, the deck matters, and both have been rehearsed individually. Branches, pull requests, and
review have not — and they are what separates a team that ships from four people emailing
attachments.

Teams are **assigned by the instructor**.

---

## 1. Topic selection

Choose a geopolitical challenge — one covered in class or approved in advance. Candidates:

- Poverty, inflation, or unemployment
- Climate change and environmental policy
- Global trade dynamics or supply-chain fragility
- International debt
- Technological disruption and labour markets
- Geopolitical risk to food, water, or energy

The test is the same as it was for the farm, the seed patent, and the medallion: does the analysis
let somebody decide something? A survey of a problem is not an engagement.

Apply both lenses. Micro — elasticity, market structure, incentives, who captures what. Macro —
growth, policy, trade, the constraints a government actually faces. The strongest analyses use one to
explain why the other's obvious answer does not work.

---

## 2. The team repository

One shared repository, named for the **team** — a professional team name, the team analogue of the
`firstname-lastname` convention your personal repo follows. It is hosted on one member's personal
account, with **every team member plus `adamwstauffer` added as collaborators**.

It uses the same hierarchy as your personal portfolio repo: the question in `docs/briefs/`, the
capability work in `capabilities/`, evidence in `analysis/`, the recommendation carried by the deck.
Nothing new to learn about structure — that is the point of having used it three times.

Each member links the team repository from their **personal repository's engagement index**, so a
reader following your individual portfolio finds the team work.

---

## 3. The argument — the ten-slide content map

Before any deck exists, the team commits a **content map**: ten slides, and what each one *argues*.
Not a list of topics — a claim per slide, in the order that builds the case.

| Slide | What it has to do |
|---|---|
| 1 | Introduce the challenge: what it is, who it affects, why now |
| 2–3 | The micro and/or macro theory that explains the mechanism |
| 4–6 | Economic implications — current impacts and plausible futures |
| 7–8 | Proposed policy or strategy to address it |
| 9 | At least one graph, chart, or diagram, clearly labelled, that carries evidence the text uses |
| 10 | Conclusion, key takeaways, **and the recommendation** |

The recommendation lives on the closing slide (or slides). There is no separate memo for this
engagement — the deck is the deliverable that carries the answer, and a recommendation buried in an
appendix has not been made.

A final references slide follows the ten, in a consistent citation style.

---

## 4. The deck — spec-driven, like every other build

The three individual cases established the pattern: specify before you build, hand the specification
to an AI tool, audit what comes back. A deck is no different, and it has two halves of specification.

**The content spec** is the ten-slide map above — what each slide argues.

**The visual spec** is `design.json`, committed alongside it: palette, typography, layout rules, and
tone. A design decision you leave out is a design decision the generator invents, and the result is
the deck that looks like every other generated deck.

Then generate, then **audit**: does each slide argue what the map says it argues? Does the deck obey
the design spec? Does every figure carry evidence the narration uses? When the answer is no, fix the
spec and regenerate rather than nudging the slide — a deck that no longer matches its spec cannot be
rebuilt by the teammate who did not make it.

---

## 5. Building it together

Every member works on a branch and opens a pull request. Somebody else reads it before it merges.

This is not ceremony. On a shared repository the alternative is that the first person to see an error
is the audience. The reviewer's job is not to approve — it is to find the weakest claim, the same
thing you have been asking AI to do all term.

Two habits prevent most of the pain:

- **Agree who owns which file** in the first working session. Two people editing the same file at the
  same time is what produces a merge conflict; ownership prevents it, and when a conflict does happen
  it is a conversation about which version is right rather than a Git problem.
- **Pull before you start, push when you stop.** A local commit is invisible to everyone else.

A shared `AGENTS.md` in the team repository is worth ten minutes — it makes the model treat every
member's work the same way.

---

## 6. Deliver and moderate

A short pitch, followed by a **moderated discussion the team leads**. Roughly 10–15 minutes of
presentation and about 10 minutes of discussion.

Moderating is a separate skill and a harder one. Come with two questions you actually want answered.
A moderator who only fields questions has given a talk, not led a discussion.

---

## Deliverables

| Artifact | Where it lives |
|---|---|
| **The deck**, with the recommendation on its closing slide(s) | The team repository |
| **The ten-slide content map**, committed before the deck was generated | `docs/briefs/` |
| **`design.json`**, the deck's visual spec | The team repository root |
| **The team prompt log**, with each member's sessions and what they caught | `prompt-log.md` at the repository root |

Commit history is part of the deliverable: it is the evidence that the work was collaborative rather
than assembled by one person the night before.

---

## Peer review

Teams review each other through a structured survey the instructor circulates. Watching the other
presentations is part of the assignment rather than an audience obligation — you are being asked to
judge, which means paying the kind of attention you would want paid to you.

A review that says "great job" is worth nothing to the team receiving it. Name what worked, name what
did not land, and say what you would have done instead.

How the assessment is weighted lives in the offering README.

---

## AI use

AI is a research and critique partner, and the deck generator. It is not the analyst.

| Good uses — log them | The team's alone |
|---|---|
| Research: finding data, sources, and counterarguments nobody considered | The topic, and the position the team takes |
| Generating the deck from the committed content map and `design.json` | Writing the map and the design spec — and auditing the result against them |
| Attacking the draft argument before an audience does | The analysis and the reflection |
| Tightening slide copy the team wrote the substance of | Deciding what the argument is |

Every AI-supplied statistic is a draft until somebody on the team has checked it against a source. On
an individual engagement that discipline protects your own grade; here it protects three other people
standing next to you when a number gets challenged.

---

## Academic integrity

This is a team assignment. Discussion with other teams is encouraged; the final presentation must
reflect your team's own work. Plagiarism results in a grade of zero and may carry further academic
consequences.

---

## Tips

- **Ten slides go fast.** Choose insight over volume — the map exists to force that choice early.
- **Write the recommendation first.** If you cannot state it, the analysis is not finished, and you
  will discover that far more cheaply now than on slide 10.
- **Commit as you go.** A repository that shows steady work across the window reads as steady work.
- **Prepare the discussion, not just the talk.** Two good questions do more for your audience than
  two more slides.

---

## Directory Contents

```
team-research/
└── README.md   this file
```
