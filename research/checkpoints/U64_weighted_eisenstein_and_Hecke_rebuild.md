# U64: a uniform Eisenstein lemma, the full cyclotomic hypothesis, and the surviving boundary obstruction

**Status: written partial results, source-application audit, and exact finite certificates. Beal's conjecture and the weighted equation remain unresolved.** This is same-model research and review, with distinct arithmetic implementations, not independent expert or proof-assistant certification. U41 remains invalidated by U63; nothing here reinstates its elimination claim.

Date checked: 2026-09-15 UTC. Private remote base inspected: `e14080a0bef24004784fa6806a111bf3006dfb76`. U63's actual manuscript, code and archive were inspected and preserved before extending them.

## 1. Exact scope

The original target is: for positive integers A,B,C,x,y,z with x,y,z>=3 and A^x+B^y=C^z, prove gcd(A,B,C)>1 or independently verify a counterexample. No finite computation below covers that infinite statement.

The active auxiliary problem is

    X^10+256Y^10=Z^17,   X,Y,Z>0,   gcd(X,Y)=1.

Put U=X^2, V=2Y^2. Then U^5+8V^5=Z^17. Necessarily X,Z are odd: if X were even, Y would be odd and the sum would have 2-adic valuation 8, not a multiple of 17. Thus gcd(U,V)=1, and the three parameters U,V,Z are pairwise coprime.

Use U63's corrected negative twist

    C^-: y^2=-f(x),
    f(x)=x^5+40UVx^3+320U^2V^2x+64(8V^5-U^5).

The symbol C^- here means this explicit negative twist, not an unannounced switch between the source's two different Frey families. U63 supplies its written good-reduction model over Q_2(sqrt(5),2^(1/5)) and the consequent local residual irreducibility and conductor exponent 2 per RM component at 2. Those arguments are inherited at their stated self-reviewed level.

The coefficient-two theorem in U62 is a separate written partial proof and is not used to assert this weighted problem is solved.

## 2. Uniform irreducibility at 5: no parameter search is needed

**Lemma 1.** For any integers U,V such that 5 does not divide U^5+8V^5, the polynomial f is irreducible over Q_5. In fact f(T-U-2V) is Eisenstein at 5.

**Proof.** Reducing coefficients modulo 5 gives

    f(x) = (x+U+2V)^5  (mod 5).

Hence every nonleading coefficient of the monic polynomial f(T-U-2V) is divisible by 5. Its constant coefficient satisfies the exact identity

    f(-U-2V)=10(U^5+8V^5)+25R(U,V),

where

    R=-3U^5-2U^4V-24U^3V^2-48U^2V^3-16UV^4+16V^5.

Therefore

    f(-U-2V)/5 = 2(U^5+8V^5) (mod 5),

which is nonzero by hypothesis. The constant coefficient has valuation exactly one, so Eisenstein's criterion applies. Translation preserves irreducibility. QED.

For an explicit coefficient certificate, the coefficients of f(T-U-2V), in ascending powers of T, are

    -65U^5-50U^4V-600U^3V^2-1200U^2V^3-400UV^4+480V^5,
    5U^4+160U^3V+920U^2V^2+640UV^3+80V^4,
    -10U^3-180U^2V-360UV^2-80V^3,
    10U^2+80UV+40V^2,
    -5U-10V,
    1.

The unit hypothesis cannot simply be omitted: U=1,V=3 gives a translated constant divisible by 25. This is a boundary check on the lemma's assumptions, not a weighted solution.

The quintic also remains irreducible over Q_5(sqrt(5)). If L=Q_5(alpha) for a root, then [L:Q_5]=5. The quadratic Galois extension E=Q_5(sqrt(5)) is not contained in L, so [LE:L]=2 and [LE:E]=5. This is a degree argument, not an unjustified general base-change assertion.

**Corollary 2.** Lemma 1 applies to every positive primitive weighted solution.

