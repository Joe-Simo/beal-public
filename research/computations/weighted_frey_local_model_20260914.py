"""Exact coordinate identities for the corrected (-1)-twist.

Domain: Q[pi,X,Y,u,v], pi**5=2, symbolic X,Y; X odd is a hypothesis of
subsequent arithmetic interpretation, not of the polynomial identities.
Smoothness and inertia interpretation are proved in the research note.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import sympy as sp


def main() -> None:
    pi, x, y, u, v, w, z = sp.symbols('pi X Y u v w z')
    old_x = pi**8 * u
    old_y = 8*(2*v+x**5)
    g = (old_x**5 + 80*x*x*y*y*old_x**3
         + 1280*x**4*y**4*old_x + 64*(x**10-256*y**10))
    affine = (v*v+x**5*v-u**5-5*pi**4*x*x*y*y*u**3
              -5*pi**8*x**4*y**4*u+64*y**10)
    identity = sp.rem(sp.expand(g-old_y**2+256*affine), pi**5-2, pi)
    if identity != 0:
        raise AssertionError('coordinate change')
    infinity = (z*z+x**5*w**3*z-w-5*pi**4*x*x*y*y*w**3
                -5*pi**8*x**4*y**4*w**5+64*y**10*w**6)
    overlap = sp.cancel(w**6*affine.subs({u: 1/w, v: z/w**3})-infinity)
    if overlap != 0:
        raise AssertionError('chart overlap')
    finite_reduction = sp.Poly(affine.subs({pi:0,x:1}),u,v,y,modulus=2)
    infinity_reduction = sp.Poly(infinity.subs({pi:0,x:1}),w,z,y,modulus=2)
    if finite_reduction.diff(v).as_expr() != 1:
        raise AssertionError('affine characteristic-2 smoothness')
    if infinity_reduction.diff(w).as_expr().subs({w:0,z:0}) != 1:
        raise AssertionError('smoothness at infinity')
    # Controlled wrong sign: the +64*X^10 cancellation must fail for f_old twist.
    wrong = sp.rem(sp.expand(g-128*x**10-old_y**2+256*affine),pi**5-2,pi)
    if sp.expand(wrong+128*x**10) != 0 or wrong == 0:
        raise AssertionError('negative control')
    print(json.dumps({
        'status':'completed; universal polynomial identities checked',
        'sympy':sp.__version__,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'coordinate_identity_remainder':str(identity),
        'chart_overlap_remainder':str(overlap),
        'affine_special_fiber':str(finite_reduction.as_expr()),
        'infinity_special_fiber':str(infinity_reduction.as_expr()),
        'affine_dF_dv':'1','infinity_dF_dw_at_origin':'1',
        'wrong_sign_remainder':str(wrong),
        'limits':'No formal kernel or global modularity / level-lowering assertion.'
    },indent=2))


if __name__ == '__main__':
    main()
