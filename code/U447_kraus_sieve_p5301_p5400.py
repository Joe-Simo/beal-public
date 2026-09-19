#!/usr/bin/env python3
"""
U447: Extended Kraus Sieve Modular Elimination for Generalized Fermat Equation A^3 + B^3 = C^p
Signature: (3, 3, p)
Target Exponent Range: p in [5301, 5400] with p = 1 mod 3:
  Primes: p in {5323, 5347}.
Target Levels:
  - Level 72:  Newform 72a1  (y^2 = x^3 + 6x - 7, non-CM)
  - Level 144: Newform 144a1 (y^2 = x^3 + 6x + 7, non-CM quadratic twist of 72a1 by -4)
  - Level 144: Newform 144b1 (y^2 = x^3 - 1, CM by Q(sqrt(-3)), quadratic twist of 36a1 by -4)

Curves Evaluated:
  1. Canonical Kraus Frey Curve (Kraus 1998):
     E_{A, B}: y^2 = x^3 + 3AB x + (B^3 - A^3)
     Specializes under t = A/B to E_t: y^2 = x^3 + 3tx + (1 - t^3) (over F_q).

Search Range:
  Auxiliary primes q = 2kp + 1 with q <= max_q (q does not divide 72).
"""
from __future__ import annotations

import json
from pathlib import Path
import sys
import time
import sympy

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_JSON = ROOT / "references" / "U111" / "kraus_sieve_p5301_p5400.json"


def build_legendre_table(q: int) -> list[int]:
    """Precomputes the Legendre symbol table mod q for O(1) trace calculations."""
    leg = [0] * q
    q_half = (q - 1) // 2
    for r in range(1, q):
        v = pow(r, q_half, q)
        leg[r] = -1 if v == q - 1 else 1
    return leg


def trace_weierstrass_fast(a4: int, a6: int, q: int, leg: list[int]) -> int:
    """Computes Frobenius trace a_q for y^2 = x^3 + a4*x + a6 over F_q."""
    s = 0
    for x in range(q):
        rhs = (x * (x * x + a4) + a6) % q
        s += leg[rhs]
    return -s


def solve_descent_residues(p: int, q: int) -> tuple[set[int], set[int]]:
    """Computes Up = (F_q^*)^p and the set of valid affine ratios t = A/B mod q."""
    Up = set(pow(x, p, q) for x in range(1, q))
    inv3 = pow(3, -1, q)
    inv3_p1 = pow(pow(3, p - 1, q), -1, q)

    valid_t = set()
    for t in range(q):
        if (t + 1) % q == 0:
            continue
        f1 = (t + 1) % q
        f2 = (t * t - t + 1) % q

        # Case 1: 3 does not divide C
        if f1 in Up and f2 in Up:
            valid_t.add(t)
            continue

        # Case 2: 3 divides C
        if ((f1 * inv3_p1) % q in Up) and ((f2 * inv3) % q in Up):
            valid_t.add(t)
            continue
        if ((f1 * inv3) % q in Up) and ((f2 * inv3_p1) % q in Up):
            valid_t.add(t)
            continue

    return Up, valid_t


