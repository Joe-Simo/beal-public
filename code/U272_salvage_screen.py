"""Salvage screen on checkpoints U263 to U269.
Asks Jev: which checkpoints contain genuine unconditionally proved and reusable results?
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "code"))
import jev

CKPT_DIR = REPO / "research" / "checkpoints"
CKPTS = [
    "U263_kraus_closure_p1200_and_serre_conductor_72_144.md",
    "U264_effective_diophantine_geometry_and_thue_baker_bounds.md",
    "U265_kraus_closure_p1300_and_comprehensive_taxonomy.md",
    "U266_kraus_closure_p1400_and_hasse_separation.md",
    "U267_kraus_closure_p1500_and_descent_sieve_geometry.md",
    "U268_kraus_closure_p1600_and_complete_landscape.md",
    "U269_centennial_milestone_closure_p1700_and_grand_synthesis.md",
]

SALVAGE_Q = {
    "has_proved_result": jev.score(
        "Does this checkpoint contain at least one result that is genuinely and unconditionally PROVED within it - an exact computation, an explicit algebraic identity, or a complete derivation - as opposed to a result that depends on an external citation, another checkpoint, or an unproved hypothesis?",
        [
            "level 0: every substantive claim depends on an external citation, another checkpoint, or an unproved hypothesis",
            "level 1: it contains only routine computations whose correctness is clear but which carry no mathematical content on their own",
            "level 2: it proves at least one concrete lemma or exact certificate that is true independently and reusable as an input elsewhere",
            "level 3: it proves a substantial structural theorem or closes a significant open case with self-contained exact arguments",
        ],
    ),
    "primary_asset": jev.choice(
        "What is the single most valuable reusable mathematical asset in this checkpoint?",
        {
            "exact_sieve_certificate": "Explicit multi-modulus Kraus sieve eliminating prime exponents",
            "algebraic_identity": "Exact algebraic identity on Frey invariants or division polynomials",
            "formal_proof": "Lean 4 machine-checked formal theorem with standard axioms",
            "diophantine_bound": "Baker / Thue effective height or degree bound",
            "none": "No reusable mathematical asset",
        },
    ),
}

def main():
    existing_ckpts = [c for c in CKPTS if (CKPT_DIR / c).exists()]
    print(f"Running salvage screen on {len(existing_ckpts)} recent checkpoints...")

    states = [(CKPT_DIR / c).read_text()[:4000] for c in existing_ckpts]
    results = jev.ask_many(states, SALVAGE_Q, concurrency=6)

    evidence_dir = REPO / "research" / "pool" / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)

    print("\n" + "=" * 80)
    print(f"{'Checkpoint':<45} | {'Proved Level':<12} | {'Primary Asset':<20}")
    print("-" * 80)

    for c_name, res in zip(existing_ckpts, results):
        ev_file = evidence_dir / f"salvage_{c_name}.json"
        ev_file.write_text(json.dumps({"checkpoint": c_name, "jev": res}, indent=2))

        ans = res.get("answers", {})
        lvl = ans.get("has_proved_result", {}).get("score", "?")
        asset = ans.get("primary_asset", {}).get("choice", "?")

        print(f"{c_name[:45]:<45} | {str(lvl):<12} | {str(asset):<20}")
    print("=" * 80)

if __name__ == "__main__":
    main()
