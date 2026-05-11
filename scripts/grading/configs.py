"""Course configs for the final-grade pipeline.

Each entry maps category -> column header *substring* (case-insensitive).
Substring match is used so configs survive minor header tweaks across
semesters. If a Brightspace export changes column names materially, update
the relevant substring here.

Letter-grade scale and EC treatment are shared across all courses.
"""

LETTER_SCALE = [  # (min_percent, letter), evaluated top-down
    (97, 'A+'), (93, 'A'), (90, 'A-'),
    (87, 'B+'), (83, 'B'), (80, 'B-'),
    (77, 'C+'), (73, 'C'), (70, 'C-'),
    (67, 'D+'), (65, 'D'),
]
LETTER_FALLBACK = 'F'

# Weights used to cap each component (component_max == its % weight).
DEFAULT_WEIGHTS = {
    'attendance': 10,
    'homework': 20,
    'project': 20,
    'midterm': 25,
    'final_exam': 25,
}

FINAL_CAP = 100  # MIN(100, ROUNDUP(total, 0))


def _hw_pairs(orig_pat, makeup_pat):
    """Build a chapter-pair config from two patterns."""
    return {'original': orig_pat, 'makeup': makeup_pat}


COURSES = {
    # ------------------------------------------------------------------
    # BUS-313 — Economic & Financial Environment of Global Business
    # 16 chapters, original max 1.25, makeup max 1.0; team project (20)
    # plus team project EC (3); attendance (10); midterm/final (25 each).
    # ------------------------------------------------------------------
    'BUS-313': {
        'attendance': 'Attendance Points',
        'midterm': '313 Midterm',
        'final_exam': '313 Final',
        'project': ['Team Project 20'],   # list -> sum of these columns
        'extra_credit': [
            ('Professional Profile', 2.5),
            ('Team Project (EC)', 3.0),
        ],
        # Chapter detection: find paired (orig, makeup) by chapter number.
        # Headers like "Ch. 1 -" / "Chapter 10 -" / "Chapter 17 -" all OK.
        'chapter_prefix_re': r'^(?:Ch\.?|Chapter)\s*(\d+)',
        'makeup_marker': '(makeup)',  # case-insensitive substring
    },

    # ------------------------------------------------------------------
    # FIN-321 — International Finance & Securities
    # 15 chapters, original max 1.33, makeup max 1.06–1.6 (varies);
    # AI + GitHub Project = sum of Stage 1 memo, Stage 3 spec, Stage 3
    # Excel, Stage 4 memo, GitHub Setup, Spec Driven Design (capped at 20).
    # ------------------------------------------------------------------
    'FIN-321': {
        'attendance': 'Attendance Points',
        'midterm': '321 Midterm',
        'final_exam': '321 Final',
        'project': [
            'Stage 1 - Memo',
            'Stage 3 - Spec',
            'Stage 3 - Excel',
            'Stage 4 - Recommendation',
            'GitHub Setup',
            'Spec Driven Design',
        ],
        'extra_credit': [
            ('Professional Profile', 2.5),
        ],
        'chapter_prefix_re': r'^(?:Ch\.?|Chapter)\s*(\d+)',
        'makeup_marker': '(makeup)',
    },

    # ------------------------------------------------------------------
    # BUS-314 — International Corporate Finance
    # 16 chapters, original max 1.25, makeup max 1.0–1.18 (varies);
    # Individual Project = Stage 1+2+3+4 GitHub stages (sum max = 20).
    # ------------------------------------------------------------------
    'BUS-314': {
        'attendance': 'Attendance Points',
        'midterm': '314 Midterm',
        'final_exam': '314 Final',
        'project': [
            'Stage 1 - GitHub Decision Memo',
            'Stage 2 - GitHub Excel',
            'Stage 3 - GitHub Specification',
            'Stage 4 - GitHub Final Analysis',
        ],
        'extra_credit': [
            ('Professional Profile', 2.5),
        ],
        'chapter_prefix_re': r'^(?:Ch\.?|Chapter)\s*(\d+)',
        'makeup_marker': '(makeup)',
    },
}
