"""Pairwise combination screen for the four live unifying candidates.
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
        "id": "UNIFYING_FREY",
        "name": "Darmon Generalized Frey Variety",
        "text": "Darmon generalized Frey hyperelliptic curve / abelian variety for A^x + B^y = C^z with x,y,z >= 3.",
    },
    {
        "id": "UNIFORM_ML",
        "name": "Dimitrov-Gao-Habegger Uniform Mordell-Lang",
        "text": "Uniform Mordell-Lang bounds on rational points of Darmon-Granville covering curves for general-type signatures.",
    },
    {
        "id": "EXP2_BOUNDARY",
        "name": "Exponent-2 Geometric Gonality Boundary",
        "text": "Classification of covering curve gonality and genus showing exponent 2 is necessary for infinite rational families.",
    },
    {
        "id": "SERRE_UNIFORM",
        "name": "Serre Uniform Exponent Bound",
        "text": "Serre uniform level-lowering bounding exponents max(x,y,z) by the conductor of weight-2 modular representations.",
    },
]

COMBINE_Q = {
    "compatible": jev.noul(
        "Are these two unifying directions mathematically compatible and mutually reinforcing?",
        true="Compatible and reinforce each other",
        false="Incompatible or unrelated"
    ),
    "combination_value": jev.score(
        "What is the combination value of fusing these two directions into a single framework?",
        [
            "level 0: no synergy",
            "level 1: minor bookkeeping synergy",
            "level 2: discharges an open obligation in the other",
            "level 3: provides a complete bridge across bounded vs unbounded exponents"
        ]
    ),
    "shared_failure": jev.noul(
        "Would these two directions fail for the same reason?",
        true="Shared vulnerability to the same obstruction",
        false="Independent failure modes"
    )
}

def main():
    pairs = list(itertools.combinations(CANDS, 2))
    print(f"Running pairwise combination screen on {len(pairs)} unifying pairs...")
    states = [
        f"DIRECTION 1 ({p1['id']}): {p1['name']}\n{p1['text']}\n\nDIRECTION 2 ({p2['id']}): {p2['name']}\n{p2['text']}"
        for p1, p2 in pairs
    ]
    results = jev.ask_many(states, COMBINE_Q, concurrency=6)

    print("\n" + "=" * 80)
    print(f"{'Pair':<28} | {'Compatible':<12} | {'Comb Value':<12} | {'Shared Failure':<15}")
    print("-" * 80)
    for (p1, p2), res in zip(pairs, results):
        pair_id = f"{p1['id']}_{p2['id']}"
        ans = res.get("answers", {})
        comp = ans.get("compatible", {}).get("noul", "?")
        val = ans.get("combination_value", {}).get("score", "?")
        fail = ans.get("shared_failure", {}).get("noul", "?")
        print(f"{pair_id:<28} | {str(comp):<12} | {str(val):<12} | {str(fail):<15}")
    print("=" * 80)

if __name__ == "__main__":
    main()
