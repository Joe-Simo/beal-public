"""Exact U63 checks of U41's prime-11 comparison and a corrected local model.

Python counts square-root multiplicities in F_11[i].  The TypeScript checker
instead uses Euler's criterion applied to norms.  These are finite certificates,
not a decision procedure for the weighted equation or for Beal's conjecture.
"""
from __future__ import annotations

from collections import Counter
import json
import sympy as sp

Pair = tuple[int, int]
Q = 11


def add(x: Pair, y: Pair) -> Pair:
    return ((x[0] + y[0]) % Q, (x[1] + y[1]) % Q)


def mul(x: Pair, y: Pair) -> Pair:
    return ((x[0] * y[0] - x[1] * y[1]) % Q,
            (x[0] * y[1] + x[1] * y[0]) % Q)


def power(x: Pair, n: int) -> Pair:
    if n < 0:
        raise ValueError("Nonnegative integer exponent required")
    out = (1, 0)
    for _ in range(n):
        out = mul(out, x)
    return out


def f(x: int, u: int, v: int) -> int:
    return x**5 + 40*u*v*x**3 + 320*u*u*v*v*x + 64*(8*v**5-u**5)


def histogram(rows: list[dict[str, int]], sign: int = 1) -> list[list[int]]:
    counts = Counter((sign*r["S"], r["P"], r["D"]) for r in rows)
    return [[*triple, n] for triple, n in sorted(counts.items())]


