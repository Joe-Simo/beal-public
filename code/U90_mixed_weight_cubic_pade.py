"""U90 mixed-weight cubic Padé certificate.

Degree-three monomials are grouped by total coefficient-index weight modulo 10,
so weights differing by 10 can cancel after factoring S=T^10.  Exact integer
nullspace arithmetic constructs the extremal residue-9 invariant.
"""
from __future__ import annotations

from fractions import Fraction
from functools import reduce
from itertools import combinations_with_replacement
from math import gcd, lcm
import json
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix

DEGREE = 3
RESIDUE = 9
CANCELLATIONS = 21
TERMS = 22
FORCED_PRODUCT = 433992707035920672833426144791


def binomial_series(limit: int) -> list[Fraction]:
    out = [Fraction(1)]
    for k in range(1, limit + 1):
        out.append(out[-1] * Fraction(1 - 17 * (k - 1), 17 * k))
    return out


B = binomial_series(260)


def f(j: int, m: int) -> Fraction:
    return B[j + 10 * m] * ((-256) ** m)


def conv(a: list[Fraction], b: list[Fraction], length: int) -> list[Fraction]:
    out = [Fraction(0)] * length
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b[: length - i]):
            out[i + j] += x * y
    return out


def base_series(indices: tuple[int, ...]) -> list[Fraction]:
    out = [Fraction(1)] + [Fraction(0)] * (TERMS - 1)
    for j in indices:
        out = conv(out, [f(j, m) for m in range(TERMS)], TERMS)
    return out


all_monomials = list(combinations_with_replacement(range(10), DEGREE))
monomials = [idx for idx in all_monomials if sum(idx) % 10 == RESIDUE]
assert len(all_monomials) == 220
assert len(monomials) == 22
assert {sum(idx) for idx in monomials} == {9, 19}

series: list[list[Fraction]] = []
for idx in monomials:
    shift = (sum(idx) - RESIDUE) // 10
    base = base_series(idx)
    series.append(([Fraction(0)] * shift + base)[:TERMS])

rows: list[list[int]] = []
for n in range(CANCELLATIONS):
    values = [s[n] for s in series]
    row_lcm = 1
    for value in values:
        row_lcm = lcm(row_lcm, value.denominator)
    row = [value.numerator * (row_lcm // value.denominator) for value in values]
    row_gcd = reduce(gcd, (abs(x) for x in row if x), 0) or 1
    rows.append([x // row_gcd for x in row])

nullspace = DomainMatrix.from_list(rows, ZZ).nullspace().to_list()
assert len(nullspace) == 1
lambda_int = [int(x) for x in nullspace[0]]
lambda_gcd = reduce(gcd, (abs(x) for x in lambda_int if x), 0) or 1
lambda_int = [x // lambda_gcd for x in lambda_int]
if lambda_int[-1] < 0:
    lambda_int = [-x for x in lambda_int]
assert all(sum(lambda_int[j] * rows[n][j] for j in range(22)) == 0 for n in range(CANCELLATIONS))

lead = sum((Fraction(lambda_int[j]) * series[j][CANCELLATIONS] for j in range(22)), Fraction(0))
assert lead != 0
assert lead.numerator % 31 != 0
assert lead.denominator % 31 != 0

local_order = RESIDUE + 10 * CANCELLATIONS
assert local_order == 219
lambda_l1 = sum(abs(x) for x in lambda_int)
assert len(str(lambda_l1)) == 1904
assert max(len(str(abs(x))) for x in lambda_int) == 1903

lhs = FORCED_PRODUCT ** (local_order * 17)
rhs_25993 = 27 * (lambda_l1**17) * (10 ** (3 * 25993))
rhs_25994 = 27 * (lambda_l1**17) * (10 ** (3 * 25994))
assert lhs > rhs_25993
assert lhs < rhs_25994

print(
    json.dumps(
        {
            "checkpoint": "U90",
            "degree": DEGREE,
            "weight_residue_mod_10": RESIDUE,
            "monomial_count": len(monomials),
            "actual_weights": sorted({sum(idx) for idx in monomials}),
            "cancelled_S_coefficients": list(range(CANCELLATIONS)),
            "first_nonzero_S_coefficient": CANCELLATIONS,
            "local_Y_order": local_order,
            "lambda_max_digits": max(len(str(abs(x))) for x in lambda_int),
            "lambda_l1_digits": len(str(lambda_l1)),
            "lead_31_adic_unit": True,
            "lead_mod31": [lead.numerator % 31, lead.denominator % 31],
            "forced_product": str(FORCED_PRODUCT),
            "forced_product_power_dividing_invariant": local_order,
            "max_base_strictly_greater_than_power_of_10": 25993,
            "full_Beal_solved": False,
        },
        indent=2,
    )
)
