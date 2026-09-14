# U31: Case-2 mod-5 residual reducibility via minimal lifts and the cyclotomic split

Status: verified partial result within the stated computational and literature dependencies. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Scope

This checkpoint concerns the four Case-2 Hilbert newforms over the cyclic quartic field F of conductor 17 that survive Michaud-Jacobs' sieve at ell=5:

- 4.4.4913.1-272.1-r,
- 4.4.4913.1-272.1-s,
- 4.4.4913.1-272.1-v,
- 4.4.4913.1-272.1-w.

Let lambda be the distinguished ramified residue-degree-one prime above 5 fixed in U27, and let rho_bar be the semisimple residual representation of G_F attached to one of these forms. The certified sigma^2-conjugation lemma gives invariance under Gal(F/K), where K=Q(sqrt(17)). Under absolute irreducibility, Clifford theory gives an extension of the projective representation, and a linear extension after enlarging the finite coefficient field if necessary.

U29-U30 already proved the following finite elimination statement over K: no parallel-weight-2 Hilbert newform at any level compatible with a prime-to-5 Artin conductor dividing

    P2a * P2b * P17^2

can have the forced pair of mod-5 traces

    (4,4)

at the two primes of K above 13. The possible level norms are

    1, 2, 4, 17, 34, 68, 289, 578, 1156,

and every LMFDB candidate at those norms was eliminated in U29-U30.

The purpose of U31 is to remove the remaining theorem-level bridge for the absolutely irreducible Case-2 branch.

## 1. Automorphy of any absolutely irreducible G_K extension

Let R_bar : G_K -> GL_2(k) be an absolutely irreducible linear extension whose projectivization restricts to the survivor representation over G_F. Its projectivization is a totally odd projective mod-5 representation over the totally real field K.

Since

    [K(zeta_5):K] = 4,

Allen-Khare-Thorne, Theorem 1.2, applies to the projective representation in either parity case for Delta o Proj(R_bar). Their Lemma 2.1 states that a linear representation is automorphic if and only if its projectivization is automorphic. Therefore R_bar is automorphic in their sense: it is the residual representation of a cuspidal regular algebraic automorphic representation of GL_2(A_K) of weight 0, i.e. parallel Hilbert weight 2.

Primary source:
Patrick B. Allen, Chandrashekhar B. Khare, Jack A. Thorne, "Modularity of PGL2(F_p)-representations over totally real fields", Theorem 1.2 and Lemma 2.1, arXiv:2104.14732 / PNAS 118 (2021).

## 2. Case A: irreducible after restriction to K(zeta_5)

Assume

    R_bar|_{G_{K(zeta_5)}}

is absolutely irreducible.

Snowden's Theorem 1.1.3(1), made explicit in Proposition 7.10.1, gives a finitely ramified weight-two p-adic lift R of R_bar whose prime-to-5 conductor is exactly the prime-to-5 Artin conductor of R_bar.

For p=5 Snowden's auxiliary hypothesis (A2) is automatic here whenever the projective image is PGL_2(F_5), because it requires [K(zeta_5):K]=4, which holds.

Snowden's weight-two convention has Hodge-Tate weights {0,-1}. Passing to the dual R^vee gives weights {0,1}, preserves the prime-to-5 conductor, and has residual representation R_bar^vee. Since automorphy is preserved under contragredients, R_bar^vee is automorphic. Allen-Khare-Thorne Theorem 2.3 therefore applies to R^vee: p>2, the residual restriction to K(zeta_5) remains absolutely irreducible, R^vee is de Rham of Hodge-Tate weights {0,1}, and its residual representation is automorphic. Hence R^vee is automorphic, and so is R.

Thus there exists a parallel-weight-2 Hilbert modular realization of R_bar whose prime-to-5 conductor is exactly the Artin conductor of R_bar.

By U30 that conductor divides P2a*P2b*P17^2. U29-U30 exhaust and eliminate all Hilbert newforms at every compatible level norm using the forced q=13 trace pair (4,4). Contradiction.

Therefore no absolutely irreducible survivor extension can remain irreducible over K(zeta_5).

