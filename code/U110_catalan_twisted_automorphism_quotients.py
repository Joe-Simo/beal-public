import sympy
from fractions import Fraction

def mult_mat(m1, m2, p):
    a1, b1, c1, d1 = m1
    a2, b2, c2, d2 = m2
    return (
        (a1*a2 + b1*c2) % p,
        (a1*b2 + b1*d2) % p,
        (c1*a2 + d1*c2) % p,
        (c1*b2 + d1*d2) % p
    )

def canon(m, p):
    a, b, c, d = m
    neg = ((-a)%p, (-b)%p, (-c)%p, (-d)%p)
    return min(m, neg)

def inv_mat(m, p):
    a, b, c, d = m
    return canon((d, (-b)%p, (-c)%p, a), p)

def get_psl2(p):
    elements = []
    seen = set()
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    if (a*d - b*c) % p == 1:
                        rep = canon((a, b, c, d), p)
                        if rep not in seen:
                            seen.add(rep)
                            elements.append(rep)
    return elements

def mat_order(m, p):
    cur = m
    identity = canon((1, 0, 0, 1), p)
    order = 1
    while cur != identity:
        cur = canon(mult_mat(cur, m, p), p)
        order += 1
    return order

def compute_genus(p, H, elts, S, R, T_powers):
    h = len(H)
    d = len(elts) // h
    seen = set()
    cusp_count = 0
    for g in elts:
        if g not in seen:
            coset = set()
            for b in H:
                for t in T_powers:
                    coset.add(canon(mult_mat(mult_mat(b, g, p), t, p), p))
            seen.update(coset)
            cusp_count += 1
    e2 = sum(1 for g in elts if canon(mult_mat(mult_mat(inv_mat(g, p), S, p), g, p), p) in H) // h
    e3 = sum(1 for g in elts if canon(mult_mat(mult_mat(inv_mat(g, p), R, p), g, p), p) in H) // h
    g = 1 + Fraction(d, 12) - Fraction(e2, 4) - Fraction(e3, 3) - Fraction(cusp_count, 2)
    assert g.denominator == 1
    return int(g), d, e2, e3, cusp_count

