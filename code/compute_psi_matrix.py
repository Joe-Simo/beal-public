import sys, subprocess
sys.path.insert(0, 'code')
from U79_dyadic_image import LocalRing, binary_rank
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

# Helper to convert polynomial to local ring vector:
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

# Helper to compute low16 code for an element in the local ring
def get_low16(vec):
    v2 = ring.multiply(vec, vec)
    v3 = ring.multiply(v2, vec)
    code, corr, res = ring.squareclass(v3)
    return code & 0xffff

unit_vecs = []
for i in range(1, 18):
    poly = sp.sympify(units_raw[i])
    unit_vecs.append(poly_to_ring_vec(poly))

# Unit g0 = -1
minus1_vec = tuple(7 if i == 0 else 0 for i in range(34))
all_units = [minus1_vec] + unit_vecs

# Non-square bit at 5:
# For units, quotient bit at 5 is: (1 - is_square) mod 2, so 0 if square, 1 if non-square.
# -1 mod 5 = 4 (square), so bit at 5 for -1 is 0.
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

# Build 17-bit vector for each candidate:
# bit 0..15: dyadic low16 bits
# bit 16: bit at 5
matrix_rows = []

# 16 unit candidates in norm kernel:
for col in null:
    b = [int(col[i]) % 2 for i in range(18)]
    v = ring.one
    bit5 = 0
    for bit, u, s5 in zip(b, all_units, sq5_all):
        if bit:
            v = ring.multiply(v, u)
            bit5 ^= s5
    low16 = get_low16(v)
    full_code = low16 | (bit5 << 16)
    matrix_rows.append(full_code)

# 17th candidate: h(s)
# h(s) has bit at 5 equal to 0 (passes at 5, see U78 / U79)
h_poly = sum((-1)**j * x**(16-j) for j in range(17))
h_vec = poly_to_ring_vec(h_poly)
h_low16 = get_low16(h_vec)
h_full_code = h_low16 | (0 << 16)
matrix_rows.append(h_full_code)

rank_17 = binary_rank(matrix_rows)
print("=" * 60)
print(f"Total global candidates: {len(matrix_rows)}")
print(f"Restriction target dimension: 17 (16 dyadic bits + 1 bit at 5)")
print(f"Rank of 17-column restriction matrix Psi: {rank_17}")
print(f"Selmer 2-rank: 17 - rank(Psi) = {17 - rank_17}")
print("=" * 60)
