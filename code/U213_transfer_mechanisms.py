"""U213 — Jev sweep OUTSIDE the survey's four dead categories and outside C083 (Darmon program).
Theme: Beal is a THEOREM over k[t] (Mason-Stothers). Which transfer mechanisms from the function-field proof to Z are
(a) not in the survey, (b) forced to fail over Z[i] (Helenius), (c) sensitive to exponent 2 (Fermat-Catalan), (d) testable here.
8 mechanisms x 8 Z-specific inputs x 6 constraints = 384 cells."""
import itertools, json, sys
sys.path.insert(0,'[LOCAL_HOME]/Downloads/beal/code'); import jev
MECH=["an arithmetic derivative (Buium p-derivation delta_p x=(x-x^p)/p... Fermat quotient) replacing d/dt in the Wronskian proof of Mason-Stothers",
 "a Wronskian-type determinant built from Fermat quotients at several primes simultaneously","a Belyi map attached to A^x/C^z and its dessin's monodromy in the triangle group",
 "the tilting/perfectoid correspondence moving the equation to characteristic p where Mason-Stothers holds","a model-theoretic transfer (Ax-Kochen style, ultraproduct of F_p[[t]] vs Z_p) of the polynomial theorem",
 "the Frobenius-lift obstruction: Z has no derivation but has Frobenius lifts on Z_p; compare delta_p(A^x)+delta_p(B^y)+carry = delta_p(C^z)","a Szpiro-type inequality for the specific elliptic curve with j-invariant built from A^x/C^z, proved only for THIS family via its extra perfect-power structure",
 "descent on the exponent lattice: a map (x,y,z)->(x',y',z') producing a smaller coprime solution"]
ZIN=["the archimedean ordering C^z>max(A^x,B^y)","units of Z are only +-1 (Z[i] has i, Z[t] over k has k*)","unique real embedding / product formula with ONE archimedean place","2 is the only even prime and is ramified in Z[i] but A,B,C parity is forced in Z",
 "the carry term in delta_p(a+b)=delta_p a+delta_p b+C_p(a,b)","class number and unit rank both trivial","Z is the initial ring (no base field to differentiate over)","the height equals log max exactly (no regulator contribution)"]
CONS=["must be false for the Helenius Z[i] identity (-2+i)^3+(-2-i)^3=(1+i)^4","must fail on at least one exponent-2 Fermat-Catalan identity such as 2^7+17^3=71^2","must yield an exact integer identity or inequality checkable in Python on known data",
 "must not be a reformulation of abc, Baker bounds, a congruence sieve, or a single-signature Frey curve","must not fix any base or restrict exponents to a finite list","must produce a statement that could be formalised in Lean with mathlib"]
CTX=("Beal conjecture research. A supplied survey lists as FAILED: bounded computation/sieves, signature-by-signature modular method, elementary congruence arguments, abc/Baker. "
 "The analogue over k[t] is a theorem (Mason-Stothers via Wronskian/derivation). Beal is FALSE over Z[i]. Judge each cell (mechanism, Z-specific input, constraint) as a concrete research statement.")
Q={"known_dead":jev.noul("Is this cell already known to fail or to be equivalent to abc/Szpiro in full strength (so no easier than the open problem)?",true="known dead or abc-equivalent",false="not known dead"),
   "uses_input":jev.noul("Does the mechanism genuinely USE the Z-specific input, in a way that would break over Z[i]?",true="uses it, breaks over Z[i]",false="does not use it"),
   "testable":jev.noul("Can the constraint be tested exactly with Python/PARI/Lean on small known data?",true="testable",false="not testable"),
   "new":jev.score("Distance from the survey's failed list",["identical to a listed failed method","reworded listed method","adjacent but not listed","genuinely not in the survey"])}
cells=list(itertools.product(MECH,ZIN,CONS))
rs=jev.ask_many([{"context":CTX,"mechanism":m,"z_input":z,"constraint":c} for m,z,c in cells],Q,concurrency=16)
rows=[]
for (m,z,c),r in zip(cells,rs):
    if "error" in r: continue
    a=r["answers"]; rows.append((round((1-a["known_dead"]["noul"])*a["uses_input"]["noul"]*a["testable"]["noul"]*a["new"]["score"],3),m,z,c))
rows.sort(reverse=True)
json.dump(rows,open("[LOCAL_HOME]/Downloads/beal/research/pool/evidence/transfer_mechanisms_U213.json","w"),indent=1)
print(len(rows),"cells")
for r in rows[:12]: print(r[0],"|",r[1][:60],"|",r[2][:50],"|",r[3][:40])
from collections import defaultdict
d=defaultdict(list)
for s,m,z,c in rows: d[m[:50]].append(s)
for k,v in sorted(d.items(),key=lambda kv:-sum(kv[1])/len(kv[1])): print(round(sum(v)/len(v),3),k)
