# U60 — audited descent and a modulo-289 square-class elimination

**Status: an established partial implication with explicit algebraic and computational certificates; not a complete solution of Beal's conjecture.**

Run date: 2026-09-14 America/New_York / 2026-09-15 UTC.
Inspected base revision: `0c4ca34375b87ab3b41e26cd7ee14bfcfdecba92` in private `Joe-Simo/beal`.
Review provenance: Astra self-review, exact TypeScript bigint and Python/SymPy checks, and separate Wolfram computations. No independent human review or proof-assistant kernel verification is claimed. Novelty is not claimed.

## 1. Scope and exact result

The original target remains: for positive integers A0,B0,C0,x,y,z with x,y,z >= 3 and A0^x+B0^y=C0^z, prove gcd(A0,B0,C0)>1 or produce an exactly verified counterexample. Nothing below replaces that target.

This checkpoint concerns only the simultaneous equations in the current auxiliary branch. Write omega=(1+sqrt(5))/2, with omega^2=omega+1, and

    H_-(m,n) = m^4+30m^2n^2+n^4 - 16m^2n^2 omega.

Suppose coprime integers r,s of opposite parity and integers m,n,A,B satisfy

    m+i n = (r+i s)^17,
    H_-(m,n) = (A+B omega)^17,
    gcd(m,n)=gcd(A,B)=1,
    mn != 0.

Here A,B are algebraic-integer coefficients, NOT the original Beal bases A0,B0.
A Gaussian unit can be absorbed into r+i s, because its 17th power equals itself. This preserves coprimality and opposite parity.

**Partial theorem.** Exactly one of r,s is divisible by 17. If k=v_17(rs), then k>=1 and

    v_17(mn)=k+1,
    v_17(B)=2k+1.

Consequently the square class B=-b^2 is impossible, and every such solution has

    B=-17 b^2,
    P16(A,-17 b^2)=17 c^2,
    17 b c=4|mn|,
    gcd(b,c)=gcd(A,b)=1,
    17|b,  17 does not divide c,  8|b,

for positive integers b,c. The previously established 103|mn condition additionally implies 103|b and 103 does not divide c, by the corrected argument in section 2.

For the upstream positive auxiliary variables X=m+n,Y=m-n, this also gives 289 | (X^2-Y^2). The theorem is an implication for the displayed system, not an assertion that all Beal signatures reach it.

Boundary: mn=0 is expressly separated, not discarded silently. For primitive m,n it is the axis case {abs(m),abs(n)}={1,0}; in the positive X,Y orientation this is X=Y=Z=1. The square-class argument divides nonzero quantities and is not applied to this case.

## 2. Audit corrections to U57–U59

### U57/U58: division does not preserve being a square

The assertion that t=b^2/A is necessarily a quadratic residue is unjustified. An explicit counterexample to that inference is A=57, b=8, q=103: A=1 mod8, gcd(A,b)=1, but b^2/A=21 mod103 and 21^51=-1 mod103. This is NOT a solution of the branch; it refutes the proposed normalization under the stated local hypotheses.

Moreover A can vanish modulo q even when B is nonzero. The safe root question, when B is a unit, is to enumerate every t=A/B in F_q, not just squares. The remaining projective point is (A:B)=(1:0).

The complete corrected numbers of roots of P16(t,1), over ALL t in F_q, are:

    q=67: 16; q=103: 0; q=409: 16; q=883: 16.

None has a root at (1:0), since P16(1,0)=17.
Full lists are in U60_typescript_output.json. U58's old 7/8-element lists are valid outputs for restricted scans but are NOT complete necessary-condition tables. They must not be used to prune all integer solutions.

**U57's conclusion is recovered with a corrected proof.** If 103 divides P16 and B is nonzero modulo 103, then P16(A/B,1)=0, contradicting the complete root enumeration. If B=0 modulo 103, coprimality makes A a unit, and P16=17 A^16 is nonzero. Therefore 103 never divides P16 for primitive A,B. From B P16=-16m^2n^2 and 103|mn, all the 103-adic contribution lies in B. Its valuation is 2v_103(mn), and v_103(b)=v_103(mn).

