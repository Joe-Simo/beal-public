# U68: a global coefficient-divisibility and height obstruction

**Status: written, self-reviewed partial theorems with distinct exact arithmetic checks. Neither the weighted equation nor Beal's conjecture is solved. No independent expert or proof-assistant certification is claimed.**

Research date: 2026-09-15. Private remote base actually inspected: `78255c2e82c19670b9cd5a2b7c44c4cbdca82783` (U67). The attached U67 archive was restored additively, with conflicting files preserved rather than overwritten. Its main manuscript agrees with the remote blob `ae9b53ae03a1dee3f9eccee002831e8255d7a04c`.

## 1. What changes in this checkpoint

The active auxiliary equation remains

    (W) X^10 + 256 Y^10 = Z^17,
        X,Y,Z positive integers, gcd(X,Y)=1.

The remote quintic U65, precisely identified in U67, supplies the necessary equation

    (Q) beta^17 = X^2 + 2 rho^3 Y^2,
        rho = positive fifth root of 2,
        beta = b0+b1 rho+b2 rho^2+b3 rho^3+b4 rho^4 in Z[rho],
        17 | XY.

Its complete unit elimination, not merely its norm equation, is essential. This is an inherited written/self-reviewed result, not a newly independently certified theorem. U68 does not invoke the boundary congruence (BC), the invalidated U41, a modular-form identification, newspace completeness, or U61/U62.

The new argument uses **one common integral beta**. Congruences force a large common divisor of three of its coefficients. All five complex embeddings bound those same coefficients from above. A binomial identity prevents all three coefficients from vanishing. This is a global size argument, rather than an attempt to contradict a passing local solution by increasing precision.

### Main conclusions

1. The sparse-root system (Q), with positive coprime X,Y, X odd and 17|XY, satisfies the explicit prime-support inequality in Theorem 1 below.
2. Every putative weighted solution, using the inherited implication (W) => (Q), has

       max(X,Y) > 10^514.

   Thus at least one of its two left-hand bases has at least 515 decimal digits. This is **not** a computer search through that range: it is a consequence of a proved inequality and fourteen fully specified finite residue certificates.
3. Let E be the part of XY supported on primes in the following eleven classes modulo 85, counting their full multiplicities:

       1,13,18,33,38,47,52,67,69,72,84.

   Then a putative weighted solution also has

       E > 10^483.

   This is a bound on a product of prime powers, **not** a claim that a single prime exceeds 10^483. In particular that exceptional part cannot be absent.

These statements do not give an upper bound, eliminate the remaining exceptional-prime possibilities, settle a new complete original-Beal exponent family, or prove the full conjecture. No novelty claim is made.

## 2. The exact prime-support theorem

Call a rational prime **exceptional** when its residue modulo 85 is in the eleven-class list above. The primes 2,5,17 are not in this list.

**Theorem 1 (global sparse-root obstruction).** Suppose (Q) holds with X,Y positive coprime integers, X odd and 17|XY. Write

    T = max(X,Y),
    E = product of q^v_q(XY) over exceptional primes q,
    S = XY/E,
    Delta = S^2/17.

Then Delta is a positive integer and

    Delta | b1, b2, b3,                              (2.1)
    at least one of b1,b2,b3 is nonzero,              (2.2)
    T^2 > Delta^17.                                 (2.3)

Equivalently,

    S^34 < 17^17 T^2,
    E > XY/(sqrt(17) T^(1/17)).                      (2.4)

In particular E>1: the sparse-root system cannot have every prime factor of XY outside the exceptional classes.

The theorem is proved in Sections 3–6. Its hypotheses state the actual integral element equation; there is no substitution of a norm identity for that equation.

## 3. Exactly where the seventeenth-power map is injective

For a prime q and n>=1 set

    R(q,n) = (Z/q^n Z)[rho]/(rho^5-2).

It is a free rank-five module in the displayed basis, even at the ramified primes. Congruence of its coordinates therefore has its usual coefficientwise meaning.

### 3.1 Residue factor degrees away from 2 and 5

For q not dividing 10, the polynomial rho^5-2 is separable modulo q. Choose one of its roots a and a primitive fifth root zeta in an algebraic closure. Its five roots are a zeta^j. Frobenius acts on their labels by

    j -> q j + c  in F_5

