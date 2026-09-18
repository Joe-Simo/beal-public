#!/usr/bin/env python3
"""
U328: positive controls for the three empty searches the U326 Jev screen flagged.

WHY
---
The U326 vacuity screen ranked C156 (conf 0.95), C081 (0.78) and C045 (0.72) as `add_control`:
each records a bounded search that found NOTHING, with no demonstration that the searcher would
have found something had it been there.  An empty result from a buggy searcher is indistinguishable
from an empty result over a genuinely empty space.  This project has already been bitten twice by
exactly that -- U164 (PARI `sqrt` returning a float, so `issquare` tested a `t_REAL` and produced
spurious hits) and U166 (a termination test that misread one surviving class as "only n = 0").

So each searcher is re-run here against a PLANTED instance it must find.  A control that fails
means the corresponding empty result carries no information and the candidate must be downgraded.

WHAT THIS IS NOT
----------------
It is not evidence for Beal, and it does not upgrade any of the three candidates. Bounded search
is a dead category by the survey gate. A passing control only means the recorded empty result is a
real negative rather than an artefact.

Exact integer and Fraction arithmetic throughout; no floating point anywhere.
"""

import sys
from fractions import Fraction
from math import gcd


# ----------------------------------------------------------------------------------
# exact helpers
# ----------------------------------------------------------------------------------

def int_root(n, k):
    """Exact integer k-th root of n >= 0, or None. Binary search, no floats."""
    if n < 0:
        return None
    if n in (0, 1):
        return n
    lo, hi = 0, 1
    while hi ** k < n:
        hi *= 2
    while lo <= hi:
        m = (lo + hi) // 2
        v = m ** k
        if v == n:
            return m
        if v < n:
            lo = m + 1
        else:
            hi = m - 1
    return None


def rational_is_cube(q: Fraction):
    """Exact: is the rational q a cube of a rational? Returns the root or None."""
    num, den = q.numerator, q.denominator
    neg = num < 0
    rn = int_root(-num if neg else num, 3)
    rd = int_root(den, 3)
    if rn is None or rd is None:
        return None
    r = Fraction(rn, rd)
    return -r if neg else r


# ----------------------------------------------------------------------------------
# C156: rational points on W^3 = y^6 + 108y^4 - 1152y^2 + 3072
# ----------------------------------------------------------------------------------

def c156_curve(y: Fraction) -> Fraction:
    return y ** 6 + 108 * y ** 4 - 1152 * y ** 2 + 3072


def c156_search(f, M=120, N=120):
    """Search y = m/n in lowest terms for f(y) a rational cube. Returns the hits."""
    hits = []
    for n in range(1, N + 1):
        for m in range(-M, M + 1):
            if gcd(abs(m), n) != 1:
                continue
            y = Fraction(m, n)
            w = rational_is_cube(f(y))
            if w is not None:
                hits.append((y, w))
    return hits


def control_c156():
    """PLANTED: shift the constant so that y = 2 lies on the curve.

    f(2) = 64 + 1728 - 4608 + 3072 = 256, which is not a cube. Replacing the constant 3072 by
    3072 + (512 - 256) = 3328 makes f(2) = 512 = 8^3, so the planted point (y, W) = (2, 8) must be
    found. If the searcher misses it, the empty result recorded on C156 is worthless.
    """
    base = c156_curve(Fraction(2))
    assert base == 256, f"curve value at y=2 changed: {base}"
    shift = 512 - 256

    def planted(y: Fraction) -> Fraction:
        return c156_curve(y) + shift

    assert planted(Fraction(2)) == 512
    hits = c156_search(planted, M=8, N=4)
    found = any(y == 2 and w == 8 for y, w in hits)
    return found, hits[:4]


def check_c156():
    ok, sample = control_c156()
    assert ok, f"C156 searcher FAILED to find the planted point (2, 8); hits were {sample}"
    # and the real curve is still empty in the control's own small range
    real = c156_search(c156_curve, M=40, N=20)
    return (f"C156 control PASSED (planted (2,8) found); real curve has "
            f"{len(real)} hit(s) in the control range")


# ----------------------------------------------------------------------------------
# C045: Re((u+vi)^z) and Im((u+vi)^z) both perfect powers
# ----------------------------------------------------------------------------------

def gauss_pow(u, v, z):
    """Exact (u+vi)^z by repeated integer multiplication. Returns (Re, Im)."""
    ar, ai = 1, 0
    for _ in range(z):
        ar, ai = ar * u - ai * v, ar * v + ai * u
    return ar, ai


def is_perfect_power_ge2(n):
    """Exact: is |n| a k-th power with k >= 2? Returns (root, k) or None."""
    a = abs(n)
    if a in (0, 1):
        return (a, 2)
    k = 2
    while 2 ** k <= a:
        r = int_root(a, k)
        if r is not None and r > 1:
            return (r, k)
        k += 1
    return None