### U59: distinguish scalar and projective kernels

For the quadratic algebra over an odd q!=5, its unit group modulo scalar units has order q-(5/q). At q=103 the discriminant 5 is nonsquare and this order is 104, coprime to 17. Thus the projective 17th-power kernel at 103 has size ONE, not 17. The factor 17 in gcd(17,103^2-1) comes from scalar units and does not survive quotienting. At 67,409,883 the projective kernel does have size 17. U59's single-valued-map objection at those three primes survives, but its uniform explanation including 103 was incorrect.

### U59: q^2 is still too shallow for the proposed coefficient test

If e=v_q(mn)>=1 and q is odd, v_q(-16m^2n^2)=2e. That coefficient remains zero modulo q^2; for e=1 its first nonzero digit is seen modulo q^3, not q^2. Section 5 goes further and constructs solutions of the surviving local equations to all orders at these primes, so merely lifting them indefinitely is not a justified route to a contradiction.

### Upstream dependencies actually rechecked

The exact P16 coefficients were regenerated from omega^2=omega+1. The U51 sieve was rerun over all nonzero Gaussian 17th powers in the full algebra at 67: k=0 and k=15 each have 132 compatible pairs, all other k have none. At 409 a full split-algebra enumeration, retaining scalar data, gives 48 compatible pairs for k=0 (all on axes) and none for k=15. This reproduces the finite sieves supporting the untwisted equation. It is not a fresh verification of every external theorem in U46 or the entire global coverage ledger.

## 3. Algebraic certificate modulo 17^2

In any commutative integer algebra,

    (a+17b)^17 = a^17 (mod 289).

Thus every 17th power modulo 289 is determined by the base modulo 17. This proves the completeness of enumerating 289 residue pairs, including zero coordinates; it is not a heuristic search bound.

A sharper certificate avoids relying solely on the table. Suppose first that s is a unit modulo 17. Divide the Gaussian base by s modulo 289 and the quadratic-field root by s^4. This is legitimate because H_- has degree four and s^68=(s^4)^17. Reduce the resulting Gaussian parameter modulo 17 to t. This does not change its 17th power modulo 289. This normalization concerns a power equation, not a square-class test on a chosen projective representative.

Put

    M(t)=Re((t+i)^17), N(t)=Im((t+i)^17).

In characteristic 17, i^17=i and omega^17=1-omega. Hence any candidate root of H_-(M(t),N(t)) must reduce modulo 17 to

    alpha0(t)=(t^4+14t^2+1)+16t^2 omega.

All lifts of alpha0 have the same 17th power modulo 289. Let D(t) be the omega coefficient of

    H_-(M(t),N(t)) - alpha0(t)^17.

Every coefficient of D is divisible by 17. Exact polynomial arithmetic yields, in F_17[t]/(t^17-t),

    D(t)/17 = t^4 R(t^2),
    R(y)=y^6+4y^5-y^4+3y^3-y^2+4y+1.

The following explicitly checkable Bezout identity holds in F_17[y]:

    U(y)R(y) + V(y)(y^8-1) = 1,

where

    U=y^7+y^6-y^5+y^4+y^3-y^2-4y-1,
    V=-y^5-5y^4-2y^3+y^2-8y-2.

For t!=0, Fermat's elementary finite-field identity gives (t^2)^8=1. The Bezout identity then forbids R(t^2)=0. Therefore the necessary condition D(t)=0 mod289 forces t=0. This proves 17|r whenever 17 does not divide s. If 17 divides s, primitivity already puts the pair on the other axis. Both cannot vanish modulo 17.

The full independent table gives exactly the same classification: 288 primitive Gaussian residue pairs tested, 32 compatible pairs, precisely (0,s) and (r,0) for nonzero r,s in F_17. No norm-zero or coordinate-zero residue was silently removed.

## 4. Valuations and the surviving square class

