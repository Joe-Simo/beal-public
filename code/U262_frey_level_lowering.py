"""U262 — the obstruction in the OTHER picture (the one C130 says rigidity does not bound):
the classical discriminant-valuation Frey curve. For a coprime a+b=c with a=A^x, b=B^y, c=C^z the
standard Frey curve  E : Y^2 = X(X - a)(X + b)  has  Delta = 16 (a b c)^2.
Ribet level lowering removes a prime l of multiplicative reduction from the conductor exactly when
p | v_l(Delta). By coprimality exactly one of A,B,C is divisible by l, so
   v_l(Delta) = 2 * (x*v_l(A) + y*v_l(B) + z*v_l(C)) with exactly one term nonzero.
Taking l with valuation 1 in its base, the three conditions are p|2x, p|2y, p|2z.
Exact integer check below."""
from math import gcd
def strips_all(p,x,y,z):
    return (2*x)%p==0 and (2*y)%p==0 and (2*z)%p==0
print("signature      gcd(x,y,z)  primes p>=3 that strip ALL bad primes   verdict")
SIGS=[(3,3,3),(3,3,5),(5,5,7),(3,4,5),(3,5,7),(4,5,7),(7,7,5),(6,6,6),(3,3,7),(4,4,5)]
for t in SIGS:
    x,y,z=t
    ps=[p for p in range(3,60) if all(p%d for d in range(2,int(p**.5)+1)) and strips_all(p,x,y,z)]
    print("%-14s %-11d %-38s %s"%(str(t),gcd(gcd(x,y),z),ps if ps else "NONE",
          "method applies" if ps else "level retains primes of the other two terms"))
print()
print("EXACT STATEMENT: p strips every bad prime iff p | 2x and p | 2y and p | 2z,")
print("i.e. iff p | 2*gcd(x,y,z). For p odd this is p | gcd(x,y,z).")
print("Check on the table:", all(
    ([p for p in range(3,60) if all(p%d for d in range(2,int(p**.5)+1)) and strips_all(p,*t)]
     == [p for p in range(3,60) if all(p%d for d in range(2,int(p**.5)+1)) and gcd(gcd(t[0],t[1]),t[2])%p==0])
    for t in SIGS))
print()
print("CONSEQUENCE: for three PAIRWISE COPRIME exponents, gcd(x,y,z) = 1, so NO odd prime strips")
print("all three; the lowered level still contains primes dividing the other two terms and is not")
print("bounded independently of the solution. Every published closure has gcd(x,y,z) > 1 or reduces")
print("to a signature that does:")
for t in SIGS:
    g=gcd(gcd(t[0],t[1]),t[2]); print("   %-12s gcd = %d  %s"%(str(t),g,"usable" if g>1 else "not usable directly"))
