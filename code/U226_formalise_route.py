"""U226 — Jev routing: which unconditional fact in the pool is worth formalising next in Lean?
Narrow questions only; HYPOTHESIS_ONLY."""
import json,sys
sys.path.insert(0,'code'); import jev
CAND={
 "rad3":"rad(A^x B^y C^z) = rad(ABC) <= ABC <= (abc)^(1/3), hence rad(abc)^3 <= abc, for any Beal counterexample (C088). Non-blind: fails on 4 of the 10 Fermat-Catalan solutions.",
 "radc":"rad(abc) <= C^z / 4^(1/3), from ab <= c^2/4 (C088).",
 "trace":"Gaussian cubic trace family: w^3+conj(w)^3 = 2u(u^2-3v^2) = +-2^k with gcd(u,v)=1, u+v odd forces (u,v)=(+-2,+-1) (C086).",
 "wronsk":"abc | a*d_p(b) - b*d_p(a) for coprime a+b=c, p odd, p not dividing abc (C084).",
 "isogeny":"for coprime a+b=c the triple ((a-b)^2, 4ab, c^2) is again an abc-triple (C085).",
 "window":"C^z > max(A^x,B^y) and C^z < 2*max(A^x,B^y) for any Beal counterexample (no-cancellation window)."}
CTX=("Beal repo, Lean 4 + mathlib v4.14.0. Goal: add machine-checked UNCONDITIONAL necessary conditions on a Beal "
 "counterexample. mathlib has Nat.factorization, Nat.primeFactors, Nat.Coprime, and UniqueFactorizationMonoid.radical. "
 "A condition is valuable only if it is NOT exponent-2-blind (does not hold on all ten Fermat-Catalan solutions).")
Q={"mathlib_ready":jev.noul("Can this be stated and proved in Lean 4 with mathlib v4.14.0 using existing API (Nat.factorization / primeFactors / radical), without new theory?",true="mathlib-ready",false="needs new theory"),
 "nonblind":jev.noul("Does this condition FAIL on at least one of the ten Fermat-Catalan solutions (i.e. it is not exponent-2-blind)?",true="non-blind",false="blind"),
 "uses_all_three":jev.noul("Does the statement genuinely use all three exponents x,y,z being >=3?",true="uses all three",false="does not")}
rs=jev.ask_many([{"context":CTX,"fact":v} for v in CAND.values()],Q,concurrency=6)
out=[]
for k,r in zip(CAND,rs):
    a={q:round(v['noul'],2) for q,v in r['answers'].items()}
    out.append((round(a['mathlib_ready']*a['nonblind']*a['uses_all_three'],3),k,a))
out.sort(reverse=True)
json.dump({"status":"HYPOTHESIS_ONLY","rows":out},open('research/pool/evidence/formalise_route_U226.json','w'),indent=1)
for s,k,a in out: print(s,k,a)
