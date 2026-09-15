"""Exact U75 quotient, Jacobi-sum and non-torsion certificates.

No rank upper bound or global point classification is computed. The group
orders use the Hasse-Davenport formula justified in the accompanying proof.
"""
from __future__ import annotations
import json
from math import gcd
import sympy as sp

PRIMES = (1021, 1361, 2381)

def cyclic_mul(a: list[int], b: list[int]) -> list[int]:
    c = [0] * 17
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[(i+j) % 17] += ai*bj
    return c


def trace(a: list[int]) -> int:
    return 16*a[0]-sum(a[1:])


def binomial_series(numerator: int, p: int, length: int) -> list[int]:
    alpha = numerator*pow(17, -1, p) % p
    out = [1]
    for j in range(1, length):
        out.append(out[-1]*(alpha-j+1)*pow(j, -1, p) % p)
    return out


def jet_record(a: int) -> dict[str, object]:
    p, zeta, length = 41, 10, 10
    assert pow(zeta, 5, p) == 1 and zeta != 1
    ks = [k for k in range(1, 17) if k+(a*k % 17) <= 17]
    assert len(ks) == 8
    columns = [[1]+[0]*9, [1, 1]+[0]*8]
    for k in ks:
        r = a*k % 17
        b = binomial_series(r, p, length)
        c = binomial_series(k, p, length)
        columns.append([pow(zeta, 3*k, p)*sum(
            b[i]*c[n-i]*pow(-pow(zeta,-1,p),n-i,p)
            for i in range(n+1)) % p for n in range(length)])
    rows = [list(row) for row in zip(*columns)]
    det = int(sp.Matrix(rows).det()) % p
    assert det != 0
    return {'a': a, 'k_values': ks, 'jet_matrix_mod41': rows,
            'determinant_mod41': det}


def reduction_records(q: int) -> list[dict[str, object]]:
    assert sp.isprime(q) and q % 340 == 1
    g = int(sp.primitive_root(q))
    logs: dict[int, int] = {}
    v = 1
    for j in range(q-1):
        assert v not in logs
        logs[v] = j % 17
        v = v*g % q
    assert v == 1 and len(logs) == q-1
    zeta, iroot = pow(g,(q-1)//5,q), pow(g,(q-1)//4,q)
    assert pow(zeta,5,q) == 1 and zeta != 1 and iroot*iroot % q == q-1
    d = (1+zeta) % q
    xi = sp.Symbol('xi')
    phi = sum(xi**k for k in range(17))
    seventeenths = {pow(x,17,q) for x in range(1,q)}
    records = []
    for a in range(1,16):
        counts = [0]*17
        for x in range(1,q):
            if x != d:
                counts[(a*logs[x]+logs[(d-x)%q]) % 17] += 1
        assert sum(counts) == q-2
        polynomial = 1+sum(c*xi**j for j,c in enumerate(counts))
        order = int(sp.resultant(phi, polynomial, xi))
        assert order > 0 and order % 17 == 0
        point_count = 3+17*sum(
            pow(x,a,q)*(d-x) % q in seventeenths
            for x in range(q) if x not in (0,d))
        assert point_count == q+1+trace(counts)
        # Jacobi purity is also checked exactly, with no floating-point roots.
        conjugate = [counts[(-j)%17] for j in range(17)]
        normpoly = cyclic_mul(counts, conjugate)
        assert normpoly[0]-q == normpoly[1]
        assert len(set(normpoly[1:])) == 1
        records.append({'q':q, 'generator':g, 'zeta':zeta, 'i':iroot,
                        'a':a, 'character_counts':counts,
                        'curve_points':point_count, 'jacobian_order':str(order)})
    return records


def main() -> None:
    triangular = [[r,s] for r in range(1,17) for s in range(1,17-r)]
    assert len(triangular) == 120
    blocks = []
    for a in range(1,16):
        chars = [[r,s] for r,s in triangular if (r-a*s)%17 == 0]
        assert len(chars) == 8
        # The character projector for this subgroup is 17 here, zero elsewhere.
        for r,s in triangular:
            distribution = [sum((r-a*s)*j % 17 == k for j in range(17))
                            for k in range(17)]
            assert distribution == ([17]+[0]*16 if [r,s] in chars else [1]*17)
        blocks.append({'a':a, 'characters':chars})
    assert sorted(pair for b in blocks for pair in b['characters']) == sorted(triangular)
    pairs = [[a,pow(a,-1,17)] for a in range(1,16) if a <= pow(a,-1,17)]
    assert pairs == [[1,1],[2,9],[3,6],[4,13],[5,7],[8,15],[10,12],[11,14]]
    for a,b in pairs:
        assert a*b-1 == 17*((a*b-1)//17)
    records = [r for q in PRIMES for r in reduction_records(q)]
    gcds=[]; cross=[]
    for a in range(1,16):
        orders = [int(r['jacobian_order']) for r in records if r['a'] == a]
        assert gcd(gcd(*orders[:2]),orders[2]) == 17
        gcds.append(17)
        # Residue characteristic torsion is NOT presumed to inject at itself.
        exclusions=[]
        for j,p in enumerate(PRIMES):
            alternatives=[orders[k] for k in range(3) if k != j]
            assert any(n % p != 0 for n in alternatives)
            exclusions.append([n % p for n in alternatives])
        cross.append({'a':a,'cross_characteristic_residues':exclusions})
    jets=[jet_record(a) for a in range(1,16)]
    # The known rational point is (1,zeta^3) on every quotient.
    z = sp.Symbol('z'); p5=sum(z**j for j in range(5))
    assert sp.rem(z**51-z,p5,z) == 0
    # The common x-coordinate of each projected degree-five orbit has an
    # explicit polynomial; this retains the shared-field condition.
    xx, uu = sp.symbols('xx uu')
    orbit_product = sp.prod((xx-1)+z**j*uu*(xx-z) for j in range(5))
    orbit_formula = (xx-1)**5+uu**5*(xx-z)**5
    assert sp.rem(sp.expand(orbit_product-orbit_formula), p5, z) == 0
    assert sp.expand(orbit_formula.subs(xx,0)) == -uu**5*z**5-1
    for a in range(1,16):
        # y_j=zeta^3*theta_(j+1)^a*theta_(j-1)/theta_j^(a+1).
        powers=[0]*5
        for j in range(5):
            powers[(j+1)%5] += a
            powers[(j-1)%5] += 1
            powers[j] -= a+1
        assert powers == [0]*5
    summary={'common_orbit_polynomial':True,'common_orbit_norms':True,
             'factor_count':15,'factor_genus':8,'jacobian_dimension':120,
             'inverse_pairs':pairs,'torsion_orders':gcds,
             'jet_determinants_mod41':[j['determinant_mod41'] for j in jets],
             'certified_rank_lower_bound':15,
             'rank_upper_bound_computed':False,'degree_five_points_classified':False,
             'full_Beal_solved':False}
    print(json.dumps({'checkpoint':'U75','summary':summary,'character_blocks':blocks,
                      'reduction_records':records,'cross_characteristic_checks':cross,
                      'jets':jets},indent=2))


if __name__ == '__main__':
    main()
