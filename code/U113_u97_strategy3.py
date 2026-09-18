"""Adversarial audit of U97 Strategy 3.

CLAIM: S = { split primes q = 1 mod 5 : for ALL t in F_q^x,
             (S,P)(C^-(1,t)) != (S,P)(b) mod 17 }  has POSITIVE DENSITY (infinite).

TEST: for each q = 1 mod 5, count the t in F_q^x whose Euler factor at q agrees
with orbit b's mod 17. q is 'forcing' iff that count is 0.

C^-(U,V): y^2 = -f(x),  f = x^5 + 40UVx^3 + 320U^2V^2x + 64(8V^5 - U^5).
Exact arithmetic throughout.
"""
import sys
from sympy import primerange


def euler_SP(q, coeffs):
    """(S,P) for y^2 = g(x) over F_q, g given by coeffs (deg 5, leading first)."""
    def g(x, mul, one, zero, powr):
        pass
    # --- F_q ---
    sq1 = {}
    for y in range(q):
        sq1[(y * y) % q] = sq1.get((y * y) % q, 0) + 1

    def gv(x):
        r = 0
        for c in coeffs:
            r = (r * x + c) % q
        return r

    n1 = sum(sq1.get(gv(x), 0) for x in range(q)) + 1
    t = q + 1 - n1

    # --- F_{q^2} as F_q[i]/(i^2 - n), n a non-residue ---
    n = next(r for r in range(2, q) if pow(r, (q - 1) // 2, q) == q - 1)

    def mul(a, b):
        return ((a[0] * b[0] + n * a[1] * b[1]) % q, (a[0] * b[1] + a[1] * b[0]) % q)

    sq2 = {}
    for a in range(q):
        for b in range(q):
            y = (a, b)
            s = mul(y, y)
            sq2[s] = sq2.get(s, 0) + 1

    def gv2(x):
        r = (0, 0)
        for c in coeffs:
            r = mul(r, x)
            r = ((r[0] + c) % q, r[1])
        return r

    n2 = 1
    for a in range(q):
        for b in range(q):
            n2 += sq2.get(gv2((a, b)), 0)

    s = (t * t - (q * q + 1 - n2)) // 2
    return t, s - 2 * q


def curve_coeffs(q, t):
    """y^2 = -f(x) with U=1, V=t  ->  coeffs of -f, leading first."""
    return [(-1) % q, 0, (-40 * t) % q, 0, (-320 * t * t) % q, (-64 * (8 * pow(t, 5, q) - 1)) % q]


print(f"{'q':>5} {'#t in F_q^x matching b mod 17':>32} {'forcing?':>10}")
forcing, nonforcing = [], []
for q in primerange(11, 140):
    if q % 5 != 1:
        continue
    S0, P0 = euler_SP(q, curve_coeffs(q, 0))          # t=0 is exactly C_0 ~ orbit b
    matches = []
    for tt in range(1, q):
        S, P = euler_SP(q, curve_coeffs(q, tt))
        if (S - S0) % 17 == 0 and (P - P0) % 17 == 0:
            matches.append(tt)
    isforcing = len(matches) == 0
    (forcing if isforcing else nonforcing).append(q)
    print(f"{q:>5} {len(matches):>32} {'YES' if isforcing else 'no':>10}"
          + ("" if not matches else f"   e.g. t={matches[:6]}"))

print()
print("forcing primes found in [11,140):", forcing)
print("NON-forcing primes found       :", nonforcing)
