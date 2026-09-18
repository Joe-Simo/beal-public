#!/usr/bin/env python3
"""
U315: the OPPOSITE-PARITY branch of (3,4,4) — does it really need elliptic Chabauty?

THE RECORDED POSITION BEING ATTACKED
------------------------------------
Pool C155/C156 and `research/checkpoints/U278_cohen344_descent.md` record the opposite-parity
branch of `A^3 + B^4 = C^4` (exactly one of B, C even) as BLOCKED: it was reduced to finding the
rational points on the Mordell curve y^2 = x^3 - 972 whose Y-coordinate is a square, i.e. elliptic
Chabauty, which PARI cannot do and which is unavailable at $0.

THE CLAIM UNDER TEST
--------------------
That reduction may be unnecessary.  In the opposite-parity case ALL THREE factors of

    A^3 = (C - B)(C + B)(C^2 + B^2)

are ODD: if C is even and B odd then C-B and C+B are odd and C^2+B^2 = even + odd is odd; if B is
even and C odd the same three are odd.  This is exactly the situation the same-parity branch had
to work for -- there the 2-adic bookkeeping was the whole difficulty -- and here it is free.

The three factors are pairwise coprime by the same Bezout argument already machine-checked
(Beal.odd_common_divisor_sub_add / _sub_sqsum / _add_sqsum), so each is a cube:

    C - B = mu^3,    C + B = nu^3,    C^2 + B^2 = tau^3.

Then C = (mu^3 + nu^3)/2 and B = (nu^3 - mu^3)/2, so

    C^2 + B^2 = ((nu^3+mu^3)^2 + (nu^3-mu^3)^2)/4 = (mu^6 + nu^6)/2 = tau^3,

that is

    (mu^2)^3 + (nu^2)^3 = 2 * tau^3.

The equation a^3 + b^3 = 2c^3 is a classical one (Euler): in coprime integers its only solutions
have a = b or abc = 0.  Applying that gives mu^2 = nu^2, hence mu = nu, hence C - B = C + B, hence
B = 0 -- excluded.  No Chabauty anywhere.

WHAT THIS SCRIPT CHECKS, EXACTLY
--------------------------------
1. PARITY: for every coprime B, C of opposite parity with B < C, all three factors are odd.
2. COPRIMALITY: the three factors are pairwise coprime.
3. THE ALGEBRAIC IDENTITY: if C-B = m^3, C+B = n^3 then (C^2+B^2)*2 = m^6 + n^6 exactly.
4. EULER'S EQUATION, as a bounded search: a^3 + b^3 = 2c^3 with a,b,c positive and coprime and
   a != b -- if any is found, the argument above is WRONG and must be withdrawn.
5. A direct search for A^3 + B^4 = C^4 with opposite parity, as an independent control.

All exact integer arithmetic; no floating point.

WHAT A PASS DOES NOT MEAN
-------------------------
A pass does NOT close the branch: step 4 is a bounded search, and a bounded search can never
establish Euler's theorem (survey gate: bounded computation is a dead category).  What a pass does
is show the REDUCTION is right, so the branch depends on a classical named theorem rather than on
an unavailable computation.  Whether mathlib has that theorem is a separate question, checked
elsewhere.  This says nothing about Beal's open core.
"""

from math import gcd, isqrt


