"""U80 exact finite certificate: every U79 dyadic Kummer basis generator
is a norm from adjoining i, modulo the s^35 squareclass cutoff.

This supports a written local norm argument. It does not compute the class group,
the full Selmer group, the weighted equation, or Beal's conjecture.
"""
from __future__ import annotations

import json
from typing import TypeAlias

Vector: TypeAlias = tuple[int, ...]
Pair: TypeAlias = tuple[int, int]


class Ring:
    """(Z/8)[phi,s]/(phi^2-phi-1, s^17-2phi+2)."""

    modulus = 8
    zero: Vector = (0,) * 34
    one: Vector = (1,) + (0,) * 33

    @staticmethod
    def pair_mul(a: Pair, b: Pair, modulus: int = 8) -> Pair:
        return (
            (a[0] * b[0] + a[1] * b[1]) % modulus,
            (a[0] * b[1] + a[1] * b[0] + a[1] * b[1]) % modulus,
        )

    def add(self, a: Vector, b: Vector) -> Vector:
        return tuple((x + y) % self.modulus for x, y in zip(a, b, strict=True))

    def scale(self, a: Vector, c: int) -> Vector:
        return tuple(c * x % self.modulus for x in a)

    def mul(self, a: Vector, b: Vector) -> Vector:
        raw = [0] * 66
        for i, x in enumerate(a):
            if not x:
                continue
            si, pi = divmod(i, 2)
            for j, y in enumerate(b):
                if not y:
                    continue
                sj, pj = divmod(j, 2)
                k = 2 * (si + sj)
                if pi + pj == 2:
                    raw[k] += x * y
                    raw[k + 1] += x * y
                else:
                    raw[k + pi + pj] += x * y
        for k in range(32, 16, -1):
            x, y = raw[2 * k : 2 * k + 2]
            raw[2 * (k - 17)] += -2 * x + 2 * y
            raw[2 * (k - 17) + 1] += 2 * x
        return tuple(x % self.modulus for x in raw[:34])

    def monomial(self, exponent: int, pair: Pair = (1, 0)) -> Vector:
        q, r = divmod(exponent, 17)
        value = pair
        for _ in range(q):
            value = self.pair_mul(value, (-2, 2), self.modulus)
        out = [0] * 34
        out[2 * r : 2 * r + 2] = value
        return tuple(out)

    def valuation(self, a: Vector) -> int:
        answer = 51
        for j in range(17):
            for x in a[2 * j : 2 * j + 2]:
                if x:
                    answer = min(answer, j + 17 * ((x & -x).bit_length() - 1))
        return answer

    def inverse_principal_unit(self, a: Vector) -> Vector:
        z = self.add(a, self.scale(self.one, -1))
        depth = self.valuation(z)
        if depth < 1:
            raise ValueError("expected a principal unit")
        out = self.one
        term = self.one
        for _ in range(1, (50 // depth) + 1):
            term = self.mul(term, self.scale(z, -1))
            out = self.add(out, term)
        assert self.mul(a, out) == self.one
        return out

    def leading(self, a: Vector, depth: int) -> Pair:
        q, r = divmod(depth, 17)
        x, y = a[2 * r : 2 * r + 2]
        assert x % (1 << q) == 0 and y % (1 << q) == 0
        coefficient = ((x >> q) % 2, (y >> q) % 2)
        for _ in range(q):
            coefficient = self.pair_mul(coefficient, (0, 1), 2)
        return coefficient


def norm_factor(ring: Ring, b: Vector) -> Vector:
    """Norm_{E(i)/E}(1+b(i-1)) = 1 - 2b + 2b^2."""
    return ring.add(
        ring.one,
        ring.add(ring.scale(b, -2), ring.scale(ring.mul(b, b), 2)),
    )


def solve(ring: Ring, n: int, coefficient: Pair) -> tuple[list[list[object]], int]:
    target = ring.add(ring.one, ring.monomial(n, coefficient))
    current = ring.one
    factors: list[list[object]] = []
    while True:
        ratio = ring.mul(target, ring.inverse_principal_unit(current))
        residual = ring.add(ratio, ring.scale(ring.one, -1))
        depth = ring.valuation(residual)
        if depth >= 35:
            final_depth = ring.valuation(ring.add(target, ring.scale(current, -1)))
            return factors, final_depth
        assert depth >= 18
        lead = ring.leading(residual, depth)
        # 2 = phi*s^17 and phi^{-1}=1+phi in F4.
        b_residue = ring.pair_mul((1, 1), lead, 2)
        b = ring.monomial(depth - 17, b_residue)
        factor = norm_factor(ring, b)
        assert ring.leading(ring.add(factor, ring.scale(ring.one, -1)), depth) == lead
        current = ring.mul(current, factor)
        factors.append([depth - 17, list(b_residue)])


def main() -> None:
    ring = Ring()
    rows = []
    for n in range(19, 34, 2):
        for label, coefficient in (("1", (1, 0)), ("phi", (0, 1))):
            factors, residual_depth = solve(ring, n, coefficient)
            assert residual_depth >= 35
            rows.append(
                {
                    "generator": f"1+{'' if label == '1' else 'phi*'}s^{n}",
                    "norm_factors_b": factors,
                    "residual_depth_at_least": residual_depth,
                }
            )
    assert len(rows) == 16
    print(
        json.dumps(
            {
                "checkpoint": "U80",
                "claim": "all 16 U79 dyadic Kummer basis generators are local quadratic norms",
                "identity": "Norm(1+b(i-1))=1-2b+2b^2",
                "precision": "modulo 8; equality modulo s^35 is enough for U79 squareclasses",
                "rows": rows,
                "class_group_2_rank_computed": False,
                "weighted_equation_solved": False,
                "full_Beal_solved": False,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
