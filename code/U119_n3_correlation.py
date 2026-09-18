"""N3: are the local conditions at coprime moduli INDEPENDENT, or correlated?

If independent, the admissible fraction at m = m1*m2 (coprime) would be the PRODUCT of the
fractions at m1 and m2.  Any shortfall is genuine correlation -- the beginning of a combined
local obstruction that no single modulus exhibits, which is the phenomenon adelic/Brauer-Manin
methods are designed to capture.
"""
from sympy import primefactors
from math import prod

def frac(m):
    """admissible fraction at modulus m (same criterion as U118)."""
    S=[]
    for X in range(m):
        seen=set(); v=pow(X,3,m)
        for _ in range(2*m+4):
            if v in seen: break
            seen.add(v); v=v*X%m
        bm=0
        for r in seen: bm |= 1<<r
        S.append((bm,seen))
    ps=primefactors(m); full=(1<<m)-1
    def rot(bm,k):
        k%=m
        return ((bm<<k)|(bm>>(m-k)))&full
    tot=adm=0
    for A in range(m):
        for B in range(m):
            if any(A%p==0 and B%p==0 for p in ps): continue
            T=0
            for b in S[B][1]:
                T|=rot(S[A][0],b)
                if T==full: break
            for C in range(m):
                if any(sum(1 for X in (A,B,C) if X%p==0)>=2 for p in ps): continue
                tot+=1
                if T & S[C][0]: adm+=1
    return adm/tot

print("=== independence test: does f(m1*m2) = f(m1)*f(m2) for coprime m1, m2? ===\n")
print(f"{'m1':>5}{'m2':>5}{'f(m1)':>9}{'f(m2)':>9}{'product':>10}{'f(m1*m2)':>11}{'ratio':>9}")
CASES=[(8,9),(8,5),(9,5),(4,9),(8,27),(16,9),(8,25),(32,9)]
for m1,m2 in CASES:
    f1,f2=frac(m1),frac(m2); m=m1*m2
    fm=frac(m)
    print(f"{m1:>5}{m2:>5}{f1:>9.4f}{f2:>9.4f}{f1*f2:>10.4f}{fm:>11.4f}{fm/(f1*f2):>9.4f}")

print("\n=== three-factor ===")
for trip in [(8,9,5),(16,9,5),(8,27,5)]:
    fs=[frac(t) for t in trip]; m=prod(trip); fm=frac(m)
    print(f"  {trip}  product {prod(fs):.4f}   f(m)={fm:.4f}   ratio {fm/prod(fs):.4f}")

print("""
INTERPRETATION.  A ratio BELOW 1 means the conditions at the two moduli are positively
correlated as constraints: satisfying both is harder than independence predicts, so the
combined local condition carries information no single modulus does.  A ratio of exactly 1
would mean the moduli constrain independently and nothing is gained by combining.
""")