If 5 divides exactly one of X,Y, the sum X^10+256Y^10 is a 5-adic unit. If neither is divisible by 5, each tenth power is +1 or -1 modulo 25, and 256=6 modulo 25. A sum that is zero modulo 5 is then +5 or -5 modulo 25, so has valuation one, impossible for Z^17. Thus 5 does not divide Z, and U^5+8V^5=Z^17 is a 5-adic unit. QED.

This replaces both the old bounded root search and the special-family implication 'reducible quintic implies a root'. No inherited condition 5|Y is needed.

## 3. Source application: the prime-5 conductor and the other valuation cases

The source and its notation are recorded in [S1]. Its defining polynomial g_5^- is exactly f after specializing the (r,r,p) construction with r=5, p=17, A=1, B=8, C=1, a=U, b=V. Indeed delta_Q^2=-8UV in Proposition 3.22, yielding the displayed positive cubic and linear coefficients. The further twist is delta_K=-1.

The relevant source valuation becomes

    nu_q=34 v_q(Z)-v_q(128U^5V^5).

At 5 this is -5v_5(UV), so nu_5<=0 and nu_5=0 modulo 5. Lemma 1 now supplies irreducibility of g_5^- over Q_5, exactly as required in Theorem 5.11, Table 2. The indicated Artin conductor is **3 per two-dimensional RM component at the prime above 5**. The twist -1 is a square in Q_5, so it makes no change locally. This is an application of the inspected preprint theorem, not a newly reconstructed conductor algorithm.

The valuation cases away from 2 and 5 do not require the old condition 17|Y either:

- If q divides Z, then q does not divide UV and nu_q=34v_q(Z)>0, divisible by 17. Theorem 5.21 gives residual unramifiedness for q!=17 and finite flatness for q=17.
- If q divides UV, then q does not divide Z and nu_q=-5v_q(UV), a nonpositive multiple of 5. The good-reduction row applies to the unit twist -1.
- If q divides neither, the integral discriminant is a q-adic unit; reduction is good.

In particular the residual component is finite flat at 17 whether or not 17 divides Z. This does not mean the characteristic-zero curve has good reduction when 17|Z; that case is toric before lowering.

The section-wide Hypothesis 4 in the source is also accounted for: positivity gives Z>1, and Z is prime to 10, so some prime q!=5 divides Z and has nu_q>0. Modularity follows from its minus-system theorem and quadratic twisting, subject to the source results as cited.

Combining these inputs with U63 points to the target level

    N=(2)^2 * p5^3,   Norm(N)=4^2*5^3=2000.

**This is not yet a completed application of the global lowering theorem.** All prescribed local lifts, determinant compatibility, and retained types still have to be supplied explicitly; the database comparison below is conditional on obtaining the intended representation at this level. In particular, finite flatness must not silently stand for an already constructed fixed-determinant characteristic-zero lift.

## 4. The full cyclotomic irreducibility requirement

The actual Breuil-Diamond Theorem 3.2.2 [S2] requires irreducibility after adjoining the p-th roots of unity. Its notation F(root[p](1)) must not be read as merely F(sqrt(p)). U63's source record named only the quadratic subfield. Its local argument can be completed to the actual requirement as follows.

**Lemma 3 (cyclic restriction).** Let G/N be finite cyclic, and let rho be an irreducible two-dimensional representation over an algebraically closed field with finite image. If rho|N is reducible, then rho is induced from a character of an index-two subgroup H containing N. In particular, if G/N has even order, rho|H is reducible for its unique such subgroup.

**Proof.** Choose a simple N-submodule. The sum of its G-translates is all of the irreducible G-module and is semisimple as an N-module. If restriction is reducible in dimension two, it is therefore a sum of characters. If the two characters are distinct, G permutes their one-dimensional spaces transitively. The stabilizer H of either line has index two and the original representation is induced from that line's character. If both characters coincide, N acts by scalars. Choose one element of G mapping to a generator of G/N. An eigenline of its matrix is invariant under it and under N, hence under G; that contradicts irreducibility. QED.

