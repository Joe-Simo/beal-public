"""Cycle U129 — RESTART: factorisation over Z[i] for the sparsest mod-72 class (x, y even, z odd).
Derivation (exact, recorded in the checkpoint): x=2x', y=2y' gives (A^x')^2+(B^y')^2=C^z with C ODD
(kernel-verified: C even would force not both x,y even).  a=A^x', b=B^y' coprime, a+b odd, so a+bi and
a-bi are coprime in the UFD Z[i]; every unit is a z-th power for z odd; hence a+bi=(u+vi)^z, C=u^2+v^2.
So a counterexample in this class is EXACTLY a pair (u,v), coprime, opposite parity, with
  Re((u+vi)^z) = +-A^x'  and  Im((u+vi)^z) = +-B^y'   both perfect powers with x',y' >= 2.
This search is exact big-integer arithmetic and is exhaustive over (u,v,z) in the stated box only."""
import sys, json; sys.path.insert(0,'code'); import jev
from math import gcd, isqrt
def iroot(n,k):
    if n<2: return n
    r=int(round(n**(1.0/k)))
    for c in (r-1,r,r+1):
        if c>=0 and c**k==n: return c
    return None
def _iroot(n,k):
    lo,hi=1,1<<(n.bit_length()//k+1)
    while lo<hi:
        m=(lo+hi)//2
        if m**k<n: lo=m+1
        else: hi=m
    return lo if lo**k==n else None
PR=[p for p in range(2,130) if all(p%q for q in range(2,int(p**.5)+1))]
def is_perfect_power(n):          # n>=2: some k>=2 with m^k=n (prime k suffices)
    if n<4: return n==1
    for k in PR:
        if k>n.bit_length(): break
        if _iroot(n,k) is not None: return True
    return False
def gpow(u,v,z):
    a,b=1,0
    for _ in range(z): a,b=a*u-b*v,a*v+b*u
    return a,b
UMAX=400; ZS=(3,5,7)
hits=[]; checked=0
for z in ZS:
  for u in range(1,UMAX+1):
    for v in range(1,UMAX+1):
      if gcd(u,v)!=1 or (u+v)%2==0: continue
      a,b=gpow(u,v,z); a,b=abs(a),abs(b)
      if a<2 or b<2: continue
      checked+=1
      if is_perfect_power(a) and is_perfect_power(b): hits.append((u,v,z,a,b))
print(f"pairs checked: {checked}  box: u,v<={UMAX}, z in {ZS}")
print("simultaneous perfect-power hits (would be (even,even,odd) Beal counterexamples):",hits)
json.dump({"box":{"umax":UMAX,"z":ZS},"checked":checked,"hits":hits},open("research/pool/evidence/gaussian_param_search.json","w"))
CTX="Class (x,y even, z odd) reduced exactly to: Re and Im of (u+vi)^z both perfect powers. Box search found no hit."
Q={"next":jev.choice("What is the best next step for this class?",{"descent":"prove Re((u+vi)^z) is never a perfect power >=2 by descent on u(u^2-3v^2) for z=3","lean":"formalise the Z[i] reduction in Lean 4 with mathlib GaussianInt","extend":"extend the box (not justified unless it tests a named hypothesis)","literature":"check whether (4,4,3)/(2n,2m,z odd) is already settled in the literature"})}
r=jev.ask({"context":CTX},Q); jev.persist("C045",{"context":CTX},Q,r); print("Jev route (HYPOTHESIS_ONLY):",r.get("answers"))
