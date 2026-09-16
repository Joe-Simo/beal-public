# U54: coefficient-2 branch — Lucas reduction and elimination of squareclass d=1

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-16.

## 1. Input from U53

We have

    (A+B omega)^17 = H_-(m,n),
    omega=(1+sqrt(5))/2,

with

    H_- = m^4+30m^2n^2+n^4 -16m^2n^2 omega,

and coefficient identity

    B P16(A,B) = -16 m^2 n^2.                      (1)

The two conjugates of A+B omega are positive because their 17th powers are the two positive quartic factors H_- and H_+.

## 2. Exact Lucas-sequence identification

Set

    P = 2A+B,
    Q = A^2+A B-B^2.

Then A+B omega and A+B(1-omega) are the roots of

    T^2-P T+Q.

Exact Wolfram recurrence verification gives

    P16(A,B) = U_17(P,Q),                             (2)

where U_n(P,Q) is the Lucas sequence

    U_0=0, U_1=1, U_n=P U_{n-1}-Q U_{n-2}.

The discriminant is

    D=P^2-4Q=5B^2.                                    (3)

The resultants

    Res_A(P,Q)=-5B^2,
    Res_B(P,Q)=-5A^2

show that gcd(P,Q) divides 5 when gcd(A,B)=1. From U49, 5 does not divide H=v^17, hence 5 does not divide v=Q. Therefore

    gcd(P,Q)=1.                                       (4)

Also A is odd and B is divisible by 8, so P is even and

    Q == 1 (mod 4).

Both roots are positive, hence P>0, Q>0 and D>0.

## 3. Sign and squareclass splitting

Because both roots alpha,beta are positive,

    U_17(P,Q)=(alpha^17-beta^17)/(alpha-beta)>0.

Equation (1) has negative right side, so necessarily

    B<0.                                               (5)

Since gcd(A,B)=1,

    gcd(B,P16) | 17,

because P16 == 17 A^16 (mod B). If 17|B, then exact substitution B=17B1 shows

    v_17(P16)=1.

For every prime q !=17 dividing B, q does not divide P16. Since B P16 is -16 times a square and P16 is odd, all nonexceptional valuations split with even parity. Consequently there is d in {1,17} and positive coprime R,S such that

    B = -d R^2,
    U_17(P,Q)=P16=d S^2.                              (6)

If d=17 then 17 does not divide S. Equation (1) becomes

    d R S = 4 |mn|.                                   (7)

## 4. Published square theorem eliminates d=1

Ribenboim and McDaniel, `Squares in Lucas sequences having an even first parameter`, Colloquium Mathematicum 78 (1998), states (building on Rotkiewicz) that for coprime Lucas parameters with

    P even,
    Q == 1 (mod 4),
    D=P^2-4Q>0,

if U_n(P,Q) is a square, then n is a square or twice an odd square (with further restrictions on prime divisors of n).

Our parameters satisfy every hypothesis above by (3)-(4) and the parity observations. If d=1 in (6), then

    U_17(P,Q)=S^2.

But 17 is neither a square nor twice an odd square. Therefore

    d != 1.

Hence the only surviving squareclass is

    B = -17 R^2,
    U_17(P,Q)=17 S^2,                                 (8)

with gcd(R,S)=1 and 17 not dividing S.

In particular (7) sharpens to

    17 R S = 4 |mn|,                                  (9)

so 17 divides mn.

The 1998 theorem does not itself rule out U_17=17 times a square; its Main Theorem produces p-times-square terms as necessary local factors in its analysis of square Lucas terms. Therefore no stronger literature conclusion is claimed here.

## 5. Normalized remaining equation

Since B=-17R^2 and B is divisible by 8, R is even. Write

    R=2r,
    P=2C.

Then A=C+34r^2 and B=-68r^2. Exact substitution into U_17/17=S^2 gives

    S^2 = C^16
        + 231200 C^14 r^4
        + 12160657600 C^12 r^8
        + 220907031488000 C^10 r^12
        + 1596053302500800000 C^8 r^16
        + 4696459390485990400000 C^6 r^20
        + 5220295245578658560000000 C^4 r^24
        + 1724188943968265512960000000 C^2 r^28
        + 73278030118651284300800000000 r^32.         (10)

Moreover

    Q=C^2-5780 r^4>0,

so C^2>5780 r^4, and gcd(C,r)=1 with 17 not dividing C.

## 6. Current bottleneck

The coefficient-2 branch is now reduced to the single exceptional Lucas squareclass

    U_17(P,Q)=17 S^2,

with fixed discriminant squareclass

    D=5*17^2*R^4,

plus the independent Gaussian 17th-power equation from U48 and the forced divisibility conditions from U52.

The general literature on `U_17(P,Q)=17*square` gives finiteness for fixed index and square multiplier but does not provide a complete classification for this case. The next useful route is therefore to exploit the extra fixed discriminant D=5*17^2*R^4 and the full cyclotomic factorization, rather than treating arbitrary Lucas parameters.