Apply this to L=K(zeta_17), K=Q(sqrt(5)), and the residual component over an algebraic closure of F_17. The intersection K cap Q(zeta_17) is Q: otherwise the quadratic field K, ramified at 5, would lie in an extension unramified at 5. Thus Gal(L/K) is cyclic of order 16. Its unique quadratic subextension is M=K(sqrt(17)), using the quadratic Gauss sum at the prime 17. Explicitly, if G(T)=sum_{a=1}^{16}(a/17)T^a, the checker verifies G(T)^2=17 modulo Phi_17(T), and G(T^a)=(a/17)G(T) for all sixteen automorphisms. Thus G(zeta_17) generates precisely the quadratic fixed field; no numerical square-root approximation is used.

U63 proves local absolute irreducibility at the prime above 2. It implies global absolute irreducibility. Since 17=1 modulo 8, sqrt(17) belongs to Q_2, and the prime above 2 splits in M/K. If the representation restricted to G_L were reducible, Lemma 3 would make it induced from M. Locally at this split prime, an induced representation is a sum of two characters, contradicting the established local irreducibility. Hence restriction to **G_{K(zeta_17)} is absolutely irreducible**.

This closes the missing field-extension implication. It corrects the source interpretation rather than asserting that the theorem asks only about M. It does not discharge the remaining prescribed-lift hypotheses in Section 3.

## 5. Rebuilding the recovered Hecke comparisons

The new entries came from the actual primary records described in [S3], not from U41. The official LMFDB exporter [S4] assigns every form's eigenvalues to the same field-wide prime list by index. The original form-a table supplies that initial order, including the two ideals

    [11,11,-3*w+2], [11,11,-3*w+1],  w^2-w-1=0.

The recovered entries at these ideals are:

| Orbit suffix | Minimal polynomial of e | Ordered pair at 11 | Sum | Product | Compatible (U,V) pairs |
|---|---|---|---:|---:|---:|
| a | e^2+e-1 | (-e-1,e) | -1 | -1 | 0 |
| b | e^2-9e+19 | (9-e,e) | 9 | 19 | 5 |
| c | e^2+5e-5 | (-e-5,e) | -5 | -5 | 0 |
| d | e^2+e-1 | (-e-1,e) | -1 | -1 | 0 |
| e | e^2+11e+29 | (-e-11,e) | -11 | 29 | 0 |
| f | e^2+5e-5 | (-e-5,e) | -5 | -5 | 0 |
| g | e^2+e-1 | (-e-1,e) | -1 | -1 | 0 |
| h | not recovered in this run | not verified | — | — | not tested |

A failed/incomplete query-mode extraction for d was discarded. The d entry above instead comes from the subsequent deterministic JSON parser. The h endpoint returned non-JSON content in that reader; no eigenvalue was inferred from the old incorrect table. The current field-metadata request also failed, so the common order is grounded in the inspected official exporter plus the previously retrieved explicit table, not in a claimed successful metadata fetch.

For the corrected curve C^-, full exact enumeration over the 35 square/twice-square pairs gives

    (S,P; multiplicity)=(-3,-9;25), (1,-1;5), (9,19;5).

