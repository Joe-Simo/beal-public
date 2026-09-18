"""M1: Is there a modulus m at which NO Beal counterexample can exist?

Structure.  For gcd(A,m)=1 the set {A^x mod m : x >= 3} equals the cyclic subgroup <A> of
(Z/m)^*, because x >= 3 already sweeps a full period of the powers of A.  If m | A then
A^x = 0 mod m for every x >= 1.

So a Beal counterexample forces, at every modulus m, the existence of
    a in S_A,  b in S_B,  c in S_C     with   a + b = c  (mod m),
where S_X = <X> if gcd(X,m)=1, and S_X = {0} if m | X, and otherwise S_X = {X^x mod m : x>=3}
computed directly.

We also impose the KERNEL-VERIFIED constraint that A, B, C are PAIRWISE COPRIME, which at a
prime power m = p^k means at most one of A, B, C is divisible by p.

A modulus at which no admissible residue triple exists would PROVE Beal.  Short of that, the
admissible fraction measures how much each modulus constrains a counterexample.
"""
from math import gcd
from sympy import primerange

def powers_set(X, m):
    """{X^x mod m : x >= 3}, computed exactly."""
    seen=set(); v=pow(X,3,m); 
    for _ in range(2*m+4):
        if v in seen: break
        seen.add(v); v = v*X % m
    return seen

def analyse(m):
    total=0; admissible=0; witness=None
    S=[powers_set(X,m) for X in range(m)]
    for A in range(m):
        for B in range(m):
            for C in range(m):
                # pairwise coprimality, reflected mod m for prime-power m:
                # at most one of A,B,C may be divisible by a prime dividing m
                ok_pair=True
                for p in set(f for f in range(2,m+1) if m%f==0 and all(f%q for q in range(2,f))):
                    cnt = sum(1 for X in (A,B,C) if X % p == 0)
                    if cnt >= 2: ok_pair=False; break
                if not ok_pair: continue
                total+=1
                hit=False
                for a in S[A]:
                    for b in S[B]:
                        if (a+b) % m in S[C]: hit=True; break
                    if hit: break
                if hit: admissible+=1
                elif witness is None: witness=(A,B,C)
    return total, admissible, witness

print(f"{'m':>5}{'coprime triples':>17}{'admissible':>12}{'fraction':>10}   obstruction?")
best=[]
for m in list(range(3,26)) + [27,32,49,64,81,121,125,128]:
    t,a,w = analyse(m)
    frac = a/t if t else 1.0
    flag = "*** NONE ADMISSIBLE -> PROOF ***" if a==0 else ("strong" if frac<0.5 else "")
    print(f"{m:>5}{t:>17}{a:>12}{frac:>10.3f}   {flag}")
    best.append((frac,m,t,a))
best.sort()
print("\nmost constraining moduli:")
for frac,m,t,a in best[:6]:
    print(f"  m={m:<4} admissible fraction {frac:.3f}  ({a}/{t})")
