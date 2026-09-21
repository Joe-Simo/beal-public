"""
Section 8: Beal Counterexample Checker Entrypoint
Re-exports the complete checker API from section8_counterexample_checker.py
"""

try:
    from .section8_counterexample_checker import (
        BealCheckResult,
        check_beal,
        gcd3,
        parse_exact,
        run_self_verification,
    )
except ImportError:
    from section8_counterexample_checker import (
        BealCheckResult,
        check_beal,
        gcd3,
        parse_exact,
        run_self_verification,
    )

__all__ = [
    "BealCheckResult",
    "check_beal",
    "gcd3",
    "parse_exact",
    "run_self_verification",
]

import sys
import json

__all__ = [
    "BealCheckResult",
    "check_beal",
    "gcd3",
    "parse_exact",
    "run_self_verification",
]

def main() -> int:
    # If called with CLI args: <A> <x> <B> <y> <C> <z>
    # (optionally with leading flags like --json or --text)
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) == 6:
        A_str, x_str, B_str, y_str, C_str, z_str = args
        A = parse_exact(A_str)
        x = parse_exact(x_str)
        B = parse_exact(B_str)
        y = parse_exact(y_str)
        C = parse_exact(C_str)
        z = parse_exact(z_str)

        if any(v is None for v in (A, x, B, y, C, z)):
            print(json.dumps({"status": "INVALID_INPUT", "reason": "Non-integer input"}))
            return 5
        if any(v <= 0 for v in (A, x, B, y, C, z)):
            print(json.dumps({"status": "NON_POSITIVE_INPUT", "reason": "All inputs must be > 0"}))
            return 4
        if any(v < 3 for v in (x, y, z)):
            print(json.dumps({"status": "EXPONENT_TOO_SMALL", "reason": "Exponents must be >= 3"}))
            return 2

        res = check_beal([A, B, C, x, y, z])
        if res.counterexample:
            print(json.dumps({
                "status": "VALID_COUNTEREXAMPLE",
                "A": str(A), "x": x, "B": str(B), "y": y, "C": str(C), "z": z,
                "reason": res.reason
            }))
            return 0
        elif res.equality and not res.primitive:
            print(json.dumps({
                "status": "COMMON_FACTOR_VIOLATION",
                "A": str(A), "x": x, "B": str(B), "y": y, "C": str(C), "z": z,
                "gcd": res.gcd, "reason": res.reason
            }))
            return 1
        else:
            print(json.dumps({
                "status": "ARITHMETIC_MISMATCH",
                "A": str(A), "x": x, "B": str(B), "y": y, "C": str(C), "z": z,
                "reason": res.reason
            }))
            return 3
    else:
        run_self_verification()
        return 0

if __name__ == "__main__":
    sys.exit(main())
