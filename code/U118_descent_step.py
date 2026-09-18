"""M6: does classical Fermat descent close on the all-even branch?

C020 (kernel-verified): an all-even counterexample A^(2r) + B^(2s) = C^(2t) gives a PRIMITIVE
Pythagorean triple of perfect powers,  (A^r)^2 + (B^s)^2 = (C^t)^2.

Parametrise: A^r = m^2 - n^2, B^s = 2mn, C^t = m^2 + n^2, gcd(m,n)=1, opposite parity.
The odd leg factors into coprime odd parts, so
        m - n = p^r,   m + n = q^r,   A = pq,   gcd(p,q) = 1, both odd.
Hence 2m = q^r + p^r and 2n = q^r - p^r, and therefore

        C^t - B^s = p^(2r),        C^t + B^s = q^(2r),        2C^t = p^(2r) + q^(2r).

QUESTION: is this descent SIZE-REDUCING within a fixed signature (which is what makes Fermat's
right-triangle theorem work), or does it merely move to a DIFFERENT signature?
"""
import sympy as sp

p,q,m,n,r,s,t = sp.symbols("p q m n r s t", positive=True, integer=True)

print("=== verify the descent identities symbolically, for r = 2,3,5 ===")
for rr in (2,3,5):
    M=(q**rr+p**rr)/2; N=(q**rr-p**rr)/2
    odd_leg = sp.simplify(M**2-N**2)          # should be (pq)^rr
    hyp     = sp.simplify(M**2+N**2)          # should be (p^(2r)+q^(2r))/2
    even_leg= sp.simplify(2*M*N)              # should be (q^(2r)-p^(2r))/2
    print(f"  r={rr}:  m^2-n^2 = {sp.factor(odd_leg)}")
    print(f"         2(m^2+n^2) = {sp.simplify(2*hyp)}")
    print(f"         2(2mn)     = {sp.simplify(2*even_leg)}")

print("""
=== signature bookkeeping ===
original equation : A^(2r) + B^(2s) = C^(2t)      signature (2r, 2s, 2t)
after descent     : p^(2r) + q^(2r) = 2 C^t       signature (2r, 2r, t), coefficient C = 2

The descent does NOT return an instance of the ORIGINAL signature with smaller entries.
It returns a DIFFERENT signature:
  * the two exponents on the left become EQUAL (2r, 2r) - the equation diagonalises;
  * the right exponent HALVES (2t -> t);
  * a coefficient 2 appears.

Contrast Fermat's right-triangle theorem, the case r = s = 2, t = 1 in this notation:
there the descent returns a solution of the SAME equation with a strictly smaller hypotenuse,
so infinite descent on that one integer closes the argument.

CONSEQUENCE.  Classical infinite descent cannot close the all-even branch, because there is no
single quantity that strictly decreases while the equation stays fixed: each step changes the
signature.  Iterating, the right exponent halves each time (2t -> t -> t/2 ...) and terminates
when it becomes odd -- at which point the equation is no longer all-even and the parametrisation
that generated the step is unavailable.

This is a DIFFERENT obstruction from the modular one (U114/U116): it is not that a hypothesis
fails, but that the descent is not a self-map of a single equation.
""")

print("=== how many descent steps are available before the parametrisation dies? ===")
for T in (2,4,8,12,16,17,24,32,34,64):
    k=0; x=T
    while x%2==0: x//=2; k+=1
    print(f"  2t = {2*T:<4} -> t = {T:<4}: {k} halvings before the exponent turns odd (odd part {x})")
