# U42: rebuilt coverage ledger from preserved evidence

Status: verified coverage checkpoint only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## 1. Exact target

A primitive counterexample is a positive-integer solution

    A^x + B^y = C^z,
    x,y,z >= 3,
    gcd(A,B,C)=1.

For such a solution the bases are pairwise coprime: if a prime divides two bases, the equation forces it to divide the third.

A base equal to 1 is impossible. For example A=1 would give C^z-B^y=1 with y,z>=3, contradicting the Catalan-Mihailescu theorem (the unique nontrivial consecutive perfect powers are 3^2 and 2^3). C=1 is impossible by positivity.

## 2. Universal exponent reduction

For every integer n>=3 there is a divisor d of n such that d is either 4 or an odd prime:

- if 4|n, take d=4;
- otherwise n has an odd prime divisor.

Therefore from any primitive Beal solution one may replace each base by a positive integral power and reduce the corresponding exponent independently. For example, if d_x|x, then

    A^x = (A^(x/d_x))^d_x.

The transformed bases remain pairwise coprime. Hence it is enough to rule out primitive solutions for exponent signatures

    (e1,e2,e3),   ei in S := {4} union {odd primes}.

This is a rigorous infinite reduction, not a finite list.

If gcd(x,y,z) has a divisor d>=3, then

    (A^(x/d))^d + (B^(y/d))^d = (C^(z/d))^d,

contradicting Fermat's Last Theorem. Thus any primitive counterexample has gcd(x,y,z) in {1,2}. Equivalently, in the reduced S^3 ledger all diagonal signatures are already impossible.

These observations still leave infinitely many mixed signatures, including triples of distinct odd primes, signatures involving one or two exponents 4, and signatures arising from original gcd(x,y,z)=2.

## 3. What the preserved U15-U41 chain actually proves

The repository currently begins the all-even specialized chain at U15. U15 explicitly states, but does not prove in that file:

    "For the surviving all-even branch with 17 | t and r a positive power of 5, prior reduction gives ...
     X^10 + 256 Y^10 = Z^17."

Thus U15-U41 do not by themselves prove that every relevant all-even Beal solution reaches the weighted equation. The missing U1-U14 derivations are not present on main and were not found by repository search.

U15-U39 rigorously analyze the weighted equation once it is assumed. U40-U41 develop a direct weighted Frey route for the equivalent equation

    U^5 + 8 V^5 = Z^17,

where U=X^2 and V=2Y^2.

U41's corrected computation gives a candidate elimination of this weighted equation through a norm-2000 Hilbert-newform space over Q(sqrt(5)) and a q=11 trace sieve. That modular argument still requires an independent audit/reproduction of the level-lowering adaptation and newspace computation before this weighted subproblem is marked independently verified.

Accordingly, U41 is NOT presently credited as eliminating the complete all-even branch in the global Beal coverage ledger.

## 4. Published theorem that can be credited directly

Philippe Michaud-Jacobs, "On some generalized Fermat equations of the form x^2+y^{2n}=z^p", Mathematika 68 (2022), proves in particular that

    X^(2*l) + Y^(2*m) = Z^17

has no nonzero coprime integer solutions when l and m are primes different from 5.

This is a genuine published elimination for those exact generalized-Fermat signatures. It does not cover l=5 or m=5, and it does not by itself prove the missing all-even reductions recorded only by summary in the previous project state.

## 5. Reconstructed elementary all-even entry point

Suppose a primitive Beal solution has x=2r, y=2s, z=2t. Then

    (A^r)^2 + (B^s)^2 = (C^t)^2.

Exactly one of A^r,B^s is even. After interchanging the two left terms if needed, primitive Pythagorean parametrization gives coprime m>n of opposite parity such that

    A^r = 2mn,
    B^s = m^2-n^2,
    C^t = m^2+n^2.

Since m-n and m+n are coprime odd integers whose product is B^s,

    m-n = u^s,
    m+n = v^s

for coprime odd u<v. Since 2mn=A^r and gcd(m,n)=1, one of m,n is an r-th power and the even one is 2^(r-1) times an r-th power (with any extra 2^r absorbed into the base). Thus for coprime positive a,b,

    {m,n} = {a^r, 2^(r-1)b^r},

and hence

    {v^s+u^s, v^s-u^s} = {2a^r, 2^r b^r}.

This part of the former U5-U6 chain is now reconstructed directly and does not depend on a missing file.

What is NOT yet reconstructed here are the later restrictions formerly attributed to U7-U14: the exact exclusions on prime divisors of r,s,t, the proof that 17|t forces one of r,s to be a power of 5, and the final orientation argument yielding X^10+256Y^10=Z^17. Those claims must be rebuilt from primary sources before they count globally.

## 6. Current global coverage status

Proved/unconditional in the present ledger:

1. Primitive bases are pairwise coprime and bases equal to 1 are impossible.
2. Every exponent may be reduced to 4 or an odd prime while preserving a primitive solution.
3. gcd(x,y,z) cannot have a divisor >=3; hence gcd(x,y,z) is 1 or 2.
4. The elementary Pythagorean structure above holds for every all-even primitive solution.
5. The published Michaud-Jacobs theorem eliminates the exact signatures X^(2*l)+Y^(2*m)=Z^17 for primes l,m !=5.

Strong candidate partial result, not yet independently certified:

6. U41 eliminates the weighted equation X^10+256Y^10=Z^17 using a corrected weighted Frey genus-2 representation and the q=11 Hilbert-newform sieve.

Not yet covered:

- the missing theorem chain connecting the complete all-even branch to the U41 weighted equation;
- all all-even cases not proved to enter that chain;
- general mixed-parity exponent signatures;
- reduced signatures with exponent 4;
- triples of distinct odd prime exponents;
- most signatures with two equal exponents outside the published solved families;
- the complete original Beal conjecture.

## 7. Priority next action

Reconstruct the missing all-even source chain before starting another narrow subcase. In particular:

1. establish or refute the claimed restrictions on r,s,t from the cited Anni-Siksek / Bennett-Chen-Dahmen-Yazdani / Billerey-et-al. results;
2. verify exactly when Michaud-Jacobs Theorem 3 forces one of r,s to be a power of 5 if 17|t;
3. reconstruct the orientation that yields either the unweighted equation X^10+Y^10=2Z^17 or the weighted equation X^10+256Y^10=Z^17;
4. only then credit U41 against the global all-even coverage.
