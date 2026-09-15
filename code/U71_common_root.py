"""Exact U71 certificates; no unbounded Diophantine search or rank assumption.

All discovery data are rechecked exactly. Approximate discovery is not used
by this verifier, nor to establish the completeness of the ideal list.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction
from math import factorial, comb
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
Vector = tuple[int, ...]


def mul(a: Vector, b: Vector, modulus: int) -> Vector:
    if len(a) != 10 or len(b) != 10 or modulus < 2:
        raise ValueError('Expected rank-ten vectors and modulus >= 2')
    c = [0] * 10
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[(i+j) % 10] += x*y*(-4 if i+j >= 10 else 1)
    return tuple(x % modulus for x in c)


def power(a: Vector, exponent: int, modulus: int) -> Vector:
    if exponent < 0:
        raise ValueError('Negative exponent')
    out = (1,) + (0,) * 9
    while exponent:
        if exponent & 1:
            out = mul(out, a, modulus)
        a = mul(a, a, modulus)
        exponent //= 2
    return out


def norm(a: Vector) -> int:
    t = sp.Symbol('t')
    return int(sp.resultant(t**10+4, sum(x*t**i for i, x in enumerate(a)), t))


def local_root(q: int, precision: int) -> dict[str, object]:
    """A common-root local survivor, never asserted to be an integer solution."""
    m = q**precision
    one = (1,) + (0,) * 9
    degree = 2 if q == 1019 else 1
    initial = power((1, 1)+(0,)*8, (q**degree-1)//17, q)
    nn = norm(initial) % q
    assert pow(nn, 17, q) == 1
    # 10*12=1 mod17: force the norm of the torsion root to be one.
    scalar = pow(nn, 12, q)
    initial = tuple(x*pow(scalar, -1, q) % q for x in initial)
    assert power(initial, 17, q) == one and norm(initial) % q == 1
    assert any(initial[1:])
    target = (1,)+(0,)*8+(q*pow(2, -1, m) % m,)
    inverse_derivative = tuple(x*pow(17, -1, q) % q for x in initial)
    current = initial
    modulus = q
    for _ in range(1, precision):
        next_modulus = modulus*q
        image = power(current, 17, next_modulus)
        residual = tuple((a-b) % next_modulus for a, b in zip(target, image))
        assert all(x % modulus == 0 for x in residual)
        correction = mul(tuple(x//modulus for x in residual), inverse_derivative, q)
        current = tuple((a+modulus*b) % next_modulus for a, b in zip(current, correction))
        assert power(current, 17, next_modulus) == tuple(x % next_modulus for x in target)
        modulus = next_modulus
    n = norm(current) % m
    assert pow(n, 17, m) == (1+256*q**10) % m
    return {'q': q, 'precision': precision, 'initial': list(initial),
            'root': list(current), 'norm': n, 'power_residual_zero': True,
            'norm_power_residual_zero': True}


def main() -> None:
    cert = json.loads((ROOT/'references/U71/certificate.json').read_text())
    t, r, x, y, z = sp.symbols('t r x y z')
    f = t**10+4
    B = sp.Matrix(cert['basis4'])/4
    basis = [sum(B[k,j]*t**k for k in range(10)) for j in range(10)]
    assert B.det() == sp.Rational(1,128)
    order_disc = sp.discriminant(f,t)*B.det()**2
    assert order_disc == -160000000000
    # The ten displayed elements are integral; the last two have explicit
    # monic equations. The span is also checked to be a ring.
    assert sp.rem(basis[8]**10+2*basis[8]**5+2,f,t) == 0
    assert sp.rem(basis[9]**10+4*basis[9]**5+8,f,t) == 0
    for a in basis:
        for b in basis:
            prod = sp.Poly(sp.rem(a*b,f,t),t)
            coordinates = B.inv()*sp.Matrix([prod.nth(i) for i in range(10)])
            assert all(v.q == 1 for v in coordinates)
    bound = Fraction(factorial(10),10**10)*Fraction(40,31)**5*400000
    assert bound < 520
    by_prime: dict[int,list[list[object]]] = {}
    for p, g, v in cert['rows']:
        by_prime.setdefault(p,[]).append([p,g,v])
        gp = sp.Poly(sum(a*t**i for i,a in enumerate(g)),t,modulus=p)
        assert gp.is_irreducible and gp.LC() == 1
        assert sp.rem(sp.Poly(f,t,modulus=p),gp).is_zero
        assert p**gp.degree() < 520
        candidate = sum(sp.Rational(a,4)*t**i for i,a in enumerate(v))
        assert sp.resultant(f,candidate,t) == p**gp.degree()
        assert sp.rem(sp.Poly(4*candidate,t,modulus=p),gp).is_zero
        coordinates = B.inv()*sp.Matrix(v)/4
        assert all(a.q == 1 for a in coordinates)
    actual=[]
    for p in sp.primerange(3,520):
        if p == 5: continue
        for g,multiplicity in sp.factor_list(sp.Poly(f,t,modulus=p))[1]:
            assert multiplicity == 1
            if p**g.degree() < 520:
                actual.append([int(p),[int(g.nth(i))%p for i in range(g.degree()+1)]])
    claimed = [[p,g] for p,g,_ in cert['rows']]
    assert sorted(actual) == sorted(claimed)
    assert len(claimed) == 89
    for p,v in cert['ramified']:
        candidate=sum(sp.Rational(a,4)*t**i for i,a in enumerate(v))
        assert sp.resultant(f,candidate,t) == p
    # Prime 5's generator rho+i and its conjugate differ by 2i, a 5-adic unit.
    p5 = sum(sp.Rational(a,4)*t**i for i,a in enumerate(cert['ramified'][1][1]))
    assert sp.expand(p5-p5.subs(t,-t)) == t**5
    assert sp.rem(t**10,f,t) == -4
    q = 17**4
    tvec=(0,1)+(0,)*8
    assert power(tvec,q,17) == tvec
    logs=[]
    for v in cert['units']:
        candidate=sum(sp.Rational(a,4)*t**i for i,a in enumerate(v))
        assert sp.resultant(f,candidate,t) == 1
        assert all(a.q == 1 for a in B.inv()*sp.Matrix(v)/4)
        image=list(power(tuple(a*pow(4,-1,289)%289 for a in v),q-1,289))
        image[0]=(image[0]-1)%289
        assert all(a%17==0 for a in image)
        logs.append([a//17 for a in image])
    assert logs == cert['unit_logs']
    mat=sp.Matrix.hstack(*(sp.Matrix(v) for v in logs),sp.eye(10)[:,0],sp.eye(10)[:,9])
    minor=mat[cert['rank_rows'],:]
    assert minor.det() == cert['rank_determinant'] == -28765
    assert minor.det()%17 == 16
    # Full Gaussian necessary residue test including all scales and both axes.
    fifth={pow(a,5,11) for a in range(11)}
    gaussian=[]
    for ca,cb,dg,dh in [(1,16,1,1),(17**4,16,17,1),(1,16*17**4,1,17)]:
        survivors=[]
        for A in range(11):
            for C in range(11):
                if A==C==0: continue
                a,b=ca*pow(A,5,11)%11, cb*pow(C,5,11)%11
                G=sum((-1)**j*comb(17,2*j)*a**(16-2*j)*b**(2*j) for j in range(9))%11
                H=sum((-1)**j*comb(17,2*j+1)*a**(16-2*j)*b**(2*j) for j in range(9))%11
                if G*pow(dg,-1,11)%11 in fifth and H*pow(dh,-1,11)%11 in fifth:
                    survivors.append([A,C])
        gaussian.append(survivors)
    assert list(map(len,gaussian)) == [0,0,10]
    assert all(C==0 and A!=0 for A,C in gaussian[2])
    master=x+y*t**9/2
    assert sp.expand(sp.resultant(f,master,t)-x**10-256*y**10)==0
    assert sp.rem(master*master.subs(t,-t)-(x*x+y*y*t**8),f,t)==0
    assert sp.expand(sp.resultant(r**5-2,x+sp.I*r**4*y,r)-x**5-16*sp.I*y**5)==0
    # Sharp finite check of the newly forced valuation at17: a principal root
    # exists locally for X=1,Y=17^2. It is not a rational integer solution.
    n=9;modulus=17**n;target=(1,)+(0,)*8+(17**2*pow(2,-1,modulus)%modulus,)
    delta=(1,)+(0,)*8+(17*pow(2,-1,modulus)%modulus,)
    for k in range(3,n):
        m=17**(k+1);value=power(delta,17,m)
        residual=tuple((a-b)%m for a,b in zip(target,value))
        assert all(a%17**k==0 for a in residual)
        # delta == 1 mod17, so the divided derivative is one mod17.
        delta=tuple((a+17**(k-1)*(b//17**k))%m for a,b in zip(delta,residual))
    assert power(delta,17,modulus)==target
    local=[local_root(p,6) for p in [1019,2381]]
    summary={'order_discriminant':int(order_disc),'minkowski_upper':str(bound),
             'unramified_prime_ideals_certified':89,'ramified_prime_ideals_certified':3,
             'unit_norms':[1]*4,'unit_logs':logs,'minor_determinant':-28765,
             'minor_mod17':16,'gaussian_case_counts':[0,0,10],
             'common_norm_identities':True,'local_e17_equals2_survives':True,
             'full_Beal_solved':False}
    print(json.dumps({'checkpoint':'U71','summary':summary,'local_common_roots':local,
                      'local_17_root':list(delta)},indent=2))


if __name__=='__main__':main()
