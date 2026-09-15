"""Exact certificates for U68's coefficient-divisibility/height argument.

This program checks stated finite identities and domains. It does not prove
rational-point completeness or search unbounded Diophantine solutions.
"""
from __future__ import annotations

import json
from math import comb, gcd, isqrt, prod
import sympy as sp

FORCERS = (11, 31, 41, 61, 71, 101, 151, 191, 211, 281, 331, 431, 461, 631)
EXCEPTIONAL = (1, 13, 18, 33, 38, 47, 52, 67, 69, 72, 84)
Vector = tuple[int, ...]


def multiply(left: Vector, right: Vector, modulus: int) -> Vector:
    """Multiply in (Z/modulus)[rho]/(rho**5-2)."""
    if len(left) != 5 or len(right) != 5 or modulus < 2:
        raise ValueError('Expected two rank-five vectors and modulus >= 2')
    out = [0] * 5
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[(i+j) % 5] += x*y*(2 if i+j >= 5 else 1)
    return tuple(x % modulus for x in out)


def power(value: Vector, exponent: int, modulus: int) -> Vector:
    if exponent < 0:
        raise ValueError('Exponent must be nonnegative')
    out = (1, 0, 0, 0, 0)
    while exponent:
        if exponent & 1:
            out = multiply(out, value, modulus)
        value = multiply(value, value, modulus)
        exponent //= 2
    return out


def gaussian_forms(a: int, b: int, q: int) -> tuple[int, int]:
    g = sum((-1)**j*comb(17, 2*j)*pow(a, 16-2*j, q)*pow(b, 2*j, q)
            for j in range(9)) % q
    h = sum((-1)**j*comb(17, 2*j+1)*pow(a, 16-2*j, q)*pow(b, 2*j, q)
            for j in range(9)) % q
    return g, h


def projective_scan(q: int, case: int) -> list[list[int]]:
    """Full P^1(F_q), using the proved equal-weight normalization in U68."""
    ca, cb, dg, dh = ((1, 16, 1, 1), (17**4, 16, 17, 1),
                      (1, 16*17**4, 1, 17))[case-1]
    fifth = {pow(x, 5, q) for x in range(q)}
    out = []
    for aa, bb in [(1, t) for t in range(q)] + [(0, 1)]:
        a, b = ca*pow(aa, 5, q) % q, cb*pow(bb, 5, q) % q
        g, h = gaussian_forms(a, b, q)
        if (g*pow(dg, -1, q) % q in fifth and h*pow(dh, -1, q) % q in fifth):
            out.append([aa, bb])
    return out


