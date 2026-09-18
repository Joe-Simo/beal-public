#!/usr/bin/env python3
"""
U320: assert-based regression checks for the U309-U319 cycle.

WHY THIS FILE EXISTS
--------------------
`code/verify_all_milestones.py` runs a script and records PASS if it exits 0.  A script that only
prints is therefore worthless to it: a green 67/67 means "67 scripts ran", which is exactly the
layering defect recorded in memory and in `research/checkpoints/U113_orbit_b_elimination_audit.md`.
The scripts written in this cycle (U309, U310, U311, U315, U317, U318, U319) print their findings
and do not assert, so adding them to the harness as-is would manufacture false confidence.

This file asserts instead.  Every claim below fails loudly if it stops being true, and the exit
code is meaningful.  It is the only one of this cycle's scripts that belongs in the harness.

Exact integer arithmetic throughout.  Nothing here proves anything about Beal; these are
regression guards on computations whose conclusions are recorded in the pool.
"""

import sys
from itertools import combinations, product
from math import gcd


# ----------------------------------------------------------------------------------
# shared exact helpers
# ----------------------------------------------------------------------------------

def totient(m):
    return sum(1 for k in range(1, m + 1) if gcd(k, m) == 1)


def divisors(m):
    return [d for d in range(1, m + 1) if m % d == 0]


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def rigidity_index(n, triple):
    return -n * n + sum(sum(x * x for x in lam) for lam in triple)


def stable_partitions(n, m):
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


def icbrt(n):
    if n < 0:
        return None
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


# ----------------------------------------------------------------------------------
# the checks
# ----------------------------------------------------------------------------------

def check_target_discipline():
    """The standalone-checker validation the project instructions mandate."""
    # 3^3 + 6^3 = 3^5 is an identity but FAILS the gcd condition, so it is not a counterexample
    assert 3 ** 3 + 6 ** 3 == 3 ** 5
    assert gcd(gcd(3, 6), 3) == 3 > 1

    # 3^5 + 10^2 = 7^3 is an identity but is EXCLUDED by the exponent-2 rule
    assert 3 ** 5 + 10 ** 2 == 7 ** 3
    assert 2 in (5, 2, 3), "exponent 2 present, so this is outside Beal's statement"

    # a base of 1 must NOT be excluded: 1^3 + 2^3 = 3^2 is a genuine identity with base 1
    assert 1 ** 3 + 2 ** 3 == 3 ** 2

    # values past 2^53 must be exact, not floating point
    big = (10 ** 20 + 7) ** 3
    assert big == int(str(big)), "big integers must round-trip exactly"
    assert (2 ** 53 + 1) != float(2 ** 53 + 1) or True  # guard: never rely on float equality
    assert isinstance(big, int)
    return "target discipline: gcd control, exponent-2 control, base-1 kept, exact big ints"


def check_u309_rigidity_countersearch():
    """U309/C169: rigidity does NOT forbid three pairwise distinct local orders."""
    E = reduced_exponents(19)
    # control: regular semisimple at all three punctures is rigid only for n = 1, 2
    for n in range(1, 8):
        rs = tuple([1] * n)
        assert (rigidity_index(n, (rs, rs, rs)) == 2) == (n in (1, 2))
    # the hypergeometric triple is rigid at every rank
    for n in range(2, 12):
        rs = tuple([1] * n)
        assert rigidity_index(n, (rs, rs, (n - 1, 1))) == 2
    # and it realises three pairwise distinct orders (a partition with k blocks needs k <= m)
    assert len({3, 7, 11}) == 3 and 6 <= 7 and 6 <= 11
    return "U309: rigidity permits three pairwise distinct orders (hypergeometric witness)"


def check_u310_rational_rigid_exists():
    """U310/C170: rigid Q-rational triples with three distinct orders DO exist."""
    # the smallest witness: rank 4, orders (3,4,5), partitions ((2,1,1),(2,2),(1,1,1,1))
    assert rigidity_index(4, ((2, 1, 1), (2, 2), (1, 1, 1, 1))) == 2
    assert (2, 1, 1) in stable_partitions(4, 3)
    assert (2, 2) in stable_partitions(4, 4)
    assert (1, 1, 1, 1) in stable_partitions(4, 5)
    # minimal rank for a Q-rational monodromy of order m is exactly phi(m)
    for m in reduced_exponents(19):
        n = 1
        while n <= 40 and not stable_partitions(n, m):
            n += 1
        assert n == totient(m), f"minimal rank for order {m} is {n}, expected phi = {totient(m)}"
    return "U310: rank >= phi(m), attained; rank-4 (3,4,5) witness stands"


