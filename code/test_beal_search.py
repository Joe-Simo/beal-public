"""
Comprehensive Test Suite for Beal Conjecture Search Tool & Section 8 Integration

Tests:
1. Strict Section 8 validation rules on near-misses and boundary cases.
2. Rejection of exponent-2 instances (13^2 + 7^3 = 2^9, 3^5 + 10^2 = 7^3, 1^3 + 2^3 = 3^2, 2^5 + 7^2 = 3^4).
3. Proper handling of non-coprime equalities (3^3 + 6^3 = 3^5, 7^3 + 7^4 = 14^3, 2^3 + 2^3 = 2^4).
4. Rejection of arithmetic near-misses (Simpsons 3987^12 + 4365^12 != 4472^12, 1782^12 + 1841^12 != 1922^12).
5. Positivity and domain violations (0, negative bases/exponents, floats, malformed input).
6. Consistency between Python multiprocessing engine and native C + GMP engine.
7. Verification of search bounds and execution on sub-ranges.
"""

from __future__ import annotations

import math
import subprocess
import sys
import unittest
from pathlib import Path

# Add code directory to path
CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from section8_counterexample_checker import BealCheckResult, check_beal, gcd3
from beal_search import (
    is_prime_or_four,
    search_gmp,
    search_python,
    test_near_misses_and_edge_cases,
)


