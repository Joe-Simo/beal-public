# U55: coefficient-2 branch — direct Q(zeta_20) descent and unit-class collapse

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-16.

## 1. Direct cyclotomic norm hidden in the second factor

Let zeta be a primitive 20th root of unity and M=Q(zeta). The second factor in U46 is

    Phi = X^8-X^6Y^2+X^4Y^4-X^2Y^6+Y^8 = v^17.

Since

    Phi_20(T)=T^8-T^6+T^4-T^2+1,

we have the exact norm identity

    Norm_{M/Q}(Y+X zeta)=Phi=v^17.                 (1)

The eight conjugate linear factors Y+X zeta^a, a in (Z/20Z)^*, are pairwise coprime as ideals.
Indeed, a common prime ideal divisor of two distinct factors divides X(zeta^a-zeta^b); it cannot divide X because gcd(X,Y)=1, and root-of-unity differences here are supported only above 2 or 5. But Phi is odd and 5 does not divide Phi by U46, so primes above 2 and 5 do not divide any factor.

The cyclotomic field Q(zeta_20) has class number 1 (Masley-Montgomery, `Cyclotomic fields with unique factorization`, J. Reine Angew. Math. 286/287 (1976), 248-256; conductor 20 is on their class-number-one list).

Therefore each linear factor is a 17th power ideal and hence

    Y+X zeta = epsilon * Gamma^17                 (2)

for a unit epsilon of O_M.

Roots of unity cause no ambiguity modulo 17th powers because gcd(17,20)=1.

## 2. Unit classes modulo 17th powers

Let L=M^+=Q(zeta+zeta^{-1})=Q(zeta_20)^+. The full and real unit groups have the same rank 3, and the Hasse unit index [E_M : mu_M E_L] is 1 or 2. Since this index is coprime to 17, real units generate E_M/E_M^17 after roots of unity are ignored.

Use the normalized real generator a=zeta+zeta^{-1}, satisfying

    a^4-5a^2+5=0.

A fundamental-unit basis for L is

    e1=a^2-3,
    e2=a^3+a^2-3a-3,
    e3=a^2-a-2.

Thus modulo 17th powers we may write

    epsilon == e1^j1 e2^j2 e3^j3,
    (j1,j2,j3) in F_17^3.

## 3. Exact q=1021 unit sieve

The first factor descent U48 also gives

    m+i n = Gaussian-unit * (r+i s)^17,

with

    m=(X+Y)/2,
    n=(X-Y)/2.

At q=1021, both -1 and all 20th roots split, and 17 divides q-1. The eight roots of Phi_20 modulo 1021 are exactly

    226, 250, 384, 486, 535, 637, 771, 795.

For each of these eight residue embeddings, take the 17th-power residue character of e1,e2,e3. Exact Wolfram finite-field arithmetic gives the 8x3 matrix

    [ 5, 6, 0 ]
    [12, 0,11 ]
    [ 5,11, 0 ]
    [12, 0,11 ]
    [12, 0, 6 ]
    [ 5, 6, 0 ]
    [12, 0, 6 ]
    [ 5,11, 0 ].

Its rank over F_17 is 3, so reduction at this one rational prime detects all three global unit exponents modulo 17.

Next enumerate the Gaussian 17th-power projective possibilities coming from m+i n. There are 62 residue-character vectors for Y+X zeta compatible with that Gaussian condition.

Testing all 17^3 unit exponent triples in (2) leaves exactly

    (j1,j2,j3)=(9,8,9)
    or
    (j1,j2,j3)=(9,9,8).                            (3)

This was reproduced directly in Wolfram; no floating-point arithmetic is involved.

## 4. The two surviving classes are the trivial cyclotomic units

At the same eight residue embeddings, the character vector of zeta-1 equals the character vector of

    e1^9 e2^8 e3^9,

and the character vector of 1+zeta equals that of

    e1^9 e2^9 e3^8.

