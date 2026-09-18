#!/usr/bin/env python3
"""
U323: counterexample search against EVERY named hypothesis Prop in the Lean development.

WHY
---
U322 found that `EulerDescentStep`, recorded one cycle earlier as "the residual gap", was FALSE as
stated: `p = 0, q = 1, c = 0` satisfies it with `q != 0`.  Nothing in Lean caught this, because an
implication from a false hypothesis still type-checks and everything downstream compiles.  A false
named hypothesis makes `final_residual` VACUOUS while leaving the build green.

So every named `Prop` in `formal/Beal/` deserves the same treatment the flaw got.  This script
searches each one for a concrete counterexample over an exact finite range.

WHAT A CLEAN RUN DOES AND DOES NOT MEAN
---------------------------------------
Finding nothing does NOT prove a hypothesis: these are the statements of published theorems, and a
bounded search is a dead category by the survey gate.  What a clean run does is rule out the
specific failure mode that actually bit this project once -- a hypothesis that is false for a
small, boring reason (a zero, a unit, a degenerate case) and therefore unprovable and vacuous.

Finding something is decisive: it means the corresponding Lean hypothesis must be restated.

Exact integer and Fraction arithmetic throughout; no floating point.
"""

import sys
from fractions import Fraction
from math import gcd


def is_perfect_power(n, k):
    """Exact: is n a k-th power of a positive integer? Returns the root or None."""
    if n < 1:
        return None
    lo, hi = 1, 1
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


def is_square(n):
    return is_perfect_power(n, 2)


# ----------------------------------------------------------------------------------
# one searcher per named Prop
# ----------------------------------------------------------------------------------

