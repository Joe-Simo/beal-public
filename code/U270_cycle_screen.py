"""Cycle 101+ triage screen for Beal research candidates.
Evaluates four active candidates using Jev typed screen:
1. Formal immersion of X_0(72), X_0(144) into Eisenstein quotients at cusps.
2. Ellenberg Frey Q-curve descent for signature (2, 4, p) over Q(i).
3. Kraus modular elimination extension for (3, 3, p) on p in [1701, 1800].
4. Arakelov height bounds and arithmetic intersection for uniform Beal bounds.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "code"))
import jev

CANDIDATES = [
    {
        "id": "C264_cusp_formal_immersion",
        "name": "Formal Immersion at Cusps for Levels 72 and 144",
        "text": (
            "Candidate: Formal immersion of modular curves X_0(72) and X_0(144) into their "
            "Eisenstein quotients J_e(N) (which have rank 0) at cusps infinity and 0. "
            "Goal: Use Mazur's formal immersion criterion to bound the prime exponents p for which "
            "a Frey curve E_{A,B} can have residual representation rho_{E,p} congruent to a newform f "
            "at level 72 or 144, leveraging that j(E_{A,B}) cannot specialize to the cusp unless C=0."
        ),
    },
    {
        "id": "C265_q_curve_descent",
        "name": "Ellenberg Frey Q-Curve Descent for Signature (2, 4, p)",
        "text": (
            "Candidate: Ellenberg Frey Q-curve descent for the generalized Fermat equation A^2 + B^4 = C^p. "
            "Associated to a primitive solution is a Q-curve E over K = Q(i) whose Galois representation "
            "arises from a Hilbert modular newform over Q(i). Elimination of residual representations "
            "via Kraus sieve over Q(i) and modular forms over imaginary quadratic fields."
        ),
    },
    {
        "id": "C266_kraus_sieve_p1701_p1800",
        "name": "Extended Kraus Sieve for (3, 3, p) on p in [1701, 1800]",
        "text": (
            "Candidate: Extended exact modular Kraus sieve for Beal signature (3, 3, p) across prime exponents "
            "p in [1701, 1800]. Uses multi-modulus auxiliary primes l = 2*k*p + 1 to eliminate potential mod-p "
            "isomorphisms between Frey elliptic curves E_{A,B} and weight-2 newforms at conductor levels 72 and 144. "
            "Provides unconditional exact integer certificate verified independently in PARI/GP."
        ),
    },
    {
        "id": "C267_arakelov_uniform_bounds",
        "name": "Arakelov Intersection and Modular Uniformity",
        "text": (
            "Candidate: Arakelov arithmetic intersection theory on modular curves X_0(N) and height bounds. "
            "Attempt to deduce uniform bounds on prime exponents p appearing in Beal solutions by bounding "
            "the Faltings height of Frey curves in terms of conductor N and Serre level lowering bounds."
        ),
    },
]

QUESTIONS = {
    "exact_computability": jev.noul(
        "Can this candidate's core assertion be certified immediately by exact finite integer / modular computation in PARI/GP or Python without relying on uncomputed modular forms over number fields?",
        true="Yes, concrete exact certificates can be computed and verified in this cycle",
        false="No, requires unresolved theoretical infrastructure or heavy non-trivial software engines not available",
    ),
    "failure_mode_risk": jev.noul(
        "Does this route risk falling into known failure modes: residual/isogeny conflation (claiming mod-p congruence impossible merely because isogeny fails), Chabauty over wrong field, or heuristic laundering?",
        true="Yes, significant risk of confusing isogeny/L-values with residual mod-p congruence or unverified field descent",
        false="No, the logical boundary between residual representations and isogenies is strictly respected",
    ),
    "relevance_level": jev.score(
        "How directly does establishing this candidate advance the resolution of Beal's conjecture?",
        [
            "level 0: peripheral or unrelated to Beal signatures",
            "level 1: general modular method context without resolving any signature",
            "level 2: settles a concrete range of exponents or a new specific signature family",
            "level 3: settles an entire infinite signature family for all exponents",
            "level 4: resolves the complete conjecture outright",
        ],
    ),
    "recommended_action": jev.choice(
        "What is the recommended immediate research action for this candidate in this cycle?",
        {
            "advance": "Advance candidate: strong theoretical footing, high Beal relevance",
            "exact_computation": "Run exact computational sieve or verification in PARI/GP or Python",
            "literature_check": "Verify key citations or prior claims in primary literature",
            "formalize": "Formalize machine-checked definitions and theorems in Lean 4",
            "park": "Temporarily park due to missing tools or non-actionable prerequisites",
            "discard": "Discard: flawed mechanism or known dead end",
        },
    ),
}

def main():
    print(f"Screening {len(CANDIDATES)} candidate routes with Jev...")
    states = [c["text"] for c in CANDIDATES]
    results = jev.ask_many(states, QUESTIONS, concurrency=4)

    evidence_dir = REPO / "research" / "pool" / "evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)

    print("\n" + "=" * 80)
    print(f"{'Candidate ID':<28} | {'Exact Comp':<12} | {'Fail Risk':<10} | {'Rel':<5} | {'Action':<15}")
    print("-" * 80)

    for cand, res in zip(CANDIDATES, results):
        cid = cand["id"]
        # Save raw evidence
        ev_file = evidence_dir / f"{cid}_jev_screen.json"
        ev_file.write_text(json.dumps({"candidate": cand, "jev_response": res}, indent=2))

        ans = res.get("answers", {})
        exact_comp = ans.get("exact_computability", {}).get("choice", "?")
        fail_risk = ans.get("failure_mode_risk", {}).get("choice", "?")
        rel = ans.get("relevance_level", {}).get("score", "?")
        action = ans.get("recommended_action", {}).get("choice", "?")
        conf = ans.get("recommended_action", {}).get("confidence", 0.0)

        print(f"{cid:<28} | {str(exact_comp):<12} | {str(fail_risk):<10} | {str(rel):<5} | {action} ({conf:.2f})")
    print("=" * 80)

if __name__ == "__main__":
    main()
