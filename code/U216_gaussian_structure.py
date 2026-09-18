"""U216 — COUNTERSEARCH, named hypothesis H216: every coprime solution of a^x+b^y=c^z over Z[i] with x,y,z>=3
(bases in a box) has conjugate-symmetric summands (b^y = conj(a^x) up to unit) — i.e. the Z[i] failure is a TRACE trick
with no Z analogue.  Exact Gaussian arithmetic. Box: |re|,|im|<=R, exponents 3..E."""
import sys
from math import gcd
R,E=int(sys.argv[1]),int(sys.argv[2])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def N(a): return a[0]*a[0]+a[1]*a[1]
bases=[(u,v) for u in range(-R,R+1) for v in range(-R,R+1) if N((u,v))>1]
P={}
for b in bases:
    p=mul(mul(b,b),b)
    for k in range(3,E+1):
        P.setdefault(p,[]).append((b,k)); p=mul(p,b)
keys=list(P); found=[]
units=[(1,0),(-1,0),(0,1),(0,-1)]
for i,p in enumerate(keys):
    for q in keys[i:]:
        s=(p[0]+q[0],p[1]+q[1])
        if s in P:
            a,x=P[p][0]; b,y=P[q][0]; c,z=P[s][0]
            if gcd(gcd(N(a),N(b)),N(c))!=1: continue   # sufficient for coprimality; (misses coprime with shared norm primes — see below)
            found.append((a,x,b,y,c,z))
# second pass: allow shared norm primes but require Gaussian gcd 1
def ggcd(a,b):
    while b!=(0,0):
        n=N(b); t=mul(a,(b[0],-b[1])); qx=(2*t[0]+n)//(2*n); qy=(2*t[1]+n)//(2*n)
        r=(a[0]-(qx*b[0]-qy*b[1]),a[1]-(qx*b[1]+qy*b[0])); a,b=b,r
    return a
sols=[]
for i,p in enumerate(keys):
    for q in keys[i:]:
        s=(p[0]+q[0],p[1]+q[1])
        if s in P and s!=(0,0):
            a,x=P[p][0]; b,y=P[q][0]; c,z=P[s][0]
            if N(ggcd(a,b))==1 and N(ggcd(a,c))==1:
                conj=any(mul(u,(p[0],-p[1]))==q for u in units)
                sols.append((a,x,b,y,c,z,conj))
print("box R=%d E=%d: powers %d, coprime solutions %d, conjugate-symmetric %d"%(R,E,len(keys),len(sols),sum(s[-1] for s in sols)))
for s in [t for t in sols if not t[-1]][:15]: print("NON-CONJ",s)
