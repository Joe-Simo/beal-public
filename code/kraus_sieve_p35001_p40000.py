#!/usr/bin/env python3
"""
Kraus Sieve Modular Elimination Frontier: Exponent Range p in [35001, 40000]
Signature: (3, 3, p)
Target Newforms:
  - Level 72:  72a1  (y^2 = x^3 + 6x - 7)
  - Level 144: 144a1 (y^2 = x^3 + 6x + 7, quadratic twist by -4)

Eliminates all prime exponents in [35001, 40000] by searching for
auxiliary primes q = 2kp + 1 (with k <= 50, adaptive up to 100) that produce a local
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
OUTPUT_FILE = REPO_ROOT / "research" / "pool" / "evidence" / "kraus_sieve_p35001_p40000.json"


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
    Since |Up| = 2k is small (<= 200 for k <= 100), generate Up in O(k) via primitive root.
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
    for u in Up:
        # Case A: (u - 1) mod q
        tA = (u - 1) % q
        if tA != 0:
            valid_t.add(tA)
        # Case B: (u - 1) * 3^(-1) mod q
        tB = ((u - 1) * inv3) % q
        if tB != 0:
            valid_t.add(tB)
        # Case C: (u - 3^(p-1)) * 3^(-1) mod q
        tC = ((u - inv3_p1) * inv3) % q
        if tC != 0:
            valid_t.add(tC)

    return Up, valid_t


def compute_admissible_frey_traces(p: int, q: int, valid_t: set[int], leg: list[int]) -> set[int]:
    """
    Compute admissible Frey curve Frobenius traces a_q(E_t) for all valid ratios t in F_q.
    Frey curve model for signature (3, 3, p):
      E_t : y^2 = x^3 + 3*(t+1)*x^2 + (3/4)*(t+1)^2*x + (1/4)*(t^2 + t + 1)*t*x ...
    Direct short Weierstrass form:
      E_t: y^2 = x^3 - 3*t*(t+1)*x + t*(t+1)*(2t+1)
      a4(t) = -3*t*(t+1) mod q
      a6(t) = t*(t+1)*(2*t+1) mod q
    When q | t*(t+1), E has bad reduction at q (not coprime case).
    """
    adm_traces = set()
    for t in valid_t:
        t_plus_1 = (t + 1) % q
        if t_plus_1 == 0:
            continue
        prod = (t * t_plus_1) % q
        a4 = (-3 * prod) % q
        a6 = (prod * (2 * t + 1)) % q
        aq = trace_weierstrass_fast(a4, a6, q, leg)
        adm_traces.add(aq)

    return adm_traces


def eliminate_exponent(p: int, max_k: int = 100) -> dict[str, object] | None:
    """
    Search for an auxiliary prime q = 2kp + 1 such that both newforms 72a1 and 144a1
    are eliminated by local Frobenius trace obstruction.
    """
    for k in range(1, max_k + 1):
        q = 2 * k * p + 1
        if not sympy.isprime(q):
            continue

        # Condition: 16q < p^2 for integer rigidity
        if 16 * q >= p * p:
            continue

        leg = build_legendre_table(q)

        # Traces of target newforms:
        # 72a1: y^2 = x^3 + 6x - 7
        aq_72 = trace_weierstrass_fast(6, -7, q, leg)
        # 144a1: y^2 = x^3 + 6x + 7
        aq_144 = trace_weierstrass_fast(6, 7, q, leg)

        Up, valid_t = solve_descent_residues_fast(p, q, k)
        adm = compute_admissible_frey_traces(p, q, valid_t, leg)

        # Check Kraus condition: aq(f) mod p not in {a mod p : a in Adm_q(E)}
        if aq_72 not in adm and aq_144 not in adm:
            return {
                "p": p,
                "q": q,
                "k": k,
                "aq_72": aq_72,
                "aq_144": aq_144,
                "aq_72_mod_p": aq_72 % p,
                "aq_144_mod_p": aq_144 % p,
                "size_Up": len(Up),
                "size_valid_t": len(valid_t),
                "size_adm": len(adm),
                "eliminated_72a1": True,
                "eliminated_144a1": True,
            }

    return None


def worker_task(p: int) -> tuple[int, dict[str, object] | None]:
    return p, eliminate_exponent(p, max_k=100)


def main():
    p_min, p_max = 35001, 40000
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
                print(f"[{completed:3d}/{len(primes)}] p = {p:5d} -> UNELIMINATED (exhausted k <= 100)")

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
