"""M2: why is the exponent 2 distinguished?  A sharp separation in the Euler characteristic.

chi(p,q,r) = 1/p + 1/q + 1/r - 1.  Exact rational arithmetic throughout.

CLAIM A: every Beal signature (min exponent >= 3) that is hyperbolic has |chi| >= 1/12,
         with equality exactly at the permutations of (3,3,4).
CLAIM B: every one of the known primitive hyperbolic solutions has |chi| < 1/12.

If both hold, the known solutions and the Beal region are SEPARATED by the single value 1/12,
and the role of the exponent 2 is quantitative: it is what allows |chi| to be small.
"""
from fractions import Fraction as F
from itertools import product

def chi(p,q,r): return F(1,p)+F(1,q)+F(1,r)-1

print("=== CLAIM A: hyperbolic Beal signatures all have |chi| >= 1/12 ===")
worst=None; ties=[]
for p,q,r in product(range(3,40), repeat=3):
    c=chi(p,q,r)
    if c==0: continue                      # (3,3,3), parabolic
    if c>0: print("  *** spherical with min>=3:",(p,q,r)); continue
    if worst is None or abs(c)<abs(worst[1]): worst=((p,q,r),c)
for p,q,r in product(range(3,40), repeat=3):
    if chi(p,q,r)==F(-1,12): ties.append((p,q,r))
print(f"  smallest |chi| over min>=3 hyperbolic: {worst[1]} at {worst[0]}  -> |chi| = {abs(worst[1])}")
print(f"  attained exactly at: {sorted(set(tuple(sorted(t)) for t in ties))}")
print(f"  so every hyperbolic Beal signature has |chi| >= 1/12 = {float(F(1,12)):.6f}: "
      f"{abs(worst[1])==F(1,12)}")

print("\n=== CLAIM B: the known primitive hyperbolic solutions ===")
KNOWN=[("1^m+2^3=3^2 (m=7)",(7,3,2)),("2^5+7^2=3^4",(5,2,4)),("7^3+13^2=2^9",(3,2,9)),
       ("2^7+17^3=71^2",(7,3,2)),("3^5+11^4=122^2",(5,4,2)),
       ("17^7+76271^3=21063928^2",(7,3,2)),("1414^3+2213459^2=65^7",(3,2,7)),
       ("9262^3+15312283^2=113^7",(3,2,7)),("43^8+96222^3=30042907^2",(8,3,2)),
       ("33^8+1549034^2=15613^3",(8,2,3))]
allbelow=True
print(f"{'solution':<30}{'signature':>12}{'chi':>10}{'|chi|':>10}{'< 1/12?':>9}")
for lbl,sig in KNOWN:
    c=chi(*sig); ok=abs(c)<F(1,12); allbelow&=ok
    print(f"{lbl:<30}{str(sig):>12}{str(c):>10}{str(abs(c)):>10}{str(ok):>9}")
print(f"\n  every known solution has |chi| < 1/12: {allbelow}")

print(f"""
=== CONCLUSION (M2) ===
The two regions are SEPARATED by the single rational number 1/12:

    known primitive hyperbolic solutions :  |chi| <= 1/18  (all of them)
    hyperbolic Beal signatures           :  |chi| >= 1/12  (all of them, min at (3,3,4))

and 1/18 < 1/12.  There is a genuine GAP, with no known solution in it.

This is what distinguishes the exponent 2 quantitatively: an exponent 2 contributes 1/2 to the
reciprocal sum, which is what permits |chi| to stay below 1/12.  With every exponent >= 3 the
reciprocal sum cannot exceed 1, and once it is below 1 it is at most 11/12.

HONEST STATUS: this is an OBSERVED separation about the known solution set plus an EXACT fact
about the Beal region.  It is not a proof that no solution exists with |chi| >= 1/12 -- that is
precisely Beal's conjecture.  It sharpens the question rather than answering it.
""")