for one c in F_5. The lengths of these Frobenius orbits are the degrees of the irreducible residue factors: an element is in F_(q^f) precisely when the f-th Frobenius fixes it.

If q=1 modulo 5, this affine map is either the identity or a nonzero translation. If q is not 1 modulo 5, translate its unique fixed point to zero. Its nonzero cycles then have length equal to the multiplicative order of q modulo 5. Consequently the only degree patterns are

| q modulo 5 | Degrees of the factors of rho^5-2 |
|---|---|
| 1 | 1,1,1,1,1 or 5 |
| 2 or 3 | 1,4 |
| 4 | 1,2,2 |

The unit group modulo q is the product of groups of orders q^f-1 for these degrees f. The kernel of reduction from R(q,n)^* to R(q,1)^* has q-power order: filter it by successive powers of q, whose subquotients are additive groups in characteristic q. Thus, when q!=17, the map u->u^17 on R(q,n)^* is an automorphism whenever no displayed q^f-1 is divisible by 17.

Because the order of a nonzero residue modulo 17 divides 16, this fails exactly as follows:

- q=1 modulo 17, in any of the four nonzero classes modulo 5;
- q=-1 modulo 17, with q=2,3,4 modulo 5;
- q=4 or -4 modulo 17, with q=2 or 3 modulo 5.

The Chinese remainder calculation gives precisely

    q mod85 in {1,13,18,33,38,47,52,67,69,72,84}.     (3.1)

The ambiguity between the two possible factorizations when q=1 modulo 5 does not affect the criterion: an order dividing both 5 and 16 is one. There is no missing degree-five exception.

### 3.2 The ramified primes 2 and 5

Modulo 2 the algebra is F_2[rho]/rho^5; its unit group has order 16. Modulo 5 it is F_5[rho]/(rho-2)^5; its unit group has order 4*5^4=2500. Higher reduction kernels have 2-power or 5-power order. All these orders are prime to 17. Hence the power map is also an automorphism on R(2,n)^* and R(5,n)^*.

This proof uses finite rings and their unit groups directly; it does not incorrectly treat a ramified quotient as a field.

## 4. Coefficient divisibility at each nonexceptional prime

### 4.1 A prime q!=17 dividing Y

Let e=v_q(Y)>0. Coprimality makes X a unit modulo q, and (Q) gives

    beta^17 = X^2  in R(q,2e).

Both beta and the right-hand side are units. For a nonexceptional q, raising to the seventeenth power is bijective both in R(q,2e)^* and in the scalar unit subgroup. In particular there is a scalar a with a^17=X^2, and uniqueness in the larger algebra forces beta=a. Therefore

    q^(2e) | b1,b2,b3,b4.                           (4.1)

This includes q=2 and q=5. No inverse of rho is needed in this case.

### 4.2 A prime q!=17 dividing X

Now Y is a unit and q is odd because X is odd. In particular rho and 2 are units. Since

    rho^68 = 2^13 rho^3,

choose a scalar unit a with a^17=Y^2/2^12 modulo q^(2e), where e=v_q(X). Then

    (a rho^4)^17 = 2 rho^3 Y^2 = beta^17

in R(q,2e). Uniqueness of the root among units gives beta=a rho^4. Consequently

    q^(2e) | b0,b1,b2,b3.                           (4.2)

This includes q=5. All divisions were by units, and all primes with a nontrivial root kernel were excluded in Section 3.

### 4.3 The exponent prime 17, with its loss of exactly one digit

Suppose first that 17 divides Y, and put e=v_17(Y). The algebra R(17,1) is reduced: rho^5-2 has no common root with 5rho^4 in characteristic 17. Frobenius u->u^17 is an automorphism of this finite reduced algebra. A scalar has its unique seventeenth root in the scalar subfield. Thus beta modulo 17 is scalar, and b0 is a 17-adic unit.

Write beta=b0+delta, where delta=b1rho+...+b4rho^4. If delta=0, (Q) forces Y=0, contrary to the hypotheses. Let k be the minimum 17-adic valuation of its nonzero coefficients. Then k>=1. Expand

    beta^17 = b0^17 + 17 b0^16 delta
              + sum_(j=2)^16 binomial(17,j)b0^(17-j)delta^j
              + delta^17.

