"""U190 — Jev at real scale on the open core: 10 objects x 10 operations x 10 inputs = 1000 cells."""
import itertools, json, sys
sys.path.insert(0,'[LOCAL_HOME]/Downloads/beal/code'); import jev
OBJ=["the cubic term A^3 in (3,5,7)","the fourth power A^4 in (4,5,7)","the difference C^r - B^q of two odd-prime powers","the sum A^p + B^q with p != q","the pair (A+B, cofactor) when two exponents share a factor after regrouping",
 "the Mordell curve Y^2 = X^3 + k obtained by fixing one term","the triple of residues mod a prime l = 1 mod pqr","the 2-adic and 3-adic valuations of the three terms","the ratio log C / log B forced by z log C ~ y log B","a hypothetical MINIMAL counterexample (smallest C^z)"]
OP=["factor over a quadratic or cyclotomic ring where it splits","map to an elliptic curve over Q and compute its rank in PARI","recognise as an instance of a solved lower signature after a substitution","derive a second independent equation and intersect","run an exact bounded search that tests a named structural hypothesis",
 "apply Lifting-the-Exponent to pin a valuation","build a descent step producing a smaller solution","compare with the ten Fermat-Catalan solutions to see which property they have that exponent>=3 forbids","count solutions mod l and look for a forced zero","feed to a conjecture mill: generate statements, filter exactly, prove survivors in Lean"]
INP=["both summands are perfect powers","exactly one base is even (kernel-verified)","C^z <= 2 max(A^x,B^y) (kernel-verified)","the dominant-term dichotomy z<=x iff A<C","pairwise coprimality of the bases",
 "the closed instance rows (PSS, Siksek-Stoll, BEN, Darmon-Merel)","Mihailescu's theorem (Catalan)","rank-0 elliptic curves from LMFDB","Z[i] / Z[omega] reductions already in the kernel","nothing beyond the equation itself"]
CTX=("Beal open core: (3,5,7),(4,5,7), (4,q,r) q!=r, (p,q,r) distinct odd primes. Tools: Lean4+mathlib, PARI/GP over Q (ellrank, thue, mf), exact Python. "
 "DEAD (do not re-propose): local sieves; FC-blind elementary conditions; one-sided identities z>=7; mixed-exponent Frey curves; Baker with two unknown bases; genus>=2 without elliptic quotients.")
Q={"concrete":jev.noul("Does this cell name a CONCRETE computation or lemma that could be started today?",true="concrete",false="vague"),
   "not_dead":jev.noul("Is it genuinely outside every DEAD route listed?",true="outside",false="a dead route reworded"),
   "could_close":jev.score("Best realistic outcome",["nothing","a recorded obstruction","a new necessary condition that is NOT exponent-2-blind","closure of one open signature or an infinite open family"])}
cells=list(itertools.product(OBJ,OP,INP))
rs=jev.ask_many([{"context":CTX,"object":o,"operation":p,"input":i} for o,p,i in cells],Q,concurrency=16)
rows=[]
for (o,p,i),r in zip(cells,rs):
    if "error" in r: continue
    a=r["answers"]; s=a["concrete"]["noul"]*a["not_dead"]["noul"]*a["could_close"]["score"]
    rows.append((round(s,3),o,p,i))
rows.sort(reverse=True)
json.dump(rows,open("[LOCAL_HOME]/Downloads/beal/research/pool/evidence/jev_1000_U190.json","w"),indent=1)
print(len(rows),"cells scored")
for r in rows[:15]: print(r[0],"|",r[1][:44],"|",r[2][:58],"|",r[3][:40])
