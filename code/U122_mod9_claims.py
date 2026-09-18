"""Cycle U122: the p = 3 analogue of the completed mod-8 analysis.

Step 1 (Jev, per the HARD RULE): rank concrete falsifiable mod-9 / 3-adic claims.
Step 2 (exact): enumerate the full mod-9 model and test every claim by brute force.
"""
from __future__ import annotations
import itertools, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

CLAIMS = [
 "At least one of A, B, C is divisible by 3.",
 "Exactly one of A, B, C is divisible by 3.",
 "If 3 divides none of A, B, C then A^x + B^y = C^z has no solution mod 9.",
 "If 3 divides A then 27 divides A^x, so B^y = C^z mod 27.",
 "If 3 divides C then A^x + B^y = 0 mod 27.",
 "For n coprime to 3, n^k mod 9 depends only on k mod 6.",
 "For n coprime to 3, if 3 divides k then n^k = 1 mod 9.",
 "If 3 divides all of x, y, z and 3 divides none of A, B, C then 1 + 1 = 1 mod 9 is required, a contradiction.",
 "If 3 divides x and y but not any base, then C^z = 2 mod 9, which forces z odd and C = 2 mod 9 or similar.",
 "If 3 divides C and x, y are both divisible by 3 then 1 + 1 = 0 mod 27 fails.",
 "The cubes mod 9 are exactly 0, 1 and 8.",
 "If x, y, z are all multiples of 3 then A^x, B^y, C^z are cubes, and cubes mod 9 lie in {0,1,8}.",
 "If all exponents are multiples of 3 then the equation mod 9 forces 3 to divide exactly one base.",
 "If 3 divides none of A,B,C and all exponents are multiples of 3 then {1,8}+{1,8} never meets {1,8} mod 9.",
 "The mod-9 obstruction is strictly weaker than the mod-8 one because 9 has a cyclic unit group.",
 "If 3 divides B then A^x = C^z mod 27, so A and C lie in the same coset of the cube subgroup.",
 "v_3(A^x + B^y) is unbounded, so no fixed power of 3 gives an obstruction.",
 "If 3 divides A and x >= 3 then v_3(A^x) >= 3 exactly when v_3(A) = 1.",
 "Combining mod 8 and mod 9 gives a mod-72 sieve strictly stronger than either alone.",
 "There is a residue class mod 9 that no Beal counterexample base C can occupy.",
]

CONTEXT = (
 "Beal counterexample: A^x+B^y=C^z, A,B,C >= 1, x,y,z >= 3, gcd(gcd(A,B),C)=1. KERNEL-VERIFIED: "
 "bases are PAIRWISE coprime; EXACTLY ONE of A,B,C is even; the full mod-8 picture is settled. "
 "Now judging the p = 3 analogue."
)

Q = {
 "likely_true": jev.score(
   "Is this claim TRUE of every Beal counterexample? Judge the exact statement as written.",
   ["level 0: false, or an easy counterexample exists",
    "level 1: true only under an extra hypothesis not stated",
    "level 2: probably true but the argument is not immediate",
    "level 3: true and follows directly from elementary residue arithmetic"]),
 "decisive": jev.score(
   "If established, how much would this claim constrain a hypothetical counterexample?",
   ["level 0: vacuous or already known",
    "level 1: a mild restriction on residues mod 9",
    "level 2: a genuine new necessary condition",
    "level 3: it forces a contradiction or excludes an infinite family of signatures"]),
 "exactly_testable": jev.noul(
   "Can this claim be settled by exact finite computation over residues?",
   true="a bounded exact enumeration settles it",
   false="it needs a deep theorem or an unbounded search"),
}

states=[{"context":CONTEXT,"claim":c} for c in CLAIMS]
rs=jev.ask_many(states,Q,concurrency=12)
rows=[]
for c,st,r in zip(CLAIMS,states,rs):
    if "error" in r:
        print("ERR", r["error"][:200]); continue
    jev.persist("C038", st, Q, r)
    a=r["answers"]
    rows.append((round(a["likely_true"]["score"],2), round(a["decisive"]["score"],2),
                 round(a["exactly_testable"]["noul"],2), c))
rows.sort(key=lambda t:-(t[0]*t[1]*t[2]))
import json, pathlib as pl
pl.Path("research/pool/evidence/mod9_claim_ranking.json").write_text(json.dumps(rows, indent=2))
print(f"{'true':>6}{'decisive':>10}{'testable':>10}  claim")
for t in rows:
    print(f"{t[0]:>6}{t[1]:>10}{t[2]:>10}  {t[3][:88]}")
print(f"\nranked {len(rows)} mod-9 claims")
