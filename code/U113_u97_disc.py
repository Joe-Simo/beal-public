"""Adversarial audit of U97 section 2.2: is disc(f) = 2^24 * 5^5 * Z^68 ?

f(x) = x^5 + 40 U V x^3 + 320 U^2 V^2 x + 64(8 V^5 - U^5),  with U^5 + 8 V^5 = Z^17.
Exact symbolic computation, no floating point.
"""
import sympy as sp

x, U, V, Z = sp.symbols("x U V Z")
f = x**5 + 40*U*V*x**3 + 320*U**2*V**2*x + 64*(8*V**5 - U**5)

d = sp.factor(sp.discriminant(f, x))
print("disc(f) raw factored:")
print(" ", d)

# The Frey relation is U^5 + 8V^5 = Z^17, i.e. 8V^5 - U^5 is NOT Z^17;
# note the sign: the constant term uses 8V^5 - U^5, while the relation is U^5 + 8V^5.
print()
print("Is disc a perfect power times a constant? Express in terms of S = U^5 + 8V^5:")
S = sp.symbols("S")
dd = sp.simplify(d)
# substitute U^5 = S - 8 V^5
sub = sp.simplify(dd.subs(U**5, S - 8*V**5))
print("  disc with U^5 -> S - 8V^5:", sp.factor(sp.expand(sub)))

print()
print("Numeric spot-checks (exact integers):")
for (u, v) in [(1, 0), (1, 1), (3, 2), (5, 7), (11, 4)]:
    dv = sp.Integer(sp.discriminant(f.subs({U: u, V: v}), x))
    s = u**5 + 8*v**5
    print(f"  U={u:>3} V={v:>3}  S=U^5+8V^5={s:<12} disc={sp.factorint(dv) if dv else 0}")
    if dv:
        # test the claim disc == 2^24 * 5^5 * S^? (Z^17 = S so Z^68 = S^4)
        claim = 2**24 * 5**5 * s**4
        print(f"        claimed 2^24*5^5*S^4 = {claim}   match: {dv == claim}")
