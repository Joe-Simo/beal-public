"""Exact certificates for U65. No unbounded Diophantine search is performed."""
from __future__ import annotations

import json
from itertools import product
import sympy as sp
from sympy.polys.numberfields import round_two

P = 17
MOD = P * P
Vector = tuple[int, ...]


def mul(a: Vector, b: Vector, polynomial: Vector, modulus: int) -> Vector:
    """Multiply in (Z/modulus)[t]/polynomial; the polynomial is monic."""
    d = len(polynomial) - 1
    assert polynomial[-1] == 1 and len(a) == len(b) == d
    c = [0] * (2 * d - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    for k in range(len(c) - 1, d - 1, -1):
        for j in range(d):
            c[k - d + j] -= c[k] * polynomial[j]
    return tuple(x % modulus for x in c[:d])


def power(a: Vector, n: int, polynomial: Vector, modulus: int) -> Vector:
    assert n >= 0
    out = (1,) + (0,) * (len(a) - 1)
    while n:
        if n & 1:
            out = mul(out, a, polynomial, modulus)
        a = mul(a, a, polynomial, modulus)
        n //= 2
    return out


def logarithm(a: Vector, polynomial: Vector) -> Vector:
    """Fermat quotient of a unit in the unramified degree-four algebra."""
    z = power(a, P**4 - 1, polynomial, MOD)
    diff = ((z[0] - 1) % MOD,) + z[1:]
    assert all(v % P == 0 for v in diff), ('nonunit or wrong algebra', a, z)
    return tuple(v // P for v in diff)


def scalar_log(a: int) -> int:
    assert a % P != 0
    z = (pow(a, P - 1, MOD) - 1) % MOD
    assert z % P == 0
    return z // P


def primitive_17th_root(q: int, chosen: int) -> dict[int, int]:
    assert sp.isprime(q) and (q - 1) % P == 0
    assert chosen % q != 1 and pow(chosen, P, q) == 1
    logs = {pow(chosen, j, q): j for j in range(P)}
    assert len(logs) == P
    return logs


def residue_sieve() -> dict[str, object]:
    """All square/twice-square pairs mod 289; no projective normalization."""
    r = next(t for t in range(MOD) if pow(t, 5, MOD) == 2)
    assert r == 49
    quartic = tuple(pow(r, 4 - j, MOD) for j in range(4)) + (1,)
    t = sp.Symbol('t')
    poly17 = sp.Poly(sum(quartic[j] * t**j for j in range(5)), t, modulus=P)
    assert poly17.is_irreducible
    e1 = (-1, 1, 0, 0)
    e2 = (1, 1, 0, 1)
    l1, l2 = logarithm(e1, quartic), logarithm(e2, quartic)
    classes: dict[Vector, tuple[int, int]] = {}
    for a, b in product(range(P), repeat=2):
        key = tuple((a*x + b*y) % P for x, y in zip(l1, l2))
        assert key not in classes
        classes[key] = (a, b)
    assert len(classes) == 289
    linear_logs = (scalar_log(r-1), scalar_log(r**3+r+1))
    roots_x: dict[int, list[int]] = {}
    roots_y: dict[int, list[int]] = {}
    for a in range(MOD):
        roots_x.setdefault(a*a % MOD, []).append(a)
        roots_y.setdefault(2*a*a % MOD, []).append(a)
    scalar_images = {pow(a, P, MOD) for a in range(MOD)}
    assert len(scalar_images) == P
    sqrt_minus_one = 38
    assert sqrt_minus_one**2 % MOD == MOD-1
    assert (2*sqrt_minus_one) % P != 0
    norm_survivors = 0
    quartic_survivors = 0
    rows: list[dict[str, object]] = []
    gaussian_total = 0
    for u in sorted(roots_x):
        for v in sorted(roots_y):
            if u % P == v % P == 0:
                continue
            if (pow(u, 5, MOD) + 8*pow(v, 5, MOD)) % MOD not in scalar_images:
                continue
            norm_survivors += 1
            key = logarithm((u, 0, 0, v), quartic)
            if key not in classes:
                continue
            quartic_survivors += 1
            a, b = classes[key]
            gamma = (u + pow(r, 3, MOD)*v) % MOD
            if gamma % P:
                if scalar_log(gamma) != (a*linear_logs[0]+b*linear_logs[1]) % P:
                    continue
            elif gamma != 0:
                continue  # A nonunit seventeenth power must vanish modulo 17^2.
            witnesses = []
            for x in roots_x[u]:
                for y in roots_y[v]:
                    re, im = pow(x, 5, MOD), 16*pow(y, 5, MOD) % MOD
                    if ((re + sqrt_minus_one*im) % MOD in scalar_images and
                            (re - sqrt_minus_one*im) % MOD in scalar_images):
                        witnesses.append([x, y])
            gaussian_total += len(witnesses)
            rows.append({'a': a, 'b': b, 'U': u, 'V': v,
                         'gaussian_witnesses': witnesses})
    before = sorted({(int(row['a']), int(row['b'])) for row in rows})
    after = sorted({(int(row['a']), int(row['b'])) for row in rows
                    if row['gaussian_witnesses']})
    assert norm_survivors == 1104 and quartic_survivors == 24
    assert len(rows) == 24 and before == [(0, 0), (0, 14)]
    assert after == [(0, 0)] and gaussian_total == 544
    assert all((row['U'] == 0) != (row['V'] == 0)
               for row in rows if row['gaussian_witnesses'])
    return {'modulus': MOD, 'linear_root': r, 'quartic': list(quartic),
            'quartic_unit_logs': [list(l1), list(l2)],
            'linear_unit_logs': list(linear_logs),
            'unit_log_image_size': len(classes),
            'square_parameter_pairs': len(roots_x)*len(roots_y)-1,
            'norm_17th_power_pairs': norm_survivors,
            'quartic_log_pairs': quartic_survivors,
            'two_component_pairs': len(rows),
            'classes_before_gaussian': [list(c) for c in before],
            'classes_after_gaussian': [list(c) for c in after],
            'gaussian_parameter_pairs': sum(bool(r['gaussian_witnesses']) for r in rows),
            'gaussian_root_pairs': gaussian_total, 'rows': rows}


def main() -> None:
    t, e, u, v, r = sp.symbols('t e u v r')
    defining = r**5-2
    assert power((0, 1, 0, 0, 0), 17**4, (-2, 0, 0, 0, 0, 1), 17) == (0, 1, 0, 0, 0)
    assert power((0, 0), 0, (1, 0, 1), 289) == (1, 0)
    assert sp.resultant(defining, 2**60+r, r) == (2**60)**5+2
    h = e**4-10*e**3-13*e**2+190*e+241
    n = -2*e**3+15*e**2+18*e+120
    assert sp.rem(n*n-5*91*n+5*91**2, h, e) == 0
    qh = t*t-5*t+5
    htests = []
    for s, p in [(-3, -9), (1, -1), (9, 19)]:
        other = t*t-s*t+p
        result = int(sp.resultant(qh, other, t))
        gcd = sp.gcd(sp.Poly(qh, t, modulus=17), sp.Poly(other, t, modulus=17))
        assert gcd.degree() == 0 and result % 17 != 0
        a, b, g = sp.gcdex(sp.Poly(qh, t, modulus=17), sp.Poly(other, t, modulus=17))
        assert g.as_expr() == 1
        htests.append({'S': s, 'P': p, 'resultant': result,
                       'bezout_h': str(a.as_expr()), 'bezout_frey': str(b.as_expr())})
    frey = t**5+40*u*v*t**3+320*u*u*v*v*t+64*(8*v**5-u**5)
    root = 2*r*u-2*r**4*v
    assert sp.rem(sp.expand(frey.subs(t, root)), defining, r) == 0
    assert sp.expand(sp.resultant(defining, t-root, r)-frey) == 0
    norm = sp.resultant(defining, u+r**3*v, r)
    assert sp.expand(norm-u**5-8*v**5) == 0
    matrix = sp.Matrix([[sp.Poly(sp.rem(root**j, defining, r), r).nth(i)
                         for j in range(5)] for i in range(5)])
    assert sp.factor(matrix.det()) == 1024*(u**5+8*v**5)**2
    disc = sp.discriminant(frey, t)
    assert sp.factor(disc) == 2**24*5**5*(u**5+8*v**5)**4
    zk, field_disc = round_two(sp.Poly(defining, r))
    assert field_disc == 50000
    norm_generators = [r, 1+r, 1+r*r, 1+r+r*r, 1+r**3-r**4]
    norms = [int(sp.resultant(defining, a, r)) for a in norm_generators]
    assert norms == [2, 3, 5, 7, 13]
    unit_norms = [int(sp.resultant(defining, a, r)) for a in [r-1, r**3+r+1]]
    assert unit_norms == [1, 1]
    # An exact, deliberately loose bound <16 suffices; no float decides coverage.
    minkowski_upper = sp.Rational(120, 3125)*sp.Rational(16, 9)*224
    assert minkowski_upper < 16
    factor_records = []
    for p, root_p in [(3, 2), (7, 4), (13, 6)]:
        cofactor = sp.div(sp.Poly(defining, r, modulus=p),
                         sp.Poly(r-root_p, r, modulus=p))[0]
        assert cofactor.degree() == 4 and cofactor.is_irreducible
        factor_records.append({'p': p, 'linear_root': root_p,
                               'irreducible_cofactor': str(cofactor.as_expr())})
    assert sp.Poly(defining, r, modulus=11).is_irreducible
    chars = []
    for p, rr, gen in [(103, 17, 64), (137, 9, 119)]:
        assert pow(rr, 5, p) == 2
        logs = primitive_17th_root(p, gen)
        values = [pow(z, (p-1)//17, p) for z in [rr-1, rr**3+rr+1]]
        row = [logs[z] for z in values]
        chars.append({'p': p, 'root': rr, 'generator': gen,
                      'values': values, 'logs': row})
    rows = [c['logs'] for c in chars]
    determinant = (rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0]) % 17
    assert determinant == 4
    # The affine action on the five roots is faithful, including the boundary.
    permutations = {tuple((a*j+b) % 5 for j in range(5))
                    for a in range(1, 5) for b in range(5)}
    assert len(permutations) == 20
    out = {'checkpoint': 'U65', 'status': 'completed', 'full_Beal_solved': False,
           'h_exclusion': htests,
           'identities': {'root': True, 'root_polynomial': True, 'norm': True,
                          'index_determinant': True, 'discriminant': True},
           'quintic_field': {'discriminant': int(field_disc), 'integer_basis': str(zk),
                             'norm_generators': [str(a) for a in norm_generators],
                             'generator_norms': norms, 'unit_norms': unit_norms,
                             'minkowski_upper': str(minkowski_upper),
                             'prime_factorizations': factor_records,
                             'polynomial_irreducible_mod11': True,
                             'affine_permutations': len(permutations)},
           'unit_basis_characters': chars, 'unit_basis_determinant_mod17': determinant,
           'sieve': residue_sieve()}
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
