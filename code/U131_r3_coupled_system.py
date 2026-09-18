"""Cycle U131 — Jev-routed sub-family (2m,2n,3), m!=n (all OPEN per U130).
From C045 with r=3:  A^m = |u(u^2-3v^2)|,  B^n = |v(3u^2-v^2)|  (or swapped), gcd(u,v)=1, u+v odd.
Exact lemma: gcd(u, u^2-3v^2) = gcd(u,3) and gcd(v, 3u^2-v^2) = gcd(v,3); at most one of u,v is divisible by 3.
Named hypothesis H1: 'Re alone is rarely a perfect power' -- measure how often each factor is a perfect
power >=2 separately, and both together, over u,v<=2000.  Relaxation counts tell us whether the coupling
(both at once) is where the obstruction lives."""
from math import gcd
import json
def _iroot(n,k):
    lo,hi=1,1<<(n.bit_length()//k+1)
    while lo<hi:
        m=(lo+hi)//2
        if m**k<n: lo=m+1
        else: hi=m
    return lo if lo**k==n else None
PR=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
def ppow(n):
    if n<4: return n==1
    for k in PR:
        if k>n.bit_length(): return False
        if _iroot(n,k) is not None: return True
    return False
U=2000; re_only=im_only=both=tot=0; ex_re=[]; ex_im=[]
for u in range(1,U+1):
  for v in range(1,U+1):
    if gcd(u,v)!=1 or (u+v)%2==0: continue
    tot+=1
    a=abs(u*(u*u-3*v*v)); b=abs(v*(3*u*u-v*v))
    pa=a>1 and ppow(a); pb=b>1 and ppow(b)
    if pa: re_only+=1; ex_re.append((u,v,a)) if len(ex_re)<8 else None
    if pb: im_only+=1; ex_im.append((u,v,b)) if len(ex_im)<8 else None
    if pa and pb: both+=1; print("BOTH:",u,v,a,b)
print(f"pairs {tot}: Re perfect power {re_only}, Im perfect power {im_only}, both {both}")
print("Re examples:",ex_re); print("Im examples:",ex_im)
# the coupled system when 3 does not divide uv:  u=s^m, u^2-3v^2=+-t^m, v=p^n, 3u^2-v^2=+-q^n  =>  8 s^{2m} = +-3 q^n -+ t^m
json.dump({"U":U,"pairs":tot,"re":re_only,"im":im_only,"both":both,"re_ex":ex_re,"im_ex":ex_im},open("research/pool/evidence/r3_coupled_counts.json","w"))
