# U39: cyclotomic allocation of J-primes and exact 2,5,17 valuations

Status: verified partial result only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Setting

Continue from U38 in the valid weighted branch

    X^10 + 256 Y^10 = Z^17.

The surviving Case III data are

    a=A^5,
    b=16*17^4*B^5,
    gcd(A,B)=1,
    G(a,b)=C^5,
    H(a,b)=17 D^5,

with gcd(C,D)=1. U38 proves

    (C-D) Phi_5(C,D) = -2^13 * 17^7 * B^10 * J(a,b),

where

    Phi_5(C,D)=C^4+C^3D+C^2D^2+CD^3+D^4,

and

    J(a,b)=51 a^14 -1071 a^12 b^2 +5967 a^10 b^4
           -12155 a^8 b^6 +9945 a^6 b^8
           -3213 a^4 b^10 +357 a^2 b^12 -9 b^14.

U38 also establishes gcd(C-D,Phi_5(C,D))=5.

## 1. Allocation theorem for odd J-primes

Let q be an odd prime with q != 5 and q | J(a,b). U38 shows q does not divide CD outside the fixed exceptional primes 2 and 17, so for q !=17 the ratio C/D is defined modulo q.

Because q divides the right side above, q divides C^5-D^5. Hence

    (C D^{-1})^5 == 1 (mod q).

If q is not congruent to 1 modulo 5, then F_q^* has no nontrivial fifth roots of unity. Therefore

    C D^{-1} == 1 (mod q),

and so

    q | C-D.

Equivalently:

> For q != 5,17 dividing J(a,b), a prime can divide Phi_5(C,D) only if q == 1 (mod 5).

This is the standard cyclotomic allocation phenomenon in the present explicit setting.

Conversely, q == 1 mod 5 is only a necessary condition for q | Phi_5(C,D), not a sufficient one. Such a q may still divide C-D.

## 2. Exact valuation at 5

U38 gives

    v5(C-D)=10 v5(B)-1.

Since 5|B by U37 and 5 does not divide CD, the usual LTE calculation gives

    v5(Phi_5(C,D))=1.

Taking 5-adic valuations in the U38 identity therefore gives

    [10 v5(B)-1] + 1
      = 10 v5(B) + v5(J).

Hence

    v5(J(a,b))=0.

This also follows directly from the explicit form: because 5 does not divide a,

    J(a,b) == 51 a^14 == a^14 (mod 5).

Thus J is a 5-adic unit in every hypothetical global solution.

## 3. Exact valuation at 17

Since 17 is not congruent to 1 modulo 5, 17 cannot divide Phi_5(C,D) when gcd(C,D)=1 and 17 does not divide D. U38 gives

    v17(C-D)=8+10 v17(B).

Taking 17-adic valuations in the same identity yields

    8+10 v17(B)
      = 7 + 10 v17(B) + v17(J),

so

    v17(J(a,b))=1.

This is also visible directly: 17 does not divide a and 17^4|b, so all b-dependent terms of J have 17-adic valuation at least 8, while the leading term is

    51 a^14 = 3*17*a^14.

Therefore the 17-adic valuation is exactly one.

## 4. Exact valuation at 2

Both C and D are odd, because G and H are odd. Hence Phi_5(C,D), being the sum of five odd terms, is odd.

Also a is odd and b is even, so

    J(a,b) == 51 a^14 == 1 (mod 2),

and J is odd.

Therefore the full 2-adic valuation on the right side of

    (C-D)Phi_5(C,D)
      = -2^13*17^7*B^10*J

lies in C-D. Thus

    v2(C-D)=13+10 v2(B).

Together with U38 this gives sharp valuations at three distinct rational primes:

    v2(C-D)=13+10v2(B),
    v5(C-D)=10v5(B)-1,
    v17(C-D)=8+10v17(B).

## 5. The q == 1 mod 5 branch is locally genuine

A finite-field test was run to check whether the special shape

    t=b^2/a^2 = 2^8*17^8*(B/A)^10

plus the two fifth-power requirements

    g(t) is a fifth power,
    h(t)/17 is a fifth power

forces away J-roots at primes q == 1 mod 5.

It does not.

For primes tested through roughly 3000, local compatible examples occur at q == 1 mod 5, including q=2081 and q=2801. Thus no claim is made that every J-prime must lie in C-D. The q == 1 mod 5 possibility for Phi_5 is a real local branch.

The dehomogenized J-polynomial

    j(t)=51-1071t+5967t^2-12155t^3+9945t^4-3213t^5+357t^6-9t^7

is irreducible over Q and remains irreducible over Q(sqrt(5)) and Q(zeta_5) in exact Wolfram factorization. Therefore there is no immediate factorization over the fifth cyclotomic field that would separate the two allocation branches.

## 6. Consequence

The U38 identity now has a precise arithmetic interpretation:

- every prime q !=5,17 dividing J with q not congruent to 1 mod5 goes entirely into C-D;
- only q ==1 mod5 may enter Phi_5(C,D);
- J itself contributes no 5-adic valuation and exactly one factor of 17;
- C-D has exact valuations at 2,5,17 as displayed above.

This strengthens the rational descent substantially, but it does not yet force a contradiction because J can have moving q ==1 mod5 prime support.

## Verification record

- The allocation argument is elementary from the order of C/D in F_q^*.
- Exact Wolfram checks verified the irreducibility of j(t) over Q, Q(sqrt(5)), and Q(zeta_5).
- Exact finite-field scans imposed simultaneously: j(t)=0, the tenth-power coset condition on t, and both fifth-power conditions for g(t) and h(t)/17. The scan exhibited compatible primes q ==1 mod5, so the simple congruence-class elimination route is closed.

## Next obligation

The remaining difficult branch is now sharply localized: q == 1 mod 5 prime divisors of J that may enter Phi_5(C,D). The next useful attack is to study these primes via fifth-power residue symbols / reciprocity using the special tenth-power parameter t, or to derive an independent factorization of J that controls exactly those q ==1 mod5 primes. If that route yields no restriction, pivot to a Frey construction for U^5+8V^5=Z^17.
