"""Exact U69 certificates. Finite checks are not a rational-point classification."""
from __future__ import annotations

import json
from math import gcd, prod
import sympy as sp

Q_OLD = (1, 13, 18, 33, 38, 47, 52, 67, 69, 72, 84)
JOINT = (1, 67, 69, 137, 203, 273, 339)
FORCERS = (11, 31, 41, 61, 71, 101, 151, 191, 211, 281, 331, 431, 461, 631)
Vector = tuple[int, ...]


def mul(a: Vector, b: Vector, constant: int, modulus: int) -> Vector:
    """Multiplication modulo T^d-constant, by direct cyclic accumulation."""
    if len(a) != len(b) or not a or modulus < 2:
        raise ValueError('Invalid quotient-ring input')
    d = len(a)
    out = [0] * d
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[(i+j) % d] += x*y*(constant if i+j >= d else 1)
    return tuple(v % modulus for v in out)


def power(a: Vector, exponent: int, constant: int, modulus: int) -> Vector:
    if exponent < 0:
        raise ValueError('Negative exponent')
    out = (1,) + (0,) * (len(a)-1)
    while exponent:
        if exponent & 1:
            out = mul(out, a, constant, modulus)
        a = mul(a, a, constant, modulus)
        exponent //= 2
    return out


def norm(a: Vector, constant: int) -> int:
    """Exact norm as the resultant of the defining polynomial and the element."""
    t = sp.Symbol('t')
    return int(sp.resultant(t**len(a)-constant,
                            sum(c*t**i for i, c in enumerate(a)), t))


