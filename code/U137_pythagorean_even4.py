"""U137 — exact checks for the all-even mechanism on signature (2m, 4, 2k).
Setup: A^{2m} + B^4 = C^{2k}, gcd=1, so (A^m, B^2, C^k) is a primitive Pythagorean triple; C^k odd.
Case E (B even): A^m = r^2 - s^2, B^2 = 2rs, C^k = r^2 + s^2, gcd(r,s)=1, opposite parity.
  B^2 = 2rs => {r,s} = {2p^2, q^2}; r-s = a^m, r+s = b^m (coprime odd) => a^m + b^m = 2r, b^m - a^m = 2s.
  r even: a^m + b^m = 4p^2   (sum of two coprime m-th powers is a square: (m,m,2), Darmon-Merel/Poonen for m>=4)
  s even: a^m + b^m = 2q^2   (Bennett-Skinner Thm 1.1, C=2, m>=4: only (5,3,-1) and (4,1,-1), neither positive)
Checks: (i) the parametrisation identities on all primitive triples; (ii) the two auxiliary equations have
NO positive coprime solutions in a box for m>=4 but DO for m=3 (so the m>=4 restriction is real);
(iii) exact search for actual (2m,4,2k) solutions with exponent 2 allowed to see the A-even case is live."""
from math import gcd, isqrt
def ppow_root(n,k):
    lo,hi=1,1<<(n.bit_length()//k+1)
    while lo<hi:
        mid=(lo+hi)//2
        if mid**k<n: lo=mid+1
        else: hi=mid
    return lo if lo**k==n else None
# (i) primitive triples: X odd, Y even
bad=0; tot=0
for r in range(1,120):
  for s in range(1,r):
    if gcd(r,s)!=1 or (r+s)%2==0: continue
    X,Y,Z=r*r-s*s,2*r*s,r*r+s*s; tot+=1
    if X*X+Y*Y!=Z*Z or gcd(X,Y)!=1 or Z%2==0: bad+=1
print("primitive triples:",tot,"identity/oddness violations:",bad)
# (ii) auxiliary equations, positive coprime odd a<b
for m in (3,4,5,6,7):
    s1=[(a,b) for a in range(1,200,2) for b in range(a+2,200,2) if gcd(a,b)==1 and (a**m+b**m)%4==0 and isqrt((a**m+b**m)//4)**2==(a**m+b**m)//4]
    s2=[(a,b) for a in range(1,200,2) for b in range(a+2,200,2) if gcd(a,b)==1 and isqrt((a**m+b**m)//2)**2==(a**m+b**m)//2]
    print(f"m={m}: a^m+b^m=4p^2 solutions {s1[:4]} ({len(s1)});  a^m+b^m=2q^2 solutions {s2[:4]} ({len(s2)})")
# (iii) actual solutions A^{2m}+B^4=C^{2k} (exponents >=2 allowed) with B even vs A even
sols=[]
for A in range(1,400):
  for B in range(1,400):
    if gcd(A,B)!=1: continue
    for m in range(1,7):
      v=A**(2*m)+B**4
      z=isqrt(v)
      if z*z!=v: continue
      for k in range(1,9):
        C=ppow_root(z,k) if k>1 else z
        if C: sols.append((A,B,C,2*m,4,2*k,"B even" if B%2==0 else "A even"))
print("model solutions A^{2m}+B^4=C^{2k}, coprime, bases<400:",sols)
