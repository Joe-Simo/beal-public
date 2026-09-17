"""
Section 8 C+GMP Counterexample Checker Test Suite

Tests `check_counterexample_gmp` binary on all Section 8 requirements:
1. Exit codes and status codes:
   - 0: VALID_COUNTEREXAMPLE
   - 1: COMMON_FACTOR_VIOLATION (e.g. 3^3 + 6^3 = 3^5)
   - 2: EXPONENT_TOO_SMALL      (e.g. 3^5 + 10^2 = 7^3)
   - 3: ARITHMETIC_MISMATCH     (e.g. 2^3 + 3^3 != 4^3)
   - 4: NON_POSITIVE_INPUT      (zeros and negatives)
   - 5: INVALID_INPUT           (non-integers, floats, malformed args)
2. Exact JSON and plain-text output validation.
3. Arbitrary-precision integer arithmetic beyond IEEE-754 binary64 safe integer limits.
"""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).resolve().parent.parent
CODE_DIR = REPO_ROOT / "code"
BINARY_PATH = CODE_DIR / "check_counterexample_gmp"


class TestCheckCounterexampleGMP(unittest.TestCase):
    """Test suite running check_counterexample_gmp and verifying exit codes and outputs."""

    @classmethod
    def setUpClass(cls) -> None:
        # Build binary if not already built
        if not BINARY_PATH.exists():
            cmd = ["make", "-C", str(CODE_DIR), "check_counterexample_gmp"]
            proc = subprocess.run(cmd, capture_output=True, text=True)
            if proc.returncode != 0:
                raise RuntimeError(f"Failed to build binary:\n{proc.stderr}")
        assert BINARY_PATH.exists(), f"Binary not found at {BINARY_PATH}"

    def run_checker(self, args: list[str], flag: str | None = None) -> tuple[int, str, dict | None]:
        """Runs the binary and returns (exit_code, stdout, parsed_json_or_None)."""
        cmd = [str(BINARY_PATH)]
        if flag:
            cmd.append(flag)
        cmd.extend(args)
        proc = subprocess.run(cmd, capture_output=True, text=True)
        parsed = None
        if proc.stdout.strip().startswith("{"):
            try:
                parsed = json.loads(proc.stdout)
            except Exception:
                pass
        return proc.returncode, proc.stdout, parsed

    # 1. Common Factor Violations (Exit code 1)
    def test_01_common_factor_violation_3_3_6_3_3_5(self) -> None:
        """3^3 + 6^3 = 3^5 (A=3, x=3, B=6, y=3, C=3, z=5) -> COMMON_FACTOR_VIOLATION (exit 1)."""
        code, out, data = self.run_checker(["3", "3", "6", "3", "3", "5"])
        self.assertEqual(code, 1)
        self.assertIsNotNone(data)
        self.assertEqual(data["status"], "COMMON_FACTOR_VIOLATION")
        self.assertEqual(data["code"], 1)
        self.assertTrue(data["admissible"])
        self.assertTrue(data["equality"])
        self.assertFalse(data["primitive"])
        self.assertFalse(data["counterexample"])
        self.assertEqual(data["gcd"], "3")

    def test_01_common_factor_violation_7_3_7_4_14_3(self) -> None:
        """7^3 + 7^4 = 14^3 (A=7, x=3, B=7, y=4, C=14, z=3) -> COMMON_FACTOR_VIOLATION (exit 1)."""
        code, out, data = self.run_checker(["7", "3", "7", "4", "14", "3"])
        self.assertEqual(code, 1)
        self.assertIsNotNone(data)
        self.assertEqual(data["status"], "COMMON_FACTOR_VIOLATION")
        self.assertEqual(data["gcd"], "7")

    def test_01_common_factor_violation_2_3_2_3_2_4(self) -> None:
        """2^3 + 2^3 = 2^4 (A=2, x=3, B=2, y=3, C=2, z=4) -> COMMON_FACTOR_VIOLATION (exit 1)."""
        code, out, data = self.run_checker(["2", "3", "2", "3", "2", "4"])
        self.assertEqual(code, 1)
        self.assertIsNotNone(data)
        self.assertEqual(data["status"], "COMMON_FACTOR_VIOLATION")
        self.assertEqual(data["gcd"], "2")

    # 2. Exponent Restrictions (Exit code 2)
    def test_02_exponent_too_small_3_5_10_2_7_3(self) -> None:
        """3^5 + 10^2 = 7^3 (A=3, x=5, B=10, y=2, C=7, z=3) -> EXPONENT_TOO_SMALL (exit 2)."""
        code, out, data = self.run_checker(["3", "5", "10", "2", "7", "3"])
        self.assertEqual(code, 2)
        self.assertIsNotNone(data)
        self.assertEqual(data["status"], "EXPONENT_TOO_SMALL")
        self.assertEqual(data["code"], 2)
        self.assertFalse(data["admissible"])
        self.assertTrue(data["equality"])  # 243 + 100 == 343
        self.assertTrue(data["primitive"]) # gcd(3, 10, 7) == 1
        self.assertFalse(data["counterexample"])
        self.assertIn("y=2", data["reason"])

    def test_02_exponent_too_small_2_5_7_2_3_4(self) -> None:
        """2^5 + 7^2 = 3^4 (A=2, x=5, B=7, y=2, C=3, z=4) -> EXPONENT_TOO_SMALL (exit 2)."""
        code, out, data = self.run_checker(["2", "5", "7", "2", "3", "4"])
        self.assertEqual(code, 2)
        self.assertIsNotNone(data)
        self.assertEqual(data["status"], "EXPONENT_TOO_SMALL")
        self.assertTrue(data["equality"])
        self.assertFalse(data["admissible"])

    def test_02_exponent_too_small_13_2_7_3_2_9(self) -> None:
        """13^2 + 7^3 = 2^9 (A=13, x=2, B=7, y=3, C=2, z=9) -> EXPONENT_TOO_SMALL (exit 2)."""
        code, out, data = self.run_checker(["13", "2", "7", "3", "2", "9"])
        self.assertEqual(code, 2)
        self.assertIsNotNone(data)
        self.assertEqual(data["status"], "EXPONENT_TOO_SMALL")
        self.assertTrue(data["equality"])
        self.assertFalse(data["admissible"])
        self.assertIn("x=2", data["reason"])

    def test_02_exponent_too_small_1_3_2_3_3_2(self) -> None:
        """1^3 + 2^3 = 3^2 (A=1, x=3, B=2, y=3, C=3, z=2) -> EXPONENT_TOO_SMALL (exit 2)."""
        code, out, data = self.run_checker(["1", "3", "2", "3", "3", "2"])
        self.assertEqual(code, 2)
        self.assertIsNotNone(data)
        self.assertEqual(data["status"], "EXPONENT_TOO_SMALL")
        self.assertTrue(data["equality"])
        self.assertFalse(data["admissible"])
        self.assertIn("z=2", data["reason"])

    def test_02_exponent_one_rejected(self) -> None:
        """Exponent equal to 1 rejected as EXPONENT_TOO_SMALL (exit 2)."""
        code, out, data = self.run_checker(["3", "1", "4", "3", "5", "3"])
        self.assertEqual(code, 2)
        self.assertEqual(data["status"], "EXPONENT_TOO_SMALL")

    # 3. Arithmetic Mismatch (Exit code 3)
    def test_03_arithmetic_mismatch_2_3_3_3_4_3(self) -> None:
        """2^3 + 3^3 != 4^3 (A=2, x=3, B=3, y=3, C=4, z=3) -> ARITHMETIC_MISMATCH (exit 3)."""
        code, out, data = self.run_checker(["2", "3", "3", "3", "4", "3"])
        self.assertEqual(code, 3)
        self.assertIsNotNone(data)
        self.assertEqual(data["status"], "ARITHMETIC_MISMATCH")
        self.assertEqual(data["code"], 3)
        self.assertTrue(data["admissible"])
        self.assertFalse(data["equality"])
        self.assertFalse(data["counterexample"])

    def test_03_arithmetic_mismatch_3_3_4_3_5_3(self) -> None:
        """3^3 + 4^3 != 5^3 (A=3, x=3, B=4, y=3, C=5, z=3) -> ARITHMETIC_MISMATCH (exit 3)."""
        code, out, data = self.run_checker(["3", "3", "4", "3", "5", "3"])
        self.assertEqual(code, 3)
        self.assertEqual(data["status"], "ARITHMETIC_MISMATCH")

    def test_03_base_one_mismatch(self) -> None:
        """1^3 + 2^3 != 3^3 (1 + 8 = 9 != 27) -> ARITHMETIC_MISMATCH (exit 3)."""
        code, out, data = self.run_checker(["1", "3", "2", "3", "3", "3"])
        self.assertEqual(code, 3)
        self.assertTrue(data["admissible"])
        self.assertFalse(data["equality"])

    # 4. Non-Positive Inputs (Exit code 4)
    def test_04_zeros_rejected(self) -> None:
        """Zero inputs in all 6 positions -> NON_POSITIVE_INPUT (exit 4)."""
        cases = [
            ["0", "3", "3", "3", "4", "3"],  # A = 0
            ["3", "0", "3", "3", "4", "3"],  # x = 0
            ["3", "3", "0", "3", "4", "3"],  # B = 0
            ["3", "3", "3", "0", "4", "3"],  # y = 0
            ["3", "3", "3", "3", "0", "3"],  # C = 0
            ["3", "3", "3", "3", "4", "0"],  # z = 0
        ]
        for c in cases:
            code, out, data = self.run_checker(c)
            self.assertEqual(code, 4, f"Expected exit code 4 for {c}")
            self.assertIsNotNone(data)
            self.assertEqual(data["status"], "NON_POSITIVE_INPUT")
            self.assertFalse(data["admissible"])

    def test_04_negatives_rejected(self) -> None:
        """Negative inputs in all 6 positions -> NON_POSITIVE_INPUT (exit 4)."""
        cases = [
            ["-2", "3", "3", "3", "4", "3"],
            ["2", "-3", "3", "3", "4", "3"],
            ["2", "3", "-3", "3", "4", "3"],
            ["2", "3", "3", "-3", "4", "3"],
            ["2", "3", "3", "3", "-4", "3"],
            ["2", "3", "3", "3", "4", "-3"],
        ]
        for c in cases:
            code, out, data = self.run_checker(c)
            self.assertEqual(code, 4, f"Expected exit code 4 for {c}")
            self.assertEqual(data["status"], "NON_POSITIVE_INPUT")

    # 5. Invalid Inputs (Exit code 5)
    def test_05_non_integer_strings_rejected(self) -> None:
        """Non-integer strings like decimals, hex, text -> INVALID_INPUT (exit 5)."""
        bads = ["1.5", "1.0", "abc", "1e5", "0x10", "3,000"]
        for b in bads:
            code, out, data = self.run_checker([b, "3", "3", "3", "4", "3"])
            self.assertEqual(code, 5, f"Expected exit code 5 for input {b}")
            self.assertEqual(data["status"], "INVALID_INPUT")

    def test_05_argument_count_mismatch(self) -> None:
        """Too few or too many arguments -> INVALID_INPUT (exit 5)."""
        for args in [[], ["3", "3"], ["3", "3", "3", "3", "3"], ["3", "3", "3", "3", "3", "3", "3"]]:
            code, out, data = self.run_checker(args)
            self.assertEqual(code, 5)
            self.assertEqual(data["status"], "INVALID_INPUT")

    # 6. Arbitrary Precision Integers Beyond Safe-Integer Limits
    def test_06_beyond_binary64_powers(self) -> None:
        """(2^60)^3 + (2^60)^3 = 2^181 with 2^60 >> 2^53."""
        base_60 = str(2**60)
        code, out, data = self.run_checker([base_60, "3", base_60, "3", "2", "181"])
        self.assertEqual(code, 1)
        self.assertEqual(data["status"], "COMMON_FACTOR_VIOLATION")
        self.assertTrue(data["equality"])
        self.assertEqual(data["gcd"], "2")

    def test_06_beyond_binary64_mismatch(self) -> None:
        """Arbitrary precision large integers that mismatch."""
        base_60 = str(2**60)
        code, out, data = self.run_checker([base_60, "3", base_60, "3", "3", "181"])
        self.assertEqual(code, 3)
        self.assertEqual(data["status"], "ARITHMETIC_MISMATCH")

    # 7. Plain Text Output Mode
    def test_07_plain_text_mode(self) -> None:
        """Verifies --text flag outputs structured plain text."""
        code, out, _ = self.run_checker(["3", "3", "6", "3", "3", "5"], flag="--text")
        self.assertEqual(code, 1)
        self.assertIn("STATUS: COMMON_FACTOR_VIOLATION", out)
        self.assertIn("CODE: 1", out)
        self.assertIn("GCD: 3", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
