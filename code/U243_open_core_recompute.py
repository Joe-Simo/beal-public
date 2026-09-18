"""U243 (v2) — recompute the REDUCED open core exactly. Beal reduces to exponents in {4} u {odd primes}
(any exponent with a divisor d>=3 is replaced by d; 4 covers the 2-power case). Closures applied are
ONLY those with a source held in references/U130/ or a machine-checked theorem in formal/Beal/."""
from itertools import combinations_with_replacement
def primes(n):
    return [p for p in range(3,n+1) if all(p%d for d in range(2,int(p**.5)+1))]
RED=sorted(set([4]+primes(60)))
CLOSURES=[
 (lambda s: s[0]==s[1]==s[2],                              "(n,n,n) FLT — survey T1.1 [149,143]"),
 (lambda s: s[0]==s[1] and s[2]==3,                        "(n,n,3) — survey T1.1 [55,117]"),
 (lambda s: s[1]==s[2] and s[0]==3,                        "(n,n,3) perm"),
 (lambda s: s[0]==3 and s[1]==3 and s[2]<=10**9,           "(3,3,n), n<=1e9 — survey T1.1"),
 (lambda s: s==[3,4,5],                                    "(3,4,5) — survey T1.1 [133]"),
 (lambda s: s==[5,5,7] or s==[5,5,19] or s==[5,7,7],       "Dahmen-Siksek — survey T1.1 [50]"),
 (lambda s: s[0]==4 and s[1]==4,                           "(4,4,p) — BEN 2010 via x^2+y^4=z^n, BCDY T1 (2,4,n) n>=4"),
 (lambda s: s.count(4)==1 and s[0]==4 and s[1]==s[2],      "(4,p,p) — Darmon-Merel (n,n,2) route, repo ClosedFamilies"),
]
def closed(t):
    s=sorted(t)
    for f,lab in CLOSURES:
        try:
            if f(s): return lab
        except Exception: pass
    return None
openset=[]
for t in combinations_with_replacement(RED,3):
    if 1/t[0]+1/t[1]+1/t[2]>=1: continue
    if closed(t) is None: openset.append(t)
print("REDUCED signatures (exponents in {4} u odd primes <= 59), hyperbolic, NOT closed by a held source:")
print("total open in range:",len(openset))
print("smallest 12:",openset[:12])
print()
print("with a 4:", [t for t in openset if 4 in t][:10])
print("all odd primes:", [t for t in openset if 4 not in t][:10])
print()
print("Repo final_residual claims the open core is:")
print("  (4,q,r), q != r odd primes, except {3,4,5} and {3,4,7}")
print("  (p,q,r) odd primes not all equal, except (p,p,3) and the Dahmen-Siksek triples")
print("Cross-check of the two smallest repo claims against this recomputation:")
for t in [(3,5,7),(4,5,7),(3,4,7),(3,4,11)]:
    print("   ",t,"->", closed(t) or "OPEN")
