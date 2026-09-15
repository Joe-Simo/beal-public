"""Exact U67 checks; finite domains are stated in each returned record.

The new identities are unconditional implications of the two element-power
identities. The imported weighted-to-quintic implication is separately audited.
No finite search here proves the weighted equation or the full Beal conjecture.
"""
from __future__ import annotations

import json
from collections import Counter
from itertools import product
from math import gcd

import sympy as sp

Vec = tuple[int, ...]


def multiply(a: Vec, b: Vec, modulus: int) -> Vec:
    """Full degree-five quotient, rho**5=2; no division by any element."""
    if len(a) != 5 or len(b) != 5 or modulus < 2:
        raise ValueError('Invalid quintic algebra input')
    result = [0] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            power = i + j
            result[power % 5] += x * y * (2 if power >= 5 else 1)
    return tuple(x % modulus for x in result)


def power(a: Vec, exponent: int, modulus: int) -> Vec:
    if exponent < 0:
        raise ValueError('Nonnegative exponent required')
    out = (1, 0, 0, 0, 0)
    while exponent:
        if exponent % 2:
            out = multiply(out, a, modulus)
        a = multiply(a, a, modulus)
        exponent //= 2
    return out


def solve_two_columns(x: Vec, y: Vec, target: Vec) -> tuple[int, int] | None:
    """Solve all five equations over F17, rejecting inconsistent rows only."""
    for i in range(5):
        for j in range(i + 1, 5):
            det = (x[i] * y[j] - x[j] * y[i]) % 17
            if det:
                inv = pow(det, -1, 17)
                a = (target[i] * y[j] - target[j] * y[i]) * inv % 17
                b = (x[i] * target[j] - x[j] * target[i]) * inv % 17
                if all((a * x[k] + b * y[k] - target[k]) % 17 == 0 for k in range(5)):
                    return a, b
                return None
    raise ArithmeticError('Rank failure; no pruning is allowed here')


