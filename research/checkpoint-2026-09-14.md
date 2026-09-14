# Beal research checkpoint — 2026-09-14

## Status

No complete proof or counterexample. This checkpoint concerns only the primitive even-leg exponent-5 generalized-Fermat subcase arising from the Beal program; closing it would not resolve Beal by itself.

## Exact target subproblem

Michaud-Jacobs (Mathematika 68 (2022), 344–361, DOI 10.1112/mtk.12127) proves that primitive nonzero solutions of

x^(2l) + y^(2m) = z^17

are impossible for primes l,m != 5. His remaining l=5 obstruction includes four Case-2 Hilbert newforms over the cyclic quartic field F of conductor 17, LMFDB base-field label 4.4.4913.1, level 272.1. The paper explicitly says the author expects their residual representations at primes lambda|5 to be reducible; proving this would eliminate them because the Frey residual representation is irreducible for l>=5 (Lemma 7.2).

Relevant public code:
- https://github.com/michaud-jacobs/thesis/blob/main/gen-fermat/cuspforms_17.m
- https://github.com/michaud-jacobs/thesis/blob/main/gen-fermat/irreducibility_17.m

## Four obstructing Case-2 forms

LMFDB labels:
- 4.4.4913.1-272.1-r, coefficient degree 2
- 4.4.4913.1-272.1-s, coefficient degree 2
- 4.4.4913.1-272.1-v, coefficient degree 6
- 4.4.4913.1-272.1-w, coefficient degree 6

For r,s the Hecke coefficient polynomial is

P2(X) = X^2 + 2X - 4.

For v,w it is

P6(X) = X^6 + 3X^5 - 42X^4 - 104X^3 + 364X^2 + 428X + 104.

## Degree-6 coefficient-field involution and the prime over 5

Let e be a root of P6. Exact computation found the nontrivial field automorphism

tau(e) = e^5/4 - e^4/4 - 17e^3/2 + 5e^2 + 41e + 17.

Independent Wolfram Language checks returned:

- P6 mod 5 = (X+1)^2 (X^4 + X^3 - 1)
- remainder P6(tau(X)) modulo P6(X) = 0
- remainder tau(tau(X)) - X modulo P6(X) = 0
- tau(-1) mod 5 = 4 = -1 mod 5
- disc(P6) = 2^20 * 5^3 * 13 * 449^2

Wolfram also computed the maximal-field discriminant as

Disc(K6) = 3354640640 = 2^8 * 5 * 13 * 449^2,

so [O_K6 : Z[e]] = 320 = 2^6*5. Because the power basis has 5-index, the naive factorization of P6 mod 5 alone is not a valid Dedekind factorization.

To repair this, an integral generator beta from a computed integral basis was found with index prime to 5. Its minimal polynomial is

X^6 - 394X^5 + 9946X^4 + 133088X^3 + 296618X^2 - 355700X + 87440,

and its polynomial discriminant divided by Disc(K6) has 5-adic valuation 0. Modulo 5 this minimal polynomial factors as

X^2 (X^4 + X^3 + 3X^2 + 3X + 3).

The quartic factor is irreducible over F5. Hence 5 has exactly one ramified residue-degree-1 prime lambda in K6, with e(lambda/5)=2, plus one unramified residue-degree-4 prime. Since P6 has only the linear residue root e=-1 modulo 5, the ramified lambda satisfies e == -1 (mod lambda). It is unique of this ramification/residue type, so tau fixes lambda; the induced map on O_K6/lambda = F5 is the identity.

This is precisely the coefficient-field ramification feature used in Billerey–Chen–Dembélé–Dieulefait–Freitas, Proposition 3.2, for a reducibility argument.

## Quartic base-field involution

The cyclic quartic base field F has defining polynomial

f(W) = W^4 - W^3 - 6W^2 + W + 1

(discriminant 17^3). A generator sigma of Gal(F/Q) can be represented by

sigma(W) = -W^3/2 + 3W + 3/2,

with order 4; sigma^2(W) = W^3 - W^2 - 6W + 1.

Using the ordered LMFDB prime ideals above q=13 and q=47, sigma^2 swaps the first two primes and swaps the last two primes in each split block.

For the degree-2 forms r,s, the coefficient involution is e |-> -e-2. For sampled q=13 and q=47 Hecke blocks, each of r and s separately satisfies the exact characteristic-zero relation expected from

f^(sigma^2) = f^tau.

For the degree-6 forms v,w, the tau above likewise sends the q=13 and q=47 Hecke blocks back to themselves after the sigma^2 prime permutation. Exact algebra verifies the required coefficient swaps (for example tau exchanges the relevant q=47 coefficients C<->D and E<->F).

This is strong structural evidence that all four characteristic-zero newforms satisfy f^(sigma^2)=f^tau. It is not yet promoted to a theorem because a finite sample of Hecke coefficients is not by itself a proof of equality of eigenforms; a Sturm/Hecke-algebra certificate or the original Magma space computation is still needed.

If the identity is certified, reduction modulo the ramified lambda|5 makes tau act trivially and gives residual invariance under Gal(F/Q(sqrt(17))). Under an irreducibility assumption, the Billerey-style descent mechanism would then extend the residual representation at least to G_{Q(sqrt(17))}.

## Reference method

Billerey, Chen, Dembélé, Dieulefait, Freitas, “Some extensions of the modular method and Fermat equations of signature (13,13,n)”, Publ. Mat. 67 (2023), arXiv:1802.04330, Proposition 3.2:
- identify a base-field Galois action intertwined with a coefficient-field automorphism;
- use total ramification of the residual prime so that the coefficient automorphism is trivial on the residue field;
- deduce Galois invariance of an assumed irreducible residual representation;
- descend/extend the representation;
- determine its Serre invariants and contradict the finite list of classical modular forms.

Michaud-Jacobs explicitly points to an extension of this method as a likely route for the four l=5 obstructions.

## Current open obligations

1. Certify f^(sigma^2)=f^tau for each of r,s,v,w, not merely at sampled Hecke primes.
2. Determine whether the residual forms are invariant under the full cyclic quartic Gal(F/Q), not just the order-2 subgroup. Full invariance would permit descent directly to Q and make Serre modularity/classical newform elimination available.
3. If only order-2 invariance is available, determine a rigorous descent/elimination over Q(sqrt(17)).
4. Audit which prime lambda|5 is the actual surviving congruence prime for the degree-6 forms; the ramified degree-1 lambda is the expected one, but this must be tied to the original sieve ideal.
5. Only after these are closed can this generalized-Fermat subcase be declared eliminated; Beal would still have other uncovered exponent patterns.
