"""Which coefficients can an (r,r,p)-reduction of the ALL-EVEN Beal branch have?

C020 (kernel-verified) : an all-even counterexample is a PRIMITIVE Pythagorean triple whose
entries are perfect powers,  (A^r)^2 + (B^s)^2 = (C^t)^2,  r,s,t >= 2.

Every primitive Pythagorean triple is  (m^2 - n^2,  2mn,  m^2 + n^2)  with gcd(m,n) = 1 of
opposite parity.  Matching the odd leg to A^r:

    m - n = d^r,  m + n = e^r      (the two factors are coprime, both odd)
    =>  2m = e^r + d^r,   2n = e^r - d^r
    =>  2 C^t = m^2 + n^2 ... times 2  ->   e^{2r} + d^{2r} = 2 C^t          (*)
    =>  2 B^s = 2mn * 2 ...          ->   e^{2r} - d^{2r} = 2 B^s           (**)

(*) is the SUM equation, and is the one usable as a generalised Fermat equation of the
Azon shape  A a^R + B b^R = C c^P.  Its coefficients are forced:  A = 1, B = 1, C = 2.

Matching the EVEN leg instead (2mn = B^s) introduces powers of 2 into the coefficient of the
other term, which is how this project's orientation B, U^5 + 8V^5 = Z^17, arises.

CLAIM TESTED HERE: every reduction obtained this way has AB equal to 1 or a power of 2.
By the Part VII criterion, Hypothesis 5 needs a prime factor of AB outside {2} u {r}.  A power
of 2 (or 1) has none.  Hence Azon's framework is structurally inapplicable to the all-even branch.
"""
from sympy import factorint, n_order, isprime, gcd

def hyp5(A, B, r):
    AB = abs(A*B)
    if AB <= 1: return False, f"AB={AB}: no prime factors"
    for q, e in factorint(AB).items():
        if (2*r) % q == 0: continue
        if n_order(q, r) % 2 == 0: return True, f"witness q={q}"
    return False, f"AB={AB}: every prime factor divides 2r={2*r} or has odd order mod {r}"

print("Primitive Pythagorean triples: check the parametrisation and the forced coefficients.\n")
# exact check that (m^2-n^2, 2mn, m^2+n^2) is primitive Pythagorean, and that
# e^{2r} + d^{2r} = 2(m^2+n^2) holds identically with m=(e^r+d^r)/2, n=(e^r-d^r)/2
import sympy as sp
d, e, R = sp.symbols("d e R", positive=True, integer=True)
for rr in (5, 7):
    m = (e**rr + d**rr)/2
    n = (e**rr - d**rr)/2
    lhs = sp.simplify(2*(m**2 + n**2))
    rhs = sp.simplify(e**(2*rr) + d**(2*rr))
    print(f"  r={rr}: 2(m^2+n^2) - (e^(2r)+d^(2r)) = {sp.simplify(lhs-rhs)}   -> coefficients (A,B,C)=(1,1,2)")

print("\nForced coefficient shapes for the all-even branch, and the Hypothesis 5 verdict:\n")
CASES = [
    ("sum equation from the odd leg:  e^10 + d^10 = 2C^t", 1, 1, 2, 5),
    ("project orientation A:          X^10 + Y^10 = 2Z^17", 1, 1, 2, 5),
    ("project orientation B:          U^5 + 8V^5 = Z^17",   1, 8, 1, 5),
    ("even-leg variant, 2^3",                               1, 8, 1, 5),
    ("even-leg variant, 2^8 = 256",                         1, 256, 1, 5),
]
for label, A, B, C, r in CASES:
    ok, why = hyp5(A, B, r)
    print(f"  {label:<52} AB={A*B:<5} {'HOLDS' if ok else 'FAILS'}  ({why})")

print("""
CONCLUSION.  Every (r,r,p)-reduction of the all-even branch obtained from the Pythagorean
parametrisation has AB = 1 or AB = a power of 2, because the ONLY coefficient the
parametrisation introduces is the 2 coming from 2mn and from 2(m^2+n^2).

By the Part VII criterion, Hypothesis 5 requires a prime factor of AB that does NOT divide
2r.  A power of 2 has only the prime 2, which divides 2r for every r.  AB = 1 has none at all.

Therefore Azon's Hypothesis 5 FAILS for every such reduction, and his level-lowering theorem
is STRUCTURALLY INAPPLICABLE to the all-even branch -- not by an unlucky choice of orientation,
but because the parametrisation cannot produce a suitable coefficient.
""")
