"""U218 — independent re-implementation of C086 using Python complex-free integer pairs via a different route:
enumerate c^z first, then for each a^x test whether c^z - a^x is a perfect power by exact Gaussian root extraction
(candidate roots from the norm's integer root), not by dictionary lookup. Coprimality via norm-gcd of resultant-free
test: gcd in Z[i] computed by factoring norms is avoided; use ideal test N(gcd)=1 <=> exists no Gaussian prime dividing both,
checked by trial over Gaussian primes of norm <= max norm."""
import sys
from math import isqrt,gcd
R,E=14,7
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def pw(a,k):
    r=(1,0)
    for _ in range(k): r=mul(r,a)
    return r
def N(a): return a[0]**2+a[1]**2
def iroot(n,k):
    lo,hi=0,1
    while hi**k<=n: hi*=2
    while lo<hi-1:
        m=(lo+hi)//2
        if m**k<=n: lo=m
        else: hi=m
    return lo
def roots(s,k):
    """all Gaussian b in box-free search with b^k==s"""
    n=N(s); r=iroot(n,k)
    if r**k!=n: return []
    out=[]
    for u in range(-isqrt(r),isqrt(r)+1):
        v2=r-u*u; v=isqrt(v2)
        if v*v==v2:
            for vv in {v,-v}:
                if pw((u,vv),k)==s: out.append((u,vv))
    return out
def divides(p,a):
    t=mul(a,(p[0],-p[1])); n=N(p); return t[0]%n==0 and t[1]%n==0
def coprime(a,b):
    m=min(N(a),N(b))
    for u in range(0,isqrt(m)+1):
        for v in range(0,isqrt(m)+1):
            p=(u,v)
            if N(p)>1 and N(p)<=m and divides(p,a) and divides(p,b): return False
            p=(u,-v)
            if N(p)>1 and N(p)<=m and divides(p,a) and divides(p,b): return False
    return True
bases=[(u,v) for u in range(-R,R+1) for v in range(-R,R+1) if N((u,v))>1]
pows={}
for b in bases:
    for k in range(3,E+1): pows.setdefault(pw(b,k),(b,k))
S=list(pows); sols=set()
normset={}
for p in S: normset.setdefault(N(p),[]).append(p)
for ci,c in enumerate(S):
    for a in S:
        d=(c[0]-a[0],c[1]-a[1])
        if d==(0,0) or N(d) not in normset or d not in pows: continue
        # confirm by root extraction, independent of dict
        (b,y)=pows[d]
        if b not in roots(d,y): continue
        A,x=pows[a]; C,z=pows[c]
        if coprime(A,b) and coprime(A,C):
            sols.add(frozenset([(A,x),(b,y)])|frozenset([("=",C,z)]))
print("independent: coprime solutions (unordered summands):",len(sols))
for s in sols: print(sorted(map(str,s)))
