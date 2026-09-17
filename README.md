# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Current audited status — U113–U118 (2026-09-17)

The strongest active weighted branch remains

`X^10 + 256Y^10 = Z^17`.

Earlier checkpoints U97–U105 contained several claims that were stronger than their evidence. U113–U118 preserve the corrections below and **supersede any older statement that the weighted equation or orbit b has been eliminated**.

### 1. U113 — universal transvection/Cartan argument refuted
[U113](research/checkpoints/U113_exploration_population_and_transvection_audit.md) checks the Tate-curve hypothesis omitted by U110–U111. At the natural solution-variable primes, the displayed discriminant valuation is divisible by the representation prime, so multiplicative reduction alone does not provide the asserted order-p transvection. The universal Cartan-elimination/surjectivity claim is therefore invalid.

### 2. U114 — genus-8 Chabauty closure refuted
[U114](research/checkpoints/U114_u105_geometric_closure_audit.md) finds two independent gaps:
- a dimension bound on the Chabauty annihilator was incorrectly turned into a claim that six prescribed canonical differentials annihilate the Mordell–Weil group;
- the Diophantine construction produces higher-degree Galois-orbit/divisor data, not a k-rational point, so classifying `C^-(k)` does not classify the relevant symmetric-power points.

The genus-8 curve computations remain possible ingredients, but the recorded geometric pathway is not a proof of the weighted equation.

### 3. U115–U116 — modular pathway repaired only through level lowering
[U115](research/checkpoints/U115_u105_modular_pathway_audit.md) removes a mixed genus-8/genus-2 dependency, an impossible `V_4`/order-5 projective-image combination, and an inapplicable Allen–Khare–Thorne citation.

[U116](research/checkpoints/U116_repaired_breuil_diamond_bridge.md) reconstructs a coherent **partial** modular path for the correct genus-2 negative Frey Jacobian:
- Azon's negative compatible-system theorem supplies modularity;
- direct local analysis at 2 supplies conductor exponent 2 and residual irreducibility;
- a Clifford-theory argument supplies irreducibility after adjoining `zeta_17`;
- Breuil–Diamond Theorem 3.2.2 can be applied using actual geometric local lifts, without the old deformation-ring uniqueness claims;
- the resulting fixed target level is `p_2^2 p_5^3`, norm 2000.

This is a level-lowering bridge, **not** a solution.

### 4. U117 — fresh level-2000 inventory: 7/8 eliminated, orbit b survives
[U117](research/checkpoints/U117_level2000_inventory_and_cm_obstruction_audit.md) re-queries the live LMFDB inventory and verifies exactly eight target newform orbits.

Current LMFDB CM classification:
- non-CM: `a,c,f,g,h`;
- CM: `b,d,e`.

Thus the older statement “seven non-CM forms plus a unique CM form b” is false.

The exact prime-11 Frey trace sieve eliminates
`a,c,d,e,f,g,h`.
Only orbit `b` survives.

The later U97/U102 “definitive elimination” of b is **not established**:
- residual mod-17 congruence was incorrectly upgraded to characteristic-zero isomorphism;
- characteristic-zero ramification was compared across a level-lowering step where residual ramification can disappear;
- finite forcing-prime checks were extrapolated without proof;
- the claimed `10^434` Baker bound was misattributed and not verified;
- the classical `X_0(17)` argument was not translated to the actual RM abelian-surface moduli problem.

### 5. U118 — uniform auxiliary-prime forcing refuted at q=211
[U118](research/checkpoints/U118_cartan_character_and_q211_counterexample.md) tests the proposed global escape

> orbit-b congruence forces `V=0 mod q` for every good `q == 1 mod 5`.

It is false.

At `q=211`, the admissible non-boundary residues
`X=1, Y=31, Z=4` give
`U=1, V=23 != 0`
and satisfy the local weighted equation. Direct exact point counts give the same Frobenius data as the boundary curve:
`#C(F_211)=193`,
`#C(F_211^2)=44983`,
`(S,P)=(19,-11)`.
A separate Wolfram computation reproduced the result.

The exact checker is [`code/U118_q211_orbit_b_counterexample.py`](code/U118_q211_orbit_b_counterexample.py).

Therefore no proof may extrapolate the successful q=11,31,41 boundary sieve to all split primes.

## Active exploration population

The persistent exploration tree is stored in
[`research/exploration/population.json`](research/exploration/population.json).

It records:
- parent/inspiration links;
- exact objectives;
- evidence and unresolved obligations;
- evaluator outcomes;
- failure mechanisms;
- novelty;
- status;
- bounded routing scores.

**Jev/Typesafe is not callable in the current research runtime.** No mathematical result is attributed to Jev. The routing fields are transparent research-management metadata only, not probabilities and not proof evidence.

The current highest-leverage restart is to eliminate surviving orbit b by a genuinely global mechanism: an RM 17-isogeny/Cartan-locus argument, a second compatible Frey system, or a Gaussian-descent invariant that is incompatible with the boundary CM specialization. Additional isolated prime sieves are deprioritized.

## Preserved earlier partial results

- [U92](research/checkpoints/U92_forcing_prime_sieve_exhausted.md): the specific Gaussian forcing-prime criterion has exactly fourteen forcing primes; blindly extending that search cannot create more.
- [U85](research/checkpoints/U85_ratio_collision_invariant.md)–[U86](research/checkpoints/U86_symmetric_X_support.md): all-prime ratio-collision/support invariants provide lower-bound and divisibility information but no contradiction.
- The Section 8 exact counterexample checker remains useful for validating explicit six-integer candidates; passing checker tests does not prove Beal.

## Global coverage

The coefficient-256 weighted orientation is unresolved. The larger mixed-signature portion of Beal is unresolved. No bounded computation, density statement, partial modular elimination, Chabauty rank bound, or AI/model agreement is counted as a solution.

Historical files are retained for provenance; downstream claims must use the U113–U118 corrected status when they conflict with older checkpoints.

## Original target

For positive integers `A,B,C,x,y,z` satisfying

`A^x + B^y = C^z`

with `x,y,z >= 3`, prove

`gcd(A,B,C) > 1`

or produce an independently verified counterexample. All bases and exponents remain unbounded.
