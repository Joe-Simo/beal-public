"""Does Azon's Hypothesis 5 hold for the weighted equation U^5 + 8V^5 = Z^17?

Azon arXiv:2504.01967v2, signature (r,r,p) with r=5, p=17, A=1, B=8, C=1.

Definition 4.1:  nu_q := v_q( s0 (s0 - 1) ).
Proposition 3.22 (2) and its proof give, for signature (r,r,p):
    t0 = A a^r / (C c^p),      t0 (t0 - 1) = - A B a^r b^r / (A a^r + B b^r)^2,
    es0 := 2 - 4 s0,           es0^2 = 1/(t0 (t0 - 1)) + 4.
Hence  s0 (s0 - 1) = (es0^2 - 4)/16 = 1 / (16 t0 (t0 - 1)),  so for q odd

    nu_q = 2 p v_q(c) + 2 v_q(C) - v_q(AB) - r v_q(ab).

Hypothesis 5 needs some prime q0 NOT dividing 2r with
   (i) nu_{q0} < 0,  (ii) nu_{q0} != 0 mod r,  (iii) ord*(q0 mod r) even.
"""
from sympy import symbols, simplify, Rational, factorint, primerange, n_order

r, p = 5, 17
A, B, C = 1, 8, 1

# --- symbolic verification of s0(s0-1) = 1/(16 t0 (t0-1)) ---
import sympy as sp
a, b, c = sp.symbols("a b c", positive=True)
t0 = sp.Rational(A, C) * a**r / c**p
lhs = sp.simplify(t0 * (t0 - 1))
rhs = sp.simplify(-sp.Integer(A * B) * a**r * b**r / (A * a**r + B * b**r)**2)
# substitute the equation A a^r + B b^r = C c^p into rhs
rhs_sub = sp.simplify(rhs.subs(A * a**r + B * b**r, C * c**p))
print("t0(t0-1) identity check (needs the equation to close):")
print("  t0(t0-1)      =", lhs)
print("  claimed form  =", sp.simplify(-sp.Integer(A*B)*a**r*b**r/(C*c**p)**2))
diff = sp.simplify(lhs - (-sp.Integer(A*B)*a**r*b**r/(C*c**p)**2))
print("  difference, after substituting B b^r = C c^p - A a^r:")
print("   ", sp.simplify(diff.subs(b**r, (C*c**p - A*a**r)/B)))

def nu(q, vc, vab):
    """nu_q for odd q, from the formula above."""
    from sympy import factorint
    vq_AB = factorint(A * B).get(q, 0)
    vq_C = factorint(C).get(q, 0) if C > 1 else 0
    return 2 * p * vc + 2 * vq_C - vq_AB - r * vab

print("\nPrimitivity: gcd(U,V)=1 and gcd(UV,Z)=1, so each prime divides at most one of ab, c.\n")
print(f"{'case':<26}{'nu_q':<22}{'nu_q<0?':<10}{'nu_q != 0 mod 5?'}")
rows = [
    ("q | Z  (vc=k>0, vab=0)", "2*17*k = 34k > 0", "NO", "-"),
    ("q | UV (vc=0, vab=m>0)", "-5m  (q does not divide AB=8)", "yes", "NO: -5m = 0 mod 5"),
    ("q | UV and q | AB=8", "q would be 2, but 2 | 2r=10", "excluded", "excluded"),
    ("q does not divide UVZ", "0", "NO", "-"),
]
for r_ in rows:
    print(f"{r_[0]:<26}{r_[1]:<22}{r_[2]:<10}{r_[3]}")

print("\nExact numeric spot-check of the formula on the two live cases:")
for (vc, vab, label) in [(1, 0, "q | Z"), (0, 1, "q | UV"), (0, 3, "q | UV, v=3")]:
    v = nu(7, vc, vab)
    print(f"  q=7 {label:<14} nu_q = {v:<6} <0: {v < 0}   nu_q mod 5 = {v % 5}")

print("\nord*(q mod 5) is even  <=>  q != 1 mod 5   (since (Z/5Z)* is cyclic of order 4)")
print("  check:", {q: n_order(q, 5) for q in [7, 11, 13, 17, 19, 23] })

print("""
CONCLUSION.  For every prime q not dividing 2r = 10:
  - if q | Z  then nu_q = 34 v_q(Z) > 0, failing condition (i);
  - if q | UV then nu_q = -5 v_q(UV), which is < 0 but is = 0 mod 5, failing condition (ii);
  - otherwise nu_q = 0, failing (i).
The only prime that could give nu_q < 0 with nu_q != 0 mod 5 would have to divide AB = 8,
i.e. q = 2 -- which is excluded because 2 | 2r = 10.

Hypothesis 5 therefore FAILS IDENTICALLY for U^5 + 8V^5 = Z^17, confirming U96's conclusion,
and the REASON is structural: A = C = 1 and AB = 8 is a power of 2.
""")
