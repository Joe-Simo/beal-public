"""
Section 8: Beal Conjecture Exact Counterexample Checker (Python)

REQUIRE EXACT, REPRODUCIBLE COMPUTATION.
Before relying on a search, validate a small transparent counterexample checker.

Requirements:
1. Checks all six inputs: bases (A, B, C) and exponents (x, y, z).
2. Positivity: all bases and exponents must be strictly positive integers (> 0).
3. Exponent restrictions: exponents must satisfy x >= 3, y >= 3, z >= 3.
4. Exact equality: verifies A^x + B^y == C^z over arbitrary-precision integers.
5. Greatest common divisor: calculates gcd(A, B, C) = gcd(gcd(A, B), C).
   A counterexample requires gcd(A, B, C) == 1 (primitive).
   If gcd(A, B, C) > 1, the equality satisfies the Beal conjecture and is NOT a counterexample.
6. Rejects non-integers, unsafe IEEE-754 floating-point numbers, zeros, negatives, and malformed inputs.
"""

from __future__ import annotations

import json
import math
import sys
from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence

# Disable string conversion limit for large integer audits (Python 3.11+)
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


@dataclass(frozen=True)
class BealCheckResult:
    """Detailed result of checking an input candidate against Section 8 criteria."""

    admissible: bool
    equality: bool
    primitive: bool
    counterexample: bool
    reason: str = ""
    a: int | None = None
    b: int | None = None
    c: int | None = None
    x: int | None = None
    y: int | None = None
    z: int | None = None
    lhs: int | None = None
    rhs: int | None = None
    gcd: int | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert result to a clean dictionary representation."""
        data = asdict(self)
        # Filter out None values in top-level view if desired, or keep exact
        return data


def parse_exact(v: Any) -> int | None:
    """
    Parse an input into an exact arbitrary-precision integer.

    - Rejects bool (since bool is an int subclass in Python).
    - Accepts int directly (arbitrary precision in Python 3).
    - Rejects float (IEEE-754 binary64 floats are non-integers or subject to precision limits).
    - Accepts str matching /^[+-]?\\d+$/. Rejects decimals ("1.2") and text.
    - Rejects None, complex, sequences, mappings, etc.
    """
    if isinstance(v, bool):
        return None
    if isinstance(v, int):
        return v
    if isinstance(v, float):
        return None
    if isinstance(v, str):
        s = v.strip()
        if not s:
            return None
        sign_offset = 1 if s[0] in "+-" else 0
        digits_part = s[sign_offset:]
        if digits_part and digits_part.isdigit():
            try:
                return int(s)
            except ValueError:
                return None
        return None
    return None


def gcd3(a: int, b: int, c: int) -> int:
    """Compute gcd of three integers: gcd(gcd(a, b), c)."""
    return math.gcd(math.gcd(a, b), c)


def check_beal(*args: Any) -> BealCheckResult:
    """
    Validates a potential Beal counterexample.

    Can be invoked with:
    - A sequence of 6 elements: check_beal([A, B, C, x, y, z]) or check_beal((A, B, C, x, y, z))
    - 6 positional arguments: check_beal(A, B, C, x, y, z)
    - A mapping/dict: check_beal({"A": 3, "B": 6, "C": 3, "x": 3, "y": 3, "z": 5})
    """
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        raw_inputs: Sequence[Any] = args[0]
    elif len(args) == 1 and isinstance(args[0], Mapping):
        mapping = args[0]
        a = mapping.get("A", mapping.get("a"))
        b = mapping.get("B", mapping.get("b"))
        c = mapping.get("C", mapping.get("c"))
        x = mapping.get("x", mapping.get("X"))
        y = mapping.get("y", mapping.get("Y"))
        z = mapping.get("z", mapping.get("Z"))
        raw_inputs = [a, b, c, x, y, z]
    else:
        raw_inputs = args

    # Check 1: Exactly six inputs
    if len(raw_inputs) != 6:
        return BealCheckResult(
            admissible=False,
            equality=False,
            primitive=False,
            counterexample=False,
            reason=f"Input size mismatch: expected exactly 6 inputs (A, B, C, x, y, z), got {len(raw_inputs)}",
        )

    # Check 2: Exact integer validation (no floats, no booleans, no decimals)
    parsed = [parse_exact(x) for x in raw_inputs]
    names = ["A", "B", "C", "x", "y", "z"]
    invalid_indices = [i for i, p in enumerate(parsed) if p is None]
    if invalid_indices:
        bad_names = ", ".join(names[i] for i in invalid_indices)
        return BealCheckResult(
            admissible=False,
            equality=False,
            primitive=False,
            counterexample=False,
            reason=f"Noninteger, unsafe floating-point, or unparseable input at: {bad_names}",
        )

    a, b, c, x, y, z = (p for p in parsed if p is not None)

    # Check 3: Positivity checks
    if a <= 0 or b <= 0 or c <= 0:
        bad_bases = []
        if a <= 0: bad_bases.append(f"A={a}")
        if b <= 0: bad_bases.append(f"B={b}")
        if c <= 0: bad_bases.append(f"C={c}")
        return BealCheckResult(
            admissible=False,
            equality=False,
            primitive=False,
            counterexample=False,
            reason=f"Positivity violation: bases must be strictly positive integers (> 0): {', '.join(bad_bases)}",
            a=a, b=b, c=c, x=x, y=y, z=z,
        )

    if x <= 0 or y <= 0 or z <= 0:
        bad_exp = []
        if x <= 0: bad_exp.append(f"x={x}")
        if y <= 0: bad_exp.append(f"y={y}")
        if z <= 0: bad_exp.append(f"z={z}")
        return BealCheckResult(
            admissible=False,
            equality=False,
            primitive=False,
            counterexample=False,
            reason=f"Positivity violation: exponents must be strictly positive integers (> 0): {', '.join(bad_exp)}",
            a=a, b=b, c=c, x=x, y=y, z=z,
        )

    # Check 4: Greatest common divisor of the three bases
    common_divisor = gcd3(a, b, c)
    primitive = (common_divisor == 1)

    # Check 5: Exact equality check (A^x + B^y == C^z)
    try:
        lhs = pow(a, x) + pow(b, y)
        rhs = pow(c, z)
        equality = (lhs == rhs)
    except Exception as err:
        return BealCheckResult(
            admissible=False,
            equality=False,
            primitive=primitive,
            counterexample=False,
            reason=f"Exponentiation overflow or error: {err}",
            a=a, b=b, c=c, x=x, y=y, z=z, gcd=common_divisor,
        )

    # Check 6: Exponent restrictions (x, y, z >= 3)
    exponents_admissible = (x >= 3 and y >= 3 and z >= 3)
    if not exponents_admissible:
        small_exp = []
        if x < 3: small_exp.append(f"x={x}")
        if y < 3: small_exp.append(f"y={y}")
        if z < 3: small_exp.append(f"z={z}")
        return BealCheckResult(
            admissible=False,
            equality=equality,
            primitive=primitive,
            counterexample=False,
            reason=f"Exponent restriction violated (x, y, z must all be >= 3): {', '.join(small_exp)}",
            a=a, b=b, c=c, x=x, y=y, z=z, lhs=lhs, rhs=rhs, gcd=common_divisor,
        )

    # All structural and domain conditions passed: admissible is True
    counterexample = equality and primitive

    if counterexample:
        reason = f"Genuine Beal counterexample verified: {a}^{x} + {b}^{y} == {c}^{z} with gcd({a}, {b}, {c}) == 1"
    elif equality and not primitive:
        reason = f"Valid equality ({a}^{x} + {b}^{y} == {c}^{z}), but fails common-factor requirement: gcd({a}, {b}, {c}) == {common_divisor} > 1 (satisfies Beal conjecture)"
    elif not equality:
        reason = f"Arithmetic mismatch: {a}^{x} + {b}^{y} == {lhs} != {rhs} == {c}^{z}"
    else:
        reason = "Conditions not satisfied"

    return BealCheckResult(
        admissible=True,
        equality=equality,
        primitive=primitive,
        counterexample=counterexample,
        reason=reason,
        a=a, b=b, c=c, x=x, y=y, z=z, lhs=lhs, rhs=rhs, gcd=common_divisor,
    )


def run_self_verification() -> None:
    """Self-verification routine when executed directly."""
    # 1. Valid equality that fails common-factor requirement: 3^3 + 6^3 = 3^5
    nonprimitive = check_beal([3, 6, 3, 3, 3, 5])
    assert nonprimitive.admissible, "3^3+6^3=3^5 must be admissible"
    assert nonprimitive.equality, "3^3+6^3=3^5 exact equality must hold"
    assert not nonprimitive.primitive, "3^3+6^3=3^5 has gcd=3, not primitive"
    assert not nonprimitive.counterexample, "3^3+6^3=3^5 is not a counterexample"
    assert nonprimitive.gcd == 3, "3^3+6^3=3^5 gcd must be 3"

    # 2. Valid equality excluded because an exponent is 2: 3^5 + 10^2 = 7^3
    exp_two = check_beal([3, 10, 7, 5, 2, 3])
    assert not exp_two.admissible, "3^5+10^2=7^3 must be excluded (exponent y=2)"
    assert exp_two.equality, "3^5+10^2=7^3 exact equality holds (243+100=343)"
    assert exp_two.primitive, "gcd(3, 10, 7) == 1"
    assert not exp_two.counterexample, "Excluded equality cannot be a counterexample"

    # 3. Arithmetic mismatch: 2^3 + 3^3 != 4^3
    mismatch = check_beal([2, 3, 4, 3, 3, 3])
    assert mismatch.admissible, "2^3+3^3!=4^3 is admissible domain"
    assert not mismatch.equality, "2^3+3^3 != 4^3 must fail equality"
    assert mismatch.primitive, "gcd(2, 3, 4) == 1"
    assert not mismatch.counterexample, "Mismatch cannot be a counterexample"

    # 4. Zero and negative inputs
    for bad in [0, -1, -100]:
        assert not check_beal([bad, 3, 4, 3, 3, 3]).admissible, f"Base A={bad} rejected"
        assert not check_beal([3, bad, 4, 3, 3, 3]).admissible, f"Base B={bad} rejected"
        assert not check_beal([3, 4, bad, 3, 3, 3]).admissible, f"Base C={bad} rejected"
        assert not check_beal([3, 4, 5, bad, 3, 3]).admissible, f"Exponent x={bad} rejected"
        assert not check_beal([3, 4, 5, 3, bad, 3]).admissible, f"Exponent y={bad} rejected"
        assert not check_beal([3, 4, 5, 3, 3, bad]).admissible, f"Exponent z={bad} rejected"

    # 5. Noninteger inputs
    for bad in [1.5, 1.0, "1.2", True, False, None, float("nan"), float("inf"), [1, 2], "abc"]:
        assert not check_beal([bad, 3, 4, 3, 3, 3]).admissible, f"Noninteger {bad!r} rejected"

    # 6. Integers beyond ordinary floating-point safe-integer limits
    # Exact arbitrary precision equality: (2^60)^3 + (2^60)^3 = 2^181
    big_check = check_beal([2**60, 2**60, 2, 3, 3, 181])
    assert big_check.admissible, "Arbitrary-precision integer input is admissible"
    assert big_check.equality, "Beyond binary64 safe integer equality verified exactly"
    assert not big_check.primitive, "gcd(2^60, 2^60, 2) == 2, not primitive"
    assert not big_check.counterexample, "Beal holds for powers of 2"

    # Decimal string serialization beyond safe integer limit (2^53 + 1)
    assert parse_exact("9007199254740993") == 9007199254740993, "Large decimal string parsed exactly"

    # 7. Base one retained
    assert check_beal([1, 2, 3, 3, 3, 3]).admissible, "Base 1 retained as positive integer"

    report = {
        "status": "verified",
        "section": 8,
        "implementation": "Python (arbitrary-precision int)",
        "checksPassed": [
            "nonprimitive_equality_3^3+6^3=3^5",
            "exponent_two_excluded_3^5+10^2=7^3",
            "arithmetic_mismatch_2^3+3^3!=4^3",
            "zero_and_negative_inputs_rejected",
            "noninteger_inputs_rejected",
            "floating_point_rejected",
            "beyond_safe_integer_exact_computation",
            "decimal_string_serialization",
            "base_one_retained",
        ],
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run_self_verification()
