"""Exact good-prime point counts for 17*y^2=Psi_17(x); no rank claim."""
from __future__ import annotations

import json
from math import gcd
from time import perf_counter

COEFFS = (1, -4, -10, 10, 15, -6, -7, 1, 1)


class FiniteField:
    """Small polynomial-basis fields; all operations use Python integers."""

    def __init__(self, p: int, degree: int) -> None:
        self.p = p
        self.degree = degree
        self.order = p**degree
        if degree == 1:
            self.modulus = [0, 1]
        elif degree == 2:
            d = next(a for a in range(2, p) if pow(a, (p-1)//2, p) == p-1)
            self.modulus = [-d, 0, 1]
        elif degree == 3:
            self.modulus = next(
                [b, a, 0, 1]
                for a in range(p) for b in range(1, p)
                if all((x*x*x+a*x+b) % p for x in range(p))
            )
        else:
            raise ValueError('Only degrees one through three are used.')
        self.digits = [tuple((a//(p**i)) % p for i in range(degree))
                       for a in range(self.order)]

    def add_scalar(self, a: int, b: int) -> int:
        return a-a % self.p+(a % self.p+b) % self.p

    def multiply(self, a: int, b: int) -> int:
        p, n = self.p, self.degree
        if n == 1:
            return a*b % p
        aa, bb = self.digits[a], self.digits[b]
        cc = [0]*(2*n-1)
        for i in range(n):
            for j in range(n):
                cc[i+j] += aa[i]*bb[j]
        for k in range(2*n-2, n-1, -1):
            for j in range(n):
                cc[k-n+j] -= cc[k]*self.modulus[j]
        return sum((cc[i] % p)*p**i for i in range(n))

    def power(self, a: int, n: int) -> int:
        out = 1
        while n:
            if n & 1:
                out = self.multiply(out, a)
            a = self.multiply(a, a)
            n >>= 1
        return out

    def count_curve(self) -> int:
        # Enumerating the square set is simpler than using a quadratic-character
        # convention in an extension. A nonzero square has exactly two roots.
        squares = {self.multiply(a, a) for a in range(self.order)}
        assert len(squares) == (self.order+1)//2
        assert all(self.power(a, self.order) == a for a in range(self.order))
        count = 2 if 17 % self.p in squares else 0  # degree-eight infinities
        for a in range(self.order):
            v = 0
            for c in reversed(COEFFS):
                v = self.add_scalar(self.multiply(v, a), c)
            v = self.multiply(17 % self.p, v)  # y^2 = 17*Psi, isomorphic model
            count += 1 if v == 0 else 2 if v in squares else 0
        return count


def jacobian_order(p: int) -> dict[str, object]:
    fields = [FiniteField(p, d) for d in (1, 2, 3)]
    counts = [field.count_curve() for field in fields]
    s1, s2, s3 = [p**n+1-counts[n-1] for n in (1, 2, 3)]
    assert (s1*s1-s2) % 2 == 0
    assert (s1**3-3*s1*s2+2*s3) % 6 == 0
    e1, e2, e3 = s1, (s1*s1-s2)//2, (s1**3-3*s1*s2+2*s3)//6
    lpoly = [1, -e1, e2, -e3, p*e2, -p*p*e1, p**3]
    return {'p': p, 'moduli': [f.modulus for f in fields],
            'curve_counts_Fp_Fp2_Fp3': counts,
            'L_polynomial_ascending': lpoly, 'jacobian_order': sum(lpoly)}


def main() -> None:
    start = perf_counter()
    rows = [jacobian_order(p) for p in (3, 5, 7, 11, 13)]
    common = 0
    for row in rows:
        common = gcd(common, int(row['jacobian_order']))
    output = {'status': 'completed', 'curve': 'y^2=17*Psi17(x)',
              'counts': rows, 'gcd_orders': common,
              'elapsed_seconds': perf_counter()-start,
              'warning': 'No Jacobian rank or rational-point completeness is inferred from these counts.'}
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
