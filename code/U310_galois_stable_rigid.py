#!/usr/bin/env python3
"""
U310: obligation (c) of pool C169 — can a rigid triple with three pairwise distinct local orders
be defined over Q?

BACKGROUND
----------
U309 refuted the U258 obstruction as stated: Katz rigidity alone does not forbid three pairwise
distinct local monodromy orders, because a pseudoreflection (n-1,1) realises any order with only
two distinct eigenvalues.  C169 then listed three untested obligations.  This script tests (c),
which is the cheapest and the most likely to bite:

    a local system defined over Q has local monodromy whose CHARACTERISTIC POLYNOMIAL lies in
    Q[T], so its eigenvalue multiset must be stable under Gal(Q(zeta_m)/Q).

THE EXACT CRITERION
-------------------
Galois acts on the m-th roots of unity with orbits = the primitive d-th roots, one orbit per
divisor d | m, of size phi(d).  A multiset of m-th roots is Galois stable iff every root in a
given orbit carries the SAME multiplicity.  So a stable multiset is exactly a choice of
multiplicities

    c_d >= 0   for each d | m,

contributing phi(d) eigenvalues of multiplicity c_d each.  The monodromy has order exactly m iff
c_m >= 1 (some primitive m-th root actually occurs).

Hence: a partition lambda of n is realisable over Q at a puncture of order m iff lambda equals,
as a multiset, the union over d | m of (phi(d) copies of c_d) for some such c with c_m >= 1.

This is a finite exact check.  No floating point.

WHAT IS BEING DECIDED
---------------------
For every rank n and every partition triple with Katz rigidity index exactly 2, ask whether there
are three PAIRWISE DISTINCT reduced Beal exponents (p, q, r) realisable simultaneously over Q.
A negative answer restores the U258 obstruction on CORRECT grounds -- rationality, not rigidity.
A positive answer leaves C169's direction open and names the witness.
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


def divisors(m):
    return [d for d in range(1, m + 1) if m % d == 0]


def totient(m):
    return sum(1 for k in range(1, m + 1) if gcd(k, m) == 1)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def rigidity_index(n, triple):
    return -n * n + sum(sum(x * x for x in lam) for lam in triple)


def stable_partitions(n, m):
    """All partitions of n realisable over Q by a monodromy of order exactly m.

    Enumerate multiplicity vectors (c_d) over d | m with sum_d phi(d)*c_d = n and c_m >= 1.
    """
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
        maxc = remaining // phis[d]
        for c in range(maxc + 1):
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
    MAXRANK = 10
    print("=" * 78)
    print("U310: obligation (c) of C169 -- rigidity PLUS definability over Q")
    print("=" * 78)
    print(f"\nreduced exponents: {EXPS}      ranks tested: 2..{MAXRANK}")

    # --- sanity controls on the Galois criterion ------------------------------------------
    print("\n[control] partitions realisable over Q at a puncture of order m:")
    for m in [3, 4, 5, 7]:
        for n in [2, 3, 4, 5]:
            sp = sorted(stable_partitions(n, m))
            print(f"   m={m}, n={n}: {sp if sp else 'NONE'}")
    print("   note the pseudoreflection (n-1,1) is absent for every m >= 3:")
    print("   a single primitive m-th root of unity with multiplicity 1 is not Galois stable")
    print("   unless phi(m) = 1, i.e. m <= 2 -- and m = 2 is excluded by the Beal exponent range.")

    # --- the decisive test -----------------------------------------------------------------
    print("\n[decisive test] rigid triples, definable over Q, with 3 pairwise distinct orders:")
    hits = []
    for n in range(2, MAXRANK + 1):
        # for each exponent, the partitions of n it can carry over Q
        carry = {m: stable_partitions(n, m) for m in EXPS}
        for p, q, r in product(EXPS, repeat=3):
            if len({p, q, r}) != 3:
                continue
            if not (carry[p] and carry[q] and carry[r]):
                continue
            for lp in carry[p]:
                for lq in carry[q]:
                    for lr in carry[r]:
                        if rigidity_index(n, (lp, lq, lr)) == 2:
                            hits.append((n, (p, q, r), (lp, lq, lr)))
        if hits and hits[-1][0] == n:
            pass

    if not hits:
        print("   NONE for any rank 2..%d and any pairwise distinct (p,q,r) from the list." % MAXRANK)
        print("\n   => The U258 obstruction is RESTORED, on correct grounds: not rigidity, but")
        print("      rigidity TOGETHER WITH definability over Q. The pseudoreflection that")
        print("      rescued three distinct orders in U309 is not rational.")
    else:
        print(f"   {len(hits)} witness(es). First few:")
        for h in hits[:20]:
            print(f"   rank {h[0]}, orders {h[1]}, partitions {h[2]}")

    print("\n" + "=" * 78)
    print("SCOPE.  This constrains local systems on P^1 minus {0,1,infinity} that are RIGID and")
    print("defined over Q.  It says nothing about non-rigid families (which cost a moduli of")
    print("dimension (n-1)(n-2)), about systems over a number field K with the exponents split")
    print("between K and Q, or about objects that are not local systems at all.  It is an")
    print("obstruction inside one setting, not a theorem about Beal.")
    print("=" * 78)


if __name__ == "__main__":
    main()
