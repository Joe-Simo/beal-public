"""Cycle U130 — Jev screen FIRST: every pool candidate against the primary-source literature state
(arXiv 2412.11933 survey, fetched and saved in references/U130/). Solved families with all exponents>=3:
(3,3,n) n<=1e9; (n,n,3) n>=3 [Darmon-Merel, Poonen]; (n,n,n) [Wiles]; (n,n,2) n>=5 (exponent 2, not Beal).
(4,4,3) is therefore SOLVED via (n,n,3). No (2m,2n,r) family with m!=n is listed as solved.
Jev routes: which candidates are subsumed, which touch an open family, which should be re-targeted."""
import json, sys; sys.path.insert(0,'code'); import jev
from pathlib import Path
db=json.load(open('research/pool/candidates.json'))['candidates']
LIT=("Literature (primary source arXiv:2412.11933, survey of solved cases): fully solved with all exponents>=3 are "
 "(3,3,n) for n<=10^9, (n,n,3) for n>=3, (n,n,n) for n>=3. Effective-finiteness only (not solved): (2p,2q,r) with "
 "p,q>=V_r [arXiv:2509.21083]. NOT solved: (4,4,5), (4,4,7), (4,6,3), any (2m,2n,r odd) with m!=n, (3,5,7), (5,5,7).")
Q={
 "subsumed":jev.noul("Is this candidate's claim ENTIRELY implied by the solved families listed?",true="yes, fully subsumed",false="no, it says something about open signatures"),
 "touches_open":jev.score("How directly does this candidate bear on a signature family the literature leaves OPEN?",
   ["level 0: not at all","level 1: tangentially","level 2: it is a necessary condition on an open family","level 3: it reduces or reformulates an open family"]),
 "retarget":jev.choice("Best next action for this candidate given the literature.",
   {"close":"mark DUPLICATE of a literature result","keep":"keep as necessary condition","sharpen":"restrict it to the open families and sharpen","combine":"combine with the (2m,2n,z odd) Z[i] reduction (C045)"}),
}
states=[{"literature":LIT,"id":c["id"],"status":c["status"],"claim":c["claim"][:600]} for c in db]
rs=jev.ask_many(states,Q,concurrency=12)
rows=[]
for st,r in zip(states,rs):
    if "error" in r: continue
    jev.persist("lit_screen_"+st["id"],st,Q,r); a=r["answers"]
    rows.append((st["id"],round(a["subsumed"]["noul"],2),round(a["touches_open"]["score"],2),a["retarget"]["choice"],round(a["retarget"]["confidence"],2)))
Path("research/pool/evidence/literature_subsumption_screen.json").write_text(json.dumps(rows,indent=1))
print(f"{'id':<6}{'subsumed':>9}{'open':>6}  action (conf)")
for t in sorted(rows,key=lambda t:-t[2]): print(f"{t[0]:<6}{t[1]:>9}{t[2]:>6}  {t[3]} ({t[4]})")
print("\nsubsumed>0.6:",[t[0] for t in rows if t[1]>0.6])
print("route=combine:",[t[0] for t in rows if t[3]=="combine"])
