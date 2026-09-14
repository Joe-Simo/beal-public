# U36: exact sum/difference factorization and coprime low-degree factors

Status: verified partial result only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Setting

Continue from U35 in the valid weighted branch

    X^10 + 256 Y^10 = Z^17.

The surviving Case III data are

    a=A^5,
    b=16*17^4*B^5,
    gcd(a,b)=1,
    G(a,b)=C^5,
    H(a,b)=17 D^5,

with a odd and b even. U15 also established gcd(G,H)=1; hence gcd(C,D)=1 and 17 does not divide C.

Define

    U=(G-H)/2,
    V=(G+H)/2.

Since G and H are odd and coprime,

    gcd(U,V)=1.

Moreover

    U+V=C^5,
    V-U=17 D^5.

## 1. Exact homogeneous factorization

The dehomogenized identities from U35 homogenize to

    G-H = 16 d1 d2 d3 d4,

where

    d1 = b^2-a^2,
    d2 = a^2+b^2,
    d3 = a^4-6a^2b^2+b^4,
    d4 = a^8-28a^6b^2+70a^4b^4-28a^2b^6+b^8,

and

    G+H = 2 s1 s2 s3 s4,

where

    s1 = b^2-3a^2,
    s2 = 3b^2-a^2,
    s3 = b^6-33a^2b^4+27a^4b^2-3a^6,
    s4 = 3b^6-27a^2b^4+33a^4b^2-a^6.

Thus

    U = 8 d1 d2 d3 d4,
    V = s1 s2 s3 s4.

Every d_i and s_i is odd because a is odd and b is even.

## 2. Pairwise gcd structure

Exact Wolfram resultants of the eight homogeneous binary forms with respect to b were computed. After removing powers of a, every pairwise resultant is a power of 2 except the two pairs

    (s1,s3),
    (s2,s4),

whose resultants contain an additional factor 3^2.

In particular, using gcd(a,b)=1 and the fact that all eight evaluated factors are odd:

- d1,d2,d3,d4 are pairwise coprime;
- every d_i is coprime to every s_j;
- among the s_j, the only possible common odd prime is 3;
- 3 can occur simultaneously only in the pair (s1,s3) or only in the pair (s2,s4).

The relevant exact resultant constants include

    Res_b(s1,s3)=2^12*3^2*a^12,
    Res_b(s2,s4)=2^12*3^2*a^12,

while

    Res_b(s3,s4)=2^42*a^36,

and all cross d_i/s_j resultants are powers of 2 times powers of a.

## 3. Exact 3-adic allocation

The possible common factor 3 can be described completely.

If 3|b, then 3 does not divide a and

    v3(s1)=v3(s3)=1,
    3 does not divide s2*s4.

Hence

    v3(V)=2.

If 3|a, then 3 does not divide b and

    v3(s2)=v3(s4)=1,
    3 does not divide s1*s3,

again giving

    v3(V)=2.

If 3 does not divide ab, then b^2/a^2 == 1 (mod 3). In this case

    3 | d1,

while the other seven low-degree factors are nonzero modulo 3. Thus any 3-adic valuation in U is carried entirely by d1=b^2-a^2.

An exact residue computation modulo 27 of the full Case-III equations found no additional restriction: all residue pairs (A,B) are locally compatible because the fifth-power map is an automorphism on the relevant 3-adic unit groups. Therefore the above 3-adic split is structural but not itself contradictory.

## 4. Consequence: an eight-factor primitive decomposition

We now have the simultaneous system

    C^5 = 8 d1 d2 d3 d4 + s1 s2 s3 s4,

    17 D^5 = s1 s2 s3 s4 - 8 d1 d2 d3 d4,

where the four d-factors are pairwise coprime, the d-side is completely coprime to the s-side, and the s-side is pairwise coprime except for the explicitly controlled possible 3^2 overlap.

This is substantially more rigid than the unfactored equations G=C^5 and H=17D^5. It converts the degree-16 forms into products of binary forms of degrees 2,2,4,8 and 2,2,6,6 with essentially disjoint prime support.

## 5. Interpretation of the d-side

The d-factors form a doubling-angle norm tower:

    d1 = b^2-a^2 = -Re((a+ib)^2),
    d2 = a^2+b^2 = Norm_Q(i)/Q(a+ib),
    d3 = Re((a+ib)^4),
    d4 = Re((a+ib)^8).

This explains the exact factorization of G-H and suggests a cyclotomic/norm descent through the 2-power cyclotomic tower. However, U is not known to be a fifth power: it is (C^5-17D^5)/2. Therefore pairwise coprimality alone does not imply that the d_i are fifth powers.

## 6. What was ruled out

The hope that the G±H factorization would immediately split into separate fifth-power equations is false. The products U and V are coprime, but neither product is individually a fifth power. Exact local testing at 3 also gives no contradiction.

The useful output is the primitive eight-factor decomposition and its nearly complete gcd graph.

## Next obligation

Exploit the norm-tower structure rather than merely its gcds. The most concrete next tests are:

1. factor the d3 and d4 pieces as norms in Q(sqrt(2)) and Q(zeta_16)^+, and determine whether a=A^5 and b=16*17^4 B^5 force nontrivial fifth-power ideal classes there;
2. seek a comparable norm interpretation for s1,...,s4 and combine the two towers with U+V=C^5 and V-U=17D^5;
3. if the norm tower does not constrain exponents, pivot to a Frey construction for U^5+8V^5=Z^17.

No Beal subbranch is eliminated by U36 alone.