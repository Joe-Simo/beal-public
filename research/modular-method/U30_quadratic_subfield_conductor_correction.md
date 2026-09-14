# U30: quadratic-subfield conductor correction and extended finite elimination

Status: verified conditional partial result only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Purpose

This checkpoint corrects and strengthens U29. The quadratic-subfield route uses

    F/Q cyclic quartic of conductor 17,
    K = Q(sqrt(17)) ⊂ F,

and a mod-5 residual representation over `G_F` attached to one of the four surviving Hilbert newforms `r,s,v,w`. The certified `sigma^2` relation gives invariance under `Gal(F/K)`. Under absolute irreducibility, Clifford theory gives a projective extension to `G_K` and, after choosing a linear extension over an algebraic closure, a 2-dimensional residual representation over `K`.

U29 only enumerated candidate Hilbert levels over `K` whose norms divide 68. That was too optimistic at the ramified prime above 17.

## 1. Correct local Artin-conductor bound over K

Let `P17` be the unique prime of `K` above 17. The extension `F/K` is quadratic and tamely ramified at `P17` because 17 is the only ramified rational prime in the conductor-17 tower and the local ramification degree is 2.

The restriction to `G_F` comes from a weight-2 Hilbert newform whose l-adic conductor exponent at the prime above 17 is one. Therefore its mod-5 restriction has Swan conductor zero and Artin conductor exponent at most one.

Because `F/K` is tame at 17, the wild inertia subgroup is unchanged. Hence any extension to `G_K` still has Swan conductor zero at `P17`. For a 2-dimensional representation,

    a(P17) = codim(V^{I_P17}) + Swan(V) <= 2.

Thus the K-level may contain `P17^2`; exponent one is not automatic.

At the two primes of `K` above 2, the extension `F/K` is unramified. Inertia is unchanged by unramified base extension, so the residual conductor exponent at each prime above 2 is at most one.

Consequently the Artin conductor of any such `G_K` extension outside 5 divides

    P2a * P2b * P17^2,

whose norm is

    2 * 2 * 17^2 = 1156.

The complete list of possible level norms is therefore

    1, 2, 4, 17, 34, 68, 289, 578, 1156.

This corrects the level list in U29.

## 2. Existing levels through 68

U29 already eliminated every recorded parallel-weight-2 Hilbert newform over `K` at level norms

    1, 2, 4, 17, 34, 68

using the forced residual traces

    a_q == 4 (mod 5)

at both primes `q|13` of `K`.

The present file checks the three previously omitted norms 289, 578, and 1156.

## 3. Level norm 1156

The current LMFDB query for

    field_label = 2.2.17.1,
    level_norm = 1156

returns no weight-2 Hilbert newform records.

Thus there is nothing to eliminate at norm 1156.

## 4. Level norm 289

LMFDB records seven weight-2 newforms at the unique level ideal of norm `289=17^2`:

    289.1-a, 289.1-b, 289.1-c,
    289.1-g, 289.1-h, 289.1-i, 289.1-j.

The two norm-13 Hecke eigenvalues are as follows.

### 289.1-a

Coefficient field Q, pair

    (-2,-2),

so the residues are `(3,3)`, not `(4,4)`.

### 289.1-b

Hecke polynomial

    x^2 - 2x - 1,

with pair

    (2e-22, 2e+10).

If the first trace were 4 modulo a prime over 5 then `e=3` in the residue field, but `3` is not a root of `x^2-2x-1` modulo 5. Hence no prime over 5 gives the required pair.

### 289.1-c

Hecke polynomial

    x^2 - x - 3,

with pair

    (-e-1,-e-1).

Equality to 4 would force `e=0`, but the polynomial is nonzero at 0 modulo 5.

### 289.1-g

Hecke polynomial

    x^2 + x - 3,

with pair

    (e-2,e-1).

The two entries differ by 1, so they cannot both equal 4 modulo 5.

### 289.1-h

Hecke polynomial

    x^2 + 2x - 1,

with pair

    (-e-1,-e-1).

Equality to 4 would force `e=0`, which is not a root modulo 5.

### 289.1-i and 289.1-j

Their Hecke data are

    i: P_i=x^3-3x-1,
       a13=-2e^2+3e+6 at both q|13;

    j: P_j=x^3-3x+1,
       a13=-2e^2-3e+6 at both q|13.

Exact Wolfram computations gave

    gcd(P_i, (-2x^2+3x+6)-4) = 1 mod 5,
    gcd(P_j, (-2x^2-3x+6)-4) = 1 mod 5.

Therefore no coefficient-field prime over 5 can make the norm-13 traces equal 4.

Hence every level-289 form is eliminated.

## 5. Level norm 578

There are two conjugate level ideals of norm `578=2*17^2`, labelled `578.1` and `578.2`. Each carries fourteen newform constituents with dimensions

    1,1,1,1,1,2,2,2,3,3,6,6,8,8.

The nontrivial automorphism of `K/Q`, written `w -> 1-w` in the LMFDB basis, sends the level generator of `578.1`

    -17w + 34

to

    17w + 17,

which is the level generator of `578.2`. Thus base-field conjugation gives a bijection between the two level spaces and swaps the two primes above 13. Since the required trace condition `(4,4)` is symmetric in those two primes, it is enough to eliminate all fourteen forms at `578.1`.

The norm-13 pairs for `578.1-a` through `578.1-i` already give immediate contradictions:

    a: (-4,0)
    b: (-4,0)
    c: (2,0)
    d: (-1,0)
    e: (-4,-1)
    f: (-3e+1,-3e-2)
    g: (-3e-1,-2)
    h: (-3e+1,-3e-2)
    i: (-2,-e^2-e+5)