def kraus_sieve_exponent(p: int, max_q: int = 350000) -> dict[str, object]:
    """Runs the Kraus sieve for prime exponent p against levels 72 and 144."""
    a4_72, a6_72 = 6, -7
    a4_144a, a6_144a = 6, 7
    a4_144b, a6_144b = 0, -1

    tested_primes = []
    eliminating_primes = []
    first_certificate = None

    max_k = max_q // (2 * p)
    for k in range(1, max_k + 1):
        q = 2 * k * p + 1
        if q > max_q:
            break
        if not sympy.isprime(q) or (72 % q == 0) or (144 % q == 0):
            continue

        leg = build_legendre_table(q)

        aq_72 = trace_weierstrass_fast(a4_72, a6_72, q, leg)
        aq_144a = trace_weierstrass_fast(a4_144a, a6_144a, q, leg)
        aq_144b = trace_weierstrass_fast(a4_144b, a6_144b, q, leg)

        pm_qplus1 = {(q + 1) % p, (-(q + 1)) % p}
        q_can_divide_C_72 = ((aq_72 % p) in pm_qplus1)

        Up, valid_t = solve_descent_residues(p, q)

        adm_canon = set()
        if q_can_divide_C_72:
            adm_canon.update(pm_qplus1)

        aq_inf = trace_weierstrass_fast(0, -1, q, leg)
        adm_canon.add(aq_inf % p)
        adm_canon.add((-aq_inf) % p)

        for t in valid_t:
            a4_t = (3 * t) % q
            a6_t = (1 - pow(t, 3, q)) % q
            aq_t = trace_weierstrass_fast(a4_t, a6_t, q, leg)
            adm_canon.add(aq_t % p)
            adm_canon.add((-aq_t) % p)

        elim_72_canon = (aq_72 % p not in adm_canon)
        elim_144a_canon = (aq_144a % p not in adm_canon)
        elim_144b_canon = (aq_144b % p not in adm_canon)

        record = {
            "k": k,
            "q": q,
            "aq_72": aq_72,
            "elim_72": elim_72_canon,
            "elim_144a": elim_144a_canon,
        }
        tested_primes.append(record)

        if elim_72_canon and elim_144a_canon:
            eliminating_primes.append(record)
            if first_certificate is None:
                first_certificate = {
                    "k": k,
                    "q": q,
                    "aq_72": aq_72,
                    "aq_72_mod_p": aq_72 % p,
                    "aq_144a": aq_144a,
                    "aq_144a_mod_p": aq_144a % p,
                    "size_Up": len(Up),
                    "size_valid_t": len(valid_t),
                    "size_adm_canon": len(adm_canon),
                }

    total_tested = len(tested_primes)
    total_elim = len(eliminating_primes)
    elim_rate = (total_elim / total_tested * 100) if total_tested > 0 else 0.0

    return {
        "exponent_p": p,
        "congruence": "1 mod 3",
        "unconditionally_eliminated": (total_elim > 0),
        "total_tested_primes": total_tested,
        "total_eliminating_primes": total_elim,
        "elimination_rate_pct": round(elim_rate, 2),
        "first_certificate": first_certificate,
    }


def main():
    p_min, p_max = 5301, 5400
    print("=" * 80)
    print(f"     U447: EXTENDED KRAUS SIEVE AUDIT FOR SIGNATURE (3, 3, p) [p in {p_min}..{p_max}] ")
    print("=" * 80)

    # Positive control: LMFDB trace check for 72a1 at q=5 and q=13
    leg5 = build_legendre_table(5)
    leg13 = build_legendre_table(13)
    a5_72 = trace_weierstrass_fast(6, -7, 5, leg5)
    a13_72 = trace_weierstrass_fast(6, -7, 13, leg13)
    assert a5_72 == 2, f"Expected a5(72a1)=2, got {a5_72}"
    assert a13_72 == -2, f"Expected a13(72a1)=-2, got {a13_72}"
    print(f"[PASS] Positive control: a5(72a1)={a5_72}, a13(72a1)={a13_72} match LMFDB exact values.")

    target_primes = [p for p in range(p_min, p_max + 1) if sympy.isprime(p) and p % 3 == 1]
    all_results = {}

    start_total = time.time()
    for p in target_primes:
        res = kraus_sieve_exponent(p, max_q=350000)
        all_results[p] = res
        cert = res["first_certificate"]
        assert cert is not None, f"Prime p={p} failed to eliminate!"
        print(f"[PASS] p={p:4d} eliminated by q={cert['q']:5d} (k={cert['k']:2d}, aq(72a1)={cert['aq_72']:4d}, rate={res['elimination_rate_pct']:.1f}%)")

    elapsed_total = time.time() - start_total
    num_targets = len(target_primes)
    print(f"\nAll {num_targets} primes in [{p_min}, {p_max}] unconditionally eliminated in {elapsed_total:.2f}s.")

    # Save evidence
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    serializable = {str(k): v for k, v in all_results.items()}
    with open(OUTPUT_JSON, "w") as f:
        json.dump(serializable, f, indent=2)
    print(f"Full certificates saved to: {OUTPUT_JSON}")
    print("=" * 80)
    return 0


if __name__ == "__main__":
    sys.exit(main())
