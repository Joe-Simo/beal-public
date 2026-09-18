"""U169 — Jev sweep aimed at the smallest open reduced signatures, with the U167 lessons built in."""
import itertools, json, sys
sys.path.insert(0,'[LOCAL_HOME]/Downloads/beal/code'); import jev
TARGETS=["(3,5,7): A^3+B^5=C^7 and arrangements","(4,5,7): A^4+B^5=C^7 and arrangements","(3,4,11) unconditionally (literature is GRH-conditional via (2,3,11))","(3,5,11)"]
MECH=["instance of a closed lower signature after grouping exponents (e.g. 4 = 2*2) and moving odd-exponent terms",
 "factor the difference of the two odd-exponent terms over Z[zeta_p] and use that the third term is a perfect power",
 "even hyperelliptic curve with elliptic quotients of rank 0 (PARI)","Frey curve over Q with classical newform elimination (PARI mf) for THIS signature",
 "reduce to a Thue or Thue-Mahler equation of small degree solvable by PARI thue()","descent via a 2-isogeny or 3-isogeny on an attached elliptic curve",
 "use the known (2,3,7)/(2,3,n) solution lists through a substitution making one term a square or cube",
 "local-global: show the attached curve has no points over some Q_p (exact enumeration)"]
CTX="Beal frontier after U168. Tools: Lean4+mathlib, PARI/GP (ellrank, mf over Q, thue, hyperellratpoints), exact Python. No Chabauty/Magma/Sage."
Q={"runnable":jev.noul("Can this be turned into a concrete PARI/Lean/Python computation TODAY that could DECIDE something?",true="yes",false="no"),
   "known_dead":jev.noul("Is this mechanism known in the literature to FAIL for this signature (e.g. no Frey curve over Q for (3,5,7))?",true="known to fail",false="not known to fail"),
   "first_step":jev.choice("Cheapest first step",{"pari":"a PARI computation","lit":"a literature lookup","derive":"a hand derivation","none":"nothing runnable"})}
cells=list(itertools.product(TARGETS,MECH))
rs=jev.ask_many([{"context":CTX,"target":t,"mechanism":m} for t,m in cells],Q,concurrency=12)
rows=[]
for (t,m),r in zip(cells,rs):
    if "error" in r: continue
    a=r["answers"]; rows.append((round(a["runnable"]["noul"]*(1-a["known_dead"]["noul"]),3),a["first_step"]["choice"],t[:12],m[:95]))
rows.sort(reverse=True)
json.dump(rows,open("[LOCAL_HOME]/Downloads/beal/research/pool/evidence/frontier_cells_U169.json","w"),indent=1)
for r in rows[:10]: print(r)