Here

    S=q+1-#C^-(F_q),
    P=(S^2-(q^2+1-#C^-(F_q^2)))/2-2q.

These are the sum and product of the two RM traces. Since 17 is inert in Q(sqrt(5)), residual Frobenius in the coefficient field interchanges the two embeddings. Consequently equality with either conjugate of a recovered quadratic Hecke trace forces the same trace and norm modulo 17. Comparing S and P is a necessary test invariant under swapping embeddings or prime labels; no choice of a favorable root is used.

Thus six of the seven recovered orbits are excluded **in this scoped comparison**. This is not six excluded Beal signatures, not a complete eight-orbit elimination, and not proof that the target level is already justified.

## 6. Investigating the actual surviving orbit rather than concealing it

For b, the prime-11 matches all have V=0 and U a nonzero square. The implication, conditional on a b congruence, is 11|Y, not Y=0.

To test a named possibility—whether the survivor is explained by the boundary curve—three further split primes were used with the correctly indexed entries of b. Exact enumeration gives:

| q | Hecke trace sum/product | Good parameter pairs | Matching pairs | Nonzero-U ratios V/U |
|---:|---|---:|---:|---|
| 11 | (9,19) | 35 | 5 | {0} |
| 19 | (0,0) | 99 | 27 | {0,8} |
| 31 | (-11,29) | 255 | 15 | {0} |
| 41 | (-1,-151) | 440 | 20 | {0} |

There are also nine U=0 matches at 19. The zero pair (U,V)=(0,0) is excluded by primitivity. Individual zero coordinates modulo a prime are retained. There are no nonzero toric pairs in these four square-structured domains; the corresponding toric norm tests are recorded separately as a cross-check, not needed to justify removing a hidden case.

In every case, U=1,V=0 produces the smooth curve

    C0: y^2=64-x^5.

Its point counts are respectively

    q=11: (Nq,Nq2)=(3,123),
    q=19: (20,438),
    q=31: (43,1023),
    q=41: (43,1543).

The resulting trace pairs match the b entries **over the integers**, not just modulo 17. Wolfram independently reproduces all four boundary counts. This is evidence for a boundary/CM identification, not a proof of global equality of Galois representations or Hecke characters. No finite comparison here is represented as a Sturm bound.

The tests at 11,31,41 would force 11*31*41|Y for a surviving b representation. There is no contradiction: these are only finitely many prime factors.

**Why enlarging this same sieve is not automatically a path to impossibility.** The auxiliary equation has the forbidden global boundary (X,Y,Z)=(1,0,1). For any finite modulus M, choosing X=Z=1 and any positive Y divisible by M gives

    X^10+256Y^10=Z^17 (mod M)

and U=1,V=0 (mod M). The analogous choice with Y divisible by M^k works at any specified finite precision. At primes away from 10 the curve at that residue is smooth. Thus finite congruence tests that accept this boundary cannot, merely by their finiteness, conclude Y=0 for an integer solution. A new prime could still distinguish b from C0 if the proposed global identification is false; that identification is not assumed here.

This obstruction changes the priority: determine the surviving representation globally, or find a genuinely global obstruction to its congruence, instead of presenting a growing list of divisibility primes as an elimination.

### 6.1 A global structural fact about the boundary curve

The boundary Jacobian does have complex multiplication by Q(zeta_5); this fact, unlike its identification with b, does not depend on the four-prime comparison. Over L=Q(zeta_5), the map tau:(x,y)->(zeta_5*x,y) is an automorphism of C0 of order five. Its quotient has function field L(y), because x^5=64-y^2, so the quotient curve has genus zero. On the Jacobian the norm correspondence 1+tau+tau^2+tau^3+tau^4 factors through that quotient's zero Jacobian, and is zero. Since Phi_5 is irreducible over Q, this embeds Q(zeta_5) into End^0(Jac(C0)); its degree four is twice the genus, establishing CM. The regular differentials dx/y and x dx/y have eigenvalues zeta_5 and zeta_5^2. Complex conjugation interchanges tau and tau^(-1), so tau+tau^(-1) gives real multiplication defined over K=Q(sqrt(5)). These statements identify the boundary CM field and type, but still do not identify its precise Hecke character with the database orbit b.

## 7. Computation and audit record

`code/U64_weighted_local.py` derives the polynomial identities symbolically and counts square-root multiplicities directly in each finite field. `code/U64_weighted_local.ts` uses bigint, direct binomial expansions, and quadratic characters of norms. Their complete 829 good-parameter rows at the four primes agree, as do all recovered-form comparisons, boundary values, and reported ratio sets. Each count includes the point at infinity and zero square values.

The modulo-25 check spans all 500 pairs (U,V) modulo 25 with U^5+8V^5 a unit modulo 5, and all 25 x values for each pair. It finds no root. This is a reproducibility check of Lemma 1's consequence, not the proof of the infinite lemma. The actual symbolic coefficients provide the parameter-independent certificate.

The Wolfram records separately corroborate the shift, divisibility, discriminant, full modulo-25 root test, and four boundary point counts. Distinct arithmetic implementations are not independent expert review of the mathematical source translations or the cyclic-restriction proof.

Strict TypeScript type checking, Python compilation, tabnanny, the exact scripts, and the row comparator were executed; their commands, output, versions, and digests are retained. No installed standalone lint tool or Lean/Magma/Sage runtime was found. None is reported as having run. The read-only public-API browser session was explicitly stopped, and no credential-bearing connection URL is retained.

## 8. Coverage, unresolved dependencies, and executable next action

New valid progress at the written/self-reviewed level consists of the uniform Eisenstein lemma, its precise prime-5 conductor application, the full cyclotomic irreducibility implication, six recovered-form exclusions, and a tested explanation of the survivor's boundary behavior. The old Gaussian conditions 5|Y and 17|Y are not needed for the local inputs established here.

The weighted equation is still open in this research record. The following must not disappear from its dependency graph:

1. Construct and verify the prescribed local lifts (including fixed determinant at 17) needed to adapt the lowering theorem, rather than invoking Azon's Hypothesis-5 package outside its assumptions.
2. Recover and check h's actual Hecke record; independently reconstruct the newspace instead of equating a database list with a proof of completeness.
3. Identify or distinguish b and the boundary CM object globally. If they coincide, use a global congruence obstruction; the finite tests already completed do not eliminate b.
4. Obtain independent expert or kernel verification for the serious written partial proofs, including U61/U62; no such verification is claimed.

The next mathematical action is (3), with the source/data work in (1)-(2) supporting it. The finite-domain scripts in this checkpoint are completed and need not be repeated as new research unless their code, source inputs, or implemented assertion changes. No full-solution candidate, counterexample, publication, submission, external contact, or prize award exists in this checkpoint.

## Sources

[S1] Martin Azon, *Effective Darmon's program for the generalised Fermat equation*, arXiv:2504.01967v2, 2025-07-03: Proposition 3.22, Hypothesis 4, Theorems 5.5, 5.11 (Table 2) and 5.21; compare Hypothesis 5 and Theorem 5.23. Original HTML and PDF inspected, including the table screenshot. This is a cited preprint dependency; the new shift identity is our derivation, not attributed to the paper.

[S2] Christophe Breuil and Fred Diamond, *Formes modulaires de Hilbert modulo p et valeurs d'extensions entre caracteres galoisiens*, Ann. Sci. ENS 47 (2014), 905-974, DOI 10.24033/asens.2230. Author PDF Theorem 3.2.2, printed pp.36-37, inspected visually and in text. The cyclic-restriction argument above supplies a missing implication in our application; it does not alter the source theorem.

[S3] LMFDB, the primary hmf_hecke records for labels 2.2.5.1-2000.1-a through -g, with the retrieval distinctions, exact selected entries and timestamps in `references/U64/hecke_records.json`. The -h response is explicitly unverified. Complete API bodies were not copied to this container; observed hashes are provenance, not substitutes for exact entries.

[S4] LMFDB official code, `lmfdb/hilbert_modular_forms/hilbert_modular_form.py`, revision `fea1c3dffe05b3ac2df3d5953885db035d9096b4`, especially `get_hmf_field` and `download_hmf_magma`/`download_hmf_sage`. The shared field prime list is paired with the indexed eigenvalues. URLs and access limitations are preserved in `references/U64/sources.json`.
