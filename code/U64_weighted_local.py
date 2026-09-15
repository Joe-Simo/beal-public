"""Exact U64 Eisenstein certificate and corrected, bounded Hecke comparisons.

No integer-height exclusion or newspace-completeness claim is made.
"""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
Pair = tuple[int, int]


def frey(x: int, u: int, v: int) -> int:
    return x**5 + 40*u*v*x**3 + 320*u*u*v*v*x + 64*(8*v**5-u**5)


def mul(a: Pair, b: Pair, p: int, d: int) -> Pair:
    return ((a[0]*b[0]+d*a[1]*b[1]) % p,
            (a[0]*b[1]+a[1]*b[0]) % p)


def fp2_power(a: Pair, n: int, p: int, d: int) -> Pair:
    out = (1, 0)
    for _ in range(n):
        out = mul(out, a, p, d)
    return out


def traces_at(p: int) -> list[dict[str, int]]:
    """Every square/twice-square pair, excluding singular fibers explicitly."""
    assert sp.isprime(p) and p not in (2, 5, 17)
    d = next(t for t in range(2, p) if pow(t, (p-1)//2, p) == p-1)
    elements = [(a,b) for a in range(p) for b in range(p)]
    squares2 = Counter(mul(a,a,p,d) for a in elements)
    squares1 = Counter(a*a % p for a in range(p))
    powers = [(x, fp2_power(x,3,p,d), fp2_power(x,5,p,d)) for x in elements]
    sq = sorted(squares1)
    twice = sorted({2*x % p for x in sq})
    rows: list[dict[str, int]] = []
    for u in sq:
        for v in twice:
            if (u**5+8*v**5) % p == 0:
                continue
            n1 = 1 + sum(squares1[-frey(x,u,v) % p] for x in range(p))
            c3,c1,c0 = 40*u*v,320*u*u*v*v,64*(8*v**5-u**5)
            n2 = 1 + sum(squares2[((-x5[0]-c3*x3[0]-c1*x[0]-c0) % p,
                                   (-x5[1]-c3*x3[1]-c1*x[1]) % p)]
                         for x,x3,x5 in powers)
            total = p+1-n1
            numerator = total*total-(p*p+1-n2)
            assert numerator % 2 == 0
            product = numerator//2-2*p
            rows.append({'U':u,'V':v,'Np':n1,'Np2':n2,'S':total,'P':product})
    return rows


def main() -> None:
    u,v,t = sp.symbols('u v t')
    f = frey(t,u,v)
    shifted = sp.Poly(sp.expand(f.subs(t,t-u-2*v)),t)
    cs = [sp.expand(shifted.nth(i)) for i in range(6)]
    assert cs[-1] == 1
    assert all(int(k) % 5 == 0 for c in cs[:-1] for k in sp.Poly(c,u,v).coeffs())
    residual = sp.Poly(sp.expand(cs[0]/5-2*(u**5+8*v**5)),u,v)
    assert all(int(k) % 5 == 0 for k in residual.coeffs())
    assert sp.factor(sp.discriminant(f,t)) == 2**24*5**5*(u**5+8*v**5)**4
    pairs = [(a,b) for a in range(25) for b in range(25) if (a**5+8*b**5) % 5]
    assert len(pairs) == 500
    roots = [(a,b,x) for a,b in pairs for x in range(25) if frey(x,a,b) % 25 == 0]
    assert roots == []
    assert all(frey(-a-2*b,a,b) % 5 == 0 and frey(-a-2*b,a,b) % 25 != 0
               for a,b in pairs)
    # The unit hypothesis is essential to this Eisenstein argument.
    assert frey(-1-2*3,1,3) % 25 == 0
    cyclotomic = sp.cyclotomic_poly(17, t)
    gauss = sum(int(sp.legendre_symbol(a, 17))*t**a for a in range(1, 17))
    assert sp.rem(gauss**2-17, cyclotomic, t) == 0
    for a in range(1, 17):
        assert sp.rem(gauss.subs(t, t**a)-int(sp.legendre_symbol(a, 17))*gauss,
                      cyclotomic, t) == 0
    e = sp.Symbol('e')
    data = json.loads((ROOT/'references/U64/hecke_records.json').read_text())
    q11 = traces_at(11)
    signature_counts = Counter((r['S'],r['P']) for r in q11)
    assert signature_counts == {(-3,-9):25,(1,-1):5,(9,19):5}
    form_rows = []
    for name,rec in data['records'].items():
        polynomial = sum(c*e**i for i,c in enumerate(rec['minpoly_ascending']))
        a,b = [c[0]+c[1]*e for c in rec['prime11_linear_pairs']]
        sm,prod = sp.rem(a+b,polynomial,e), sp.rem(a*b,polynomial,e)
        assert sm.is_Integer and prod.is_Integer
        matches = [r for r in q11 if (r['S']-int(sm)) % 17 == 0 and (r['P']-int(prod)) % 17 == 0]
        form_rows.append({'suffix':name,'sum':int(sm),'product':int(prod),
                          'compatible_parameter_pairs':len(matches)})
    assert [r['suffix'] for r in form_rows if r['compatible_parameter_pairs']] == ['b']
    assert all(r['V'] == 0 for r in q11 if r['S'] == 9 and r['P'] == 19)
    # Diagnostic comparisons for the surviving orbit, not its global identification.
    bpoly = e**2-9*e+19
    bvalues = {11:(9-e,e),19:(sp.Integer(0),sp.Integer(0)),
               31:(-e-1,e-10),41:(11*e-50,-11*e+49)}
    local = []
    for p,(a,b) in bvalues.items():
        sm,prod = int(sp.rem(a+b,bpoly,e)),int(sp.rem(a*b,bpoly,e))
        rows = q11 if p == 11 else traces_at(p)
        matches = [r for r in rows if (r['S']-sm) % 17 == 0 and (r['P']-prod) % 17 == 0]
        boundary = next(r for r in rows if r['U']==1 and r['V']==0)
        assert (boundary['S'],boundary['P']) == (sm,prod)
        toric_norm = int(sp.resultant(bpoly,a*a-(p+1)**2,e))
        assert toric_norm % 17 != 0
        sq = {x*x % p for x in range(p)};twice={2*x % p for x in sq}
        toric_pairs = sum(1 for uu in sq for vv in twice
                          if (uu, vv) != (0, 0) and (uu**5+8*vv**5) % p == 0)
        ratios = sorted({r['V']*pow(r['U'],-1,p) % p for r in matches if r['U']})
        local.append({'prime':p,'form_b_sum_product':[sm,prod],
                      'good_pairs':len(rows),'toric_nonzero_pairs':toric_pairs,
                      'compatible_good_pairs':len(matches),'boundary':boundary,
                      'compatible_V_over_U':ratios,'compatible_U_zero':sum(r['U']==0 for r in matches),
                      'toric_norm_mod17':toric_norm % 17,'rows':rows})
    print(json.dumps({'checkpoint':'U64','status':'completed','full_Beal_solved':False,
          'arithmetic':'Exact Python integers and SymPy',
          'eisenstein':{'shift_coefficients_ascending':[str(c) for c in cs],
                       'constant_quotient_mod5':'2*(U^5+8*V^5)',
                       'all_lower_coefficients_divisible_by5':True,
                       'mod25_parameter_pairs':500,'roots_mod25':roots},
          'cyclotomic_quadratic_certificate':{'gauss_sum_squared_mod_Phi17':17,
                       'automorphisms_checked':16,'quadratic_subfield':'Q(sqrt(17))'},
          'prime11_recovered_forms':form_rows,'unchecked_orbits':['h'],
          'form_b_diagnostics':local},indent=2))

if __name__ == '__main__':
    main()