For `a-e`, at least one rational entry is not 4 modulo 5. For `f,h` the two entries differ by 3 modulo 5, so they cannot both equal 4. For `g,i`, one entry is `-2 == 3 mod 5`.

For the remaining five forms, exact polynomial gcd tests were performed modulo 5. Let `P` be the displayed Hecke polynomial and `A,B` the two norm-13 eigenvalue polynomials. Wolfram returned

    gcd(P,A-4,B-4) = 1

for each of `j,k,l,m,n`.

The data used were:

    j:
      P=x^3-x^2-7x+6,
      A=-x^2+x+7,
      B=x^2+3x-6;

    k:
      P=x^6-6x^4+x^3+6x^2-1,
      A=2x^5-2x^4-12x^3+14x^2+10x-6,
      B=-3x^5+x^4+16x^3-10x^2-6x+4;

    l:
      P=x^6-6x^4-x^3+6x^2-1,
      A=2x^5-10x^3-2x^2+4x-2,
      B=2x^5+2x^4-10x^3-14x^2+7;

    m:
      P=x^8-4x^7-6x^6+36x^5-x^4-96x^3+44x^2+64x-34,
      A=(-3x^7+7x^6+25x^5-53x^4-62x^3+110x^2+42x-50)/4,
      B=(x^7+x^6-19x^5+5x^4+74x^3-42x^2-54x+30)/4;

    n:
      P=x^8+4x^7-6x^6-36x^5-x^4+96x^3+44x^2-64x-34,
      A=(3x^7+7x^6-25x^5-53x^4+62x^3+110x^2-42x-50)/4,
      B=(-x^7+x^6+19x^5+5x^4-74x^3-42x^2+54x+30)/4.

For `m,n` the gcd test was performed after multiplying `A-4` and `B-4` by 4, which is invertible modulo 5.

Thus all fourteen `578.1` forms are excluded, and by conjugation all fourteen `578.2` forms are excluded as well.

## 6. Strengthened finite elimination

Combining U29 with the corrected conductor bound and the new checks above:

> There is no recorded parallel-weight-2 Hilbert newform over `K=Q(sqrt(17))` at any level whose norm is compatible with an Artin conductor dividing `P2a*P2b*P17^2` and whose two norm-13 traces can equal the forced pair `(4,4)` modulo a coefficient-field prime above 5.

Equivalently, every recorded candidate at norms

    1,2,4,17,34,68,289,578,1156

is eliminated.

This finite statement is now robust against the previously omitted possible second power of the prime above 17.

## 7. Projective-to-linear modularity bridge

Assume the `G_K` extension is absolutely irreducible. Its projectivization is a totally odd `PGL_2(F_5)` representation: the residual coefficient prime has residue field `F_5`, and oddness is inherited from the weight-2 representation over the totally real extension `F`.

For `K=Q(sqrt(17))`,

    [K(zeta_5):K] = 4,

since the quadratic subfield of `Q(zeta_5)` is `Q(sqrt(5))`, not `K`.

Allen--Khare--Thorne, *Modularity of PGL2(F_p)-representations over totally real fields*, Theorem 1.2, therefore applies to the projective representation and gives projective automorphy by a regular algebraic weight-0 cuspidal automorphic representation of `GL_2(A_K)`. Weight 0 in their automorphic normalization corresponds to parallel Hilbert weight 2.

If two linear residual representations have the same projectivization, then after conjugacy they differ by a scalar character:

    r_2 = r_1 ⊗ chi.

Here `chi` has finite image in `Fbar_5^*`, hence order prime to 5. Its Teichmuller lift is a finite-order characteristic-zero character. Twisting the automorphic representation by the inverse lifted character therefore produces a regular algebraic automorphic representation whose residual linear representation is the specific desired `G_K` extension. Finite-order twisting does not change the parallel weight.

Thus, under absolute irreducibility, the projective-to-linear modularity and weight-2 portions of the U29 bridge are no longer the main gap.

Primary source checked:

- Patrick B. Allen, Chandrashekhar Khare, Jack A. Thorne, *Modularity of PGL2(F_p)-representations over totally real fields*, PNAS 118 (2021), arXiv:2104.14732, Theorem 1.2.

## 8. Remaining theorem-level gap: level optimization

To invoke the finite elimination, one still needs an automorphic realization at the residual Artin conductor (or at least at a level dividing `P2a*P2b*P17^2`).

Fujiwara, *Level optimization in the totally real case*, Theorem 1.1, gives optimal local conductor equal to the Artin conductor outside `ell` under its stated hypotheses. The source explicitly isolates the Mazur-principle difficulty when a residual representation is unramified at `v` and `Norm(v) == 1 mod ell`; the OCR/extraction of the theorem's condition A-3 is easy to misread because the not-congruent sign is poorly rendered. The paper's surrounding text confirms that this is the exceptional case.

Relevant literature also includes Jarvis and Rajaei on Hilbert level lowering. Their exact applicability to the automorphic lift produced above still has to be checked hypothesis-by-hypothesis. Until that is done, U30 does not claim the `G_K` branch is eliminated.

## Current obligations

1. Complete the level-optimization theorem chain for the specific absolutely irreducible `G_K` representation, including any exceptional primes with norm congruent to 1 modulo 5.
2. Independently, the direct full-Galois route still requires the paired residual congruences `r ~= s (mod lambda)` and `v ~= w (mod lambda)`.
3. If level optimization is certified, combine it with the exhaustive finite elimination in this file to eliminate the entire absolutely irreducible quadratic-subfield extension branch.

No complete Beal case is declared closed by U30.