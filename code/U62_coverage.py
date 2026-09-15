"""Exact upstream certificates for the coefficient-two branch.

Finite-field domains are complete residue algebras, not selected square classes.
The manuscript, not these tests alone, supplies the infinite implication proof.
"""
from __future__ import annotations

import json
from math import gcd
from typing import TypeAlias

import sympy as sp

Pair: TypeAlias = tuple[int, int]


def multiply(x: Pair, y: Pair, relation: Pair, modulus: int) -> Pair:
    """Multiply in (Z/modulus)[w]/(w^2-relation[1]w-relation[0])."""
    a, b = x
    c, d = y
    c0, c1 = relation
    return ((a*c+c0*b*d) % modulus, (a*d+b*c+c1*b*d) % modulus)


def power17(x: Pair, relation: Pair, modulus: int) -> Pair:
    # Repeated multiplication deliberately differs from the TypeScript binary power.
    result = (1, 0)
    for _ in range(17):
        result = multiply(result, x, relation, modulus)
    return result


def h(m: int, n: int, modulus: int) -> Pair:
    return ((m**4+30*m*m*n*n+n**4) % modulus, -16*m*m*n*n % modulus)


def norm(x: Pair, relation: Pair, modulus: int) -> int:
    a, b = x
    c0, c1 = relation
    return (a*a+c1*a*b-c0*b*b) % modulus


def sieve(q: int, classes: tuple[int, ...]) -> dict[str, object]:
    gauss, golden = (-1, 0), (1, 1)
    # Exactly q^2 inputs to each map, including both zero coordinates and zero divisors.
    gi = {power17((a, b), gauss, q) for a in range(q) for b in range(q)}
    ai = {power17((a, b), golden, q) for a in range(q) for b in range(q)}
    gi.remove((0, 0))  # The only exclusion: simultaneous zero, impossible for gcd(m,n)=1.
    unit = (1, 0)
    rows = []
    for k in range(17):
        if k in classes:
            targets = {multiply(unit, z, golden, q) for z in ai}
            kept = sorted(z for z in gi if h(*z, q) in targets)
            rows.append({
                'k': k,
                'compatible_count': len(kept),
                'axis_count': sum(m*n % q == 0 for m, n in kept),
                'diagonal_count': sum((m-n)*(m+n) % q == 0 for m, n in kept),
                'zero_norm_gaussian_survivors': sum(norm(z, gauss, q) == 0 for z in kept),
                'sample': [list(z) for z in kept[:4]],
            })
        unit = multiply(unit, (0, 1), golden, q)
    return {
        'q': q, 'inputs_each_algebra': q*q,
        'nonzero_gaussian_image_size': len(gi), 'quadratic_image_size': len(ai),
        'nonzero_zero_norm_gaussian_images': sum(norm(z, gauss, q) == 0 for z in gi),
        'rows': rows,
    }


def algebra() -> dict[str, object]:
    x, y, a, b, m, n, u, v = sp.symbols('x y a b m n u v')
    phi = a**4-a**3*b+a*a*b*b-a*b**3+b**4
    h0, h1 = m**4+30*m*m*n*n+n**4, -16*m*m*n*n
    octic = m**8+44*m**6*n*n+166*m**4*n**4+44*m*m*n**6+n**8
    checks = {
        'rational_factorization': sp.expand((a+b)*phi-a**5-b**5) == 0,
        'phi_mod_sum': sp.rem(phi, a+b, a) == 5*b**4,
        'phi_mod5': sp.Poly(phi-(a+b)**4, a, b, modulus=5).is_zero,
        'square_substitution': sp.expand(phi.subs({a:(m+n)**2, b:(m-n)**2})-octic) == 0,
        'quadratic_norm': sp.expand(h0*h0+h0*h1-h1*h1-octic) == 0,
        'h0_at_m_zero': h0.subs(m,0) == n**4,
        'h0_at_n_zero': h0.subs(n,0) == m**4,
        'pythagorean_hypotenuse': sp.expand(((v+u)/2)**2+((v-u)/2)**2-(u*u+v*v)/2) == 0,
        'pythagorean_odd_leg': sp.expand(((v+u)/2)**2-((v-u)/2)**2-u*v) == 0,
        'quartic_conjugate_difference': sp.expand((h0+h1*(1+sp.sqrt(5))/2)-(h0+h1*(1-sp.sqrt(5))/2)+16*sp.sqrt(5)*m*m*n*n) == 0,
    }
    assert all(checks.values()), checks
    # Boundary/signed-input diagnostics for the proved content lemma.
    tested = 0
    for mm in range(-12, 13):
        for nn in range(-12, 13):
            if gcd(mm, nn) != 1 or (mm-nn) % 2 == 0:
                continue
            assert gcd(mm**4+30*mm*mm*nn*nn+nn**4, -16*mm*mm*nn*nn) == 1
            tested += 1
    return {'identities': checks, 'content_lemma_diagnostic_pairs': tested,
            'diagnostic_not_infinite_proof': True}


def main() -> None:
    first = sieve(67, tuple(range(17)))
    second = sieve(409, (0, 15))
    active = [row['k'] for row in first['rows'] if row['compatible_count']]
    assert active == [0, 15]
    assert [(row['compatible_count'], row['axis_count'], row['diagonal_count'])
            for row in first['rows'] if row['compatible_count']] == [(132,132,0),(132,0,132)]
    assert [(row['compatible_count'], row['axis_count']) for row in second['rows']] == [(48,48),(0,0)]
    assert first['nonzero_gaussian_image_size'] == 264
    assert second['nonzero_gaussian_image_size'] == 624
    assert second['nonzero_zero_norm_gaussian_images'] == 48
    print(json.dumps({'status':'completed','arithmetic':'Python exact integers and SymPy',
                      'algebra':algebra(),'unit_sieves':[first,second],
                      'full_Beal_solved':False}, indent=2))


if __name__ == '__main__':
    main()
