"""U91 mixed degree-four Padé audit for the weighted Beal branch.

The finite-field scan certifies exact upper bounds on cancellation order because a
nonzero minor modulo 5003 is a nonzero integer minor.  The exact rational part
then reconstructs one 58-term mixed-weight relation (weights 8 and 18) and
checks its actual height tradeoff.  Nothing here proves the weighted equation
or Beal's conjecture.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import combinations_with_replacement
from math import gcd, lcm
import json
import sys

from sympy import ZZ
from sympy.polys.matrices import DomainMatrix

sys.set_int_max_str_digits(1_000_000)

MOD = 5003
DEGREE = 4
FORCED_PRODUCT = 433992707035920672833426144791


def modular_binomials(limit: int) -> list[int]:
    out = [1]
    for k in range(1, limit + 1):
        out.append(
            out[-1]
            * ((1 - 17 * (k - 1)) % MOD)
            * pow((17 * k) % MOD, -1, MOD)
            % MOD
        )
    return out


MB = modular_binomials(900)


def mod_f(j: int, m: int) -> int:
    return MB[j + 10 * m] * pow(-256, m, MOD) % MOD


def mod_conv(a: list[int], b: list[int], length: int) -> list[int]:
    out = [0] * length
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b[: length - i]):
            if y:
                out[i + j] = (out[i + j] + x * y) % MOD
    return out


def mod_base_series(indices: tuple[int, ...], length: int) -> list[int]:
    out = [1] + [0] * (length - 1)
    for j in indices:
        out = mod_conv(out, [mod_f(j, m) for m in range(length)], length)
    return out


def first_full_row_count(series: list[list[int]]) -> int:
    columns = len(series)
    pivots: dict[int, list[int]] = {}
    rank = 0
    for row_index in range(len(series[0])):
        row = [s[row_index] for s in series]
        for column in sorted(pivots):
            if row[column]:
                pivot = pivots[column]
                factor = row[column] * pow(pivot[column], -1, MOD) % MOD
                row = [
                    (row[j] - factor * pivot[j]) % MOD for j in range(columns)
                ]
        first = next((j for j, x in enumerate(row) if x), None)
        if first is not None:
            pivots[first] = row
            rank += 1
            if rank == columns:
                return row_index + 1
    raise AssertionError("modular scan did not reach full column rank")


ALL = list(combinations_with_replacement(range(10), DEGREE))
assert len(ALL) == 715
counts = Counter(sum(m) % 10 for m in ALL)
assert counts == Counter({0: 73, 2: 73, 4: 73, 6: 73, 8: 73,
                          1: 70, 3: 70, 5: 70, 7: 70, 9: 70})

scan: list[dict[str, int]] = []
for residue in range(10):
    monomials = [m for m in ALL if sum(m) % 10 == residue]
    columns = len(monomials)
    length = columns + 3
    shifted: list[list[int]] = []
    for indices in monomials:
        shift = (sum(indices) - residue) // 10
        base = mod_base_series(indices, length)
        shifted.append(([0] * shift + base)[:length])
    full_rows = first_full_row_count(shifted)
    assert full_rows == columns
    max_local_order = residue + 10 * (columns - 1)
    scan.append(
        {
            "residue": residue,
            "monomials": columns,
            "first_full_row_count_mod_5003": full_rows,
            "max_possible_local_order": max_local_order,
        }
    )

assert max(row["max_possible_local_order"] for row in scan) == 728
assert [row for row in scan if row["max_possible_local_order"] == 728][0]["residue"] == 8


# Exact 58-term mixed subspace: all residue-8 monomials of actual weights 8 or 18.
TERMS = 59
exact_limit = 9 + 10 * (TERMS - 1)
B = [Fraction(1)]
for k in range(1, exact_limit + 1):
    B.append(B[-1] * Fraction(1 - 17 * (k - 1), 17 * k))


def exact_f(j: int, m: int) -> Fraction:
    return B[j + 10 * m] * ((-256) ** m)


def exact_conv(a: list[Fraction], b: list[Fraction], length: int) -> list[Fraction]:
    out = [Fraction(0)] * length
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b[: length - i]):
            if y:
                out[i + j] += x * y
    return out


def exact_base_series(indices: tuple[int, ...], length: int) -> list[Fraction]:
    out = [Fraction(1)] + [Fraction(0)] * (length - 1)
    for j in indices:
        out = exact_conv(out, [exact_f(j, m) for m in range(length)], length)
    return out


residue8 = [m for m in ALL if sum(m) % 10 == 8]
subset = [m for m in residue8 if sum(m) in (8, 18)]
assert Counter(map(sum, residue8)) == Counter({18: 43, 8: 15, 28: 15})
assert len(subset) == 58

exact_series: list[list[Fraction]] = []
for indices in subset:
    shift = (sum(indices) - 8) // 10
    base = exact_base_series(indices, TERMS)
    exact_series.append(([Fraction(0)] * shift + base)[:TERMS])

rows: list[list[int]] = []
for n in range(57):
    values = [s[n] for s in exact_series]
    row_lcm = 1
    for value in values:
        row_lcm = lcm(row_lcm, value.denominator)
    row = [value.numerator * (row_lcm // value.denominator) for value in values]
    row_gcd = reduce(gcd, (abs(x) for x in row if x), 0) or 1
    rows.append([x // row_gcd for x in row])

nullspace = DomainMatrix.from_list(rows, ZZ).nullspace().to_list()
assert len(nullspace) == 1
relation = [int(x) for x in nullspace[0]]
relation_gcd = reduce(gcd, (abs(x) for x in relation if x), 0) or 1
relation = [x // relation_gcd for x in relation]
if relation[-1] < 0:
    relation = [-x for x in relation]

assert all(
    sum(relation[j] * rows[n][j] for j in range(len(subset))) == 0
    for n in range(57)
)
lead = sum(
    (Fraction(relation[j]) * exact_series[j][57] for j in range(len(subset))),
    Fraction(0),
)
assert lead != 0
assert lead.numerator % 31 == 10
assert lead.denominator % 31 == 25

local_order = 8 + 10 * 57
assert local_order == 578
l1 = sum(abs(x) for x in relation)
max_digits = max(len(str(abs(x))) for x in relation)
assert len(str(l1)) == 15884
assert max_digits == 15884

lhs = FORCED_PRODUCT ** (local_order * 17)
rhs_5297 = 81 * (l1**17) * (10 ** (4 * 5297))
rhs_5298 = 81 * (l1**17) * (10 ** (4 * 5298))
assert lhs > rhs_5297
assert lhs < rhs_5298

print(
    json.dumps(
        {
            "checkpoint": "U91",
            "degree": DEGREE,
            "all_residue_scan": scan,
            "best_modular_upper_order": 728,
            "best_residue": 8,
            "exact_partial_subspace": {
                "weights": [8, 18],
                "monomial_count": len(subset),
                "cancelled_S_coefficients": list(range(57)),
                "local_Y_order": local_order,
                "lead_mod31": [lead.numerator % 31, lead.denominator % 31],
                "lambda_l1_digits": len(str(l1)),
                "lambda_max_digits": max_digits,
                "max_base_strictly_greater_than_power_of_10": 5297,
            },
            "full_73_term_relation_reconstructed": False,
            "full_Beal_solved": False,
        },
        indent=2,
    )
)
