import itertools, json, sys
sys.path.insert(0,'[LOCAL_HOME]/Downloads/beal/code'); import jev
TARGETS=["(3,5,7) all arrangements","(4,5,7) all arrangements","(4,q,r), q != r odd primes, general","(p,q,r) distinct odd primes, general"]
VOCAB=["Eisenstein-integer factorisation of the cubic term A^3 = C^r - B^q (needs a sum/difference of cubes: not available) — check applicability",
 "treat the exponent-4 term as a norm from Z[i]: A^4 = N(A^2) and factor C^r - B^q over Z[i]? (needs a sum of two squares) — check applicability",
 "Runge's method or Thue-type finiteness with PARI thue() after fixing one base to a small value (a named-hypothesis bounded search: 'no solution with min base <= 50')",
 "p-adic / LTE constraints on v_p(C^r - B^q) when p | (C - B) and q = r fails; find a forced prime-power structure",
 "solve the S-unit-like specialisation: fix A in {2,3,5,6,7,10} and use known results on Pillai/Catalan-type equations a^x - b^y = c (Mihailescu, Bennett) — named hypothesis: no counterexample with a base <= 10",
 "parity/2-adic structure beyond mod 8 for the specific signature (exponent 4 term is 0 or 1 mod 16)",
 "reduce (4,q,r) to x^2 + y^q = z^r with x a square and use the (2,q,r) literature row by row (which (2,q,r) are solved?)",
 "descent on the Frey-Hellegouarch curve of the (2,q,r)-type equation over Q when one exponent is 2 after writing A^4=(A^2)^2"]
CTX="Beal open core after U172. PARI/GP (ellrank, thue, mf over Q), Lean4, Python. Dead: local sieves, FC-blind conditions, Chabauty/Hilbert/Q-curve methods unavailable."
Q={"applicable":jev.noul("Is this mechanism actually APPLICABLE to this target (the algebraic structure it needs is present)?",true="applicable",false="structure absent"),
   "decides":jev.score("If run, what could it decide?",["nothing","a bounded named-hypothesis statement only","one signature or one fixed-base family","an infinite family in the open core"])}
cells=list(itertools.product(TARGETS,VOCAB))
rs=jev.ask_many([{"context":CTX,"target":t,"mechanism":m} for t,m in cells],Q,concurrency=12)
rows=sorted(((round(r["answers"]["applicable"]["noul"]*r["answers"]["decides"]["score"],2),t[:24],m[:100]) for (t,m),r in zip(cells,rs) if "error" not in r),reverse=True)
json.dump(rows,open("[LOCAL_HOME]/Downloads/beal/research/pool/evidence/vocab2_sweep_U173.json","w"),indent=1)
for r in rows[:8]: print(r)
