"""U252 — RESTART. The pool has converged on ONE obstruction: no Frey-type object attached to
A^x+B^y=C^z for three INDEPENDENT exponents (C083, C110, C111, C117 all terminate there).
This sweep asks only: what would such an object have to be, and is any candidate testable here?
Each cell is filtered by the gate-2 generator (must be false for a generic coprime a+b=c) and by
the requirement that it degenerate when an exponent is 2."""
import itertools,json,sys
sys.path.insert(0,'code'); import jev
OBJ=["a motive over Q whose Hodge numbers depend on all three of x,y,z",
 "an abelian variety of GL_2-type over the compositum Q(zeta_x, zeta_y, zeta_z)",
 "the fibre product of the three cyclic covers y^x = t, y^y = 1-t, y^z = t/(t-1) over the thrice-punctured line",
 "a rigid local system on P^1 minus {0,1,inf} with local monodromy of orders x, y, z (Katz middle convolution)",
 "the Jacobian of the smooth projective model of u^x + v^y = 1 pulled back along t = A^x/C^z",
 "a Shimura curve / quaternionic form attached to the triangle group Delta(x,y,z)",
 "the Kummer-type variety Spec Q[U,V,W]/(U^x+V^y-W^z) with its Galois descent data",
 "a perverse sheaf / D-module whose characteristic cycle records (x,y,z)"]
PROP=["its L-function has a functional equation whose conductor involves A,B,C symmetrically",
 "it specialises to the classical Frey curve when two of the three exponents coincide",
 "its mod-p representation is irreducible for p larger than an effective bound in x,y,z",
 "it degenerates exactly when 1/x+1/y+1/z >= 1",
 "it is defined over Q, not merely over a field growing with the exponents",
 "its dimension is bounded independently of x,y,z",
 "it admits a modularity lifting theorem already in the literature",
 "level lowering applies and the lowered level is independent of A,B,C"]
CONS=["must be FALSE for a generic coprime a+b=c with non-power terms (gate 2)",
 "must degenerate when an exponent equals 2, so it separates Fermat-Catalan (gate 1)",
 "must not require a Frey curve for a single fixed signature",
 "must be constructible, at least in one small case, with PARI/GP or Lean here",
 "must not presuppose Darmon's Big Image Conjecture or any unproved modularity",
 "must be stated over Q or a field of bounded degree"]
CTX=("Beal. The SINGLE obstruction on which this pool has converged: there is no known Frey-type object for three "
 "INDEPENDENT exponents. Darmon's program proposes hypergeometric abelian varieties but needs unproved modularity and "
 "big-image inputs (pool C083). Every milestone claiming a universal reduction failed precisely here (C110, C111, C117). "
 "Two gates apply: gate 1, the statement must fail on at least one of the ten exponent-2 Fermat-Catalan solutions; "
 "gate 2, its proof must use the equation A^x+B^y=C^z, not merely the exponent bounds.")
Q={"exists_in_lit":jev.noul("Is an object of this description ALREADY constructed in the literature (not merely conjectured)?",true="already constructed",false="not constructed"),
 "needs_unproved":jev.noul("Would using it require an unproved modularity or big-image conjecture?",true="needs unproved input",false="no unproved input"),
 "testable":jev.noul("Could a SMALL CASE of it be constructed or checked exactly with PARI/GP or Lean here, at zero budget?",true="testable here",false="not testable here")}
cells=list(itertools.product(OBJ,PROP,CONS))
rs=jev.ask_many([{"context":CTX,"object":o,"property":p,"constraint":c} for o,p,c in cells],Q,concurrency=16)
rows=[]
for (o,p,c),r in zip(cells,rs):
    if 'answers' not in r: continue
    a={k:round(v['noul'],2) for k,v in r['answers'].items()}
    rows.append((round((1-a['needs_unproved'])*a['testable'],3),a,o,p,c))
rows.sort(key=lambda r:-r[0])
json.dump({"status":"HYPOTHESIS_ONLY","rows":rows},open('research/pool/evidence/three_exponent_object_U252.json','w'),indent=1)
print(len(rows),"cells")
for s,a,o,p,c in rows[:8]: print(s,a,"|",o[:48],"|",p[:44])
