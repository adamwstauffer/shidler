# Courses

Directories here are named by subject, not by Shidler course code, since some subjects are taught under more than one code to different populations. This maps every active Shidler course code to its directory, grouped by subject.

### [International Corporate Finance](International-Corporate-Finance/)

| Shidler Code | Level / Population | Offering |
|---|---|---|
| BUS 629 | Masters — VEMBA | [`BUS-629-VEMBA/`](International-Corporate-Finance/BUS-629-VEMBA/) |
| BUS 314 | Undergrad (inactive) | [`BUS-314/`](International-Corporate-Finance/BUS-314/) |

### [International Economics and Trade](International-Economics-And-Trade/)

| Shidler Code | Level / Population | Offering |
|---|---|---|
| BUS 313 | Undergrad | [`BUS-313/`](International-Economics-And-Trade/BUS-313/) |

### [International Finance and Securities](International-Finance-And-Securities/)

| Shidler Code | Level / Population | Offering |
|---|---|---|
| FIN 321 | Upper undergrad | [`FIN-321/`](International-Finance-And-Securities/FIN-321/) |

### [Micro- and Macro-Economics](Micro-And-Macro-Economics/)

| Shidler Code | Level / Population | Offering |
|---|---|---|
| BUS 620 | Masters — MBA | [`BUS-620/`](Micro-And-Macro-Economics/BUS-620/) |
| BUS 620 DLEMBA | Masters — DLEMBA (in setup) | [`BUS-620-DLEMBA/`](Micro-And-Macro-Economics/BUS-620-DLEMBA/) |

### [Sustainable Agriculture Entrepreneurship](Sustainable-Agriculture-Entrepreneurship/)

| Shidler Code | Level / Population | Offering |
|---|---|---|
| BUS 122B | Community college | [`BUS-122B/`](Sustainable-Agriculture-Entrepreneurship/BUS-122B/) |

Every subject directory shares the same shape:

```
<Subject-Name>/
├── README.md          subject hub — this level of detail
├── projects/           shared curriculum: stage docs, analysis, deliverables, models, _templates/, _tools/
└── <CODE[-POPULATION]>/  one per offering: syllabus, roster, ignore/ (student data)
```

See `docs/decisions/2026-07-08-generic-course-directory-naming.md` for the rationale behind this structure.

## Directory Contents

```
courses/
├── International-Corporate-Finance/       BUS 314 (inactive), BUS 629
│   ├── BUS-314/                             offering: syllabus (inactive; materials at _archive/bus314/)
│   ├── BUS-629-VEMBA/                      offering: syllabus, roster
│   ├── projects/performance-ratios/        shared curriculum (6-stage)
│   └── README.md
├── International-Economics-And-Trade/     BUS 313
│   ├── BUS-313/                            offering: syllabus, _tools/
│   ├── projects/github-portfolio-extra-credit/
│   └── README.md
├── International-Finance-And-Securities/  FIN 321
│   ├── FIN-321/                            offering: syllabus
│   ├── projects/fx-hedging/                shared curriculum (5-stage)
│   └── README.md
├── Micro-And-Macro-Economics/              BUS 620, BUS 620 DLEMBA
│   ├── BUS-620/                            offering: syllabus
│   ├── BUS-620-DLEMBA/                     offering: syllabus (in setup)
│   ├── projects/                           individual-research/, team-research/, in-progress/
│   └── README.md
├── Sustainable-Agriculture-Entrepreneurship/  BUS 122B
│   ├── BUS-122B/                            offering: syllabus
│   └── README.md
└── README.md                               you are here
```

Each subject README below has its own full downstream hierarchy.
