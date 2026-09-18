#!/usr/bin/env python3
"""
U319: does a larger base field rescue regularity?  Testing C174/C175's second named escape.

THE ESCAPE UNDER TEST
---------------------
C175 closed the "non-rigid families" escape: over Q, regular semisimplicity at a puncture of order
m pins the rank to the interval [phi(m), m], and for three pairwise distinct reduced exponents
those intervals are disjoint, rigidity or no rigidity.

The next named escape is a larger base field K.  Over K the relevant group is Gal(K(zeta_m)/K), a
subgroup H_m of (Z/m)*, and the orbits of primitive m-th roots have size |H_m| exactly (the action
is free).  So the minimal rank of a regular semisimple K-rational monodromy of order m is |H_m|,
and

    |H_m| = phi(m) / [K cap Q(zeta_m) : Q]   >=   phi(m) / [K : Q].

Widening K shrinks the orbits and widens the admissible rank interval.  The question is HOW MUCH
field is needed -- whether the escape is cheap or whether it costs so much that it is no better
than the obstruction it dodges.

TWO MEASURES, BOTH COMPUTED EXACTLY
-----------------------------------
1. The EXPENSIVE reading: if K is asked to contain all three roots of unity, every orbit becomes a
   singleton and any rank >= 3 works, but [K:Q] >= phi(lcm(p,q,r)) = (p-1)(q-1)(r-1) for distinct
   primes.  That is the quantity already machine-checked as `Beal.minBaseDegree_le_triple` and
   `Beal.totient_mul_primes` in `formal/Beal/Rigidity.lean`.

2. The CHEAP reading, which is the honest one: K only has to shrink the largest exponent's orbit
   enough to meet the smallest exponent's rank ceiling, which needs only

       [K : Q] >= phi(r) / p.

Exact integer arithmetic; no floating point.

WHY THIS MATTERS FOR THE RECORD
-------------------------------
If measure 2 is small, the escape is REAL and C174/C175 must not be stated as if the regularity
obstruction were field-independent.  Reporting only measure 1 would overstate the obstruction in
exactly the way U258 was overstated before U309 caught it.
"""

from itertools import combinations
from math import ceil


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def totient(m):
    return sum(1 for k in range(1, m + 1) if gcd(k, m) == 1)


def lcm(a, b):
    return a * b // gcd(a, b)


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
    E = reduced_exponents(19)
    triples = list(combinations(E, 3))
    print("=" * 78)
    print("U319: the cost of the larger-base-field escape")
    print("=" * 78)

    print("\n[measure 1] K contains all three roots of unity: [K:Q] >= phi(lcm(p,q,r))")
    all_eq = True
    worst = 0
    for t in triples:
        L = lcm(t[0], lcm(t[1], t[2]))
        ph = totient(L)
        prod = 1
        for m in t:
            prod *= totient(m)
        all_eq &= (ph == prod)
        worst = max(worst, ph)
    print(f"   phi(lcm) = product of phi over the triple, for all {len(triples)} triples: {all_eq}")
    print(f"   range: {min(totient(lcm(t[0], lcm(t[1], t[2]))) for t in triples)} "
          f"to {worst} over exponents up to 19 -- grows like the product, so this reading is "
          f"expensive.")

    print("\n[measure 2] K only shrinks the largest orbit to the smallest ceiling:")
    print("            [K:Q] >= phi(r)/p, where p < q < r")
    costs = []
    for t in triples:
        p, q, r = sorted(t)
        costs.append((tuple(sorted(t)), ceil(totient(r) / p)))
    mx = max(c for _, c in costs)
    mn = min(c for _, c in costs)
    print(f"   required degree ranges from {mn} to {mx} over the same triples.")
    print("   examples:")
    for t, c in costs[:6]:
        print(f"      {t}: [K:Q] >= {c}")
    for t, c in costs[-4:]:
        print(f"      {t}: [K:Q] >= {c}")

    print("\n" + "=" * 78)
    print("RESULT: the two measures disagree by orders of magnitude, and MEASURE 2 IS THE BINDING")
    print(f"ONE. A field of degree as small as {mn}-{mx} already reconciles the ranks. So the")
    print("larger-base-field escape is REAL: the regularity obstruction of C174/C175 is a")
    print("statement about Q, not a field-independent fact, and must be recorded as such.")
    print()
    print("What the escape does NOT do: over K the modular method still needs automorphy of an")
    print("n-dimensional motive with n > 2 (C171), now over K rather than Q, which is harder and")
    print("not easier. The escape moves the problem; it does not remove it. This is why the")
    print("(5,5,p) literature works over Q(sqrt 5) at rank 2 and stops there.")
    print("=" * 78)


if __name__ == "__main__":
    main()
