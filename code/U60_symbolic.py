"""Exact SymPy audit and constructive local witnesses for U60; not a Beal solver."""
from __future__ import annotations

import json
import platform
from itertools import product
from math import comb
from pathlib import Path

import sympy as sp

Pair = tuple[int, int]


def mul(x: Pair, y: Pair, modulus: int, basis: Pair = (1, 1)) -> Pair:
    a, b = x
    c, d = y
    return ((a*c + basis[0]*b*d) % modulus,
            (a*d + b*c + basis[1]*b*d) % modulus)


def power(x: Pair, n: int, modulus: int, basis: Pair = (1, 1)) -> Pair:
    out = (1, 0)
    while n:
        if n & 1:
            out = mul(out, x, modulus, basis)
        x = mul(x, x, modulus, basis)
        n //= 2
    return out


def h(m: int, n: int, modulus: int) -> Pair:
    return ((m**4+30*m*m*n*n+n**4) % modulus, -16*m*m*n*n % modulus)


def p16(a: int, b: int) -> int:
    # Generate Fibonacci/binomial coefficients rather than transcribing U53.
    f = [0, 1]
    for _ in range(16):
        f.append(f[-1]+f[-2])
    return sum(comb(17, j)*f[j]*a**(17-j)*b**(j-1) for j in range(1, 18))


def valuation(n: int, prime: int) -> int:
    if n == 0:
        raise ValueError("Zero has no finite valuation")
    v = 0
    while n % prime == 0:
        n //= prime
        v += 1
    return v


