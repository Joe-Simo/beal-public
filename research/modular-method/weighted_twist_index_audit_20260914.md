# We have not solved Beal’s conjecture yet.

## Additive audit; no subcase elimination claimed

This note audits the primitive equation X^10+256Y^10=Z^17, not all Beal signatures. It does not replace or erase U40-U42. The global reduction gap recorded in U42 remains open.

Pinned records read in full: U15 blob `003506f12b6ce675c465463e797137c69447519a`; U32 blob `143003bf4d995a1600849dd55af6ee50d595702f`; concurrent U41 `U41_weighted_level2000_q11_elimination.md` blob `d11be773928d88d87f4d5a09ab963574ed3a767e`; U42 blob `1f051247b1cf8d923c6174f87f2b76a1ec01578f`. Pre-write main was `af20e9a234e417732de64c539d42b35d8dead6b9`. Other new work is preserved; these conclusions concern the pinned U41, not uninspected later revisions.

Evidence status: self-reviewed derivations with exact symbolic/finite corroboration. No expert review, formal kernel proof, authenticated newspace reconstruction, complete Beal solution, or prize claim.

## 1. Polynomial, root field and index

The equation forces X,Z odd: if X is even, Y is odd and the left side has 2-adic valuation 8, incompatible with Z^17. Put U=X^2, V=2Y^2 and S=U^5+8V^5=Z^17. Then gcd(U,V)=1 and gcd(Z,XY)=1.

The correctly signed polynomial is

    f(x)=x^5+40UVx^3+320U^2V^2x+64(8V^5-U^5).

For P=x^5+5tx^3+5t^2x and Q=x^4+3tx^2+t^2, direct multiplication gives P^2+4t^5=(x^2+4t)Q^2 and P'=5Q. The roots of Q occur in opposite pairs; evaluating P+d at them gives resultant 5^5(d^2+4t^5)^2. Hence

    Disc_x(f)=2^24*5^5*S^4.

This is a polynomial discriminant, not the field or minimal-model discriminant. The old negative-cubic polynomial instead has discriminant 2^24*5^5*(U^10-48U^5V^5+64V^10)^2.

Let theta^5=2 and alpha=2U theta-2V theta^4. Expansion gives f(alpha)=0. Since

    (h+2)^5-2=h^5+10h^4+40h^3+80h^2+80h+30

is Eisenstein at 5, Q_5(theta) has degree 5. Alpha is not rational over Q_5 for rational U,V not both zero, by independence of 1,theta,...,theta^4. The tower law gives degree 5 for alpha. Thus f is irreducible over Q_5 and Q, and its root field is Q(2^(1/5)). This is a universal proof, not extrapolation from a residue search.

The ring of integers of L=Q(theta) is Z[theta]. Indeed Disc(h^5-2)=50000=2^4*5^5, so only 2 and 5 could divide the index. At 2, theta is an Eisenstein uniformizer; at 5, theta-2 is one. In either local degree-5 totally ramified extension, the valuations of c_i*pi^i are distinct modulo 5. Integrality of their sum therefore forces all c_i in Z_p. This proves maximality at both possible index primes.

The columns of 1,alpha,...,alpha^4 in the theta basis are

    [1,  0, -16UV,        0,       384U^2V^2]
    [0, 2U,      0, -48U^2V,            128V^4]
    [0,  0,   4U^2,  -32V^3,         -128U^3V]
    [0,  0,   8V^2,    8U^3,         -256UV^3]
    [0,-2V,      0,  48UV^2,             16U^4].

Their determinant is 1024*S^2. A hand reduction deletes the first row/column, then adds 24UV times column 1 to column 3 and 32UV times column 2 to column 4 of the remaining matrix. Rearrangement gives two 2-by-2 blocks each of determinant 32S, with net positive sign. Thus

    [O_L:Z[alpha]]=2^10*S^2=2^10*Z^34.

SymPy and Wolfram independently confirmed the discriminants, root identity, determinant and discriminant/index equality. A fixed root field does NOT imply a fixed curve, or good Jacobian reduction at primes dividing Z.

Also 5 does not divide Z. Otherwise U,V are units modulo 25 and U^5=-8V^5. Fourth powers give 1=8^4=21 modulo 25, a contradiction. Both exact implementations checked all 400 unit pairs.