For 1<=j<=16, binomial(17,j) has valuation one. Each j>=2 term therefore has coefficient valuations at least 1+jk>=k+2; the final term has valuations at least 17k>=k+2. The nonconstant coefficients of the leading term 17b0^16delta have minimum exactly k+1. They cannot be canceled by those higher terms. The nonconstant coefficients of (Q) have minimum 2e, giving

    min_(i=1,...,4) v_17(bi) = 2e-1.               (4.3)

Zero coefficients are assigned valuation infinity in this minimum.

If instead 17 divides X, multiply beta by rho/2=rho^(-4). Set beta'=beta rho/2. Then

    (beta')^17 = Y^2/2^12 + X^2 rho^2/2^14.

The coefficients of beta' are (b4,b0/2,b1/2,b2/2,b3/2). Applying the preceding leading-term argument, with e=v_17(X), shows that b0,b1,b2,b3 are all divisible by 17^(2e-1). Denominators are powers of 2 and are 17-adic units.

The two cases exhaust 17|XY by coprimality. Combining them with (4.1) and (4.2) over all nonexceptional primes proves

    S^2/17 | b1,b2,b3.

In particular the single factor of 17 lost from S^2 is retained explicitly. Treating the seventeenth-power map as an automorphism of principal units at 17 would be wrong.

## 5. The three coefficients cannot all vanish

Suppose b1=b2=b3=0. Write beta=a+b rho^4. The coefficient of rho in its seventeenth power is exactly

    2720 a^3 b^4 (7a^10+1144a^5b^5+512b^10),

and the coefficient of rho^2 is exactly

    2720 a^4 b^3 (a^10+572a^5b^5+896b^10).

These identities follow by selecting, in the binomial expansion, respectively the terms whose rho powers are 1 and 2 modulo 5 and replacing rho^5 by 2. The code and Wolfram also check them exactly.

If a and b are nonzero, put t=a^5/(16b^5). Vanishing of the two coefficients is equivalent to

    14t^2+143t+4 = 0,
     4t^2+143t+14 = 0.

Subtracting gives 10(t^2-1)=0. But the first polynomial has values 161 and -125 at t=1 and t=-1. There is no common root, even over C. The independently computed resultant is -2012500, consistent with this direct proof.

If b=0, the rho^3 coefficient of beta^17 is zero, forcing Y=0. If a=0, beta^17=2^13 b^17 rho^3 has constant coefficient zero, forcing X=0. Both contradict positivity. This proves (2.2), without a sign assumption on a or b.

## 6. All conjugates give a global coefficient bound

Let zeta be a primitive complex fifth root of unity. The five conjugates of beta are

    beta_j = sum_(k=0)^4 bk rho^k zeta^(jk), j=0,...,4.

The element equation, not just its norm, gives

    |beta_j|^17 = |X^2 + rho^8 Y^2 zeta^(3j)|
                <= X^2 + rho^8 Y^2.

Here 2rho^3=rho^8. Define M=(X^2+rho^8Y^2)^(1/17). Fourier inversion on the five roots gives, for every k,

    bk rho^k = (1/5) sum_(j=0)^4 beta_j zeta^(-jk),
    |bk| <= M/rho^k.                               (6.1)

No complex seventeenth-root branch was chosen or discarded; only the absolute values of the actual conjugates were used.

By Sections 4–5 there is an i in {1,2,3} with 0!=bi and Delta|bi. Thus Delta<=|bi|<=M/rho. Since rho>1,

    1+rho^8 < 1+rho^10 = 5 < 8 = rho^15 < rho^17.

Therefore

    Delta^17 <= (X^2+rho^8Y^2)/rho^17
              <= (1+rho^8)T^2/rho^17 < T^2.

This proves (2.3) and hence (2.4).

To see E>1, suppose E=1. Then S=XY>=T, so T^2>(T^2/17)^17, which gives T^32<17^17. But 17|XY implies T>=17, a contradiction. This is an infinite prime-support exclusion for (Q), not a finite experiment.

## 7. Rebuilding the Gaussian divisibility needed for an explicit height

This section rechecks a historical finite restriction for a new purpose: it supplies the numerical input to the global height inequality. It does not relabel the old residue tests themselves as new mathematics.

For (W), X is odd: if X were even, Y would be odd and the left side would have 2-adic valuation 8, impossible for Z^17. Thus Z is odd and gcd(X,16Y)=1. In Z[i], the factors X^5+16iY^5 and its conjugate are coprime. A common odd Gaussian prime would contradict gcd(X,Y)=1; the prime above 2 does not divide the first factor because X is odd. Gaussian unique factorization, with the unit absorbed because eta^17=eta for each Gaussian unit, gives

    X^5+16iY^5=(a+bi)^17,
    gcd(a,b)=1, a odd, b even.

Define the homogeneous degree-sixteen forms

    G(a,b)=sum_(j=0)^8 (-1)^j binomial(17,2j) a^(16-2j)b^(2j),
    H(a,b)=sum_(j=0)^8 (-1)^j binomial(17,2j+1)a^(16-2j)b^(2j).

Then aG=X^5 and bH=16Y^5. Reduction modulo a or b gives gcd(a,G)|17 and gcd(b,H)|17. Also G and H are odd. Modulo 17 they are a^16 and b^16. If 17|a, the last term 17b^16 of G has exact valuation one and all its other terms have higher valuation; similarly 17|b implies v_17(H)=1. They cannot both divide a,b.

Prime valuations in the two factorizations therefore give exactly the following three cases, with signed integer A,B,C,D permitted:

| Case | a | b | G | H |
|---|---|---|---|---|
| I | A^5 | 16B^5 | C^5 | D^5 |
| II | 17^4 A^5 | 16B^5 | 17C^5 | D^5 |
| III | A^5 | 16*17^4 B^5 | C^5 | 17D^5 |

In particular v_2(b)=4+5v_2(Y); no factor at 2 is lost. The fifth powers allow all signs. Case III gives Y=17BD.

### Complete finite certificates

Modulo 11, the full fifth-power image is {0,1,-1}. Testing the displayed cases excludes I and II. In III the only possible projective pair (A:B) is (1:0). The TypeScript checker alternatively uses all distinct fifth-power image pairs without projective normalization; its surviving actual (a,b) pairs for III are (1,0) and (-1,0).

The same Case-III calculation at each prime in

    Pset = {11,31,41,61,71,101,151,191,211,281,331,431,461,631}

again leaves precisely (A:B)=(1:0). It follows that each prime divides B, and hence Y.

The Python/Wolfram projective test is legitimate here: replacing (A,B) by (lambda A,lambda B) multiplies a,b by lambda^5 and G,H by lambda^80=(lambda^16)^5. Therefore membership in the required fifth-power cosets is unchanged. The finite chart A=1 includes B=0, and the chart (0:1) is tested separately. No arbitrary nonsquare denominator is assumed square. The TypeScript full-scale calculation does not use this reduction at all and agrees.

All fourteen primes are 1 modulo 5 and are not 1 modulo 17, so Section 3 proves they are nonexceptional. Their product is

    P = 433992707035920672833426144791.

Since 17|Y as well, S>=17P. Theorem 1 gives

    T^2 > (17 P^2)^17,
    17 P^2 = 3201944385926229974390094081047983998097094024728211239372577.

Exact integer exponentiation verifies

    (17 P^2)^17 > 10^1028.

Consequently T>10^514. The exact integer lower bound floor(sqrt((17P^2)^17))+1 has 515 digits and is stored in `certificate_summary.json`; no floating-point logarithm decides this threshold.

For the exceptional part, (2.4) and XY>=T give E>T^(16/17)/sqrt(17). Substituting the preceding lower bound yields

    E^2 > 17^15 P^32 > 10^966,

where the last comparison is again an exact integer calculation. Thus E>10^483.

## 8. An adversarial check of the new limitation

The exception at q=13 is real. In F_13[rho]/(rho^5-2), the nonscalar element

    eta = 1+7rho+10rho^2+5rho^3

satisfies eta^17=1, while eta!=1. Both implementations verify this explicitly. Therefore beta^17 being scalar modulo 13 does not force beta to be scalar. Extending Section 4's divisibility assertion to every prime would create a false proof; this counterexample blocks that extension.

This is a counterexample to an overbroad local lemma, not a counterexample to (W) or Beal. The product E remains unbounded by this checkpoint. It may be large enough to make (2.4) perfectly consistent. In particular, a very large lower bound is not evidence that no solution exists.

## 9. Computational audit, source scope, and verification status

`code/U68_coefficient_height.py` checks the polynomial coefficient identities with SymPy, enumerates all twenty affine permutations of five roots, derives the complete eleven-class list, and tests it against the actual factorization of rho^5-2 at all 300 primes 3<=q<2000 other than 5 and 17. The finite factorization test corroborates the uniform proof in Section 3; it is not substituted for that proof. It also executes the complete projective Gaussian domains, the explicit q=13 kernel witness, and the large exact integer comparisons.

`code/U68_coefficient_height.ts` uses bigint, direct binomial coefficient extraction, a fraction-free determinant, trial-division primality, and all pairs of fifth-power images without projective normalization. Its integer square root is independently implemented and certified by adjacent-square inequalities. All shared mathematical output agrees exactly with Python. Counts for different domains are labeled rather than forced to be identical.

Wolfram independently reproduces the symbolic coefficient identities, resultant, all fourteen projective residue tests, exceptional classes, and integer threshold comparisons. The full expressions and returned results are retained. This is computational separation, not independent scrutiny of the entire proof.

The reproduction script runs strict TypeScript type checking including unchecked-index and unused-variable checks, both mathematical checkers, Python compilation and tabnanny, then compares their outputs. Bun and a standalone linter are not installed in this runtime; they are not reported as executed. SymPy emits an internal modular-integer ordering deprecation warning during factorization; the warning is preserved in stderr, and it does not change any assertion or output. No package was downgraded and no warning was hidden to obtain a passing result.

The new global proof was reviewed for these failure modes: losing a factor at 17, treating ramified algebras as fields, applying injectivity at an exceptional prime, requiring all embeddings to have a common analytic root branch, ignoring X=1 or Y=1, dropping a projective axis, confusing the product E with its largest prime, and treating a lower bound as a contradiction. The stated proof retains these cases. This is same-model review, not a fresh expert, independent agent, or kernel certificate.

### Dependencies and sources

- **Q65:** `research/checkpoints/U65_weighted_quintic_unit_elimination.md`, remote revision `a15e419765463f68a641ed71fd549aafae2cc95d`, blob `c3b180d626e6434116cc9aed54a6e585b5e0ac28`. The exact inherited implication is (W) => (Q) and 17|XY. U67's pinned manuscript identifies and audits this input; U68 does not claim a fresh replay of its complete unit sieve. Any flaw in Q65 would require withdrawing U68's weighted corollaries until repaired; Theorem 1 with (Q) as an explicit hypothesis would be unaffected.
- **U67:** pinned revision `78255c2e82c19670b9cd5a2b7c44c4cbdca82783`, blob `ae9b53ae03a1dee3f9eccee002831e8255d7a04c`. Sections 0 and 8 supply the precise continuity and next global question. Its two Kummer tests are not assumed as additional hypotheses in Theorem 1.
- **U15/U16:** the historical Gaussian three-case descent and prime list motivated Section 7. Their needed argument is reconstructed and their finite domains are rerun here rather than accepted from their historical status labels.
- The new finite-ring, affine-cycle, binomial and Fourier arguments are proved above. No new unverified literature theorem or database datum is required. Web searches for the exact weighted equation and related sparse quintic formulations did not produce a directly applicable result; that is not evidence of novelty or literature completeness.

## 10. Coverage and the remaining mathematical task

U68 establishes a global obstruction for a specified integral auxiliary system and, through Q65, a quantitative restriction on every putative positive primitive weighted solution. It does not settle the weighted equation, any unbounded remaining Beal exponent family, or the complete conjecture. Seven-of-eight elimination in the separate modular list is unchanged; U41 remains invalidated, (BC) remains unproved, and U61/U62 retain their separate prior status.

The next substantive question is whether the common Gaussian and quintic roots impose a global restriction on the exceptional-prime part E strong enough to oppose (2.4), or supply an effective upper bound for the sparse integral beta. At those exceptional primes, explicit nonscalar seventeenth roots of unity prevent the simple coefficient-divisibility argument. Controlling those choices globally is the missing step; increasing local precision or extending the old finite forcing-prime list does not by itself supply it.