def sqrt_unit(target: int, prime: int, precision: int) -> int:
    x = 1
    assert (x*x-target) % prime == 0
    for k in range(1, precision):
        modulus = prime**k
        assert (target-x*x) % modulus == 0
        x += ((target-x*x)//modulus * pow(2*x, -1, prime) % prime)*modulus
    assert (x*x-target) % prime**precision == 0
    return x


def witness(prime: int, precision: int = 6) -> dict:
    # Four guard digits protect all subsequent exact divisions.
    work = precision+4
    modulus = prime**work
    r, s = 1, prime
    m, n = power((r, s), 17, modulus, (-1, 0))
    target = h(m, n, modulus)
    alpha = (1, 0)
    start = 2 if prime == 17 else 1
    for k in range(start, work):
        old_modulus = prime**k
        image = power(alpha, 17, modulus)
        assert all((target[i]-image[i]) % old_modulus == 0 for i in (0, 1))
        inverse = 1 if prime == 17 else pow(17, -1, prime)
        digit = tuple((target[i]-image[i])//old_modulus*inverse % prime for i in (0, 1))
        step = prime**(k-1) if prime == 17 else old_modulus
        alpha = (alpha[0]+step*digit[0], alpha[1]+step*digit[1])
    assert power(alpha, 17, modulus) == target
    pvalue = p16(*alpha)
    root_modulus = prime**(work-1)
    if prime == 17:
        assert pvalue % 17 == 0
        square = pvalue//17 % root_modulus
    else:
        square = pvalue*pow(17, -1, root_modulus) % root_modulus
    c = sqrt_unit(square, prime, work-1)
    if prime == 17:
        assert (4*m*n) % 17 == 0
        b = (4*m*n//17)*pow(c, -1, root_modulus) % root_modulus
    else:
        b = 4*m*n*pow(17*c, -1, root_modulus) % root_modulus
    outmod = prime**precision
    aa, bb = (v % outmod for v in alpha)
    m, n, b, c = (v % outmod for v in (m, n, b, c))
    checks = {
        "gaussian": power((r, s), 17, outmod, (-1, 0)) == (m, n),
        "quadratic": power((aa, bb), 17, outmod) == h(m, n, outmod),
        "B_square": (bb+17*b*b) % outmod == 0,
        "P_square": (p16(aa, bb)-17*c*c) % outmod == 0,
        "product": (17*b*c-4*m*n) % outmod == 0,
        "norm": (m*m+n*n-pow(r*r+s*s, 17, outmod)) % outmod == 0,
    }
    assert all(checks.values())
    return {"p": str(prime), "precision": precision, "modulus": str(outmod),
            **dict(zip(("r", "s", "m", "n", "A", "B", "b", "c"),
                       map(str, (r, s, m, n, aa, bb, b, c)))),
            "valuations": dict(zip(("mn", "B", "b", "c"),
                                   (valuation(v, prime) for v in (m*n, bb, b, c)))),
            "checks": checks}


def symbolic_certificate() -> dict:
    t, y, a, b, trace, x = sp.symbols("t y a b trace x")
    m = sum((-1)**j*comb(17, 2*j)*t**(17-2*j) for j in range(9))
    n = sum((-1)**j*comb(17, 2*j+1)*t**(16-2*j) for j in range(9))
    aa, bb = t**4+14*t*t+1, 16*t*t
    u0, u1 = sp.Poly(1, t), sp.Poly(0, t)
    pa, pb = sp.Poly(aa, t), sp.Poly(bb, t)
    for _ in range(17):
        u0, u1 = pa*u0+pb*u1, pb*u0+(pa+pb)*u1
    difference = sp.Poly(sp.expand(-16*m*m*n*n), t)-u1
    assert all(int(c) % 17 == 0 for c in difference.all_coeffs())
    quotient = sp.Poly.from_list([int(c)//17 for c in difference.all_coeffs()], t, modulus=17)
    obstruction = quotient.rem(sp.Poly(t**17-t, t, modulus=17))
    rr = y**6+4*y**5-y**4+3*y**3-y**2+4*y+1
    uu = y**7+y**6-y**5+y**4+y**3-y**2-4*y-1
    vv = -y**5-5*y**4-2*y**3+y**2-8*y-2
    assert sp.Poly(uu*rr+vv*(y**8-1), y, modulus=17).as_expr() == 1
    assert obstruction == sp.Poly(t**4*rr.subs(y, t*t), t, modulus=17)
    aa_poly, bb_poly = sp.Integer(1), sp.Integer(0)
    for _ in range(17):
        aa_poly, bb_poly = sp.expand(a*aa_poly+b*bb_poly), sp.expand(b*aa_poly+(a+b)*bb_poly)
    pp = sp.cancel(bb_poly/b)
    f8 = sp.Poly(sum(comb(17, 2*j+1)*5**j*x**(8-j) for j in range(9)), x)
    transformed = (2**16*pp).subs(a, (trace-b)/2)
    expected = sum(comb(17, 2*j+1)*5**j*trace**(16-2*j)*b**(2*j) for j in range(9))
    assert sp.expand(transformed-expected) == 0
    assert sp.gcd(f8, f8.diff()).degree() == 0
    return {"omega_obstruction": str(obstruction.as_expr()), "R": str(rr),
            "U": str(uu), "V": str(vv), "bezout": "1 mod 17",
            "quotient_curve_f8": str(f8.as_expr()), "f8_squarefree": True,
            "f8_discriminant_factors": {str(p): int(e) for p, e in sp.factorint(f8.discriminant()).items()}}


def upstream_checks() -> dict:
    q = 67
    pairs = list(product(range(q), repeat=2))
    gp = {power(pair, 17, q, (-1, 0)) for pair in pairs}
    kp = {power(pair, 17, q) for pair in pairs}
    surviving = {}
    for k in range(17):
        unit = power((0, 1), k, q)
        targets = {mul(unit, v, q) for v in kp}
        count = sum(h(*v, q) in targets for v in gp if v != (0, 0))
        if count:
            surviving[str(k)] = count
    assert surviving == {"0": 132, "15": 132}
    q = 409
    scalar = {pow(v, 17, q) for v in range(q)}
    def split_images(u: int, v: int) -> set[Pair]:
        inverse = pow(u-v, -1, q)
        return {((a-u*((a-b)*inverse % q)) % q, (a-b)*inverse % q)
                for a, b in product(scalar, repeat=2)}
    i = next(v for v in range(q) if v*v % q == q-1)
    gp, kp = split_images(i, -i), split_images(130, 280)
    counts = {}
    for k in (0, 15):
        targets = {mul(power((0, 1), k, q), v, q) for v in kp}
        compatible = [v for v in gp if v != (0, 0) and h(*v, q) in targets]
        counts[str(k)] = len(compatible)
        if k == 0:
            assert all(m*n % q == 0 for m, n in compatible)
    assert counts == {"0": 48, "15": 0}
    return {"q67_compatible_full_pairs_by_k": surviving,
            "q409_compatible_full_pairs_by_k": counts,
            "warning": "Finite computations reproduce only the specified unit sieves, not the entire earlier proof chain."}


def main() -> None:
    result = {"status": "completed", "python": platform.python_version(), "sympy": sp.__version__,
              "symbolic": symbolic_certificate(), "upstream_sieves": upstream_checks(),
              "local_witnesses": [witness(p) for p in (17, 67, 103, 409, 883)],
              "full_Beal_solved": False}
    path = Path(__file__).resolve().parents[1]/"research/computations/U60_python_output.json"
    path.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
