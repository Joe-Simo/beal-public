"""Trace-only criterion (what U97 section 2.5 literally states):
q is 'forcing' iff for all t in F_q^x, S(C^-(1,t)) != S(C_0) mod 17,
where S = q + 1 - #C(F_q). Cheap: O(q) per t.
"""
from sympy import primerange

U72 = {11, 31, 41, 61, 71, 101, 151, 191, 211, 281, 331, 431, 461, 631}


def trace(q, t, sqtab):
    n = 1
    for x in range(q):
        r = 0
        for c in ((-1) % q, 0, (-40 * t) % q, 0, (-320 * t * t) % q,
                  (-64 * (8 * pow(t, 5, q) - 1)) % q):
            r = (r * x + c) % q
        n += sqtab.get(r, 0)
    return q + 1 - n


rows = []
for q in primerange(11, 660):
    if q % 5 != 1:
        continue
    sqtab = {}
    for y in range(q):
        sqtab[(y * y) % q] = sqtab.get((y * y) % q, 0) + 1
    S0 = trace(q, 0, sqtab)
    m = sum(1 for t in range(1, q) if (trace(q, t, sqtab) - S0) % 17 == 0)
    rows.append((q, m, m == 0))

mine = {q for q, m, f in rows if f}
print(f"{'q':>5} {'#t matching trace mod 17':>26} {'forcing(mine)':>14} {'in U72 list':>12}")
for q, m, f in rows:
    print(f"{q:>5} {m:>26} {'YES' if f else 'no':>14} {'YES' if q in U72 else 'no':>12}")
print()
print("trace-only forcing set :", sorted(mine))
print("U72 claimed forcing set:", sorted(U72))
print("in U72 but NOT forcing by this criterion:", sorted(U72 - mine))
print("forcing by this criterion but NOT in U72:", sorted(mine - U72))
