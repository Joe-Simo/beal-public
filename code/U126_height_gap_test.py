"""Cycle U126 — cheapest discriminating test for the Jev-routed 'height gap' cell.
Named hypothesis H: with A^x dominant and A < C (so z <= x, kernel-verified), the gap between C^z
and the next z-th power below it already exceeds A^x, i.e.  A^x <= (C-1)^z  -- which would give
B^y = C^z - A^x >= C^z - (C-1)^z >= z (C-1)^{z-1}, an effective lower bound on B in terms of C.
If H fails on the exponent>=2 model, the height-gap route needs more than elementary input."""
P={(n,k):n**k for n in range(1,121) for k in range(2,16)}
inv={}
for (n,k),v in P.items(): inv.setdefault(v,[]).append((n,k))
S=[(A,B,C,x,y,z) for (A,x),va in P.items() for (B,y),vb in P.items() for (C,z) in inv.get(va+vb,[]) if A!=B]
dom=[s for s in S if s[1]**s[4] <= s[0]**s[3] and s[0]<s[2]]
print("model solutions:",len(S)," dominant-A with A<C:",len(dom))
bad=[s for s in dom if not (s[0]**s[3] <= (s[2]-1)**s[5])]
print("H violated on",len(bad),"of",len(dom))
for s in bad[:6]: print("  ",s, "ratio A^x/(C-1)^z =",s[0]**s[3],"/",(s[2]-1)**s[5])
# does z<=x hold on all of them (sanity: theorem must hold on the model)
print("z<=x violations (must be 0):",sum(1 for s in dom if s[5]>s[3]))
