# U44: small-prime factor bottleneck in the all-even Beal branch

Status: verified coverage/audit checkpoint only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## 1. Context

For a primitive all-even Beal candidate, write the exponent triple as

    (2r, 2s, 2t)

so that

    (A^r)^2 + (B^s)^2 = (C^t)^2.

After choosing the even and odd legs, primitive Pythagorean parametrization gives coprime integers m>n of opposite parity with

    odd leg  = m^2-n^2,
    even leg = 2mn,
    C^t      = m^2+n^2.

U43 reconstructed the valid later part of the historical chain: once every prime divisor of r and s is at least 5, published results for x^(2l)+y^(2m)=z^p eliminate p=3,5,7,11,13 and, for p=17, eliminate all cases except those in which at least one of l,m is 5. This explains why the t-divisible-by-17 branch reduces to a 5-power orientation and thence to one of the two equations

    X^10+Y^10=2 Z^17

or

    X^10+256 Y^10=Z^17.

The second of these is the U41 weighted branch.

The remaining missing prerequisite in the repository is the exclusion of prime divisors 2 and 3 from r and s. U15 had assumed this earlier reduction rather than preserving its proof.

## 2. Exact consequence of 2 | r on the odd leg

Assume the odd leg is A^r=m^2-n^2 and 2|r. Put A^(r/2)=w. Since m,n have opposite parity,

    gcd(m-n,m+n)=1.

Thus

    (m-n)(m+n)=w^2

forces

    m-n=v^2,
    m+n=u^2

for coprime odd u>v. Hence

    m=(u^2+v^2)/2,
    n=(u^2-v^2)/2.

The hypotenuse identity becomes

    C^t=m^2+n^2=(u^4+v^4)/2,

or equivalently

    u^4+v^4=2 C^t.                (Q1)

So any proof excluding 2|r in this orientation must, explicitly or implicitly, exclude primitive positive solutions of (Q1) arising with coprime odd u,v.

## 3. Exact consequence of 2 | s on the even leg

Assume the even leg is B^s=2mn and 2|s. Put B^(s/2)=w. Since gcd(m,n)=1 and m,n have opposite parity, take m odd and n even. From

    2mn=w^2

unique factorization of integer valuations forces

    m=u^2,
    n=2v^2

with gcd(u,v)=1 and u odd. Then

    C^t=m^2+n^2=u^4+4v^4.          (Q2)

Thus exclusion of 2|s requires the special quartic perfect-power equation

    u^4+4v^4=C^t.

By Sophie Germain,

    u^4+4v^4=(u^2-2uv+2v^2)(u^2+2uv+2v^2).

For coprime u,v with u odd, the two factors are odd and their gcd divides both 4uv and 2(u^2+2v^2), hence their gcd is 1. Therefore if t has an odd prime divisor p, each Sophie-Germain factor must separately be a p-th power. This is a genuine reduction, but no contradiction has yet been proved from it.

## 4. Literature audit

The 2025 survey `Generalised Fermat equation: a survey of solved cases` does not list a theorem solving either Q1 or Q2 uniformly for arbitrary t. Searches for the exact equations did not locate a primary-source theorem that would justify a blanket elimination.

In particular, Darmon-Merel's well-known `x^n+y^n=2z^n` result has equal exponents and does not imply Q1, where the left exponent is 4 and the right exponent is t. Likewise the literature on `x^4+y^4=qz^p` treats selected coefficients q and/or ranges of p; it cannot be silently substituted for Q1 or Q2.

A direct local scan at odd primes also does not give an immediate congruence obstruction for Q1 or Q2 for p in {3,5,7,11,13,17,19,23}; local solutions exist modulo every tested prime below 200. This finite computation is diagnostic only, not a theorem.

## 5. What is now proved

The missing `2|r` and `2|s` cases have been reduced exactly to Q1 and Q2, respectively. This makes the coverage gap precise rather than implicit.

No valid theorem currently in the repository excludes Q1 or Q2 for all possible t. Therefore the statement `every prime divisor of r and s is at least 5` must NOT be used as an established fact yet.

## 6. Next obligation

Attack Q1 and Q2 directly. The cheapest mathematically meaningful route is:

1. reduce t to one prime divisor p (or t=power of 2 separately);
2. exploit the coprime Sophie-Germain factors for Q2;
3. use Gaussian factorization for Q1;
4. identify whether the resulting curves/representations fall under an established modular theorem for signatures (4,4,p) or (4,2,p);
5. only after a rigorous uniform argument may the old all-even coverage chain be restored.
