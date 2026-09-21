#!/usr/bin/env python3
"""
Kraus Sieve Modular Elimination Frontier: Exponent Range p in [15001, 20000]
Signature: (3, 3, p)
Target Newforms:
  - Level 72:  72a1  (y^2 = x^3 + 6x - 7)
  - Level 144: 144a1 (y^2 = x^3 + 6x + 7, quadratic twist by -4)

Eliminates all prime exponents in [15001, 20000] by searching for
auxiliary primes q = 2kp + 1 (with adaptive k in [1, 200]) that produce a local
Frobenius trace obstruction in the Kraus Frey curve representation.
"""
from __future__ import annotations

import json
import time
from pathlib import Path
import sympy

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "research" / "pool" / "evidence" / "kraus_sieve_p15001_p20000.json"


def build_legendre_table(q: int) -> list[int]:
    """Precompute the Legendre symbol table mod q in O(q) via Euler's criterion."""
    leg = [0] * q
    q_half = (q - 1) // 2
    for r in range(1, q):
        v = pow(r, q_half, q)
        leg[r] = -1 if v == q - 1 else 1
    return leg


def trace_weierstrass_fast(a4: int, a6: int, q: int, leg: list[int]) -> int:
    """Compute Frobenius trace a_q for y^2 = x^3 + a4*x + a6 over F_q."""
    s = 0
    for x in range(q):
        rhs = (x * (x * x + a4) + a6) % q
        s += leg[rhs]
    return -s


def solve_descent_residues_fast(p: int, q: int, k: int) -> tuple[set[int], set[int]]:
    """
    Compute Up = (F_q^*)^p and valid affine ratios t = A/B mod q.
    Since |Up| = 2k is small (<= 400 for k <= 200), generate Up in O(k) via primitive root.
    """
    g = sympy.primitive_root(q)
    gen_Up = pow(g, p, q)
    Up = set()
    cur = 1
    for _ in range(2 * k):
        Up.add(cur)
        cur = (cur * gen_Up) % q

    inv3 = pow(3, -1, q)
    inv3_p1 = pow(pow(3, p - 1, q), -1, q)

    valid_t = set()
    for t in range(q):
        if (t + 1) % q == 0:
            continue
        f1 = (t + 1) % q
        f2 = (t * t - t + 1) % q

        # Subcase 1: 3 does not divide C
        if f1 in Up and f2 in Up:
            valid_t.add(t)
            continue

        # Subcase 2: 3 divides C
        if ((f1 * inv3_p1) % q in Up) and ((f2 * inv3) % q in Up):
            valid_t.add(t)
            continue
        if ((f1 * inv3) % q in Up) and ((f2 * inv3_p1) % q in Up):
            valid_t.add(t)
            continue

    return Up, valid_t


def eliminate_exponent(p: int, max_k: int = 200) -> dict[str, object] | None:
    """Search for an eliminating auxiliary prime q = 2kp + 1 for exponent p."""
    a4_72, a6_72 = 6, -7
    a4_144, a6_144 = 6, 7

    for k in range(1, max_k + 1):
        q = 2 * k * p + 1
        if not sympy.isprime(q) or (q % 72 == 0) or (q % 144 == 0):
            continue

        leg = build_legendre_table(q)
        aq_72 = trace_weierstrass_fast(a4_72, a6_72, q, leg)
        aq_144 = trace_weierstrass_fast(a4_144, a6_144, q, leg)

        pm_qplus1 = {(q + 1) % p, (-(q + 1)) % p}
        q_can_divide_C = ((aq_72 % p) in pm_qplus1) or ((aq_144 % p) in pm_qplus1)

        Up, valid_t = solve_descent_residues_fast(p, q, k)

        adm = set()
        if q_can_divide_C:
            adm.update(pm_qplus1)

        aq_inf = trace_weierstrass_fast(0, -1, q, leg)
        adm.add(aq_inf % p)
        adm.add((-aq_inf) % p)

        for t in valid_t:
            a4_t = (3 * t) % q
            a6_t = (1 - pow(t, 3, q)) % q
            aq_t = trace_weierstrass_fast(a4_t, a6_t, q, leg)
            adm.add(aq_t % p)
            adm.add((-aq_t) % p)

        elim_72 = (aq_72 % p not in adm)
        elim_144 = (aq_144 % p not in adm)

        if elim_72 and elim_144:
            return {
                "p": p,
                "k": k,
                "q": q,
                "aq_72": aq_72,
                "aq_72_mod_p": aq_72 % p,
                "aq_144": aq_144,
                "aq_144_mod_p": aq_144 % p,
                "size_Up": len(Up),
                "size_valid_t": len(valid_t),
                "size_adm": len(adm),
                "eliminated_72a1": True,
                "eliminated_144a1": True,
            }

    return None


def main():
    p_min, p_max = 15001, 20000
    primes = list(sympy.primerange(p_min, p_max + 1))
    print("=" * 80)
    print(f"KRAUS MODULAR SIEVE EXTENSION: Signatures (3, 3, p) for p in [{p_min}, {p_max}]")
    print(f"Target Primes: {len(primes)} primes to eliminate against levels 72 and 144")
    print("=" * 80)

    # Positive control: verify LMFDB known traces
    leg5 = build_legendre_table(5)
    leg13 = build_legendre_table(13)
    assert trace_weierstrass_fast(6, -7, 5, leg5) == 2, "72a1 trace at 5 must be 2"
    assert trace_weierstrass_fast(6, -7, 13, leg13) == -2, "72a1 trace at 13 must be -2"
    print("[PASS] Known LMFDB trace calibration verified.")

    t0 = time.time()
    certificates = []
    uneliminated = []

    for i, p in enumerate(primes, 1):
        cert = eliminate_exponent(p, max_k=200)
        if cert:
            certificates.append(cert)
            if i % 50 == 0 or i == len(primes):
                print(f"[{i:3d}/{len(primes)}] p = {p:5d} -> ELIMINATED with q = {cert['q']:7d} (k={cert['k']:2d}, |Adm|={cert['size_adm']})")
        else:
            uneliminated.append(p)
            print(f"[{i:3d}/{len(primes)}] p = {p:5d} -> UNELIMINATED (exhausted k <= 200)")

    elapsed = time.time() - t0
    rate = len(certificates) / len(primes) * 100.0

    print("=" * 80)
    print("KRAUS MODULAR SIEVE EXTENSION SUMMARY:")
    print(f"  Target Range:           p in [{p_min}, {p_max}]")
    print(f"  Total Primes:           {len(primes)}")
    print(f"  Successfully Eliminated: {len(certificates)} / {len(primes)} ({rate:.2f}%)")
    print(f"  Uneliminated Primes:    {len(uneliminated)}")
    print(f"  Elapsed Time:           {elapsed:.2f} seconds")
    print("=" * 80)

    result_data = {
        "status": "completed",
        "p_min": p_min,
        "p_max": p_max,
        "primes_count": len(primes),
        "eliminated_count": len(certificates),
        "elimination_rate_pct": rate,
        "all_eliminated": (len(uneliminated) == 0),
        "elapsed_seconds": elapsed,
        "certificates": certificates,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(result_data, f, indent=2)
    print(f"Logged {len(certificates)} certificates to: {OUTPUT_FILE}")

    assert len(uneliminated) == 0, f"Failed to eliminate {len(uneliminated)} primes: {uneliminated}"
    print(f"[SUCCESS] 100% of primes in [{p_min}, {p_max}] unconditionally eliminated against newforms 72a1 and 144a1.")


if __name__ == "__main__":
    main()
