#!/usr/bin/env python3
"""
U318: does dropping RIGIDITY rescue regularity?  Testing C174's first named escape.

THE ESCAPE UNDER TEST
---------------------
C174 showed that a RIGID, Q-rational local system on P^1 minus {0,1,infinity} carrying three
pairwise distinct Beal exponents is never regular, because rig = 2 plus regular semisimplicity at
two punctures forces a pseudoreflection at the third, and pseudoreflections are not Q-rational for
order >= 3.  C174 listed "non-rigid families" as the first untested escape: dropping rigidity costs
a moduli of dimension (n-1)(n-2), but it also removes the constraint that produced the
pseudoreflection.

So: WITHOUT the rigidity constraint, can a Q-rational local system be regular semisimple at all
three punctures with three pairwise distinct local orders?

THE EXACT CRITERION
-------------------
Regular semisimple at a puncture = partition (1^n): n distinct eigenvalues, every multiplicity 1.

Q-rationality = the eigenvalue multiset is a union of Galois orbits, the orbit of primitive d-th
roots having size phi(d), with all elements of an orbit sharing a multiplicity.  With every
multiplicity equal to 1, the multiset is a union of WHOLE orbits each taken once, so

    n = sum of phi(d) over a set D of divisors of m,    and order exactly m requires m in D.

Write S(m) for the set of such n.  A regular Q-rational system of rank n carrying orders p, q, r
needs n in S(p) and n in S(q) and n in S(r) simultaneously.

This criterion uses NO rigidity at all, so it applies to rigid and non-rigid systems alike.

Exact integer arithmetic; no floating point.

WHAT EITHER ANSWER MEANS
------------------------
EMPTY INTERSECTION for every pairwise distinct triple: the regularity obstruction is INDEPENDENT of
rigidity, and dropping rigidity does not rescue it.  C174's first escape closes, and the obstruction
becomes: over Q, regular weights and three distinct exponents are incompatible at any rank, for any
local system on the thrice-punctured line.

A NON-EMPTY INTERSECTION: the escape is real and the non-rigid direction deserves the next cycle.

Either way this proves nothing about Beal; it classifies an obstruction and tests one escape.
"""

from itertools import combinations


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def totient(m):
    return sum(1 for k in range(1, m + 1) if gcd(k, m) == 1)


def divisors(m):
    return [d for d in range(1, m + 1) if m % d == 0]


def regular_ranks(m, maxrank):
    """S(m): ranks n of a regular semisimple Q-rational monodromy of order exactly m.

    n = sum of phi(d) over a set D of divisors of m with m in D.
    """
    ds = divisors(m)
    others = [d for d in ds if d != m]
    base = totient(m)
    out = set()
    for k in range(len(others) + 1):
        for sub in combinations(others, k):
            n = base + sum(totient(d) for d in sub)
            if n <= maxrank:
                out.add(n)
    return out


def reduced_exponents(limit):
    out = []
    for m in range(3, limit + 1):
        if m == 4:
            out.append(4)
            continue
        if m % 2 == 0:
            continue
        if all(m % d for d in range(3, int(m ** 0.5) + 1, 2)):
            out.append(m)
    return sorted(out)


def main():
    EXPS = reduced_exponents(31)
    MAXRANK = 64
    print("=" * 78)
    print("U318: regularity over Q without the rigidity constraint")
    print("=" * 78)
    print(f"\nreduced exponents: {EXPS}      ranks considered: up to {MAXRANK}")

    print("\n[1] S(m) = ranks admitting a regular semisimple Q-rational monodromy of order m:")
    S = {}
    for m in EXPS:
        S[m] = regular_ranks(m, MAXRANK)
        print(f"   m={m:2d}: phi={totient(m):2d}, divisors={divisors(m)}, S(m)={sorted(S[m])}")

    print("\n[2] pairwise intersections S(p) ∩ S(q) for p != q:")
    for p, q in combinations(EXPS, 2):
        inter = sorted(S[p] & S[q])
        print(f"   S({p}) ∩ S({q}) = {inter if inter else 'EMPTY'}")

    print("\n[3] THE DECISIVE TEST: triples of pairwise distinct exponents with S(p)∩S(q)∩S(r) != {}")
    hits = []
    for p, q, r in combinations(EXPS, 3):
        inter = sorted(S[p] & S[q] & S[r])
        if inter:
            hits.append(((p, q, r), inter))
    if not hits:
        print(f"   NONE over all {len(list(combinations(EXPS, 3)))} triples from {EXPS}.")
    else:
        print(f"   {len(hits)} triple(s):")
        for t, inter in hits:
            print(f"      {t}: ranks {inter}")

    # --- control: the same test on triples that are NOT pairwise distinct ----------------
    print("\n[control] the test must SUCCEED when exponents may repeat, or it is vacuous:")
    ctl = []
    for p in EXPS:
        inter = sorted(S[p])
        if inter:
            ctl.append((p, inter[:3]))
    print(f"   equal-exponent triples (p,p,p) admit ranks: {ctl[:6]}  -> {'PASS' if ctl else 'VACUOUS'}")
    # and a mixed pair where one exponent is repeated
    mixed = [((p, p, q), sorted(S[p] & S[q])) for p, q in combinations(EXPS, 2)
             if S[p] & S[q]]
    print(f"   (p,p,q) triples with a nonempty rank set: {len(mixed)} of "
          f"{len(list(combinations(EXPS, 2)))} pairs; e.g. {mixed[:3]}")

    print("\n" + "=" * 78)
    if not hits:
        print("RESULT: EMPTY for every pairwise distinct triple.")
        print()
        print("The regularity obstruction does NOT depend on rigidity. A Q-rational local system on")
        print("the thrice-punctured line that is regular semisimple at all three punctures must have")
        print("rank n lying in S(p), S(q) and S(r) at once, and for pairwise distinct reduced")
        print("exponents those sets are disjoint -- because n is pinned to phi(m) plus a sum of")
        print("phi over proper divisors, which differs for different m. Dropping rigidity buys a")
        print("moduli of dimension (n-1)(n-2) and buys nothing here. C174's first escape closes.")
    else:
        print("RESULT: the non-rigid escape is REAL for the triples listed; next cycle should")
        print("test whether the Beal equation's single parameter can cut out such a family.")
    print()
    print("SCOPE: this is about local systems on P^1 minus three points, defined over Q, regular")
    print("semisimple at every puncture. It says nothing about irregular-weight objects, larger")
    print("base fields, or objects that are not local systems -- and nothing about Beal.")
    print("=" * 78)


if __name__ == "__main__":
    main()
