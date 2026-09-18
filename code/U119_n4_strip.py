"""N4 / COUNTERSEARCH: is the strip 1/18 < |chi| < 1/12 actually mysterious?

C033 recorded that all ten known solutions have |chi| <= 1/18 while every Beal signature has
|chi| >= 1/12, and called the region between them a "gap containing no known solution".
That phrasing suggests something unexplained.  This tests it by enumerating the strip.
"""
from fractions import Fraction as F

def chi(x,y,z): return F(1,x)+F(1,y)+F(1,z)-1

LO,HI=F(1,18),F(1,12)
print(f"strip: {LO} < |chi| < {HI}   i.e.  {float(LO):.4f} < |chi| < {float(HI):.4f}\n")
sigs=[]
for x in range(2,60):
    for y in range(x,60):
        for z in range(2,200):
            c=chi(x,y,z)
            if c<0 and LO<abs(c)<HI: sigs.append((x,y,z,abs(c)))
print(f"signatures in the strip (x<=y, z<200): {len(sigs)}")
seen=set(); out=[]
for x,y,z,a in sorted(sigs,key=lambda t:t[3]):
    k=tuple(sorted((x,y,z)))
    if k in seen: continue
    seen.add(k); out.append((k,a))
print(f"distinct up to permutation: {len(out)}\n")
SOLVED={(2,3,7),(2,3,8),(2,3,9),(2,3,10),(2,3,15),(2,4,5),(2,5,5),(3,3,4),(2,3,11)}
print(f"{'signature':>14}{'|chi|':>10}   status")
for k,a in out[:18]:
    st = "SOLVED, no solutions" if k in SOLVED else "open or unlisted here"
    minexp=min(k)
    note = "  (min exp >= 3 -> Beal region!)" if minexp>=3 else ""
    print(f"{str(k):>14}{str(a):>10}   {st}{note}")

print(f"""
=== COUNTERSEARCH VERDICT ===
The strip is NOT empty and NOT mysterious: it contains {len(out)} signatures up to permutation,
every one of which has an exponent equal to 2 (so none is a Beal signature -- consistent with the
Beal region beginning at exactly 1/12).  Several, such as (2,3,10), are SOLVED with no solutions;
others are simply not in the ten-solution list because they have none or are unresolved.

So the correct statement is NOT "a mysterious gap".  It is:

    the ten known solutions happen to occupy the LOW-|chi| end of the non-Beal region,
    and the non-Beal region itself stops at 1/12 because an exponent 2 is what buys |chi| < 1/12.

The 1/12 threshold is real and exact (kernel-verified).  The "gap" framing in C033 overstated it.
""")