def main() -> None:
    r, a, b, t = sp.symbols('r a b t')
    poly = sp.Poly(sp.rem((a+b*r**4)**17, r**5-2, r), r)
    c1 = 2720*a**3*b**4*(7*a**10+1144*a**5*b**5+512*b**10)
    c2 = 2720*a**4*b**3*(a**10+572*a**5*b**5+896*b**10)
    assert sp.expand(poly.nth(1)-c1) == 0
    assert sp.expand(poly.nth(2)-c2) == 0
    q1, q2 = 14*t*t+143*t+4, 4*t*t+143*t+14
    assert sp.expand(q1-q2) == 10*(t*t-1)
    assert (q1.subs(t, 1), q1.subs(t, -1)) == (161, -125)
    assert sp.gcd(q1, q2) == 1
    resultant = int(sp.resultant(q1, q2, t))
    assert resultant == -2012500

    # Exhaust all 20 affine permutations on the five roots.
    affine_types: dict[int, list[list[int]]] = {}
    for slope in range(1, 5):
        types = set()
        for translation in range(5):
            unseen = set(range(5))
            lengths = []
            while unseen:
                start = min(unseen)
                current, length = start, 0
                while current in unseen:
                    unseen.remove(current)
                    length += 1
                    current = (slope*current+translation) % 5
                lengths.append(length)
            types.add(tuple(sorted(lengths)))
        affine_types[slope] = [list(x) for x in sorted(types)]
    assert affine_types == {1: [[1, 1, 1, 1, 1], [5]], 2: [[1, 4]],
                            3: [[1, 4]], 4: [[1, 2, 2]]}
    classes = []
    for residue in range(1, 85):
        if gcd(residue, 85) != 1:
            continue
        degrees = {degree for pattern in affine_types[residue % 5] for degree in pattern}
        if any(pow(residue, degree, 17) == 1 for degree in degrees):
            classes.append(residue)
    assert tuple(classes) == EXCEPTIONAL

    # Cross-check the cycle argument against actual polynomial factorizations.
    factor_rows = []
    for q in sp.primerange(3, 2000):
        if q in (5, 17):
            continue
        factors = sp.factor_list(sp.Poly(r**5-2, r, modulus=q))[1]
        degrees = sorted(f.degree() for f, multiplicity in factors for _ in range(multiplicity))
        assert degrees in affine_types[q % 5]
        obstructs = any(pow(q, d, 17) == 1 for d in degrees)
        assert obstructs == (q % 85 in EXCEPTIONAL)
        factor_rows.append({'q': q, 'degrees': degrees, 'exceptional': obstructs})

    scans11 = [projective_scan(11, case) for case in (1, 2, 3)]
    assert scans11 == [[], [], [[1, 0]]]
    forcing = []
    for q in FORCERS:
        assert sp.isprime(q) and q % 5 == 1 and q % 17 != 1
        survivors = projective_scan(q, 3)
        assert survivors == [[1, 0]]
        assert q % 85 not in EXCEPTIONAL
        forcing.append({'q': q, 'projective_survivors': survivors})

    # A negative control: the power map really fails to be injective at q=13.
    eta = power((1, 1, 0, 0, 0), (13**4-1)//17, 13)
    assert eta != (1, 0, 0, 0, 0)
    assert any(eta[1:])
    assert power(eta, 17, 13) == (1, 0, 0, 0, 0)

    # The valuation inequalities here hold for all k>=1 by their linear form.
    binomial_valuations = []
    for j in range(1, 18):
        n, valuation = comb(17, j), 0
        while n % 17 == 0:
            n //= 17
            valuation += 1
        binomial_valuations.append(valuation)
    assert binomial_valuations == [1]*16+[0]
    assert all(1+j > 2 for j in range(2, 17)) and 17 > 2
    normalized = sp.rem((a+b*r**3)*(r/2)**17, r**5-2, r)
    assert sp.expand(normalized - (a*r**2/16384+b/8192)) == 0

    p = prod(FORCERS)
    divisor = 17*p*p
    square_bound = divisor**17
    integer_lower_bound = isqrt(square_bound)+1
    assert (integer_lower_bound-1)**2 <= square_bound < integer_lower_bound**2
    assert square_bound > 10**1028
    assert len(str(integer_lower_bound)) == 515
    exceptional_square_bound = 17**15*p**32
    assert exceptional_square_bound > 10**966

    summary = {
        'exceptional_classes_mod85': classes,
        'forced_product': str(p), 'coefficient_divisor': str(divisor),
        'integer_lower_bound': str(integer_lower_bound),
        'lower_bound_digits': len(str(integer_lower_bound)),
        'base_gt_10_to_514': True, 'exceptional_part_gt_10_to_483': True,
        'sparsity_resultant': resultant, 'q13_nontrivial_kernel': list(eta),
        'q11_case_nonempty': [bool(x) for x in scans11],
        'forcing_primes': list(FORCERS),
    }
    print(json.dumps({'checkpoint': 'U68', 'full_Beal_solved': False,
                      'summary': summary, 'forcing_scans': forcing,
                      'affine_cycle_types': affine_types,
                      'factorization_domain': 'all primes 3<=q<2000 except 5,17',
                      'factorization_rows': factor_rows,
                      'binomial_17_valuations': binomial_valuations}, indent=2))


if __name__ == '__main__':
    main()
