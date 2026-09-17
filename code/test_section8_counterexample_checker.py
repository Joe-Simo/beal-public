"""
Comprehensive Test Suite for Section 8 Beal Counterexample Checker (Python)

Covers all Section 8 requirements:
1. Valid equality that fails the common-factor requirement: 3^3 + 6^3 = 3^5
2. Valid equality excluded because an exponent is 2: 3^5 + 10^2 = 7^3
3. Arithmetic mismatch
4. Zero and negative inputs
5. Noninteger inputs
6. Integers beyond ordinary floating-point safe-integer limits
7. Boundary conditions, input lengths, and calling conventions
"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

# Add code directory to path if needed
CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from section8_counterexample_checker import (
    BealCheckResult,
    check_beal,
    gcd3,
    parse_exact,
)


class TestSection8BealChecker(unittest.TestCase):
    """Exhaustive test suite verifying Section 8 counterexample checker requirements."""

    # 1. Valid equalities failing common-factor requirement (gcd > 1)
    def test_01_nonprimitive_equality_3_3_6_3_3_5(self) -> None:
        """3^3 + 6^3 = 3^5 (27 + 216 = 243, gcd(3, 6, 3) = 3)."""
        res = check_beal([3, 6, 3, 3, 3, 5])
        self.assertTrue(res.admissible)
        self.assertTrue(res.equality)
        self.assertFalse(res.primitive)
        self.assertFalse(res.counterexample)
        self.assertEqual(res.gcd, 3)
        self.assertEqual(res.lhs, 243)
        self.assertEqual(res.rhs, 243)
        self.assertIn("fails common-factor requirement", res.reason)

    def test_01_nonprimitive_equality_7_3_7_4_14_3(self) -> None:
        """7^3 + 7^4 = 14^3 (343 + 2401 = 2744, gcd(7, 7, 14) = 7)."""
        res = check_beal([7, 7, 14, 3, 4, 3])
        self.assertTrue(res.admissible)
        self.assertTrue(res.equality)
        self.assertFalse(res.primitive)
        self.assertFalse(res.counterexample)
        self.assertEqual(res.gcd, 7)
        self.assertEqual(res.lhs, 2744)
        self.assertEqual(res.rhs, 2744)

    def test_01_nonprimitive_equality_2_3_2_3_2_4(self) -> None:
        """2^3 + 2^3 = 2^4 (8 + 8 = 16, gcd(2, 2, 2) = 2)."""
        res = check_beal([2, 2, 2, 3, 3, 4])
        self.assertTrue(res.admissible)
        self.assertTrue(res.equality)
        self.assertFalse(res.primitive)
        self.assertFalse(res.counterexample)
        self.assertEqual(res.gcd, 2)

    # 2. Valid equalities excluded because an exponent is 2 (< 3)
    def test_02_exponent_two_excluded_3_5_10_2_7_3(self) -> None:
        """3^5 + 10^2 = 7^3 (243 + 100 = 343, gcd=1, excluded by y=2)."""
        res = check_beal([3, 10, 7, 5, 2, 3])
        self.assertFalse(res.admissible)
        self.assertTrue(res.equality)
        self.assertTrue(res.primitive)
        self.assertFalse(res.counterexample)
        self.assertEqual(res.lhs, 343)
        self.assertEqual(res.rhs, 343)
        self.assertEqual(res.gcd, 1)
        self.assertIn("y=2", res.reason)

    def test_02_exponent_two_excluded_2_5_7_2_3_4(self) -> None:
        """2^5 + 7^2 = 3^4 (32 + 49 = 81, gcd=1, excluded by y=2)."""
        res = check_beal([2, 7, 3, 5, 2, 4])
        self.assertFalse(res.admissible)
        self.assertTrue(res.equality)
        self.assertTrue(res.primitive)
        self.assertFalse(res.counterexample)
        self.assertIn("y=2", res.reason)

    def test_02_exponent_two_excluded_13_2_7_3_2_9(self) -> None:
        """13^2 + 7^3 = 2^9 (169 + 343 = 512, gcd=1, excluded by x=2)."""
        res = check_beal([13, 7, 2, 2, 3, 9])
        self.assertFalse(res.admissible)
        self.assertTrue(res.equality)
        self.assertTrue(res.primitive)
        self.assertFalse(res.counterexample)
        self.assertIn("x=2", res.reason)

    def test_02_exponent_two_excluded_1_3_2_3_3_2(self) -> None:
        """1^3 + 2^3 = 3^2 (1 + 8 = 9, gcd=1, excluded by z=2)."""
        res = check_beal([1, 2, 3, 3, 3, 2])
        self.assertFalse(res.admissible)
        self.assertTrue(res.equality)
        self.assertTrue(res.primitive)
        self.assertFalse(res.counterexample)
        self.assertIn("z=2", res.reason)

    def test_02_multiple_exponents_two(self) -> None:
        """Excluded when all exponents are 2."""
        res = check_beal([1, 2, 3, 2, 2, 2])
        self.assertFalse(res.admissible)
        self.assertFalse(res.counterexample)
        self.assertIn("x=2", res.reason)
        self.assertIn("y=2", res.reason)
        self.assertIn("z=2", res.reason)

    # 3. Arithmetic mismatches (A^x + B^y != C^z)
    def test_03_arithmetic_mismatch_2_3_4_3_3_3(self) -> None:
        """2^3 + 3^3 != 4^3 (8 + 27 = 35 != 64)."""
        res = check_beal([2, 3, 4, 3, 3, 3])
        self.assertTrue(res.admissible)
        self.assertFalse(res.equality)
        self.assertTrue(res.primitive)
        self.assertFalse(res.counterexample)
        self.assertEqual(res.lhs, 35)
        self.assertEqual(res.rhs, 64)
        self.assertIn("Arithmetic mismatch", res.reason)

    def test_03_arithmetic_mismatch_3_4_5_3_3_3(self) -> None:
        """3^3 + 4^3 != 5^3 (27 + 64 = 91 != 125)."""
        res = check_beal([3, 4, 5, 3, 3, 3])
        self.assertTrue(res.admissible)
        self.assertFalse(res.equality)
        self.assertTrue(res.primitive)
        self.assertFalse(res.counterexample)
        self.assertEqual(res.lhs, 91)
        self.assertEqual(res.rhs, 125)

    def test_03_arithmetic_mismatch_5_6_7_3_3_3(self) -> None:
        """5^3 + 6^3 != 7^3 (125 + 216 = 341 != 343)."""
        res = check_beal([5, 6, 7, 3, 3, 3])
        self.assertTrue(res.admissible)
        self.assertFalse(res.equality)
        self.assertTrue(res.primitive)
        self.assertFalse(res.counterexample)

    # 4. Zero and negative inputs
    def test_04_zero_and_negative_inputs(self) -> None:
        """Verify zero and negative inputs for all 6 positions."""
        bad_values = [0, -1, -50]
        for bad in bad_values:
            # Base A
            rA = check_beal([bad, 3, 4, 3, 3, 3])
            self.assertFalse(rA.admissible)
            self.assertIn(f"A={bad}", rA.reason)
            # Base B
            rB = check_beal([3, bad, 4, 3, 3, 3])
            self.assertFalse(rB.admissible)
            self.assertIn(f"B={bad}", rB.reason)
            # Base C
            rC = check_beal([3, 4, bad, 3, 3, 3])
            self.assertFalse(rC.admissible)
            self.assertIn(f"C={bad}", rC.reason)
            # Exponent x
            rx = check_beal([3, 4, 5, bad, 3, 3])
            self.assertFalse(rx.admissible)
            self.assertIn(f"x={bad}", rx.reason)
            # Exponent y
            ry = check_beal([3, 4, 5, 3, bad, 3])
            self.assertFalse(ry.admissible)
            self.assertIn(f"y={bad}", ry.reason)
            # Exponent z
            rz = check_beal([3, 4, 5, 3, 3, bad])
            self.assertFalse(rz.admissible)
            self.assertIn(f"z={bad}", rz.reason)

    def test_04_all_zeros_and_all_negatives(self) -> None:
        """All zeros and all negative inputs rejected."""
        self.assertFalse(check_beal([0, 0, 0, 0, 0, 0]).admissible)
        self.assertFalse(check_beal([-1, -2, -3, -3, -3, -3]).admissible)

    # 5. Noninteger inputs
    def test_05_noninteger_inputs(self) -> None:
        """Verify non-integer inputs: floats, booleans, None, strings, structures."""
        bads = [
            1.5,
            1.0,  # float 1.0 rejected due to floating-point precision policy
            "1.2",
            "-0.5",
            True,   # bool is int subclass in python; must be rejected
            False,
            None,
            float("nan"),
            float("inf"),
            float("-inf"),
            [1, 2],
            {"val": 1},
            "abc",
            "",
            "   ",
            "1e5",
        ]
        for bad in bads:
            res = check_beal([bad, 3, 4, 3, 3, 3])
            self.assertFalse(res.admissible, f"Noninteger {bad!r} should be rejected")
            self.assertFalse(res.counterexample)
            self.assertIn("Noninteger", res.reason)

    # 6. Integers beyond ordinary floating-point safe-integer limits
    def test_06_beyond_safe_integer_exact_computation(self) -> None:
        """Exact integer equality: (2^60)^3 + (2^60)^3 = 2^181."""
        # 2^60 = 1152921504606846976 >> 2^53 (9007199254740992)
        res = check_beal([2**60, 2**60, 2, 3, 3, 181])
        self.assertTrue(res.admissible)
        self.assertTrue(res.equality)
        self.assertFalse(res.primitive)
        self.assertFalse(res.counterexample)
        self.assertEqual(res.gcd, 2)
        self.assertEqual(res.lhs, 2**181)
        self.assertEqual(res.rhs, 2**181)

    def test_06_massive_powers(self) -> None:
        """Massive power of 2: (2^100)^3 + (2^100)^3 = 2^301."""
        res = check_beal([2**100, 2**100, 2, 3, 3, 301])
        self.assertTrue(res.admissible)
        self.assertTrue(res.equality)
        self.assertFalse(res.primitive)
        self.assertFalse(res.counterexample)
        self.assertEqual(res.gcd, 2)

    def test_06_decimal_string_beyond_safe_integer(self) -> None:
        """String with 2^53 + 1 correctly parsed without precision loss."""
        val = parse_exact("9007199254740993")
        self.assertEqual(val, 9007199254740993)

    def test_06_large_integer_mismatch(self) -> None:
        """Large integer mismatch beyond safe integer limit."""
        res = check_beal([2**60, 2**60, 3, 3, 3, 181])
        self.assertTrue(res.admissible)
        self.assertFalse(res.equality)
        self.assertFalse(res.counterexample)

    # 7. Boundary conditions, GCD correctness, and calling conventions
    def test_07_base_one_retained(self) -> None:
        """Base 1 is a valid positive integer and retained as admissible."""
        res = check_beal([1, 2, 3, 3, 3, 3])
        self.assertTrue(res.admissible)
        self.assertFalse(res.equality)  # 1 + 8 != 27
        self.assertTrue(res.primitive)
        self.assertFalse(res.counterexample)

    def test_07_input_size_validation(self) -> None:
        """Check rejection of incorrect input lengths (0, 5, 7 inputs)."""
        self.assertFalse(check_beal([]).admissible)
        self.assertFalse(check_beal([1, 2, 3, 4, 5]).admissible)
        self.assertFalse(check_beal([1, 2, 3, 4, 5, 6, 7]).admissible)

    def test_07_calling_conventions(self) -> None:
        """Verify calling with 6 positional arguments and dict."""
        # Positional arguments
        pos = check_beal(3, 6, 3, 3, 3, 5)
        self.assertTrue(pos.admissible)
        self.assertTrue(pos.equality)
        self.assertFalse(pos.primitive)

        # Dict with uppercase keys
        d_upper = check_beal({"A": 3, "B": 6, "C": 3, "x": 3, "y": 3, "z": 5})
        self.assertTrue(d_upper.admissible)
        self.assertTrue(d_upper.equality)

        # Dict with lowercase keys
        d_lower = check_beal({"a": 3, "b": 6, "c": 3, "x": 3, "y": 3, "z": 5})
        self.assertTrue(d_lower.admissible)
        self.assertTrue(d_lower.equality)

    def test_07_gcd_correctness(self) -> None:
        """Verify GCD implementation on arbitrary integers."""
        self.assertEqual(gcd3(12, 18, 24), 6)
        self.assertEqual(gcd3(7, 11, 13), 1)
        self.assertEqual(gcd3(27, 216, 243), 27)

    def test_07_hypothetical_counterexample_logic(self) -> None:
        """Verify that counterexample is True iff admissible, equality, and primitive hold."""
        # Mismatch with gcd=1
        mismatch = check_beal([2, 3, 4, 3, 3, 3])
        self.assertTrue(mismatch.primitive)
        self.assertTrue(mismatch.admissible)
        self.assertFalse(mismatch.counterexample)


if __name__ == "__main__":
    unittest.main(verbosity=2)
