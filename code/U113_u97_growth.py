from sympy import primerange
def trace(q, t, sqtab):
    n = 1
    c5 = (-64 * (8 * pow(t, 5, q) - 1)) % q
    c2 = (-40 * t) % q; c4 = (-320 * t * t) % q; c0 = (-1) % q
    for x in range(q):
        r = (((((c0 * x) % q) * x + c2) % q * x % q) * x + c4) % q
        r = (r * x + c5) % q
        n += sqtab.get(r, 0)
    return q + 1 - n
print(f"{'q':>6}{'#t match':>10}{'q/17':>8}  forcing")
zero = []
for q in primerange(11, 1600):
    if q % 5 != 1: continue
    sqtab = {}
    for y in range(q): sqtab[(y*y) % q] = sqtab.get((y*y) % q, 0) + 1
    S0 = trace(q, 0, sqtab)
    m = sum(1 for t in range(1, q) if (trace(q, t, sqtab) - S0) % 17 == 0)
    if m == 0: zero.append(q)
    if q > 600 or m == 0:
        print(f"{q:>6}{m:>10}{q/17:>8.1f}  {'YES' if m==0 else ''}")
print("\nALL forcing primes q<1600:", zero)
