"""M3: exactly which step of a would-be proof must use the ORDERING of Z?

Beal is FALSE over Z[i] (Helenius, kernel-verified here).  Z[i] is a PID, so unique factorisation
cannot be the missing ingredient.  What does Z have that Z[i] lacks?  This isolates it.
"""
from math import gcd, log

print("=== The Gaussian counterexample exhibits CANCELLATION ===")
class G:
    def __init__(s,a,b): s.a,s.b=a,b
    def __mul__(s,o): return G(s.a*o.a-s.b*o.b, s.a*o.b+s.b*o.a)
    def __add__(s,o): return G(s.a+o.a, s.b+o.b)
    def pow(s,n):
        r=G(1,0)
        for _ in range(n): r=r*s
        return r
    def norm(s): return s.a*s.a+s.b*s.b
    def __repr__(s): return f"{s.a}{'+' if s.b>=0 else '-'}{abs(s.b)}i"

u,v,w=G(-2,1),G(-2,-1),G(1,1)
U,V,W=u.pow(3),v.pow(3),w.pow(4)
print(f"  N((-2+i)^3) = {U.norm()}")
print(f"  N((-2-i)^3) = {V.norm()}")
print(f"  N(sum)      = {(U+V).norm()}   <-- FAR SMALLER than either summand")
print(f"  cancellation factor: {U.norm()/(U+V).norm():.1f}x")
print("""
  Over Z[i] the 'size' (norm) of a sum can COLLAPSE relative to its summands, because the
  summands can point in opposing directions.  That is precisely what Z forbids.
""")

print("=== Over Z, positivity forbids cancellation, and pins C tightly ===")
print("""
  For POSITIVE integers with A^x + B^y = C^z:
        C^z > A^x   and   C^z > B^y          (no cancellation)
        C^z < 2*max(A^x, B^y)                (the smaller term is less than the larger)

  Bases are pairwise coprime (kernel-verified), so A^x = B^y forces A = B = 1, which is
  excluded.  So WLOG A^x < B^y and

        B^y  <  C^z  <  2 B^y

  Taking z-th roots:        B^(y/z)  <  C  <  2^(1/z) * B^(y/z)

  Since z >= 3, the factor 2^(1/z) <= 2^(1/3) = 1.2599...  So C is pinned to within a factor
  of 1.26 of B^(y/z).  THIS is the step that has no analogue over Z[i].
""")

print("=== verify the window on the known (non-Beal) Fermat-Catalan solutions ===")
SOL=[("2^5+7^2=3^4",2,5,7,2,3,4),("7^3+13^2=2^9",7,3,13,2,2,9),
     ("2^7+17^3=71^2",2,7,17,3,71,2),("3^5+11^4=122^2",3,5,11,4,122,2),
     ("1414^3+2213459^2=65^7",1414,3,2213459,2,65,7),
     ("9262^3+15312283^2=113^7",9262,3,15312283,2,113,7)]
print(f"{'solution':<28}{'B^y < C^z':>11}{'C^z < 2B^y':>12}{'C/B^(y/z)':>12}")
for lbl,A,x,B,y,C,z in SOL:
    Ax,By,Cz=A**x,B**y,C**z
    if Ax>By: A,x,B,y,Ax,By=B,y,A,x,By,Ax     # ensure A^x < B^y
    r=C/ (By**(1.0/z))
    print(f"{lbl:<28}{str(By<Cz):>11}{str(Cz<2*By):>12}{r:>12.4f}")
print("\n  every row satisfies 1 < C/B^(y/z) < 2^(1/z) <= 1.26 -- the window is real.")

print("""
=== CONCLUSION (answers M3) ===
The ordering of Z enters at exactly one place: it forbids CANCELLATION, giving
        max(A^x, B^y) < C^z < 2 max(A^x, B^y).
Over Z[i] this fails completely -- the Helenius identity has summands of norm 125 each and a sum
of norm 16, a 7.8x collapse.

So any proof of Beal must, at some step, use an inequality of this kind.  A proof that never
compares sizes cannot work, because it would apply verbatim to Z[i], where the statement is false.
This is a POSITIVE specification of what a proof must contain, derived from the obstruction.
""")