for p in [13, 17]:
    elts = get_psl2(p)
    mu = len(elts)
    I = canon((1, 0, 0, 1), p)
    S = canon((0, (-1)%p, 1, 0), p)
    R = canon((0, (-1)%p, 1, 1), p)
    T = canon((1, 1, 0, 1), p)
    T_powers = [I]
    cur = I
    for _ in range(p-1):
        cur = canon(mult_mat(cur, T, p), p)
        T_powers.append(cur)

    # Find generator of order (p-1)//2 in F_p^x / +-1
    for g_cand in range(2, p):
        powers = [pow(g_cand, i, p) for i in range((p-1))]
        mod_pm = set(min(x, p - x) for x in powers)
        if len(mod_pm) == (p-1)//2:
            gen_mult = g_cand
            break

    subgroups = []
    subgroups.append(("Trivial {1} [X(p)]", {I}))
    subgroups.append((f"Full PSL_2(F_{p}) [X(1)]", set(elts)))
    subgroups.append((f"Unipotent U = <T> [X_1({p})]", set(T_powers)))
    
    # Borel
    B_elts = set(m for m in elts if m[2] % p == 0)
    subgroups.append((f"Borel B [X_0({p})]", B_elts))
    
    # Sub-borels
    divs = sympy.divisors((p-1)//2)
    for k in divs:
        if k == 1 or k == (p-1)//2:
            continue
        step = ((p-1)//2) // k
        sub_mults = [pow(gen_mult, step * i, p) for i in range(k)]
        sub_B = set()
        for b in range(p):
            for a in sub_mults:
                a_inv = pow(a, -1, p)
                sub_B.add(canon((a, b, 0, a_inv), p))
        subgroups.append((f"Sub-Borel U : Z/{k} (order {len(sub_B)})", sub_B))

    # Split Cartan
    C_sp_elts = set(m for m in elts if m[1] % p == 0 and m[2] % p == 0)
    subgroups.append((f"Split Cartan C_sp [X_sp({p})]", C_sp_elts))
    
    for k in divs:
        if k == 1 or k == (p-1)//2:
            continue
        step = ((p-1)//2) // k
        sub_C_sp = set()
        for i in range(k):
            a = pow(gen_mult, step * i, p)
            a_inv = pow(a, -1, p)
            sub_C_sp.add(canon((a, 0, 0, a_inv), p))
        subgroups.append((f"Sub-Cartan cyclic Z/{k} (order {len(sub_C_sp)})", sub_C_sp))

    # Involution <w>
    subgroups.append(("Involution <w> (Cartan/Atkin-Lehner)", {I, S}))
    # Order 3
    R2 = canon(mult_mat(R, R, p), p)
    subgroups.append(("Cyclic <R> (order 3)", {I, R, R2}))

    # Normalizer N_sp
    N_sp_elts = set(C_sp_elts)
    for m in C_sp_elts:
        N_sp_elts.add(canon(mult_mat(m, S, p), p))
    subgroups.append((f"Split Cartan Normalizer N_sp [X_sp^+({p})]", N_sp_elts))

    for k in divs:
        if k == 1:
            continue
        step = ((p-1)//2) // k
        sub_D = set()
        for i in range(k):
            a = pow(gen_mult, step * i, p)
            a_inv = pow(a, -1, p)
            m = canon((a, 0, 0, a_inv), p)
            sub_D.add(m)
            sub_D.add(canon(mult_mat(m, S, p), p))
        if k != (p-1)//2:
            subgroups.append((f"Dihedral D_{k} (order {len(sub_D)}, in N_sp)", sub_D))

    # Non-split Cartan
    xi = 2
    while sympy.is_quad_residue(xi, p):
        xi += 1
    C_ns_elts = []
    for x in range(p):
        for y in range(p):
            if (x*x - xi*y*y) % p == 1:
                C_ns_elts.append(canon((x, (xi*y)%p, y, x), p))
    C_ns_elts = list(set(C_ns_elts))
    subgroups.append((f"Non-split Cartan C_ns [X_ns({p})]", set(C_ns_elts)))

    divs_ns = sympy.divisors((p+1)//2)
    gen_ns = None
    for m in C_ns_elts:
        if mat_order(m, p) == (p+1)//2:
            gen_ns = m
            break
    if gen_ns is not None:
        for k in divs_ns:
            if k == 1 or k == (p+1)//2:
                continue
            step = ((p+1)//2) // k
            sub_C_ns = set()
            cur_m = I
            base = I
            for _ in range(step):
                base = canon(mult_mat(base, gen_ns, p), p)
            for _ in range(k):
                sub_C_ns.add(cur_m)
                cur_m = canon(mult_mat(cur_m, base, p), p)
            subgroups.append((f"Sub-Cartan cyclic Z/{k} (in C_ns)", sub_C_ns))

    # N_ns
    w_ns = None
    C_ns_set = set(C_ns_elts)
    for m in elts:
        if mat_order(m, p) == 2 and m not in C_ns_set:
            normalizes = True
            for c in C_ns_elts:
                conj = canon(mult_mat(mult_mat(m, c, p), m, p), p)
                if conj not in C_ns_set:
                    normalizes = False
                    break
            if normalizes:
                w_ns = m
                break
    if w_ns is not None:
        N_ns_elts = set(C_ns_elts)
        for c in C_ns_elts:
            N_ns_elts.add(canon(mult_mat(c, w_ns, p), p))
        subgroups.append((f"Non-split Cartan Normalizer N_ns [X_ns^+({p})]", N_ns_elts))

        for k in divs_ns:
            if k == 1:
                continue
            step = ((p+1)//2) // k
            sub_D_ns = set()
            base = I
            for _ in range(step):
                base = canon(mult_mat(base, gen_ns, p), p)
            cur_m = I
            for _ in range(k):
                sub_D_ns.add(cur_m)
                sub_D_ns.add(canon(mult_mat(cur_m, w_ns, p), p))
                cur_m = canon(mult_mat(cur_m, base, p), p)
            if k != (p+1)//2:
                subgroups.append((f"Dihedral D_{k} (order {len(sub_D_ns)}, in N_ns)", sub_D_ns))

    # Exceptional A_4 (order 12)
    A4 = None
    for s_cand in elts:
        if mat_order(s_cand, p) == 2:
            for r_cand in elts:
                if mat_order(r_cand, p) == 3:
                    sr = canon(mult_mat(s_cand, r_cand, p), p)
                    if mat_order(sr, p) == 3:
                        group = {I, s_cand, r_cand}
                        while True:
                            new_group = set(group)
                            for g1 in group:
                                for g2 in group:
                                    new_group.add(canon(mult_mat(g1, g2, p), p))
                            if len(new_group) == len(group):
                                break
                            group = new_group
                            if len(group) > 12:
                                break
                        if len(group) == 12:
                            A4 = group
                            break
            if A4 is not None:
                break
    if A4 is not None:
        subgroups.append(("Exceptional A_4 (order 12)", A4))

    # Exceptional S_4 (order 24)
    S4 = None
    if p % 8 in [1, 7]:
        for s_cand in elts:
            if mat_order(s_cand, p) == 2:
                for r_cand in elts:
                    if mat_order(r_cand, p) == 3:
                        sr = canon(mult_mat(s_cand, r_cand, p), p)
                        if mat_order(sr, p) == 4:
                            group = {I, s_cand, r_cand}
                            while True:
                                new_group = set(group)
                                for g1 in group:
                                    for g2 in group:
                                        new_group.add(canon(mult_mat(g1, g2, p), p))
                                if len(new_group) == len(group):
                                    break
                                group = new_group
                                if len(group) > 24:
                                    break
                            if len(group) == 24:
                                S4 = group
                                break
                if S4 is not None:
                    break
        if S4 is not None:
            subgroups.append(("Exceptional S_4 (order 24)", S4))

    print("=" * 85)
    print(f"EXHAUSTIVE MODULAR SUBGROUPS & QUOTIENT GENERA FOR LEVEL p = {p}")
    print(f"|PSL_2(F_{p})| = {mu}, g(X({p})) = {1 + (p**2 - 1)*(p - 6)//24}")
    print("=" * 85)
    print(f"{'Subgroup H':<50} | {'|H|':<5} | {'deg':<5} | {'e2':<4} | {'e3':<4} | {'e_inf':<5} | {'g(X/H)':<6}")
    print("-" * 88)
    for name, H in subgroups:
        g, d, e2, e3, e_inf = compute_genus(p, H, elts, S, R, T_powers)
        print(f"{name:<50} | {len(H):<5} | {d:<5} | {e2:<4} | {e3:<4} | {e_inf:<5} | {g:<6}")
    print()
