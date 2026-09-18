"""Second restart batch. Each mechanism exploits something ESTABLISHED in this session."""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

CONTEXT = (
 "Established here this session: (a) Beal <=> no primitive solution with |chi| >= 1/12, where "
 "chi = 1/x+1/y+1/z-1; the Beal region has |chi| >= 1/12 (kernel-verified) and all ten known "
 "solutions have |chi| <= 1/18. (b) Positivity forbids cancellation: B^y < C^z <= 2B^y when "
 "A^x <= B^y, so C is pinned within a factor 2^(1/z) <= 1.26 of B^(y/z) (kernel-verified). "
 "(c) {A^x mod m : x>=3} = <A>, giving a congruence sieve rejecting 77.7% at m=240. "
 "(d) Classical descent is not a self-map. (e) Bases pairwise coprime, A != B, bases >= 2. "
 "BLOCKED: modular method on the all-even branch, Chabauty over the base field, abc/IUT "
 "(finiteness only), Darmon's program, naive search extension, Baker via the size window."
)

M=[
 {"id":"N1","mechanism":"Split by curvature. Prove Beal first for VERY hyperbolic signatures, |chi| >= T for some threshold T > 1/12, where the associated orbifold is far from Euclidean and genus is large; then the remaining strip 1/12 <= |chi| < T is a FINITE set of signatures which could be attacked one by one.","why_new":"Uses the verified 1/12 threshold to stratify the problem. Turns an infinite problem into a large-|chi| family plus a finite list, which no route in the pool attempts."},
 {"id":"N2","mechanism":"Reorganise the counterexample search around the verified window. Instead of enumerating (A,x,B,y) and hashing sums, enumerate (B,y,z) and test only the O(1) integers C in (B^(y/z), 2^(1/z) B^(y/z)], checking whether C^z - B^y is a perfect power. Each (B,y,z) costs one perfect-power test.","why_new":"A different search ORGANISATION, enabled by a constraint this project proved. Published searches enumerate summands; this enumerates one summand plus the exponent and derives C."},
 {"id":"N3","mechanism":"Adelic / Brauer-Manin style obstruction. No single modulus obstructs (established). Ask whether the PRODUCT over all places carries an obstruction that no individual place does - the standard modern refinement when local obstructions individually fail.","why_new":"A genuinely different level of the local-global machinery; its failure mode would be that the Brauer group is trivial, unrelated to any recorded obstruction."},
 {"id":"N4","mechanism":"Explain the empty strip 1/18 < |chi| < 1/12. No known solution has curvature there, and the Beal region begins at 1/12. If a mechanism explains why the strip is empty, it may extend past 1/12.","why_new":"Targets the boundary of the known-solution region rather than the interior of the Beal region; the gap is an observed fact not previously explained."},
 {"id":"N5","mechanism":"Asymptotic Beal: prove it for all signatures with min exponent >= N for some explicit N, using the fact that large exponents force large |chi| and hence high genus, in the style of asymptotic Fermat results over number fields.","why_new":"Attacks the large-exponent tail rather than small signatures; complements N1 and would leave only bounded exponents."},
]

Q={
 "genuinely_new": jev.noul(
   "Is this mechanism materially different from every route already blocked in this project?",
   true="it draws on a different source of constraint and would fail for a different reason",
   false="it is a variant of a blocked route or meets the same obstruction"),
 "executable_here": jev.noul(
   "Can a discriminating test be run NOW with exact computation, elementary derivation, or Lean - "
   "no Magma, no class groups of large fields, no unproved theorem?",
   true="a concrete test can be run immediately with the tools available",
   false="it needs machinery or theorems not available here"),
 "payoff": jev.score(
   "If the test came out favourably, how much would be learned?",
   ["level 0: nothing new","level 1: a minor constraint","level 2: a new necessary condition or a genuine search capability",
    "level 3: an infinite family excluded, or the open problem genuinely reduced"]),
}

states=[{"context":CONTEXT,"candidate":m} for m in M]
rs=jev.ask_many(states,Q,concurrency=5)
rows=[]
for m,st,r in zip(M,states,rs):
    if "error" in r: continue
    jev.persist(f"batch2_{m['id']}",st,Q,r)
    a=r["answers"]
    rows.append((m["id"],round(a["genuinely_new"]["noul"],2),round(a["executable_here"]["noul"],2),
                 round(a["payoff"]["score"],2),m["mechanism"][:58]))
rows.sort(key=lambda t:-(t[1]*t[2]*(1+t[3])))
print(f"{'id':<4}{'new':>6}{'exec':>6}{'payoff':>8}  mechanism")
for t in rows: print(f"{t[0]:<4}{t[1]:>6}{t[2]:>6}{t[3]:>8}  {t[4]}")
