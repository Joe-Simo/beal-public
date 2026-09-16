"""U89 exact/modular audit of the degree-four Padé continuation.

A mod-5003 scan provides rigorous upper bounds on cancellation order because a
nonzero minor modulo 5003 is nonzero over Q.  The extremal weight-18 candidate
is then reconstructed over Q exactly.
"""
from __future__ import annotations

from fractions import Fraction
from functools import reduce
from itertools import combinations_with_replacement
from math import gcd, lcm
import json
import sympy as sp

DEGREE = 4
MODULUS = 5003
SCAN_TERMS = 50
FORCED_PRODUCT = 433992707035920672833426144791


def rank_mod(matrix: list[list[int]], p: int) -> int:
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col] % p, -1, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for r in range(rank + 1, rows):
            if a[r][col] % p:
                factor = a[r][col] % p
                a[r] = [(a[r][j] - factor * a[rank][j]) % p for j in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def binomial_mod(limit: int, p: int) -> list[int]:
    assert limit < p
    out = [1]
    for k in range(1, limit + 1):
        out.append(out[-1] * (1 - 17 * (k - 1)) % p * pow(17 * k % p, -1, p) % p)
    return out


max_index = 9 + 10 * (SCAN_TERMS - 1)
bmod = binomial_mod(max_index, MODULUS)
fmod = {
    j: [bmod[j + 10 * m] * pow(-256, m, MODULUS) % MODULUS for m in range(SCAN_TERMS)]
    for j in range(10)
}


def conv_mod(a: list[int], b: list[int], length: int) -> list[int]:
    out = [0] * length
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b[: length - i]):
            out[i + j] = (out[i + j] + x * y) % MODULUS
    return out


def monomial_series_mod(indices: tuple[int, ...]) -> list[int]:
    out = [1] + [0] * (SCAN_TERMS - 1)
    for j in indices:
        out = conv_mod(out, fmod[j], SCAN_TERMS)
    return out


scan: list[dict[str, int]] = []
for weight in range(0, 9 * DEGREE + 1):
    monomials = [
        idx
        for idx in combinations_with_replacement(range(10), DEGREE)
        if sum(idx) == weight
    ]
    if len(monomials) < 2:
        continue
    series = [monomial_series_mod(idx) for idx in monomials]
    full_matrix = [[series[col][n] for col in range(len(monomials))] for n in range(SCAN_TERMS)]
    full_rank = rank_mod(full_matrix, MODULUS)
    first_full = next(
        k for k in range(1, SCAN_TERMS + 1) if rank_mod(full_matrix[:k], MODULUS) == full_rank
    )
    order_upper_bound = weight + 10 * (first_full - 1)
    scan.append(
        {
            "weight": weight,
            "monomials": len(monomials),
            "rank_mod_5003": full_rank,
            "first_full_row_count": first_full,
            "order_upper_bound": order_upper_bound,
        }
    )

best_upper = max(row["order_upper_bound"] for row in scan)
best_rows = [row for row in scan if row["order_upper_bound"] == best_upper]
assert best_upper == 438
assert [row["weight"] for row in best_rows] == [18]

# Exact reconstruction of the extremal weight-18 candidate.
WEIGHT = 18
CANCELLATIONS = 42
TERMS = 43
bq = [Fraction(1)]
for k in range(1, 451):
    bq.append(bq[-1] * Fraction(1 - 17 * (k - 1), 17 * k))


def fq(j: int, m: int) -> Fraction:
    return bq[j + 10 * m] * ((-256) ** m)


def conv_q(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * TERMS
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b[: TERMS - i]):
            out[i + j] += x * y
    return out


fseries_q = {j: [fq(j, m) for m in range(TERMS)] for j in range(10)}
monomials_q = [
    idx
    for idx in combinations_with_replacement(range(10), DEGREE)
    if sum(idx) == WEIGHT
]
assert len(monomials_q) == 43
series_q: list[list[Fraction]] = []
for idx in monomials_q:
    current = [Fraction(1)] + [Fraction(0)] * (TERMS - 1)
    for j in idx:
        current = conv_q(current, fseries_q[j])
    series_q.append(current)

rows_q: list[list[int]] = []
for n in range(CANCELLATIONS):
    values = [s[n] for s in series_q]
    row_lcm = 1
    for value in values:
        row_lcm = lcm(row_lcm, value.denominator)
    row = [value.numerator * (row_lcm // value.denominator) for value in values]
    row_gcd = reduce(gcd, (abs(x) for x in row if x), 0) or 1
    rows_q.append([x // row_gcd for x in row])

matrix_q = sp.Matrix(rows_q)
assert matrix_q.rank() == 42
nullspace = matrix_q.nullspace()
assert len(nullspace) == 1
vector = nullspace[0]
vector_lcm = 1
for entry in vector:
    vector_lcm = lcm(vector_lcm, int(entry.q))
lambda_int = [int(entry * vector_lcm) for entry in vector]
lambda_gcd = reduce(gcd, (abs(x) for x in lambda_int if x), 0) or 1
lambda_int = [x // lambda_gcd for x in lambda_int]
lead = sum((Fraction(lambda_int[j]) * series_q[j][CANCELLATIONS] for j in range(43)), Fraction(0))
assert lead != 0
assert lead.numerator % 31 != 0 and lead.denominator % 31 != 0

local_order = WEIGHT + 10 * CANCELLATIONS
assert local_order == 438
lambda_l1 = sum(abs(x) for x in lambda_int)
assert len(str(lambda_l1)) == 8818
lhs = FORCED_PRODUCT ** (local_order * 17)
rhs_17696 = 81 * (lambda_l1**17) * (10 ** (4 * 17696))
rhs_17697 = 81 * (lambda_l1**17) * (10 ** (4 * 17697))
assert lhs > rhs_17696
assert lhs < rhs_17697

print(
    json.dumps(
        {
            "checkpoint": "U89",
            "degree": DEGREE,
            "modular_scan_best_order_upper_bound": best_upper,
            "modular_scan_best_weights": [row["weight"] for row in best_rows],
            "exact_weight": WEIGHT,
            "exact_monomial_count": len(monomials_q),
            "exact_cancelled_S_coefficients": list(range(CANCELLATIONS)),
            "exact_first_nonzero_S_coefficient": CANCELLATIONS,
            "exact_local_order": local_order,
            "lambda_max_digits": max(len(str(abs(x))) for x in lambda_int),
            "lambda_l1_digits": len(str(lambda_l1)),
            "lead_31_adic_unit": True,
            "lead_mod31": [lead.numerator % 31, lead.denominator % 31],
            "degree4_max_base_strictly_greater_than_power_of_10": 17696,
            "U88_degree3_bound_remains_stronger": True,
            "full_Beal_solved": False,
        },
        indent=2,
    )
)