Because the unit-character matrix above has rank 3, these local equalities identify the corresponding global classes in E_M/E_M^17.

Hence (2) sharpens globally to exactly one of

    Y+X zeta = (1+zeta) Gamma^17,                  (4+)

or

    Y+X zeta = (zeta-1) Gamma^17.                  (4-)

All other unit classes are impossible.

The original Diophantine equation is invariant under X -> -X. Applying the automorphism zeta -> -zeta to (4-) and replacing X by -X converts it to the plus form, with -1 absorbed as a 17th power. Therefore, up to this legitimate sign symmetry, we may work with the single exact equation

    Y+X zeta = (1+zeta) Gamma^17.                  (5)

## 5. A very simple 17th-power equation in m,n

Using X=m+n and Y=m-n,

    Y+X zeta
      = m(1+zeta)+n(zeta-1).

Since 1+zeta is a unit,

    (Y+X zeta)/(1+zeta)
      = m + mu n,

where

    mu=(zeta-1)/(zeta+1).

Thus the surviving coefficient-2 branch satisfies the exact untwisted cyclotomic equation

    m + mu n = Gamma^17                              (6)

in Q(zeta_20), in addition to

    m+i n=(r+i s)^17

in Z[i].

The q=1021 sieve shows that in the plus orientation (6),

    1021 | n,
    1021 does not divide m.

Without choosing the sign orientation, the invariant statement is 1021|mn.

## 6. Two lower-degree relative norm descents

Taking the relative norm of (1) to Q(i) gives the exact identity

    R+iS = Norm_{M/Q(i)}(Y+X zeta),

where

    R = X^4-X^2Y^2+Y^4,
    S = XY(X^2-Y^2),

and

    R^2+S^2 = Phi = v^17.

Since gcd(R,S)=1, R is odd and S is even, Gaussian UFD gives

    R+iS=(C+iD)^17                                  (7)

with coprime C,D.

Likewise the subgroup fixing Q(sqrt(-5)) gives

    E + sqrt(-5) S = Norm_{M/Q(sqrt(-5))}(Y+X zeta),

where

    E = X^4-3X^2Y^2+Y^4,

and

    E^2+5S^2=Phi=v^17.

The ring Q(sqrt(-5)) has class number 2. The two conjugate ideals are coprime; since gcd(17,2)=1, an ideal whose 17th power is principal is itself principal. Its only units are +/-1, both absorbed for odd exponent 17. Therefore

    E+sqrt(-5)S=(P+Q sqrt(-5))^17.                  (8)

Equations (6), (7), and (8) are simultaneous exact descents, not heuristic congruences.

## 7. 2-adic root locking in the quadratic descents

Because X,Y are odd,

    R == 1 (mod 8),
    E == -1 == 7 (mod 8),
    S == 0 (mod 8).

Exact enumeration in Z[i]/8 and Z[sqrt(-5)]/8 gives uniquely

    C == 1 (mod 8), D == 0 (mod 8),
    P == 7 (mod 8), Q == 0 (mod 8).

Thus both new imaginary root coordinates are divisible by 8.

## Consequence

The coefficient-2 branch is no longer merely an equation whose norm is a 17th power. Its individual cyclotomic linear factor has been determined up to the two trivial sign-related units, and after symmetry it is an exact 17th power after division by 1+zeta.

The active system is now

    m+i n = rho^17,
    m+mu n = Gamma^17,
    R+iS = delta^17,
    E+sqrt(-5)S = eta^17,

with the explicit definitions above and 1021|n in the chosen orientation.

## Next obligation

Exploit the simultaneous exact powers rather than add isolated forcing primes. In particular, compare

    (m+mu n)/(m+i n) = (Gamma/rho)^17

inside Q(zeta_20). This gives a fixed Kummer equation in the rational parameter n/m. Its rationality/Galois constraints are now the narrowest remaining target for the coefficient-2 orientation.
