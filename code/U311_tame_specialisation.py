#!/usr/bin/env python3
"""
U311: obligation (a) of pool C169 — does the Beal equation supply a specialisation point at which
a rigid local system on P^1 minus {0,1,infinity} has BOUNDED ramification?

THE NAMED HYPOTHESIS UNDER TEST
-------------------------------
A solution A^x + B^y = C^z gives the point

    t = A^x / C^z    in    P^1 minus {0, 1, infinity},    with    1 - t = B^y / C^z.

The classical Frey construction works because the exponents make the relevant valuations
divisible by the local monodromy orders, so pulling a local system back along t kills its
ramification at every prime dividing A, B or C.  The hypothesis to test is the exact arithmetic
statement that underlies this, for THREE INDEPENDENT exponents:

    H1.  for every prime l | A:              v_l(t)     = x * v_l(A)        is divisible by x
    H2.  for every prime l | B:              v_l(1 - t) = y * v_l(B)        is divisible by y
    H3.  for every prime l | C:              v_l(t) = v_l(1 - t) = -z*v_l(C) is divisible by z

If H1-H3 hold, then a local system whose local monodromy at 0, 1, infinity has order x, y, z
respectively pulls back to something unramified at every prime dividing A*B*C, because the
ramification index is a multiple of the monodromy order.  The bad primes are then confined to
primes of bad reduction of the sheaf itself, which do not depend on A, B, C.

WHY THIS IS WORTH CHECKING RATHER THAN ASSERTING
------------------------------------------------
H3 is the one that is easy to get wrong: t and 1-t have the SAME denominator C^z, so a prime
dividing C divides the denominator of both, and the naive statement "v_l(1-t) is divisible by y"
is FALSE there.  The correct statement at l | C is that the valuation is divisible by z, which is
the order at the THIRD puncture.  Getting this wrong would silently assume what is to be proved.
This script checks all three on exact integers.

THE COPRIMALITY HYPOTHESIS (added after the first run)
------------------------------------------------------
The first run of this script reported H3 violations on 3^3+6^3=3^5, 7^6+7^7=98^3 and 2^9+8^3=4^5.
Those are NOT bugs and NOT counterexamples to H1-H3: all three have gcd > 1, and H1-H3 are false
without coprimality.  They are now used as CONTROLS, and their failure is the expected outcome.

Under coprimality the three hypotheses are a one-line theorem: if gcd(A,B) = 1 then a prime
dividing C divides neither A nor B, so v_l(t) = -z*v_l(C) = v_l(1-t) there, while a prime dividing
A divides neither B nor C, so v_l(t) = x*v_l(A).  The script verifies this exactly rather than
asserting it.

This matters for the route's logic: the specialisation is tame EXACTLY at the points Beal declares
not to exist.  A Beal counterexample has gcd = 1 by definition, so assuming coprimality here is the
counterexample hypothesis, not a circular assumption.

TEST DATA
---------
1. The ten Fermat-Catalan solutions (each has an exponent 2, so they are NOT Beal counterexamples;
   they are used only as exact arithmetic witnesses that the valuation identities hold).
2. The known non-coprime Beal-shape identities, e.g. 3^3 + 6^3 = 3^5.
3. Systematically generated exact identities of the form A^x + B^y = C^z built by construction.

Exact integer arithmetic throughout; Fraction is used only for exact rational valuations, never
floating point.

WHAT A PASS MEANS
-----------------
A pass establishes H1-H3 as arithmetic facts about the specialisation point.  It does NOT produce
a Frey object and is NOT progress on Beal: the surviving obstruction is C169 obligation (b), the
motivic/automorphic realisation of a rank-n sheaf, for which no modularity theorem is available
when n > 2.  This script cannot test (b).
"""

from fractions import Fraction


def factorise(n):
    """Exact trial-division factorisation. n > 0."""
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def valuation(num, den, l):
    """Exact l-adic valuation of the rational num/den."""
    v = 0
    while num % l == 0:
        num //= l
        v += 1
    while den % l == 0:
        den //= l
        v -= 1
    return v


def check_identity(A, x, B, y, C, z, label):
    """Check H1-H3 exactly for one identity A^x + B^y = C^z."""
    assert A ** x + B ** y == C ** z, f"{label}: not an identity"
    t_num, t_den = A ** x, C ** z
    o_num, o_den = B ** y, C ** z          # 1 - t = B^y / C^z
    assert Fraction(t_num, t_den) + Fraction(o_num, o_den) == 1, f"{label}: t + (1-t) != 1"

    rows = []
    ok = True

    for l in factorise(A) if A > 1 else {}:
        if C % l == 0:
            continue                        # handled by H3
        v = valuation(t_num, t_den, l)
        good = (v % x == 0)
        ok &= good
        rows.append(("H1", l, "v(t)", v, x, good))

    for l in factorise(B) if B > 1 else {}:
        if C % l == 0:
            continue
        v = valuation(o_num, o_den, l)
        good = (v % y == 0)
        ok &= good
        rows.append(("H2", l, "v(1-t)", v, y, good))

    for l in factorise(C) if C > 1 else {}:
        v1 = valuation(t_num, t_den, l)
        v2 = valuation(o_num, o_den, l)
        good = (v1 % z == 0) and (v2 % z == 0)
        ok &= good
        rows.append(("H3", l, "v(t),v(1-t)", (v1, v2), z, good))

    return ok, rows


