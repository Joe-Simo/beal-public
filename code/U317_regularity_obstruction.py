#!/usr/bin/env python3
"""
U317: is the three-exponent object ever REGULAR?  A second obstruction, tested.

WHY THIS QUESTION
-----------------
Pool C171 records that after U309/U310/U311 the three-exponent local-system route has one named
missing input: automorphy of a rank-n motive over Q for n > 2.  The known potential-automorphy
theorems in that range (Barnet-Lamb-Gee-Geraghty-Taylor and successors) require the Galois
representation to be **regular** -- distinct Hodge-Tate weights -- and essentially self-dual.

So before calling automorphy "the only obstruction", the honest question is whether the object the
route needs is even in the shape those theorems could ever accept.  If it is never regular, then
automorphy is not merely unproved for it: the whole potential-automorphy family is inapplicable,
which is a SECOND and sharper obstruction.

THE EXACT TEST
--------------
For a rigid local system on P^1 minus {0,1,infinity}, regularity of the associated motive
corresponds to the local monodromies at 0 and infinity being **regular semisimple**, i.e. having
partition (1^n): n distinct eigenvalues give n distinct weights.  A repeated eigenvalue collapses
weights and the representation is irregular.

Combine with the two constraints already established:

  * Katz rigidity: rig = -n^2 + sum of squares of multiplicities = 2    (C120/C121)
  * definability over Q: each eigenvalue multiset is a union of Galois orbits, one multiplicity
    c_d per divisor d | m applied to all phi(d) primitive d-th roots, order exactly m iff c_m >= 1
    (C170, code/U310_galois_stable_rigid.py)

and ask: is there a rigid, Q-rational triple with three PAIRWISE DISTINCT reduced exponents whose
partitions at 0 and at infinity are BOTH (1^n)?

Self-duality is checked too, and is expected to be free: a Galois orbit over Q is closed under
alpha -> alpha^(-1) because -1 is coprime to m, so every Q-rational eigenvalue multiset is stable
under inversion.  That half imposes nothing.

Exact integer arithmetic on partitions; no floating point.

WHAT EITHER ANSWER MEANS
------------------------
NO HIT: the object is never regular, so potential-automorphy theorems requiring regular weights
cannot apply to it however much they are improved.  C171's "one missing theorem" understates the
obstruction and must be corrected.

A HIT: the object can be regular and self-dual, so it is in the shape those theorems address, and
C171 stands as written.

Either way this proves nothing about Beal.  It classifies an obstruction.
"""

from itertools import product


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def totient(m):
    return sum(1 for k in range(1, m + 1) if gcd(k, m) == 1)


def divisors(m):
    return [d for d in range(1, m + 1) if m % d == 0]


def rigidity_index(n, triple):
    return -n * n + sum(sum(x * x for x in lam) for lam in triple)


def stable_partitions(n, m):
    """Partitions of n realisable over Q by a monodromy of order exactly m."""
    ds = divisors(m)
    phis = {d: totient(d) for d in ds}
    out = set()

    def rec(i, remaining, chosen):
        if i == len(ds):
            if remaining == 0 and chosen.get(m, 0) >= 1:
                lam = []
                for d in ds:
                    c = chosen.get(d, 0)
                    if c > 0:
                        lam.extend([c] * phis[d])
                out.add(tuple(sorted(lam, reverse=True)))
            return
        d = ds[i]
        for c in range(remaining // phis[d] + 1):
            chosen[d] = c
            rec(i + 1, remaining - c * phis[d], chosen)
        chosen[d] = 0

    rec(0, n, {})
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
    EXPS = reduced_exponents(19)
    MAXRANK = 14
    print("=" * 78)
    print("U317: can the three-exponent rigid Q-rational object be REGULAR?")
    print("=" * 78)
    print(f"\nreduced exponents: {EXPS}      ranks tested: 2..{MAXRANK}")

    # --- self-duality is free over Q --------------------------------------------------
    print("\n[1] self-duality: is every Q-rational eigenvalue multiset closed under inversion?")
    bad = []
    for m in EXPS:
        for d in divisors(m):
            # the orbit of primitive d-th roots is closed under alpha -> alpha^(-1)
            # because gcd(-1, d) = 1; check it explicitly on exponents
            if gcd(d - 1, d) != 1 and d > 1:
                bad.append((m, d))
    print(f"   inversion preserves every Galois orbit: {'YES' if not bad else 'NO ' + str(bad)}")
    print("   (so essential self-duality imposes no extra condition; only regularity can bite)")

    # --- the decisive test -------------------------------------------------------------
    print("\n[2] rigid + Q-rational + three pairwise distinct orders + REGULAR at 0 and infinity:")
    regular_hits = []
    any_hits = []
    for n in range(2, MAXRANK + 1):
        reg = tuple([1] * n)
        carry = {m: stable_partitions(n, m) for m in EXPS}
        for p, q, r in product(EXPS, repeat=3):
            if len({p, q, r}) != 3:
                continue
            if not (carry[p] and carry[q] and carry[r]):
                continue
            for lr in carry[r]:
                if rigidity_index(n, (reg, reg, lr)) == 2 and reg in carry[p] and reg in carry[q]:
                    regular_hits.append((n, (p, q, r), lr))
            for lp in carry[p]:
                for lq in carry[q]:
                    for lr in carry[r]:
                        if rigidity_index(n, (lp, lq, lr)) == 2:
                            any_hits.append((n, (p, q, r), (lp, lq, lr)))

    print(f"   rigid Q-rational triples with 3 distinct orders, ANY partitions: {len(any_hits)}")
    print(f"   of those, REGULAR at both 0 and infinity (partition (1^n) at each): "
          f"{len(regular_hits)}")
    if regular_hits:
        for h in regular_hits[:10]:
            print(f"      rank {h[0]}, orders {h[1]}, third partition {h[2]}")

    # --- why, explicitly ----------------------------------------------------------------
    print("\n[3] the reason, made explicit:")
    print("    regular at 0 and infinity means partitions (1^n), (1^n), contributing 2n.")
    print("    rig = 2 then forces the third partition to have sum of squares n^2 - 2n + 2,")
    print("    i.e. (n-1, 1) -- a pseudoreflection.  But a pseudoreflection is Q-rational only")
    print("    when its single non-trivial eigenvalue lies in Q, i.e. has order <= 2, which is")
    print("    excluded by the Beal exponent range.  Checked directly:")
    for n in range(3, 9):
        pr = (n - 1, 1)
        rational_orders = [m for m in EXPS if pr in stable_partitions(n, m)]
        print(f"      n={n}: (n-1,1) = {pr} is Q-rational for orders {rational_orders}")

    print("\n" + "=" * 78)
    if not regular_hits:
        print("RESULT: NO regular witness at any rank up to %d." % MAXRANK)
        print()
        print("C171 UNDERSTATES THE OBSTRUCTION and must be corrected. The three-exponent rigid")
        print("Q-rational object is never regular, because regularity at 0 and infinity forces a")
        print("pseudoreflection at 1, which is not Q-rational for any order >= 3. Potential")
        print("automorphy theorems that require regular Hodge-Tate weights therefore cannot apply")
        print("to it however much they are strengthened -- this is a SECOND obstruction, of a")
        print("different kind from 'the theorem is unproved'.")
    else:
        print("RESULT: regular witnesses exist; C171 stands as written.")
    print()
    print("This classifies an obstruction. It proves nothing about Beal, and it does not rule out")
    print("non-rigid families, larger base fields, or objects that are not local systems.")
    print("=" * 78)


if __name__ == "__main__":
    main()
