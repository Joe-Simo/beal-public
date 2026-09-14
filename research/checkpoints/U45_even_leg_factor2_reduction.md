# U45: near-complete elimination of the 2-divisible even-leg exponent

Status: verified partial theorem. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## 1. Setup

From U44, if the exponent-half `s` on the even Pythagorean leg is even, then primitive parametrization forces

    m=u^2,
    n=2v^2,

with gcd(u,v)=1 and u odd, and therefore

    u^4 + 4 v^4 = C^t.                    (1)

Equivalently, with

    a=2v^2,
    b=u,

we obtain

    a^2 + b^4 = C^t,                       (2)

with gcd(a,b)=1 and ab != 0.

## 2. Published complete theorem for t >= 4

A theorem assembled from Bruin, Ellenberg, and Bennett-Ellenberg-Ng states:

    For every integer n >= 4, the equation a^2+b^4=c^n
    has no solutions in coprime nonzero integers.

A convenient secondary source giving the theorem explicitly is `Reverse engineered Diophantine equations over Q`, Theorem 4, which attributes n=6 to Bruin, prime n>=211 to Ellenberg, and the remaining n>=4 to Bennett-Ellenberg-Ng.

Applying this theorem to (2) eliminates (1) for every t>=4.

## 3. The t=2 case

If t=2, (1) is

    (u^2)^2 + (2v^2)^2 = C^2.

This is a right triangle with integer legs u^2 and 2v^2 and hypotenuse C. Its area is

    (u^2)(2v^2)/2 = (uv)^2,

an integer square. Fermat's right-triangle theorem (equivalently, the classical infinite-descent theorem that no right triangle with positive integer sides has square area) rules this out.

Therefore t=2 is impossible.

## 4. The only remaining case: t=3

The only exponent not covered by the two preceding arguments is

    u^4 + 4v^4 = C^3,                      (3)

with gcd(u,v)=1 and u odd.

Sophie Germain gives

    u^4+4v^4 = (u^2-2uv+2v^2)(u^2+2uv+2v^2).

For gcd(u,v)=1 and u odd, the two factors are odd and coprime. Hence (3) forces

    u^2-2uv+2v^2 = r^3,
    u^2+2uv+2v^2 = s^3

for coprime positive integers r,s.

Taking the ratio and writing Y=s/r gives a rational point on the genus-2 curve

    W^2 = -Y^6 + 6Y^3 - 1.                (4)

Derivation: if x=u/v, then

    Y^3 = (x^2+2x+2)/(x^2-2x+2).

Solving this quadratic for x requires its discriminant to be a rational square, which after removing a square factor is exactly (4).

The obvious rational points Y=1, W=+/-2 correspond to the degenerate condition s=r, hence uv=0, and do not give positive solutions of (3).

A bounded exact search found no positive coprime solution of (3) for u,v<500, but this is evidence only.

## 5. Additional structure of the genus-2 curve

Curve (4) has the rational involution

    (Y,W) -> (1/Y, W/Y^3).

With invariant coordinates

    S = Y + 1/Y,
    V = W(Y+1)/Y^2,

its quotient is the genus-1 quartic

    V^2 = -(S+2)(S^3-3S-6)
        = -S^4-2S^3+3S^2+12S+12.          (5)

Thus the remaining t=3 problem can be attacked by determining rational points on a genus-1 quotient together with the lifting condition `S^2-4` square, or directly by a genus-2 Chabauty/descent computation.

## 6. Consequence for Beal coverage

The historical claim `2 does not divide s` is now reduced to one explicit finite-genus Diophantine problem, (3)/(4). It is NOT yet fully proved.

What is rigorously established:

- if 2|s and t=2: impossible;
- if 2|s and t>=4: impossible by the complete (2,4,n) theorem;
- if 2|s: only t=3 remains.

Next: determine C(Q) for the genus-2 curve W^2=-Y^6+6Y^3-1, or enough of it to show that no nondegenerate rational point lifts to a positive solution of (3). In parallel, perform the analogous reduction for the `2|r` odd-leg equation u^4+v^4=2C^t.
