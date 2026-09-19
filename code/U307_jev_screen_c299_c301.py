"""Jev screen for C299, C300, C301.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "code"))
import jev

requests = [
    {
        "id": "C299",
        "question": "Does extending the Kraus sieve for signature (3, 3, p) to primes p in [2401, 2500] provide exact, unconditional elimination of counterexamples for those exponents without circular assumptions?",
        "context": "Kraus sieve testing auxiliary primes q = 2kp + 1 against newforms 72a1 and 144a1 for signature (3,3,p)."
    },
    {
        "id": "C300",
        "question": "Does the Lawrence-Venkatesh method on variations of Hodge structures attached to covers branched at orders (p, q, r) apply across varying exponent families or is it restricted to fixed algebraic families?",
        "context": "Lawrence-Venkatesh (Annals 2020) uses p-adic period maps and Galois representations to prove Mordell / Faltings for families of varieties over a fixed base. Does varying the branch orders (p, q, r) break the constancy of the Hodge structure family?"
    },
    {
        "id": "C301",
        "question": "Does the hyperbolic defect -chi = 1 - 1/p - 1/q - 1/r >= 1/12 impose an absolute lower bound on the canonical height of rational points on triangle orbifolds Delta(p, q, r)?",
        "context": "Triangle orbifolds with p,q,r >= 3 have negative Euler characteristic bounded away from zero by -chi >= 1/12. Does Arakelov intersection theory yield an effective height bound independent of (p, q, r)?"
    }
]

questions = {
    "relevance": jev.score("Rate relevance to resolving Beal conjecture", [
        "level 0: irrelevant or already solved",
        "level 1: general Diophantine geometry, no direct signature resolution",
        "level 2: settles bounded exponents or single signature range",
        "level 3: settles infinite family of exponents",
        "level 4: settles all remaining signatures or full conjecture"
    ]),
    "failure_risk": jev.noul("Does this candidate risk suffering one of the three known failure modes (isogeny/residual conflation, Chabauty wrong field, heuristic laundering)?",
        true="high risk of recurring failure mode",
        false="orthogonal to recorded failure modes"
    ),
    "action": jev.choice("Recommended next action", {
        "advance": "proceed to verification or derivation",
        "discard": "refuted or unviable",
        "literature_check": "needs primary source audit",
        "exact_computation": "run exact computation"
    })
}

def main():
    try:
        results = jev.ask_many([{"cand": r} for r in requests], questions, concurrency=3)
        print("JEV_SUCCESS")
        for r, res in zip(requests, results):
            jev.persist(r["id"], {"cand": r}, questions, res)
            an = res.get("answers", {})
            cid = r["id"]
            rel = an.get("relevance", {}).get("score")
            risk = an.get("failure_risk", {}).get("noul")
            act = an.get("action", {}).get("choice")
            print(f"[{cid}] relevance={rel} risk={risk} action={act}")
    except Exception as e:
        print(f"JEV_ERROR: {e}")

if __name__ == "__main__":
    main()
