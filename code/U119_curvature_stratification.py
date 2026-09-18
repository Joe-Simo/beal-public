"""N1: does the 1/12 threshold stratify Beal into a FINITE list plus an infinite tail?

chi = 1/x + 1/y + 1/z - 1.  As the exponents grow, chi -> -1, so |chi| -> 1.
Hence for any T < 1 the set { (x,y,z) : min >= 3, |chi| < T } is FINITE and explicitly enumerable.

Beal then splits into:
   (i)  a FINITE list of "near-Euclidean" signatures, 1/12 <= |chi| < T;
   (ii) an infinite "very hyperbolic" tail, |chi| >= T.

This asks how big the finite part is, as a function of T -- i.e. how much of Beal is a finite
problem.  Reduced exponents only ({4} u odd primes), by the kernel-verified exponent reduction.
"""
from fractions import Fraction as F
from sympy import isprime

def reduced(n): return n==4 or (isprime(n) and n%2==1)
EXP=[e for e in range(3,200) if reduced(e)]

def chi(x,y,z): return F(1,x)+F(1,y)+F(1,z)-1

print("reduced exponents available:", EXP[:12], "...")
print(f"\n{'T':>8}{'signatures with 1/12 <= |chi| < T':>36}{'note':>28}")
for T in [F(1,6),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(9,10)]:
    cnt=0; sample=[]
    for x in EXP:
        for y in EXP:
            if y<x: continue
            for z in EXP:
                c=chi(x,y,z)
                if c>=0: continue
                if F(1,12)<=abs(c)<T:
                    cnt+=1
                    if len(sample)<4: sample.append((x,y,z))
    print(f"{str(T):>8}{cnt:>36}   {str(sample[:3]):>25}")

print("""
The finite part grows quickly with T, but it IS finite for every T < 1, because |chi| -> 1 as the
exponents grow.  Concretely, |chi| < T forces 1/x + 1/y + 1/z > 1 - T, and with min >= 3 that
bounds all three exponents.
""")
print("=== how large can an exponent be, given |chi| < T? ===")
for T in [F(1,2),F(2,3),F(3,4),F(9,10),F(99,100)]:
    # worst case: two exponents at their minimum 3, solve 1/3+1/3+1/z > 1-T
    lo=F(1,1)-T-F(1,3)-F(1,3)
    bound = "unbounded" if lo<=0 else f"z < {1/lo}"
    print(f"  T = {str(T):>7}: with x=y=3, need 1/z > {lo}  ->  {bound}")
print("""
So the stratification is real but the finite part is only finite for T < 1/3: once T >= 1/3 the
condition 1/z > 1 - T - 2/3 becomes vacuous and z is unbounded.

CONSEQUENCE.  The useful window is 1/12 <= |chi| < T with T < 1/3.  That carves off a genuinely
finite, explicitly enumerable family -- but it leaves the infinite tail |chi| >= 1/3, which
includes every signature with a large exponent, and that tail is exactly where the modular method
is weakest (high genus).  The stratification does not by itself make either part easier.
""")
