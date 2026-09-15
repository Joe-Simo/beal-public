"""Exact U79 dyadic-image certificates, modulo 8 in a rank-34 integer ring.

A finite certificate is not a standalone proof of Kummer membership. The
manuscript constructs local divisors, derives their norm series, and proves
that congruence modulo s^35 preserves squareclasses.
"""
from __future__ import annotations

import json
from math import comb
from pathlib import Path
from random import Random
from typing import TypeAlias

Vector: TypeAlias = tuple[int, ...]
Pair: TypeAlias = tuple[int, int]
ROOT = Path(__file__).resolve().parents[1]


class LocalRing:
    """(Z/2^m)[phi,s]/(phi^2-phi-1, s^17-2phi+2)."""

    def __init__(self, bits: int = 3) -> None:
        if bits < 3:
            raise ValueError('At least 3 binary digits are required')
        self.bits = bits
        self.modulus = 1 << bits
        self.zero = (0,) * 34
        self.one = (1,) + (0,) * 33
        self.inverse_cache: dict[tuple[int, Pair, bool], Vector] = {}

    @staticmethod
    def pair_mul(a: Pair, b: Pair, modulus: int) -> Pair:
        return ((a[0]*b[0]+a[1]*b[1]) % modulus,
                (a[0]*b[1]+a[1]*b[0]+a[1]*b[1]) % modulus)

    def add(self, a: Vector, b: Vector) -> Vector:
        return tuple((x+y) % self.modulus for x, y in zip(a, b, strict=True))

    def scale(self, a: Vector, coefficient: int) -> Vector:
        return tuple(x*coefficient % self.modulus for x in a)

    def multiply(self, a: Vector, b: Vector) -> Vector:
        if len(a) != 34 or len(b) != 34:
            raise ValueError('Expected rank-34 coefficient vectors')
        c = [0]*66
        for i, x in enumerate(a):
            if x == 0:
                continue
            si, pi = divmod(i, 2)
            for j, y in enumerate(b):
                if y == 0:
                    continue
                sj, pj = divmod(j, 2)
                k = 2*(si+sj)
                if pi+pj == 2:
                    c[k] += x*y
                    c[k+1] += x*y
                else:
                    c[k+pi+pj] += x*y
        for k in range(32, 16, -1):
            x, y = c[2*k:2*k+2]
            c[2*(k-17)] += -2*x+2*y
            c[2*(k-17)+1] += 2*x
        return tuple(x % self.modulus for x in c[:34])

    def monomial(self, exponent: int, pair: Pair = (1, 0)) -> Vector:
        if exponent < 0:
            raise ValueError('Negative integral monomial exponent')
        quotient, remainder = divmod(exponent, 17)
        value = pair
        for _ in range(quotient):
            value = self.pair_mul(value, (-2, 2), self.modulus)
        out = [0]*34
        out[2*remainder:2*remainder+2] = value
        return tuple(out)

    def valuation(self, a: Vector) -> int:
        """Valuation truncated at 17*bits; no floating-point logarithm."""
        answer = 17*self.bits
        for j in range(17):
            for x in a[2*j:2*j+2]:
                if x:
                    two_valuation = (x & -x).bit_length()-1
                    answer = min(answer, j+17*two_valuation)
        return answer

    def inverse_principal_unit(self, a: Vector) -> Vector:
        z = self.add(a, self.scale(self.one, -1))
        depth = self.valuation(z)
        if depth < 1:
            raise ValueError('Expected a unit congruent to 1 modulo s')
        out = self.one
        term = self.one
        for _ in range(1, (17*self.bits-1)//depth+1):
            term = self.multiply(term, self.scale(z, -1))
            out = self.add(out, term)
        assert self.multiply(a, out) == self.one
        return out

    def inverse_factor(self, n: int, pair: Pair, square: bool = False) -> Vector:
        key = n, pair, square
        if key not in self.inverse_cache:
            a = self.add(self.one, self.monomial(n, pair))
            inverse = self.inverse_principal_unit(a)
            self.inverse_cache[key] = self.multiply(inverse, inverse) if square else inverse
        return self.inverse_cache[key]

    def leading(self, a: Vector, depth: int) -> Pair:
        quotient, remainder = divmod(depth, 17)
        x, y = a[2*remainder:2*remainder+2]
        assert x % (1 << quotient) == y % (1 << quotient) == 0
        coefficient: Pair = ((x >> quotient) % 2, (y >> quotient) % 2)
        # 2=phi*s^17, so division by s^(17q) multiplies this residue by phi^q.
        for _ in range(quotient):
            coefficient = self.pair_mul(coefficient, (0, 1), 2)
        return coefficient

    def squareclass(self, initial: Vector) -> tuple[int, list[list[int]], Vector]:
        """Principal unit normal form: 34 odd-grade bits and one top bit.

        Valuation and nontrivial residue factors must be normalized before
        calling this function. All constructed witnesses already have residue 1.
        """
        a = initial
        assert self.valuation(self.add(a, self.scale(self.one, -1))) >= 1
        code = 0
        corrections: list[list[int]] = []
        for depth in range(1, 34):
            pair = self.leading(self.add(a, self.scale(self.one, -1)), depth)
            if pair == (0, 0):
                continue
            if depth % 2 == 0:
                root = self.pair_mul(pair, pair, 2)
                a = self.multiply(a, self.inverse_factor(depth//2, root, True))
                corrections.append([depth//2, root[0], root[1]])
            else:
                for bit, on in enumerate(pair):
                    if on:
                        code ^= 1 << (depth-1+bit)
                        b: Pair = (1, 0) if bit == 0 else (0, 1)
                        a = self.multiply(a, self.inverse_factor(depth, b))
            assert self.valuation(self.add(a, self.scale(self.one, -1))) > depth
        pair = self.leading(self.add(a, self.scale(self.one, -1)), 34)
        # Square leading terms at level 34 form phi^2*(z^2+z), z in F4.
        # Trace_F4/F2(b/phi^2) is the coefficient of phi in b*phi.
        top = self.pair_mul(pair, (0, 1), 2)[1]
        if top:
            code ^= 1 << 34
        return code, corrections, a


def logarithmic_numerator(n: int) -> int:
    """n*[q^n] log(H(q)+q), by the proved Lagrange-inversion formula."""
    answer = sum(comb(n, j)*(-1)**(n-1-17*j)
                 for j in range((n-1)//17+1))
    if n % 17 == 0:
        answer -= 17*comb(n-1, (n-17)//17)
    return answer


def norm_series(d: int, degree: int) -> list[int]:
    coefficients = [1]
    for n in range(1, degree+1):
        numerator = sum(logarithmic_numerator(d*j)*coefficients[n-j]
                        for j in range(1, n+1))
        assert numerator % n == 0
        coefficients.append(numerator//n)
    return coefficients


def witness(ring: LocalRing, d: int, parameter: str) -> tuple[Vector, list[int]]:
    depth = 34-2*d
    coefficient: Pair = (1, 1)  # phi^2
    for _ in range(d):
        coefficient = ring.pair_mul(coefficient, (3, -1), ring.modulus)
    if parameter == 'phi':
        coefficient = ring.pair_mul(coefficient, (2, -1), ring.modulus)
    elif parameter != '1':
        raise ValueError('Unsupported parameter')
    series = norm_series(d, (17*ring.bits-1)//depth)
    t = ring.monomial(depth, coefficient)
    term = ring.one
    result = ring.zero
    for c in series:
        result = ring.add(result, ring.scale(term, c))
        term = ring.multiply(term, t)
    assert ring.valuation(term) >= 17*ring.bits
    return result, series


def binary_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for row in rows:
        while row:
            pivot = row.bit_length()-1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def basis_product(ring: LocalRing, code: int) -> Vector:
    out = ring.one
    for n in range(1, 34, 2):
        for bit, pair in enumerate(((1, 0), (0, 1))):
            if (code >> (n-1+bit)) & 1:
                out = ring.multiply(out, ring.add(ring.one, ring.monomial(n, pair)))
    if code >> 34:
        out = ring.multiply(out, ring.add(ring.one, ring.monomial(34)))
    return out


def base_square_cosets() -> int:
    """Norms of the remaining grade-17/top unit generators are independent."""
    mul = lambda a, b: LocalRing.pair_mul(a, b, 8)
    units = [(a, b) for a in range(8) for b in range(8) if (a % 2, b % 2) != (0, 0)]
    squares = {mul(a, a) for a in units}
    assert len(units) == 48 and len(squares) == 6
    c = (-2, 2)
    c2 = mul(c, c)
    # (1+s^17), (1+phi*s^17), (1+s^34) are scalar elements of E.
    generators = [((1+c[0]) % 8, c[1] % 8), (3, 0), ((1+c2[0]) % 8, c2[1])]
    cosets = set()
    for code in range(8):
        a: Pair = (1, 0)
        for i, g in enumerate(generators):
            if code >> i & 1:
                a = mul(a, g)
        cosets.add(tuple(sorted(mul(a, b) for b in squares)))
    assert len(cosets) == 8
    return len(cosets)


def main() -> None:
    ring = LocalRing()
    high_mask = ((1 << 16)-1) << 18
    rows = []
    codes = []
    for d in range(1, 16, 2):
        for parameter in ('1', 'phi'):
            a, series = witness(ring, d, parameter)
            code, corrections, residual = ring.squareclass(a)
            assert code & ~high_mask == 0
            assert ring.valuation(ring.add(residual, ring.scale(ring.one, -1))) >= 35
            square_factor = ring.one
            for n, b0, b1 in corrections:
                square_factor = ring.multiply(square_factor,
                    ring.add(ring.one, ring.monomial(n, (b0, b1))))
            product = ring.multiply(basis_product(ring, code),
                                    ring.multiply(square_factor, square_factor))
            congruence_depth = ring.valuation(ring.add(a, ring.scale(product, -1)))
            assert congruence_depth >= 35
            # Higher-precision arithmetic must not change any squareclass.
            higher, _ = witness(LocalRing(4), d, parameter)
            assert LocalRing(4).squareclass(higher)[0] == code
            codes.append(code >> 18)
            rows.append({'d': d, 'parameter': parameter,
                         't_depth': 34-2*d, 'norm_polynomial': list(map(str, series)),
                         'unit_mod8': list(a), 'high_basis_code': code >> 18,
                         'square_corrections': corrections,
                         'square_congruence_depth_at_least': min(congruence_depth, 35)})
    assert binary_rank(codes) == 16
    # Complete 35-generator unit normal form, with negative controls.
    for i in range(35):
        a = basis_product(ring, 1 << i)
        assert ring.squareclass(a)[0] == 1 << i
        assert ring.squareclass(ring.multiply(a, a))[0] == 0
    rng = Random(79)
    for _ in range(32):
        a, b = rng.getrandbits(35), rng.getrandbits(35)
        product = ring.multiply(basis_product(ring, a), basis_product(ring, b))
        assert ring.squareclass(product)[0] == a ^ b
    alpha = ring.multiply(ring.add(ring.one, ring.monomial(1)),
                          ring.inverse_principal_unit(ring.add(ring.one, ring.monomial(17))))
    alpha_code = ring.squareclass(alpha)[0]
    assert alpha_code == 65537 and alpha_code & 65535 == 1
    output = {'checkpoint': 'U79', 'summary': {
        'dyadic_Kummer_dimension': 16,
        'dyadic_basis': ['1+s^n', '1+phi*s^n'],
        'basis_exponents': list(range(19, 34, 2)),
        'witness_count': 16, 'witness_matrix_rank': 16,
        'high_basis_codes_by_d': [codes[i:i+2] for i in range(0, 16, 2)],
        'precision': 'modulo 8, congruence modulo s^35; v_s(2)=17',
        'higher_precision_codes_identical': True,
        'base_norm_cosets': base_square_cosets(),
        'restriction_coordinates': '16 bits at odd depths 1,3,...,15',
        'alpha_global_candidate': '(s+1)/(1+s^17)=1/h(s)',
        'alpha_squareclass_code': alpha_code, 'alpha_low16_code': 1,
        'alpha_passes_at5': True, 'alpha_fails_at2': True,
        'class_group_2_rank_computed': False,
        'global_candidate_basis_computed': False,
        'global_restriction_matrix_computed': False,
        'numerical_rank_upper_bound_computed': False,
        'full_Beal_solved': False}, 'witnesses': rows}
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
