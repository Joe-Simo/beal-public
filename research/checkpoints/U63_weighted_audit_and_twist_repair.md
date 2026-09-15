# U63: U41 invalidation and an explicit local repair for the weighted curve

**Status: a flaw was found in U41's claimed weighted-equation elimination. The full Beal conjecture is not solved.** This checkpoint supplies exact counterevidence to U41's finite nonmatching assertion, a written local-model/conductor repair, and new reproducible checks. It does not supply a completed replacement elimination. Review is by the same model; there is no independent expert review or proof-assistant certificate.

Research date: 2026-09-14 America/New_York / 2026-09-15 UTC. Inspected private repository revision: `77ccf1cc4054f22e3a3e35baa34f1ed1a7951ad7`.

## 1. Scope and dependency correction

The original target remains: for positive integers A,B,C,x,y,z, with x,y,z>=3 and A^x+B^y=C^z, prove gcd(A,B,C)>1, or independently verify a counterexample.

The active auxiliary equation is

    X^10+256Y^10=Z^17,   gcd(X,Y)=1,   X,Y,Z>0,
    X and Z odd.

The oddness of X is necessary: if X were even, coprimality would make Y odd and v2(X^10+256Y^10)=8, not a multiple of 17. Then Z is odd as well. Set U=X^2 and V=2Y^2. The attached genus-two curve used in U41 has polynomial

    f(x)=x^5+40UV x^3+320U^2V^2 x+64(8V^5-U^5).       (1.1)

This is the positive-cubic polynomial in the author's executable source [S1]. Its discriminant, recomputed symbolically, is

    Disc(f)=2^24*5^5*(U^5+8V^5)^4.

Thus the curves considered are nonsingular for positive weighted parameters. This identity also checks the good-reduction domain at 11.

U41's Sections 11-12 must no longer be credited as eliminating this equation. There are two distinct issues: incorrect Hecke-entry assignment at 11, and an inappropriate square test in the local twisting argument at 2. The latter is the earlier unsupported implication in the ordered proof. A third, less serious discrepancy is the size of its modulo-125 enumeration.

U62's coefficient-two equation X^10+Y^10=2Z^17 and its parity-specific Beal corollary do not use U41. Their written/self-reviewed status is unchanged by this audit; they have not thereby gained independent certification. No assertion that all all-even or all exponent-17 cases are solved survives here.

## 2. The prime-11 comparison in U41 is false as written

The primary LMFDB page for form `2.2.5.1-2000.1-a`, obtained this session, gives e^2+e-1=0 and these entries [S2]:

| Norm | Prime ideal in the database basis | Eigenvalue |
|---:|---|---|
| 9 | [9,3,3] | -5 |
| 11 | [11,11,-3*w+2] | -e-1 |
| 11 | [11,11,-3*w+1] | e |
| 19 | [19,19,-4*w+3] | -5 |

U41 instead used (e,-5) at the two norm-11 primes. Its pair combines entries associated with different primes. We do not infer the correctness of any other orbit's entries from the old table.

The actual pair (-e-1,e) has sum -1 and product -1. Take the permitted square-structured residue (U,V)=(0,2) modulo 11. Direct counting on y^2=f(x) gives

    #C(F_11)=13,   #C(F_121)=163.

