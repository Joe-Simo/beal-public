"""U214 — Jev screen of CONCRETE descent maps on coprime solutions of A^x+B^y=C^z (top cluster of U213).
Each map is then tested exactly on the Fermat-Catalan set (does it send a known solution to another solution?)."""
import json, sys
sys.path.insert(0,'[LOCAL_HOME]/Downloads/beal/code'); import jev
MAPS={"vieta":"Vieta jumping: fix B^y and exponents, view A^x+B^y=C^z as a relation in (A,C) and jump to a second root",
"norm_split":"factor C^z-B^y over Z[zeta] when gcd(y,z)=d>1 and descend to the factor equation with exponents (x,y/d,z/d)",
"frey_isogeny":"pass to the 2-isogenous Frey curve: (a,b,c)->(( a-b)^2, 4ab, (a+b)^2) i.e. c^2=(a-b)^2+4ab, and ask whether perfect-power shape persists",
"abc_square":"the map (a,b,c)->(a^2, 2ab+b^2, c^2) or (a^2,b^2,c^2-2ab) keeping two terms perfect powers",
"belyi_pull":"pull back along a Belyi map of degree n preserving {0,1,inf}: (a:b:c)->(a^n : c^n-a^n : c^n) style, keeping power structure on two terms",
"exponent_gcd":"if p | x, replace A by A^(x/p): reduces to prime/4 exponents (known reduction) then descend via signature-specific parametrisation to a smaller solution of a DIFFERENT signature",
"pss_chain":"the chain 2^7+17^3=71^2 -> 17^7+76271^3=21063928^2 sharing base 17: a map reusing a base with a new exponent",
"infinite_descent_height":"classical infinite descent on height via 2-descent on the Frey curve E: y^2=x(x-a)(x+b), using that E has full 2-torsion"}
CTX="Beal conjecture. Beal is FALSE over Z[i] (Helenius (-2+i)^3+(-2-i)^3=(1+i)^4). Ten coprime solutions with an exponent 2 exist (Fermat-Catalan). A descent map that would prove Beal must be undefined or non-decreasing on those."
Q={"well_defined":jev.noul("Is the map an explicit, well-defined operation on integer solutions?",true="explicit",false="vague"),
 "preserves":jev.noul("Does the image again have ALL THREE terms perfect powers with exponents >=3 (not just two)?",true="preserves all three",false="loses a perfect power"),
 "zi_blocks":jev.noul("Is there a reason the map would break over Z[i] but work over Z?",true="breaks over Z[i]",false="works equally over Z[i]"),
 "known":jev.noul("Is this map already a standard known step in the generalized Fermat literature?",true="standard",false="not standard")}
rs=jev.ask_many([{"context":CTX,"map":v} for v in MAPS.values()],Q,concurrency=8)
out={}
for k,r in zip(MAPS,rs):
    a=r.get("answers",{}); out[k]={q:round(a[q]["noul"],2) for q in a}; print(k,out[k])
json.dump({"status":"HYPOTHESIS_ONLY","maps":MAPS,"answers":out},open("research/pool/evidence/descent_maps_U214.json","w"),indent=1)
