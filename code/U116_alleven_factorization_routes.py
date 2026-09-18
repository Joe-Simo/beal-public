"""Does the DIRECT factorization route escape the AB-coefficient obstruction?

U114 Part VIII showed: every (r,r,p)-reduction of the all-even branch obtained from the
PYTHAGOREAN parametrisation has AB = 1 or a power of 2, hence fails Azon's Hypothesis 5.

There is a second, independent way to reduce the all-even case, not via Pythagorean triples:
factor the difference of powers directly.

    A^(2r) = C^(2t) - B^(2s) = (C^t - B^s)(C^t + B^s).

Let d = gcd(C^t - B^s, C^t + B^s).  Then d | 2C^t and d | 2B^s, and gcd(B,C)=1 (verified:
gcd_bc_eq_one), so d | 2.

CASE 1, A odd.  Then A^(2r) is odd, so both factors are odd, so d = 1 and each factor is a
perfect (2r)-th power:
        C^t - B^s = u^(2r),   C^t + B^s = v^(2r)
    =>  2 C^t = u^(2r) + v^(2r)                       coefficients (A,B,C) = (1, 1, 2)

CASE 2, A even.  B, C are then both odd (they cannot both be even, by coprimality), so
C^t - B^s and C^t + B^s are both even with d = 2.  Exactly one of them is divisible by 4
(their sum is 2C^t, which is 2 x odd).  Writing the (2r)-th power split accordingly:
        C^t - B^s = 2 u^(2r),   C^t + B^s = 2^(2r-1) v^(2r)      (or the two swapped)
    =>  2 C^t = 2 u^(2r) + 2^(2r-1) v^(2r)
    =>  C^t = u^(2r) + 2^(2r-2) v^(2r)                coefficients (A,B,C) = (1, 2^(2r-2), 1)

In BOTH cases AB is 1 or a power of 2 -- the same obstruction.
"""
import sympy as sp
from sympy import factorint, n_order

u, v, Bs, Ct = sp.symbols("u v Bs Ct", positive=True)

print("=== CASE 1 (A odd): verify 2C^t = u^(2r) + v^(2r) follows from the split ===")
for r in (5, 7):
    # C^t - B^s = u^(2r),  C^t + B^s = v^(2r)
    sol = sp.solve([sp.Eq(Ct - Bs, u**(2*r)), sp.Eq(Ct + Bs, v**(2*r))], [Ct, Bs], dict=True)[0]
    lhs = sp.simplify(2*sol[Ct])
    print(f"  r={r}: 2C^t = {sp.simplify(lhs)}   -> (A,B,C) = (1,1,2), AB = 1")

print("\n=== CASE 2 (A even): verify C^t = u^(2r) + 2^(2r-2) v^(2r) ===")
for r in (5, 7):
    sol = sp.solve([sp.Eq(Ct - Bs, 2*u**(2*r)), sp.Eq(Ct + Bs, 2**(2*r-1)*v**(2*r))],
                   [Ct, Bs], dict=True)[0]
    print(f"  r={r}: C^t = {sp.simplify(sol[Ct])}   -> (A,B,C) = (1, 2^(2r-2), 1), "
          f"AB = 2^{2*r-2}")

def hyp5(A, B, r):
    AB = abs(A*B)
    if AB <= 1: return False, f"AB={AB} has no prime factors"
    for q, e in factorint(AB).items():
        if (2*r) % q == 0: continue
        if n_order(q, r) % 2 == 0: return True, f"witness q={q}"
    return False, f"every prime factor of AB={AB} divides 2r={2*r} or has odd order mod {r}"

print("\n=== Hypothesis 5 verdict for every reduction reachable by either route ===")
for label, A, B, r in [
    ("Pythagorean, odd leg      (1,1,2)", 1, 1, 5),
    ("direct factorisation, A odd (1,1,2)", 1, 1, 5),
    ("direct factorisation, A even (1,2^8)", 1, 2**8, 5),
    ("project orientation B        (1,8)", 1, 8, 5),
    ("direct factorisation, r=7, A even", 1, 2**12, 7),
]:
    ok, why = hyp5(A, B, r)
    print(f"  {label:<40} {'HOLDS' if ok else 'FAILS':<6} ({why})")

print("""
CONCLUSION.  The two independent reduction routes for the all-even branch -- the Pythagorean
parametrisation and the direct factorisation of A^(2r) = (C^t - B^s)(C^t + B^s) -- BOTH force
AB to be 1 or a power of 2.

The reason is structural and the same in both: the only ambiguity in splitting coprime factors
of a difference of powers is the factor 2 coming from parity.  No other prime can enter the
coefficients, because the two factors are coprime away from 2.

Since Azon's Hypothesis 5 requires a prime factor of AB NOT dividing 2r, and 2 | 2r always,
the hypothesis fails for EVERY reduction reachable by either route.
""")