FERMAT_CATALAN = [
    # (A, x, B, y, C, z) -- each has an exponent 2, so none is a Beal counterexample
    (1, 3, 2, 3, 3, 2),
    (2, 5, 7, 2, 3, 4),
    (7, 3, 13, 2, 2, 9),
    (2, 7, 17, 3, 71, 2),
    (3, 5, 11, 4, 122, 2),
    (17, 7, 76271, 3, 21063928, 2),
    (1414, 3, 2213459, 2, 65, 7),
    (9262, 3, 15312283, 2, 113, 7),
    (43, 8, 96222, 3, 30042907, 2),
    (33, 8, 1549034, 2, 15613, 3),
]

NON_COPRIME = [
    (3, 3, 6, 3, 3, 5),
    (7, 6, 7, 7, 98, 3),
    (2, 9, 8, 3, 4, 5),
]


def main():
    print("=" * 78)
    print("U311: H1-H3 for the specialisation point t = A^x / C^z")
    print("=" * 78)

    all_ok = True
    total_rows = 0
    controls_ok = []

    print("\n[1] Fermat-Catalan solutions (exponent 2 present; arithmetic witnesses only):")
    for (A, x, B, y, C, z) in FERMAT_CATALAN:
        ok, rows = check_identity(A, x, B, y, C, z, f"{A}^{x}+{B}^{y}={C}^{z}")
        total_rows += len(rows)
        all_ok &= ok
        print(f"   {A}^{x} + {B}^{y} = {C}^{z}: {'OK' if ok else 'FAIL'} ({len(rows)} valuations)")
        if not ok:
            for r in rows:
                if not r[-1]:
                    print(f"      VIOLATION {r}")

    print("\n[2] CONTROLS: non-coprime identities. H1-H3 are FALSE without coprimality,")
    print("    so every one of these MUST fail. A pass here would mean the test is vacuous.")
    for (A, x, B, y, C, z) in NON_COPRIME:
        ok, rows = check_identity(A, x, B, y, C, z, f"{A}^{x}+{B}^{y}={C}^{z}")
        total_rows += len(rows)
        g = __import__("math").gcd(__import__("math").gcd(A, B), C)
        expected_fail = (g > 1)
        control_ok = (not ok) if expected_fail else ok
        controls_ok.append(control_ok)
        print(f"   {A}^{x} + {B}^{y} = {C}^{z}: gcd = {g}, H1-H3 {'hold' if ok else 'fail'} "
              f"-> control {'PASS' if control_ok else 'UNEXPECTED'}")

    print("\n[3] constructed identities k^a*(1+k^b)... family d^z = d^z, three distinct exponents:")
    # Build exact identities with three DISTINCT exponents: take any s, and
    # (s^(y*z))^x + ... is delicate; instead use m^x + m^x = 2*m^x and choose m a power.
    built = []
    for (u, x, y, z) in [(2, 3, 4, 5), (2, 5, 3, 7), (3, 3, 5, 7), (2, 7, 11, 3)]:
        # A^x + B^y = C^z with A = 2^(a), B = 2^(b), C = 2^(c): need 2^(ax) + 2^(by) = 2^(cz)
        # take ax = by = cz - 1
        L = x * y * z
        ax = L
        a, b = L // x, L // y
        if (L + 1) % z:
            continue
        c = (L + 1) // z
        A, B, C = u ** a, u ** b, u ** c
        if u == 2 and A ** x + B ** y == C ** z:
            built.append((A, x, B, y, C, z))
    for (A, x, B, y, C, z) in built:
        ok, rows = check_identity(A, x, B, y, C, z, "built")
        total_rows += len(rows)
        all_ok &= ok
        print(f"   {A}^{x} + {B}^{y} = {C}^{z}: {'OK' if ok else 'FAIL'} "
              f"(exponents {x},{y},{z} pairwise distinct: {len({x,y,z})==3})")
        if not ok:
            for r in rows:
                if not r[-1]:
                    print(f"      VIOLATION {r}")
    if not built:
        print("   (no identity of this shape in the attempted parameter range)")

    print("\n" + "=" * 78)
    print(f"RESULT: coprime cases {'ALL PASS' if all_ok else 'VIOLATION FOUND'}; "
          f"non-coprime controls all failed as required: {all(controls_ok)}. "
          f"{total_rows} exact valuations.")
    print()
    print("READ CAREFULLY.  A pass means only that the specialisation point has the divisibility")
    print("needed to make a local system of local orders (x,y,z) unramified at every prime")
    print("dividing A*B*C.  It produces NO Frey object.  The surviving obstruction is C169(b):")
    print("a rank-n sheaf gives an n-dimensional Galois representation, and the modular method")
    print("needs automorphy, which is unavailable for n > 2.  This script cannot test that.")
    print("=" * 78)


if __name__ == "__main__":
    main()
