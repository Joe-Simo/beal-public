"""Exact U73 identities and local examples, not a global point classifier.

Python constructs roots by a convergent binomial series and computes their
cyclotomic products in a rank-40 algebra. The separate TypeScript checker
uses digit lifting and a rank-20 trace recurrence instead.
"""
from __future__ import annotations

from fractions import Fraction
import json
import sympy as sp

Vector = tuple[int, ...]


def mul10(a: Vector, b: Vector, modulus: int) -> Vector:
    if len(a) != 10 or len(b) != 10 or modulus < 2:
        raise ValueError('Expected rank-ten vectors and a positive modulus')
    out = [0] * 10
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[(i+j) % 10] += x*y*(-256 if i+j >= 10 else 1)
    return tuple(x % modulus for x in out)


def mul40(a: Vector, b: Vector, modulus: int) -> Vector:
    """Basis c^i*zeta^j, index 4*i+j; c^10=-256, Phi5(zeta)=0."""
    if len(a) != 40 or len(b) != 40:
        raise ValueError('Wrong cyclotomic-algebra rank')
    out = [0] * 40
    for i, x in enumerate(a):
        if not x:
            continue
        ci, zi = divmod(i, 4)
        for j, y in enumerate(b):
            if not y:
                continue
            cj, zj = divmod(j, 4)
            c, z = (ci+cj) % 10, (zi+zj) % 5
            coefficient = x*y*(-256 if ci+cj >= 10 else 1)
            if z == 4:
                for k in range(4):
                    out[4*c+k] -= coefficient
            else:
                out[4*c+z] += coefficient
    return tuple(x % modulus for x in out)


def power(a: Vector, n: int, modulus: int) -> Vector:
    if n < 0:
        raise ValueError('Negative exponent')
    multiply = {10: mul10, 40: mul40}[len(a)]
    out = (1,) + (0,) * (len(a)-1)
    while n:
        if n & 1:
            out = multiply(out, a, modulus)
        a = multiply(a, a, modulus)
        n //= 2
    return out


def embed(a: Vector, twist: int = 0, modulus: int = 17) -> Vector:
    out = [0] * 40
    for i, x in enumerate(a):
        j = (i*twist) % 5
        if j == 4:
            for k in range(4):
                out[4*i+k] -= x
        else:
            out[4*i+j] += x
    return tuple(x % modulus for x in out)


def to20(a: Vector, modulus: int) -> Vector:
    """phi=1+zeta+zeta^-1=-zeta^2-zeta^3. Verify invariance, do not assume it."""
    out = []
    for i in range(10):
        u, v, w, z = a[4*i:4*i+4]
        assert v == 0 and w == z, ('not in the real cyclotomic subalgebra', i)
        out.extend([u, -w % modulus])
    return tuple(out)


def add(a: Vector, b: Vector, modulus: int, scale: int = 1) -> Vector:
    return tuple((x+scale*y) % modulus for x, y in zip(a, b, strict=True))


def valuation(a: int, p: int) -> int:
    if a == 0:
        raise ValueError('Valuation of zero needs a precision bound')
    out = 0
    while a % p == 0:
        a //= p
        out += 1
    return out


def inverse_linear(x: int, y: int, modulus: int) -> Vector:
    """Exact geometric inverse of x+c*y whenever its norm is a unit."""
    a = y*pow(x, -1, modulus) % modulus
    denominator = (1+256*pow(a, 10, modulus)) % modulus
    scale = pow(x*denominator, -1, modulus)
    return tuple(scale*pow(-a, j, modulus) % modulus for j in range(10))


