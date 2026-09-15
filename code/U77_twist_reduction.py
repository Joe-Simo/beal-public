"""Exact U77 algebra, good-reduction and cyclic-orbit certificates.

No rank upper bound is computed. Finite-field points are not number-field
points. The conceptual descent is in the accompanying written proof.
"""
from __future__ import annotations
import json
from math import gcd
import sympy as sp

PRIMES = (1021, 1361, 1531)
Vector = tuple[int, ...]


def finite_mul(a: Vector, b: Vector, q: int, c5: int) -> Vector:
    if len(a) != 5 or len(b) != 5:
        raise ValueError('Expected two rank-five field vectors')
    out = [0]*5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[(i+j) % 5] += x*y*(c5 if i+j >= 5 else 1)
    return tuple(x % q for x in out)


def finite_power(a: Vector, n: int, q: int, c5: int) -> Vector:
    if n < 0:
        raise ValueError('Power exponent must be nonnegative')
    out = (1, 0, 0, 0, 0)
    while n:
        if n & 1:
            out = finite_mul(out, a, q, c5)
        a = finite_mul(a, a, q, c5)
        n //= 2
    return out


def orbit_example() -> dict[str, object]:
    q, zeta, iroot = 41, 10, 9
    c5 = 16*iroot % q
    x = sp.Symbol('x')
    assert sp.Poly(x**5-c5, x, modulus=q).is_irreducible
    order = q**5-1
    assert gcd(17, order) == 1
    inverse = pow(17, -1, order)
    phi = (1+zeta+pow(zeta, -1, q)) % q
    eps = (zeta*zeta-pow(zeta, 3, q)) % q
    def scale(a: Vector, n: int) -> Vector:
        return tuple(n*x % q for x in a)
    def add(a: Vector, b: Vector) -> Vector:
        return tuple((x+y) % q for x,y in zip(a,b))
    def mul(a: Vector,b: Vector) -> Vector:
        return finite_mul(a,b,q,c5)
    def power(a: Vector,n: int) -> Vector:
        return finite_power(a,n,q,c5)
    def invert(a: Vector) -> Vector:
        assert a != (0,)*5
        return power(a,order-1)
    one = (1,0,0,0,0)
    c = (0,1,0,0,0)
    examples=[]
    for sign in (1,-1):
        taus = [add(one,scale(c,sign*pow(zeta,j,q))) for j in range(5)]
        roots = [power(t,inverse) for t in taus]
        assert all(power(r,17)==t for r,t in zip(roots,taus))
        uvals=[];vvals=[];xvals=[]
        for j in range(5):
            u=mul(mul(roots[(j+1)%5],roots[(j-1)%5]),invert(power(roots[j],2)))
            s=scale(c,sign*pow(zeta,j,q))
            v=scale(mul(add(one,scale(s,-1)),invert(add(one,s))),eps)
            assert add(power(v,2),scale(power(u,17),4)) == scale(one,phi*phi)
            xx=mul(taus[(j+1)%5],invert(taus[j]))
            assert xx == scale(add(scale(one,1+zeta),scale(v,pow(zeta,3,q))),pow(2,-1,q))
            uvals.append(u);vvals.append(v);xvals.append(xx)
        assert len(set(uvals)) == len(set(xvals)) == 5
        assert all(v!=(0,)*5 for v in vvals)
        vand=one
        for j in range(5):
            for k in range(j):
                vand=mul(vand,add(uvals[j],scale(uvals[k],-1)))
        assert vand != (0,)*5
        vand_norm=power(vand,(q**5-1)//(q-1))
        assert all(a==0 for a in vand_norm[1:]) and vand_norm[0]!=0
        coeffs=[one]
        for xx in xvals:
            nxt=[(0,)*5 for _ in range(len(coeffs)+1)]
            for j,co in enumerate(coeffs):
                nxt[j]=add(nxt[j],scale(mul(co,xx),-1))
                nxt[j+1]=add(nxt[j+1],co)
            coeffs=nxt
        assert all(all(v==0 for v in co[1:]) for co in coeffs)
        examples.append({'sign':sign,'theta_roots':[list(r) for r in roots],
                         'u_values':[list(r) for r in uvals],
                         'v_values':[list(r) for r in vvals],
                         'x_polynomial':[co[0] for co in coeffs],
                         'vandermonde_norm':vand_norm[0]})
    assert examples[0]['x_polynomial']!=examples[1]['x_polynomial']
    return {'q':q,'zeta':zeta,'i':iroot,'c5':c5,'X':1,'Y':1,
            'scope':'one finite-field example, not a global solution','orbits':examples}


def reductions() -> list[dict[str, object]]:
    u=sp.Symbol('u');phi17=sum(u**j for j in range(17));records=[]
    for q in PRIMES:
        assert sp.isprime(q) and q%85==1
        g=int(sp.primitive_root(q));zeta=pow(g,(q-1)//5,q)
        ph=(1+zeta+pow(zeta,-1,q))%q
        delta=(3-ph)%q;eps=(zeta*zeta-pow(zeta,3,q))%q
        assert eps*eps%q == (-delta)%q
        sign=1 if pow(delta,(q-1)//2,q)==1 else -1
        assert sign==(1 if q%4==1 else -1)
        logs={pow(g,j,q):j%17 for j in range(q-1)}
        assert len(logs)==q-1
        d=(1+zeta)%q;counts=[0]*17
        for t in range(1,q):
            if t!=d:counts[(logs[t]+logs[(d-t)%q])%17]+=1
        assert sum(counts)==q-2
        S=sum(v*u**j for j,v in enumerate(counts))
        jac=int(sp.resultant(phi17,1+sign*S,u))
        assert jac>0
        character=lambda t: 0 if t%q==0 else (1 if pow(t%q,(q-1)//2,q)==1 else -1)
        count=1+sum(1+character((ph+2-4*delta*pow(t,17,q))%q) for t in range(q))
        traceS=16*counts[0]-sum(counts[1:])
        assert count==q+1+sign*traceS
        records.append({'q':q,'generator':g,'zeta':zeta,'phi':ph,'delta':delta,
                        'quadratic_character_delta':sign,'character_counts':counts,
                        'curve_points':count,'jacobian_order':str(jac)})
    orders=[int(r['jacobian_order']) for r in records]
    assert gcd(gcd(orders[0],orders[1]),orders[2])==1
    for i,q in enumerate(PRIMES):
        assert any(orders[j]%q for j in range(3) if i!=j)
    return records


def main() -> None:
    z,s,h,x,l,U,V,p=sp.symbols('z s h x l U V p')
    cyc=sum(z**j for j in range(5))
    phi=1+z+z**4;eps=z**2-z**3;delta=3-phi
    red=lambda a: sp.rem(sp.expand(a),cyc,z)
    assert red(phi**2-phi-1)==0
    assert red(eps**2+delta)==0
    assert red(1+z+z**3*phi)==0
    assert red(eps.subs(z,z**4)+eps)==0
    assert red(phi.subs(z,z**4)-phi)==0
    assert red(delta*phi**2-phi-2)==0
    # The original C_1 coordinates and the normalized hyperelliptic curve.
    xn=(1+z*s)/(1+s);vn=eps*(1-s)/(1+s)
    r17=(1+z*s)*(1+z**4*s)/(1+s)**2
    assert red(sp.cancel((vn**2-phi**2+4*r17)*(1+s)**2))==0
    assert red(sp.cancel((2*xn-(1+z)-z**3*vn)*(1+s)))==0
    # Two distinct cyclic orbit parameters cannot have the same u^17.
    diff=sp.cancel((s/(1+s)**2-h*s/(1+h*s)**2)*(1+s)**2*(1+h*s)**2)
    assert sp.expand(diff-s*(1-h)*(1-h*s*s))==0
    P=(x-1)**5;Q=(x-z)**5
    hdiff=sp.expand((P+l*Q)*(1-l)-(P-l*Q)*(1+l))
    assert sp.expand(hdiff-2*l*(Q-P))==0
    assert sp.Poly(Q-P,x).coeff_monomial(x**4)==5*(1-z)
    # Character bookkeeping for Gal(B/k)=<eta,kappa> on the class Z.
    chars={'eta':-1,'kappa':-1,'eta_kappa':1}
    assert [chars['eta']**2,chars['kappa']**2,chars['eta']*chars['kappa']]==[1,1,1]
    # q0=i*eps has square delta and changes sign under both generators.
    assert red(-eps**2-delta)==0
    # Model v^2=phi+2-4(3-phi)u^17; discriminant has only 2,5,17 support.
    fieldpoly=p*p-p-1
    f=p+2-4*(3-p)*U**17
    discriminant=sp.rem(sp.discriminant(f,U),fieldpoly,p)
    dn=sp.resultant(fieldpoly,discriminant,p)
    assert set(sp.factorint(abs(int(dn)))) <= {2,5,17}
    rec=reductions();example=orbit_example()
    out={'checkpoint':'U77','summary':{
        'symbolic_identities_verified':True,
        'twist':'(3-phi)w^2=phi^2-4u^17, phi^2-phi-1=0',
        'integral_model':'v^2=phi+2-4(3-phi)u^17',
        'base_field_degree':2,'genus':8,
        'torsion_order':1,'rank_upper_bound_computed':False,
        'rank_positive_is_necessary_for_weighted_solution':True,
        'known_smaller_field_subgroup_saturation_excluded_as_target':True,
        'full_Beal_solved':False},
        'reduction_records':rec,
        'character_signs':chars,
        'model_discriminant_norm_factorization':{str(k):v for k,v in sp.factorint(abs(int(dn))).items()},
        'finite_orbit_example':example}
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
