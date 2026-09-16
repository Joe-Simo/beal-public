"""Exact algebraic certificates used by U92's Kummer-cover proof."""
from __future__ import annotations

from math import comb
import json
import sympy as sp

v = sp.symbols("v")
G = sum((-1) ** j * comb(17, 2 * j) * v**j for j in range(9))
H = sum((-1) ** j * comb(17, 2 * j + 1) * v**j for j in range(9))

assert sp.Poly(G, v).all_coeffs() == [17, -680, 6188, -19448, 24310, -12376, 2380, -136, 1]
assert sp.Poly(H, v).all_coeffs() == [1, -136, 2380, -12376, 24310, -19448, 6188, -680, 17]

resultant = abs(int(sp.resultant(G, H, v)))
disc_g = abs(int(sp.discriminant(G, v)))
disc_h = abs(int(sp.discriminant(H, v)))
assert sp.factorint(resultant) == {2: 136}
assert sp.factorint(disc_g) == {2: 112, 17: 7}
assert sp.factorint(disc_h) == {2: 112, 17: 7}

# Three independent degree-five Kummer directions give degree 125.
degree = 5**3
branch_points = 1 + 16 + 16 + 1
ramification_contribution_per_branch = (degree // 5) * (5 - 1)
rh_right = -2 * degree + branch_points * ramification_contribution_per_branch
assert rh_right == 3150
genus = (rh_right + 2) // 2
assert genus == 1576
branch_fiber_point_cap = branch_points * (degree // 5)
assert branch_fiber_point_cap == 850

# q+1-2g sqrt(q)>850 is implied, for q>849, by
# (q-849)^2 > (2g)^2 q.
threshold = 850
while (threshold - 849) ** 2 <= (2 * genus) ** 2 * threshold:
    threshold += 1
assert threshold == 9_936_802
assert (threshold - 1 - 849) ** 2 <= (2 * genus) ** 2 * (threshold - 1)
assert (threshold - 849) ** 2 > (2 * genus) ** 2 * threshold

print(json.dumps({
    "checkpoint": "U92",
    "resultant_G_H_factorization": {"2": 136},
    "discriminant_G_factorization": {"2": 112, "17": 7},
    "discriminant_H_factorization": {"2": 112, "17": 7},
    "kummer_degree": degree,
    "branch_points": branch_points,
    "riemann_hurwitz_right_side": rh_right,
    "genus": genus,
    "branch_fiber_point_cap": branch_fiber_point_cap,
    "hasse_weil_coefficient": 2 * genus,
    "threshold": threshold,
    "full_Beal_solved": False,
}, indent=2))
