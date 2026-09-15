"""Exact certificates for the cyclotomic quotient and the rank-one descent.

The script checks algebra and finite residue assertions. The accompanying
manuscript supplies the ideal, real-sign, Kummer, and group-index arguments.
"""
from __future__ import annotations

import json
import sympy as s
from math import gcd

PI = s.sqrt(17)
U, T, Z, X, Y = s.symbols('u t z x y')
EPS = 4+PI
G = U**8+U**7-7*U**6-6*U**5+15*U**4+10*U**3-10*U**2-4*U+1
GP = U**4+(1+PI)*U**3/2+(-3+PI)*U**2/2+(2-PI)*U-1
GM = U**4+(1-PI)*U**3/2+(-3-PI)*U**2/2+(2+PI)*U-1
A4, B4, C4, D4 = 1-4*PI/17, (13-3*PI)/2, (23-5*PI)/2, 6-PI
AE, BE = 4-PI, -8+33*PI/17


def zero(expression: s.Expr) -> bool:
    numerator = s.fraction(s.together(expression))[0]
    symbols = sorted(numerator.free_symbols, key=str)
    if symbols:
        return s.Poly(numerator, *symbols, extension=PI).is_zero
    return s.simplify(numerator) == 0


def local_classes(modulus: int, root: int) -> dict[str, object]:
    assert root*root % modulus == 17 % modulus
    a = -34*(4-root) % modulus
    b = 17*root*pow(4+root, -3, modulus) % modulus
    squares = {n*n % modulus for n in range(modulus)}
    rows = []
    for sign in (1, -1):
        for e in (0, 1):
            for f in (0, 1):
                gamma = sign*pow(4+root, e)*pow(root, f) % modulus
                assert gcd(gamma, modulus) == 1
                scaled_b = b*pow(gamma, -1, modulus) % modulus
                witnesses = [
                    (u, v) for u in range(modulus) for v in range(modulus)
                    if (u % 2 or v % 2)
                    and (gamma*u**4+a*u*u*v*v+scaled_b*v**4) % modulus in squares
                ]
                name = ('-' if sign == -1 else '')+('*'.join(
                    part for part, flag in (('eps', e), ('pi', f)) if flag) or '1')
                rows.append({'class': name, 'representative': gamma,
                             'count_primitive_pairs': len(witnesses),
                             'first_witness': list(witnesses[0]) if witnesses else None})
    return {'modulus': modulus, 'root_pi': root, 'a_dual': a, 'b_dual': b,
            'primitive_pairs_total': modulus*modulus-(modulus//2)**2,
            'square_residues': sorted(squares), 'classes': rows,
            'allowed': [r['class'] for r in rows if r['count_primitive_pairs']]}


def main() -> None:
    checks: dict[str, bool] = {}
    f8 = sum(s.binomial(17, 2*j+1)*5**j*X**(8-j) for j in range(9))
    checks['compact_coordinate_identity'] = zero(
        (U-2)**8*f8.subs(X, 5*(U+2)/(U-2))-2**16*5**8*G)
    checks['cyclotomic_identity'] = zero(Z**8*G.subs(U, Z+1/Z)-sum(Z**j for j in range(17)))
    checks['quartic_factorization'] = zero(GP*GM-G)
    checks['quartic_resultant'] = zero(s.resultant(GP, GM, U)+17**2)
    checks['g_discriminant'] = s.discriminant(G, U) == 17**7
    checks['mod17_shift'] = s.Poly(G-(U-2)**8, U, modulus=17).is_zero
    checks['norm_epsilon'] = zero((4+PI)*(4-PI)+1)
    checks['norm_prime2_generator'] = s.expand((5+PI)*(5-PI)/4) == 2
    checks['quartic_at_2'] = zero(GP.subs(U, 2)-(17+4*PI))
    q = 1+D4*T+C4*T*T+B4*T**3+A4*T**4
    checks['quartic_expansion'] = zero(GP.subs(U, T+2)/(17+4*PI)-q)
    xx = (2*(Z+1)+D4*T)/T**2
    yy = ((xx*xx-4*A4)*T-D4*xx-2*B4)/2
    cubic = X**3+C4*X**2+(B4*D4-4*A4)*X+(B4**2+A4*D4**2-4*A4*C4)
    numerator = s.fraction(s.cancel(yy**2-cubic.subs(X, xx), extension=PI))[0]
    remainder = s.rem(numerator, Z*Z-q, Z)
    checks['quartic_to_cubic'] = zero(remainder)
    shift = (PI-5)/2
    checks['cubic_translation'] = zero(cubic.subs(X, X+shift)-(X**3+AE*X*X+BE*X))
    inv_t = (2*Y+D4*(X+shift)+2*B4)/((X+shift)**2-4*A4)
    inv_z = ((X+shift)*inv_t**2-D4*inv_t-2)/2
    inverse_num = s.fraction(s.cancel(inv_z**2-q.subs(T, inv_t), extension=PI))[0]
    checks['inverse_map'] = zero(s.rem(inverse_num, Y*Y-X**3-AE*X*X-BE*X, Y))
    checks['norm_leading_quartic'] = zero((1-4*PI/17)*(1+4*PI/17)-s.Rational(1,17))
    checks['elliptic_coefficients'] = zero(BE-EPS**(-2)/PI)
    checks['dual_coefficient'] = zero(AE**2-4*BE-EPS**(-3)/PI)
    checks['integral_b'] = zero(17**2*BE-17*PI*EPS**(-2))
    checks['integral_b_dual'] = zero((17*AE)**2-4*17**2*BE-17*PI*EPS**(-3))
    checks['norm_dual_coefficient'] = zero((AE**2-4*BE)*((4+PI)**2-4*(-8-33*PI/17))-s.Rational(1,17))
    px, py = s.Rational(17,4)-PI, -16+s.Rational(31,8)*PI
    checks['P_on_curve'] = zero(py*py-px**3-AE*px*px-BE*px)
    checks['P_squareclass'] = zero(px-PI/(4*EPS))
    checks['inverse_P'] = zero(inv_t.subs({X:px,Y:py}))
    deriv_u = 2*Y*s.diff(inv_t, X)+(3*X*X+2*AE*X+BE)*s.diff(inv_t, Y)
    checks['invariant_derivative_u_at_P'] = zero(deriv_u.subs({X:px, Y:py})-2)
    # With tau=-x/y, x=tau^-2-AE+O(tau^2), y=-x/tau.
    # These leading terms suffice for du/dtau at O.
    checks['invariant_derivative_u_at_O'] = zero(s.limit(inv_t.subs({X:T**(-2)-AE, Y:-T**(-3)+AE/T})/T, T, 0)+2)
    # General isogeny algebra, independent of this example's coefficient values.
    a, b, x, y = s.symbols('a b x y')
    xp, yp = x+a+b/x, y*(1-b/x**2)
    bdual = a*a-4*b
    expr = s.together(yp**2-(xp**3-2*a*xp**2+bdual*xp))
    checks['isogeny_maps_curve'] = s.rem(s.fraction(expr)[0], y*y-x**3-a*x*x-b*x, y) == 0
    psi_x = (xp-2*a+bdual/xp)/4
    double_x = (x*x-b)**2/(4*x*(x*x+a*x+b))
    checks['isogeny_composition_x'] = s.cancel(psi_x-double_x) == 0
    psi_y = yp*(1-bdual/xp**2)/8
    slope = (3*x*x+2*a*x+b)/(2*y)
    double_y = slope*(x-double_x)-y
    checks['isogeny_composition_y'] = zero(s.rem(
        s.fraction(s.together(psi_y-double_y))[0], y*y-x**3-a*x*x-b*x, y))
    root = s.symbols('root')
    pre_x = a+2*root**2+2*y/root
    pre_y = 2*root*pre_x
    pre_relation = y*y-root**6-a*root**4-b*root**2
    preimage = pre_y**2-pre_x**3+2*a*pre_x**2-bdual*pre_x
    checks['kummer_preimage_on_partner'] = zero(s.rem(
        s.fraction(s.together(preimage))[0], pre_relation, y))
    recovered_x = (pre_x-2*a+bdual/pre_x)/4
    checks['kummer_preimage_recovers_x'] = zero(s.rem(
        s.fraction(s.together(recovered_x-root**2))[0], pre_relation, y))
    assert all(checks.values()), [k for k, v in checks.items() if not v]
    local = [local_classes(16, 7), local_classes(64, 41)]
    common = sorted(set(local[0]['allowed']) & set(local[1]['allowed']))
    assert common == ['1', 'eps*pi']
    # The roots arise from the two simple roots of w^2-w-4 over Z_2.
    assert (4**2-4-4) % 8 == 0 and (21**2-21-4) % 32 == 0
    print(json.dumps({'status':'completed','symbolic_checks': checks,
                      'two_adic_descent': local, 'dual_kummer_upper_bound_classes':common,
                      'rank_computation_note': 'The manuscript proves that these upper bounds are attained; a residue count alone is not a rank proof.'}, indent=2))

if __name__ == '__main__':
    main()
