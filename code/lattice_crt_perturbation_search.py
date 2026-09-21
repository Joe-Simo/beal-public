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
    """Exact integer exp-th root using integer bisection / Newton's method."""
    if val <= 0 or exp < 1:
        return None
    if exp == 1:
        return val
    # Initial floating point guess if within double range, else bit length
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

def search_fc_perturbations(radius: int = 500, max_exp_scan: int = 15) -> dict:
    """
    Search around Fermat-Catalan seeds by:
    1. Perturbing bases A' = A + delta_A, B' = B + delta_B.
    2. Elevating exponent 2 to exponents >= 3.
    3. Testing modular CRT shifts.
    """
    print("=================================================================")
    print("Lattice & CRT Near-Miss Perturbation Search")
    print(f"Fermat-Catalan Seeds: {len(FERMAT_CATALAN_SEEDS)}")
    print(f"Base Perturbation Radius: [-{radius}, +{radius}]")
    print(f"Exponent Search Range: [3, {max_exp_scan}]")
    print("=================================================================")

    t0 = time.time()
    pairs_tested = 0
    non_primitive_count = 0

    for s_idx, (A0, B0, C0, x0, y0, z0) in enumerate(FERMAT_CATALAN_SEEDS):
        # We enforce all exponents >= 3
        x_min = max(3, x0 if x0 > 2 else 3)
        y_min = max(3, y0 if y0 > 2 else 3)

        # Scale radius based on base size
        eff_radius = min(radius, max(50, A0 // 2, B0 // 2))

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
                        pairs_tested += 1

                        # Quick modular filters for val = C^z:
                        # For z >= 3, val must be a cubic residue mod 7 (residues {0, 1, 6})
                        m7 = val % 7
                        # For z in [3, max_exp_scan]
                        for z in range(3, max_exp_scan + 1):
                            # Sieve mod 7
                            if z % 3 == 0 and m7 not in (0, 1, 6):
                                continue
                            # Sieve mod 9
                            if z % 3 == 0 and (val % 9) not in (0, 1, 8):
                                continue

                            C = exact_root(val, z)
                            if C is not None and C >= 2:
                                g = gcd3(A, B, C)
                                if g == 1:
                                    verify_and_claim_counterexample(A, x, B, y, C, z)
                                else:
                                    non_primitive_count += 1

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
