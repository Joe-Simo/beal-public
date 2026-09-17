# Checkpoint U117: Fresh Level-2000 Inventory, Seven Exact Eliminations, and the Surviving CM/Cartan Obstruction

**Date:** 2026-09-17
**Status:** PARTIAL_RESULT. The norm-2000 Hilbert newspace has been freshly inventoried and seven of its eight orbits are eliminated at the split prime 11. Orbit b survives the validated local sieve. The later U97/U102 claims eliminating b are not established. The weighted equation and Beal's conjecture remain unresolved.

## 1. Fresh current LMFDB inventory

A live uncached request to the LMFDB hmf_forms API for field 2.2.5.1 and level norm 2000 returned exactly the eight records a,b,c,d,e,f,g,h at level 2000.1, with dimensions 2,2,2,2,2,2,2,4. The returned timestamp was 2026-09-17T22:50:12.369793. A second request at offset 8 returned an empty data array at 2026-09-17T22:50:20.028144.

This verifies the current database inventory of exactly eight orbits. It is still a database-completeness statement rather than an independent Magma or Sage reconstruction.

## 2. Correction: three CM orbits, not one

The current live LMFDB records classify:
- a: non-CM
- b: CM
- c: non-CM
- d: CM
- e: CM
- f: non-CM
- g: non-CM
- h: non-CM

Thus the repeated repository statement “seven non-CM orbits and a unique CM orbit b” is false. The correct current database classification is five non-CM orbits a,c,f,g,h and three CM orbits b,d,e.

This does not rescue d or e, because their prime-11 Hecke data eliminate them independently of CM status. It invalidates arguments and ledgers that depend on b being the unique CM constituent.

## 3. Fresh orbit-h verification

A live uncached hmf_hecke request for 2.2.5.1-2000.1-h returned record id 126931. Its coefficient polynomial is

P(e)=e^4-10e^3-13e^2+190e+241.

At the two norm-11 prime indices the eigenvalues are

a1=(-2e^3+15e^2+18e+120)/91,

a2=(2e^3-15e^2-18e+335)/91.

An independent Wolfram exact polynomial-remainder calculation in Q[e]/(P(e)) returned

a1+a2=5,  a1*a2=5,  (a2-a1)^2=5.

For the negative genus-2 Frey curve, U64's exact square/twice-square enumeration at 11 gives precisely

(S,P) in {(-3,-9),(1,-1),(9,19)}.

Modulo 17 these are (14,8), (1,16), and (9,2), none equal to orbit h's (5,5). Therefore h is eliminated at 11.

## 4. Correct level-2000 local ledger

- a: (-1,-1), 0 compatible Frey pairs, eliminated at 11.
- b: (9,19), 5 compatible Frey pairs, survives.
- c: (-5,-5), 0 compatible Frey pairs, eliminated at 11.
- d: (-1,-1), 0 compatible Frey pairs, eliminated at 11.
- e: (-11,29), 0 compatible Frey pairs, eliminated at 11.
- f: (-5,-5), 0 compatible Frey pairs, eliminated at 11.
- g: (-1,-1), 0 compatible Frey pairs, eliminated at 11.
- h: (5,5), 0 compatible Frey pairs, eliminated at 11.

Thus seven of the eight level-2000 orbits are eliminated by the authenticated prime-11 sieve. The sole survivor is b.

For b, all five matches at 11 lie on the boundary residue V=0. This implies 11 divides Y for a surviving congruence; it does not imply Y=0.

## 5. Why the later “definitive b elimination” is not valid

### 5.1 Residual congruence does not imply characteristic-zero isomorphism

From bar-rho(J-,17) isomorphic to bar-rho(b,17), one cannot conclude that the characteristic-zero 17-adic representations are isomorphic merely because orbit b has multiplicity one in the characteristic-zero newspace.

The step “isolated eigenspace + multiplicity one => localized deformation ring is O => unique characteristic-zero lift” was not proved. Breuil-Diamond Theorem 3.2.2 used in U116 gives existence of a modular lift with prescribed local type, not this asserted global uniqueness. Therefore the downstream Faltings-isogeny and endomorphism-dimension contradiction do not eliminate a residual mod-17 congruence.