For the degree-four Euler polynomial, let S=12-#C(F_11) and

    a2=(S^2-(122-#C(F_121)))/2,   P=a2-22.

Here S=-1, P=-1. The real-multiplication trace polynomial is T^2+T-1, exactly matching the corrected pair. Both possible assignments to its conjugate embeddings were among the assignments U41 purported to exclude.

This residue really is in the necessary weighted domain: (X,Y,Z)=(0,1,5) modulo 11 satisfies X^10+256Y^10=Z^17, with U=X^2=0 and V=2Y^2=2. A zero coordinate *modulo 11* is not a zero positive integer base. These are local residues, not a global weighted solution and not a Beal counterexample.

The exact match disproves the claim of no local matches in U41's stated untwisted comparison. It does not prove that form a survives a correctly retwisted global argument. In fact Section 5 gives a valid exclusion of form a after repairing the twist and retaining the square conditions.

## 3. The local square test must retain its normalized unit

For X odd, the constant in (1.1) is

    c0=64d,   d=256Y^10-X^10,   v2(c0)=6,   d=7 (mod 8).

The integer predicate in the source [S1] tests whether the valuation is even and the unnormalized integer is 0 or 1 modulo 4. It returns true here because c0 is 0 modulo 4. But that says nothing about whether the normalized odd unit d is square modulo 4.

Let F=Q_2(sqrt(5)), the completion of K=Q(sqrt(5)) at 2, and omega=(1+sqrt(5))/2. Its integer ring is Z_2[omega], omega^2=omega+1, with residue field F_4. Complete enumeration in O_F/4 gives the square coefficient pairs

    (0,0), (1,0), (1,1), (2,3).

The element d corresponds to (3,0), which is absent. Thus d is not square modulo 4, even in this unramified quadratic field. For example X=Y=1 gives c0=16320 and normalized unit 255; this is a test of the predicate, not a claimed solution of the weighted equation.

The inspected paper defines the normalized constant kappa and normalized twist in Definition 4.25; its Proposition 4.28 proof uses their product being square modulo the square of the prime ideal [S3]. The code's test on the nonunit cannot replace that normalized requirement. We flag this precise application/code inconsistency, not a claim that every result of the paper is false. No source code was changed and no author was contacted.

## 4. Explicit repair, without relying on the ambiguous predicate

**Local-model lemma.** For odd X and integral Y, the negative quadratic twist

    C^-: y^2=-f(x)

has good reduction over the tame degree-five extension F(pi), pi^5=2.

**Proof.** The integer X^10-256Y^10 is 1 modulo 8, so it has an odd square root kappa in Z_2. The usual square-root criterion follows constructively: start with an odd solution modulo 8 and, at each step, change a root modulo 2^j by 2^(j-1) when needed to correct its square modulo 2^(j+1); choosing compatible roots gives the limit. Hence

    kappa^2=X^10-256Y^10.

Substitute x=pi^8*t and y=16w+8*kappa into y^2=-f(x). Exact cancellation gives

    w^2+kappa*w = -t^5-5X^2Y^2*pi^4*t^3-5X^4Y^4*pi^8*t.      (4.1)

This polynomial identity was checked in the quotient by pi^5-2 and kappa^2-X^10+256Y^10, with zero remainder, in SymPy and Wolfram. It is not merely a numerical approximation.

Equation (4.1) is integral. Its reduction is w^2+w=t^5 over F_4; the affine derivative with respect to w is 1. At infinity use u=1/t and v=w*u^3. With a=5X^2Y^2*pi^4 and b=5X^4Y^4*pi^8 the second chart is

    v^2+kappa*v*u^3 = -u-a*u^3-b*u^5.

The unique point at infinity is (u,v)=(0,0), and the derivative of the defining equation with respect to u there is 1. The two finite, degree-two covers of the standard charts of P^1 glue to a proper flat model; these derivative tests establish smoothness of its special fiber. This proves good reduction. The polynomial pi^5-2 is Eisenstein, and 5 is prime to the residue characteristic, so the extension is tame. QED.

### 4.1 Inertia and conductor consequences

Over an unramified extension containing the fifth roots of unity, a tame generator pi -> zeta_5*pi acts on the special fiber by

    (t,w) -> (zeta_5^(-8)*t,w).

A nonidentity element has exactly three geometric fixed points: the two points above t=0 and the point at infinity. The tame fixed-point formula gives trace -1 on H^1 for each of the four nonidentity elements. Together with dim(H^1)=4 this identifies the inertia characteristic polynomial as Phi_5. In particular there are no inertia invariants, and wild inertia is trivial.

Consequently the Artin conductor of H^1(C^-) at 2 is 4. Under the K-defined real-multiplication decomposition used in the Frey construction, each two-dimensional component has conductor exponent 2. Each K-defined RM component is stable under the decomposition group. Frobenius acts on the inertia characters by multiplication by 4 modulo 5, so a two-dimensional stable component contains one inverse pair of nontrivial fifth-order characters. Frobenius interchanges this pair, since 4=-1 modulo 5. They remain distinct modulo 17. This also proves absolute irreducibility of the local residual component, rather than invoking the problematic nonunit SQ test.

For comparison, C^+:y^2=f(x) is the quadratic twist of C^- by the character of F(i)/F. This ramified quadratic character has conductor 2, as follows from the Eisenstein polynomial of i-1, T^2+2T+2, and its different. Its Swan conductor is 1. Twisting a tame four-dimensional representation by it gives Swan conductor 4 and still no inertia invariants. Thus H^1(C^+) has conductor 8, or exponent 4 per two-dimensional RM component, not the exponent 2 assigned to this curve in U41.

These are written local arguments, not claims of a machine-checked conductor computation. If the unreviewed exponent 3 at the prime above 5 and all other lowering inputs are ultimately justified, the corrected negative twist leads to norm 2000 whereas the original positive curve has norm 32000 at these two primes. This conditional level calculation is not a completed global level-lowering theorem.

### 4.2 A repaired irreducibility hypothesis

Let rho-bar be a two-dimensional residual component for the corrected negative twist, and use its local irreducibility just established. It is then globally absolutely irreducible. Its restriction to G_{K(sqrt(17))} is also absolutely irreducible.

Indeed, if restriction to this index-two normal subgroup were reducible, Clifford theory gives two characters exchanged by G_K and rho-bar would be induced from that quadratic extension. The alternative that the subgroup acts by a scalar character is impossible: the remaining cyclic quotient has an invariant eigenline over the algebraic closure. But 17 is 1 modulo 8, so sqrt(17) belongs to Q_2. The prime of K above 2 splits in K(sqrt(17))/K. The restriction of such an induced representation to that local decomposition group would be a sum of characters, contradicting local irreducibility.

This addresses the irreducibility hypothesis inspected in Breuil-Diamond Theorem 3.2.2 [S4]. It does not establish the theorem's other local-lift, determinant, modularity and prescribed-type hypotheses. These must be audited separately for the repaired representation.

## 5. Recomputed prime-11 inventory, with the twist and square structure retained

For all 120 nonzero pairs (U,V) in F_11^2, U^5+8V^5 is nonzero; no toric pair is silently omitted. The full untwisted distribution (S,P,D; multiplicity), D=S^2-4P, is

    (-9,19,5;5), (-7,11,5;25), (-3,-9,45;25), (-1,-1,5;5),
    ( 1,-1,5;5), ( 3,-9,45;25), ( 7,11,5;25), ( 9,19,5;5).

This part of U41 is reproduced. Imposing U square and V twice a square leaves exactly 35 pairs, including the coordinate-axis cases. Their distributions are:

    y^2= f(x): (-9,19,5;5), (-1,-1,5;5), ( 3,-9,45;25);
    y^2=-f(x): ( 9,19,5;5), ( 1,-1,5;5), (-3,-9,45;25).

Direct counting verifies the quadratic-twist identities N11(C^+)+N11(C^-)=24 and N121(C^+)=N121(C^-) for every pair. Keeping only the unrestricted symmetric distribution would conceal the effect of the twist on the necessary square domain.

**A valid repaired exclusion.** Form a has rational trace sum -1, hence 16 modulo 17. The corrected negative-twist square domain instead has sums 9,1,-3, or 9,1,14 modulo 17. None is 16. Therefore form a is eliminated in this corrected, explicitly scoped comparison. This does not validate U41 retrospectively and does not eliminate the other seven orbits without their correctly keyed data. The trace-sum test is invariant under swapping the two primes and both coefficient-field embeddings. In particular 5 is nonsquare modulo 17, so Frobenius on the quadratic residue coefficient field interchanges the two RM traces; equality with an eigenvalue of form a requires its conjugate sum -1 as well.

## 6. Modulo-125 root certificate

Enumerate all squares U modulo 125 and all twice-squares V modulo 125, retaining exactly U^5+8V^5 nonzero modulo 5. Both residue sets have 53 elements; the retained pair count is 1550. All 125 x residues were tested for every pair. No root of f was found. The subset with 5 dividing V has 150 pairs. U41's count of 793 was not reproduced under its stated domain and must not be retained.

This finite computation proves that no polynomial with parameters lifting this domain has a Q_5 root: a root of a monic integral polynomial would be 5-integral and would reduce modulo 125. It does not, by itself, prove irreducibility of an arbitrary quintic. The special-family implication and the resulting conductor row remain source-application obligations.

For a primitive weighted solution, Z is a 5-adic unit. If both X and Y are units, their tenth powers are +/-1 modulo 25 and 256=6 modulo 25. A sum divisible by 5 is then +/-5 modulo 25, so has valuation 1, impossible for Z^17. If one coordinate is divisible by 5, the other is a unit and the sum is a unit. Thus the retained domain is a necessary one, without needing an unreviewed claim that 5 divides Y.

## 7. Computation audit and reproducibility

The mathematical assertions and exact finite domains are stated above. Python counts square-root multiplicities in F_11[i] using pair multiplication; TypeScript uses bigint, direct real/imaginary expansions and Euler's criterion on the field norm. Every one of the 120 rows agrees, not merely the final histograms. Zero values, coordinate axes, and the point at infinity are retained. SymPy checks squarefreeness at 11 and the symbolic model/discriminant identities. Wolfram separately reproduces the finite distributions, the modulo-125 obstruction, the mod-4 square set, and the model and witness identities.

Run from the repository root:

    python code/U63_weighted_audit.py
    tsc --target ES2022 --module commonjs --strict --noUncheckedIndexedAccess \
        --noUnusedLocals --noUnusedParameters --outDir <temporary-directory> \
        code/U63_weighted_audit.ts
    node <temporary-directory>/U63_weighted_audit.js

The commands, versions, source digests, outputs, comparison record, and a replay of the pre-existing U60 exact counterexample checker are preserved in the evidence archive. No bound on positive solutions has been obtained. No interrupted or unavailable calculation is counted as an exclusion.

## 8. Current coverage and next obligation

U41's claimed weighted exclusion is invalidated, not merely awaiting endorsement. Its historical file is retained; this checkpoint and the repository index supersede its success label. Claims relying on its all-eight-orbit nonmatching assertion must be withheld. U60-U62 are not downstream of that assertion and retain only their previously stated self-reviewed status.

The repair establishes a usable local model at 2, its written conductor/irreducibility consequences, and one correctly scoped form-a exclusion. The weighted equation, its original-Beal orientation, and the general conjecture remain unresolved.

The next mathematical task is to rebuild the other Hecke comparisons for y^2=-f, using actual prime-ideal labels rather than array offsets, while auditing the remaining level-lowering assumptions for this twist. The successful LMFDB inventory and form-a page did not justify guessing entries for the seven other forms: subsequent download/form-page requests returned a browser challenge. No challenge was bypassed. Independent newspace reconstruction and expert/kernel verification are still absent. This is a concrete data/verification limitation, not an argument that further research is impossible.

Source identities, exact accessible entries, versions and access limitations are recorded in `references/U63/sources.json`. No paper, claim or error report was sent externally, and no public repository was used to preserve the original research.
