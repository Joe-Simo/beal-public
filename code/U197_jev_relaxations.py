"""U197 — second large Jev sweep: WHAT to fix/relax x WHICH open signature x WHICH decidable object. 12x6x8 = 576 cells."""
import itertools, json, sys
sys.path.insert(0,'[LOCAL_HOME]/Downloads/beal/code'); import jev
FIX=["fix the base of the largest-exponent term","fix the base of the smallest-exponent term","fix two of the three bases (exponential equation in the exponents)","fix all prime factors of ABC to lie in a finite set S (S-unit equation)",
 "fix one base to be a prime power","fix the difference C - B","fix the ratio of two exponents","require one base to be a perfect square or cube (extra structure)","fix the residue of a base modulo a small prime AND its exponent class",
 "fix A = 1 or A = 2 (Catalan / Pillai type)","assume the counterexample is minimal in C^z and derive a smaller one","fix the 2-adic valuation pattern of the even base"]
SIG=["(3,5,7)","(4,5,7)","(3,5,r) r varying","(4,q,r) q != r","(p,q,r) distinct odd primes","(5,7,r) r varying"]
OBJ=["a genus-1 curve over Q (PARI ellrank)","a Thue or Thue-Mahler equation (PARI thue)","a finite exponential congruence sieve with a PROVED covering (exact)","a Pell/continued-fraction condition","a known theorem on perfect powers in recurrences or a^x - b^y = c (Mihailescu, Bennett, Bugeaud-Mignotte-Siksek)",
 "a rank-0 Jacobian quotient of a higher-genus curve","a classical-newform elimination over Q (PARI mf)","a Lean-provable elementary contradiction"]
CTX=("Beal open core. WORKED: fixing the base of the r-th power term turned {3,4,r} and (3,3,r) into rank-0 genus-1 curves closing all r at once. "
 "DEAD: local sieves without a covering proof; FC-blind elementary conditions; Chabauty/Hilbert/Q-curve machinery unavailable. Tools: Lean4, PARI/GP over Q, Python.")
Q={"decidable":jev.noul("After this fixing, does the problem become a DECIDABLE object of the named kind with the tools listed?",true="yes",false="no"),
   "reaches_open":jev.noul("Does the resulting statement say something about an OPEN signature (not an already closed one)?",true="open signature",false="already closed"),
   "all_exponents":jev.noul("Would it hold for infinitely many exponents at once (not one signature at a time)?",true="infinitely many",false="single case")}
cells=list(itertools.product(FIX,SIG,OBJ))
rs=jev.ask_many([{"context":CTX,"fix":f,"signature":s,"object":o} for f,s,o in cells],Q,concurrency=16)
rows=[]
for (f,s,o),r in zip(cells,rs):
    if "error" in r: continue
    a=r["answers"]; rows.append((round(a["decidable"]["noul"]*a["reaches_open"]["noul"]*(0.5+a["all_exponents"]["noul"]),3),f,s,o))
rows.sort(reverse=True)
json.dump(rows,open("[LOCAL_HOME]/Downloads/beal/research/pool/evidence/jev_relaxations_U197.json","w"),indent=1)
print(len(rows),"cells"); seen=set()
for sc,f,s,o in rows:
    k=(f,o)
    if k in seen: continue
    seen.add(k); print(sc,"|",f[:52],"|",s,"|",o[:52])
    if len(seen)>=12: break