### 5.2 Characteristic-zero ramification at q|Z is not a residual contradiction

At q|Z, the original Frey 17-adic representation can have toric monodromy while its residual representation is unramified because the relevant discriminant/Tate valuation is divisible by 17. That is precisely the phenomenon level lowering uses.

Hence comparing characteristic-zero monodromy of the Frey variety with the unramified characteristic-zero representation of the lowered form b does not contradict residual isomorphism.

### 5.3 The infinite-prime extrapolation is unproved

U64 computed finite exact local tests and explicitly warned that boundary-compatible congruence tests cannot by themselves force Y=0. U102 replaced this by a universal assertion for all suitable split primes and then a density conclusion. No proof of that universal local assertion or the required family equidistribution implication is preserved. The finite checks do not establish it.

### 5.4 The claimed Baker bound 10^434 is unsupported and misattributed

U102 attributes a bound max(X,Y)<=10^434 for X^10+256Y^10=Z^17 to “Bugeaud-Gyory 1996.”

The cited 1996 paper is Yann Bugeaud and Kalman Gyory, “Bounds for the solutions of unit equations,” Acta Arithmetica 74 (1996), 67-80, DOI 10.4064/aa-74-1-67-80. Current bibliographic and publisher records identify it as a unit-equation paper. No source was located that derives the repository's numerical 10^434 bound for this weighted equation. The asserted 10^4810 > 10^434 contradiction is therefore not evidence.

### 5.5 The classical X_0(17) step is not an established theorem for this RM surface

U102 argues that reducibility over Q(zeta_5) gives an O_K-linear 17-isogeny of the Frey abelian surface and then invokes rational-point results on the classical elliptic modular curve X_0(17). No verified moduli translation is supplied that turns the exact RM abelian-surface problem, with its polarization and endomorphism structure, into the cited classical elliptic-curve X_0(17) problem. This pillar remains an unsupported theorem application.

## 6. Correct interpretation of the survivor

Orbit b is a genuine Cartan/dihedral-style obstruction. The Frey local representation at 2 has order-5 inertia, and a non-split Cartan normalizer over the residual coefficient field can contain elements of order 5. Thus local order-5 inertia does not by itself exclude b.

This is consistent with U113: the earlier attempted universal transvection exclusion fails at natural solution-variable primes because their discriminant valuations are divisible by the representation prime.

The surviving global question is:

Can the residual genus-2 Frey representation attached to a positive weighted solution be induced from the CM quadratic extension corresponding to b, or otherwise lie in the same Cartan-normalizer class?

## 7. Research-population decisions

C117-01 — PARTIAL_RESULT
Objective: authenticate the norm-2000 newspace and eliminate every constituent the prime-11 Frey sieve actually excludes.
Result: exactly eight current LMFDB orbits; seven eliminated at 11; b survives.

C117-02 — REFUTED
Objective: treat U97/U102 as a definitive elimination of b.
Failure: unsupported deformation uniqueness, characteristic-zero/residual conflation, unproved infinite-prime extrapolation, unsupported 10^434 bound, and an unverified X_0(17) moduli translation.

C117-03 — ACTIVE
Objective: eliminate b directly at the residual-representation level.
Method: assume bar-rho(J-,17) isomorphic to bar-rho(b) and extract consequences of the inducing quadratic character, local decomposition groups at 2 and 5, determinant, and Frobenius traces without upgrading the residual congruence to a characteristic-zero isomorphism.
First discriminator: identify the exact quadratic inducing character of b and test whether the Frey residual representation is forced to have the same character.

## 8. Jev status

No callable Jev/Typesafe decision tool is exposed in this session. No result here is attributed to Jev. The persistent population uses the requested routing schema only as transparent research-management scores, not as proof evidence or probabilities.

## 9. Next exact action

Identify the quadratic inducing character of orbit b from its CM field and compare it with the quadratic character forced by the Frey representation's local decomposition groups at 2 and 5.

If they are incompatible, b is eliminated by a residual argument. If they coincide, preserve that failure and restart toward a genuine Cartan/big-image obstruction rather than reusing the invalid U97/U102 characteristic-zero argument.
