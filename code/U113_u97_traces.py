"""Adversarial audit of U97 section 1.4: Frobenius traces of C_0: y^2 = 64 - x^5.

Exact point counting over F_q and F_{q^2}. For the abelian surface A_0 = Jac(C_0)/Q
with char poly  T^4 - t T^3 + s T^2 - q t T + q^2, and a split prime q of K = Q(sqrt5)
with primes q1,q2 above it, the Euler factor prod_i (1 - a_{qi}T + qT^2) gives
    S := a_q1 + a_q2 = t      and      P := a_q1 * a_q2 = s - 2q.
"""
def count_affine(q, k=1):
    """#{(x,y) in F_{q^k}^2 : y^2 = 64 - x^5}, computed in F_{q^k} via F_q[t]/(irred)."""
    if k == 1:
        sq = {}
        for y in range(q):
            sq.setdefault((y * y) % q, 0)
            sq[(y * y) % q] += 1
        return sum(sq.get((64 - pow(x, 5, q)) % q, 0) for x in range(q))
    raise NotImplementedError


def count_Fq(q):
    """#C_0(F_q) including the single point at infinity (y^2 = deg-5 poly, genus 2)."""
    return count_affine(q) + 1


def count_Fq2(q):
    """Point count over F_{q^2} using an explicit quadratic extension F_q[i]/(i^2 - n)."""
    n = next(r for r in range(2, q) if pow(r, (q - 1) // 2, q) == q - 1)  # a non-residue

    def mul(a, b):
        return ((a[0] * b[0] + n * a[1] * b[1]) % q, (a[0] * b[1] + a[1] * b[0]) % q)

    def power(a, e):
        r = (1, 0)
        while e:
            if e & 1:
                r = mul(r, a)
            a = mul(a, a)
            e >>= 1
        return r

    elems = [(a, b) for a in range(q) for b in range(q)]
    squares = {}
    for y in elems:
        squares[mul(y, y)] = squares.get(mul(y, y), 0) + 1
    total = 0
    for x in elems:
        rhs = ((64 - power(x, 5)[0]) % q, (-power(x, 5)[1]) % q)
        total += squares.get(rhs, 0)
    return total + 1


CLAIMS = {11: (9, 19), 31: (-11, 29), 41: (-1, -151)}
print("q  = 1 mod 5 (split in Q(sqrt5)) -- U97 section 1.4 claims S and P:")
ok = True
for q, (Sc, Pc) in CLAIMS.items():
    n1, n2 = count_Fq(q), count_Fq2(q)
    t = q + 1 - n1
    s = (t * t - (q * q + 1 - n2)) // 2
    S, P = t, s - 2 * q
    good = (S == Sc and P == Pc)
    ok &= good
    print(f"  q={q:<3} #C(F_q)={n1:<5} #C(F_q^2)={n2:<6} -> S={S:<5} P={P:<6} "
          f"claimed S={Sc:<5} P={Pc:<6} {'MATCH' if good else '*** MISMATCH ***'}")

print("\nq not = 1 mod 5: U97 claims the Frobenius trace vanishes (x->x^5 bijective):")
for q in [2, 3, 7, 13, 17, 19, 23, 29, 37, 43, 47, 53]:
    if q % 5 == 1:
        continue
    t = q + 1 - count_Fq(q)
    flag = "" if t == 0 else "  *** NONZERO TRACE ***"
    ok &= (t == 0)
    print(f"  q={q:<3} q mod 5={q%5}  trace t={t}{flag}")

print("\nAUDIT RESULT:", "all U97 section 1.4 trace claims reproduced exactly" if ok else "DISCREPANCY FOUND")
