"""Use Jev at the scale it is actually good for: generate a LARGE mechanism space and rank it all.

Prior attempts on Beal were bounded by how many approaches one person could generate and triage.
That is the bound Jev removes.  So rather than hand-picking five or six mechanisms, build the
space systematically as (TOOL) x (TARGET) x (ANGLE) and let Jev rank every combination.
"""
from __future__ import annotations
import itertools, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

TOOLS = [
 ("congruence/local", "residues, subgroup structure of powers, local solubility"),
 ("descent", "infinite descent, 2-descent, parametrised descent on the base variables"),
 ("size/height", "inequalities, logarithmic forms, Diophantine approximation of exponent ratios"),
 ("factorisation in rings", "splitting in Z[i], Z[zeta_n], quadratic and cyclotomic orders"),
 ("modular/Galois", "Frey curves, residual representations, level lowering, image of inertia"),
 ("curvature/orbifold", "the Euler characteristic chi, genus growth, stacky structure"),
 ("combinatorial", "counting solutions, density of powerful numbers, additive structure"),
 ("valuation/p-adic", "v_p of the terms, Lifting the Exponent, ramification"),
 ("symmetry", "the interchange of A and B, the distinguished role of C, permutation structure"),
 ("gap/threshold", "the verified 1/12 curvature threshold and the exponent-2 phenomenon"),
]
TARGETS = [
 ("the whole conjecture", "all signatures with min exponent >= 3"),
 ("the odd-prime signatures", "x, y, z all odd primes >= 5 - the untouched majority"),
 ("the frontier signature (3,5,7)", "the smallest signature the literature records as open"),
 ("the large-exponent tail", "signatures with |chi| >= 1/3, where exponents are unbounded"),
 ("necessary conditions", "sharpening the constraints on a hypothetical counterexample"),
 ("the counterexample side", "constructing, or proving impossible, an explicit solution"),
]
ANGLES = [
 ("exploit a verified fact", "build directly on something kernel-verified in this project"),
 ("import from an adjacent problem", "transfer a technique that works on Catalan, FLT, or Pillai"),
 ("invert the question", "ask what a counterexample would have to look like, and derive from that"),
 ("seek an invariant", "find a quantity preserved or forced by the equation"),
 ("seek a contradiction from two directions", "combine an upper and a lower bound on the same object"),
]

CONTEXT = (
 "Beal: A^x+B^y=C^z, x,y,z>=3, gcd(gcd(A,B),C)=1 has no solutions. KERNEL-VERIFIED here: exponent "
 "reduction to {4} u odd primes; bases pairwise coprime; A != B; no counterexample when 3|gcd(x,y,z) "
 "or 4|gcd(x,y,z); the all-even case IS perfect powers in a primitive Pythagorean triple; Beal is "
 "FALSE over Z[i] so any proof must use the ordering of Z; positivity forbids cancellation giving "
 "B^y < C^z <= 2B^y; every Beal signature has |chi| >= 1/12 with equality at (3,3,4); all ten known "
 "solutions have an exponent 2 and |chi| <= 1/18. BLOCKED: modular method on the all-even branch "
 "(Azon Hypothesis 5 provably unsatisfiable); Chabauty over the base field; abc/IUT (finiteness "
 "only); Darmon's program (min exponent 3 largely inaccessible); extending computation (literature "
 "reached bases 2^100, min exponent <=113, (3,3,p) to 10^7); Baker via the size window (the linear "
 "form is identically log(1+A^x/B^y)); classical descent (not a self-map); curvature stratification "
 "(exact but moves no difficulty); congruence obstruction (no local obstruction exists)."
)

Q = {
 "not_already_blocked": jev.noul(
   "Would a discriminating test of this mechanism fail for a reason DIFFERENT from every obstruction "
   "already recorded as blocked in the context?",
   true="it would fail for a new reason, or might not fail",
   false="it would meet one of the recorded obstructions"),
 "executable_now": jev.noul(
   "Can a discriminating test be run immediately with exact integer or symbolic computation, "
   "elementary derivation, or Lean 4 with mathlib - no Magma, no class groups of large number "
   "fields, no unproved theorem, no new deep machinery?",
   true="a concrete test can be run now with those tools",
   false="it requires machinery or results not available"),
 "payoff": jev.score(
   "If the test came out favourably, how much would be learned about Beal's conjecture itself?",
   ["level 0: nothing beyond what is already recorded",
    "level 1: a minor constraint on hypothetical counterexamples",
    "level 2: a new necessary condition, a new equivalent formulation, or a new verified family",
    "level 3: an infinite family of signatures excluded, or the open problem genuinely reduced"]),
}

def main() -> int:
    combos=[]
    for (tn,td),(gn,gd),(an,ad) in itertools.product(TOOLS,TARGETS,ANGLES):
        combos.append({"tool":tn,"tool_detail":td,"target":gn,"target_detail":gd,
                       "angle":an,"angle_detail":ad,
                       "mechanism":f"Apply {tn} ({td}) to {gn} ({gd}), by the strategy: {an} - {ad}."})
    print(f"mechanism space: {len(combos)} combinations", file=sys.stderr)
    states=[{"context":CONTEXT,"candidate":c} for c in combos]
    rs=jev.ask_many(states,Q,concurrency=12)
    rows=[]
    for c,st,r in zip(combos,states,rs):
        if "error" in r: continue
        a=r["answers"]
        rows.append({"tool":c["tool"],"target":c["target"],"angle":c["angle"],
                     "new":round(a["not_already_blocked"]["noul"],3),
                     "exec":round(a["executable_now"]["noul"],3),
                     "payoff":round(a["payoff"]["score"],3)})
    # persist the whole ranking once, rather than 300 separate files
    Path("research/pool/evidence/mechanism_space_ranking.json").write_text(
        json.dumps({"state":"HYPOTHESIS_ONLY","n":len(rows),"rows":rows}, indent=1))
    rows.sort(key=lambda r:-(r["new"]*r["exec"]*(1+r["payoff"])))
    print(f"{'score':>7}{'new':>7}{'exec':>7}{'pay':>6}  tool / target / angle")
    for r in rows[:18]:
        s=r["new"]*r["exec"]*(1+r["payoff"])
        print(f"{s:>7.3f}{r['new']:>7.2f}{r['exec']:>7.2f}{r['payoff']:>6.2f}  "
              f"{r['tool']:<20} | {r['target']:<32} | {r['angle']}")
    print(f"\nranked {len(rows)} mechanisms")
    return 0

if __name__=="__main__": raise SystemExit(main())