def icbrt(n):
    """Exact integer cube root, or None."""
    if n < 0:
        return None
    r = round(n ** (1 / 3)) if n < 2 ** 52 else int(n ** (1 / 3))
    for c in range(max(0, r - 2), r + 3):
        if c ** 3 == n:
            return c
    # exact fallback: binary search, no floats
    lo, hi = 0, 1
    while hi ** 3 < n:
        hi *= 2
    while lo <= hi:
        mid = (lo + hi) // 2
        v = mid ** 3
        if v == n:
            return mid
        if v < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def main():
    print("=" * 78)
    print("U315: the opposite-parity branch of (3,4,4) without elliptic Chabauty")
    print("=" * 78)

    # --- 1 & 2: parity and pairwise coprimality of the three factors -------------------
    LIMIT = 400
    pairs = 0
    parity_ok = True
    coprime_ok = True
    for B in range(1, LIMIT):
        for C in range(B + 1, LIMIT):
            if gcd(B, C) != 1:
                continue
            if (B % 2) == (C % 2):
                continue                       # same parity: handled by the closed branch
            pairs += 1
            f1, f2, f3 = C - B, C + B, C * C + B * B
            if not (f1 % 2 and f2 % 2 and f3 % 2):
                parity_ok = False
                print(f"   PARITY VIOLATION at B={B}, C={C}: {f1}, {f2}, {f3}")
            if gcd(f1, f2) != 1 or gcd(f1, f3) != 1 or gcd(f2, f3) != 1:
                coprime_ok = False
                print(f"   COPRIMALITY VIOLATION at B={B}, C={C}: "
                      f"gcds {gcd(f1,f2)}, {gcd(f1,f3)}, {gcd(f2,f3)}")
    print(f"\n[1] all three factors odd, over {pairs} opposite-parity coprime pairs "
          f"1 <= B < C < {LIMIT}: {'PASS' if parity_ok else 'FAIL'}")
    print(f"[2] the three factors pairwise coprime, same pairs: "
          f"{'PASS' if coprime_ok else 'FAIL'}")

    # --- 3: the algebraic identity -------------------------------------------------------
    ident_ok = True
    checked = 0
    for m in range(1, 60, 2):
        for n in range(m + 2, 60, 2):
            if gcd(m, n) != 1:
                continue
            m3, n3 = m ** 3, n ** 3
            if (m3 + n3) % 2 or (n3 - m3) % 2:
                continue
            C = (m3 + n3) // 2
            B = (n3 - m3) // 2
            if B <= 0:
                continue
            checked += 1
            if 2 * (C * C + B * B) != m ** 6 + n ** 6:
                ident_ok = False
                print(f"   IDENTITY VIOLATION at m={m}, n={n}")
            if C - B != m3 or C + B != n3:
                ident_ok = False
                print(f"   RECONSTRUCTION VIOLATION at m={m}, n={n}")
    print(f"[3] 2(C^2+B^2) = mu^6 + nu^6 and the reconstruction, over {checked} cases: "
          f"{'PASS' if ident_ok else 'FAIL'}")

    # --- 4: Euler's equation a^3 + b^3 = 2c^3, bounded search --------------------------
    NB = 3000
    euler_hits = []
    for a in range(1, NB):
        a3 = a ** 3
        for b in range(a + 1, NB):          # a != b, and a < b by symmetry
            if gcd(a, b) != 1:
                continue
            s = a3 + b ** 3
            if s % 2:
                continue
            c = icbrt(s // 2)
            if c is not None and c > 0:
                euler_hits.append((a, b, c))
    print(f"[4] a^3 + b^3 = 2c^3 with coprime a < b, bounded by {NB}: "
          f"{'NONE (as Euler predicts)' if not euler_hits else 'HITS ' + str(euler_hits[:5])}")

    # --- 5: independent control, direct search --------------------------------------------
    DA, DC = 400, 200
    direct = []
    for C in range(2, DC):
        C4 = C ** 4
        for B in range(1, C):
            if gcd(B, C) != 1 or (B % 2) == (C % 2):
                continue
            rem = C4 - B ** 4
            if rem <= 0:
                continue
            A = icbrt(rem)
            if A is not None and A > 0:
                direct.append((A, B, C))
    print(f"[5] direct search A^3 + B^4 = C^4, opposite parity, coprime, C < {DC}: "
          f"{'NONE' if not direct else direct}")

    print("\n" + "=" * 78)
    ok = parity_ok and coprime_ok and ident_ok and not euler_hits and not direct
    print(f"RESULT: {'reduction confirmed' if ok else 'REDUCTION IS WRONG — WITHDRAW IT'}")
    print()
    print("This does NOT close the branch. Step 4 is a bounded search and bounded search is a")
    print("dead category by the survey gate; Euler's theorem is what actually closes it. What is")
    print("established is that the branch reduces to a CLASSICAL NAMED THEOREM rather than to an")
    print("elliptic Chabauty computation that is unavailable here. Nothing about Beal's open core.")
    print("=" * 78)


if __name__ == "__main__":
    main()
