# U47: prime-divisor coverage for the all-even right half-exponent t

Status: verified coverage checkpoint only. This does not resolve Beal's conjecture.

Date: 2026-09-14; updated 2026-09-16 after U56.

## 1. Setup

Let a primitive all-even Beal candidate satisfy

    A^(2r)+B^(2s)=C^(2t),

with r,s,t>=2 and pairwise coprime positive bases.

U46 proves the t=2 boundary impossible and, together with U45, proves that every prime divisor of r and s is at least 5.

## 2. t is odd

If 2|t, write t=2u. Then

    A^(2r)+B^(2s)=(C^u)^4,

which is exactly the t=2 shape eliminated in U46. Therefore

    2 does not divide t.

## 3. Small odd prime divisors of t are impossible

Suppose a prime p in {3,5,7,11,13} divides t. Choose prime divisors

    l|r, m|s.

By U45-U46, l,m>=5. Write

    X=A^(r/l), Y=B^(s/m), Z=C^(2t/p).

Then

    X^(2l)+Y^(2m)=Z^p.

Anni-Siksek, `Modular elliptic curves over real abelian fields and the generalized Fermat equation x^(2l)+y^(2m)=z^p`, proves no nontrivial primitive solutions for p=3,5,7,11,13 with l,m>=5, with the original p=13 l,m!=7 restriction later completed by Billerey-Chen-Dembele-Dieulefait-Freitas.

Hence no prime in {3,5,7,11,13} divides t.

Combining with oddness:

    every prime divisor of t is at least 17.                 (1)

## 4. The 17-divisible branch

If 17|t, U43 and Michaud-Jacobs imply that at least one of r,s is a positive power of 5. The two Pythagorean orientations reduce exactly to

    X^10+Y^10=2Z^17                                      (A)

or

    X^10+256Y^10=Z^17.                                   (B)

### Branch (A) is now closed

U56 corrects the project's earlier literature record. Freitas' 2012 doctoral thesis, Theorem 2.0.3, proves for beta supported only on primes not congruent to 1 mod 5 that

    x^5+y^5=2 beta z^p

has no non-trivial primitive solutions for p>13 whenever

    p == 1 (mod 4) OR p == +/-1 (mod 5).

This is the strengthened multi-Frey/Q-curve result associated with the later Dieulefait-Freitas Mathematics of Computation article; the old arXiv:1103.5388v1 statement used the narrower AND condition and is not the final result for this application.

In (A), put x=X^2, y=Y^2, beta=1 and p=17. Since 17>13 and 17==1 mod4, the theorem applies. The only positive trivial solution would have X=Y=Z=1, but U43 has X<Y in this orientation. Hence (A) is impossible.

### Branch (B)

Branch (B) is the U41 weighted Frey candidate elimination. Its finite q=11 trace sieve eliminates the recorded norm-2000 Hilbert-newform candidates, but independent certification of the complete newspace inventory and the adapted level-lowering bridge remains open. Therefore (B) is not yet counted as independently verified closed.

## 5. If 17 does not divide t

By (1), every prime divisor of t is then at least 19. Taking any prime p|t and any prime divisors l|r,m|s reduces the original all-even candidate to

    X^(2l)+Y^(2m)=Z^p,

where

    l,m>=5 primes,
    p>=19 prime.

This is a genuine residual generalized-Fermat family. No theorem found in the current literature audit completely resolves all such signatures.

## 6. Current 2025 asymptotic result

Satyabrate Sahoo, `Effective Generalized Fermat equation of signature (2p,2q,r) with odd narrow class number`, arXiv:2509.21083 (2025), studies

    x^(2p)+y^(2q)=z^r

for fixed prime r>=5 and varying primes p,q>=5.

For r=19 the paper verifies criteria implying the existence of an effectively computable constant V_19 such that there are no nontrivial primitive solutions when the two varying primes exceed V_19, treating both 19|a and 19 not dividing a through its two main local/S-unit criteria.

Crucially, this is an asymptotic/effective theorem, not a complete solution for r=19:

- the paper does not provide a blanket elimination of all p,q>=5;
- the finite range p<=V_19 or q<=V_19 still requires explicit treatment;
- therefore r=19 cannot currently be removed from the Beal coverage ledger by citation alone.

The same caution applies a fortiori to the full family of right primes >=19.

## 7. Coverage status

The all-even branch is now partitioned rigorously as follows:

1. t has no prime divisor below 17;
2. if 17|t, orientation (A) is closed by U56 and only the weighted orientation (B) remains, with U41 a serious but not independently certified candidate elimination;
3. if 17 does not divide t, every prime divisor of t is >=19 and the problem enters an unresolved large-right-prime generalized-Fermat family, though modern results give effective asymptotic control for each fixed right prime under explicit conditions.

No statement that `17 must divide t` is currently proved.

## 8. Next actions

Highest-value immediate actions:

1. independently certify U41 so the entire `17|t` all-even branch can be closed;
2. inspect the r=19 effective bounds/S-unit computations to determine whether the residual finite range is computationally tractable;
3. keep U48-U55 as independent arithmetic work but do not spend further effort on the coefficient-2 orientation unless auditing U56 reveals a source/application flaw.
