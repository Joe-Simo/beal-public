"""Cycle U124 — NOVEL COMBINATION at Jev scale.
Machine-generate implications  P(bases) -> Q(exponents)  from atomic predicates, filter them
EXACTLY on the full solution model (A,B,C<=60, x,y,z<=12, exponents 1,2 allowed), then let Jev
rank the surviving TRUE, NON-VACUOUS, NOT-ALREADY-PROVED statements by provability and payoff.
Jev never decides truth here: truth on the model is decided by enumeration, proof by Lean."""
from __future__ import annotations
import itertools, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import jev

# --- exact solution model -------------------------------------------------------------
P={(n,k):n**k for n in range(1,61) for k in range(1,13)}
inv={}
for (n,k),v in P.items(): inv.setdefault(v,[]).append((n,k))
S=[(A,B,C,x,y,z) for (A,x),va in P.items() for (B,y),vb in P.items() for (C,z) in inv.get(va+vb,[])]
S=[s for s in S if s[0]!=s[1]]   # A != B is kernel-verified for Beal; keep model honest
print("model solutions:",len(S))

# --- atomic predicates ----------------------------------------------------------------
HYP = {
 "A<B": lambda A,B,C,x,y,z: A<B, "B<A": lambda A,B,C,x,y,z: B<A,
 "A<C": lambda A,B,C,x,y,z: A<C, "C<A": lambda A,B,C,x,y,z: C<A,
 "B<C": lambda A,B,C,x,y,z: B<C, "C<B": lambda A,B,C,x,y,z: C<B,
 "A even": lambda A,B,C,x,y,z: A%2==0, "B even": lambda A,B,C,x,y,z: B%2==0, "C even": lambda A,B,C,x,y,z: C%2==0,
 "A^x<B^y": lambda A,B,C,x,y,z: A**x<B**y, "B^y<A^x": lambda A,B,C,x,y,z: B**y<A**x,
 "x<y": lambda A,B,C,x,y,z: x<y, "y<x": lambda A,B,C,x,y,z: y<x,
}
CON = {
 "z<=max(x,y)": lambda A,B,C,x,y,z: z<=max(x,y), "max(x,y)<z": lambda A,B,C,x,y,z: max(x,y)<z,
 "x<z": lambda A,B,C,x,y,z: x<z, "y<z": lambda A,B,C,x,y,z: y<z, "z<x": lambda A,B,C,x,y,z: z<x, "z<y": lambda A,B,C,x,y,z: z<y,
 "x<=y": lambda A,B,C,x,y,z: x<=y, "y<=x": lambda A,B,C,x,y,z: y<=x,
 "z<=x": lambda A,B,C,x,y,z: z<=x, "z<=y": lambda A,B,C,x,y,z: z<=y,
 "z<x+y": lambda A,B,C,x,y,z: z<x+y, "C<A+B": lambda A,B,C,x,y,z: C<A+B, "C<=max(A,B)": lambda A,B,C,x,y,z: C<=max(A,B),
 "C^z<=2*max(A^x,B^y)": lambda A,B,C,x,y,z: C**z<=2*max(A**x,B**y),
}
KNOWN = {("A<C","B<C","z<=max(x,y)"),("C<A","C<B","max(x,y)<z"),("C<B","y<z"),("C<A","x<z")}

def implied_by_known(hyps, con):
    hs=set(hyps)
    for k in KNOWN:
        *kh, kc = k
        if set(kh)<=hs and kc==con: return True
    return False

cands=[]
for r in (1,2):
    for hyps in itertools.combinations(HYP,r):
        if r==2 and {hyps[0],hyps[1]} in ({"A<B","B<A"},{"A<C","C<A"},{"B<C","C<B"},{"x<y","y<x"},{"A^x<B^y","B^y<A^x"}): continue
        sub=[s for s in S if all(HYP[h](*s) for h in hyps)]
        if len(sub)<40: continue                # non-vacuous
        for c,f in CON.items():
            if all(f(*s) for s in sub) and not implied_by_known(hyps,c):
                cands.append((hyps,c,len(sub)))
print("true, non-vacuous, not-yet-proved implications on the model:",len(cands))

# --- Jev routes which to prove ---------------------------------------------------------
CTX=("Beal counterexample A^x+B^y=C^z, x,y,z>=3, gcd(A,B,C)=1. Already kernel-verified: pairwise coprime bases; A!=B; "
 "exactly one base even; if A^x<=B^y then B^y<C^z<=2B^y; C largest base => z<=max(x,y); C smallest base => z>max(x,y); "
 "C<=B => y<z. The statement below is TRUE on every solution with bases<=60 and exponents<=12 (exponents 1,2 included).")
Q={
 "provable": jev.score("Is this a THEOREM about all Beal counterexamples (not a small-model artifact), provable elementarily?",
   ["level 0: almost surely a finite-model artifact","level 1: plausibly true but hard","level 2: true and provable with some work","level 3: true and a few lines from the verified facts"]),
 "payoff": jev.score("How much does this add beyond the verified facts listed?",
   ["level 0: trivially implied by them","level 1: a small refinement","level 2: a genuinely new necessary condition","level 3: excludes an infinite family of signatures"]),
}
states=[{"context":CTX,"statement":f"IF {' AND '.join(h)} THEN {c}","support":n} for h,c,n in cands]
rs=jev.ask_many(states,Q,concurrency=12)
rows=[]
for (h,c,n),st,r in zip(cands,states,rs):
    if "error" in r: continue
    jev.persist("C040",st,Q,r); a=r["answers"]
    rows.append((round(a["provable"]["score"],2),round(a["payoff"]["score"],2),n,st["statement"]))
rows.sort(key=lambda t:-(t[0]*t[1]))
Path("research/pool/evidence/conjecture_mill_ranking.json").write_text(json.dumps(rows,indent=2))
print(f"\n{'prov':>5}{'pay':>5}{'supp':>6}  statement")
for t in rows[:25]: print(f"{t[0]:>5}{t[1]:>5}{t[2]:>6}  {t[3]}")
print(f"\nJev-ranked {len(rows)} machine-generated true statements")