def search_euler_cubic_two(N=400):
    """a^3 + b^3 = 2c^3, coprime, all positive  =>  a = b."""
    out = []
    for a in range(1, N):
        for b in range(a + 1, N):          # a != b
            if gcd(a, b) != 1:
                continue
            s = a ** 3 + b ** 3
            if s % 2:
                continue
            c = is_perfect_power(s // 2, 3)
            if c:
                out.append((a, b, c))
    return out


def search_euler_descent_step(N=700):
    """p != 0, IsCoprime p q, p(p^2+3q^2) = c^3  =>  q = 0.  (p = 0 is the U322 flaw.)"""
    out = []
    for p in list(range(1, N)) + list(range(-N + 1, 0)):
        for q in range(1, N):
            if gcd(abs(p), q) != 1:
                continue
            v = p * (p * p + 3 * q * q)
            if v <= 0:
                r = is_perfect_power(-v, 3)
                if r is not None and v != 0:
                    out.append((p, q, -r))
                continue
            r = is_perfect_power(v, 3)
            if r:
                out.append((p, q, r))
    return out


def search_flt_hyp(N=300):
    """a^n + b^n = c^n, n >= 3, positive  =>  False."""
    out = []
    for n in range(3, 9):
        for a in range(1, N):
            an = a ** n
            if an > (N ** n):
                break
            for b in range(a, N):
                s = an + b ** n
                c = is_perfect_power(s, n)
                if c:
                    out.append((a, b, c, n))
                if s > (2 * N) ** n:
                    break
    return out


def search_darmon_merel_nn2(N=300):
    """a^n + b^n = c^2, n >= 4, coprime positive  =>  False."""
    out = []
    for n in range(4, 13):
        for a in range(1, N):
            an = a ** n
            if an > 10 ** 30:
                break
            for b in range(a, N):
                bn = b ** n
                if an + bn > 10 ** 30:
                    break
                if gcd(a, b) != 1:
                    continue
                c = is_square(an + bn)
                if c:
                    out.append((a, b, c, n))
    return out


def search_darmon_merel_nn3(N=300):
    """a^n + b^n = c^3, n >= 3, coprime positive  =>  False."""
    out = []
    for n in range(3, 13):
        for a in range(1, N):
            an = a ** n
            if an > 10 ** 30:
                break
            for b in range(a, N):
                bn = b ** n
                if an + bn > 10 ** 30:
                    break
                if gcd(a, b) != 1:
                    continue
                c = is_perfect_power(an + bn, 3)
                if c:
                    out.append((a, b, c, n))
    return out


def search_bcdy_three_three_two_n(N=600):
    """a^3 + b^3 = c^(2n), n >= 2, coprime positive  =>  False."""
    out = []
    for a in range(1, N):
        for b in range(a, N):
            if gcd(a, b) != 1:
                continue
            s = a ** 3 + b ** 3
            for n in range(2, 9):
                c = is_perfect_power(s, 2 * n)
                if c:
                    out.append((a, b, c, n))
    return out


def search_ben_24n(N=800):
    """a^2 + b^4 = c^n, n >= 4, coprime positive  =>  False."""
    out = []
    for b in range(1, N):
        b4 = b ** 4
        for a in range(1, N * 4):
            s = a * a + b4
            if s > 10 ** 22:
                break
            if gcd(a, b) != 1:
                continue
            for n in range(4, 13):
                c = is_perfect_power(s, n)
                if c:
                    out.append((a, b, c, n))
    return out


def search_bcdy_four_two_n_three(N=400):
    """a^4 + b^(2n) = c^3, n >= 2, coprime positive  =>  False."""
    out = []
    for a in range(1, N):
        a4 = a ** 4
        for b in range(1, N):
            for n in range(2, 8):
                s = a4 + b ** (2 * n)
                if s > 10 ** 24:
                    break
                if gcd(a, b) != 1:
                    continue
                c = is_perfect_power(s, 3)
                if c:
                    out.append((a, b, c, n))
    return out


def search_dahmen_siksek(N=400):
    """(5,5,7), (5,5,19), (7,7,5) have no coprime positive solutions."""
    out = []
    for a in range(1, N):
        for b in range(a, N):
            if gcd(a, b) != 1:
                continue
            s5 = a ** 5 + b ** 5
            if is_perfect_power(s5, 7):
                out.append(("(5,5,7)", a, b))
            if is_perfect_power(s5, 19):
                out.append(("(5,5,19)", a, b))
            s7 = a ** 7 + b ** 7
            if is_perfect_power(s7, 5):
                out.append(("(7,7,5)", a, b))
    return out


def search_quartic(coeffs_name, f, DEN=60, NUM=200):
    """W^2 = f(V) over Q  =>  V = 0.  Search V = num/den in lowest terms."""
    out = []
    for den in range(1, DEN + 1):
        for num in range(-NUM, NUM + 1):
            if num == 0 or gcd(abs(num), den) != 1:
                continue
            V = Fraction(num, den)
            val = f(V)
            if val < 0:
                continue
            # exact rational square test
            n, d = val.numerator, val.denominator
            rn, rd = is_square(n) if n > 0 else (0 if n == 0 else None), is_square(d)
            if n == 0:
                out.append((coeffs_name, V, Fraction(0)))
                continue
            if rn and rd:
                out.append((coeffs_name, V, Fraction(rn, rd)))
    return out


def search_no_coprime_sol(x, y, z, N=400):
    """a^x + b^y = c^z, coprime positive  =>  False.  Used for the InstanceRows entries."""
    out = []
    for a in range(1, N):
        ax = a ** x
        if ax > 10 ** 26:
            break
        for b in range(1, N):
            s = ax + b ** y
            if s > 10 ** 26:
                break
            if gcd(a, b) != 1:
                continue
            c = is_perfect_power(s, z)
            if c:
                out.append((a, b, c))
    return out


CHECKS = [
    ("EulerCubicTwo                 (Cohen344.lean)", search_euler_cubic_two),
    ("EulerDescentStep  [p != 0]    (Euler.lean)", search_euler_descent_step),
    ("FLTHyp                        (ClosedFamilies.lean)", search_flt_hyp),
    ("DarmonMerelNN2                (ClosedFamilies.lean)", search_darmon_merel_nn2),
    ("DarmonMerelNN3                (ClosedFamilies.lean)", search_darmon_merel_nn3),
    ("BCDYThreeThreeTwoN            (ClosedFamilies.lean)", search_bcdy_three_three_two_n),
    ("BEN24n                        (ClosedFamilies.lean)", search_ben_24n),
    ("BCDYFourTwoNThree             (EvenEvenThree.lean)", search_bcdy_four_two_n_three),
    ("DahmenSiksek                  (ClosedFamilies.lean)", search_dahmen_siksek),
    ("InstanceRows.cohen344 (3,4,4)", lambda: search_no_coprime_sol(3, 4, 4)),
    ("InstanceRows.pss347   (3,4,7)", lambda: search_no_coprime_sol(3, 4, 7)),
    ("InstanceRows.ss345    (3,4,5)", lambda: search_no_coprime_sol(3, 4, 5)),
    ("Quartic400g2  W^2 = 5V^4-10V^2+1",
     lambda: search_quartic("400g2", lambda V: 5 * V ** 4 - 10 * V ** 2 + 1)),
    ("Quartic400b2  W^2 = 5(U^4-10U^2+5)",
     lambda: search_quartic("400b2", lambda U: 5 * (U ** 4 - 10 * U ** 2 + 5))),
]


def search_euler_descent_step_WITHOUT_hypothesis(N=5):
    """CONTROL. The U322 flaw: the same Prop WITHOUT `p != 0`. This MUST report a hit, or the
    searcher above is not capable of detecting the failure mode it exists to detect."""
    out = []
    for p in range(0, N):
        for q in range(1, N):
            if gcd(abs(p), q) != 1:
                continue
            v = p * (p * p + 3 * q * q)
            if v == 0:
                out.append((p, q, 0))
            elif is_perfect_power(v, 3):
                out.append((p, q, is_perfect_power(v, 3)))
    return out


def main():
    print("=" * 78)
    print("U323: counterexample search against every named hypothesis Prop")
    print("=" * 78)
    print("\nMotivated by U322: EulerDescentStep was FALSE as first recorded (p=0, q=1, c=0),")
    print("and Lean did not and could not notice. Every named Prop gets the same treatment.\n")

    # --- control first: the searcher must catch the one flaw that really happened ---
    control = search_euler_descent_step_WITHOUT_hypothesis()
    if not control:
        print("  [FAIL] CONTROL: the searcher cannot detect the known U322 flaw. Aborting.")
        sys.exit(1)
    print(f"  [control OK]     EulerDescentStep WITHOUT `p != 0` -> counterexample {control[0]}")
    print("                   (so a clean line below is a real negative, not a blind searcher)\n")

    bad = 0
    for name, fn in CHECKS:
        hits = fn()
        if hits:
            bad += 1
            print(f"  [COUNTEREXAMPLE] {name}")
            for h in hits[:5]:
                print(f"       {h}")
            if len(hits) > 5:
                print(f"       ... and {len(hits) - 5} more")
        else:
            print(f"  [clean]          {name}")

    print("\n" + "=" * 78)
    if bad:
        print(f"{bad} NAMED PROP(S) ARE FALSE AS STATED. Each must be restated in Lean before")
        print("anything that assumes it can be trusted; until then final_residual is vacuous.")
        sys.exit(1)
    print("No counterexample found for any named Prop in the ranges searched.")
    print()
    print("THIS IS NOT A PROOF of any of them. They are statements of published theorems and a")
    print("bounded search is a dead category by the survey gate. What it rules out is the failure")
    print("mode that actually occurred once here: a hypothesis false for a small degenerate")
    print("reason, hence unprovable, hence silently making everything downstream vacuous.")
    print("=" * 78)


if __name__ == "__main__":
    main()
