"""U212 — Jev at scale on the ONLY two directions the user's survey leaves open:
(L1) a single modular/motivic object attached to A^x+B^y=C^z for three INDEPENDENT exponents;
(L2) effective Diophantine geometry.  Generate concrete requirement-statements and screen them with two hard filters that can be
checked exactly afterwards: (F1) must FAIL over Z[i] (Helenius: Beal is false there), (F2) must distinguish exponent >= 3 from
exponent 2 (the ten Fermat-Catalan solutions).  8 objects x 8 properties x 6 constraints = 384 cells."""
import itertools, json, sys
sys.path.insert(0,'[LOCAL_HOME]/Downloads/beal/code'); import jev
OBJ=["a hypergeometric motive / Darmon's Frey representation of signature (p,q,r)","the Jacobian of the superelliptic curve y^p = x^q (1-x) type attached to the signature","a Frey abelian variety of GL2-type over Q(zeta_p,zeta_q,zeta_r)^+",
 "the orbifold P^1(p,q,r) and its triangle-group covers (Darmon-Granville)","an Artin representation of the triangle group Delta(p,q,r) reduced mod a prime","a family of curves over the (x,y,z)-exponent lattice with a common fibre",
 "the height pairing on a generalized Fermat surface","a p-adic period / Coleman integral attached to the descent curve"]
PROP=["its residual representation is irreducible for all large primes","its conductor is bounded independently of the solution","it is modular over a totally real field by a KNOWN modularity lifting theorem","level lowering removes all primes dividing ABC",
 "the space of newforms at the lowered level is computable and SMALL","it detects the real ordering C^z > max(A^x,B^y) (the one input that fails over Z[i])","it degenerates exactly when an exponent equals 2","it is functorial under the exponent reductions x -> x/d"]
CONS=["must be false for the Helenius solution (-2+i)^3+(-2-i)^3=(1+i)^4","must not hold for the ten Fermat-Catalan solutions","must be stated without fixing any base or exponent","must be checkable in a small case with PARI/GP over Q","must not rely on GRH or an unproved big-image conjecture","must survive the residual/isogeny conflation trap (CLAUDE.md failure mode 1)"]
CTX=("Beal. The user's survey says every tried method fails: bounded computation, signature-by-signature modular method, elementary arguments, abc/Baker. "
 "The survey's only live directions: a unifying modular/motivic object for THREE independent exponents, or effective Diophantine geometry. Judge each cell as a concrete research statement.")
Q={"known_obstruction":jev.noul("Is there a KNOWN theorem or obstruction in the literature that already rules this cell out (e.g. Darmon: Frey representations for general (p,q,r) are not known to be modular; no unconditional big-image result)?",true="known obstruction",false="no known obstruction"),
   "testable":jev.noul("Can the constraint be TESTED exactly on a small case with the tools here (PARI/GP over Q, Lean, Python)?",true="testable here",false="not testable here"),
   "new":jev.score("How far is this from what the survey lists as tried?",["identical to a listed failed method","a reworded listed method","adjacent but not listed","genuinely not in the survey"])}
cells=list(itertools.product(OBJ,PROP,CONS))
rs=jev.ask_many([{"context":CTX,"object":o,"property":p,"constraint":c} for o,p,c in cells],Q,concurrency=16)
rows=[]
for (o,p,c),r in zip(cells,rs):
    if "error" in r: continue
    a=r["answers"]; rows.append((round((1-a["known_obstruction"]["noul"])*a["testable"]["noul"]*a["new"]["score"],3),o,p,c))
rows.sort(reverse=True)
json.dump(rows,open("[LOCAL_HOME]/Downloads/beal/research/pool/evidence/live_directions_U212.json","w"),indent=1)
print(len(rows),"cells"); 
for r in rows[:10]: print(r[0],"|",r[1][:50],"|",r[2][:55],"|",r[3][:45])
