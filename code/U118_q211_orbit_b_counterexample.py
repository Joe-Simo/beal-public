"""U118 exact counterexample to a proposed uniform orbit-b forcing lemma.

This does NOT produce a Beal counterexample. It proves only that the local
Frobenius sieve against Hilbert newform orbit b does not uniformly force V=0
at every rational prime q == 1 (mod 5).

At q=211 the admissible nonzero projective parameter U=1, V=23 comes from
X=1, Y=31 because V = 2*Y^2 mod q. Moreover

    U^5 + 8 V^5 = 4^17 mod 211,

and the genus-2 Frey curve has exactly the same Frobenius invariants (S,P)
as the boundary curve V=0.

All arithmetic is exact integer arithmetic.
"""
from __future__ import annotations

from math import gcd

Q = 211
D = 2  # a nonsquare modulo 211
MOD = 17
Pair = tuple[int, int]


def legendre(a: int) -> int:
    a %= Q
    if a == 0:
        return 0
    value = pow(a, (Q - 1) // 2, Q)
    if value == 1:
        return 1
    if value == Q - 1:
        return -1
    raise AssertionError("Euler criterion returned an impossible value")


def mul(a: Pair, b: Pair) -> Pair:
    """Multiply in F_q[s]/(s^2-D)."""
    return (
        (a[0] * b[0] + D * a[1] * b[1]) % Q,
        (a[0] * b[1] + a[1] * b[0]) % Q,
    )


def power(a: Pair, n: int) -> Pair:
    out: Pair = (1, 0)
    base = a
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n //= 2
    return out


def fp2_quadratic_character(a: Pair) -> int:
    """Quadratic character in F_{q^2}; chi(a)=chi_q(Norm(a))."""
    norm = (a[0] * a[0] - D * a[1] * a[1]) % Q
    return legendre(norm)


def frey_rhs_fp(x: int, u: int, v: int) -> int:
    f = (
        x**5
        + 40 * u * v * x**3
        + 320 * u * u * v * v * x
        + 64 * (8 * v**5 - u**5)
    )
    return (-f) % Q


def frey_rhs_fp2(x: Pair, u: int, v: int) -> Pair:
    x3 = power(x, 3)
    x5 = power(x, 5)
    c3 = 40 * u * v
    c1 = 320 * u * u * v * v
    c0 = 64 * (8 * v**5 - u**5)
    return (
        (-x5[0] - c3 * x3[0] - c1 * x[0] - c0) % Q,
        (-x5[1] - c3 * x3[1] - c1 * x[1]) % Q,
    )


def frobenius_invariants(u: int, v: int) -> tuple[int, int, int, int]:
    """Return (#C(F_q), #C(F_q^2), S=a1+a2, P=a1*a2)."""
    n1 = 1
    for x in range(Q):
        n1 += 1 + legendre(frey_rhs_fp(x, u, v))

    n2 = 1
    for a in range(Q):
        for b in range(Q):
            n2 += 1 + fp2_quadratic_character(frey_rhs_fp2((a, b), u, v))

    s = Q + 1 - n1
    numerator = s * s - (Q * Q + 1 - n2)
    assert numerator % 2 == 0
    p = numerator // 2 - 2 * Q
    return n1, n2, s, p


def main() -> None:
    assert gcd(17, Q - 1) == 1
    assert legendre(D) == -1

    # Boundary orbit-b parameter.
    boundary = frobenius_invariants(1, 0)
    assert boundary == (193, 44983, 19, -11)

    # Nonzero square-structured parameter:
    # U=X^2=1, V=2Y^2=23 with X=1, Y=31.
    x_residue = 1
    y_residue = 31
    z_residue = 4
    u = x_residue * x_residue % Q
    v = 2 * y_residue * y_residue % Q
    assert (u, v) == (1, 23)
    assert v != 0

    # The generalized-Fermat relation is locally admissible.
    assert (pow(u, 5, Q) + 8 * pow(v, 5, Q)) % Q == pow(z_residue, 17, Q)
    assert pow(v, 5, Q) == Q - 1

    candidate = frobenius_invariants(u, v)
    assert candidate == boundary
    assert candidate[2] % MOD == boundary[2] % MOD
    assert candidate[3] % MOD == boundary[3] % MOD

    # All five fifth roots of -1 that also have the required twice-square
    # structure produce the same exact Frobenius invariants.
    matches: list[int] = []
    for t in range(1, Q):
        if pow(t, 5, Q) != Q - 1:
            continue
        if legendre(t * pow(2, -1, Q)) != 1:
            continue
        if frobenius_invariants(1, t) == boundary:
            matches.append(t)

    assert matches == [23, 104, 140, 156, 210]

    print(
        {
            "q": Q,
            "boundary": boundary,
            "nonzero_parameter": {"X": 1, "Y": 31, "Z": 4, "U": 1, "V": 23},
            "matching_nonzero_V_over_U": matches,
            "mod17_invariants": (boundary[2] % 17, boundary[3] % 17),
            "claim_refuted": "orbit-b congruence uniformly forces V=0 at every q == 1 mod 5",
            "beal_counterexample": False,
        }
    )


if __name__ == "__main__":
    main()
