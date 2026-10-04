# Courses

Directories here are named by subject, not by course code, since some subjects are taught under more than one code to different populations. This table maps every active course code to its directory.

| Code | Level / Population | Subject Directory |
|---|---|---|
| BUS 313 | Undergrad | [`International-Economics-And-Trade/`](International-Economics-And-Trade/) → [`BUS-313/`](International-Economics-And-Trade/BUS-313/) |
| BUS 314 | Undergrad (archived; not on the public tree) | [`International-Corporate-Finance/`](International-Corporate-Finance/) |
| BUS 620 | MBA | [`Micro-And-Macro-Economics/`](Micro-And-Macro-Economics/) → [`BUS-620/`](Micro-And-Macro-Economics/BUS-620/) |
| BUS 620 DLEMBA | Distance EMBA | [`Micro-And-Macro-Economics/`](Micro-And-Macro-Economics/) → [`BUS-620-DLEMBA/`](Micro-And-Macro-Economics/BUS-620-DLEMBA/) |
| BUS 629 | Vietnam EMBA | [`International-Corporate-Finance/`](International-Corporate-Finance/) → [`BUS-629-VEMBA/`](International-Corporate-Finance/BUS-629-VEMBA/) |
| FIN 321 | Upper undergrad | [`International-Finance-And-Securities/`](International-Finance-And-Securities/) → [`FIN-321/`](International-Finance-And-Securities/FIN-321/) |
| BUS 122B | Community college (Windward) | [`Windward-Community-College/`](Windward-Community-College/) → [`BUS-122B-…/`](Windward-Community-College/BUS-122B-Intro-Entrepreneurship-Sustainable-Agriculture/) |

Every subject directory shares the same shape:

```
<Subject-Name>/
├── README.md          subject hub — this level of detail
├── projects/           shared curriculum: stage docs, analysis, deliverables, models, _templates/
└── <CODE[-POPULATION]>/  one per offering: syllabus and schedule
```

See [the 2026-07-08 decision memo](../docs/decisions/2026-07-08-generic-course-directory-naming.md) for the rationale behind this structure (it is the one decision memo kept in this repo; notable changes since are in [CHANGELOG.md](../CHANGELOG.md)). Deliverable templates are in [`templates/`](../templates/) at the repo root; setup how-tos are on [Kumu onboarding](https://adamwstauffer.github.io/ai-lms/onboarding.html).

## Directory Contents

```
courses/
├── International-Corporate-Finance/       BUS 314 (archived), BUS 629
│   ├── BUS-629-VEMBA/                      offering: syllabus
│   ├── projects/performance-ratios/        shared curriculum (6-stage)
│   └── README.md
├── International-Economics-And-Trade/     BUS 313
│   ├── BUS-313/                            offering: syllabus
│   └── README.md
├── International-Finance-And-Securities/  FIN 321
│   ├── FIN-321/                            offering: syllabus
│   ├── projects/fx-hedging/                shared curriculum (6-stage, Stage 0–5)
│   └── README.md
├── Micro-And-Macro-Economics/              BUS 620, BUS 620 DLEMBA
│   ├── BUS-620/                            offering: syllabus
│   ├── BUS-620-DLEMBA/                     offering: syllabus
│   ├── projects/                           case studies, individual-research/, team-research/
│   └── README.md
├── Windward-Community-College/             BUS 122B
│   └── BUS-122B-Intro-Entrepreneurship-Sustainable-Agriculture/
└── README.md                               you are here
```

Each subject README below has its own full downstream hierarchy.