Primary source for the minimal lift:
Andrew Snowden, "On two dimensional weight two odd representations of totally real fields", Theorem 1.1.3(1) and Proposition 7.10.1, arXiv:0905.4266.

## 3. Case B: reducible after restriction to K(zeta_5)

Assume R_bar is absolutely irreducible over G_K but

    R_bar|_{G_{K(zeta_5)}}

is reducible.

The finite quotient

    Gal(K(zeta_5)/K) ~= C4

has order prime to 5. Clifford theory therefore applies to the finite-image representation. Since R_bar has dimension 2 and is irreducible over G_K, the reducible restriction to the normal subgroup G_{K(zeta_5)} must have an orbit of two distinct one-dimensional constituents. The stabilizer of one constituent has index 2 in G_K.

There is a unique quadratic intermediate field in K(zeta_5)/K, namely

    L = K(sqrt(5)).

Hence R_bar is dihedral/monomial:

    R_bar ~= Ind_{G_L}^{G_K}(chi)

for a character chi of G_L.

For a prime q of K unramified in L/K and inert in L/K, Frobenius lies outside G_L, so the trace of the induced representation is zero:

    tr R_bar(Frob_q) = 0.

Now rational 13 splits in K=Q(sqrt(17)), since 17 == 4 mod 13 is a square. For either prime q|13 of K, the residue field is F_13. The polynomial X^2-5 is irreducible over F_13 because

    (5/13) = -1.

Exact Wolfram verification returned

    JacobiSymbol[5,13] = -1,
    5^6 mod 13 = 12,
    X^2-5 mod 13 is irreducible.

Therefore both primes q|13 are inert in L/K, and the dihedral representation forces

    tr R_bar(Frob_q) = 0

at both q|13.

But the four Case-2 survivor systems all have residual trace

    tr R_bar(Frob_q) = 4 mod 5

at both primes q|13, as proved in U28-U30.

Contradiction.

Therefore the cyclotomic-reducible absolutely irreducible case is also impossible.

## 4. Case-2 reducibility conclusion

Combining Sections 2 and 3:

> For each of the four Case-2 survivor newforms r,s,v,w, the distinguished mod-5 residual representation at lambda cannot be absolutely irreducible.

Equivalently, every one of the four Case-2 residual representations is reducible (at the semisimple level relevant to the modular-method comparison).

This is exactly the type of conclusion Michaud-Jacobs identifies as sufficient to discard these obstructing forms against a Frey representation whose mod-5 representation is irreducible.

## 5. Coverage warning: this does not yet eliminate the entire ell=5 obstruction

The original Michaud-Jacobs paper explicitly notes that removing the condition ell,m != 5 requires more than the four Case-2 forms. In the original Case-1 treatment, three high-degree newforms also survive at ell=5. The paper also discusses twisting the Case-1 Frey curve down to a smaller field, but reports four obstructing newforms in that alternate treatment.

Therefore U31 closes the four Case-2 residual obstructions only. It does not by itself extend Michaud-Jacobs Theorem 3 to ell=5, and it does not by itself eliminate the full equation X^10+256Y^10=Z^17 unless one proves that the present Beal-derived branch lies exclusively in Case 2 or separately eliminates the surviving Case-1 forms.

Primary source:
Philippe Michaud-Jacobs, "On some generalized Fermat equations of the form x^2+y^{2n}=z^p", Mathematika 68 (2022), 344-361, DOI 10.1112/mtk.12127.

## 6. Remaining obligations

1. Audit the exact correspondence between the Beal-derived equation X^10+256Y^10=Z^17 and Michaud-Jacobs' Case 1 / Case 2 split. If the branch can enter Case 1, the Case-1 ell=5 forms must also be eliminated.
2. Reproduce the finite K-level enumeration with an independent Hilbert modular-form computation when a Magma/Sage environment capable of these fields is available; U29-U30 currently rely on complete LMFDB level queries plus exact coefficient-field reductions.
3. If Case 1 is genuinely needed, attack its surviving high-degree residual representations by the same strategy: identify a lower subfield/projective automorphy route, construct a minimal lift, and force a finite lower-level contradiction, or prove residual reducibility directly.

No complete Beal case is declared closed by U31.
