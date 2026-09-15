# U51: coefficient-2 branch — combined Gaussian / Q(sqrt(5)) sieve at 67

Status: verified partial result. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## Input

U48 gives

    m+i n = Gaussian-unit*(r+i s)^17.

U50 gives

    H_-(m,n)=omega^k alpha^17,
    omega=(1+sqrt(5))/2,
    k mod 17.

The earlier q=67 sieve tested only the second condition. Here both are imposed simultaneously.

## Exact finite-field computation

Since 67 == 3 (mod 4), F_67[i] is the field F_(67^2). Enumerating all 17th powers in this field shows that their nonzero projective coordinate ratios n/m are exactly

    0, infinity, +1, -1.

Equivalently a Gaussian 17th power modulo 67 must satisfy one of

    n=0, m=0, n=m, n=-m   (mod 67).

Independently, O_{Q(sqrt5)}/67 was represented as pairs a+b*omega with omega^2=omega+1, and all values of

    H_-(m,n)=m^4+30m^2n^2+n^4-16m^2n^2 omega

coming from Gaussian 17th powers were compared with omega^k times 17th powers in that algebra.

The result is decisive for the unit parameter:

    k=0  : compatible,
    k=15 : compatible,
    every other k=0,...,16 : incompatible.

Thus U50's eleven classes collapse to only

    k in {0,15}.

Moreover the compatible projective patterns separate:

    k=0  => n/m in {0,infinity},
    k=15 => n/m in {+1,-1}                 (mod 67).

Therefore every surviving integer solution satisfies exactly one of the following local alternatives:

(A) k=0 and 67 divides m*n;
(B) k=15 and 67 divides (m-n)(m+n).

Since gcd(m,n)=1, alternative (A) means exactly one of m,n is divisible by 67. Alternative (B) means 67 divides exactly one of m-n or m+n unless both coordinates vanish, which primitivity excludes.

## Interaction with q=103

U48 independently proves 103|mn. A combined q=103 computation imposing both the Gaussian 17th-power condition and 103|mn leaves both k=0 and k=15 possible. Thus q=103 does not choose between the two q=67 alternatives.

## Sign/unit conventions

The Gaussian unit in m+i n=epsilon(r+i s)^17 can interchange/sign the coordinates. The set {0,infinity,+1,-1} is stable under these unit actions, so the q=67 projective conclusion is unaffected.

## Next obligation

We are down to two global unit equations:

    H_- = alpha^17,

or

    H_- = omega^15 alpha^17.

Use another auxiliary rational prime q for which 17 divides the projective order in F_q[i] and in O_K/q, and intersect its combined sieve with the two q=67 alternatives. The ideal target is to eliminate one or both unit classes; if both persist, lift the q=67 alternatives 17-adically / 67-adically to obtain exact valuations and feed them into the Gaussian parametrization.