def upstream_certificate() -> dict[str, object]:
    """Rebuild the new remote U65 sieve independently in its unsplit algebra."""
    modulus = 289
    q = 17**4
    unit_vectors = [(-1, 1, 0, 0, 0), (1, 1, 0, 1, 0)]
    logs = []
    for unit in unit_vectors:
        coeffs = list(power(unit, q - 1, modulus))
        coeffs[0] = (coeffs[0] - 1) % modulus
        assert all(c % 17 == 0 for c in coeffs)
        logs.append(tuple(c // 17 for c in coeffs))
    assert logs == [(0, 10, 4, 3, 12), (0, 14, 13, 7, 6)]
    assert power((0, 1, 0, 0, 0), q, 17) == (0, 1, 0, 0, 0)
    square_roots: dict[int, list[int]] = {}
    twice_square_roots: dict[int, list[int]] = {}
    for x in range(modulus):
        square_roots.setdefault(x * x % modulus, []).append(x)
        twice_square_roots.setdefault(2 * x * x % modulus, []).append(x)
    scalar_image = {pow(x, 17, modulus) for x in range(modulus)}
    assert len(scalar_image) == 17
    norm_count = 0
    rows = []
    for u, v in product(sorted(square_roots), sorted(twice_square_roots)):
        if u % 17 == 0 and v % 17 == 0:
            continue
        if (pow(u, 5, modulus) + 8 * pow(v, 5, modulus)) % modulus not in scalar_image:
            continue
        norm_count += 1
        gamma = (u, 0, 0, v, 0)
        pq = power(gamma, q, modulus)
        dif = tuple((a - b) % modulus for a, b in zip(pq, gamma))
        assert all(c % 17 == 0 for c in dif)
        target = tuple(c // 17 for c in dif)
        columns = [multiply(gamma, li, 17) for li in logs]
        solution = solve_two_columns(columns[0], columns[1], target)
        if solution is None:
            continue
        witnesses = []
        for x, y in product(square_roots[u], twice_square_roots[v]):
            re = pow(x, 5, modulus)
            im = 16 * pow(y, 5, modulus) % modulus
            if ((re + 38 * im) % modulus in scalar_image
                    and (re - 38 * im) % modulus in scalar_image):
                witnesses.append([x, y])
        rows.append({'U': u, 'V': v, 'unit_class': list(solution), 'witnesses': witnesses})
    good = [row for row in rows if row['witnesses']]
    distribution = Counter(tuple(row['unit_class']) for row in rows)
    assert norm_count == 1104
    assert distribution == {(0, 0): 16, (0, 14): 8}
    assert len(good) == 16
    assert sum(len(row['witnesses']) for row in good) == 544
    assert all(row['unit_class'] == [0, 0] for row in good)
    assert all((row['U'] == 0) != (row['V'] == 0) for row in good)
    return {'source_revision': 'a15e419765463f68a641ed71fd549aafae2cc95d',
            'domain_square_pairs': 18768, 'norm_survivors': norm_count,
            'full_algebra_unit_logs': [list(x) for x in logs],
            'classes_before_gaussian': [{'class': list(k), 'count': v}
                                        for k, v in sorted(distribution.items())],
            'gaussian_survivor_pairs': len(good), 'gaussian_witnesses': 544,
            'rows': rows}


def symbolic_certificates() -> dict[str, object]:
    r, a, v, z, x, u = sp.symbols('r a v z x u')
    quotient = r**4 + a*r**3 + a*a*r*r + a**3*r + a**4
    partial_norm = sp.resultant(quotient, v*(r**3-a**3), r)
    assert sp.expand(partial_norm-5*a**12*v**4) == 0
    phi5 = z**4+z**3+z*z+z+1
    phi = 1+z+z**4
    assert sp.rem(phi**2-phi-1, phi5, z) == 0
    assert sp.rem((1+z)+z**3*phi, phi5, z) == 0
    assert sp.rem((-z)**17*(1+z)-phi, phi5, z) == 0
    cyclotomic_product = sp.rem(sp.prod(1-z**j for j in range(1, 5)), phi5, z)
    assert cyclotomic_product == 5
    # This is the seventeenth power of X*s/t^5 after substituting
    # s^17=5X^8 and t^17=2X^5. No formal seventeenth-root simplifier is used.
    witness_power = sp.cancel(x**17*(5*x**8)/(2*x**5)**5)
    assert witness_power == sp.Rational(5, 32)
    # The quotient factor and linear factor are comaximal modulo N:
    # h(a)=5*a^4, a and 5 are units.
    assert sp.expand(quotient.subs(r, a)) == 5*a**4
    aa = u*u/(2*v*v)
    norm = u**5+8*v**5
    assert sp.cancel((aa**5-2)*32*v**10 - norm*(u**5-8*v**5)) == 0
    assert sp.cancel((v*aa**3+u)*8*v**5 - u*norm) == 0
    assert sp.gcd(sp.Poly(phi5, z, modulus=17), sp.Poly(sp.diff(phi5, z), z, modulus=17)).degree() == 0
    assert sp.Poly(phi5, z, modulus=17).is_irreducible
    # Defining polynomial of phi^(1/17); this is not itself the whole field T.
    root_polynomial = z**34-z**17-1
    root_resultant = sp.resultant(u*u-u-1, z**17-u, u)
    assert sp.expand(root_resultant-root_polynomial) == 0
    return {'quartic_norm': str(partial_norm), 'cyclotomic_product': 5,
            'unit_minimal_polynomial_check': True, 'root_of_phi_formula': True,
            'rational_kummer_witness_power': str(witness_power),
            'linear_root_and_factor_checks': True,
            'phi_radical_polynomial': str(root_polynomial),
            'base_degree_over_Q': 32, 'kummer_degree_over_base': 289,
            'total_field_degree': 9248,
            'CM_torsion_degree_divisor': 4*(17**4-1),
            'coprime_extension_degrees': gcd(17**2, 4*(17**4-1))}


def named_residue_tests() -> list[dict[str, object]]:
    # Named witnesses test each separate Kummer obstruction, not a height range.
    ans = []
    for p in [2381, 17681, 610301]:
        assert sp.isprime(p) and p % 340 == 1
        zeta = pow(int(sp.primitive_root(p)), (p-1)//5, p)
        assert zeta != 1 and pow(zeta, 5, p) == 1
        phi = (1+zeta+pow(zeta, -1, p)) % p
        assert (phi*phi-phi-1) % p == 0
        c = 5*pow(32, -1, p) % p
        c_char = pow(c, (p-1)//17, p)
        phi_char = pow(phi, (p-1)//17, p)
        # A toric residue with Y=1 exists; retain every tenth root.
        roots = sorted(int(t) for t in sp.nthroot_mod(-256 % p, 10, p, all_roots=True))
        assert len(roots) == 10
        assert all((pow(t, 10, p)+256) % p == 0 for t in roots)
        y = next(t for t in range(1, p) if pow(2*pow(roots[0]*t % p, 5, p) % p, (p-1)//17, p) == 1)
        witness_x = roots[0]*y % p
        witness_gauss = 2*pow(witness_x, 5, p) % p
        assert pow(witness_gauss, (p-1)//17, p) == 1
        ans.append({'q': p, 'gaussian_toric_witness': [witness_x, y], 'zeta': zeta, 'phi': phi, 'c': c,
                    'c_character': c_char, 'phi_character': phi_char,
                    'c_passes': c_char == 1, 'phi_passes': phi_char == 1,
                    'toric_X_roots_for_Y_1': roots})
    assert [(r['c_passes'], r['phi_passes']) for r in ans] == [(False, False), (True, False), (False, True)]
    return ans


def toric_equivalence_check() -> list[dict[str, object]]:
    """Exhaust the new equivalence in the split primes q=241, q=2381 and q=17681.

    Keep all nonzero X,Y with X^10+256Y^10=0 and the Gaussian power condition.
    Compare the entire quintic power condition with the two constant tests.
    All fields split here; no projective scale is thrown away.
    """
    records = []
    for p in [241, 2381, 17681]:
        assert sp.isprime(p) and p % 20 == 1
        rho_roots = [int(t) for t in sp.nthroot_mod(2, 5, p, all_roots=True)]
        ratios = [int(t) for t in sp.nthroot_mod(-256 % p, 10, p, all_roots=True)]
        image = {pow(x, 17, p) for x in range(p)}
        i = int(sp.sqrt_mod(-1, p))
        phis = [(1+int(s))*pow(2, -1, p) % p for s in sp.sqrt_mod(5, p, all_roots=True)]
        const_pass = (5*pow(32, -1, p) % p in image and all(t in image for t in phis))
        toric = gaussian = joint = 0
        for ratio, y in product(ratios, range(1, p)):
            x = ratio*y % p
            toric += 1
            re, im = pow(x, 5, p), 16*pow(y, 5, p) % p
            if (re+i*im) % p not in image or (re-i*im) % p not in image:
                continue
            gaussian += 1
            gamma = [(x*x+2*pow(r, 3, p)*y*y) % p for r in rho_roots]
            assert len(rho_roots) == 5
            has_quintic_root = all(c in image for c in gamma)
            assert has_quintic_root == const_pass
            joint += has_quintic_root
        assert toric > 0 and gaussian > 0
        records.append({'q': p, 'toric_pairs': toric, 'gaussian_pairs': gaussian,
                        'joint_pairs': joint, 'constant_tests': const_pass})
    return records



def surviving_local_witness() -> dict[str, object]:
    """An actual joint residue witness; it is not an integer solution."""
    z = sp.Symbol('z')
    beta = (1, 6, 3, 0, 7)
    quintic_image = power(beta, 17, 13)
    gaussian = sp.Poly(sp.rem((5+z)**17, z*z+1, z), z, modulus=13)
    gaussian_image = [int(gaussian.nth(j)) % 13 for j in range(2)]
    phi_power = sp.Poly(sp.rem((3+5*z)**17, z*z-z-1, z), z, modulus=13)
    phi_image = [int(phi_power.nth(j)) % 13 for j in range(2)]
    assert quintic_image == (10, 0, 0, 2, 0)
    assert gaussian_image == [2, 3] and phi_image == [0, 1]
    assert (6**10+256) % 13 == 0 and pow(9, 17, 13) == 3
    return {'q': 13, 'X_Y_Z_residues': [6, 1, 0], 'beta': list(beta),
            'beta_power': list(quintic_image), 'gaussian_root': [5, 1],
            'gaussian_power': gaussian_image, 'c_root': 9, 'c_root_power': 3,
            'phi_root': [3, 5], 'phi_root_power': phi_image}



def main() -> None:
    out = {'checkpoint': 'U67', 'full_Beal_solved': False,
           'symbolic': symbolic_certificates(),
           'upstream_rebuild': upstream_certificate(),
           'named_residue_tests': named_residue_tests(),
           'toric_equivalence': toric_equivalence_check(),
           'surviving_local_witness': surviving_local_witness(),
           'c_at_17_squared': {'modulus': 289, 'c': 5*pow(32, -1, 289) % 289,
                               'c_to_16': pow(5*pow(32, -1, 289) % 289, 16, 289)}}
    assert out['c_at_17_squared']['c_to_16'] == 256
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