class TestBealSearchAndSection8(unittest.TestCase):
    """Test suite ensuring complete compliance with Section 8 and search verification."""

    # -------------------------------------------------------------
    # 1. Section 8 Exponent Restriction Tests (< 3 rejected)
    # -------------------------------------------------------------
    def test_exponent_two_near_misses(self) -> None:
        """Known relations with an exponent of 2 must be strictly rejected as counterexamples."""
        cases = [
            (13, 7, 2, 2, 3, 9, "13^2 + 7^3 = 2^9"),
            (3, 10, 7, 5, 2, 3, "3^5 + 10^2 = 7^3"),
            (1, 2, 3, 3, 3, 2, "1^3 + 2^3 = 3^2"),
            (2, 7, 3, 5, 2, 4, "2^5 + 7^2 = 3^4"),
            (17, 2, 71, 3, 7, 2, "17^3 + 2^7 = 71^2"),
        ]
        for A, B, C, x, y, z, desc in cases:
            res = check_beal(A, B, C, x, y, z)
            self.assertFalse(res.admissible, f"{desc} should be non-admissible due to exponent < 3")
            self.assertTrue(res.equality, f"{desc} equality should hold")
            self.assertTrue(res.primitive, f"{desc} bases are coprime")
            self.assertFalse(res.counterexample, f"{desc} must NOT be considered a counterexample")
            self.assertIn("Exponent restriction violated", res.reason)

    # -------------------------------------------------------------
    # 2. Section 8 Coprimality Tests (gcd > 1 rejected as counterexamples)
    # -------------------------------------------------------------
    def test_non_coprime_beal_equalities(self) -> None:
        """Known valid Beal equalities with common factors must not be counterexamples."""
        cases = [
            (3, 6, 3, 3, 3, 5, 3, "3^3 + 6^3 = 3^5"),
            (7, 7, 14, 3, 4, 3, 7, "7^3 + 7^4 = 14^3"),
            (2, 2, 2, 3, 3, 4, 2, "2^3 + 2^3 = 2^4"),
            (2, 2, 2, 10, 10, 11, 2, "2^10 + 2^10 = 2^11"),
            (8, 8, 4, 3, 3, 5, 4, "8^3 + 8^3 = 4^5 (512+512=1024)"),
        ]
        for A, B, C, x, y, z, exp_gcd, desc in cases:
            res = check_beal(A, B, C, x, y, z)
            self.assertTrue(res.admissible, f"{desc} satisfies domain conditions")
            self.assertTrue(res.equality, f"{desc} exact equality holds")
            self.assertFalse(res.primitive, f"{desc} is not primitive")
            self.assertEqual(res.gcd, exp_gcd, f"{desc} gcd should be {exp_gcd}")
            self.assertFalse(res.counterexample, f"{desc} is NOT a counterexample (satisfies Beal)")
            self.assertIn("fails common-factor requirement", res.reason)

    # -------------------------------------------------------------
    # 3. Arithmetic Mismatch Tests (Near-Misses and Non-Equalities)
    # -------------------------------------------------------------
    def test_simpsons_and_arithmetic_mismatches(self) -> None:
        """Arbitrary precision integers must reject false-positive near misses."""
        cases = [
            (3987, 4365, 4472, 12, 12, 12, "Simpsons 1 (3987^12 + 4365^12 != 4472^12)"),
            (1782, 1841, 1922, 12, 12, 12, "Simpsons 2 (1782^12 + 1841^12 != 1922^12)"),
            (2, 3, 4, 3, 3, 3, "2^3 + 3^3 != 4^3"),
            (3, 4, 5, 3, 3, 3, "3^3 + 4^3 != 5^3"),
            (5, 6, 7, 3, 3, 3, "5^3 + 6^3 != 7^3"),
        ]
        for A, B, C, x, y, z, desc in cases:
            res = check_beal(A, B, C, x, y, z)
            self.assertTrue(res.admissible, f"{desc} is admissible domain")
            self.assertFalse(res.equality, f"{desc} must fail exact equality")
            self.assertFalse(res.counterexample, f"{desc} cannot be a counterexample")
            self.assertIn("Arithmetic mismatch", res.reason)

    # -------------------------------------------------------------
    # 4. Positivity, Boundary, and Type Validation
    # -------------------------------------------------------------
    def test_domain_positivity_and_types(self) -> None:
        """Bases and exponents must be positive integers > 0; non-integers rejected."""
        # Zero and negative
        self.assertFalse(check_beal(0, 3, 4, 3, 3, 3).admissible)
        self.assertFalse(check_beal(3, -2, 4, 3, 3, 3).admissible)
        self.assertFalse(check_beal(3, 3, 4, 3, 3, 0).admissible)
        self.assertFalse(check_beal(3, 3, 4, -5, 3, 3).admissible)

        # Floats and invalid types
        self.assertFalse(check_beal(1.0, 2, 3, 3, 3, 3).admissible)
        self.assertFalse(check_beal(True, 2, 3, 3, 3, 3).admissible)
        self.assertFalse(check_beal("1.5", 2, 3, 3, 3, 3).admissible)
        self.assertFalse(check_beal("abc", 2, 3, 3, 3, 3).admissible)

    # -------------------------------------------------------------
    # 5. Helper Logic & Mathematical Reduction Tests
    # -------------------------------------------------------------
    def test_is_prime_or_four(self) -> None:
        """Canonical exponent reduction targets 4 and all odd primes."""
        self.assertTrue(is_prime_or_four(3))
        self.assertTrue(is_prime_or_four(4))
        self.assertTrue(is_prime_or_four(5))
        self.assertTrue(is_prime_or_four(7))
        self.assertTrue(is_prime_or_four(11))
        self.assertTrue(is_prime_or_four(13))
        self.assertTrue(is_prime_or_four(17))

        self.assertFalse(is_prime_or_four(2))
        self.assertFalse(is_prime_or_four(6))
        self.assertFalse(is_prime_or_four(8))
        self.assertFalse(is_prime_or_four(9))
        self.assertFalse(is_prime_or_four(10))
        self.assertFalse(is_prime_or_four(12))

    # -------------------------------------------------------------
    # 6. Python Search Engine Verification
    # -------------------------------------------------------------
    def test_python_search_engine_no_counterexamples(self) -> None:
        """Python search engine confirms no counterexamples exist up to base 200."""
        res = search_python(
            min_base=2,
            max_base=200,
            min_exp=3,
            max_exp=8,
            threads=4,
            prime_exponents_only=False,
            allow_non_coprime=False,
        )
        self.assertEqual(res.counterexample_count(), 0) if hasattr(res, 'counterexample_count') else self.assertEqual(res.counterexamples_found, 0)
        self.assertTrue(res.conjecture_verified)
        self.assertGreater(res.pairs_checked, 0)

    def test_python_search_engine_detects_non_coprime_equality(self) -> None:
        """When allow_non_coprime is enabled, 3^3 + 6^3 = 3^5 is detected and correctly categorized."""
        res = search_python(
            min_base=2,
            max_base=10,
            min_exp=3,
            max_exp=6,
            threads=2,
            prime_exponents_only=False,
            allow_non_coprime=True,
        )
        self.assertEqual(res.counterexamples_found, 0)
        self.assertGreaterEqual(res.non_primitive_equalities, 1)
        found_3_6_3 = any(
            d.get("a") == 3 and d.get("b") == 6 and d.get("c") == 3
            for d in res.details
        )
        self.assertTrue(found_3_6_3, "3^3 + 6^3 = 3^5 should be detected in non-coprime search")

    # -------------------------------------------------------------
    # 7. C + GMP Engine Verification & Parity
    # -------------------------------------------------------------
    def test_gmp_search_engine_parity(self) -> None:
        """C+GMP engine and Python engine must check the identical number of pairs."""
        gmp_bin = CURRENT_DIR / "beal_search_gmp"
        if not gmp_bin.exists():
            self.skipTest("beal_search_gmp binary not found")

        mb = 100
        me = 8
        res_py = search_python(min_base=2, max_base=mb, min_exp=3, max_exp=me, threads=4)
        res_gmp = search_gmp(min_base=2, max_base=mb, min_exp=3, max_exp=me, threads=4)

        self.assertEqual(res_py.pairs_checked, res_gmp.pairs_checked,
                         "Python and C+GMP engines must evaluate identical pair counts")
        self.assertEqual(res_py.counterexamples_found, 0)
        self.assertEqual(res_gmp.counterexamples_found, 0)
        self.assertTrue(res_py.conjecture_verified)
        self.assertTrue(res_gmp.conjecture_verified)

    # -------------------------------------------------------------
    # 8. Automated Pre-flight Near-Miss Runner
    # -------------------------------------------------------------
    def test_preflight_runner(self) -> None:
        """Verify preflight near-misses test suite returns 100% pass."""
        results = test_near_misses_and_edge_cases(verbose=False)
        self.assertTrue(all(r["passed"] for r in results))
        self.assertEqual(len(results), 13)


if __name__ == "__main__":
    unittest.main(verbosity=2)
