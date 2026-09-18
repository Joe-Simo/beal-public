"""U222 — exact test of the top U221 cell: rad(ABC) compared to A^x,B^y,C^z SEPARATELY.
Derivation to be checked numerically:
  coprime A^x+B^y=C^z, x,y,z>=3  =>  rad(abc)=rad(ABC)<=ABC<=(abc)^(1/3), and ab<=c^2/4, so
  rad <= (c^3/4)^(1/3) = c/4^(1/3), i.e. quality q=log c/log rad >= 1/(1-log(4^(1/3))/log c) -> 1.
Exponent-2 comparison: with one exponent 2 only rad<=(abc)^(1/2) follows, so the condition is NOT blind.
Exact integer arithmetic; floats only for reporting q."""
from math import gcd, log
def rad(n):
    r=1; d=2
    while d*d<=n:
        if n%d==0:
            r*=d
            while n%d==0: n//=d
        d+=1
    return r*(n if n>1 else 1)
FC=[(1,1,2,3,3,2),(2,5,7,2,3,4),(7,3,13,2,2,9),(2,7,17,3,71,2),(3,5,11,4,122,2),
    (33,8,1549034,2,15613,3),(1414,3,2213459,2,65,7),(9262,3,15312283,2,113,7),
    (17,7,76271,3,21063928,2),(43,8,96222,3,30042907,2)]
print("Fermat-Catalan (all have an exponent 2):")
for A,x,B,y,C,z in FC:
    a,b,c=A**x,B**y,C**z
    assert a+b==c and gcd(gcd(A,B),C)==1
    R=rad(a*b*c); assert R==rad(A*B*C)
    q=log(c)/log(R) if R>1 else float('inf')
    third = R**3<=a*b*c            # does rad<=(abc)^(1/3) hold here?
    print("  (%d,%d,%d) exps(%d,%d,%d) q=%.4f  rad^3<=abc: %s"%(A,B,C,x,y,z,q,third))
print("\nCheck the two inequalities on coprime NON-power triples (control) and on exponent>=3 triples:")
ok3=True
for A in range(2,40):
  for B in range(2,40):
    for x in (3,4,5):
      for y in (3,4,5):
        a,b=A**x,B**y; c=a+b
        if gcd(A,B)!=1: continue
        # ABC <= (abc)^(1/3) requires C^3<=c, i.e. C=c^(1/z) with z>=3; test the A,B part only:
        if not (A**3<=a and B**3<=b): ok3=False
print("  A^3<=A^x and B^3<=B^y for x,y>=3:",ok3)
print("\nSharp bound: ab<=c^2/4 for a+b=c  =>  abc<=c^3/4  =>  rad<=c/4^(1/3)=c/%.4f"%(4**(1/3)))
print("  so q>=1/(1-log(4^(1/3))/log c); at c=10^50 this is q>=%.6f  (vacuous)"%(1/(1-log(4**(1/3))/log(10**50))))
