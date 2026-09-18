"""Audit of U105 Pathway 2 'Diophantine Degree Obstruction'.

U105 states: a positive integer solution gives c = i*2^(4/5), which generates degree 10
over k = Q(sqrt5), so [k(u,v):k] = 10 != 1, hence C^-(k) contains no points from solutions.

If that degree claim is TRUE, it is fatal to the argument, not supportive: Chabauty-Coleman
with rank < genus bounds only the k-RATIONAL points. Points of degree 10 over k are simply
not in C^-(k), so a bound on #C^-(k) says nothing about them.
"""
import sympy as sp

x = sp.symbols("x")
c = sp.I * 2 ** sp.Rational(4, 5)
mp = sp.minimal_polynomial(c, x)
print("c = i * 2^(4/5)")
print("  minimal polynomial over Q:", mp)
print("  degree over Q            :", sp.degree(mp, x))

# degree over k = Q(sqrt5): Q(i, 2^(1/5)) has degree 10 and is linearly disjoint from Q(sqrt5)
# (its Galois closure ramifies only at 2 and 5... check disjointness by degree of mp over k)
sqrt5 = sp.sqrt(5)
mp_k = sp.minimal_polynomial(c, x, domain=sp.QQ.algebraic_field(sqrt5))
print("  minimal polynomial over k=Q(sqrt5) has degree:", sp.degree(mp_k, x))

print()
print("CONSEQUENCE:")
d = sp.degree(mp_k, x)
if d > 1:
    print(f"  A solution yields a point of degree {d} over k, i.e. a point of C^-(L) with [L:k]={d}.")
    print("  Such a point is NOT an element of C^-(k).")
    print("  Chabauty-Coleman (rank_Z J^-(k) <= 2 < g = 8) bounds #C^-(k) ONLY.")
    print("  Therefore the bound #C^-(k) <= 9 is silent about solutions, and the step")
    print("  'C^-(k) contains NO POINTS arising from solutions => no solutions' is a NON SEQUITUR:")
    print("  it is vacuously true and carries no Diophantine content.")
    print()
    print("  To reach the intended conclusion one needs Chabauty over L (degree 10 over k,")
    print("  so degree 20 over Q), where rank_Z J^-(L) < g = 8 must be RE-ESTABLISHED --")
    print("  ranks grow in extensions -- or a symmetric-power / covering-collection argument.")
    print("  Neither is present in U105, U99 or U102.")
