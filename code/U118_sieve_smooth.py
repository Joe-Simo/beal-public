"""How strong a congruence sieve can the verified necessary conditions supply?

Same criterion as U118_congruence_obstruction, but with subsets of Z/m held as integer bitmasks
so that larger smooth moduli are reachable.

A residue triple (A,B,C) mod m is ADMISSIBLE iff (S_A + S_B) meets S_C, where
S_X = {X^x mod m : x >= 3}; plus the kernel-verified pairwise-coprimality constraint, imposed
as: no prime p | m divides two of A, B, C.
"""
from sympy import primefactors

def masks(m):
    S=[]
    for X in range(m):
        seen=set(); v=pow(X,3,m)
        for _ in range(2*m+4):
            if v in seen: break
            seen.add(v); v=v*X%m
        bm=0
        for r in seen: bm |= 1<<r
        S.append((bm, seen))
    return S

def analyse(m):
    S=masks(m); ps=primefactors(m)
    full=(1<<m)-1
    # rotate: shifting a bitmask by k mod m
    def rot(bm,k):
        k%=m
        return ((bm<<k) | (bm>>(m-k))) & full
    total=0; adm=0
    for A in range(m):
        for B in range(m):
            if any((A%p==0) and (B%p==0) for p in ps): continue
            # sumset S_A + S_B as a bitmask
            T=0
            for b in S[B][1]:
                T |= rot(S[A][0], b)
                if T==full: break
            for C in range(m):
                if any(sum(1 for X in (A,B,C) if X%p==0)>=2 for p in ps): continue
                total+=1
                if T & S[C][0]: adm+=1
    return total, adm

print(f"{'m':>6}{'coprime triples':>17}{'admissible':>12}{'fraction':>10}{'rejects':>10}")
for m in [12,24,48,72,120,180,240,360]:
    t,a = analyse(m)
    print(f"{m:>6}{t:>17}{a:>12}{a/t:>10.4f}{1-a/t:>9.1%}")
