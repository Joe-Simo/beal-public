"""Cycle U123 (EXPLORATION: a different mechanism from the mined p-adic cells).
Jev cell: 'gap/threshold + combinatorial' x 'the large-exponent tail' x 'exploit a verified fact'.
Verified facts exploited: no_cancellation (B^y < C^z <= 2*max(A^x,B^y) when A^x <= B^y),
bases pairwise coprime, A != B, exactly one base even.
Each claim is concrete and falsifiable; the survivors are formalised in Lean."""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

CLAIMS = [
 "If C is the largest of the three bases then z <= max(x, y).",
 "If C is the smallest of the three bases then z > max(x, y).",
 "If A^x <= B^y, C > B and z >= y, then A^x >= y * B^(y-1).",
 "If A^x <= B^y, C > B and z >= y, then y <= B.",
 "If A^x <= B^y and C <= B then z > y.",
 "If A^x <= B^y then C^z / B^y lies in the half-open interval (1, 2].",
 "z * log C - y * log B lies in (0, log 2] whenever A^x <= B^y.",
 "The two largest of the three terms A^x, B^y, C^z differ by a factor of at most 2.",
 "If A^x <= B^y and C > B then z < y * log(B) / log(C) + 1.",
 "At most one of the three exponents can exceed the logarithm base 2 of the largest base times the largest other exponent.",
 "If C is the largest base then z <= max(x,y) and hence the signature is not of the form (x, y, z) with z > x and z > y.",
 "If A < B < C then z <= y.",
 "If A < B < C then x >= y and x >= z is impossible unless A^x is the largest term.",
 "If B < C and A^x <= B^y then y < z * log(C)/log(B).",
 "If C > B then B^y < C^z gives no exponent constraint on its own.",
 "min(x, y) <= max(x, y) is always true and constrains nothing.",
 "The largest base carries an exponent no larger than the largest of the other two exponents.",
 "If the even base is the largest base then its exponent is at most the max of the other two.",
]
CONTEXT = ("Beal counterexample: A^x+B^y=C^z, A,B,C >= 1, x,y,z >= 3, gcd(gcd(A,B),C)=1. KERNEL-VERIFIED: bases "
 "pairwise coprime; A != B; exactly one base even; if A^x <= B^y then B^y < C^z <= 2*B^y. Judge each claim as an exact "
 "statement about such a counterexample.")
Q = {
 "likely_true": jev.score("Is this claim TRUE of every Beal counterexample, exactly as written?",
   ["level 0: false or vacuous","level 1: true only with an unstated extra hypothesis",
    "level 2: probably true, argument not immediate","level 3: true and follows directly from the verified facts"]),
 "decisive": jev.score("If established, how much would this claim constrain a hypothetical counterexample?",
   ["level 0: vacuous or already known","level 1: mild","level 2: a genuine new necessary condition on the signature",
    "level 3: excludes an infinite family of signatures"]),
 "formalisable": jev.noul("Can this be proved in Lean 4 + mathlib in under fifty lines from the verified facts?",
   true="yes, elementary inequalities on naturals", false="no, needs real logarithms or deep results"),
}
states=[{"context":CONTEXT,"claim":c} for c in CLAIMS]
rs=jev.ask_many(states,Q,concurrency=12)
rows=[]
for c,st,r in zip(CLAIMS,states,rs):
    if "error" in r: print("ERR",r["error"][:160]); continue
    jev.persist("C039", st, Q, r); a=r["answers"]
    rows.append((round(a["likely_true"]["score"],2),round(a["decisive"]["score"],2),round(a["formalisable"]["noul"],2),c))
rows.sort(key=lambda t:-(t[0]*t[1]*t[2]))
Path("research/pool/evidence/tail_claim_ranking.json").write_text(json.dumps(rows,indent=2))
print(f"{'true':>6}{'decisive':>10}{'lean':>6}  claim")
for t in rows: print(f"{t[0]:>6}{t[1]:>10}{t[2]:>6}  {t[3][:90]}")