## 2. A concrete defect in the untwisted U41 calculation

For X odd, c=f(0)=64(256Y^10-X^10) has valuation 6 and normalized unit c/64=-1 modulo 4. In the unramified quadratic completion K_2 of K=Q(sqrt(5)), -1 is not a square modulo 4. Reduction of tau^2=-1 modulo 4 to F_4 forces tau=1 modulo 2, whence tau^2=1 modulo 4, contradiction.

The author's `Frey_cvs.m`, blob `381f9b8635df091f7cb64809ed4783614366b03d`, tests even valuation and the unscaled integer modulo 4. It accepts -64, and it accepts c. That code result does not establish the normalized unit condition needed by the model proof in Azon Definition 4.25/Proposition 4.28, printed pp.35-36. That proof explicitly uses kappa=c/2^mu and requires delta_2*kappa to be a square modulo 4.

Therefore pinned U41's assertion that the untwisted curve satisfies the normalized condition is false. Its use of conductor exponent 2 for this untwisted curve is not justified by the cited table. This is a source-application/code audit, not a claim to have refuted the entire paper.

## 3. Repair by an explicit smooth model

Use the (-1)-twist and reflect x. The monic equation is

    D: y^2=g(x)
      =x^5+80X^2Y^2x^3+1280X^4Y^4x+64(X^10-256Y^10).

Indeed g(x)=-f(-x). Also g(0)-(8X^5)^2=-2^14Y^10.

Let pi^5=2 over K_2. The change x=pi^8u, y=8(2v+X^5), followed by division by 256, gives

    v^2+X^5v=u^5+5pi^4X^2Y^2u^3+5pi^8X^4Y^4u-64Y^10.  (M)

This identity is universal modulo pi^5-2. Its special fiber is v^2+v=u^5, smooth on the affine chart since the derivative in v is 1. At infinity, w=1/u and z=v/u^3 give

    z^2+X^5w^3z=w+5pi^4X^2Y^2w^3+5pi^8X^4Y^4w^5-64Y^10w^6.

The unique point at infinity is (w,z)=(0,0), with derivative in w a unit. The two monic double-cover charts glue to a finite flat proper cover of P^1 with smooth special fiber. Thus D has good reduction over this degree-5 tame extension. The included Python checker verifies the coordinate change, overlap and both derivative tests; geometry is justified by this argument, not by the program alone.

Over an unramified extension containing fifth roots of unity, tame inertia pi -> zeta*pi acts on the special fiber by u -> zeta^2u, v -> v. Its quotient has rational coordinate v. For ell=17, invariant H^1 is the H^1 of the quotient and is zero. By specialization, the full four-dimensional Tate representation is tame with conductor 4; each two-dimensional RM summand has conductor 2.

Twisting back by -1 introduces the ramified quadratic character of K_2(i)/K_2, of conductor 2. Since the corrected representation is tame, its twisted two-dimensional summands have Swan conductor 2 and tame conductor 2, hence conductor 4, not 2. This explains why the two twists cannot be assigned the same local type.

Consequently a norm-2000 core may be pursued for D, not by declaring the original f to satisfy the normalized square condition. Global modularity and level lowering do not follow from this local model.

## 4. Cyclotomic restriction hypothesis

For D, the local residual two-dimensional representation at 2 is absolutely irreducible: inertia has distinct inverse characters of order 5 and Frobenius, with residue cardinality 4, interchanges the two lines.

A useful general lemma follows. If a two-dimensional absolutely irreducible representation of G_K over algebraically closed characteristic 17 is locally absolutely irreducible at 2, its restriction to G_{K(zeta_17)} is absolutely irreducible. Indeed the quotient is cyclic of order 16, with unique quadratic intermediate K(sqrt(17)). If restriction were reducible, it is a sum of two characters. If scalar, the full projective image is cyclic and the full representation has an eigenline. Otherwise the two lines have index-2 stabilizer G_{K(sqrt(17))}. But 17 is a square in Q_2, so this quadratic extension splits at 2; the local decomposition group preserves both lines, contradicting local irreducibility. Semisimplicity of the restriction follows by summing translates of a minimal invariant subspace.

