"""U166 — Jev-at-scale mechanism generation aimed ONLY at the residual core, with tools restricted to
what is executable here (Lean 4 + mathlib, PARI/GP over Q: elliptic-curve ranks, 2-descent, classical
newforms; exact Python). 8 tools x 6 targets x 6 angles = 288 cells."""
import itertools, json, sys
from pathlib import Path
sys.path.insert(0,'code'); import jev
TOOLS=["rank-0 elliptic curve over Q (PARI ellrank)","genus-1 quartic with local obstruction","one-sided published ternary theorem (Bennett-Skinner / Ivorra / Kraus / Darmon-Merel)",
 "factorisation in Z[i] or Z[omega] or Z[sqrt2] with both summands powers","classical newform elimination over Q (PARI mf)","Lifting-the-Exponent / p-adic valuation split",
 "descent to a smaller solution of the same signature","exponent-divisibility pullback to a closed family"]
TARGETS=["(4,4,p), p>=7","(4,p,q), p!=q odd primes","(3,3,p) beyond 10^9 classes","(p,p,r), p>=5, r>=5","(3,p,q) with 3 in the signature","(p,q,r) distinct odd primes >=5"]
ANGLES=["use that TWO terms are perfect powers of known exponent","use the exponent-4 term as a square of a square","move a term across (odd exponent allows sign change)","treat the smallest exponent side only","combine two closed conditional families","look for an accidental low-degree identity"]
CTX=("Beal residual core after U165. CLOSED (conditionally): (even,even,3k), (4k,even,5j), (n,n,2k), (4,p,p), (3,3,2k), (p,p,p), (p,p,3). "
 "DEAD: local sieves, height gap, elementary FC-blind conditions, one-sided identity for z>=7, genus>=2 curves (no Chabauty here), Hilbert modular forms, Q-curves.")
Q={"executable":jev.noul("Can this cell be turned into a concrete computation or Lean proof with ONLY the listed tool, today?",true="yes, concrete and runnable",false="no, needs unavailable machinery"),
   "not_dead":jev.noul("Is this cell genuinely different from every DEAD route listed?",true="different",false="a dead route reworded"),
   "payoff":jev.score("If it works, what does it close?",["nothing new","one signature","an infinite family conditional on published theorems","an infinite family of REDUCED signatures in the residual core"])}
cells=list(itertools.product(TOOLS,TARGETS,ANGLES))
rs=jev.ask_many([{"context":CTX,"tool":t,"target":g,"angle":a} for t,g,a in cells],Q,concurrency=12)
rows=[]
for (t,g,a),r in zip(cells,rs):
    if "error" in r: continue
    x=r["answers"]; rows.append({"tool":t,"target":g,"angle":a,"exec":round(x["executable"]["noul"],2),"new":round(x["not_dead"]["noul"],2),"payoff":round(x["payoff"]["score"],2)})
for r in rows: r["s"]=round(r["exec"]*r["new"]*r["payoff"],3)
rows.sort(key=lambda r:-r["s"])
Path("research/pool/evidence/residual_mechanism_space_U166.json").write_text(json.dumps({"state":"HYPOTHESIS_ONLY","rows":rows},indent=1))
print(len(rows),"cells ranked"); 
for r in rows[:14]: print(f"{r['s']:.3f} | {r['tool'][:44]:<44} | {r['target']:<28} | {r['angle'][:48]}")
