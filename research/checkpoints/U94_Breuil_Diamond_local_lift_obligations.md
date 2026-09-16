# U94: the Breuil--Diamond prescribed-lift theorem is now mapped exactly, but local lift existence is not yet discharged

**Status: source-verified modular-route audit. The weighted equation and Beal's conjecture remain unresolved.**

Research date: 2026-09-16.

## 1. Why this checkpoint exists

U64 left one explicit gap before its level-2000 Hilbert-form comparison can become unconditional: the global prescribed-lift theorem was cited without writing down every local lift, its determinant, and its Weil--Deligne/ordinary type. U93 therefore returned priority to this point.

The primary Breuil--Diamond paper was reopened directly and Theorem 3.2.2 was checked at author-PDF printed pp.36--37. The theorem is an existence theorem for a global weight-two Hilbert modular lift **provided suitable local characteristic-zero lifts already exist at every place in a finite set S**.

## 2. Exact theorem obligations

In the notation of Breuil--Diamond Theorem 3.2.2, one must choose:

- a finite-order-adjusted determinant character `psi` lifting `det(rho)`, with `psi*epsilon^{-1}` finite order;
- a finite set `S` containing the places above `p=17` and every place where the residual representation or `psi` ramifies;
- a subset `T` of the places above 17 specifying potential ordinarity;
- a Weil--Deligne type `[r_v,N_v]` for every `v in S`;
- and, for every `v in S`, an actual characteristic-zero lift `rho_v` satisfying all five local conditions below.

The five conditions in the primary source are:

1. at `v|17`, `rho_v` is potentially semistable with Hodge--Tate weights `(0,1)` for every embedding;
2. at `v|17`, `rho_v` is potentially ordinary exactly when `v in T`;
3. `rho_v` has the prescribed Weil--Deligne type `[r_v,N_v]`;
4. at ordinary `v|17` and at `v not|17` with `N_v !=0`, `rho_v` contains a one-dimensional subrepresentation with the specified residual character and finite-order inertial quotient after dividing by cyclotomic;
5. `det(rho_v)|I_v = psi|I_v`.

Only after these hypotheses are supplied does the theorem produce a global lift with determinant exactly `psi`, the prescribed local types, and Hilbert modular weight `(2,...,2)`.

## 3. What U64 already supplies

The following pieces survive the source re-audit:

- modularity of the corrected negative-twist residual system is inherited from the cited Darmon-program result at U64's stated status;
- the required irreducibility after adjoining the seventeenth roots of unity is supplied by U64's cyclic-restriction argument and the local irreducibility at 2;
- the residual conductor bookkeeping points to exponent 2 at the prime over 2 and exponent 3 at the prime over 5;
- at primes dividing `Z` away from 17 the residual representation is unramified after lowering;
- at 17 the cited source gives residual finite flatness.

These facts determine the intended residual level, but **they do not themselves construct the local characteristic-zero lifts required by Theorem 3.2.2**.

## 4. The remaining modular obligation is narrower than before

The theorem statement makes clear that the unresolved issue is not a vague global modularity question. It is the explicit local deformation problem:

- identify `psi` globally and its inertial restrictions;
- for the prime over 2, exhibit a lift of the required determinant and the retained local type compatible with conductor exponent 2;
- for the prime over 5, exhibit a lift with the irreducible/Eisenstein local type giving conductor exponent 3 and determinant `psi` on inertia;
- at the prime(s) over 17, decide the correct potentially Barsotti--Tate/ordinary component and exhibit a fixed-determinant lift;
- verify that no other residual ramification forces an additional place into `S`.

If those local lifts are constructed, Breuil--Diamond 3.2.2 supplies the global modular lift needed to justify comparison with the level-2000 Hilbert newspace. U64's finite Hecke comparison would still leave the surviving boundary orbit `b` to be treated globally; completing the lift theorem alone is therefore not yet an elimination of the weighted equation.

## 5. Important correction to route expectations

Finite flatness at 17 is only a property of the residual/local deformation situation; it is **not** interchangeable with an explicit characteristic-zero fixed-determinant lift satisfying all five theorem conditions. Likewise, a conductor exponent from the Darmon-program table does not automatically select a Weil--Deligne type or prove determinant compatibility.

Therefore no level-lowering conclusion is upgraded in U94. The gain is that the missing work is now an explicit finite list of local deformation constructions rather than an unspecified theorem-application gap.

## 6. Next mathematical step

The next checkpoint should attack the prime over 5 first. U64 already proves the Frey quintic is Eisenstein there uniformly and the twist `-1` is locally a square. This gives the most concrete local representation among the three difficult places. The objective is to determine its inertial Weil--Deligne type and construct (or cite with hypotheses checked) a characteristic-zero lift with the required determinant. Only a source-backed construction will be counted.

No contradiction, counterexample, weighted-equation impossibility theorem, or complete Beal solution is claimed.