This establishes the full cyclotomic restriction, not merely a statement about the quadratic intermediate field. It supplies one hypothesis of Breuil-Diamond Theorem 3.2.2, not an entire level-lowering application.

## 5. Finite checks reproduced; newform input not authenticated

An exact TypeScript bigint computation over all 120 nonzero pairs in F_11^2 reproduces the eight triples (S,P,S^2-4P) of pinned U41, with its multiplicities:

    (-9,19,5;5), (-7,11,5;25), (-3,-9,45;25), (-1,-1,5;5),
    (1,-1,5;5), (3,-9,45;25), (7,11,5;25), (9,19,5;5).

Here the Euler polynomial is 1-ST+(P+22)T^2-11ST^3+121T^4. The field F_121 was represented by j^2=2. Quadratic-character counts were checked against square-fiber enumeration for all field elements; both counters share field arithmetic, so they are not independent arithmetic kernels.

The (-1)-twist changes S to -S at 11, leaving the unrestricted inventory invariant as a set. It does not leave a specified parameter pair's trace unchanged.

The separate U15 mod-11 checker confirms that only case III survives, with B=0 modulo 11. Hence 11|Y in that branch. The corrected curve then reduces, after scaling by powers of X, to y^2=x^5+64. Its counts are #D(F_11)=3 and #D(F_121)=123, giving S=9,P=19 and RM trace polynomial T^2-9T+19. The untwisted x^5-64 has counts 21 and 123. These boundary/control curves are not positive-integer Beal solutions.

LMFDB browser/API requests failed or encountered access controls, and a bounded Wolfram JSON import returned $Failed. No Hecke record, prime ordering, full newspace or completeness claim was authenticated in this audit. Pinned U41's eight newform records therefore remain unverified external input, not a certified elimination.

## 6. Open obligations and next action

- Audit Azon's modularity theorem for the precise weighted specialization and its dependencies, rather than confusing citation with independently reconstructed proof.
- Apply Breuil-Diamond with D, the full cyclotomic restriction, determinant, all local types and the ordinary/nonordinary alternatives at 17 explicitly checked.
- Authenticate or reconstruct the norm-2000 newspace, including correctly indexed Hecke eigenvalues and coefficient embeddings; use T^2-9T+19 for the surviving branch at 11.
- Reconstruct the missing global reduction and retain every untouched Beal signature in the coverage gap.

No branch is eliminated by this note. No background process is running.

## Sources and execution record

Martin Azon, *Effective Darmon's program for the generalised Fermat equation*, arXiv:2504.01967v2, 3 July 2025: https://arxiv.org/abs/2504.01967v2 . Source locators: section 3.3.2, Proposition 3.22; Definition 4.25/Proposition 4.28, printed pp.35-36; Table 2/Theorem 5.11, printed p.48; Propositions 5.20, Theorem 5.21, Hypothesis 5/Theorem 5.23. The original model proof and table were inspected in PDF screenshots. This run does not certify every external proof dependency or publication status.

Author implementation: https://github.com/martin-azon/effective_Darmon , pinned `Frey_cvs.m` blob above; read through GitHub, not modified.

Breuil-Diamond, Ann. Sci. ENS 47 (2014), 905-974, DOI 10.24033/asens.2230. Theorem 3.2.2 read in the author manuscript, printed pp.36-37: https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/extensions.pdf . Its application remains an obligation.

Observed tools: Python 3.13.5, SymPy 1.14.0, TypeScript 5.8.3, Node 22.16.0, Wolfram 15.0.1. Strict TypeScript checks with noUnusedLocals/noUnusedParameters/noUncheckedIndexedAccess, assertion tests and Python compilation passed. No full lint or Python static-type-check pass is claimed: the relevant standalone tools and Bun were not found. No Lean, Sage, Magma or PARI runtime was found. Wolfram independently returned determinant 1024*(u^5+8v^5)^2, base discriminant 50000 and discriminant/index remainder zero.

The literal File Library RESEARCH_PROMPT.txt was identified as Beal, but only indexed sections were retrievable; a provably complete full-file read was not achieved. No selected-project filesystem metadata was exposed. The existing private Beal repository was the research reference, with local companion files under /mnt/data/beal; this was not represented as a full repository clone. All remote writes from this audit are additive and confined to this repository. No public posting, expenditure or prize contact was made.