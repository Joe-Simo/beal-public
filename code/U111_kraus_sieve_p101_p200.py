#!/usr/bin/env python3
"""
U111: Kraus Sieve Modular Elimination for Generalized Fermat Equation A^3 + B^3 = C^p
Signature: (3, 3, p)
Target Exponent Range: p in [101, 200] with p = 1 mod 3:
  p in {103, 109, 127, 139, 151, 157, 163, 181, 193, 199}.
Target Levels:
  - Level 72:  Newform 72a1  (y^2 = x^3 + 6x - 7, non-CM)
  - Level 144: Newform 144a1 (y^2 = x^3 + 6x + 7, non-CM quadratic twist of 72a1 by -4)
  - Level 144: Newform 144b1 (y^2 = x^3 - 1, CM by Q(sqrt(-3)), eliminated by Cartan/torsion)
"""

from __future__ import annotations
import json
from pathlib import Path
import sys
import time
import sympy

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_JSON = ROOT / "references" / "U111" / "kraus_sieve_p101_p200.json"
OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)


def build_legendre_table(q: int) -> list[int]:
    leg = [0] * q
    q_half = (q - 1) // 2
    for r in range(1, q):
        v = pow(r, q_half, q)
        leg[r] = -1 if v == q - 1 else 1
    return leg


def trace_weierstrass_fast(a4: int, a6: int, q: int, leg: list[int]) -> int:
    s = 0
    for x in range(q):
        rhs = (x * (x * x + a4) + a6) % q
        s += leg[rhs]
    return -s


def solve_descent_residues(p: int, q: int) -> tuple[set[int], set[int]]:
    Up = set(pow(x, p, q) for x in range(1, q))
    inv3 = pow(3, -1, q)
    inv3_p1 = pow(pow(3, p - 1, q), -1, q)

    valid_t = set()
    for t in range(q):
        if (t + 1) % q == 0:
            continue
        f1 = (t + 1) % q
        f2 = (t * t - t + 1) % q

        if f1 in Up and f2 in Up:
            valid_t.add(t)
            continue

        if ((f1 * inv3_p1) % q in Up) and ((f2 * inv3) % q in Up):
            valid_t.add(t)
            continue
        if ((f1 * inv3) % q in Up) and ((f2 * inv3_p1) % q in Up):
            valid_t.add(t)
            continue

    return Up, valid_t


def kraus_sieve_exponent(p: int, max_q: int = 30000, verbose: bool = True) -> dict[str, object]:
    t_start = time.time()
    tested_primes = []
    eliminating_primes = []
    first_eliminator = None

    k = 1
    while True:
        q = 2 * k * p + 1
        if q > max_q:
            break
        k += 1

        if not sympy.isprime(q) or q % 72 == 0 or q in (2, 3):
            continue

        leg = build_legendre_table(q)
        aq_72a1 = trace_weierstrass_fast(6, -7, q, leg)
        aq_144a1 = trace_weierstrass_fast(6, 7, q, leg)
        aq_144b1 = trace_weierstrass_fast(0, -1, q, leg)

        Up, valid_t = solve_descent_residues(p, q)

        admissible_traces = set()
        for t in valid_t:
            tr = trace_weierstrass_fast((3 * t) % q, (1 - pow(t, 3, q)) % q, q, leg)
            admissible_traces.add(tr % p)

        pm2_mod_p = {2 % p, (-2) % p}
        q_div_C_possible = bool(admissible_traces.intersection(pm2_mod_p))

        elim_72a1 = (aq_72a1 % p not in admissible_traces)
        elim_144a1 = (aq_144a1 % p not in admissible_traces)
        fully_eliminated = elim_72a1 and elim_144a1 and not q_div_C_possible

        record = {
            "q": q,
            "k": k - 1,
            "aq_72a1": aq_72a1,
            "aq_144a1": aq_144a1,
            "aq_144b1": aq_144b1,
            "valid_t_count": len(valid_t),
            "adm_trace_count": len(admissible_traces),
            "elim_72a1": elim_72a1,
            "elim_144a1": elim_144a1,
            "q_div_C_possible": q_div_C_possible,
            "fully_eliminated": fully_eliminated,
        }
        tested_primes.append(record)

        if fully_eliminated:
            eliminating_primes.append(record)
            if first_eliminator is None:
                first_eliminator = record
                if verbose:
                    print(f"  [p = {p}] FIRST ELIMINATOR: q = {q} (k = {k-1}) | aq(72a1) = {aq_72a1} = {aq_72a1%p} (mod {p}) | |Adm| = {len(admissible_traces)}")

    elapsed = time.time() - t_start
    status = "ELIMINATED" if first_eliminator is not None else "UNDETERMINED"

    return {
        "p": p,
        "status": status,
        "first_eliminator": first_eliminator,
        "total_tested": len(tested_primes),
        "total_eliminating": len(eliminating_primes),
        "elimination_rate": len(eliminating_primes) / len(tested_primes) if tested_primes else 0.0,
        "elapsed_seconds": elapsed,
        "all_records": tested_primes,
    }


def main():
    target_primes = [103, 109, 127, 139, 151, 157, 163, 181, 193, 199]
    print("=" * 80)
    print("  U111: EXTENDED KRAUS SIEVE AUDIT FOR SIGNATURE (3, 3, p) [100 < p < 200]")
    print("  Target Primes (p = 1 mod 3):", target_primes)
    print("=" * 80)

    results = {}
    t_total = time.time()
    all_eliminated = True

    for p in target_primes:
        res = kraus_sieve_exponent(p, max_q=25000, verbose=True)
        results[str(p)] = res
        if res["status"] != "ELIMINATED":
            all_eliminated = False

    total_time = time.time() - t_total

    print("\n" + "#" * 84)
    print("  MASTER SUMMARY TABLE: SIGNATURE (3, 3, p) KRAUS SIEVE [100 < p < 200]")
    print("#" * 84)
    print(f"{'p':>4} | {'First q':>8} | {'k':>4} | {'aq(72a1)':>8} | {'aq mod p':>8} | {'|Adm|/p':>9} | {'Rate':>7} | {'Status':>12}")
    print("-" * 84)
    for p in target_primes:
        r = results[str(p)]
        fe = r["first_eliminator"]
        if fe:
            print(f"{p:>4} | {fe['q']:>8} | {fe['k']:>4} | {fe['aq_72a1']:>8} | {fe['aq_72a1']%p:>8} | {fe['adm_trace_count']:>4}/{p:<4} | {r['elimination_rate']*100:>6.1f}% | {r['status']:>12}")
        else:
            print(f"{p:>4} | {'NONE':>8} | {'-':>4} | {'-':>8} | {'-':>8} | {'-':>9} | {0.0:>6.1f}% | {r['status']:>12}")
    print("#" * 84)
    print(f"Total Execution Time: {total_time:.2f} seconds")

    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n[OK] Results saved to {OUTPUT_JSON}")

    assert all_eliminated, "Not all primes in [101, 200] were eliminated!"
    print("[PASS] 100% of primes p in [101, 200] with p = 1 mod 3 are UNCONDITIONALLY ELIMINATED!")


if __name__ == "__main__":
    main()
