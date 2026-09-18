"""Independent cross-check of the U123 exponent-order theorems on the full solution model
A^x+B^y=C^z with A,B,C in [1,60], x,y,z in [1,12] (exponent 2 and 1 ALLOWED here on purpose:
the proofs use only positivity, so the statements must hold on the wider model too)."""
sols=[]
P={}
for n in range(1,61):
    for k in range(1,13): P[(n,k)]=n**k
inv={}
for (n,k),v in P.items(): inv.setdefault(v,[]).append((n,k))
for (A,x),va in P.items():
    for (B,y),vb in P.items():
        for (C,z) in inv.get(va+vb,[]):
            sols.append((A,B,C,x,y,z))
print("solutions in model:",len(sols))
v1=[s for s in sols if s[0]<s[2] and s[1]<s[2] and not s[5]<=max(s[3],s[4])]
v2=[s for s in sols if s[2]<s[0] and s[2]<s[1] and not max(s[3],s[4])<s[5]]
v3=[s for s in sols if s[2]<=s[1] and not s[4]<s[5]]
print("violations z_le_max_of_C_largest:",len(v1))
print("violations max_lt_z_of_C_smallest:",len(v2))
print("violations y_lt_z_of_C_le_B:",len(v3))
