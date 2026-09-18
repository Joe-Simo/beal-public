"""Exponent Reduction Lemma for Beal, with exact verification.

LEMMA. Suppose (A,B,C,x,y,z) satisfies A^x + B^y = C^z with A,B,C >= 1, x,y,z >= 3 and
gcd(gcd(A,B),C) = 1.  Then there exist A',B',C' >= 1 and x',y',z' with
    A'^x' + B'^y' = C'^z',   gcd(gcd(A',B'),C') = 1,
and each of x',y',z' lies in {4} union {odd primes}.

PROOF. Treat x. Every integer x >= 3 either (a) has an odd prime factor p, or (b) is a power
of 2, in which case x >= 3 and x a power of 2 force x >= 4, so 4 | x.
  (a) write x = p*m with m >= 1 and set A' = A^m, x' = p.  Then A'^{x'} = A^{pm} = A^x.
  (b) write x = 4*m with m >= 1 and set A' = A^m, x' = 4.  Then A'^{x'} = A^{4m} = A^x.
Same for y,z. The equation is preserved by construction.

GCD PRESERVATION (the step that must not be waved through). Let q be a prime with
q | gcd(gcd(A',B'),C'). Since A' = A^m with m >= 1, q | A^m implies q | A (q prime).
Likewise q | B and q | C. Hence q | gcd(gcd(A,B),C) = 1, impossible. So the reduced triple
is again primitive.  QED

Note the direction: a counterexample maps to a counterexample. That is what is needed to
restrict attention to signatures with exponents in {4} u {odd primes}. The converse is not
claimed and is not needed.
"""
from math import gcd
from sympy import primefactors, isprime


def reduce_exponent(e: int) -> tuple[int, int]:
    """Return (e', m) with e = e'*m, e' in {4} u {odd primes}, for any e >= 3."""
    if e < 3:
        raise ValueError("exponent must be >= 3")
    odd = [p for p in primefactors(e) if p % 2 == 1]
    if odd:
        p = odd[0]
        return p, e // p
    # e is a power of 2 and e >= 3, hence e >= 4 and 4 | e
    assert e % 4 == 0, f"power of two >= 3 must be divisible by 4, got {e}"
    return 4, e // 4


ok = True
print("1. reduce_exponent is total on e >= 3 and lands in {4} u {odd primes}")
for e in range(3, 400):
    ep, m = reduce_exponent(e)
    good = (ep * m == e) and m >= 1 and (ep == 4 or (isprime(ep) and ep % 2 == 1))
    ok &= good
    if not good:
        print(f"   FAIL e={e} -> {ep}*{m}")
print(f"   all e in [3,400): {'OK' if ok else 'FAILED'}")

print("\n2. powers of two >= 3 are divisible by 4 (the only delicate case)")
for k in range(2, 20):
    e = 2 ** k
    assert e % 4 == 0
print("   2^k for k>=2 all divisible by 4: OK   (2^1 = 2 < 3 is excluded by x >= 3)")

print("\n3. equation and primitivity preserved -- exhaustive test on the identity")
print("   A^x + B^y = C^z reduced to A'^x' + B'^y' = C'^z'")
tests = 0
for A in range(1, 12):
    for B in range(1, 12):
        for C in range(1, 12):
            for (x, y, z) in [(3, 3, 3), (4, 6, 9), (8, 12, 16), (6, 10, 15), (9, 27, 4)]:
                lhs, rhs = A ** x + B ** y, C ** z
                xp, mx = reduce_exponent(x)
                yp, my = reduce_exponent(y)
                zp, mz = reduce_exponent(z)
                Ap, Bp, Cp = A ** mx, B ** my, C ** mz
                assert Ap ** xp + Bp ** yp == lhs, "equation not preserved"
                assert Cp ** zp == rhs, "equation not preserved"
                if gcd(gcd(A, B), C) == 1:
                    assert gcd(gcd(Ap, Bp), Cp) == 1, \
                        f"PRIMITIVITY LOST: ({A},{B},{C}) -> ({Ap},{Bp},{Cp})"
                tests += 1
print(f"   {tests} cases: equation preserved and primitivity preserved in every case")

print("\n4. COUNTERSEARCH: can primitivity be CREATED (imprimitive -> primitive)?")
print("   If so the reduction would be unsound in the reverse direction (not needed, but check).")
created = 0
for A in range(1, 30):
    for B in range(1, 30):
        for C in range(1, 30):
            if gcd(gcd(A, B), C) > 1:
                Ap, Bp, Cp = A ** 2, B ** 3, C ** 2
                if gcd(gcd(Ap, Bp), Cp) == 1:
                    created += 1
print(f"   imprimitive triples becoming primitive under q -> q^m: {created}")
print("   (0 expected: prime divisors are preserved by taking powers)")

print("\n5. Resulting signature set")
print("   After reduction every exponent lies in {4} u {3,5,7,11,13,...}.")
print("   1/x + 1/y + 1/z <= 1 always, with equality ONLY at (3,3,3) [Fermat cubic].")
print("   Every other reduced Beal signature is hyperbolic: 1/x + 1/y + 1/z < 1.")
for sig in [(3, 3, 3), (3, 3, 4), (3, 4, 4), (4, 4, 4), (3, 3, 5)]:
    s = sum(1 / e for e in sig)  # display only; the exact comparison below uses integers
    num = sig[1] * sig[2] + sig[0] * sig[2] + sig[0] * sig[1]
    den = sig[0] * sig[1] * sig[2]
    rel = "=" if num == den else ("<" if num < den else ">")
    print(f"   {sig}: {num}/{den} {rel} 1   (exact integer comparison)")
