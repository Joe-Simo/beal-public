"""Jev triage over candidate ELEMENTARY lemmas about Beal counterexamples.

Each is a structural constraint that might be provable in Lean with no external theorem.
Rank by how much structure they impose and whether they are actually elementary.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

LEMMAS = [
 {"id":"L1","statement":"In any Beal counterexample, gcd(A,B) = 1.","sketch":"A prime p dividing A and B divides A^x + B^y = C^z, hence divides C, hence divides gcd(gcd(A,B),C) = 1."},
 {"id":"L2","statement":"In any Beal counterexample, gcd(A,C) = 1 and gcd(B,C) = 1; so A,B,C are PAIRWISE coprime.","sketch":"p | A and p | C gives p | C^z - A^x = B^y, so p | B, contradicting L1."},
 {"id":"L3","statement":"No Beal counterexample has A = B.","sketch":"By L1, gcd(A,A) = A = 1, so 1 + 1 = C^z with z >= 3, impossible since 2 is not a perfect power."},
 {"id":"L4","statement":"No Beal counterexample has A = 1 and B = 1.","sketch":"2 = C^z with z >= 3 has no solution."},
 {"id":"L5","statement":"In any Beal counterexample, C > A and C > B.","sketch":"C^z = A^x + B^y > A^x >= A, and similarly for B; needs care since exponents differ."},
 {"id":"L6","statement":"No Beal counterexample has A = 1 (equivalently B = 1), i.e. all three bases are at least 2.","sketch":"1 + B^y = C^z with y,z >= 3 is Catalan's equation; by Mihailescu the only solution of u^p - v^q = 1 with u,v,p,q > 1 is 3^2 - 2^3, whose exponents are 2 and 3, so none has both exponents >= 3. REQUIRES Mihailescu as an external theorem."},
 {"id":"L7","statement":"In any Beal counterexample, exactly one of A, B is even and C is odd.","sketch":"By pairwise coprimality not both A,B even. If both odd then A^x + B^y is even so C is even, contradicting coprimality of A and C only if... needs checking."},
 {"id":"L8","statement":"For every n with 3 | n, the diagonal signature (n,n,n) admits no Beal counterexample.","sketch":"Reduce to (A^m)^3 + (B^m)^3 = (C^m)^3 and apply FLT for exponent 3. REQUIRES FLT3, which mathlib v4.14.0 does NOT yet prove completely."},
]

CONTEXT = ("Beal: A^x + B^y = C^z, A,B,C >= 1 positive integers, x,y,z >= 3, gcd(gcd(A,B),C) = 1. "
           "Already kernel-verified in this project: the exponent reduction lemma, and the diagonal "
           "family (n,n,n) with 4|n via mathlib fermatLastTheoremFour. Goal is to add unconditional "
           "kernel-verified structure with NO custom axioms.")

Q = {
    "is_true": jev.score(
        "Is this stated lemma actually TRUE as written, given the Beal hypotheses? Judge the exact "
        "statement, not the sketch. Watch for statements that quietly need a base to be at least 2, "
        "that mishandle the case where a base equals 1, or that assume the exponents are equal.",
        [
            "level 0: the statement is false as written, or a counterexample within the Beal hypotheses exists",
            "level 1: the statement is probably true but as written has an unhandled edge case such as a base equal to 1",
            "level 2: the statement is true and its sketch is essentially a correct argument",
            "level 3: the statement is true, standard, and the sketch is a complete argument",
        ],
    ),
    "elementary": jev.noul(
        "Can this lemma be proved using only elementary number theory - divisibility, coprimality, "
        "and basic inequalities - with NO appeal to a deep external theorem such as Fermat's Last "
        "Theorem, Mihailescu's theorem, or the modular method?",
        true="only divisibility, gcd manipulation and elementary inequalities are needed",
        false="it requires a deep external theorem, for example Catalan/Mihailescu or FLT for some exponent",
    ),
    "structural_value": jev.score(
        "How much does this lemma constrain the search space for a Beal counterexample, or how much "
        "does it simplify later arguments?",
        [
            "level 0: it restates a hypothesis or follows immediately with no new constraint",
            "level 1: it rules out a single degenerate case such as one specific pair of bases",
            "level 2: it imposes a structural condition used repeatedly in later arguments, such as pairwise coprimality or a parity constraint",
            "level 3: it eliminates an infinite family of signatures or bases outright",
        ],
    ),
}


def main() -> int:
    states = [{**{"context": CONTEXT}, "lemma": L} for L in LEMMAS]
    resps = jev.ask_many(states, Q, concurrency=8)
    rows = []
    for L, st, r in zip(LEMMAS, states, resps):
        if "error" in r:
            print(f"! {L['id']}: {r['error']}", file=sys.stderr); continue
        jev.persist(f"lemma_{L['id']}", st, Q, r)
        a = r["answers"]
        rows.append({"id": L["id"], "true": round(a["is_true"]["score"], 2),
                     "elementary": round(a["elementary"]["noul"], 2),
                     "value": round(a["structural_value"]["score"], 2),
                     "stmt": L["statement"][:64]})
    rows.sort(key=lambda r: -(r["true"] + r["value"] + 2 * r["elementary"]))
    print(f"{'id':<4}{'true':>6}{'elem':>7}{'value':>7}  statement")
    for r in rows:
        print(f"{r['id']:<4}{r['true']:>6}{r['elementary']:>7}{r['value']:>7}  {r['stmt']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
