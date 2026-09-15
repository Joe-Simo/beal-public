"""Exact certificates for U72; finite local examples are not global solutions."""
from __future__ import annotations

from fractions import Fraction
from math import comb, factorial, prod
import json
import sympy as sp

PRIMES = (11, 31, 41, 61, 71, 101, 151, 191, 211, 281, 331, 431, 461, 631)
Vector = tuple[int, ...]


def mul(left: Vector, right: Vector, modulus: int) -> Vector:
    """Multiply in (Z/modulus)[c]/(c^10+256), in the c power basis."""
    if len(left) != 10 or len(right) != 10 or modulus < 2:
        raise ValueError('Expected rank-ten vectors and modulus at least two')
    out = [0] * 10
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[(i+j) % 10] += a*b*(-256 if i+j >= 10 else 1)
    return tuple(a % modulus for a in out)


def power(value: Vector, exponent: int, modulus: int) -> Vector:
    if exponent < 0:
        raise ValueError('Negative exponent')
    out = (1,) + (0,)*9
    while exponent:
        if exponent & 1:
            out = mul(out, value, modulus)
        value = mul(value, value, modulus)
        exponent //= 2
    return out


def valuation(n: int, p: int) -> int:
    if n == 0:
        raise ValueError('A zero residue cannot certify an exact valuation')
    n = abs(n)
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def rational_mod(a: Fraction, modulus: int) -> int:
    return a.numerator * pow(a.denominator, -1, modulus) % modulus


