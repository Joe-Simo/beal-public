"""
Lattice & CRT Near-Miss Perturbation Search Engine
Target: Search near known Fermat-Catalan solutions, modular points, and CRT lattices
for primitive Beal counterexamples:
    A^x + B^y = C^z with A, B, C > 0, x, y, z >= 3, gcd(A, B, C) == 1.

Triple-Check Validation:
Any potential match is independently verified with:
1. code/check_counterexample_gmp
2. code/beal_counterexample_checker.py
3. PARI/GP exact arithmetic
"""

import sys
import os
import math
import json
import time
import subprocess

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

# The 10 known primitive Fermat-Catalan integer solutions
# Format: (A, B, C, x, y, z) with exactly one exponent equal to 2
FERMAT_CATALAN_SEEDS = [
    (1, 2, 3, 7, 3, 2),
    (2, 7, 3, 5, 2, 4),
    (7, 13, 2, 3, 2, 9),
    (2, 17, 71, 7, 3, 2),
    (3, 11, 122, 5, 4, 2),
    (17, 76271, 21063928, 7, 3, 2),
    (1414, 2213459, 65, 3, 2, 7),
    (9262, 15312283, 113, 3, 2, 7),
    (43, 96222, 30042907, 8, 3, 2),
    (33, 1549034, 15613, 8, 2, 3),
]

def gcd3(a: int, b: int, c: int) -> int:
    return math.gcd(a, math.gcd(b, c))

