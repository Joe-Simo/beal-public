# U28: conditional full-Galois descent to Q and level-34 contradiction

Status: verified conditional partial result only. This does not resolve Beal's conjecture and does not yet eliminate the four exponent-5 Hilbert-form obstructions.

## Setting

Retain the notation of U26. Let

    F = Q(w),  w^4 - w^3 - 6w^2 + w + 1 = 0,

with `disc(F)=17^3`, and let `f` be one of the four surviving parallel-weight-2 Hilbert newforms

    r, s, v, w

at level norm `272 = 16*17` over `F`. Let `lambda|5` be the ramified residue-degree-one prime in the relevant coefficient field singled out in U27, and let

    rho_bar_f : G_F -> GL_2(F_5bar)

be the associated semisimple residual representation.

U26 reduced full `Gal(F/Q)`-invariance to the missing paired congruences

    rho_bar_r ~= rho_bar_s,
    rho_bar_v ~= rho_bar_w.

This file proves a useful *conditional elimination*: if one of these residual representations is absolutely irreducible, is fully `Gal(F/Q)`-invariant, and remains ramified at every prime of its Hilbert level, then it cannot exist.

## 1. Exact level support in F

The LMFDB Hilbert-field record for `4.4.4913.1` lists the two primes above 2 with norm 4

    P2a = [4, 2, -1/2*w^3 + 3*w + 5/2],
    P2b = [4, 2, w^3 - w^2 - 6*w],

and the unique prime above 17

    P17 = [17, 17, 1/2*w^3 - w^2 - w + 3/2].

The Atkin-Lehner records of the four forms show exactly these three primes in the level, each to exponent one. Thus the Hilbert level ideal has norm

    4 * 4 * 17 = 272.

This exact ideal data is used instead of naive factorization of the displayed power-basis polynomial modulo 2, because that polynomial has index 2 in the maximal order.

Source:
- https://www.lmfdb.org/api/hmf_fields/?label=4.4.4913.1&_format=json
- https://www.lmfdb.org/api/hmf_hecke/?label=4.4.4913.1-272.1-r&_format=json

## 2. The descent theorem that is actually needed

Billerey--Chen--Dembélé--Dieulefait--Freitas, Proposition 3.2, supplies the relevant template. In their cyclic totally real setting, once an irreducible residual representation is invariant under the full base-field Galois group, they invoke the extension theorem [their ref. 24, Ch. III, Thm. 2.14] to obtain an irreducible representation of `G_Q` whose restriction is the original representation. They then compute the Serre weight and conductor, twist at the ramified rational prime when necessary, and apply Khare--Wintenberger (Serre modularity) to force a classical weight-2 newform.

The crucial points from their proof are:

1. full Galois invariance + irreducibility gives an extension to `G_Q`;
2. because the residual characteristic is unramified in the totally real base field and the Hilbert form has parallel weight 2, the Serre weight is 2;
3. unramified base change preserves the conductor exponent at the rational primes where the number field is unramified;
4. at the ramified rational prime, one may twist the extension by a character factoring through the base-field Galois group to normalize the local Steinberg character;
5. if the resulting representation is Steinberg at every ramified rational prime and unramified elsewhere, its nebentype is trivial;
6. Serre modularity then places it in the corresponding classical newspace.

Primary source:
- Billerey--Chen--Dembélé--Dieulefait--Freitas, *Some extensions of the modular method and Fermat equations of signature (13,13,n)*, Proposition 3.2, https://lmbp.uca.fr/~billerey/Research/revised_version5.pdf

## 3. Conditional Serre invariants in the present field

Assume now:

(A1) `rho_bar_f` is absolutely irreducible;

(A2) `rho_bar_f^sigma ~= rho_bar_f` for every `sigma in Gal(F/Q)`;

(A3) `rho_bar_f` is ramified at all three Hilbert-level primes `P2a`, `P2b`, `P17`.

By (A1)--(A2) and the same extension theorem used in Proposition 3.2, there is an irreducible odd residual representation

    rho : G_Q -> GL_2(F_5bar)

whose restriction to `G_F` is `rho_bar_f`, up to the harmless choice of extension character.

Because 5 is unramified in F and the Hilbert form has parallel weight 2, the Serre weight of `rho` is 2.

