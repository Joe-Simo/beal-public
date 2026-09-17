import sys
sys.path.append("code")
from U110_psl2_13_subgroups_and_genera import *

m6 = canon([[2, 0], [0, 7]])
idx_m6 = elem_to_idx[m6]
m3 = mult_table[idx_m6][idx_m6]
m2_diag = mult_table[m3][idx_m6]

# 1. Trivial
H_triv = get_subgroup([])

# 2. Cyclic C_2
H_2 = get_subgroup([idx_S])

# 3. Cyclic C_3
H_3 = get_subgroup([m3])

# 4. Klein 4-group V_4
H_4_v4 = get_subgroup([m2_diag, idx_S])

# 5. Split Cartan C_6
H_6 = get_subgroup([idx_m6])

# 6. Dihedral D_3 = S_3
H_6_d3 = get_subgroup([m3, idx_S])

# 7. Non-split Cartan C_7
elem_7 = None
for i in range(n):
    cur = i
    ord_i = 1
    while cur != elem_to_idx[canon([[1,0],[0,1]])]:
        cur = mult_table[cur][i]
        ord_i += 1
    if ord_i == 7:
        elem_7 = i
        break
H_7 = get_subgroup([elem_7])

# 8. Alternating group A_4
elem_norm_3 = None
for i in range(n):
    if mult_table[mult_table[i][i]][i] == elem_to_idx[canon([[1,0],[0,1]])] and i != elem_to_idx[canon([[1,0],[0,1]])]:
        norm = True
        for h in H_4_v4:
            conj = mult_table[mult_table[i][h]][inv_table[i]]
            if conj not in H_4_v4:
                norm = False
                break
        if norm:
            elem_norm_3 = i
            break
H_12_a4 = get_subgroup([m2_diag, idx_S, elem_norm_3])

# 9. Split Cartan normalizer D_6 (N_sp)
H_12_sp = get_subgroup([idx_m6, idx_S])

# 10. Non-split Cartan normalizer D_7 (N_ns)
elem_inv_7 = None
for i in range(n):
    if mult_table[i][i] == elem_to_idx[canon([[1,0],[0,1]])]:
        conj = mult_table[mult_table[i][elem_7]][i]
        if conj in H_7 and conj != elem_7:
            elem_inv_7 = i
            break
H_14_ns = get_subgroup([elem_7, elem_inv_7])

# 11. Sylow 13 C_13
H_13 = get_subgroup([idx_T])

# 12. Borel sub C_13 : C_2
H_26 = get_subgroup([idx_T, m2_diag])

# 13. Borel sub C_13 : C_3
H_39 = get_subgroup([idx_T, m3])

# 14. Borel B = C_13 : C_6 = X_0(13)
H_78 = get_subgroup([idx_T, idx_m6])

# 15. Full PSL(2, 13)
H_full = frozenset(range(n))

subs = [
    ("X(13) [H = {1}]", H_triv),
    ("C_2", H_2),
    ("C_3", H_3),
    ("V_4 = C_2 x C_2", H_4_v4),
    ("C_6 (Split Cartan)", H_6),
    ("D_3 = S_3", H_6_d3),
    ("C_7 (Non-split Cartan)", H_7),
    ("A_4", H_12_a4),
    ("D_6 = N_sp (Split Cartan Norm)", H_12_sp),
    ("D_7 = N_ns (Non-split Cartan Norm)", H_14_ns),
    ("C_13 (Sylow 13)", H_13),
    ("C_13 : C_2", H_26),
    ("C_13 : C_3", H_39),
    ("Borel B = X_0(13)", H_78),
    ("Full PSL(2, 13) = X(1)", H_full)
]

print(f"{'Quotient Curve / Subgroup H':<35} | {'|H|':<5} | {'mu':<5} | {'nu_2':<5} | {'nu_3':<5} | {'nu_inf':<6} | {'Genus g':<7}")
print("-" * 80)
for name, sub in subs:
    res = compute_genus(sub)
    print(f"{name:<35} | {res['order']:<5} | {res['mu']:<5} | {res['nu_2']:<5} | {res['nu_3']:<5} | {res['nu_inf']:<6} | {res['genus']:<7}")