Expand the Gaussian coordinates as m=rF(r,s), n=sG(r,s). If 17|r and 17 does not divide s, then

    F(r,s)=17s^16 + terms divisible by 17^3,
    G(r,s)=s^16 (mod17).

(The first assertion uses r^2 in every nonconstant term of F except r^16; all the corresponding binomial coefficients are divisible by 17.) Hence v_17(mn)=v_17(r)+1. The other axis is symmetric.

Define P16 by

    (A+B omega)^17 = P0(A,B)+B P16(A,B) omega.

Its coefficients are generated by

    P16(A,B)=sum_{j=1}^{17} binom(17,j) Fibonacci(j) A^(17-j) B^(j-1).

Then B P16=-16m^2n^2 and P16=17A^16 mod B, so gcd(B,P16)=gcd(B,17) for gcd(A,B)=1. Also P16>0 for real A,B with B!=0: it is (alpha^17-alpha'^17)/(alpha-alpha'), positive because the real seventeenth-power function is strictly increasing. Thus B<0.

The modulo-17 equation gives B=0 mod17, since the omega coefficient of alpha^17 is -B and 17|mn. Coprimality makes A a unit at 17. In P16, the first term 17A^16 has valuation one and every other term has larger valuation. Thus v_17(P16)=1 and

    v_17(B)=2v_17(mn)-1=2k+1.

At every other prime the coprime factors B and P16 have even valuations, because their product is minus a square. Hence B=-17b^2, P16=17c^2, with 17 not dividing c and v_17(b)=k>=1. Taking absolute values gives 17bc=4|mn| and gcd(b,c)=1.

For completeness, opposite parity gives H_-=1 modulo 8 in Z[omega]. Its unit group modulo 8 has order 48, so exponentiation by 17 is bijective. Therefore A=1 mod8 and B=0 mod8. The form P16 is odd, giving v_2(B)=4+2v_2(mn), and hence v_2(b)=2+v_2(mn)>=3. This proves 8|b without assuming the earlier sign scan.

## 5. Executed next test: the remaining class has local lifts

The following is a limit of this local route, not evidence for an integer counterexample.

For each q in {67,103,409,883}, take r=1,s=q in Z_q. The Gaussian equation gives m=1 mod q and n=0 mod q. The map alpha -> alpha^17 on the quadratic algebra has derivative 17 times multiplication by alpha^16. At alpha=1 its two-coordinate Jacobian is 17I, invertible at these q. Consequently the equation alpha^17=H_-(m,n) has a unique solution alpha=1 mod q, by Hensel lifting.

For the new class delta=17, P16/17=1 mod q, so choose its square root c=1 mod q. Put b=4mn/(17c). The coefficient equation implies B=-17b^2 exactly in Z_q, and b has valuation one. Thus the simultaneous Gaussian equation, quadratic-field equation, and surviving square class have local solutions at every power of each of these primes.

At q=17 the same family r=1,s=17 also lifts. Here H_-=1 mod17^3. Substitute alpha=1+17z and divide the equation by 17^2. The polynomial

    ((1+17z)^17-1)/17^2

is integral and equals z modulo 17, so its Jacobian is the identity modulo 17. This gives the root. Then P16/17 is a unit congruent to 1, and b=4mn/(17c) is integral with valuation one. The other exact valuations are v_17(mn)=2, v_17(B)=3, v_17(c)=0.

Actual compatible residues modulo q^6 were constructed for all FIVE q in {17,67,103,409,883}; each of the Gaussian, quadratic, B-square, P-square, product, and norm congruences passed. Wolfram separately recomputed the Gaussian powers, quadratic powers, and square/product equations on the full integer residues. The q=883 modulus is 473984589097059769, larger than binary64's safe-integer range; no floating-point comparisons were used. Full residues are in U60_python_output.json.

Hensel reference checked: Keith Conrad, *Hensel's Lemma*, Theorem 2.1, pp.1-3; *A Multivariable Hensel's Lemma*, Theorem 3.3, p.3. The maps and invertible derivatives above are this checkpoint's applications, not claims made about Beal in those sources. The lifting argument may also be checked directly one digit at a time, as in the code.

