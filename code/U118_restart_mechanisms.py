"""RESTART: genuinely new candidate mechanisms, none of which is a variant of a refuted route.

Every route in the pool is now blocked. The exploration policy calls for materially different
mechanisms at this point. These are generated from first principles and from the two NEW facts
established late in this session:
  * Beal <=> "2 is an obligatory exponent" in the hyperbolic regime (kernel-verified for the
    ten known solutions);
  * Beal is FALSE over Z[i], so any proof must use the ORDERING of Z or the ramification of
    rational primes -- a positive constraint on what a proof must contain.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

CONTEXT = (
  "Beal: A^x+B^y=C^z, x,y,z>=3, gcd(gcd(A,B),C)=1 has no solutions. ALREADY BLOCKED in this "
  "project: the modular method on the all-even branch (Azon Hypothesis 5 provably fails for every "
  "reduction, derived); Chabauty over the base field (bounds the wrong point set); abc and IUT "
  "(give finiteness only, ineffectively); Darmon's program (literature says min exponent 3 is "
  "largely inaccessible); extending computation (far behind the literature: min exponent <=113, "
  "bases to 2^100, (3,3,p) to p<=10^7). ALREADY KERNEL-VERIFIED here: exponent reduction to "
  "{4} u odd primes; bases pairwise coprime; A != B; no counterexample when 3|gcd(x,y,z) or "
  "4|gcd(x,y,z); the all-even case IS perfect powers in a primitive Pythagorean triple; Beal is "
  "FALSE over Z[i] (so any proof must use the ordering of Z or ramification of rational primes); "
  "and every one of the ten known Fermat-Catalan solutions fails Beal because it has an exponent 2."
)

M = [
 {"id":"M1","mechanism":"Congruence obstruction search. Exhaustively search small moduli m for a congruence condition that EVERY Beal counterexample must satisfy, beyond pairwise coprimality. Concretely: for each m, compute the set of residue triples (A,B,C) mod m admitting a solution with exponents >=3 mod ord(m), and look for a modulus where that set is empty or tiny.","why_new":"Purely local/elementary; uses no Frey curve, no Chabauty, no abc. Independent failure mode: it would fail by finding no obstruction, not by a hypothesis being unsatisfiable."},
 {"id":"M2","mechanism":"Exploit 'exponent 2 is obligatory'. Beal is equivalent to: every primitive hyperbolic solution has an exponent equal to 2. Seek a mechanism explaining WHY 2 is distinguished - e.g. that a solution with all exponents >=3 would force a rational point on a variety whose 2-part is what makes the known solutions possible.","why_new":"Attacks the reformulation rather than the original statement. The distinguished role of 2 is a structural fact not previously exploited here."},
 {"id":"M3","mechanism":"Locate where the ordering of Z must enter. Beal is FALSE over Z[i], so any valid proof uses the total ordering of Z or ramification of rational primes. Determine precisely which step of a would-be proof must be order-dependent, by finding the minimal additional axiom on an ordered ring that rules out the Helenius identity.","why_new":"Turns an obstruction into a POSITIVE specification of what a proof must contain. No route in the pool does this."},
 {"id":"M4","mechanism":"Size/height constraints from the verified necessary conditions. Combine pairwise coprimality, A != B, bases >=2, and the exponent constraints to derive an explicit inequality relating A,B,C,x,y,z, then test whether it is ever satisfiable.","why_new":"Elementary inequality reasoning on the verified constraint set; fails by the inequality being satisfiable, a different mode from every blocked route."},
 {"id":"M5","mechanism":"Enumerate the signatures NOT excluded by the verified families, to identify exactly where a counterexample could live, and check whether that residual set has exploitable structure.","why_new":"A coverage computation rather than a proof attempt; its output directs all later work and has not been done."},
 {"id":"M6","mechanism":"Descent on the Pythagorean characterisation. The all-even case is perfect powers in a primitive Pythagorean triple (m^2-n^2, 2mn, m^2+n^2). Run classical infinite descent on (m,n) directly, in the style of Fermat's right-triangle theorem, rather than passing to a Frey curve.","why_new":"Fermat-style descent on the parametrisation, avoiding the modular method entirely - and the r=s=2 case of exactly this IS Fermat's right-triangle theorem, which succeeds."},
]

Q = {
 "genuinely_new": jev.noul(
   "Is this mechanism materially different from the routes already blocked in this project - the "
   "modular method, Chabauty, abc/IUT, Darmon's program, and extending computation - rather than a "
   "restatement or a variant of one of them?",
   true="it uses a different source of constraint, so it would fail for a different reason than the blocked routes",
   false="it is a variant of a blocked route, or it would meet the same obstruction"),
 "executable_here": jev.noul(
   "Can a discriminating test of this mechanism actually be executed with exact computation, "
   "elementary derivation, or Lean - with no access to Magma, no large class-group computation, "
   "and no new deep theorem?",
   true="a concrete test can be run now with exact arithmetic, elementary reasoning, or a proof assistant",
   false="it needs machinery not available, such as hyperelliptic Jacobian arithmetic, class groups of high-degree fields, or an unproved theorem"),
 "payoff": jev.score(
   "If the discriminating test came out favourably, how much would be learned?",
   ["level 0: nothing that is not already recorded",
    "level 1: a minor constraint on hypothetical counterexamples",
    "level 2: a new necessary condition, or a precise specification of what a proof must contain",
    "level 3: a new infinite family excluded, or a genuine reduction of the open problem"]),
}

def main() -> int:
    states=[{"context":CONTEXT,"candidate":m} for m in M]
    rs=jev.ask_many(states,Q,concurrency=6)
    rows=[]
    for m,st,r in zip(M,states,rs):
        if "error" in r: print(f"! {m['id']}: {r['error']}",file=sys.stderr); continue
        jev.persist(f"restart_{m['id']}",st,Q,r)
        a=r["answers"]
        rows.append({"id":m["id"],"new":round(a["genuinely_new"]["noul"],2),
                     "exec":round(a["executable_here"]["noul"],2),
                     "payoff":round(a["payoff"]["score"],2),
                     "mech":m["mechanism"][:60]})
    rows.sort(key=lambda r:-(r["new"]*r["exec"]*(1+r["payoff"])))
    print(f"{'id':<4}{'new':>6}{'exec':>6}{'payoff':>8}  mechanism")
    for r in rows: print(f"{r['id']:<4}{r['new']:>6}{r['exec']:>6}{r['payoff']:>8}  {r['mech']}")
    return 0

if __name__=="__main__": raise SystemExit(main())
