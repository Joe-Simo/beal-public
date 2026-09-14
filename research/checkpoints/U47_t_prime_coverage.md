# U47: prime-divisor coverage for the all-even right half-exponent t

Status: verified coverage checkpoint only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

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

Branch (B) is the U41 weighted Frey candidate elimination, pending its independent level-lowering/newspace audit.

Branch (A) remains an active unresolved obligation in this repository.

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
2. if 17|t, the problem reduces to the two explicit weighted (5,5,17) equations (A) and (B);
3. if 17 does not divide t, every prime divisor of t is >=19 and the problem enters an unresolved large-right-prime generalized-Fermat family, though modern results give effective asymptotic control for each fixed right prime under explicit conditions.

No statement that `17 must divide t` is currently proved.

## 8. Next actions

Highest-value immediate actions:

1. eliminate (A), X^10+Y^10=2Z^17, using the same 2025 weighted Frey framework already specialized for (B);
2. independently audit U41 so the entire 17-divisible branch can potentially be closed;
3. in parallel, inspect r=19 effective bounds/S-unit computations to determine whether the residual finite range is computationally tractable.
