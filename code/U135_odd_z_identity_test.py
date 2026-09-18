"""Cycle U135 — cheapest exact test for the (2m,2n,z) route with odd prime z>=7.
For z=3: Re((u+vi)^3)/u = u^2-3v^2 is already BS-shaped.  For z=5: P_5 + 4u^4 = 5(u^2-v^2)^2 gave a BS-shaped
one-sided equation (C048).  Named hypothesis H_z: there exist a rational c and a homogeneous R of degree
(z-1)/2 with  P_z(u,v) + c*u^(z-1) = z*R(u,v)^2  (the identity that produced the BS shape for z=5).
Test exactly over Q by solving the coefficient system with fractions."""
from fractions import Fraction as F
from itertools import product
def P(z):
    # Re((u+vi)^z) = sum_k C(z,2k) u^(z-2k) (-1)^k v^(2k);  divide by u -> coefficients of u^(z-1-2k) v^(2k)
    from math import comb
    return {k: F((-1)**k * comb(z,2*k)) for k in range(0,(z+1)//2)}   # coefficient of u^(z-1-2k) v^(2k)
def test(z):
    d=(z-1)//2                      # deg R
    # R = sum_j r_j u^(d-2j) v^(2j)  (even in v; the odd-in-v ansatz has no u^(z-1) term and is checked below)
    js=list(range(0,d//2+1))
    p=P(z)
    # unknowns r_j; equation: p_k + c*[k==0] = z * sum_{i+j=k} r_i r_j  -- nonlinear; brute-force r_0 = +-sqrt((p_0+c)/z) by scanning small c
    # Instead: eliminate: r_0^2 z = p_0 + c  free (c absorbs), then solve successively r_1.. from p_1.. linear in r_j given r_0
    for r0 in [F(1),F(-1),F(1,2),F(2),F(1,3),F(3)]:       # scaling of R only rescales the identity; r0 fixes normalisation
        r={0:r0}; ok=True
        for k in range(1,d//2+1):
            # p_k = z * (2 r0 r_k + sum_{i+j=k, 0<i,j<k} r_i r_j)
            s=sum(r[i]*r[k-i] for i in range(1,k))
            r[k]=(p[k]/z - s)/(2*r0)
        # now check remaining equations k = d//2+1 .. (z-1)//2
        for k in range(d//2+1,(z-1)//2+1):
            s=sum(r[i]*r[k-i] for i in range(max(0,k-d//2),min(k,d//2)+1) if i in r and (k-i) in r)
            if z*s!=p[k]: ok=False
        if ok: return True,r
    return False,None
for z in (3,5,7,11,13,17,19):
    ok,r=test(z); print(f"z={z}: identity P_z + c u^(z-1) = z R^2 exists over Q: {ok}",("R coeffs "+str(r)) if ok else "")
