"""U213 exact test: Fermat-quotient Wronskian W_p = a*d(b) - b*d(a), d(u)=(u-u^p)/p, for a+b=c coprime.
Claim tested: abc | W_p ALWAYS (any coprime a+b=c, p odd, p∤abc) => carries no perfect-power / exponent information => BLIND."""
from math import gcd
FC=[(1,2**3,3**2),(2**5,7**2,3**4),(7**3,13**2,2**9),(2**7,17**3,71**2),(3**5,11**4,122**2),(33**8,1549034**2,15613**3),
    (1414**3,2213459**2,65**7),(9262**3,15312283**2,113**7),(17**7,76271**3,21063928**2),(43**8,96222**3,30042907**2)]
GEN=[(a,b,a+b) for a in range(1,40) for b in range(a,40) if gcd(a,b)==1]   # arbitrary non-power triples
def ok(a,b,c,p):
    if (a*b*c)%p==0: return None
    d=lambda u:(u-u**p)//p
    W=a*d(b)-b*d(a); return W%(a*b*c)==0
for name,S in(("FermatCatalan",FC),("generic",GEN)):
    res=[ok(a,b,c,p) for a,b,c in S for p in(3,5,7,11,13)]; res=[r for r in res if r is not None]
    print(name,len(res),"tests, all divisible:",all(res))