def exact_root(val: int, exp: int) -> int | None:
    """Exact integer exp-th root with fast hardware float screening."""
    if val <= 0 or exp < 1:
        return None
    if exp == 1:
        return val
    if exp == 2:
        r = math.isqrt(val)
        return r if r * r == val else None
    try:
        if val.bit_length() <= 1020:
            approx = int(round(val ** (1.0 / exp)))
        else:
            log2_v = math.log2(val)
            approx = int(round(2.0 ** (log2_v / exp)))
        if approx > 0 and approx ** exp == val:
            return approx
        for r in (approx - 1, approx + 1):
            if r > 0 and r ** exp == val:
                return r
        return None
    except Exception:
        pass

    # Fallback integer Newton method
    bit_len = val.bit_length()
    guess_bits = (bit_len + exp - 1) // exp
    x = 1 << guess_bits
    while True:
        x_prev = x
        x = ((exp - 1) * x + val // (x ** (exp - 1))) // exp
        if x >= x_prev:
            break
    for r in (x - 1, x, x + 1):
        if r > 0 and r ** exp == val:
            return r
    return None

def verify_and_claim_counterexample(A: int, x: int, B: int, y: int, C: int, z: int) -> bool:
    """Mandatory triple-check independent verification."""
    print(f"\n*****************************************************************")
    print(f"POTENTIAL COUNTEREXAMPLE DETECTED: {A}^{x} + {B}^{y} == {C}^{z}")
    print(f"Executing Independent Triple-Check Verification Suite...")
    print(f"*****************************************************************")

    # 1. C/GMP checker
    cmd1 = f"./code/check_counterexample_gmp {A} {x} {B} {y} {C} {z}"
    res1 = subprocess.run(cmd1, shell=True, capture_output=True, text=True)
    print(f"1. C/GMP return code: {res1.returncode}")

    # 2. Python checker
    cmd2 = f"PYTHONPATH=code python3 code/beal_counterexample_checker.py {A} {x} {B} {y} {C} {z}"
    res2 = subprocess.run(cmd2, shell=True, capture_output=True, text=True)
    print(f"2. Python checker return code: {res2.returncode}")

    # 3. PARI/GP checker
    cmd3 = f"echo 'if(gcd(gcd({A}, {B}), {C}) == 1 && {A}^{x} + {B}^{y} == {C}^{z}, quit(0), quit(1))' | gp -q"
    res3 = subprocess.run(cmd3, shell=True, capture_output=True, text=True)
    print(f"3. PARI/GP return code: {res3.returncode}")

    if res1.returncode == 0 and res2.returncode == 0 and res3.returncode == 0:
        found_data = {
            "status": "COUNTEREXAMPLE_DISCOVERED",
            "claim": "Primitive counterexample to Beal conjecture verified by C/GMP, Python, and PARI/GP",
            "A": str(A), "x": x,
            "B": str(B), "y": y,
            "C": str(C), "z": z,
            "primitive": True,
            "verified_by": ["check_counterexample_gmp.c", "beal_counterexample_checker.py", "pari_gp"],
            "timestamp": int(time.time()),
        }
        with open("COUNTEREXAMPLE_FOUND.json", "w") as fp:
            json.dump(found_data, fp, indent=2)
        with open("PRIZE_CLAIM_COUNTEREXAMPLE.json", "w") as fp:
            json.dump(found_data, fp, indent=2)
        print("\n=================================================================")
        print("VICTORY CONDITION A ACHIEVED: COUNTEREXAMPLE DISCOVERED AND CERTIFIED!")
        print("Wrote COUNTEREXAMPLE_FOUND.json and PRIZE_CLAIM_COUNTEREXAMPLE.json")
        print("=================================================================\n")
        sys.exit(0)
    else:
        print(">>> Candidate failed triple-check independent verification. Continuing search...")
        return False

def _process_seed(args):
    s_idx, (A0, B0, C0, x0, y0, z0), radius, max_exp_scan = args
    res_mod7 = {z: {pow(i, z, 7) for i in range(7)} for z in range(3, max_exp_scan + 1)}
    res_mod9 = {z: {pow(i, z, 9) for i in range(9)} for z in range(3, max_exp_scan + 1)}
    res_mod13 = {z: {pow(i, z, 13) for i in range(13)} for z in range(3, max_exp_scan + 1)}

    x_min = max(3, x0 if x0 > 2 else 3)
    y_min = max(3, y0 if y0 > 2 else 3)
    eff_radius = min(radius, 600)

    pairs = 0
    non_prim = 0

    for da in range(-eff_radius, eff_radius + 1):
        A = A0 + da
        if A < 2:
            continue
        for db in range(-eff_radius, eff_radius + 1):
            B = B0 + db
            if B < 2:
                continue
            for x in range(3, min(max_exp_scan + 1, x_min + 3)):
                Ax = A ** x
                for y in range(3, min(max_exp_scan + 1, y_min + 3)):
                    By = B ** y
                    val = Ax + By
                    pairs += 1

                    m7 = val % 7
                    m9 = val % 9
                    m13 = val % 13

                    for z in range(3, max_exp_scan + 1):
                        if m7 not in res_mod7[z]:
                            continue
                        if m9 not in res_mod9[z]:
                            continue
                        if m13 not in res_mod13[z]:
                            continue

                        C = exact_root(val, z)
                        if C is not None and C >= 2:
                            g = gcd3(A, B, C)
                            if g == 1:
                                verify_and_claim_counterexample(A, x, B, y, C, z)
                            else:
                                non_prim += 1
    return pairs, non_prim

def search_fc_perturbations(radius: int = 500, max_exp_scan: int = 15) -> dict:
    """
    Search around Fermat-Catalan seeds using 8 parallel worker processes.
    """
    print("=================================================================")
    print("Lattice & CRT Near-Miss Perturbation Search (Parallel 8-Worker)")
    print(f"Fermat-Catalan Seeds: {len(FERMAT_CATALAN_SEEDS)}")
    print(f"Base Perturbation Radius: [-{radius}, +{radius}]")
    print(f"Exponent Search Range: [3, {max_exp_scan}]")
    print("=================================================================")

    t0 = time.time()
    pairs_tested = 0
    non_primitive_count = 0

    import concurrent.futures
    tasks = [(s_idx, seed, radius, max_exp_scan) for s_idx, seed in enumerate(FERMAT_CATALAN_SEEDS)]
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        for p, np in executor.map(_process_seed, tasks):
            pairs_tested += p
            non_primitive_count += np

    elapsed = time.time() - t0
    rate = pairs_tested / elapsed if elapsed > 0 else 0
    print("-----------------------------------------------------------------")
    print(f"Lattice/CRT Perturbation Scan Completed: {pairs_tested:,} pairs tested in {elapsed:.2f}s ({rate:,.0f} pairs/sec)")
    print(f"Non-primitive equalities detected: {non_primitive_count}")
    print(f"Primitive counterexamples found: 0")
    print("-----------------------------------------------------------------")

    return {
        "status": "completed",
        "perturbation_radius": radius,
        "max_exp_scan": max_exp_scan,
        "pairs_tested": pairs_tested,
        "non_primitive_count": non_primitive_count,
        "elapsed_seconds": round(elapsed, 4),
        "counterexample_found": False
    }

if __name__ == "__main__":
    radius = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    max_exp = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    search_fc_perturbations(radius, max_exp)