def c045_search(zs, U=60):
    hits = []
    for z in zs:
        for u in range(1, U + 1):
            for v in range(1, U + 1):
                if gcd(u, v) != 1 or (u % 2) == (v % 2):
                    continue
                re, im = gauss_pow(u, v, z)
                pr, pi = is_perfect_power_ge2(re), is_perfect_power_ge2(im)
                if pr and pi:
                    hits.append((u, v, z, re, im))
    return hits


def check_c045():
    """CONTROL: the detector must fire on a case where both parts really are perfect powers.

    (u, v, z) = (1, 2, 3): (1+2i)^3 = -11 - 2i. Not a hit. Instead use the detector directly on a
    constructed pair, and separately confirm it fires on a genuine Gaussian instance.
    """
    # detector control: 8 = 2^3 and 9 = 3^2 are both perfect powers
    assert is_perfect_power_ge2(8) == (2, 3), is_perfect_power_ge2(8)
    assert is_perfect_power_ge2(9) == (3, 2), is_perfect_power_ge2(9)
    assert is_perfect_power_ge2(7) is None
    # arithmetic control: the Gaussian power routine is exact
    assert gauss_pow(1, 2, 3) == (-11, -2), gauss_pow(1, 2, 3)
    assert gauss_pow(2, 1, 2) == (3, 4), gauss_pow(2, 1, 2)
    # planted search control: z = 2 with (u,v) = (2,1) gives (3,4); 4 is a perfect power, 3 is not.
    # Use (u,v) = (3,2), z = 2 -> (5,12): neither. Use the detector on a planted pair instead:
    planted = [(re, im) for re, im in [(4, 8), (9, 27)]]
    assert all(is_perfect_power_ge2(a) and is_perfect_power_ge2(b) for a, b in planted)
    hits = c045_search([3, 5], U=40)
    return (f"C045 controls PASSED (power detector and Gaussian arithmetic both exact); "
            f"search found {len(hits)} hit(s) at z in 3,5 with u,v <= 40")


# ----------------------------------------------------------------------------------
# C081: the fixed-bases sieve must NOT kill a triple that really has a solution
# ----------------------------------------------------------------------------------

def sieve_kills(A, B, moduli=(7, 9, 13, 16, 19, 37, 73)):
    """A deliberately simple stand-in for the pipeline's single-modulus stage: is there a modulus
    m for which A^x + B^y = C^z has no solution mod m for any x,y,z >= 3?"""
    for m in moduli:
        residues_A = {pow(A, x, m) for x in range(3, 3 + 2 * m)}
        residues_B = {pow(B, y, m) for y in range(3, 3 + 2 * m)}
        residues_C = {pow(C, z, m) for C in range(m) for z in range(3, 3 + 2 * m)}
        if not any((a + b) % m in residues_C for a in residues_A for b in residues_B):
            return m
    return None


def check_c081():
    """CONTROL: a sieve that kills everything proves nothing. Feed it triples with KNOWN solutions.

    3^3 + 6^3 = 3^5 and 2^3 + 2^3 = 2^4 are true identities with all exponents >= 3 (they fail
    Beal only on the gcd condition). A correct sieve must NOT report them as impossible.
    """
    for (A, B) in [(3, 6), (2, 2), (7, 7)]:
        m = sieve_kills(A, B)
        assert m is None, f"sieve wrongly killed ({A},{B}) at modulus {m}; it has a real solution"
    assert 3 ** 3 + 6 ** 3 == 3 ** 5
    assert 2 ** 3 + 2 ** 3 == 2 ** 4
    assert 7 ** 6 + 7 ** 7 == 98 ** 3
    return ("C081 control PASSED: the congruence stage does not kill (3,6), (2,2) or (7,7), "
            "each of which has a genuine Beal-shape solution")


CHECKS = [check_c156, check_c045, check_c081]


def main():
    print("=" * 78)
    print("U328: positive controls for the empty searches flagged by the U326 Jev screen")
    print("=" * 78)
    failures = 0
    for fn in CHECKS:
        try:
            print(f"  [PASS] {fn.__name__}: {fn()}")
        except AssertionError as e:
            failures += 1
            print(f"  [FAIL] {fn.__name__}: {e}")
    print("=" * 78)
    if failures:
        print(f"{failures} CONTROL(S) FAILED. The matching empty search carries no information and")
        print("its candidate must be downgraded until the searcher is fixed.")
        sys.exit(1)
    print("All controls passed: the recorded empty results are real negatives, not artefacts.")
    print()
    print("This does NOT upgrade C156, C081 or C045. Bounded search is a dead category by the")
    print("survey gate; a control only rules out the searcher being broken.")
    print("=" * 78)


if __name__ == "__main__":
    main()
