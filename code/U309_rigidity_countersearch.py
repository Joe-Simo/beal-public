#!/usr/bin/env python3
"""
U309 COUNTERSEARCH against my own rigidity obstruction (memory item
`beal-rigidity-obstruction`, pool C120-C128, research/checkpoints/U258_rigidity_obstruction.md).

THE CLAIM UNDER ATTACK
----------------------
U258 concluded: "no rigid local system on P^1 minus {0,1,infinity} can carry three independent
Beal exponents", on the grounds that

    regular semisimple at all three punctures  =>  rig = -n^2 + 3n = 2  =>  n <= 2,

and that a rigid triple has at most 2n+2 distinct eigenvalues against 3n for regular semisimple.

THE SUSPECTED FLAW
------------------
Those two computations are correct, but the conclusion conflates two different conditions:

  (a) local monodromy has ORDER p  (what a signature-p exponent actually forces), versus
  (b) local monodromy is REGULAR SEMISIMPLE with eigenvalues of order p  (what U258 assumed).

A pseudoreflection with partition (n-1, 1) has order equal to the order of its single non-trivial
eigenvalue, which may be ANY m.  So (a) does not imply (b).

THE DISCRIMINATING TEST
-----------------------
Exhaustively enumerate partition triples of n and compute Katz's rigidity index

    rig = -n^2 + sum over the three punctures of sum_i (multiplicity_i)^2,

keeping the rigid ones (rig = 2).  For each, compute the set of local monodromy ORDERS that the
partition can realise: a partition with k distinct eigenvalue-blocks can have order exactly m for
any m admitting k distinct m-th roots of unity whose lcm of orders is m, i.e. any m >= 1 with
k <= m (choose a primitive m-th root plus k-1 others).  Then ask the decisive question:

    does there exist a RIGID triple whose three local orders are three PAIRWISE DISTINCT
    reduced Beal exponents?

All arithmetic is exact integer arithmetic on partitions; no floating point anywhere.

WHAT A HIT WOULD AND WOULD NOT MEAN
-----------------------------------
A hit REFUTES the stated obstruction as written.  It does NOT produce a Frey object: it shows the
rigidity budget does not forbid three distinct exponents, so the real obstruction (if any) lies
elsewhere -- in whether such a sheaf can be attached to the Beal equation over Q with the right
Galois/motivic realisation, not in the numerology.  This script proves nothing about Beal.
"""

from itertools import product


def partitions(n, maxpart=None):
    """All partitions of n as non-increasing tuples. Exact, no floats."""
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def sum_sq(lam):
    return sum(m * m for m in lam)


def rigidity_index(n, triple):
    """Katz rigidity index rig = -n^2 + sum of sum_i m_i^2 over the three punctures."""
    return -n * n + sum(sum_sq(lam) for lam in triple)


def num_blocks(lam):
    """Number of distinct eigenvalues the partition prescribes."""
    return len(lam)


def realisable_orders(lam, candidate_orders):
    """Orders m realisable by a monodromy with eigenvalue-multiplicity partition `lam`.

    The partition fixes k = len(lam) distinct eigenvalues.  Order exactly m is realisable iff we
    can pick k distinct m-th roots of unity whose orders have lcm m.  Taking one primitive m-th
    root and k-1 further distinct m-th roots works whenever k <= m.  (For k = 1 the single
    eigenvalue must itself be primitive, which is fine.)
    """
    k = num_blocks(lam)
    return sorted(m for m in candidate_orders if k <= m)


def reduced_exponents(limit):
    """Reduced Beal exponents: 4 together with the odd primes, up to `limit`."""
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
    print("=" * 78)
    print("U309 COUNTERSEARCH: does rigidity forbid three pairwise distinct Beal exponents?")
    print("=" * 78)
    print(f"\nreduced exponents considered: {EXPS}")

    # --- control 1: reproduce the U258 computation that is NOT under attack -------------
    print("\n[control 1] regular semisimple at all three punctures, partition (1^n):")
    for n in range(1, 8):
        rs = tuple([1] * n)
        rig = rigidity_index(n, (rs, rs, rs))
        print(f"   n={n}: rig = -{n}^2 + 3*{n} = {rig}" + ("   <= RIGID" if rig == 2 else ""))
    print("   -> rigid only for n = 1, 2.  U258's computation stands.")

    # --- control 2: the eigenvalue budget ---------------------------------------------
    print("\n[control 2] max distinct eigenvalues over all rigid triples, by rank:")
    for n in range(2, 8):
        best = 0
        best_triple = None
        for triple in product(list(partitions(n)), repeat=3):
            if rigidity_index(n, triple) == 2:
                k = sum(num_blocks(l) for l in triple)
                if k > best:
                    best, best_triple = k, triple
        print(f"   n={n}: max = {best} (= 2n+2 = {2*n+2}? {best == 2*n+2}), attained at {best_triple}")

    # --- the decisive test -------------------------------------------------------------
    print("\n[decisive test] rigid triples whose three local ORDERS are pairwise distinct")
    print("                reduced exponents:")
    hits = []
    for n in range(2, 8):
        parts = list(partitions(n))
        for triple in product(parts, repeat=3):
            if rigidity_index(n, triple) != 2:
                continue
            opts = [realisable_orders(lam, EXPS) for lam in triple]
            for p, q, r in product(*opts):
                if len({p, q, r}) == 3:
                    hits.append((n, triple, (p, q, r)))
                    break
            else:
                continue
            break

    if not hits:
        print("   NONE -- the obstruction as stated survives.")
    else:
        print(f"   {len(hits)} rank(s) admit one.  Smallest witnesses:")
        for n, triple, orders in hits:
            print(f"   n={n}: partitions {triple}, local orders {orders}, rig=2")

    # --- explicit hypergeometric witness ------------------------------------------------
    print("\n[witness] the hypergeometric family, partitions ((1^n), (1^n), (n-1,1)):")
    for n in range(2, 8):
        rs = tuple([1] * n)
        pr = (n - 1, 1) if n >= 2 else (1,)
        triple = (rs, rs, pr)
        rig = rigidity_index(n, triple)
        blocks = sum(num_blocks(l) for l in triple)
        orders0 = realisable_orders(rs, EXPS)
        orders2 = realisable_orders(pr, EXPS)
        print(f"   n={n}: rig={rig}, distinct eigenvalues={blocks}, "
              f"orders at 0,inf from {orders0}, order at 1 from {orders2}")

    print("\n" + "=" * 78)
    print("READ THE RESULT CAREFULLY.  A hit refutes the stated obstruction, not Beal, and")
    print("produces no Frey object: it only shows the rigidity numerology does not forbid three")
    print("pairwise distinct exponents.  Whether such a sheaf is attachable to A^x+B^y=C^z over Q")
    print("with the right motivic realisation is untouched by this computation.")
    print("=" * 78)


if __name__ == "__main__":
    main()
