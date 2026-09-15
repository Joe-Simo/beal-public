# U46: coefficient-2 square branch — literature pruning and a mod-103 constraint

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## 1. Branch

The unresolved all-even orientation from U45 is

    X^10 + Y^10 = 2 Z^17,

with positive pairwise-coprime X,Y,Z. Put

    a = X^2,  b = Y^2,  c = Z.

Then

    a^5 + b^5 = 2 c^17,                              (1)

where a,b are squares and gcd(a,b)=1.

Since X,Y must both be odd in this primitive coefficient-2 orientation, a,b are odd squares and hence

    a ≡ b ≡ 1 (mod 8),
    a+b ≡ 2 (mod 8).

## 2. Published results that prune (1)

Billerey–Chen–Dieulefait–Freitas, `A multi-Frey approach to Fermat equations of signature (r,r,p)`, Trans. AMS 371 (2019), proves for x^5+y^5=d z^p:

- Theorem 3: no non-trivial solution for d in {1,2} if p | c.
- Theorem 4: no non-trivial solution for d=2 if c is even; also none if 5 | c.
- Theorem 5: no non-trivial primitive solution for d=2 if 5 | a+b.
- Theorem 6: no non-trivial primitive solution for d=2 if 4 | a+b.

Applied to p=17,d=2, any non-trivial primitive solution of (1) must therefore satisfy

    c odd,
    5 ∤ c,
    17 ∤ c,
    5 ∤ a+b,
    4 ∤ a+b.

The last condition is automatic for our square branch because a+b ≡ 2 (mod 8).

The older Dieulefait–Freitas Q-curve theorem (Math. Comp. 83 (2014), Theorem 1.1) does not cover p=17: it requires p>13, p≡1 (mod 4), and p≡±1 (mod 5). Although 17≡1 (mod4), it is 2 mod5.

Thus published d=2 results do not by themselves close the square branch.

## 3. Exact factorization in the remaining branch

Let

    Phi(a,b) = a^4-a^3 b+a^2 b^2-a b^3+b^4.

Then

    (a+b) Phi(a,b) = 2 c^17.

For primitive a,b, gcd(a+b,Phi(a,b)) divides 5. Since Theorem 5 excludes 5 | a+b, the factors are coprime. Since a,b are odd and a+b≡2 (mod8), Phi(a,b) is odd. Therefore there exist coprime positive integers u,v with

    a+b = 2 u^17,
    Phi(a,b) = v^17,
    c = uv.                                           (2)

This is a stronger square-specific reformulation of the surviving branch.

## 4. A certified mod-103 obstruction

A Wolfram finite-field enumeration over F_103 was performed on the necessary conditions from (2), with a,b restricted to quadratic residues. The conditions tested were

    (a+b)/2 is a 17th power in F_103,
    Phi(a,b) is a 17th power in F_103,
    a,b are squares.

The only square pairs (a,b) satisfying both conditions are

    (0,0), (1,1), (46,46), (56,56).

Hence every primitive integer solution to (2) satisfies

    a ≡ b (mod 103),

and because gcd(a,b)=1, neither is 0 mod103. Equivalently,

    103 | (X^2-Y^2),
    103 ∤ XY.                                         (3)

This is a rigorous local constraint, but not yet a contradiction.

## 5. Current bottleneck

Azon's Proposition 5.20 cannot supply residual irreducibility for this branch because its q=2 criterion requires negative nu_2, whereas here nu_2=30>0. The 2014 Q-curve theorem also misses p=17 because 17 is inert modulo the CM condition at Q(sqrt(-5)).

The promising next route is therefore to exploit the additional square restrictions a=X^2,b=Y^2 inside the multi-Frey/Q-curve elimination, especially against the CM-by-Q(sqrt(-5)) residual forms that survive for p=17, or to combine (2) with descent on the superelliptic equation Phi(X^2,Y^2)=v^17.
