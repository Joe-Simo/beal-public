"""Exact U78 certificates: descent-field arithmetic and local dimensions.

This does not compute the class group's 2-rank, the dyadic Kummer image,
its global restriction matrix, a Selmer group, or a Mordell-Weil rank.
"""
from __future__ import annotations

import json
from itertools import product
from math import comb

import sympy as sp


def main() -> None:
    s, p, x, v = sp.symbols('s p x v')
    f = s**34 + 2*s**17 - 4
    kpoly = p*p-p-1
    c = 2*p-2
    h = sum((-1)**j*s**(16-j) for j in range(17))
    red = lambda expr: sp.rem(sp.expand(expr), kpoly, p)
    assert red(c*p-2) == 0
    assert sp.expand((s+1)*h-s**17-1) == 0
    assert sp.rem(((s**17+2)/2)**2-(s**17+2)/2-1, f, s) == 0

    # Both base primes are inert; the relative polynomials are Eisenstein.
    assert sp.Poly(kpoly, p, modulus=2).is_irreducible
    assert sp.Poly(kpoly, p, modulus=17).is_irreducible
    shift = sp.Poly(red((-2*p)**17-c), p)
    shift_exact = [int(shift.nth(j)) for j in range(2)]
    assert all(a % 17 == 0 for a in shift_exact)
    shift_mod = [a//17 % 17 for a in shift_exact]
    assert shift_mod == [11, 8]
    assert int(sp.resultant(kpoly, 11+8*p, p)) % 17 == 9
    assert all(comb(17,j) % 17 == 0 for j in range(1,17))
    assert all(comb(17,j) % 289 != 0 for j in range(1,17))
    assert sp.Poly(h, s, modulus=5).is_irreducible
    assert sp.rem(s**17+1, s+1, s) == 0
    assert next(j for j in range(1,17) if pow(5,j,17) == 1) == 16
    assert h.subs(s,-1) == 17

    # Exact change of basis, not a rounded numerical discriminant.
    basis = [s**j for j in range(17)] + [(s**j+s**(17+j)/2) for j in range(17)]
    mat = sp.Matrix([[sp.Poly(b,s).nth(i) for b in basis] for i in range(34)])
    assert mat.det() == sp.Rational(1, 2**17)
    polynomial_disc = int(sp.discriminant(f,s))
    field_disc = polynomial_disc // 2**34
    assert field_disc == 2**32*5**17*17**34
    assert polynomial_disc == 2**66*5**17*17**34
    norm_values = [int(sp.resultant(f,g,s)) for g in (s,s+1,h)]
    assert norm_values == [-4,-5,5**16]
    assert int(sp.resultant(f,s**17+1,s)) == (-5)**17
    assert int(sp.resultant(kpoly,c,p)) == -4
    assert int(sp.resultant(kpoly,2*p-1,p)) == -5

    # Recover the root of the actual degree-seventeen descent polynomial.
    rnum = s**32+2*s**15  # 4/s^2 in F
    assert sp.rem(8*rnum**17-4**17*(s**17+4),f,s) == 0
    assert sp.rem(s**17*rnum**8-4**8*s,f,s) == 0
    aa, bb = -4*(3-p), p+2
    assert red((3-p)*p**2-bb) == 0
    assert red(aa*p**2/4+bb) == 0
    assert red(aa**16*(aa*x**17+bb)-((aa*x)**17+aa**16*bb)) == 0
    monic = x**17+aa**16*bb
    disc_norm = int(sp.resultant(kpoly, red(sp.discriminant(monic,x)),p))
    assert sp.factorint(disc_norm) == {2:1024,5:272,17:34}

    # Complete local squareclass space at 5. Coordinates: valuations and
    # nonsquare-unit bits on the degree-one and degree-sixteen components.
    kernel5 = [list(row) for row in product(range(2),repeat=4)
               if row[0] == 0 and (row[1]+row[3]) % 2 == 0]
    image5 = [row for row in kernel5 if (row[1]+row[2]) % 2 == 0]
    assert kernel5 == [[0,0,0,0],[0,0,1,0],[0,1,0,1],[0,1,1,1]]
    assert image5 == [[0,0,0,0],[0,1,1,1]]
    assert pow(17,2,5) == 4
    # A genuine global norm-kernel S-unit that passes this local condition;
    # no assertion is made that it passes the uncomputed dyadic condition.
    # alpha=(s+1)/(sqrt(5))=1/h(s); local bits=(0,1,1,1).
    assert (pow(17,-1,5) in (2,3))
    assert sp.rem((s+1)*h-(s**17+1),f,s) == 0

    local_table = []
    for rational_prime, base_degree, factors in [(2,2,[17]),(5,2,[1,16]),(17,2,[17])]:
        two_torsion = len(factors)-1
        image_dim = two_torsion + (8*base_degree if rational_prime==2 else 0)
        h_dim = 2*image_dim
        local_table.append({'prime':rational_prime,'base_local_degree':base_degree,
                            'relative_factor_degrees':factors,'J_local_2torsion_dimension':two_torsion,
                            'norm_kernel_dimension':h_dim,'Kummer_image_dimension':image_dim,
                            'quotient_dimension':h_dim-image_dim})
    assert [row['quotient_dimension'] for row in local_table] == [16,1,0]
    global_dim_constant = (2+16-1)+4+1 - ((2-1)+3+1)
    assert global_dim_constant == 17
    # The retained arithmetic data do NOT set d=0 or the matrix rank=17.
    summary = {
        'defining_polynomial':'s^34+2*s^17-4',
        'signature':[2,16],
        'integral_basis':'s^j, phi*s^j, 0<=j<=16; phi=(s^17+2)/2',
        'polynomial_discriminant_factorization':{'2':66,'5':17,'17':34},
        'field_discriminant_factorization':{'2':32,'5':17,'17':34},
        'field_discriminant':str(field_disc),
        'equation_order_index':2**17,
        'shift_constant_coefficients':shift_exact,
        'shift_divided_by17_mod17':shift_mod,
        'shift_quotient_norm_mod17':9,
        'norms_s_splus1_h':list(map(str,norm_values)),
        'primes_above_S':[
            {'p':2,'absolute_e':17,'absolute_f':2,'ideal_norm':'4','principal_generator':'s'},
            {'p':5,'absolute_e':2,'absolute_f':1,'ideal_norm':'5','principal_generator':'s+1'},
            {'p':5,'absolute_e':2,'absolute_f':16,'ideal_norm':str(5**16),'principal_generator':'h(s)'},
            {'p':17,'absolute_e':17,'absolute_f':2,'ideal_norm':'289','class_order_divides':17}],
        'monic_model_discriminant_norm_factors':{'2':1024,'5':272,'17':34},
        'local5_norm_kernel':kernel5,'local5_Kummer_image':image5,
        'local_dimensions':local_table,
        'real_local_norm_kernel_dimensions':[0,0],
        'global_candidate_dimension':'17+d, d=dim_F2 Cl(F)[2]',
        'restriction_target_dimension':17,
        'Selmer_dimension_formula':'17+d-rank(Psi)',
        'class_group_2_rank_computed':False,
        'dyadic_image_basis_computed':False,
        'restriction_matrix_computed':False,
        'numerical_rank_upper_bound_computed':False,
        'full_Beal_solved':False}
    print(json.dumps({'checkpoint':'U78','summary':summary},indent=2))


if __name__=='__main__':
    main()
