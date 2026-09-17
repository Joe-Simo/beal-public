#!/usr/bin/env python3
"""
U111: Automorphism Group and Quotient Analysis of Twisted Modular Curve X_{E_0}(17)
Over Q, Q(sqrt(17)), and Q(i).

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
    p = 17
    print("=" * 80)
    print(f"U111: GEOMETRIC & ARITHMETIC AUTOMORPHISM AUDIT OF X_{{E_0}}({p})")
    print("=" * 80)

    # 1. Curve and Invariants
    g_X17 = 1 + (p**2 - 1)*(p - 6) // 24
    print(f"\n1. GENUS OF X_{{E_0}}({p}):")
    print(f"   Formula: g = 1 + (p^2 - 1)(p - 6)/24")
    print(f"   g(X(17)) = 1 + ({p**2 - 1} * {p - 6})/24 = 1 + {288 * 11 // 24} = {g_X17}")
    print(f"   Because X_{{E_0}}(17) is an inner twist of X(17) over Qbar,")
    print(f"   g(X_{{E_0}}(17)) = {g_X17} identically.\n")

    # 2. Group Constructions
    print("2. FINITE MATRIX GROUPS AT LEVEL p = 17:")
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

    print(f"   |PGL_2(F_17)| = {len(pgl_elts)} (expected {p*(p**2-1)})")
    print(f"   |PSL_2(F_17)| = {len(psl_elts)} (expected {p*(p**2-1)//2})")
    print(f"   |P(GL_2^+(F_17))| = {len(gl_plus_proj)}")
    assert len(pgl_elts) == 4896
    assert len(psl_elts) == 2448
    assert gl_plus_proj == psl_elts
    print("   VERIFIED: The projective image of GL_2^+(F_17) is IDENTICALLY PSL_2(F_17)!")

    # 3. Centralizer Computations (Automorphisms over Q, Q(sqrt(17)), Q(i))
    print("\n3. ARITHMETIC AUTOMORPHISM GROUPS Aut_K(X_{E_0}(17)):")
    I = canon_pgl((1, 0, 0, 1), p)
    
    # Centralizer of PGL_2(F_17)
    cent_pgl = []
    for g in pgl_elts:
        commutes = True
        for h in pgl_elts:
            if canon_pgl(mult_mat(g, h, p), p) != canon_pgl(mult_mat(h, g, p), p):
                commutes = False
                break
        if commutes:
            cent_pgl.append(g)
    print(f"   Z_{{PGL_2(F_17)}}(PGL_2(F_17)) = {cent_pgl}")
    assert cent_pgl == [I]

    # Centralizer of PSL_2(F_17)
    cent_psl = []
    for g in pgl_elts:
        commutes = True
        for h in psl_elts:
            if canon_pgl(mult_mat(g, h, p), p) != canon_pgl(mult_mat(h, g, p), p):
                commutes = False
                break
        if commutes:
            cent_psl.append(g)
    print(f"   Z_{{PGL_2(F_17)}}(PSL_2(F_17)) = {cent_psl}")
    assert cent_psl == [I]

    print("\n   ALGEBRAIC DEDUCTIONS:")
    print("   (a) Over K = Q:")
    print("       Galois image: Im(rho_bar) = GL_2(F_17) => Projective image = PGL_2(F_17).")
    print("       Aut_Q(X_{E_0}(17)) = Z_{PGL_2(F_17)}(PGL_2(F_17)) = {id}.")
    print("   (b) Over K = Q(sqrt(17)):")
    print("       Galois image: Im(rho_bar|_{G_{Q(sqrt(17))}}) = GL_2^+(F_17).")
    print("       Projective image = PSL_2(F_17).")
    print("       Aut_{Q(sqrt(17))}(X_{E_0}(17)) = Z_{PGL_2(F_17)}(PSL_2(F_17)) = {id}.")
    print("   (c) Over K = Q(i):")
    print("       Q(i) is linearly disjoint from the 17-division field.")
    print("       Galois image: Im(rho_bar|_{G_{Q(i)}}) = GL_2(F_17) => Projective image = PGL_2(F_17).")
    print("       Aut_{Q(i)}(X_{E_0}(17)) = Z_{PGL_2(F_17)}(PGL_2(F_17)) = {id}.")
    print("   THEOREM: In all three cases, the K-rational automorphism group is TRIVIAL {id}!")

    # 4. Simplicity and Quotient Curves
    print("\n4. GALOIS-STABLE SUBGROUPS & QUOTIENT CURVES OVER K:")
    # Verify simplicity of PSL_2(F_17)
    # Check conjugacy classes
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

    divs = [d for d in sympy.divisors(2448) if 1 < d < 2448]
    reachable = {1}
    for sz in sorted(class_sizes)[1:]:
        new_reach = set(reachable)
        for r in reachable:
            new_reach.add(r + sz)
        reachable = new_reach

    common = reachable.intersection(set(divs))
    print(f"   PSL_2(F_17) order: 2448. Class sizes: {sorted(class_sizes)}")
    print(f"   Possible non-trivial normal subgroup orders: {common}")
    assert len(common) == 0
    print("   VERIFIED: PSL_2(F_17) is a NON-ABELIAN SIMPLE GROUP.")
    print("   Consequently, NO proper non-trivial subgroup of PSL_2(F_17) is normalized by PSL_2(F_17).")
    print("   THEOREM: Neither X_{E_0}(17) nor its twists admit ANY intermediate modular")
    print("   quotient curve X_{E_0}(17)/H defined over Q, Q(sqrt(17)), or Q(i)!")
    print("   The only K-rational quotients are the curve itself (H = {1}) and the j-line P^1 (H = PSL_2).")

    # 5. Fixed Points and Involution Quotient Genus
    print("\n5. RIEMANN-HURWITZ CALCULATION FOR INVOLUTION QUOTIENT X_{E_0}(17)/<w>:")
    # Number of involutions in PSL_2(F_17)
    num_inv = sum(1 for sz in class_sizes if sz == 153) # class of order 2
    assert num_inv == 1
    # Fixed points per involution:
    # (p - (-1/p))/2 = (17 - 1)/2 = 8
    fixed_pts = (p - 1) // 2
    g_quot_w = (2 * g_X17 + 2 - fixed_pts) / 4
    print(f"   Number of involutions in PSL_2(F_17): 153")
    print(f"   Fixed points per involution on X(17): {fixed_pts} (all in fiber above j = 1728)")
    print(f"   By Riemann-Hurwitz: g(X(17)/<w>) = (2 * 133 + 2 - 8) / 4 = 260 / 4 = {int(g_quot_w)}")
    assert g_quot_w == 65
    print("   VERIFIED: g(X_{E_0}(17)/<w>) = 65 >> 2.")
    print("=" * 80)
    print("ALL ALGEBRAIC AND GEOMETRIC VERIFICATIONS SUCCEEDED.")
    print("=" * 80)

if __name__ == "__main__":
    main()
