"""Pairwise combination screen for Cycle 105+ candidates using Jev.
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
        "id": "C273",
        "name": "Kraus Sieve for (3, 3, p) on [1901, 2000]",
        "text": "Exact modular Kraus multi-modulus sieve for signature (3, 3, p) on primes p in [1901, 2000].",
    },
    {
        "id": "C274",
        "name": "Ellenberg Q-Curve Resolution for Small Primes p < 211",
        "text": "Elimination of open primes p in [5, 211] for A^2 + B^4 = C^p via Hilbert modular newforms over Q(i).",
    },
    {
        "id": "C275",
        "name": "Lean 4 Formal Statement Fidelity Audit",
        "text": "Audit of formal definitions in Beal.Signature3 and Beal.PostCentennial.",
    },
    {
        "id": "C276",
        "name": "Uniform Conductor Bound for Generalized Frey Varieties",
        "text": "Bounding the conductor of the minimal abelian variety quotient of J(C_{A, B, C}) uniformly.",
    },
]

COMBINE_Q = {
    "compatible": jev.noul(
        "Are these two candidates mathematically compatible and mutually reinforcing?",
        true="Compatible and reinforce each other",
        false="Incompatible or unrelated"
    ),
    "combination_value": jev.score(
        "What is the combination value of fusing these two candidates?",
        [
            "level 0: no synergy",
            "level 1: minor bookkeeping synergy",
            "level 2: discharges an open obligation in the other",
            "level 3: provides a breakthrough bridge"
        ]
    ),
    "shared_failure": jev.noul(
        "Would these two candidates fail for the same reason?",
        true="Shared vulnerability to the same obstruction",
        false="Independent failure modes"
    )
}

def main():
    pairs = list(itertools.combinations(CANDS, 2))
    print(f"Running pairwise combination screen on {len(pairs)} candidate pairs...")
    states = [
        f"CANDIDATE 1 ({p1['id']}): {p1['name']}\n{p1['text']}\n\nCANDIDATE 2 ({p2['id']}): {p2['name']}\n{p2['text']}"
        for p1, p2 in pairs
    ]
    results = jev.ask_many(states, COMBINE_Q, concurrency=6)

    print("\n" + "=" * 80)
    print(f"{'Pair':<20} | {'Compatible':<12} | {'Comb Value':<12} | {'Shared Failure':<15}")
    print("-" * 80)
    for (p1, p2), res in zip(pairs, results):
        pair_id = f"{p1['id']}_{p2['id']}"
        ans = res.get("answers", {})
        comp = ans.get("compatible", {}).get("noul", "?")
        val = ans.get("combination_value", {}).get("score", "?")
        fail = ans.get("shared_failure", {}).get("noul", "?")
        print(f"{pair_id:<20} | {str(comp):<12} | {str(val):<12} | {str(fail):<15}")
    print("=" * 80)

if __name__ == "__main__":
    main()
