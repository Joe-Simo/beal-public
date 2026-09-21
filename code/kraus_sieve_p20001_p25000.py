#!/usr/bin/env python3
"""
Kraus Sieve Modular Elimination Frontier: Exponent Range p in [20001, 25000]
Signature: (3, 3, p)
Target Newforms:
  - Level 72:  72a1  (y^2 = x^3 + 6x - 7)
  - Level 144: 144a1 (y^2 = x^3 + 6x + 7, quadratic twist by -4)

Eliminates all prime exponents in [20001, 25000] by searching for
auxiliary primes q = 2kp + 1 (with adaptive k in [1, 300]) that produce a local
Frobenius trace obstruction in the Kraus Frey curve representation.
Parallelized with multiprocessing for high throughput across all CPU cores.
"""
from __future__ import annotations

import concurrent.futures
import json
import os
import time
from pathlib import Path
import sympy

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "research" / "pool" / "evidence" / "kraus_sieve_p20001_p25000.json"


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
    Since |Up| = 2k is small (<= 600 for k <= 300), generate Up in O(k) via primitive root.
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


def eliminate_exponent(p: int, max_k: int = 300) -> dict[str, object] | None:
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


def worker_task(p: int) -> tuple[int, dict[str, object] | None]:
    return p, eliminate_exponent(p, max_k=300)


def main():
    p_min, p_max = 20001, 25000
    primes = list(sympy.primerange(p_min, p_max + 1))
    print("=" * 80)
    print(f"KRAUS MODULAR SIEVE EXTENSION: Signatures (3, 3, p) for p in [{p_min}, {p_max}]")
    print(f"Target Primes: {len(primes)} primes to eliminate against levels 72 and 144")
    print(f"Parallel Workers: {os.cpu_count() or 8}")
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

    workers = os.cpu_count() or 8
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(worker_task, p): p for p in primes}
        completed = 0
        for fut in concurrent.futures.as_completed(futures):
            p, cert = fut.result()
            completed += 1
            if cert:
                certificates.append(cert)
                if completed % 50 == 0 or completed == len(primes):
                    print(f"[{completed:3d}/{len(primes)}] p = {p:5d} -> ELIMINATED with q = {cert['q']:8d} (k={cert['k']:2d}, |Adm|={cert['size_adm']})")
            else:
                uneliminated.append(p)
                print(f"[{completed:3d}/{len(primes)}] p = {p:5d} -> UNELIMINATED (exhausted k <= 300)")

    elapsed = time.time() - t0
    rate = len(certificates) / len(primes) * 100.0

    # Sort certificates by prime p
    certificates.sort(key=lambda c: c["p"])

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
        "exponent_range": [p_min, p_max],
        "prime_count": len(primes),
        "eliminated_count": len(certificates),
        "uneliminated_count": len(uneliminated),
        "elimination_rate_percent": rate,
        "all_eliminated": len(certificates) == len(primes),
        "max_multiplier_k": max(c["k"] for c in certificates) if certificates else 0,
        "elapsed_seconds": round(elapsed, 4),
        "target_newforms": ["72a1", "144a1"],
        "certificates": certificates
    }

    OUTPUT_FILE.write_text(json.dumps(result_data, indent=2))
    print(f"Wrote Kraus elimination certificates to: {OUTPUT_FILE}")

    if uneliminated:
        print(f"WARNING: {len(uneliminated)} primes were not eliminated: {uneliminated}")
        exit(1)


if __name__ == "__main__":
    main()
