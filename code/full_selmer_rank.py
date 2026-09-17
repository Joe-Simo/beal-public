import sys, subprocess
sys.path.insert(0, 'code')
from U79_dyadic_image import LocalRing, witness, binary_rank
import sympy as sp

ring = LocalRing()

# 1. Get fundamental units and mod p1 info from PARI/GP
pari_code = """
default(parisize, "512M");
f = x^34 + 2*x^17 - 4;
bnf = bnfinit(f, 1);
rel_pol = x^17 - (2*y - 2);
k_pol = y^2 - y - 1;
pr5 = idealprimedec(bnf.nf, 5);
p1 = if(pr5[1].f == 1, pr5[1], pr5[2]);

{
for(i=1, 17, 
  print("UNIT|", i, "|", lift(bnf.fu[i]));
  res = polresultant(rel_pol, lift(bnf.fu[i]), x);
  print("NORM|", i, "|", Mod(res, k_pol));
  val = nfmodpr(bnf.nf, bnf.fu[i], p1);
  sq = (val == 1 || val == 4);
  print("SQ5|", i, "|", sq);
);
}
"""

p = subprocess.run(['gp', '-q'], input=pari_code, capture_output=True, text=True)
lines = p.stdout.split('\n')

x = sp.Symbol('x')
units_raw = {}
norms_raw = {}
sq5_raw = {}
for l in lines:
    if l.startswith('UNIT|'):
        parts = l.split('|')
        units_raw[int(parts[1])] = parts[2].replace(' ', '')
    elif l.startswith('NORM|'):
        parts = l.split('|')
        norms_raw[int(parts[1])] = parts[2].replace(' ', '')
    elif l.startswith('SQ5|'):
        parts = l.split('|')
        sq5_raw[int(parts[1])] = 1 if parts[2].strip() == '1' else 0

def poly_to_ring_vec(poly_expr):
    p = sp.Poly(poly_expr, x)
    vec = [0]*34
    for m in range(34):
        coeff = p.nth(m)
        if m < 17:
            vec[2*m] += coeff
        else:
            j = m - 17
            vec[2*j] -= 2*coeff
            vec[2*j+1] += 2*coeff
    int_vec = [int(round(float(v))) for v in vec]
    mod8_vec = tuple(v % 8 for v in int_vec)
    return mod8_vec

def get_full_code(vec):
    v2 = ring.multiply(vec, vec)
    v3 = ring.multiply(v2, vec)
    code, corr, res = ring.squareclass(v3)
    return code

unit_vecs = [poly_to_ring_vec(sp.sympify(units_raw[i])) for i in range(1, 18)]
minus1_vec = tuple(7 if i == 0 else 0 for i in range(34))
all_units = [minus1_vec] + unit_vecs
sq5_all = [0] + [1 - sq5_raw[i] for i in range(1, 18)]

norms = [
    (1, 0), # g0 = -1
    (1, 1), # u1
    (0, 1), # u2
    (1, 1), # u3
    (1, 0), # u4
    (1, 0), # u5
    (1, 0), # u6
    (1, 1), # u7
    (1, 0), # u8
    (1, 1), # u9
    (1, 1), # u10
    (0, 1), # u11
    (1, 1), # u12
    (0, 1), # u13
    (1, 1), # u14
    (0, 1), # u15
    (1, 1), # u16
    (0, 0), # u17
]

A = sp.Matrix([[n[0] for n in norms], [n[1] for n in norms]])
null = A.nullspace(iszerofunc=lambda x: x % 2 == 0)

# Build candidate vectors in local ring:
cand_vecs = []
bit5_list = []
for col in null:
    b = [int(col[i]) % 2 for i in range(18)]
    v = ring.one
    b5 = 0
    for bit, u, s5 in zip(b, all_units, sq5_all):
        if bit:
            v = ring.multiply(v, u)
            b5 ^= s5
    cand_vecs.append(v)
    bit5_list.append(b5)

# Add 17th candidate: h(s)
h_poly = sum((-1)**j * x**(16-j) for j in range(17))
h_vec = poly_to_ring_vec(h_poly)
cand_vecs.append(h_vec)
bit5_list.append(0)

# U79 witnesses:
w_codes = []
for d in range(1, 16, 2):
    for parameter in ('1', 'phi'):
        a, series = witness(ring, d, parameter)
        code, corr, res = ring.squareclass(a)
        w_codes.append(code)

w_pivots = {}
for code in w_codes:
    row = code
    while row:
        p = row.bit_length() - 1
        if p in w_pivots:
            row ^= w_pivots[p]
        else:
            w_pivots[p] = row
            break

def reduce_mod_W2(code):
    row = code
    while row:
        p = row.bit_length() - 1
        if p in w_pivots:
            row ^= w_pivots[p]
        else:
            break
    return row

cand_full_codes = [get_full_code(v) for v in cand_vecs]
reduced_cands = [reduce_mod_W2(c) for c in cand_full_codes]

full_local_coords = [(r | (b5 << 36)) for r, b5 in zip(reduced_cands, bit5_list)]
rank_final = binary_rank(full_local_coords)

print("=" * 60)
print(f"Total global candidates: {len(cand_vecs)}")
print(f"Rank of reduced candidates modulo W_2 (dyadic condition alone): {binary_rank(reduced_cands)}")
print(f"Rank of candidates combined with prime 5 condition: {rank_final}")
print(f"Dimension of 2-Selmer upper bound: {len(cand_vecs) - rank_final}")
print("=" * 60)
