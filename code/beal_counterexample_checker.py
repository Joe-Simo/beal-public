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

if __name__ == "__main__":
    run_self_verification()