def series_root(scalar_root: int, y: int, precision: int) -> Vector:
    x, modulus = scalar_root**17, 17**precision
    e = valuation(y, 17)
    assert e >= 2 and scalar_root % 17 != 0
    # v17(k!) < k/16. At and beyond this index all terms vanish at the
    # requested precision. This bounds the entire tail, not just one term.
    cutoff = (16*precision + (16*e-17) - 1)//(16*e-17)
    coeff = Fraction(1)
    out = [0] * 10
    for k in range(cutoff):
        if k:
            coeff *= Fraction(1-17*(k-1), 17*k)
        term = scalar_root*coeff*Fraction(y, x)**k
        assert term.denominator % 17 != 0
        residue = term.numerator*pow(term.denominator, -1, modulus) % modulus
        out[k % 10] += residue*pow(-256, k//10, modulus)
    root = tuple(a % modulus for a in out)
    target = (x % modulus, y % modulus)+(0,)*8
    assert power(root, 17, modulus) == target
    return root


def local_example(scalar_root: int, y: int, precision: int) -> dict[str, object]:
    modulus, x = 17**precision, scalar_root**17
    theta = series_root(scalar_root, y, precision)
    tau_inverse = inverse_linear(x, y, modulus)
    theta_inverse = mul10(power(theta, 16, modulus), tau_inverse, modulus)
    assert mul10(theta, theta_inverse, modulus) == (1,)+(0,)*9
    inverse_square = embed(mul10(theta_inverse, theta_inverse, modulus), 0, modulus)
    numerator = mul40(embed(theta, 1, modulus), embed(theta, -1, modulus), modulus)
    U = mul40(numerator, inverse_square, modulus)
    U_conjugate = mul40(mul40(embed(theta, 2, modulus), embed(theta, -2, modulus), modulus),
                       inverse_square, modulus)
    V10 = mul10((x, -y)+(0,)*8, tau_inverse, modulus)
    V = embed(V10, 0, modulus)
    theta_bar = tuple((-1)**j*a % modulus for j, a in enumerate(theta))
    R10 = mul10(theta_bar, theta_inverse, modulus)
    assert power(R10, 17, modulus) == V10
    assert mul10(V10, tuple((-1)**j*a % modulus for j, a in enumerate(V10)), modulus) == (1,)+(0,)*9
    phi = (0, 0, -1 % modulus, -1 % modulus)+(0,)*36
    one = (1,)+(0,)*39
    three_minus_phi = add(tuple(3*a for a in one), phi, modulus, -1)
    curve_left = mul40(three_minus_phi, power(V, 2, modulus), modulus)
    curve_right = add(tuple(4*a % modulus for a in power(U, 17, modulus)),
                      power(phi, 2, modulus), modulus, -1)
    assert curve_left == curve_right
    # Do not divide by the nonunit Y at 17 in the recovery identity.
    recovery_left = mul10((0, y)+(0,)*8, add((1,)+(0,)*9, V10, modulus), modulus)
    recovery_right = tuple(x*a % modulus for a in add((1,)+(0,)*9, V10, modulus, -1))
    assert recovery_left == recovery_right
    U20, Uprime20 = to20(U, modulus), to20(U_conjugate, modulus)
    assert Uprime20 == tuple(v for j in range(10)
                            for v in ((U20[2*j]+U20[2*j+1]) % modulus,
                                      -U20[2*j+1] % modulus))
    e = valuation(y, 17)
    difference = add(U20, Uprime20, modulus, -1)
    assert min(valuation(a, 17) for a in difference if a) == e-1
    lead = y//17*pow(x, -1, modulus) % modulus
    expected = (0, 0, -lead % modulus, 2*lead % modulus)+(0,)*16
    assert all((a-b) % (17**e) == 0 for a, b in zip(difference, expected, strict=True))
    assert any(U20[2*j+1] for j in range(10)), 'Example silently descended to L'
    return {'scalar_root': scalar_root, 'X': str(x), 'Y': str(y),
            'precision': precision, 'modulus': str(modulus),
            'theta': [str(a) for a in theta], 'U_in_c_phi_basis': [str(a) for a in U20],
            'V_in_c_basis': [str(a) for a in V10], 'R_in_c_basis': [str(a) for a in R10],
            'difference_valuation': e-1, 'curve_residual_zero': True,
            'power_condition_R17_equals_V': True, 'recovery_identity_zero': True,
            'scope': 'local example only; no positive-integer W solution asserted'}


def main() -> None:
    z, c, x, y, u, v, p, s = sp.symbols('z c x y u v p s')
    cyclotomic5 = z**4+z**3+z**2+z+1
    phi = 1+z+z**4
    assert sp.rem(phi**2-phi-1, cyclotomic5, z) == 0
    pair = (x+c*z*y)*(x+c*z**4*y)
    identity = 4*pair-(phi+1)*(x+c*y)**2-(3-phi)*(x-c*y)**2
    assert sp.rem(sp.expand(identity), cyclotomic5, z) == 0
    curve = (3-p)*v**2-4*u**17+p**2
    reduced_curve = sp.rem(curve, p**2-p-1, p)
    assert sp.expand(reduced_curve - ((1-v**2)*p+3*v**2+1-4*u**17)) == 0
    assert sp.cancel(c-x*(1-(x-c*y)/(x+c*y))/(y*(1+(x-c*y)/(x+c*y)))) == 0
    # The Möbius transform certifies the field degree symbolically. Irreducibility
    # follows from Q(c)=L of degree ten, not from a sample factorization.
    mobius_poly = x**10*(1-v)**10+256*y**10*(1+v)**10
    substituted = sp.cancel(mobius_poly.subs(v, (x-c*y)/(x+c*y)))
    assert sp.cancel(substituted - 2**10*x**10*y**10*(c**10+256)/(x+c*y)**10) == 0
    assert sp.Poly(mobius_poly, v).degree() == 10
    assert sp.Poly(4*u**17-p**2, u, domain=sp.QQ.frac_field(p)).gcd(
        sp.Poly(68*u**16, u, domain=sp.QQ.frac_field(p))).degree() == 0
    assert sp.rem((3-p)-4+p**2, p**2-p-1, p) == 0  # U=1,V=+/-1
    phi17 = sum(s**j for j in range(17))
    shifted = sp.Poly(sp.expand(phi17.subs(s, s+1)), s)
    assert shifted.LC() == 1 and shifted.TC() == 17
    assert all(shifted.nth(j) % 17 == 0 for j in range(16))
    assert shifted.TC() % 289 != 0
    assert set(pow(3, j, 17) for j in range(16)) == set(range(1, 17))
    subgroups = sorted({tuple(sorted({pow(a, j, 17) for j in range(16)}))
                        for a in range(1, 17)}, key=len)
    assert [len(g) for g in subgroups] == [1, 2, 4, 8, 16]
    assert all(16 in g for g in subgroups if len(g) > 1)
    cm_type = set(range(1, 9))
    assert cm_type.isdisjoint({-a % 17 for a in cm_type})
    assert cm_type | {-a % 17 for a in cm_type} == set(range(1, 17))
    stabilizer = [a for a in range(1, 17) if {a*j % 17 for j in cm_type} == cm_type]
    assert stabilizer == [1]
    genus = (-4+18+2)//2
    cover_genus = (17*(2*genus-2)+17*16+2)//2
    assert genus == 8 and cover_genus == 256
    assert cover_genus == (-2*17+34*16+2)//2
    examples = [local_example(a, b, 12) for a, b in [(1, 17**2), (1, 17**3), (2, 3*17**2)]]
    summary = {'genus': genus, 'power_condition_cover_genus': cover_genus,
               'cm_degree': 16, 'cm_type_exponents': sorted(cm_type),
               'cm_stabilizer': stabilizer, 'subgroup_orders': [len(g) for g in subgroups],
               'all_nontrivial_subgroups_contain_minus_one': True,
               'mobius_polynomial_degree': 10, 'image_field_degree_over_Q': 20,
               'image_field_degree_over_Q_sqrt5': 10,
               'global_point_classification_performed': False, 'full_Beal_solved': False}
    print(json.dumps({'checkpoint': 'U73', 'summary': summary,
                      'cyclic_subgroups': [list(g) for g in subgroups],
                      'local_examples': examples}, indent=2))


if __name__ == '__main__':
    main()