These local solutions do not show global integer solutions exist. Conversely, the constraints at these five primes alone cannot yield the proposed empty intersection: compatible finite-precision systems persist, and the Chinese remainder theorem combines their residues. Additional global arithmetic is needed for this route.

## 6. A concrete global model, derived and checked

The involution alpha <-> alpha' sends A/B to -1-A/B. Set T=2A+B. Direct binomial expansion gives

    2^16 P16(A,B)=sum_{j=0}^{8} binom(17,2j+1)5^j T^(16-2j) B^(2j).

For B!=0 put x=(T/B)^2 and Y=256c/B^8. The remaining equation implies

    f8(x)=17Y^2,

    f8(x)=17x^8+3400x^7+154700x^6+2431000x^5
          +15193750x^4+38675000x^3+37187500x^2
          +10625000x+390625.

Its discriminant is 2^112*5^56*17^7, nonzero. The degree-two map to the x-line is branched at its eight simple roots, giving genus three by Riemann-Hurwitz. The polynomial identity, squarefreeness and discriminant were checked exactly with SymPy. This is a necessary quotient model, not an equivalence: x must itself be a rational square, and reconstruction must retain B=-17b^2, primitivity and the original Gaussian equations. Those constraints must not disappear in a rational-point calculation.

**Next mathematical action:** investigate the rational points of this explicit genus-three quotient (and the square/reconstruction conditions), rather than repeatedly increasing precision at the same five primes. No Jacobian rank, rational-point completeness bound, or emptiness theorem for this curve has been established in this run.

## 7. Reproduction, limits and current state

Commands actually completed from the repository root:

    tsc code/U60_audit.ts --target ES2022 --module commonjs --strict --noUncheckedIndexedAccess --noUnusedLocals --noUnusedParameters --noEmit
    tsc code/U60_audit.ts --target ES2022 --module commonjs --strict --noUncheckedIndexedAccess --noUnusedLocals --noUnusedParameters --outDir .build
    node .build/U60_audit.js
    python -m py_compile code/U60_symbolic.py
    python code/U60_symbolic.py

Environment: Node 22.16.0, TypeScript 5.8.3; Python and SymPy versions are in the Python output. The TypeScript checker includes the original Beal specification's zero, negative, noninteger, exponent-two, nonprimitive-equality, arithmetic-mismatch, base-one and beyond-safe-integer tests. These tests are not discoveries.

Lint limitation: an attempt to acquire/run Biome 2.3.11 timed out after 45 seconds; an offline retry returned ENOTCACHED. No linter success is claimed. Strict TypeScript checks and executed arithmetic assertions passed. No Lean, Lake or Sage executable was present. Mathbox discovery returned no available plugin in this session; no Mathbox audit or independent expert audit is claimed.

A first Wolfram table implementation encountered its 0^0 convention and incorrectly returned 273 alpha images. That run was discarded. The corrected evaluator explicitly defines the polynomial zero-exponent convention and returns all 289 images. The proof certificate and full table were separately rerun successfully. Preserve this failure as an implementation issue, not mathematical evidence.

Official-status check: the AMS prize page and rules page could not be retrieved in this run. The UNT page still displays the exact conjecture and $1,000,000 offer; this is not proof of a fresh AMS adjudication or award. No award or eligibility certification is claimed.

Strongest new result: one of the two square classes of the explicitly assumed auxiliary system is eliminated by the modulo-289 algebraic certificate. The other survives the tested local conditions to all orders. No original Beal exponent signature is newly certified empty by this checkpoint; the full conjecture, publication and prize remain separate unresolved milestones.

Sources inspected:
- https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf
- https://kconrad.math.uconn.edu/blurbs/gradnumthy/multivarhensel.pdf
- https://sites.math.unt.edu/~mauldin/beal.html
- Repository U46 (coefficient-2 branch), U48-U59, and U42 coverage checkpoint at the inspected base revision. External dependencies in older notes were not silently promoted to freshly verified facts.
