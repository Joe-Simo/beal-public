"""U88 exact cubic Padé certificate for the weighted Beal subproblem.

The checker constructs the invariant from the binomial series; it does not
hard-code the large null-vector. All arithmetic deciding the theorem is exact.
"""
from __future__ import annotations

from fractions import Fraction
from functools import reduce
from itertools import combinations_with_replacement
from math import gcd, lcm
import json
import sympy as sp

WEIGHT = 15
DEGREE = 3
S_CANCELLATIONS = 14
SERIES_TERMS = 15
FORCED_PRODUCT = 433992707035920672833426144791


def binomial_series(limit: int) -> list[Fraction]:
    out = [Fraction(1)]
    for k in range(1, limit + 1):
        out.append(out[-1] * Fraction(1 - 17 * (k - 1), 17 * k))
    return out


B = binomial_series(200)


def f(j: int, m: int) -> Fraction:
    return B[j + 10 * m] * ((-256) ** m)


def conv(a: list[Fraction], b: list[Fraction], length: int) -> list[Fraction]:
    out = [Fraction(0)] * length
    for i, x in enumerate(a):
        for j, y in enumerate(b[: length - i]):
            out[i + j] += x * y
    return out


def monomial_series(indices: tuple[int, ...]) -> list[Fraction]:
    out = [Fraction(1)] + [Fraction(0)] * (SERIES_TERMS - 1)
    for j in indices:
        out = conv(out, [f(j, m) for m in range(SERIES_TERMS)], SERIES_TERMS)
    return out


monomials = [
    idx
    for idx in combinations_with_replacement(range(10), DEGREE)
    if sum(idx) == WEIGHT
]
assert len(monomials) == 15
series = [monomial_series(idx) for idx in monomials]

rows: list[list[int]] = []
for n in range(S_CANCELLATIONS):
    values = [s[n] for s in series]
    row_lcm = 1
    for value in values:
        row_lcm = lcm(row_lcm, value.denominator)
    row = [value.numerator * (row_lcm // value.denominator) for value in values]
    row_gcd = reduce(gcd, (abs(x) for x in row if x), 0) or 1
    rows.append([x // row_gcd for x in row])

matrix = sp.Matrix(rows)
assert matrix.rank() == 14
nullspace = matrix.nullspace()
assert len(nullspace) == 1
vector = nullspace[0]
vector_lcm = 1
for entry in vector:
    vector_lcm = lcm(vector_lcm, int(entry.q))
lambda_int = [int(entry * vector_lcm) for entry in vector]
lambda_gcd = reduce(gcd, (abs(x) for x in lambda_int if x), 0) or 1
lambda_int = [x // lambda_gcd for x in lambda_int]
assert reduce(gcd, (abs(x) for x in lambda_int if x), 0) == 1

combo: list[Fraction] = []
for n in range(SERIES_TERMS):
    combo.append(sum((Fraction(lambda_int[j]) * series[j][n] for j in range(15)), Fraction(0)))
assert combo[:S_CANCELLATIONS] == [0] * S_CANCELLATIONS
lead = combo[S_CANCELLATIONS]
assert lead != 0
assert lead.numerator % 31 != 0
assert lead.denominator % 31 != 0

local_order = WEIGHT + 10 * S_CANCELLATIONS
assert local_order == 155
lambda_l1 = sum(abs(x) for x in lambda_int)
assert len(str(lambda_l1)) == 867

lhs = FORCED_PRODUCT ** (local_order * 17)
rhs_21122 = 27 * (lambda_l1**17) * (10 ** (3 * 21122))
rhs_21123 = 27 * (lambda_l1**17) * (10 ** (3 * 21123))
assert lhs > rhs_21122
assert lhs < rhs_21123

print(
    json.dumps(
        {
            "checkpoint": "U88",
            "degree": DEGREE,
            "weight": WEIGHT,
            "monomials": [list(x) for x in monomials],
            "monomial_count": len(monomials),
            "cancelled_S_coefficients": list(range(S_CANCELLATIONS)),
            "first_nonzero_S_coefficient": S_CANCELLATIONS,
            "local_Y_order": local_order,
            "lambda_max_digits": max(len(str(abs(x))) for x in lambda_int),
            "lambda_l1_digits": len(str(lambda_l1)),
            "lead_31_adic_unit": True,
            "lead_mod31": [lead.numerator % 31, lead.denominator % 31],
            "forced_product": str(FORCED_PRODUCT),
            "forced_product_power_dividing_invariant": local_order,
            "max_base_strictly_greater_than_power_of_10": 21122,
            "full_Beal_solved": False,
        },
        indent=2,
    )
)
