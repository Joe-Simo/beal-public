import numpy as np

p = 13
def canon(A):
    for r in range(2):
        for c in range(2):
            if A[r][c] % p != 0:
                if (A[r][c] % p) > (p-1)//2:
                    return (((-A[0][0])%p, (-A[0][1])%p), ((-A[1][0])%p, (-A[1][1])%p))
                else:
                    return (((A[0][0])%p, (A[0][1])%p), ((A[1][0])%p, (A[1][1])%p))
    return ((0,0),(0,0))

def mmult(A, B):
    return canon([
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0])%p, (A[0][0]*B[0][1] + A[0][1]*B[1][1])%p],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0])%p, (A[1][0]*B[0][1] + A[1][1]*B[1][1])%p]
    ])

def minv(A):
    return canon([[A[1][1], (-A[0][1])%p], [(-A[1][0])%p, A[0][0]]])

# Elements of PSL(2, 13)
G = []
for a in range(p):
    for b in range(p):
        for c in range(p):
            for d in range(p):
                if (a*d - b*c) % p == 1:
                    m = canon([[a, b], [c, d]])
                    if m not in G:
                        G.append(m)

elem_to_idx = {g: i for i, g in enumerate(G)}
idx_to_elem = G
n = len(G)
assert n == 1092

mult_table = [[elem_to_idx[mmult(G[i], G[j])] for j in range(n)] for i in range(n)]
inv_table = [elem_to_idx[minv(G[i])] for i in range(n)]

# Generators S, R, T
S = canon([[0, -1], [1, 0]])
T = canon([[1, 1], [0, 1]])
R = mmult(S, T)

idx_S = elem_to_idx[S]
idx_T = elem_to_idx[T]
idx_R = elem_to_idx[R]

def get_subgroup(gens):
    sub = set(gens) | {elem_to_idx[canon([[1, 0], [0, 1]])]}
    queue = list(sub)
    while queue:
        x = queue.pop()
        for y in list(sub):
            for xy in [mult_table[x][y], mult_table[y][x]]:
                if xy not in sub:
                    sub.add(xy)
                    queue.append(xy)
    return frozenset(sub)

def conjugate_subgroup(sub, g_idx):
    g_inv = inv_table[g_idx]
    return frozenset(mult_table[mult_table[g_idx][h]][g_inv] for h in sub)

def compute_genus(sub):
    order_H = len(sub)
    mu = n // order_H
    
    # Left cosets gH
    cosets = []
    elem_to_coset = {}
    for g in range(n):
        if g not in elem_to_coset:
            c_idx = len(cosets)
            coset = [mult_table[g][h] for h in sub]
            cosets.append(coset)
            for ch in coset:
                elem_to_coset[ch] = c_idx
    
    assert len(cosets) == mu
    
    # Action of S on cosets: S * (gH)
    nu_2 = 0
    for i, coset in enumerate(cosets):
        rep = coset[0]
        s_rep = mult_table[idx_S][rep]
        if elem_to_coset[s_rep] == i:
            nu_2 += 1
            
    # Action of R on cosets: R * (gH)
    nu_3 = 0
    for i, coset in enumerate(cosets):
        rep = coset[0]
        r_rep = mult_table[idx_R][rep]
        if elem_to_coset[r_rep] == i:
            nu_3 += 1
            
    # Orbits of T on cosets
    visited = set()
    nu_inf = 0
    for i in range(mu):
        if i not in visited:
            nu_inf += 1
            cur = i
            while cur not in visited:
                visited.add(cur)
                rep = cosets[cur][0]
                t_rep = mult_table[idx_T][rep]
                cur = elem_to_coset[t_rep]
                
    num = mu - 3*nu_2 - 4*nu_3 - 6*nu_inf
    assert num % 12 == 0
    g = 1 + num // 12
    return {
        "order": order_H,
        "mu": mu,
        "nu_2": nu_2,
        "nu_3": nu_3,
        "nu_inf": nu_inf,
        "genus": g
    }

if __name__ == "__main__":
    print("Setup verified.")