At 2, the extension `F/Q` is unramified and the two primes above 2 are Galois conjugate. By (A3), their residual conductor exponent is one. Therefore the rational 2-part of the Serre conductor has exponent one.

At 17, `F/Q` is totally ramified of degree 4. Under (A3), the local representation is Steinberg-type. Twisting `rho`, if necessary, by a character factoring through `Gal(F/Q)` normalizes the local character exactly as in the proof of Proposition 3.2, so the 17-part of the Serre conductor has exponent one.

After this normalization the representation is Steinberg at 2 and 17 and unramified elsewhere away from 5, hence its nebentype is trivial. Consequently

    k(rho) = 2,
    N(rho) = 2*17 = 34,
    epsilon(rho) = 1.

This conclusion is conditional on (A1)--(A3); in particular, it does **not** assert that residual ramification at `P17` has already been proved.

## 4. The classical level-34 space is a singleton

LMFDB records a unique weight-2, level-34, trivial-character newform orbit:

    34.2.a.a,

with coefficient field `Q` and q-expansion beginning

    q + q^2 - 2q^3 + q^4 - 2q^6 - 4q^7 + q^8 + q^9
      + 6q^11 - 2q^12 + 2q^13 + ...

Thus

    a_13(34.2.a.a) = 2,

so modulo 5 the classical trace at 13 is `2`.

Source:
- https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/34/2/a/a/

## 5. Every survivor forces trace 4 modulo lambda at q=13

The exact LMFDB prime ordering over rational 13 consists of four degree-one primes. U26 established the q=13 Hecke blocks and U27 fixed the residue map at `lambda`.

For r and s, the coefficient polynomial is

    e^2 + 2e - 4,

and the ramified prime has `e == -1 (mod lambda)`. Their q=13 blocks consist only of `e` and `-e-2`, hence every q=13 trace reduces to

    -1 == 4 (mod 5).

For v and w, U26/U27 established the same ramified residue map and that the coefficient involution `tau` is trivial modulo lambda. Their q=13 blocks consist of the elements denoted `A`, `e`, and `tau(e)`, with the exact stored expression for A having denominator prime to 5; direct reduction gives

    A == e == tau(e) == -1 == 4 (mod lambda).

Therefore every one of the four survivors satisfies, at each prime Q|13,

    a_Q(f) == 4 (mod lambda).

Since 13 splits completely in F, the extension `rho` has the same Frobenius trace at rational 13. Thus the hypothetical classical modular form attached to `rho` must satisfy

    a_13 == 4 (mod 5).

But the unique possible level-34 form has

    a_13 == 2 (mod 5).

Contradiction.

## 6. Conditional elimination lemma

**Lemma U28.** Let `f` be any of `r,s,v,w`. If its mod-5 residual representation at the distinguished ramified degree-one prime `lambda` is

1. absolutely irreducible,
2. invariant under the full `Gal(F/Q)`, and
3. ramified at `P2a`, `P2b`, and `P17`,

then no such representation exists.

**Proof.** Sections 2--3 extend and normalize it to an odd irreducible representation of `G_Q` with Serre invariants `(N,k,epsilon)=(34,2,1)`. Serre modularity forces the unique classical newform `34.2.a.a`. Section 5 gives trace `4 mod 5` at 13 from the Hilbert survivor, whereas the classical form has trace `2 mod 5`. Contradiction. QED.

## 7. What remains open

U28 is not the missing congruence certificate. It does not prove

    rho_bar_r ~= rho_bar_s,
    rho_bar_v ~= rho_bar_w.

Nor does it yet prove that residual ramification at `P17` (or at every prime over 2) cannot drop.

The strongest immediate consequence is that the modular route has split into two sharply defined obligations:

1. **Full-invariance obligation:** certify the paired residual congruences from U26. A Proposition-6.1-style mod-5 Hecke-module multiplicity-one computation remains the preferred proof.

2. **Conductor obligation:** once full invariance is available, prove residual ramification at the three Hilbert-level primes. If ramification at 17 can drop, the descended representation may instead have conductor dividing `2*17^2=578` with a character of conductor dividing 17 and order dividing 4; those finite classical spaces must then be enumerated and eliminated separately.

The level-34 ramified-everywhere branch is now conditionally closed, but no full Beal case is closed by this checkpoint.