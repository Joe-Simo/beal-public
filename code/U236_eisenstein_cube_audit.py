#!/usr/bin/env python3
"""U236 / Milestone 76: Eisenstein Cube Integrality and Norm Verification.

Replicates the Lean 4 theorems:
- odd_cube_real_div_eight
- odd_cube_imag_div_eight
- eisenstein_cube_coords_integral

For any beta = (A + B*sqrt(-3))/2 in Z[omega] with A, B odd:
beta^3 = (X + Y*sqrt(-3)) in Z[sqrt(-3)] where
X = A*(A^2 - 9*B^2)/8, Y = 3*B*(A^2 - B^2)/8.
Verifies exact integer divisibility by 8 and Norm(beta^3) == Norm(beta)^3.
"""
from __future__ import annotations
import math
import sys
import time

def verify_controls() -> None:
    # Control 1: A=1, B=1 -> beta = (1+sqrt(-3))/2 = -omega^2, beta^3 = -1
    A1, B1 = 1, 1
    X1 = A1 * (A1**2 - 9 * B1**2)
    Y1 = 3 * B1 * (A1**2 - B1**2)
    assert X1 % 8 == 0 and Y1 % 8 == 0
    assert X1 // 8 == -1 and Y1 // 8 == 0

    # Control 2: A=-1, B=1 -> beta = (-1+sqrt(-3))/2 = omega, beta^3 = 1
    A2, B2 = -1, 1
    X2 = A2 * (A2**2 - 9 * B2**2)
    Y2 = 3 * B2 * (A2**2 - B2**2)
    assert X2 % 8 == 0 and Y2 % 8 == 0
    assert X2 // 8 == 1 and Y2 // 8 == 0

    # Control 3: A=1, B=3 -> beta = (1+3*sqrt(-3))/2, Norm = 7, beta^3 Norm = 343
    A3, B3 = 1, 3
    X3 = A3 * (A3**2 - 9 * B3**2)
    Y3 = 3 * B3 * (A3**2 - B3**2)
    assert X3 % 8 == 0 and Y3 % 8 == 0
    x3, y3 = X3 // 8, Y3 // 8
    assert x3 == -10 and y3 == -9
    norm_beta = (A3**2 + 3 * B3**2) // 4
    norm_cube = x3**2 + 3 * y3**2
    assert norm_cube == norm_beta**3 == 343

def run_audit(max_coord: int = 500) -> int:
    pairs_tested = 0
    for a in range(-max_coord, max_coord + 1):
        A = 2 * a + 1
        A2 = A * A
        for b in range(-max_coord, max_coord + 1):
            B = 2 * b + 1
            B2 = B * B
            pairs_tested += 1

            real_num = A * (A2 - 9 * B2)
            imag_num = 3 * B * (A2 - B2)

            assert real_num % 8 == 0, f"Real part not divisible by 8 for A={A}, B={B}"
            assert imag_num % 8 == 0, f"Imag part not divisible by 8 for A={A}, B={B}"

            X = real_num // 8
            Y = imag_num // 8

            # Exact norm check
            # Norm(beta) = (A^2 + 3B^2)/4
            # Norm(beta^3) = X^2 + 3Y^2
            norm_beta4 = A2 + 3 * B2
            assert norm_beta4 % 4 == 0
            norm_beta = norm_beta4 // 4
            norm_cube = X * X + 3 * Y * Y
            assert norm_cube == norm_beta ** 3, f"Norm identity failure for A={A}, B={B}"

    return pairs_tested

def main() -> int:
    t0 = time.perf_counter()
    print("=== Milestone 76: Eisenstein Cube Integrality and Norm Verification ===")
    print("Testing positive controls...")
    verify_controls()
    print("  [PASS] Control 1: (1, 1) -> beta = -omega^2, beta^3 = -1 (X=-1, Y=0)")
    print("  [PASS] Control 2: (-1, 1) -> beta = omega, beta^3 = 1 (X=1, Y=0)")
    print("  [PASS] Control 3: (1, 3) -> Norm = 7, Norm(beta^3) = 343 = 7^3")

    max_coord = 250  # 501 * 501 = 251,001 pairs
    print(f"Auditing all { (2*max_coord+1)**2:,} odd coordinate pairs with |A|, |B| <= {2*max_coord+1}...")
    tested = run_audit(max_coord)
    elapsed = time.perf_counter() - t0

    print(f"  Odd pairs verified: {tested:,}")
    print(f"  Divisibility by 8: 100% verified (0 exceptions)")
    print(f"  Norm(beta^3) == Norm(beta)^3: 100% verified (0 exceptions)")
    print(f"  Elapsed time: {elapsed:.2f}s")
    print("ALL TESTS PASSED: Eisenstein cube integrality verified consistent with Lean Beal.Euler.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