def lift_root(initial: Vector, target: Vector, q: int, precision: int,
              constant: int) -> Vector:
    """Digit-by-digit Hensel lifting of a seventeenth root starting over F_q."""
    one = (1,) + (0,) * (len(initial)-1)
    assert power(initial, 17, constant, q) == one
    assert tuple(x % q for x in target) == one
    inv_derivative = tuple(x*pow(17, -1, q) % q for x in initial)
    current = initial
    modulus = q
    for _ in range(1, precision):
        next_modulus = modulus*q
        value = power(current, 17, constant, next_modulus)
        difference = tuple((t-v) % next_modulus for t, v in zip(target, value))
        assert all(x % modulus == 0 for x in difference)
        correction = mul(tuple(x//modulus for x in difference), inv_derivative,
                         constant, q)
        current = tuple((b+modulus*c) % next_modulus
                        for b, c in zip(current, correction))
        assert power(current, 17, constant, next_modulus) == tuple(
            x % next_modulus for x in target)
        modulus = next_modulus
    return current


def main() -> None:
    t = sp.Symbol('t')
    rows = []
    for q in sp.primerange(3, 2000):
        if q in (5, 17):
            continue
        factors = sp.factor_list(sp.Poly(t**5-2, t, modulus=q))[1]
        degrees = [f.degree() for f, multiplicity in factors for _ in range(multiplicity)]
        # Relative quotient by scalar units, not the full unit group.
        relative_order = prod(q**d-1 for d in degrees)//(q-1)
        quintic_bad = relative_order % 17 == 0
        old_bad = q % 85 in Q_OLD
        refined_bad = old_bad and not (q % 5 == 1 and pow(2, (q-1)//5, q) != 1)
        assert quintic_bad == refined_bad
        gaussian_order = q - (1 if q % 4 == 1 else -1)
        gaussian_bad = gaussian_order % 17 == 0
        assert gaussian_bad == (q % 68 in (1, 67))
        joint_bad = quintic_bad and gaussian_bad
        predicted_joint = q % 340 in JOINT and (
            q % 340 != 1 or pow(2, (q-1)//5, q) == 1)
        assert joint_bad == predicted_joint
        rows.append({'q': q, 'degrees': sorted(degrees),
                     'quintic_bad': quintic_bad, 'gaussian_bad': gaussian_bad,
                     'joint_bad': joint_bad})
    classes = [r for r in range(1, 340) if gcd(r, 340) == 1
               and r % 85 in Q_OLD and r % 68 in (1, 67)]
    assert tuple(classes) == JOINT
    gaussian_counts = []
    for q in (13, 19, 67, 101, 103, 137):
        kernel = [(a, b) for a in range(q) for b in range(q)
                  if (a*a+b*b) % q == 1 and power((a, b), 17, -1, q) == (1, 0)]
        count = len(kernel)
        assert count == (17 if q % 68 in (1, 67) else 1)
        gaussian_counts.append([q, count])
    fifth_examples = []
    for q in (1021, 1361, 2381, 3061):
        assert sp.isprime(q) and q % 340 == 1
        value = pow(2, (q-1)//5, q)
        fifth_examples.append([q, value, value == 1])

    # A jointly exceptional prime with non-scalar, norm-one torsion in both algebras.
    q, rho0, zeta = 137, 9, 119
    assert pow(rho0, 5, q) == 2 and pow(zeta, 17, q) == 1 and zeta != 1
    idempotent = tuple(pow(rho0, 4-j, q)*pow(5*pow(rho0, 4, q), -1, q) % q
                       for j in range(5))
    assert mul(idempotent, idempotent, 2, q) == idempotent
    delta = pow(zeta, -4, q)
    eta = tuple(((zeta if j == 0 else 0)+(delta-zeta)*idempotent[j]) % q
                for j in range(5))
    assert eta == (67, 116, 89, 86, 40)
    assert power(eta, 17, 2, q) == (1, 0, 0, 0, 0) and norm(eta, 2) % q == 1
    assert all(x != 0 for x in eta[1:4])
    i0 = next(x for x in range(q) if x*x % q == q-1)
    theta = ((zeta+pow(zeta, -1, q))*pow(2, -1, q) % q,
             (zeta-pow(zeta, -1, q))*pow(2*i0, -1, q) % q)
    assert i0 == 37 and theta == (10, 77)
    assert power(theta, 17, -1, q) == (1, 0) and norm(theta, -1) % q == 1
    precision = 12
    modulus = q**precision
    X, Y = 1, q
    target_beta = (X*X, 0, 0, 2*Y*Y, 0)
    target_gaussian = (X**5, 16*Y**5)
    beta = lift_root(eta, target_beta, q, precision, 2)
    gaussian = lift_root(theta, target_gaussian, q, precision, -1)
    N = X**10+256*Y**10
    z = lift_root((1,), (N,), q, precision, 1)[0]
    assert norm(beta, 2) % modulus == z
    assert norm(gaussian, -1) % modulus == z
    assert pow(z, 17, modulus) == N % modulus
    assert tuple(b % q for b in beta) == eta
    assert tuple(b % q for b in gaussian) == theta
    witness = {'q': q, 'precision': precision, 'modulus': str(modulus),
               'X': str(X), 'Y': str(Y), 'Z_modulus': str(z),
               'beta_coefficients': [str(x) for x in beta],
               'gaussian_coefficients': [str(x) for x in gaussian],
               'all_equations_and_norms_verified_modulo_modulus': True,
               'global_integer_solution_claimed': False}
    p = prod(FORCERS)
    assert all(r % 68 not in (1, 67) and r % 85 not in Q_OLD for r in FORCERS)
    numerator, denominator = 257*17**17, 32**17
    assert numerator < denominator
    joint_bound = 17**15*p**30
    assert joint_bound > 10**906
    assert len(str(joint_bound)) == 908
    summary = {'joint_classes_mod340': classes,
               'extra_fifth_residue_test_in_class1': True,
               'gaussian_norm_one_kernel_counts': gaussian_counts,
               'fifth_residue_examples': fifth_examples,
               'forcing_product': str(p),
               'gaussian_bound_numerator': str(numerator),
               'gaussian_bound_denominator': str(denominator),
               'joint_exceptional_product_gt_10_to_453': True,
               'joint_bound_squared_decimal_digits': len(str(joint_bound)),
               'initial_quintic_root': list(eta), 'initial_gaussian_root': list(theta),
               'local_witness': witness}
    print(json.dumps({'checkpoint': 'U69', 'full_Beal_solved': False,
                      'summary': summary, 'factorization_rows': rows}, indent=2))


if __name__ == '__main__':
    main()
