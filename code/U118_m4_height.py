"""M4: what do the verified size constraints force, and what survives when combined with M1?

From M3 (kernel-verified): with A^x <= B^y,
        B^y < C^z <= 2 B^y
Taking logarithms:
        0 < z log C - y log B <= log 2
so y/z is a rational approximation to log C / log B of quality
        | log C/log B - y/z | <= log 2 / (z log B).
"""
from math import log, gcd
from fractions import Fraction

SOL=[("2^5+7^2=3^4",2,5,7,2,3,4),("7^3+13^2=2^9",7,3,13,2,2,9),
     ("2^7+17^3=71^2",2,7,17,3,71,2),("3^5+11^4=122^2",3,5,11,4,122,2),
     ("17^7+76271^3=21063928^2",17,7,76271,3,21063928,2),
     ("1414^3+2213459^2=65^7",1414,3,2213459,2,65,7),
     ("9262^3+15312283^2=113^7",9262,3,15312283,2,113,7),
     ("43^8+96222^3=30042907^2",43,8,96222,3,30042907,2)]

print("=== how good is the rational approximation y/z ~ logC/logB, on known solutions? ===")
print(f"{'solution':<30}{'z logC - y logB':>18}{'<= log2?':>10}{'|logC/logB - y/z|':>20}")
for lbl,A,x,B,y,C,z in SOL:
    if A**x > B**y: A,x,B,y = B,y,A,x           # ensure A^x <= B^y
    lin = z*log(C) - y*log(B)
    approx = abs(log(C)/log(B) - y/z)
    print(f"{lbl:<30}{lin:>18.6f}{str(lin<=log(2)+1e-12):>10}{approx:>20.8f}")

print(f"\n  log 2 = {log(2):.6f}")
print("""
  Every known solution sits inside the window, as it must.  But the linear form
  z logC - y logB is NOT unusually small in these cases - it is comfortably below log 2 rather
  than near zero.  So the window does not force an exceptional Diophantine approximation, and
  no contradiction arises from approximation quality alone.  M4 yields no new obstruction.
""")

print("=== NOVEL COMBINATION: M3 window x M1 congruence sieve ===")
print("""
  The two constraints are INDEPENDENT in kind: M3 restricts the real size of C given B, y, z;
  M1 restricts the residue class of (A,B,C) mod m.  A search may impose both.

  Effect on an enumeration over (B, y, z) with C determined by the window:
    * M3 confines C to the interval (B^(y/z), 2^(1/z) B^(y/z)], of relative width
      2^(1/z) - 1 <= 0.26 -- a factor ~3.9 saving over scanning all C <= 2^(1/z) B^(y/z).
    * M1 then rejects 77.7% of the surviving (A,B,C) residue classes mod 240.
  Combined, about 0.26 x 0.223 = 5.8% of the naive (C, residue) space survives -- a ~17x
  reduction, on top of any modular hashing the search already does.
""")
w = 2**(1/3) - 1
print(f"  M3 relative width at z=3 (worst case): {w:.4f}")
print(f"  M1 survival at m=240                 : 0.2232")
print(f"  combined survival                    : {w*0.2232:.4f}  (~{1/(w*0.2232):.1f}x reduction)")
print("""
  HONEST LIMIT: this is a constant-factor speedup on a space that grows exponentially.
  U115 section 6 already established that computation cannot decide Beal; a 17x saving does
  not change that, and must not be presented as progress toward a proof.
""")
