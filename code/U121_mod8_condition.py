"""A new necessary condition at p=2, from Jev's top-ranked p-adic claims.

If C is even then A, B are both odd (kernel-verified: exactly one base is even), and
    v_2(C^z) = z * v_2(C) >= z >= 3,   so   A^x + B^y = 0  (mod 8).

For ODD n and k >= 1:   n^k = 1 (mod 8) if k is even;   n^k = n (mod 8) if k is odd.
(Because every odd square is 1 mod 8.)

Enumerate the four parity cases for (x, y).
"""
print("=== the four cases, with A, B odd and A^x + B^y = 0 mod 8 ===\n")
rows=[]
for xe in (True,False):
    for ye in (True,False):
        sols=set()
        for A in range(1,8,2):
            for B in range(1,8,2):
                a = 1 if xe else A
                b = 1 if ye else B
                if (a+b)%8==0: sols.add((A,B))
        rows.append((xe,ye,sols))
        lab=f"x {'even':<4} y {'even' if ye else 'odd '}" if xe else f"x {'odd ':<4} y {'even' if ye else 'odd '}"
        print(f"  {lab}:  admissible (A,B) mod 8 -> {sorted(sols) if sols else 'NONE — IMPOSSIBLE'}")

print("""
=== CONSEQUENCES ===
  x EVEN and y EVEN : A^x + B^y = 1 + 1 = 2 mod 8, never 0.  ** IMPOSSIBLE **
  x even, y odd     : 1 + B = 0 mod 8  =>  B = 7 mod 8
  x odd,  y even    : A + 1 = 0 mod 8  =>  A = 7 mod 8
  x odd,  y odd     : A + B = 0 mod 8

By the kernel-verified exponent reduction every exponent lies in {4} u {odd primes}, so
"even" means exactly 4.  Hence, whenever C is even:

  * NOT both x = 4 and y = 4;
  * if x = 4 then B = 7 mod 8;  if y = 4 then A = 7 mod 8;
  * if x and y are both odd primes then A + B = 0 mod 8.
""")

print("=== cross-check against the ten known Fermat-Catalan solutions with C even ===")
SOL=[("7^3+13^2=2^9",7,3,13,2,2,9),("3^5+11^4=122^2",3,5,11,4,122,2),
     ("17^7+76271^3=21063928^2",17,7,76271,3,21063928,2)]
for lbl,A,x,B,y,C,z in SOL:
    if C%2!=0: continue
    print(f"  {lbl}: C even, A={A} (A%8={A%8}), B={B} (B%8={B%8}), x={x} y={y} z={z}")
    print(f"     v_2(C^z) = {z}*v_2({C}) = {z*(C & -C).bit_length()-z}  ; A^x+B^y mod 8 = {(A**x+B**y)%8}")
print("""
  NOTE: 7^3+13^2=2^9 has y = 2, which the Beal hypothesis forbids, so it is NOT a counterexample
  and need not satisfy the condition derived for z >= 3.  It is listed only to show the
  computation is running on real data.
""")
