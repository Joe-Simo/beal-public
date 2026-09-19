"""Pairwise combination screen for active candidate pairs in cycle 101+.
Tests compatibility, combination value, and shared failure modes using Jev.
"""
from __future__ import annotations
import itertools
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "code"))
import jev

CANDS = [
    {
        "id": "C264",
        "name": "Formal Immersion at Cusps for Levels 72 and 144",
        "text": "Formal immersion of X_0(72) and X_0(144) into Eisenstein quotients J_e(N) (rank 0) at cusps infinity and 0 to bound prime exponents p where Frey curve E_{A,B} has rho_{E,p} ~ f.",
    },
    {
        "id": "C265",
        "name": "Ellenberg Frey Q-Curve Descent for (2, 4, p)",
        "text": "Ellenberg Frey Q-curve descent for A^2 + B^4 = C^p over Q(i) to Hilbert modular newforms over Q(i) and modular Kraus sieve.",
    },
    {
        "id": "C266",
        "name": "Extended Kraus Sieve for (3, 3, p) on [1701, 1800]",
        "text": "Exact modular Kraus multi-modulus sieve for signature (3, 3, p) across primes p in [1701, 1800], eliminating levels 72 and 144 via auxiliary primes l = 2*k*p + 1.",
    },
    {
        "id": "C267",
        "name": "Arakelov Intersection and Uniform Bounds",
        "text": "Arakelov intersection theory and height bounds on modular curves X_0(N) to obtain uniform bounds on exponents p for Frey representations.",
    },
]

COMBINE_Q = {
    "compatible": jev.noul(
        "Are these two research candidates mathematically COMPATIBLE, in the sense that the objects, fields, exponents and equations they concern are the same or are related by a reduction that the project has already proved?",
        true="they concern the same equation, signature, curve or field, or one supplies an input the other consumes",
        false="they concern unrelated equations, signatures or methods, so no joint statement could be formed without inventing a new reduction",
    ),
    "combination_value": jev.score(
        "If these two candidates were combined into a single line of attack, how much would the combination accomplish beyond what the better of the two accomplishes alone?",
        [
            "level 0: nothing; the combination is just the stronger candidate restated, or they are incompatible",
            "level 1: the combination tidies bookkeeping but resolves no obligation that either one leaves open",
            "level 2: one candidate discharges a specific open obligation recorded in the other",
            "level 3: the combination closes a case or an infinite family that neither one closes alone",
        ],
    ),
    "shared_failure": jev.noul(
        "Would these two candidates FAIL FOR THE SAME REASON, so that combining them adds no diversity of failure mechanism and a single obstruction would defeat both?",
        true="both depend on the same blocked step, the same unverified citation, or the same one of the three recorded failure modes",
        false="they would fail for different reasons, so each provides genuine independent information",
    ),
}

def main():
    pairs = list(itertools.combinations(CANDS, 2))
    print(f"Running pairwise combination screen on {len(pairs)} pairs...")

    states = [
        f"CANDIDATE 1 ({p1['id']}): {p1['name']}\n{p1['text']}\n\nCANDIDATE 2 ({p2['id']}): {p2['name']}\n{p2['text']}"
        for p1, p2 in pairs
    ]

    results = jev.ask_many(states, COMBINE_Q, concurrency=6)

    evidence_dir = REPO / "research" / "pool" / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)

    print("\n" + "=" * 80)
    print(f"{'Pair':<15} | {'Compatible':<12} | {'Comb Value':<12} | {'Shared Failure':<15}")
    print("-" * 80)

    for (p1, p2), res in zip(pairs, results):
        pair_id = f"{p1['id']}_{p2['id']}"
        ev_file = evidence_dir / f"pairwise_{pair_id}.json"
        ev_file.write_text(json.dumps({"pair": [p1["id"], p2["id"]], "jev": res}, indent=2))

        ans = res.get("answers", {})
        comp = ans.get("compatible", {}).get("noul", "?")
        val = ans.get("combination_value", {}).get("score", "?")
        fail = ans.get("shared_failure", {}).get("noul", "?")

        print(f"{pair_id:<15} | {str(comp):<12} | {str(val):<12} | {str(fail):<15}")
    print("=" * 80)

if __name__ == "__main__":
    main()
