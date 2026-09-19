"""Jev screen for strategy options on OddPrimeDivisorForm, EulerDescentStep, and Signature (3,4,4).

Routing signal only: stored HYPOTHESIS_ONLY.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

CANDIDATES = [
    {
        "id": "C229",
        "name": "OddPrimeDivisorForm strong induction",
        "statement": "In Lean 4, prove OddPrimeDivisorForm (every odd prime p dividing a^2+3b^2 with gcd(a,b)=1 is represented as x^2+3y^2) by strong induction on the quotient m = (a^2+3b^2)/p using already machine-checked lemmas descent_strict, descent_quotient_lt, and form_div_four_of_even.",
        "context": "We have machine checked in Beal.Euler: descent_strict, descent_quotient_lt, descent_quotient_pos', form_div_four_of_even, form_four_dvd_of_even, form_quotient_of_prime, represents_of_natAbs_prime_factors. All that remains is chaining them via Nat.strong_induction_on.",
    },
    {
        "id": "C230",
        "name": "EulerDescentStep unified dispatch",
        "statement": "Combine descent_step_smaller_natAbs (3 nmid p branch) and three_dvd_p_branch_step3 (3 | p branch) to prove that any non-trivial integer solution to p(p^2+3q^2)=c^3 with q != 0 produces a strictly smaller non-trivial solution on Nat, yielding a contradiction via Nat.find or WellFounded.fix.",
        "context": "We have proved descent_step_smaller_natAbs (|e| < |c|) for 3 nmid p, and three_dvd_p_branch_step3 swaps (p, q) to (q, 3p'') with 3 nmid q, reducing 3 | p directly to the 3 nmid p branch.",
    },
    {
        "id": "C231",
        "name": "Signature (3,4,4) resolution via quartic Pythagorean descent",
        "statement": "For x^3 + y^4 = z^4 with gcd(x,y,z)=1, rewrite as x^3 = z^4 - y^4 = (z^2-y^2)(z^2+y^2). Analyze gcd(z^2-y^2, z^2+y^2) in {1, 2} and apply coprime factor descent to constrain x, y, z.",
        "context": "Existing checkpoints contain partial work on (3,4,4) and Mihailescu/Catalan Catalan cases. We want to test whether elementary descent can unconditionally rule out primitive solutions x,y,z >= 1.",
    }
]

QUESTIONS = {
    "soundness": jev.score(
        "Does the proposed mathematical mechanism hold without hidden gaps, circularity, or unproved external dependencies?",
        [
            "level 0: flawed mechanism or known circularity",
            "level 1: substantial unproved dependencies or heuristic assumptions",
            "level 2: sound outline but non-trivial technical lemmas still unformalized",
            "level 3: completely rigorous, sound, and fully supported by existing proved lemmas",
        ],
    ),
    "lean4_feasibility": jev.score(
        "How feasible is complete formal verification in Lean 4 + mathlib with zero sorry and standard axioms only?",
        [
            "level 0: impossible or requires major missing mathlib theories (e.g. modular forms over number fields)",
            "level 1: very difficult, requires thousands of lines of new algebraic theory",
            "level 2: moderately difficult, standard Diophantine/algebraic techniques, achievable in tens to hundreds of lines",
            "level 3: immediate or nearly immediate from existing lemmas in the repo",
        ],
    ),
    "recommended_action": jev.choice(
        "What is the recommended next action for this candidate in the research loop?",
        {
            "formalize": "Candidate is fully ready to be formally coded and machine-checked in Lean 4",
            "advance": "Candidate is theoretically sound; advance to detailed symbolic/exact derivation first",
            "counterexample_search": "Candidate requires bounded adversarial countersearch to test robustness",
            "park": "Candidate is low priority or blocked by external prerequisites",
            "discard": "Candidate is flawed or redundant",
        },
    ),
}

def main() -> int:
    states = [f"{c['id']}: {c['name']}\nClaim: {c['statement']}\nContext: {c['context']}" for c in CANDIDATES]
    results = jev.ask_many(states, QUESTIONS)
    for c, r in zip(CANDIDATES, results):
        print(f"=== {c['id']}: {c['name']} ===")
        if "error" in r:
            print("  Error:", r["error"])
            continue
        jev.persist(c["id"], c, QUESTIONS, r)
        answers = r.get("answers", {})
        for qname, ans in answers.items():
            if ans.get("type") == "score":
                print(f"  {qname}: score={ans.get('score')} (conf={ans.get('confidence')})")
            elif ans.get("type") == "choice":
                print(f"  {qname}: choice={ans.get('choice')} (conf={ans.get('confidence')})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
