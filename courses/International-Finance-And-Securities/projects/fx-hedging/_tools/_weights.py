"""Single source of truth for FX-hedging (v2) grade weights.

Everything is a percentage, nothing is a hardcoded point total. The rationale
(Adam, 2026-07): the project's absolute contribution to the semester course
grade is *variable* and set in the LMS gradebook — so a weight here should
never need touching when that contribution changes. A stage is a % of the
project; a criterion is a % of its stage.

Consumed by grade_stage{0..5}.py (and the offering README's weight table).

    from _weights import STAGE_WEIGHTS, CRITERIA_WEIGHTS, stage_pct, criterion_pcts

Design decisions locked with Adam:
  - Keep the draft's *relative* weighting (repo 2 / memo 4 / spec 5 / build 4 /
    data 3 / capstone 6 out of 24), expressed as % that sum to 100.
  - No extra credit — the six stages are the whole grade.
"""
from __future__ import annotations

# --- Stage weights: % of the project (sum == 100) -------------------------
# Derived from the draft's 2/4/5/4/3/6-of-24 points, rounded to whole % that
# still sum to 100 (max drift 0.9pp from the exact fractions).
STAGE_WEIGHTS: dict[int, int] = {
    0: 8,    # Portfolio repository (repo setup)
    1: 17,   # Executive memo
    2: 21,   # Model specification
    3: 17,   # AI-assisted build + audit
    4: 12,   # Market data + population
    5: 25,   # LLM analysis & validation (capstone)
}

# --- Criteria weights: % of the *stage* (each inner dict sums to 100) ------
# Keys mirror each stage doc's Evaluation table, top to bottom.
CRITERIA_WEIGHTS: dict[int, dict[str, int]] = {
    0: {
        "public_accessible": 25,   # Public, professionally named, URL submitted
        "skeleton_readmes": 25,    # Canonical structure + stub READMEs + prompt-log
        "bio_resume": 25,          # Recruiter-ready, edited beyond raw LLM
        "commit_hygiene": 25,      # >=2 meaningful commits
    },
    1: {
        "exposure_framing": 25,    # Currency, amount, timing, consequence
        "hedge_families": 25,      # Forward / MM / options with honest trade-offs
        "next_steps": 25,          # Frames the Stage 2-5 arc
        "professionalism": 25,     # Tone, template, location/filename, committed
    },
    2: {
        "named_range_contract": 30,      # Inputs table + tab architecture
        "calculation_flow": 30,          # All three hedge families, named-range notation
        "validation_sensitivity": 20,    # Check figures + sensitivity plan
        "reproducibility_prompt": 20,    # Context-free buildable + HIL iteration logged
    },
    3: {
        "contract_compliance": 50,       # Named ranges + formulas-only (mechanical) + hedges/sensitivity
        "structure_presentation": 25,    # Cover, legend/key, color convention, layout
        "audit_note": 25,                # >=3 substantive findings with committed fixes
    },
    4: {
        "data_provenance": 50,           # Every input sourced, timestamped, proxies documented
        "model_resolves": 33,            # Live data loads cleanly; checks pass; fixes honest
        "lab_crosscheck": 17,            # FX Hedging Lab comparison performed + resolved
    },
    5: {
        "llm_execution_comparison": 25,  # Clean two-doc run; discrepancies diagnosed
        "hand_verification": 25,         # >=3 outcomes recomputed with arithmetic
        "recommendation_voice": 25,      # Data-supported, decision-ready, CFO voice
        "spec_retrospective": 17,        # Specific, honest, ties LLM failures to spec gaps
        "repo_polish": 8,                # Portfolio-ready repo
    },
}


def _validate() -> None:
    assert sum(STAGE_WEIGHTS.values()) == 100, (
        f"stage weights must sum to 100, got {sum(STAGE_WEIGHTS.values())}"
    )
    for stage, crit in CRITERIA_WEIGHTS.items():
        assert sum(crit.values()) == 100, (
            f"stage {stage} criteria must sum to 100, got {sum(crit.values())}"
        )
    assert set(STAGE_WEIGHTS) == set(CRITERIA_WEIGHTS), "stage keys must match"


def stage_pct(stage: int) -> int:
    """Return the stage's weight as a % of the project."""
    return STAGE_WEIGHTS[stage]


def criterion_pcts(stage: int) -> dict[str, int]:
    """Return the stage's criteria weights as % of the stage."""
    return dict(CRITERIA_WEIGHTS[stage])


_validate()

if __name__ == "__main__":
    print("FX-hedging v2 grade weights (% of project):")
    for s, w in STAGE_WEIGHTS.items():
        print(f"  Stage {s}: {w:>3}%   criteria: {CRITERIA_WEIGHTS[s]}")
    print(f"  Total: {sum(STAGE_WEIGHTS.values())}%")
