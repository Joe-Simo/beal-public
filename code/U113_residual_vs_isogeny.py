"""Exact demonstration that a residual mod-l congruence does NOT imply isogeny.

Tate normal form for a rational point of order 5:  E_c : y^2 + (1-c)xy - c y = x^3 - c x^2.
Every such curve has a rational 5-torsion point, so rho-bar_{E,5} is REDUCIBLE with
semisimplification 1 (+) chi_5, giving  a_p = 1 + p  (mod 5)  at every good p.
Different c give curves with different a_p over Z, hence NON-isogenous (Faltings/Tate).
So: congruent residual mod-5 representations, non-isogenous curves.
"""
from sympy import primerange


def count_points(a1, a2, a3, a4, a6, p):
    """#E(F_p) affine + 1, or None at bad reduction (detected via singularity)."""
    n = 1
    sing = False
    for x in range(p):
        for y in range(p):
            f = (y * y + a1 * x * y + a3 * y - x ** 3 - a2 * x * x - a4 * x - a6) % p
            if f == 0:
                fx = (-(3 * x * x + 2 * a2 * x + a4) + a1 * y) % p
                fy = (2 * y + a1 * x + a3) % p
                if fx == 0 and fy == 0:
                    sing = True
                n += 1
    return None if sing else n


def ap(c, p):
    n = count_points(1 - c, -c, -c, 0, 0, p)
    return None if n is None else p + 1 - n


PRIMES = [p for p in primerange(2, 40)]
CS = [1, 2, 3, -1, -2]
print("E_c : y^2 + (1-c)xy - c y = x^3 - c x^2   (rational 5-torsion by construction)\n")
print(f"{'p':>4} " + " ".join(f"c={c:<5}" for c in CS) + "   p+1 mod 5")
table = {}
for p in PRIMES:
    row = []
    for c in CS:
        row.append(ap(c, p))
    table[p] = row
    cong = all(v is None or (v - (p + 1)) % 5 == 0 for v in row)
    print(f"{p:>4} " + " ".join(f"{('bad' if v is None else v):<7}" for v in row)
          + f"   {(p+1)%5}   {'OK' if cong else '*** FAILS ***'}")

print("\nAll a_p = p+1 (mod 5) -> all five curves share the same semisimplified residual mod-5 representation.")
pairs = []
for i in range(len(CS)):
    for j in range(i + 1, len(CS)):
        d = [(p, table[p][i], table[p][j]) for p in PRIMES
             if table[p][i] is not None and table[p][j] is not None and table[p][i] != table[p][j]]
        if d:
            pairs.append((CS[i], CS[j], d[0]))
print("\nNon-isogeny witnesses (a_p differ over Z, so no isogeny by Faltings/Tate):")
for c1, c2, (p, v1, v2) in pairs[:6]:
    print(f"  c={c1} vs c={c2}: a_{p} = {v1} vs {v2}   (differ over Z, agree mod 5)")

print("\nCONCLUSION (exact, no floating point):")
print("  Non-isogenous curves CAN and DO share a residual mod-l representation.")
print("  Therefore U102 arguments 1-3, which refute isogeny / 17-adic isomorphism,")
print("  do NOT refute the residual congruence rho-bar_{J^-,17} = rho-bar_{b,17}.")