def main() -> None:
    assert pow(5, 8, 17) == 16  # Inert RM coefficient field at 17.
    assert pow(10, 5, Q) == Q - 1  # -1 is nonsquare, so the pair algebra is a field.
    assert mul((0, 1), (0, 1)) == (10, 0)
    assert power((0, 0), 0) == (1, 0)
    elements = [(a, b) for a in range(Q) for b in range(Q)]
    squares2 = Counter(mul(x, x) for x in elements)
    squares1 = Counter(x*x % Q for x in range(Q))
    assert sum(squares2.values()) == Q*Q and squares2[(0, 0)] == 1
    assert sorted(set(squares2.values())) == [1, 2]
    x3 = {x: power(x, 3) for x in elements}
    x5 = {x: power(x, 5) for x in elements}
    rows: list[dict[str, int]] = []
    z = sp.Symbol("z")
    for u in range(Q):
        for v in range(Q):
            if u == 0 and v == 0:
                continue
            assert (u**5+8*v**5) % Q != 0
            fp = sp.Poly(f(z, u, v), z, modulus=Q)
            assert sp.gcd(fp, fp.diff()).degree() == 0
            c3, c1, c0 = 40*u*v % Q, 320*u*u*v*v % Q, 64*(8*v**5-u**5) % Q
            n1 = 1 + sum(squares1[f(x, u, v) % Q] for x in range(Q))
            n1_twist = 1 + sum(squares1[-f(x, u, v) % Q] for x in range(Q))
            values = [add(add(x5[x], mul((c3, 0), x3[x])),
                          add(mul((c1, 0), x), (c0, 0))) for x in elements]
            n2 = 1 + sum(squares2[value] for value in values)
            n2_twist = 1 + sum(squares2[((-value[0]) % Q, (-value[1]) % Q)]
                               for value in values)
            assert n1 + n1_twist == 2*(Q+1) and n2 == n2_twist
            s = Q+1-n1
            numerator = s*s-(Q*Q+1-n2)
            assert numerator % 2 == 0
            p = numerator//2-2*Q
            rows.append(dict(U=u, V=v, N11=n1, N121=n2,
                             N11_negative_twist=n1_twist, S=s, P=p, D=s*s-4*p))
    sq = {x*x % Q for x in range(Q)}
    twice_sq = {2*x*x % Q for x in range(Q)}
    structured = [r for r in rows if r["U"] in sq and r["V"] in twice_sq]
    assert len(rows) == 120 and len(structured) == 35
    expected_all = [[-9,19,5,5],[-7,11,5,25],[-3,-9,45,25],[-1,-1,5,5],
                    [1,-1,5,5],[3,-9,45,25],[7,11,5,25],[9,19,5,5]]
    assert histogram(rows) == expected_all
    assert histogram(structured) == [[-9,19,5,5],[-1,-1,5,5],[3,-9,45,25]]
    assert histogram(structured, -1) == [[-3,-9,45,25],[1,-1,5,5],[9,19,5,5]]
    witness = next(r for r in rows if (r["U"], r["V"]) == (0, 2))
    assert (witness["N11"], witness["N121"], witness["S"], witness["P"]) == (13, 163, -1, -1)
    assert (0**10+256*1**10-pow(5,17,Q)) % Q == 0

    e = sp.Symbol("e")
    minpoly = e**2+e-1
    # Correct LMFDB norm-11 pair for orbit a: (-e-1,e), not the U41 pair (e,-5).
    assert sp.rem((-e-1)+e+1, minpoly, e) == 0
    assert sp.rem((-e-1)*e+1, minpoly, e) == 0
    # The repaired negative twist changes this conclusion: orbit a's rational sum
    # is -1, unequal mod17 to each negative-twist square-structured trace sum.
    assert all((r[0]+1) % 17 != 0 for r in histogram(structured, -1))

    sq125 = sorted({x*x % 125 for x in range(125)})
    twice125 = sorted({2*x*x % 125 for x in range(125)})
    pairs125 = [(u,v) for u in sq125 for v in twice125 if (u**5+8*v**5) % 5 != 0]
    roots125 = [[u,v,x] for u,v in pairs125 for x in range(125) if f(x,u,v) % 125 == 0]
    assert len(sq125) == len(twice125) == 53
    assert len(pairs125) == 1550 and roots125 == []
    assert sum(v % 5 == 0 for u,v in pairs125) == 150

    quadratic_squares = sorted({((a*a+b*b) % 4,(2*a*b+b*b) % 4)
                                for a in range(4) for b in range(4)})
    assert quadratic_squares == [(0,0),(1,0),(1,1),(2,3)]
    assert (3,0) not in quadratic_squares
    # A concrete non-solution parameter example auditing the integer SQ predicate.
    old_constant = 64*(256-1)
    valuation = 0
    unit = old_constant
    while unit % 2 == 0:
        unit //= 2
        valuation += 1
    assert valuation == 6 and old_constant % 4 == 0 and unit % 8 == 7

    X,Y,t,w,k,pi = sp.symbols("X Y t w k pi")
    def f_special(zz: sp.Expr) -> sp.Expr:
        return zz**5+80*X**2*Y**2*zz**3+1280*X**4*Y**4*zz+64*(256*Y**10-X**10)
    lhs = sp.expand(((16*w+8*k)**2+f_special(pi**8*t))/256)
    target = w*w+k*w+t**5+5*X**2*Y**2*pi**4*t**3+5*X**4*Y**4*pi**8*t
    remainder = sp.rem(sp.rem(lhs-target,k*k-X**10+256*Y**10,k),pi**5-2,pi)
    assert sp.expand(remainder) == 0
    # Smoothness at infinity in the integral quadratic-cover chart.
    u,v,a,b = sp.symbols("u v a b")
    infinity_equation = v*v+k*v*u**3+u+a*u**3+b*u**5
    assert sp.diff(infinity_equation,u).subs({u:0,v:0}) == 1
    inertia_poly = sum(z**j for j in range(5))
    assert sp.expand((z-1)*inertia_poly-(z**5-1)) == 0
    U,V = sp.symbols("U V")
    discriminant = sp.factor(sp.discriminant(f(z,U,V),z))
    assert discriminant == 2**24*5**5*(U**5+8*V**5)**4

    output = {
        "checkpoint": "U63", "arithmetic": "Python exact integers and SymPy",
        "status": "completed", "full_Beal_solved": False,
        "prime11": {"all_pairs": len(rows), "structured_pairs": len(structured),
                    "all_trace_distribution": histogram(rows),
                    "structured_plus_f": histogram(structured),
                    "structured_minus_f": histogram(structured,-1),
                    "rows": rows, "U41_nonmatching_counterexample": witness,
                    "local_weighted_base_residues_X_Y_Z": [0,1,5],
                    "correct_form_a_sum_product": [-1,-1],
                    "form_a_excluded_after_repair_in_square_domain": True},
        "mod125": {"square_residues":len(sq125),"pairs":len(pairs125),
                   "tested_x_per_pair":125,"root_triples": roots125,
                   "subdomain_5_divides_V_pairs":150},
        "mod4_quadratic_squares": quadratic_squares,
        "source_SQ_counterexample": {"X":1,"Y":1,"constant":old_constant,
                                     "valuation2":valuation,"normalized_unit":unit},
        "negative_twist_model_identity": True, "infinity_smoothness_identity": True,
        "inertia_cyclotomic_identity": True, "discriminant_identity": True,
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
