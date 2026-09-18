"""Exact enumeration of the mod-9 model of A^x+B^y=C^z, x,y,z>=3, bases pairwise coprime."""
U = [u for u in range(9) if u % 3]          # units mod 9
CUBES = sorted({(u*u*u) % 9 for u in U})    # cubes among units

def pows(n, m, lo=3, hi=20):
    return sorted({pow(n, k, m) for k in range(lo, hi) if True})

print("units mod 9      :", U)
print("cubes of units   :", CUBES)
print("sums of two cubes:", sorted({(a+b) % 9 for a in CUBES for b in CUBES}))

# Claim 1: 3 | x, 3 | y, 3 does not divide C  ==>  C^z = 2 or 7 mod 9.
bad = []
for A in U:
  for B in U:
    for C in U:
      for x in range(3, 39):
        for y in range(3, 39):
          for z in range(3, 39):
            if x % 3 or y % 3: continue
            if (pow(A,x,9) + pow(B,y,9)) % 9 != pow(C,z,9) % 9: continue
            if pow(C,z,9) not in (2, 7): bad.append((A,B,C,x,y,z))
print("\nclaim C^z in {2,7} mod 9 -- counterexamples in model:", len(bad))

# Claim 2: same hypotheses ==> C is not 1 or 8 mod 9, and 3 does not divide z.
bad2 = [t for t in [] ]
bad3 = []
adm = 0
for A in U:
  for B in U:
    for C in U:
      for x in range(3, 39, 1):
        if x % 3: continue
        for y in range(3, 39):
          if y % 3: continue
          for z in range(3, 39):
            if (pow(A,x,9) + pow(B,y,9)) % 9 != pow(C,z,9): continue
            adm += 1
            if C % 9 in (1, 8): bad3.append(("C is a cube mod 9", A,B,C,x,y,z))
            if z % 3 == 0: bad3.append(("3 | z", A,B,C,x,y,z))
print("admissible (A,B,C,x,y,z) mod-9 tuples with 3|x, 3|y, 3 coprime to ABC:", adm)
print("violations of 'C != 1,8 mod 9' or '3 does not divide z':", len(bad3))

# And the case 3 | ABC: which base can it be?
print("\n--- 3 | one base (pairwise coprime, so exactly one) ---")
for who in "ABC":
  ok = 0
  for a in range(9):
    for b in range(9):
      for c in range(9):
        A = 0 if who=="A" else a; B = 0 if who=="B" else b; C = 0 if who=="C" else c
        if who!="A" and A%3==0: continue
        if who!="B" and B%3==0: continue
        if who!="C" and C%3==0: continue
        for x in (3,4,6,9):
          for y in (3,4,6,9):
            for z in (3,4,6,9):
              if (pow(A,x,9)+pow(B,y,9)) % 9 == pow(C,z,9) % 9: ok += 1
  print(f"  3 | {who}: {ok} admissible mod-9 tuples -> {'possible' if ok else 'IMPOSSIBLE'}")
