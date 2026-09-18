"""U231 — exact test of the top U230 cell: 'the Galois action on the set of z-th roots of A^x+B^y'.
Concrete content: T^z - (A^x+B^y) has a rational root, so its splitting field is Q(zeta_z) of degree
phi(z) instead of the generic z*phi(z). GATE-2 TEST: is this FALSE for a generic coprime triple
a+b=c whose terms are NOT perfect powers? If it holds there too, the cell carries no Beal content."""
from math import gcd
def is_perfect_power(n):
    if n<2: return n==1
    for k in range(2,n.bit_length()+1):
        lo,hi=1,1
        while hi**k<=n: hi*=2
        while lo<hi-1:
            m=(lo+hi)//2
            if m**k<=n: lo=m
            else: hi=m
        if lo**k==n: return True
    return False
def zth_power(n,z):
    lo,hi=1,1
    while hi**z<=n: hi*=2
    while lo<hi-1:
        m=(lo+hi)//2
        if m**z<=n: lo=m
        else: hi=m
    return lo**z==n
print("GATE-2 TEST: coprime a+b=c with c a perfect z-th power (z>=3) and a,b NOT perfect powers.")
print("If such triples exist, the Galois/splitting-field condition holds for them too -> no Beal content.\n")
found=[]
for c_root in range(2,60):
  for z in (3,4,5):
    c=c_root**z
    for a in range(2,min(c,4000)):
      b=c-a
      if b<2 or gcd(a,b)!=1: continue
      if not is_perfect_power(a) and not is_perfect_power(b):
        found.append((a,b,c,c_root,z)); break
    if len(found)>=6: break
  if len(found)>=6: break
for a,b,c,r,z in found[:6]:
    print("  %d + %d = %d = %d^%d   a perfect power:%s  b perfect power:%s  T^%d-c has rational root:%s"
          %(a,b,c,r,z,is_perfect_power(a),is_perfect_power(b),z,zth_power(c,z)))
print("\nverdict: the condition holds on %d generic non-power triples -> FAILS gate 2 (proof would not"%len(found[:6]))
print("need the perfect-power structure of A^x and B^y; it only sees that the SUM is a z-th power).")