def series_example(p: int, e: int, precision: int, scalar: int, y_unit: int) -> dict[str, object]:
    """Truncate a proved convergent local series; TS instead performs digit lifts."""
    modulus = p**precision
    if p == 17:
        assert e >= 2
        # v17 of all omitted terms >= k*15/16, for every k >= cutoff.
        cutoff = (16*precision+14)//15+1
        assert Fraction(15*cutoff, 16) >= precision
    else:
        cutoff = precision  # binomial(1/17,k) is p-integral, and e>=1.
    z = Fraction(y_unit*p**e, scalar**17)
    bj = Fraction(1)
    current = Fraction(scalar)
    coefficients = [0] * 10
    for k in range(cutoff):
        if k:
            bj *= Fraction(1-17*(k-1), 17*k)
            current = scalar*bj*z**k
        term = current*(-256)**(k//10)
        coefficients[k % 10] = (coefficients[k % 10]+rational_mod(term, modulus)) % modulus
    root = tuple(coefficients)
    target = (pow(scalar, 17, modulus), y_unit*p**e % modulus)+(0,)*8
    assert power(root, 17, modulus) == target
    known_precision = precision-1 if p == 17 else precision
    known_modulus = p**known_precision
    root = tuple(a % known_modulus for a in root)
    values = [valuation(a, p) for a in root]
    assert max(values) < known_precision
    return {'p': p, 'e': e, 'power_precision': precision, 'root_precision': known_precision,
            'scalar_root': scalar, 'y_unit': y_unit,
            'root': [str(a) for a in root], 'valuations': values,
            'power_residual_zero': True}


def forcing_scan(p: int, case: int = 3) -> list[list[int]]:
    """Complete P^1 parameter chart; homogeneity of fifth powers justifies it."""
    ca, cb, dg, dh = ((1,16,1,1),(17**4,16,17,1),(1,16*17**4,1,17))[case-1]
    fifth = {pow(a, 5, p) for a in range(p)}
    out = []
    for A, B in [(1, b) for b in range(p)]+[(0,1)]:
        a, b = ca*pow(A,5,p) % p, cb*pow(B,5,p) % p
        ap = [pow(a,j,p) for j in range(17)]
        bp = [pow(b,j,p) for j in range(17)]
        g = sum((-1)**j*comb(17,2*j)*ap[16-2*j]*bp[2*j] for j in range(9)) % p
        h = sum((-1)**j*comb(17,2*j+1)*ap[16-2*j]*bp[2*j] for j in range(9)) % p
        if g*pow(dg,-1,p) % p in fifth and h*pow(dh,-1,p) % p in fifth:
            out.append([A,B])
    return out


def main() -> None:
    u, c = sp.symbols('u c')
    h = u**10+2*u**5+2
    i = u**5+1
    rho = u**7+u**2
    cg = -u**8-2*u**3
    assert sp.rem(i*i+1,h,u) == 0
    assert sp.rem(rho**5-2,h,u) == 0
    assert sp.rem(cg-i*rho**4,h,u) == 0
    assert sp.rem(cg**10+256,h,u) == 0
    assert sp.rem(cg**4-8*rho,h,u) == 0
    assert sp.rem(cg**5-16*i,h,u) == 0
    # Direct coordinate determinant, not a decimal discriminant comparison.
    matrix = sp.Matrix([[sp.Poly(sp.rem(cg**j,h,u),u).nth(k)
                         for j in range(10)] for k in range(10)])
    index = abs(int(matrix.det()))
    assert index == 2**34
    disc_h = int(sp.discriminant(h,u))
    disc_c = int(sp.discriminant(c**10+256,c))
    assert disc_h == -160000000000 and disc_c == disc_h*index**2
    assert sp.expand((u+2)**5-2).subs(u,0) == 30

    # Exact leading coefficients, including their only exceptional primes in P.
    bj = [Fraction(1)]
    for k in range(1,10):
        bj.append(bj[-1]*Fraction(1-17*(k-1),17*k))
    leading = [rational_mod(a*17**j,17) for j,a in enumerate(bj)]
    assert leading == [pow(factorial(j),-1,17) for j in range(10)]
    assert bj[9] == Fraction(658767450,17**9)
    q_rows = []
    forcing = []
    for p in PRIMES:
        assert sp.isprime(p) and p % 5 == 1
        degree = 5 if p % 4 == 1 else 10
        assert pow(p,degree,17) != 1
        c_residue = (0,1)+(0,)*8
        image = c_residue
        for _ in range(degree):
            image = power(image, p, p)
        assert image == c_residue
        local_valuations = [valuation(a.numerator,p)-valuation(a.denominator,p) for a in bj]
        expected = [int(p==11 and j>=3)+int(p==101 and j>=7) for j in range(10)]
        assert local_valuations == expected
        q_rows.append([p,degree,pow(p,degree,17),local_valuations])
        survivors = forcing_scan(p)
        assert survivors == [[1,0]]
        forcing.append({'p':p,'survivors':survivors})
    assert [forcing_scan(11,k) for k in (1,2,3)] == [[],[],[[1,0]]]

    examples17 = [series_example(17,e,9*(e-1)+10,1,1) for e in (2,3,4)]
    examples17.append(series_example(17,2,22,2,3))
    for row in examples17:
        e = int(row['e'])
        assert row['valuations'] == [j*(e-1) for j in range(10)]
        root = list(map(int,row['root']))
        a, v = int(row['scalar_root']), int(row['y_unit'])
        for j in range(10):
            expected = a*pow(a**17,-j,17)*pow(v,j,17)*pow(factorial(j),-1,17) % 17
            assert root[j]//17**(j*(e-1)) % 17 == expected
    examples_good = [series_example(p,1,12,2,1) for p in PRIMES]
    for row in examples_good:
        p = int(row['p'])
        assert row['valuations'] == [j+int(p==11 and j>=3)+int(p==101 and j>=7) for j in range(10)]

    examples2 = []
    for X,Y in ((1,1),(3,2),(5,7),(11,4)):
        n = 12
        m = 2**n
        target = (X,Y)+(0,)*8
        inverse_exponent = pow(17,-1,2**(10*n-1))
        root = power(target,inverse_exponent,m)
        assert power(root,17,m) == target
        examples2.append({'X':X,'Y':Y,'precision':n,'root':[str(a) for a in root]})

    P = prod(PRIMES)
    D = 11*101*(17*P)**9
    numerator = 16**153*D**85
    # Large integers are compared directly: no string-limit change or log rounding.
    assert numerator > 243*10**(5*4810)
    assert numerator < 243*10**(5*4811)
    summary = {'power_order_index':str(index),'field_discriminant':str(disc_h),
               'power_order_discriminant':str(disc_c),
               'ninth_binomial':[str(bj[9].numerator),str(bj[9].denominator)],
               'forcing_prime_rows':q_rows,'forced_product':str(P),
               'ninth_coefficient_divisor':str(D),'base_bound_decimal_exponent':4810,
               'full_support_17_profiles':[row['valuations'] for row in examples17],
               'all_local_examples_pass':True,'full_Beal_solved':False}
    print(json.dumps({'checkpoint':'U72','summary':summary,'forcing_scans':forcing,
                      'examples17':examples17,'examples_good':examples_good,
                      'examples2':examples2},indent=2))


if __name__ == '__main__':
    main()