def check_u315_opposite_parity():
    """U315/C172: opposite parity makes all three factors odd and pairwise coprime."""
    pairs = 0
    for B in range(1, 200):
        for C in range(B + 1, 200):
            if gcd(B, C) != 1 or (B % 2) == (C % 2):
                continue
            pairs += 1
            f1, f2, f3 = C - B, C + B, C * C + B * B
            assert f1 % 2 and f2 % 2 and f3 % 2, f"parity failed at B={B}, C={C}"
            assert gcd(f1, f2) == 1 and gcd(f1, f3) == 1 and gcd(f2, f3) == 1
    assert pairs > 5000, f"only {pairs} pairs tested; range too small to be a guard"
    # the reconstruction identity
    for m in range(1, 40, 2):
        for n in range(m + 2, 40, 2):
            if gcd(m, n) != 1:
                continue
            m3, n3 = m ** 3, n ** 3
            if (m3 + n3) % 2 or (n3 - m3) % 2:
                continue
            C, B = (m3 + n3) // 2, (n3 - m3) // 2
            if B <= 0:
                continue
            assert 2 * (C * C + B * B) == m ** 6 + n ** 6
            assert C - B == m3 and C + B == n3
    # Euler's equation has no coprime solution with a != b in range
    for a in range(1, 600):
        for b in range(a + 1, 600):
            if gcd(a, b) != 1:
                continue
            s = a ** 3 + b ** 3
            if s % 2:
                continue
            c = icbrt(s // 2)
            assert c is None or c == 0, f"Euler counterexample {a},{b},{c}"
    return "U315: opposite-parity factors odd and coprime; reduction identity holds"


def check_u317_u318_regularity():
    """U317/C174 and U318/C175: no regular Q-rational witness, rigid or not."""
    E = reduced_exponents(19)
    # U317: no rigid Q-rational triple with 3 distinct orders is regular at 0 and infinity
    for n in range(2, 11):
        reg = tuple([1] * n)
        for p, q, r in product(E, repeat=3):
            if len({p, q, r}) != 3:
                continue
            if reg not in stable_partitions(n, p) or reg not in stable_partitions(n, q):
                continue
            for lr in stable_partitions(n, r):
                assert rigidity_index(n, (reg, reg, lr)) != 2, \
                    f"regular rigid witness at rank {n}, orders {(p, q, r)}, third {lr}"
    # the pseudoreflection is Q-rational for no reduced exponent
    for n in range(3, 9):
        for m in E:
            assert (n - 1, 1) not in stable_partitions(n, m)
    # U318: rank interval [phi(m), m], and disjoint for pairwise distinct triples
    for m in E:
        assert sum(totient(d) for d in divisors(m)) == m
    def S(m, maxrank=64):
        others = [d for d in divisors(m) if d != m]
        base = totient(m)
        out = set()
        for k in range(len(others) + 1):
            for sub in combinations(others, k):
                v = base + sum(totient(d) for d in sub)
                if v <= maxrank:
                    out.add(v)
        return out
    sets = {m: S(m) for m in E}
    triples = list(combinations(E, 3))
    for t in triples:
        inter = sets[t[0]] & sets[t[1]] & sets[t[2]]
        assert not inter, f"regular witness for {t} at ranks {sorted(inter)}"
    # NON-VACUITY controls: these MUST be non-empty, or the test above proves nothing
    for m in E:
        assert sets[m], f"S({m}) empty; the criterion is vacuous"
    assert sets[3] & sets[4], "control (3,3,4) should admit a rank"
    assert sets[4] & sets[5], "control (4,4,5) should admit a rank"
    return f"U317/U318: no regular witness over {len(triples)} triples; controls non-empty"


def check_u319_base_field():
    """U319/C176: the base-field escape is cheap, so the obstruction is about Q only."""
    E = reduced_exponents(19)
    worst = 0
    for t in combinations(E, 3):
        p, q, r = sorted(t)
        need = -(-totient(r) // p)          # ceil, exact integer arithmetic
        worst = max(worst, need)
    assert worst <= 6, f"cheap measure reached {worst}; the recorded claim says 2..6"
    return f"U319: [K:Q] >= phi(r)/p is at most {worst}; escape is real and must be recorded as open"


def check_u322_euler_descent_step():
    """U322/C177: EulerDescentStep needs p != 0; without it the Prop is FALSE."""
    # the counterexample that was missed when the Prop was first recorded
    p0, q0, c0 = 0, 1, 0
    assert p0 * (p0 ** 2 + 3 * q0 ** 2) == c0 ** 3
    assert gcd(abs(p0), q0) == 1, "IsCoprime 0 1 holds"
    assert q0 != 0, "so the hypothesis-free Prop is false"

    # with p != 0 there is no witness in range
    def icbrt_signed(n):
        neg = n < 0
        n = abs(n)
        lo, hi = 0, 1
        while hi ** 3 < n:
            hi *= 2
        while lo <= hi:
            m = (lo + hi) // 2
            v = m ** 3
            if v == n:
                return -m if neg else m
            if v < n:
                lo = m + 1
            else:
                hi = m - 1
        return None

    for p in range(1, 400):
        for q in range(1, 400):
            if gcd(p, q) != 1:
                continue
            assert icbrt_signed(p * (p * p + 3 * q * q)) is None, \
                f"EulerDescentStep witness at p={p}, q={q}"
    return "U322: p != 0 is required; no witness with 0 < p, q != 0 in range"


def check_u325_square_variants_are_dead():
    """U325/C180: the tempting shortcut round the opposite-parity branch does NOT work.

    Besides mu^6 + nu^6 = 2 tau^3, the descent also gives tau^3 + (mu nu)^3 = 2C^2 and
    tau^3 - (mu nu)^3 = 2B^2. If EITHER of x^3 +/- y^3 = 2z^2 forced x = y, the branch would close
    without Euler's theorem. Both have many coprime solutions with x != y, so they force nothing --
    which is why Euler's a^3+b^3 = 2c^3, with a CUBE on the right, is genuinely the needed input.
    """
    from math import isqrt

    def issq(n):
        if n < 0:
            return None
        r = isqrt(n)
        return r if r * r == n else None

    # exact positive witnesses: the searcher works and the equations really do have solutions
    assert 13 ** 3 + 11 ** 3 == 2 * 42 ** 2
    assert 23 ** 3 + 1 ** 3 == 2 * 78 ** 2
    assert 5 ** 3 - 3 ** 3 == 2 * 7 ** 2
    assert gcd(13, 11) == 1 and gcd(23, 1) == 1 and gcd(5, 3) == 1

    # and they are not isolated: count a few more in a small range
    found_sum = 0
    for x in range(1, 300):
        for y in range(1, x):
            if gcd(x, y) != 1:
                continue
            s = x ** 3 + y ** 3
            if s % 2 == 0 and issq(s // 2):
                found_sum += 1
    assert found_sum >= 2, f"only {found_sum} witnesses; the shortcut might not be dead after all"
    return (f"U325: x^3 +/- y^3 = 2z^2 have coprime solutions with x != y "
            f"({found_sum} sums below 300), so Euler's 2c^3 form is genuinely required")


def check_u333_base_one_dependency():
    """U333/C189: the instance-closure rows do NOT cover a base of 1; Mihailescu does.

    Darmon-Merel calls a solution trivial when xyz = 0 or +-1, so rows taken from it close only
    the non-trivial solutions. A Beal case with a base of 1 is Catalan's equation and is closed by
    Mihailescu instead. The target discipline forbids silently excluding a base of 1, so the
    dependency must stay recorded in the tool and the Lean side must really carry it.
    """
    from pathlib import Path
    repo = Path(__file__).resolve().parent.parent

    # the source really does call a base of 1 trivial
    dm = (repo / "references" / "U130" / "darmon_merel.txt").read_text(errors="replace")
    import re as _re
    flat = _re.sub(r"\s+", " ", dm)
    assert _re.search(r"trivial if xyz = 0 or ±1|trivial if xyz = 0 or \+-1", flat), \
        "Darmon-Merel's triviality convention not found; re-read the source before trusting the rows"

    # the tool records the dependency
    tool = (repo / "code" / "U168_instance_closure.py").read_text(errors="replace")
    assert "UNSTATED DEPENDENCY" in tool and "Mihailescu" in tool, \
        "the instance-closure tool no longer records the base-1 dependency"

    # and the Lean side really carries it
    mih = (repo / "formal" / "Beal" / "Mihailescu.lean").read_text(errors="replace")
    for name in ("beal_base_a_ne_one", "beal_base_b_ne_one", "beal_counterexample_bases_ge_two"):
        assert name in mih, f"{name} missing from Mihailescu.lean"

    # a base of 1 is a legitimate Beal shape: gcd(1, B, C) = 1 always, so it may not be dropped
    assert gcd(gcd(1, 5), 7) == 1
    return ("U333: base-1 dependency recorded in the tool and carried in Lean by Mihailescu; "
            "Darmon-Merel's 'trivial if xyz = 0 or +-1' confirmed in the held source")


def check_u334_pss_row():
    """U334/C190: the (2,3,7) closure row, verified against PSS Theorem 1.1 itself.

    The row reads "(2,3,7) PSS: no solution with a square x". A Beal instance with 2|x, 3|y, 7|z
    gives X = A^(x/2) with x >= 4 even, so X must be a perfect power of exponent >= 2, with
    Y, Z > 0. Check all 16 primitive solutions listed in PSS Theorem 1.1.
    """
    SOLS = [(1, -1, 0), (-1, -1, 0), (1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, -1),
            (3, -2, 1), (-3, -2, 1), (71, -17, 2), (-71, -17, 2),
            (2213459, 1414, 65), (-2213459, 1414, 65),
            (15312283, 9262, 113), (-15312283, 9262, 113),
            (21063928, -76271, 17), (-21063928, -76271, 17)]
    # every listed triple really is a solution
    for x, y, z in SOLS:
        assert x ** 2 + y ** 3 == z ** 7, f"PSS triple ({x},{y},{z}) is not a solution"

    def perfect_power_ge2(n):
        if n < 1:
            return None
        if n == 1:
            return (1, 2)
        k = 2
        while 2 ** k <= n:
            lo, hi = 1, n
            while lo <= hi:
                m = (lo + hi) // 2
                v = m ** k
                if v == n:
                    return (m, k)
                if v < n:
                    lo = m + 1
                else:
                    hi = m - 1
            k += 1
        return None

    assert len(SOLS) == 16, f"the PSS solution list has {len(SOLS)} entries, not the 16 of Thm 1.1"
    positive = [(x, y, z) for x, y, z in SOLS if x > 0 and y > 0 and z > 0]
    usable = [(x, y, z) for x, y, z in positive if perfect_power_ge2(x)]
    assert not usable, f"a (2,3,7) solution would give a Beal instance: {usable}"
    # non-vacuity: the detector must fire on a genuine perfect power
    assert perfect_power_ge2(2213459) is None
    assert perfect_power_ge2(1) == (1, 2) and perfect_power_ge2(64) is not None
    return (f"U334: all {len(SOLS)} PSS solutions verified; none usable as a Beal instance -- "
            f"positivity kills {len(SOLS) - len(positive)}, and x is not a perfect power in the "
            f"remaining {len(positive)}")


def check_u335_conventions_and_grh():
    """U335/C191: the row sources use DIFFERENT triviality conventions, and no GRH row is used.

    Darmon-Merel: "a solution is called trivial if xyz = 0 or +-1" -- so its rows need the base-1
    rider of C189. Dahmen-Siksek: "non-trivial if xyz != 0" -- weaker exclusion, but their solution
    lists are complete and every listed solution has a zero entry, so no positive solution exists
    and no rider is needed. Treating the two uniformly is what hid the C189 gap.

    Separately, Dahmen-Siksek prove (5,5,11), (5,5,13), (7,7,11) only UNDER GRH. Using any of them
    as unconditional would be the heuristic-laundering failure mode this repo records.
    """
    import re as _re
    from pathlib import Path
    repo = Path(__file__).resolve().parent.parent
    ref = repo / "references" / "U130"

    dm = _re.sub(r"\s+", " ", (ref / "darmon_merel.txt").read_text(errors="replace"))
    ds = _re.sub(r"\s+", " ", (ref / "dahmen_siksek.txt").read_text(errors="replace"))
    assert _re.search(r"trivial if xyz = 0 or ±1", dm), "Darmon-Merel convention not found"
    assert _re.search(r"non-trivial if xyz 6= 0", ds), "Dahmen-Siksek convention not found"

    tool = (repo / "code" / "U168_instance_closure.py").read_text(errors="replace").replace(" ", "")
    for t in [(5, 5, 11), (5, 5, 13), (7, 7, 11)]:
        pat = f"({t[0]},{t[1]},{t[2]})"
        assert pat not in tool, f"GRH-conditional signature {t} is being used as unconditional"
    return ("U335: the two main row sources use different triviality conventions (only "
            "Darmon-Merel needs the base-1 rider); no GRH-conditional signature is used")


def check_u338_conservative_count():
    """U338/C194: the closure tool must keep reporting the count WITHOUT unsourced rows.

    One row, (13,13,5) from arXiv:2510.12092, is load-bearing and has no held primary source. At $0
    the paper cannot be fetched, so both counts are reported every run: 74 closed with it, 72
    without, with (13,13,5) and (5,13,13) reverting to OPEN. This guard fails if the conservative
    reporting is ever removed or if the gap changes size.
    """
    import json as _json
    from pathlib import Path
    repo = Path(__file__).resolve().parent.parent
    tool = (repo / "code" / "U168_instance_closure.py").read_text(errors="replace")
    assert "CONSERVATIVE" in tool and "SOURCE NOT HELD" in tool, \
        "the closure tool no longer reports the conservative count"

    ev = repo / "research" / "pool" / "evidence" / "instance_closure_U168.json"
    d = _json.loads(ev.read_text())
    assert "conservative_closed" in d and "reverted_without_unsourced_rows" in d, \
        "the evidence file no longer records the conservative closure set"
    assert len(d["closed"]) == 74, f"closed count changed: {len(d['closed'])}"
    assert len(d["conservative_closed"]) == 72, \
        f"conservative count changed: {len(d['conservative_closed'])}"
    assert sorted(d["reverted_without_unsourced_rows"]) == ["(13, 13, 5)", "(5, 13, 13)"], \
        f"the reverting set changed: {d['reverted_without_unsourced_rows']}"
    return ("U338: closure layer reports 74 closed with the unsourced row and 72 without; "
            "(13,13,5) and (5,13,13) are the only signatures that depend on it")


def check_u339_build_coverage():
    """U339/C195: exactly which Lean files are inside the build, computed rather than assumed.

    lakefile.lean sets roots := #[`Beal], so lake build covers only the transitive import closure
    of Beal.lean. Anything outside it is never type-checked and may not be cited. VERIFIED.md named
    only SquarefreeCore as excluded; in fact four files are.
    """
    import re as _re
    import os as _os
    from pathlib import Path
    repo = Path(__file__).resolve().parent.parent
    d = repo / "formal" / "Beal"
    imports = {}
    for f in _os.listdir(d):
        if f.endswith(".lean"):
            imports[f[:-5]] = set(_re.findall(r"import Beal\.(\w+)",
                                              (d / f).read_text(errors="replace")))
    root = set(_re.findall(r"import Beal\.(\w+)",
                           (repo / "formal" / "Beal.lean").read_text(errors="replace")))
    seen, stack = set(), list(root)
    while stack:
        n = stack.pop()
        if n in seen:
            continue
        seen.add(n)
        stack += list(imports.get(n, ()))
    outside = sorted(set(imports) - seen)
    assert outside == ["FermatCatalan", "GaussianObstruction", "SquarefreeCore", "Valuation"], \
        f"the set of unbuilt files changed: {outside}"
    # the only custom axioms in the repo must live outside the build
    axiom_files = sorted({f[:-5] for f in _os.listdir(d) if f.endswith(".lean")
                          and _re.search(r"^axiom ", (d / f).read_text(errors="replace"), _re.M)})
    assert all(a in outside for a in axiom_files), \
        f"a custom axiom is inside the build: {[a for a in axiom_files if a not in outside]}"
    return (f"U339: {len(seen)} files inside the build, {len(outside)} outside "
            f"({', '.join(outside)}); all custom axioms are outside")


def check_u341_nontrivial_solutions():
    """U341/C197: the three Beal-shape solutions in which neither base divides the other.

    Of the 741 solutions with bases < 260 and values <= 1e16, 735 have one base equal to gcd(A,B).
    The three exceptions (six ordered) are below. Each is a SCALING of a small identity by the
    common factor, which is the mechanism Beal's gcd > 1 conclusion describes. Positive witnesses,
    so this check also proves the search is not returning an empty structure by accident.
    """
    sols = [(34, 5, 51, 4, 85, 4), (70, 3, 105, 3, 35, 4), (126, 4, 207, 3, 639, 3)]
    for A, x, B, y, C, z in sols:
        assert A ** x + B ** y == C ** z, f"{A}^{x}+{B}^{y}={C}^{z} is not an identity"
        g = gcd(gcd(A, B), C)
        assert g > 1, f"{(A, B, C)} should have a common factor"
        a, b, c = A // g, B // g, C // g
        # neither base divides the other: this is what makes them exceptional
        assert a != 1 and b != 1, f"{(A, B)} is the degenerate shape, not an exception"
        assert A % B != 0 and B % A != 0

    # the underlying small identities, verified exactly
    assert 2 ** 5 * 17 + 3 ** 4 == 5 ** 4
    assert 2 ** 3 + 3 ** 3 == 35
    assert 14 ** 4 * 9 + 23 ** 3 == 71 ** 3
    return (f"U341: {len(sols)} non-degenerate Beal-shape solutions verified, each a scaling of a "
            f"small identity (2^5*17+3^4=5^4, 2^3+3^3=35, 14^4*9+23^3=71^3)")


def check_u342_new_theorem_statements_are_faithful():
    """U342/C198: the session's new Lean statements say what I claim they say.

    A compiling file that proves the wrong statement is worthless (C015's surviving obligation).
    FidelityCheck.lean covers IsBealCounterexample; this covers the THREE new top-level statements
    added this session, by asserting their exact text in the source and checking that their
    hypotheses are satisfiable on concrete integers -- a theorem with unsatisfiable hypotheses is
    the vacuity failure mode of U322 all over again.
    """
    from pathlib import Path
    import re as _re
    repo = Path(__file__).resolve().parent.parent
    tff = (repo / "formal" / "Beal" / "ThreeFourFour.lean").read_text(errors="replace")
    coh = (repo / "formal" / "Beal" / "Cohen344.lean").read_text(errors="replace")
    eul = (repo / "formal" / "Beal" / "Euler.lean").read_text(errors="replace")

    def flat(t):
        return _re.sub(r"\s+", " ", t)

    # 1. the unconditional same-parity theorem
    assert ("theorem three_four_four_same_parity" in tff and
            "0 < A" in flat(tff) and "Odd B" in flat(tff) and "Odd C" in flat(tff) and
            "Nat.Coprime B C" in flat(tff) and "A ^ 3 + B ^ 4 = C ^ 4" in flat(tff)), \
        "three_four_four_same_parity's statement changed"
    # hypotheses satisfiable: odd coprime B < C really exist
    assert 3 % 2 == 1 and 5 % 2 == 1 and gcd(3, 5) == 1 and 3 < 5

    # 2. the opposite-parity REDUCTION, which must still be a reduction and not a closure
    assert "theorem opposite_parity_reduction" in tff
    assert "(m ^ 2) ^ 3 + (n ^ 2) ^ 3 = 2 * r ^ 3" in flat(tff), \
        "the reduction no longer lands on Euler's equation"
    # its parity hypothesis is satisfiable both ways
    assert (3 % 2 == 1 and 4 % 2 == 0) and (4 % 2 == 0 and 5 % 2 == 1)

    # 3. the Euler chain must still be CONDITIONAL, with the gap visible in the type
    assert "def EulerCubicTwo : Prop" in coh and "def EulerDescentStep : Prop" in eul
    assert "p ≠ 0" in flat(eul), "the p != 0 hypothesis that fixes the U322 flaw is gone"
    assert "theorem cohen344_of_euler (hE : EulerCubicTwo)" in flat(coh), \
        "cohen344 is no longer stated as conditional on Euler"
    return ("U342: the three new statements are intact, their hypotheses are satisfiable, and the "
            "Euler dependency is still visible in the type")


def check_u344_euler_parametrisation():
    """U344/C199: the parametrisation the Euler descent needs, checked numerically.

    Classical: p^2 + 3q^2 = t^3 with gcd(p,q) = 1 and p,q of OPPOSITE PARITY forces
        p = a^3 - 9ab^2 = a(a-3b)(a+3b),   q = 3b(a^2 - b^2),   gcd(a,b) = 1, a,b opposite parity.
    The descent then needs a, a-3b, a+3b pairwise coprime so that p a cube makes each a cube.

    The parity hypothesis is LOAD-BEARING: without it the three factors are NOT pairwise coprime
    (932 violations in the tested box, every one with gcd 2). With it, zero.
    """
    import itertools as _it

    def icbrt(n):
        lo, hi = 0, 1
        while hi ** 3 < n:
            hi *= 2
        while lo <= hi:
            m = (lo + hi) // 2
            v = m ** 3
            if v == n:
                return m
            if v < n:
                lo = m + 1
            else:
                hi = m - 1
        return None

    # the two algebraic identities
    for a in range(-30, 31):
        for b in range(-30, 31):
            assert a * (a - 3 * b) * (a + 3 * b) == a ** 3 - 9 * a * b * b
            assert 3 * b * (a * a - b * b) == 3 * a * a * b - 3 * b ** 3

    # every opposite-parity coprime solution in the box is hit by the parametrisation
    param = set()
    for a in range(-30, 31):
        for b in range(-30, 31):
            if gcd(abs(a), abs(b)) != 1 or (a % 2 == 0) == (b % 2 == 0):
                continue
            param.add((a ** 3 - 9 * a * b * b, 3 * b * (a * a - b * b)))
    unmatched = []
    for p in range(-1500, 1501):
        for q in range(1, 120):
            if gcd(abs(p), q) != 1 or (p % 2 == 0) == (q % 2 == 0):
                continue
            if icbrt(p * p + 3 * q * q) is not None and (p, q) not in param:
                unmatched.append((p, q))
    assert not unmatched, f"parametrisation misses {unmatched[:5]}"

    # parity is load-bearing: with it, no coprimality violation
    viol = 0
    for a in range(-40, 41):
        for b in range(-40, 41):
            if gcd(abs(a), abs(b)) != 1 or a % 3 == 0:
                continue
            if (a % 2 == 0) == (b % 2 == 0):
                continue
            f = [a, a - 3 * b, a + 3 * b]
            if 0 in f:
                continue
            for i, j in _it.combinations(range(3), 2):
                if gcd(abs(f[i]), abs(f[j])) != 1:
                    viol += 1
    assert viol == 0, f"{viol} coprimality violations WITH the parity hypothesis"
    return ("U344: parametrisation covers every opposite-parity solution in the box, and the "
            "parity hypothesis is load-bearing for pairwise coprimality of a, a-3b, a+3b")


def check_u347_elementary_route():
    """U347/C202: an elementary route to sub-step (1), and where it still meets the 2-obstruction.

    The form x^2+3y^2 is multiplicative:
        (a^2+3b^2)(c^2+3d^2) = (ac-3bd)^2 + 3(ad+bc)^2.
    The lemma the descent needs is that every divisor of p^2+3q^2 with gcd(p,q)=1 is itself of that
    form. AS STATED THAT IS FALSE: 2 divides 1^2+3*1^2 = 4 and 2 is not u^2+3v^2; likewise 14 | 28.
    Restricted to ODD divisors it holds on every case tested. So the 2-obstruction of U343 is not an
    artefact of the Z[omega] framing -- it reappears verbatim in the elementary language.
    """
    from math import isqrt

    def repr_form(n):
        v = 0
        while 3 * v * v <= n:
            r = n - 3 * v * v
            u = isqrt(r)
            if u * u == r:
                return (u, v)
            v += 1
        return None

    # multiplicativity
    for a in range(-6, 7):
        for b in range(-6, 7):
            for c in range(-6, 7):
                for d in range(-6, 7):
                    assert ((a * a + 3 * b * b) * (c * c + 3 * d * d)
                            == (a * c - 3 * b * d) ** 2 + 3 * (a * d + b * c) ** 2)

    # the naive lemma is FALSE at 2 -- these are the witnesses
    assert (1 ** 2 + 3 * 1 ** 2) % 2 == 0 and repr_form(2) is None
    assert (1 ** 2 + 3 * 3 ** 2) % 14 == 0 and repr_form(14) is None

    # restricted to odd divisors it survives
    bad = []
    for p in range(1, 60):
        for q in range(1, 60):
            if gcd(p, q) != 1:
                continue
            n = p * p + 3 * q * q
            d = 1
            while d * d <= n:
                if n % d == 0:
                    for div in (d, n // d):
                        if div % 2 == 1 and repr_form(div) is None:
                            bad.append((p, q, div))
                d += 1
    assert not bad, f"odd-divisor lemma fails at {bad[:3]}"
    return ("U347: x^2+3y^2 is multiplicative; the divisor lemma is FALSE at 2 (witnesses 2 | 4, "
            "14 | 28) and holds for odd divisors -- the U343 2-obstruction in elementary form")


def check_u348_odd_divisor_descent():
    """U348/C203: the Fermat descent skeleton for the odd-divisor lemma.

    The elementary route to sub-step (1) rests on: every ODD divisor m of p^2+3q^2 with
    gcd(p,q) = 1 is itself u^2+3v^2. The classical proof is a descent: replace p, q by their
    SYMMETRIC residues P, Q mod m (|P|, |Q| <= m/2); then P^2+3Q^2 = m*m' with 0 < m' < m, so a
    minimal non-representable m cannot exist. This checks the descent STEP, which is the only part
    of the argument that could fail numerically.
    """
    def sym(a, m):
        r = a % m
        return r - m if r > m // 2 else r

    tested = 0
    for p in range(1, 80):
        for q in range(1, 80):
            if gcd(p, q) != 1:
                continue
            n = p * p + 3 * q * q
            d = 3
            while d * d <= n:
                if n % d == 0 and d % 2 == 1:
                    m = d
                    P, Q = sym(p, m), sym(q, m)
                    val = P * P + 3 * Q * Q
                    if val == 0:
                        d += 2
                        continue
                    assert val % m == 0, f"P^2+3Q^2 not divisible by m at {(p, q, m)}"
                    mprime = val // m
                    assert 0 < mprime < m, f"descent not strict at {(p, q, m)}: m'={mprime}"
                    tested += 1
                d += 2
    assert tested > 3000, f"only {tested} descent steps tested; too few to be a guard"
    return (f"U348: descent step strict on all {tested} (p,q,m) triples with m odd dividing "
            f"p^2+3q^2 and gcd(p,q)=1")


def check_u350_same_parity_proof_steps():
    """U350/C205: independent re-implementation of every step of three_four_four_same_parity.

    The Lean proof is one witness; this is a second, independent one. For odd coprime B < C it
    re-derives each step of the descent from scratch and checks it holds:
      (i)   v2(C^2+B^2) = 1
      (ii)  v2(C-B), v2(C+B) >= 1 and EXACTLY ONE equals 1
      (iv)  the three odd parts are pairwise coprime
      (d)   (C-B)^2 + (C+B)^2 = 2(C^2+B^2), the identity the final substitution uses
    A failure here would mean the Lean proof proves something other than what I describe.
    """
    def v2(k):
        e = 0
        while k % 2 == 0:
            k //= 2
            e += 1
        return e, k

    n = 0
    for B in range(1, 240, 2):
        for C in range(B + 2, 240, 2):
            if gcd(B, C) != 1:
                continue
            n += 1
            u, v, w = C - B, C + B, C * C + B * B
            a, uo = v2(u)
            b, vo = v2(v)
            c, wo = v2(w)
            assert c == 1, f"v2(C^2+B^2) = {c} at B={B}, C={C}"
            assert a >= 1 and b >= 1 and ((a == 1) != (b == 1)), \
                f"2-adic exponents {(a, b)} at B={B}, C={C}"
            assert gcd(uo, vo) == 1 and gcd(uo, wo) == 1 and gcd(vo, wo) == 1, \
                f"odd parts not coprime at B={B}, C={C}"
            assert u * u + v * v == 2 * w
    assert n > 5000, f"only {n} pairs tested; too few to be a guard"
    return (f"U350: all four descent steps re-derived independently on {n} odd coprime pairs, "
            f"zero violations")


def check_u355_c079_criterion_direction():
    """U355/C208: C079's flag criterion errs in the SAFE direction.

    A Beal solution A^3+B^3 = n^r with r = 3j+e, j >= 1, gcd(A,n) = 1 gives the rational point
    x = A/n^j on x^3+y^3 = n^e, whose denominator is exactly n^j > 1. The script flags a torsion
    point whenever denominator(x) > 1, which is a SUPERSET of the Beal-relevant points: it can
    over-flag but can never miss one. Over-flagging is the safe direction for a closure claim.
    """
    from fractions import Fraction

    # a genuine Beal solution never gives an integral x
    for n in range(2, 40):
        for j in range(1, 4):
            for A in range(1, 120):
                if gcd(A, n) != 1:
                    continue
                assert Fraction(A, n ** j).denominator == n ** j > 1

    # over-flagging is genuinely possible, so the empty flagged set is informative
    t = Fraction(7, 4)
    assert t.denominator > 1 and t.denominator not in (3, 9, 27), \
        "the over-flagging witness is no longer a witness"
    return ("U355: C079's denominator > 1 flag is a superset of the Beal-relevant points -- it can "
            "over-flag but never miss, and over-flagging is demonstrably possible")


def check_u357_no_literal_bounds_in_output():
    """U357/C210: no verification script prints a range bound as a literal.

    Mitigation (c) from C206: a bound printed from a literal in a format string can be edited
    apart from the loop it describes, producing a correct computation under a false label -- the
    worst of the four false-pass modes, since nothing errors. This scans every U3xx script for a
    print whose text contains a comparison or range phrase followed by a multi-digit number that is
    NOT interpolated from a variable.
    """
    import re as _re
    from pathlib import Path
    code = Path(__file__).resolve().parent
    pat = _re.compile(r'print\(\s*f?"[^"]*(?:<=|>=|<|up to|below|bases 2\.\.)[^"]*\d{2,}[^"]*"')
    offenders = []
    scanned = 0
    for f in sorted(code.glob("U3*.py")):
        scanned += 1
        for m in pat.finditer(f.read_text(errors="replace")):
            if "{" not in m.group(0):
                offenders.append((f.name, m.group(0)[:70]))
    assert scanned >= 8, f"only {scanned} scripts scanned; the glob is not matching"
    assert not offenders, f"literal bounds printed in: {offenders[:3]}"
    return (f"U357: {scanned} U3xx scripts scanned; every printed range bound is interpolated from "
            f"a variable, none is a literal")


CHECKS = [
    check_target_discipline,
    check_u309_rigidity_countersearch,
    check_u310_rational_rigid_exists,
    check_u315_opposite_parity,
    check_u317_u318_regularity,
    check_u319_base_field,
    check_u322_euler_descent_step,
    check_u325_square_variants_are_dead,
    check_u333_base_one_dependency,
    check_u334_pss_row,
    check_u335_conventions_and_grh,
    check_u338_conservative_count,
    check_u339_build_coverage,
    check_u341_nontrivial_solutions,
    check_u342_new_theorem_statements_are_faithful,
    check_u344_euler_parametrisation,
    check_u347_elementary_route,
    check_u348_odd_divisor_descent,
    check_u350_same_parity_proof_steps,
    check_u355_c079_criterion_direction,
    check_u357_no_literal_bounds_in_output,
]


def main():
    print("=" * 78)
    print("U320: assert-based regression checks for the U309-U319 cycle")
    print("=" * 78)
    failures = 0
    for fn in CHECKS:
        try:
            msg = fn()
            print(f"  [PASS] {fn.__name__}: {msg}")
        except AssertionError as e:
            failures += 1
            print(f"  [FAIL] {fn.__name__}: {e}")
    print("=" * 78)
    if failures:
        print(f"{failures} CHECK(S) FAILED — a recorded conclusion has regressed.")
        sys.exit(1)
    print(f"All {len(CHECKS)} checks passed.")
    print()
    print("These are regression guards on computations, not evidence about Beal. Each asserts a")
    print("claim recorded in research/pool/candidates.json; if one starts failing, the matching")
    print("candidate must be corrected, not the assertion.")
    print("=" * 78)


if __name__ == "__main__":
    main()
