#!/usr/bin/env python3
"""
U111: Automorphism Group and Quotient Analysis of Twisted Modular Curve X_{E_0}(19)
Over Q, Q(sqrt(-19)), and Q(i).

Author: Arithmetic Number Theory Research Group (Catalan Twisted Automorphism Auditor)
Date: 2026-09-17
"""

import sys
import sympy
from fractions import Fraction
from collections import Counter

def mult_mat(m1, m2, p):
    a1, b1, c1, d1 = m1
    a2, b2, c2, d2 = m2
    return (
        (a1*a2 + b1*c2) % p,
        (a1*b2 + b1*d2) % p,
        (c1*a2 + d1*c2) % p,
        (c1*b2 + d1*d2) % p
    )

def canon_pgl(m, p):
    for x in m:
        if x % p != 0:
            inv = pow(x, -1, p)
            return tuple((c * inv) % p for c in m)
    return m

def canon_psl(m, p):
    a, b, c, d = m
    neg = ((-a)%p, (-b)%p, (-c)%p, (-d)%p)
    return min(m, neg)

def inv_mat_psl(m, p):
    a, b, c, d = m
    return canon_psl((d, (-b)%p, (-c)%p, a), p)

def main():
    p = 19
    print("=" * 80)
    print(f"U111: GEOMETRIC & ARITHMETIC AUTOMORPHISM AUDIT OF X_{{E_0}}({p})")
    print("=" * 80)

    # 1. Curve and Invariants
    g_X19 = 1 + (p**2 - 1)*(p - 6) // 24
    mu = p * (p**2 - 1) // 2
    e2 = mu // 2
    e3 = mu // 3
    e_inf = (p**2 - 1) // 2
    rh_check = 1 + (-2*mu + e2*(2-1) + e3*(3-1) + e_inf*(p-1)) // 2

    print(f"\n1. GENUS OF X_{{E_0}}({p}):")
    print(f"   Formula: g = 1 + (p^2 - 1)(p - 6)/24")
    print(f"   g(X(19)) = 1 + ({p**2 - 1} * {p - 6})/24 = 1 + {360 * 13 // 24} = {g_X19}")
    print(f"   Riemann-Hurwitz Covering Verification:")
    print(f"     Index mu = [PSL_2(Z) : Gamma(19)] = {mu}")
    print(f"     Order 2 elliptic points (j = 1728): {e2}")
    print(f"     Order 3 elliptic points (j = 0)   : {e3}")
    print(f"     Cusps (j = oo, width 19)          : {e_inf}")
    print(f"     2g - 2 = -2({mu}) + {e2}(1) + {e3}(2) + {e_inf}(18) = {-2*mu + e2 + 2*e3 + 18*e_inf}")
    print(f"     g = {rh_check}")
    assert g_X19 == 196
    assert rh_check == 196
    print(f"   Because X_{{E_0}}(19) is an inner twist of X(19) over Qbar,")
    print(f"   g(X_{{E_0}}(19)) = {g_X19} identically.\n")

    # 2. Group Constructions
    print("2. FINITE MATRIX GROUPS AT LEVEL p = 19:")
    pgl_elts = set()
    psl_elts = set()
    gl_plus_proj = set()

    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    det = (a*d - b*c) % p
                    if det != 0:
                        rep_pgl = canon_pgl((a, b, c, d), p)
                        pgl_elts.add(rep_pgl)
                        if sympy.is_quad_residue(det, p):
                            gl_plus_proj.add(rep_pgl)
                        if det == 1:
                            psl_elts.add(rep_pgl)

    print(f"   |PGL_2(F_19)| = {len(pgl_elts)} (expected {p*(p**2-1)})")
    print(f"   |PSL_2(F_19)| = {len(psl_elts)} (expected {p*(p**2-1)//2})")
    print(f"   |P(GL_2^+(F_19))| = {len(gl_plus_proj)}")
    assert len(pgl_elts) == 6840
    assert len(psl_elts) == 3420
    assert gl_plus_proj == psl_elts
    print("   VERIFIED: The projective image of GL_2^+(F_19) is IDENTICALLY PSL_2(F_19)!")

    # 3. Centralizer Computations (Automorphisms over Q, Q(sqrt(-19)), Q(i))
    print("\n3. ARITHMETIC AUTOMORPHISM GROUPS Aut_K(X_{E_0}(19)):")
    I = canon_pgl((1, 0, 0, 1), p)
    
    # Generators of PSL_2(F_19): T = [[1, 1], [0, 1]], S = [[0, -1], [1, 0]]
    # Generator of PGL_2(F_19): D = [[2, 0], [0, 1]] (since 2 is primitive root mod 19)
    gens_psl = [canon_pgl((1, 1, 0, 1), p), canon_pgl((0, p - 1, 1, 0), p)]
    gens_pgl = gens_psl + [canon_pgl((2, 0, 0, 1), p)]

    # Verify generators generate full groups
    frontier = set(gens_psl)
    gen_subgroup = set(gens_psl)
    while frontier:
        new_frontier = set()
        for g in frontier:
            for h in gens_psl:
                prod = canon_pgl(mult_mat(g, h, p), p)
                if prod not in gen_subgroup:
                    gen_subgroup.add(prod)
                    new_frontier.add(prod)
        frontier = new_frontier
    assert len(gen_subgroup) == 3420
    print("   VERIFIED: S and T generate the full PSL_2(F_19) of order 3420.")

    # Centralizer of PGL_2(F_19)
    cent_pgl = [g for g in pgl_elts if all(
        canon_pgl(mult_mat(g, h, p), p) == canon_pgl(mult_mat(h, g, p), p) for h in gens_pgl
    )]
    print(f"   Z_{{PGL_2(F_19)}}(PGL_2(F_19)) = {cent_pgl}")
    assert cent_pgl == [I]

    # Centralizer of PSL_2(F_19)
    cent_psl = [g for g in pgl_elts if all(
        canon_pgl(mult_mat(g, h, p), p) == canon_pgl(mult_mat(h, g, p), p) for h in gens_psl
    )]
    print(f"   Z_{{PGL_2(F_19)}}(PSL_2(F_19)) = {cent_psl}")
    assert cent_psl == [I]

    print("\n   ALGEBRAIC DEDUCTIONS:")
    print("   (a) Over K = Q:")
    print("       Galois image: Im(rho_bar) = GL_2(F_19) => Projective image = PGL_2(F_19).")
    print("       Aut_Q(X_{E_0}(19)) = Z_{PGL_2(F_19)}(PGL_2(F_19)) = {id}.")
    print("   (b) Over K = Q(sqrt(-19)):")
    print("       Note: 19 = 3 (mod 4) => (-1/19) = -1 => p* = -19.")
    print("       Unique quadratic subfield of Q(zeta_19) is IMAGINARY QUADRATIC Q(sqrt(-19)).")
    print("       Galois image: Im(rho_bar|_{G_{Q(sqrt(-19))}}) = GL_2^+(F_19).")
    print("       Projective image = PSL_2(F_19).")
    print("       Aut_{Q(sqrt(-19))}(X_{E_0}(19)) = Z_{PGL_2(F_19)}(PSL_2(F_19)) = {id}.")
    print("   (c) Over K = Q(i):")
    print("       Q(i) is ramified solely at 2, while Q(zeta_19) is ramified solely at 19.")
    print("       The 19-division field L_19 has unique quadratic subfield Q(sqrt(-19)) != Q(i).")
    print("       Thus Q(i) is linearly disjoint from L_19.")
    print("       Galois image: Im(rho_bar|_{G_{Q(i)}}) = GL_2(F_19) => Projective image = PGL_2(F_19).")
    print("       Aut_{Q(i)}(X_{E_0}(19)) = Z_{PGL_2(F_19)}(PGL_2(F_19)) = {id}.")
    print("   THEOREM: In all cases, the K-rational automorphism group is TRIVIAL {id}!")

    # 4. Simplicity and Quotient Curves
    print("\n4. GALOIS-STABLE SUBGROUPS & QUOTIENT CURVES OVER K:")
    # Check conjugacy classes of PSL_2(F_19)
    psl_list = []
    seen_psl = set()
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    if (a*d - b*c) % p == 1:
                        rep = canon_psl((a, b, c, d), p)
                        if rep not in seen_psl:
                            seen_psl.add(rep)
                            psl_list.append(rep)

    visited = set()
    class_sizes = []
    for g in psl_list:
        if g not in visited:
            c_class = set()
            for x in psl_list:
                x_inv = inv_mat_psl(x, p)
                conj = canon_psl(mult_mat(mult_mat(x_inv, g, p), x, p), p)
                c_class.add(conj)
            visited.update(c_class)
            class_sizes.append(len(c_class))

    divs = [d for d in sympy.divisors(3420) if 1 < d < 3420]
    reachable = {1}
    for sz in sorted(class_sizes)[1:]:
        new_reach = set(reachable)
        for r in reachable:
            new_reach.add(r + sz)
        reachable = new_reach

    common = reachable.intersection(set(divs))
    print(f"   PSL_2(F_19) order: 3420. Class sizes: {sorted(class_sizes)}")
    print(f"   Possible non-trivial normal subgroup orders: {common}")
    assert len(common) == 0
    print("   VERIFIED: PSL_2(F_19) is a NON-ABELIAN SIMPLE GROUP.")
    print("   Consequently, NO proper non-trivial subgroup of PSL_2(F_19) is normalized by PSL_2(F_19).")
    print("   THEOREM: Neither X_{E_0}(19) nor its twists admit ANY intermediate modular")
    print("   quotient curve X_{E_0}(19)/H defined over Q, Q(sqrt(-19)), or Q(i)!")
    print("   The only K-rational quotients are the curve itself (H = {1}) and the j-line P^1 (H = PSL_2).")

    # 5. Fixed Points and Involution Quotient Genus
    print("\n5. RIEMANN-HURWITZ CALCULATION FOR INVOLUTION QUOTIENT X_{E_0}(19)/<w>:")
    # Number of involutions in PSL_2(F_19)
    num_inv = sum(1 for sz in class_sizes if sz == 171) # class of order 2 has size 171
    assert num_inv == 1
    # Fixed points per involution:
    # (p - (-1/p))/2 = (19 - (-1))/2 = 10
    fixed_pts = (p - sympy.legendre_symbol(-1, p)) // 2
    assert fixed_pts == 10
    g_quot_w = (2 * g_X19 + 2 - fixed_pts) / 4
    print(f"   Number of involutions in PSL_2(F_19): 171 (single conjugacy class)")
    print(f"   Fixed points per involution on X(19): {fixed_pts} (all in fiber above j = 1728)")
    print(f"   By Riemann-Hurwitz: g(X(19)/<w>) = (2 * 196 + 2 - 10) / 4 = 384 / 4 = {int(g_quot_w)}")
    assert g_quot_w == 96
    print("   VERIFIED: g(X_{E_0}(19)/<w>) = 96 >> 2.")

    # 6. Modular Descent to X_0(19)
    print("\n6. MODULAR DESCENT TO X_0(19):")
    # Borel subgroup index in PGL_2(F_19)
    borel_pgl = set()
    for a in range(1, p):
        for b in range(p):
            for d in range(1, p):
                borel_pgl.add(canon_pgl((a, b, 0, d), p))
    deg_K_E0 = len(pgl_elts) // len(borel_pgl)
    print(f"   Borel subgroup B has order {len(borel_pgl)} in PGL_2(F_19).")
    print(f"   Index [PGL_2(F_19) : B] = {deg_K_E0} (= 19 + 1 lines in F_19^2).")
    print(f"   Degree of isogeny field [K_{{E_0}} : Q] = {deg_K_E0}.")

    # Linear disjointness of K_{E_0} and Q(sqrt(-19))
    borel_psl = borel_pgl.intersection(psl_elts)
    print(f"   |B cap PSL_2(F_19)| = {len(borel_psl)}, index in PSL_2 = {len(psl_elts) // len(borel_psl)}")
    assert len(borel_pgl) // len(borel_psl) == 2
    print("   Because B surjects onto PGL_2 / PSL_2 = Z/2Z, K_{E_0} is LINEARLY DISJOINT from Q(sqrt(-19)).")
    print(f"   The compositum L = K_{{E_0}}(sqrt(-19)) has degree [L : Q] = 20 * 2 = 40!")
    print("   This exactly explains Freitas, Naskrecki, and Stoll (2020, line 627):")
    print("   'requiring arithmetic information of number fields of degree 36 or 40'.")

    print("\n" + "=" * 80)
    print("ALL LEVEL 19 ALGEBRAIC AND GEOMETRIC AUDITS COMPLETED SUCCESSFULLY.")
    print("=" * 80)

if __name__ == "__main__":
    main()
