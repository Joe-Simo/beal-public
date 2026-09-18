"""M5: which REDUCED Beal signatures are still open?

By the kernel-verified exponent reduction, every exponent may be taken in {4} u {odd primes}.
Mark each small reduced signature (x,y,z) with min >= 3 by what closes it.

Sources, all recorded in this project:
  FLT           (n,n,n) for all n >= 3                      Wiles-Taylor            [U114]
  ours-3        3|x, 3|y, 3|z                               mathlib FLT3            [kernel-verified]
  ours-4        4|x, 4|y, z even                            mathlib not_fermat_42   [kernel-verified]
  (p,p,3)       p >= 3                                      Darmon-Merel, Poonen    [U114]
  (3,3,p)       p <= 10^7                                   Kraus; Chen-Siksek      [U114 IV]
  (5,5,p)       p = 7, 19 unconditional; 11, 13 under GRH   Dahmen-Siksek           [U114 VI]
  (3,4,5)                                                   Siksek-Stoll            [external survey]
  (3,3,4)                                                   resolved                [Darmon survey]
Note x,y are interchangeable; z is not.
"""
from sympy import isprime

REDUCED = [3,4,5,7,11,13,17,19,23]

def status(x,y,z):
    if x==y==z: return "FLT (Wiles-Taylor)"
    if x%3==0 and y%3==0 and z%3==0: return "ours: 3|x,y,z (kernel-verified)"
    if x%4==0 and y%4==0 and z%2==0: return "ours: 4|x,4|y,z even (kernel-verified)"
    if x==y and z==3: return "(p,p,3) Darmon-Merel/Poonen"
    if y==z and x==3: return "(p,p,3) Darmon-Merel/Poonen"
    if {x,y}=={3} and isprime(z) and z<=10**7: return "(3,3,p), p<=1e7 Kraus/Chen-Siksek"
    if {x,y}=={3} and z==4: return "(3,3,4) resolved"
    if {x,y}=={5} and z in (7,19): return "(5,5,p) Dahmen-Siksek, unconditional"
    if {x,y}=={5} and z in (11,13): return "(5,5,p) Dahmen-Siksek, UNDER GRH"
    if sorted((x,y,z))==[3,4,5]: return "(3,4,5) Siksek-Stoll"
    return None

rows=[]
for x in REDUCED:
    for y in REDUCED:
        if y<x: continue                      # x,y interchangeable
        for z in REDUCED:
            s=status(x,y,z)
            rows.append(((x,y,z), s))

closed=[r for r in rows if r[1]]
opn   =[r for r in rows if not r[1]]
print(f"reduced signatures enumerated (x<=y, exponents in {REDUCED}): {len(rows)}")
print(f"  closed by a recorded result : {len(closed)}")
print(f"  OPEN                        : {len(opn)}\n")
print("SMALLEST OPEN SIGNATURES (by exponent sum):")
opn.sort(key=lambda r: (sum(r[0]), r[0]))
for sig,_ in opn[:20]:
    print(f"   {sig}   sum={sum(sig)}")
print("\nclosed, for contrast (first 12):")
for sig,s in closed[:12]:
    print(f"   {str(sig):<12} {s}")
