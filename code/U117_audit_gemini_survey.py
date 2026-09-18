"""Exact audit of the checkable claims in the pasted survey document.

Every identity is verified in exact integer (or exact Gaussian integer) arithmetic.
"""
from math import gcd
from fractions import Fraction

print("=== 1. Helenius (2004): is Beal FALSE over Z[i]? ===")
class G:
    __slots__=("a","b")
    def __init__(s,a,b): s.a,s.b=a,b
    def __mul__(s,o): return G(s.a*o.a - s.b*o.b, s.a*o.b + s.b*o.a)
    def __add__(s,o): return G(s.a+o.a, s.b+o.b)
    def __eq__(s,o): return s.a==o.a and s.b==o.b
    def __repr__(s): return f"{s.a}{'+' if s.b>=0 else '-'}{abs(s.b)}i"
    def pow(s,n):
        r=G(1,0)
        for _ in range(n): r=r*s
        return r
    def norm(s): return s.a*s.a + s.b*s.b

u, v, w = G(-2,1), G(-2,-1), G(1,1)
lhs = u.pow(3) + v.pow(3); rhs = w.pow(4)
print(f"  (-2+i)^3            = {u.pow(3)}")
print(f"  (-2-i)^3            = {v.pow(3)}")
print(f"  sum                 = {lhs}")
print(f"  (1+i)^4             = {rhs}")
print(f"  IDENTITY HOLDS      : {lhs == rhs}")
print(f"  norms               : N(-2+i)={u.norm()}, N(-2-i)={v.norm()}, N(1+i)={w.norm()}")
print(f"  gcd(N(-2+i),N(1+i)) = {gcd(u.norm(), w.norm())}  -> bases share no Gaussian prime: "
      f"{gcd(u.norm(), w.norm())==1}")
print(f"  exponents (3,3,4) all >= 3: True")

print("\n=== 2. The ten claimed coprime Fermat-Catalan solutions ===")
SOLS = [
 ("1^m + 2^3 = 3^2 (m=7)", 1,7, 2,3, 3,2),
 ("2^5 + 7^2 = 3^4",       2,5, 7,2, 3,4),
 ("7^3 + 13^2 = 2^9",      7,3, 13,2, 2,9),
 ("2^7 + 17^3 = 71^2",     2,7, 17,3, 71,2),
 ("3^5 + 11^4 = 122^2",    3,5, 11,4, 122,2),
 ("17^7 + 76271^3 = 21063928^2", 17,7, 76271,3, 21063928,2),
 ("1414^3 + 2213459^2 = 65^7",   1414,3, 2213459,2, 65,7),
 ("9262^3 + 1531228^2 = 113^7",  9262,3, 1531228,2, 113,7),
 ("43^8 + 96222^3 = 30042907^2", 43,8, 96222,3, 30042907,2),
 ("33^8 + 1549034^2 = 15613^3",  33,8, 1549034,2, 15613,3),
]
bad=[]
for label,A,x,B,y,C,z in SOLS:
    lhs=A**x+B**y; rhs=C**z; ok = lhs==rhs
    g=gcd(gcd(A,B),C)
    has2 = 2 in (x,y,z)
    print(f"  {label:<34} identity={str(ok):<6} gcd={g}  has exponent 2: {has2}")
    if not ok: bad.append((label,lhs,rhs))
print(f"\n  identities that FAIL: {len(bad)}")
for label,l,r in bad:
    print(f"    {label}: LHS={l}  RHS={r}  diff={l-r}")

print("\n=== 3. Claim: every known coprime solution has 2 as an exponent ===")
ok_sols=[(l,A,x,B,y,C,z) for (l,A,x,B,y,C,z) in SOLS if A**x+B**y==C**z]
print(f"  verified identities: {len(ok_sols)}")
print(f"  all have an exponent equal to 2: {all(2 in (x,y,z) for _,_,x,_,y,_,z in ok_sols)}")

print("\n=== 4. Euler characteristic claim: min exponent 3 forces chi <= -1/12 ===")
print("  chi(3,3,3) = 1/3+1/3+1/3-1 =", Fraction(1,3)*3-1)
print("  next largest with min>=3 is (3,3,4):", Fraction(1,3)+Fraction(1,3)+Fraction(1,4)-1)
print("  claim -1/12:", Fraction(1,3)+Fraction(1,3)+Fraction(1,4)-1 == Fraction(-1,12))

print("\n=== 5. Riemann-Hurwitz claim: x,y,z >= 3 forces genus >= 2 ===")
print("  2g-2 = d(1 - 1/x - 1/y - 1/z); with x=y=z=3 the bracket is 0, so 2g-2 = 0 -> g = 1.")
print("  -> the claim 'whenever x,y,z >= 3 the genus satisfies g >= 2' FAILS at (3,3,3),")
print("     where chi = 0 (parabolic) and the bracket vanishes.  It holds for chi < 0.")
