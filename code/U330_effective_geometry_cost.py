#!/usr/bin/env python3
"""
U330: RESTART into effective Diophantine geometry -- what does it actually cost?

WHY THIS DIRECTION
------------------
C184 recorded the pool-convergence condition: the obstruction line C169-C176 has collapsed onto one
mechanism, and the Jev pairwise screen found no combination inside it that discharges an obligation
of another.  The exploration loop names RESTART for exactly this.  The survey
(`research/checkpoints/U117_external_survey_audit.md`) lists two live directions; one is the line
just declared converged.  The other -- EFFECTIVE DIOPHANTINE GEOMETRY -- this session has not
touched.  Its failure mechanism, if it has one, is guaranteed to be different from automorphy,
which is what the loop asks for.

THE STANDARD SET-UP, AND THE EXACT QUANTITY TO COMPUTE
------------------------------------------------------
Darmon-Granville: for a FIXED hyperbolic signature (x, y, z), the coprime solutions of
A^x + B^y = C^z correspond to rational points on finitely many twists of a curve that is a Galois
cover of P^1 branched over {0, 1, infinity} with ramification indices x, y, z.  For such a cover of
degree N, Riemann-Hurwitz gives

    2g - 2 = N * (1 - 1/x - 1/y - 1/z) = N * |chi|,      so      g = 1 + N*|chi|/2.

The minimal such N is the order of the quotient of the (x,y,z) triangle group that the cover
realises; the smallest Galois cover has N = lcm-related and is at least lcm(x,y,z).  Using
N = lcm(x, y, z) as a LOWER-BOUND proxy for the degree gives a lower bound on the genus that is
exact for the covers actually used in the literature for small signatures.

The question this script answers exactly: does the genus stay bounded as the signature varies over
the Beal range?  If it grows without bound, then effective Diophantine geometry needs an effective
Mordell statement UNIFORM IN THE GENUS, which is a different and more demanding object than the
per-curve computations (Chabauty-Coleman, Mordell-Weil sieve) that this project already used and
found insufficient.

Exact integer and Fraction arithmetic throughout; no floating point.

WHAT THIS PROVES
----------------
Nothing about Beal.  It quantifies the cost of one direction, so that the direction is entered with
its price known rather than discovered halfway through -- which is what happened with the rigidity
line (U258, refuted at U309).
"""

from fractions import Fraction
from itertools import combinations_with_replacement


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def reduced_exponents(limit):
    """Reduced Beal exponents: 4 together with the odd primes."""
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


def chi(x, y, z):
    """|chi| = 1 - 1/x - 1/y - 1/z, exactly."""
    return 1 - Fraction(1, x) - Fraction(1, y) - Fraction(1, z)


def genus_lower_bound(x, y, z):
    """g = 1 + N*|chi|/2 with N = lcm(x,y,z), as an exact Fraction."""
    N = lcm(x, lcm(y, z))
    return 1 + Fraction(N) * chi(x, y, z) / 2, N


def main():
    print("=" * 78)
    print("U330: the cost of the effective-Diophantine-geometry direction")
    print("=" * 78)

    E = reduced_exponents(19)

    # --- control: the hyperbolicity floor for Beal exponents --------------------------
    print("\n[control] |chi| = 1 - 1/x - 1/y - 1/z over Beal signatures:")
    # (3,3,3) has |chi| = 0 -- EUCLIDEAN, not hyperbolic; it is FLT3 and is excluded here.
    # The first run of this script asserted 1/12 without that exclusion and FAILED, which is the
    # assertion doing its job: the hyperbolic condition 1/x + 1/y + 1/z < 1 is a real restriction
    # inside the Beal range, not automatic.
    euclid = [t for t in combinations_with_replacement([3, 4, 5, 7], 3) if chi(*t) == 0]
    print(f"   Beal signatures with |chi| = 0 (euclidean, NOT hyperbolic): {euclid}")
    assert euclid == [(3, 3, 3)], f"expected only (3,3,3), got {euclid}"
    worst = None
    for t in combinations_with_replacement([3, 4, 5, 7], 3):
        c = chi(*t)
        if c <= 0:
            continue
        if worst is None or c < worst[1]:
            worst = (t, c)
    print(f"   smallest POSITIVE |chi| among small Beal signatures: {worst[0]} gives {worst[1]}")
    assert worst[1] == Fraction(1, 12), f"expected 1/12, got {worst[1]}"
    # and the Fermat-Catalan floor, which is SMALLER because exponent 2 is allowed
    fc = chi(2, 3, 7)
    print(f"   for comparison, the Fermat-Catalan floor (2,3,7) is {fc} = 1/42, which is smaller")
    print("   -- the exponent-2 cases are the hard ones geometrically, and Beal excludes them")
    assert fc == Fraction(1, 42)

    # --- the decisive quantity: does the genus stay bounded? ---------------------------
    print("\n[decisive] genus lower bound g = 1 + lcm(x,y,z)*|chi|/2, pairwise distinct signatures:")
    print(f"   {'signature':>14} | {'lcm':>6} | {'|chi|':>10} | {'genus >=':>10}")
    print("   " + "-" * 50)
    rows = []
    for t in combinations_with_replacement(E, 3):
        if len(set(t)) != 3:
            continue
        g, N = genus_lower_bound(*t)
        rows.append((t, N, chi(*t), g))
    rows.sort(key=lambda r: r[3])
    for t, N, c, g in rows[:6]:
        print(f"   {str(t):>14} | {N:>6} | {str(c):>10} | {str(g):>10}")
    print("   ...")
    for t, N, c, g in rows[-6:]:
        print(f"   {str(t):>14} | {N:>6} | {str(c):>10} | {str(g):>10}")

    gmin = min(r[3] for r in rows)
    gmax = max(r[3] for r in rows)
    print(f"\n   genus ranges from {gmin} to {gmax} over pairwise distinct signatures with "
          f"exponents <= 19")

    # --- growth: fix two exponents, let the third grow ---------------------------------
    print("\n[growth] fix (3,4,*) and let the third exponent run over the reduced exponents:")
    print(f"   {'r':>4} | {'lcm(3,4,r)':>11} | {'genus >=':>10}")
    print("   " + "-" * 32)
    for r in E:
        if r in (3, 4):
            continue
        g, N = genus_lower_bound(3, 4, r)
        print(f"   {r:>4} | {N:>11} | {str(g):>10}")

    # the genus is unbounded: |chi| -> 1 - 1/3 - 1/4 = 5/12 and lcm grows linearly in r
    big = genus_lower_bound(3, 4, 9973)[0]
    print(f"\n   at r = 9973 (prime) the bound is already g >= {big}")
    assert big > 1000, "the genus should be unbounded in the third exponent"

    print("\n" + "=" * 78)
    print("RESULT: the genus is UNBOUNDED over the Beal range. For a fixed signature the")
    print("Darmon-Granville curve has genus >= 2 and Faltings gives finiteness, but ineffectively;")
    print("making it effective for ONE curve is already open in general, and Beal needs it for")
    print("infinitely many curves of unbounded genus, plus control of the twists.")
    print()
    print("SO THE FAILURE MECHANISM HERE IS DIFFERENT from the automorphy obstruction, which is")
    print("what the loop asks for in a RESTART: automorphy fails on the RANK of a single object;")
    print("this fails on UNIFORMITY over a family whose genus grows. Neither is reachable at $0,")
    print("but they are not the same wall, so recording both is worth more than mining either.")
    print()
    print("This proves nothing about Beal. It prices one direction before entering it.")
    print("=" * 78)


if __name__ == "__main__":
    main()
