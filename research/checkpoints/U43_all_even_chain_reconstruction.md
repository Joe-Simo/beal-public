# U43: reconstruction of the all-even chain through the 17-divisible branch

Status: verified partial reconstruction only. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## 1. Elementary Pythagorean reduction

Let a primitive Beal solution have

    x=2r, y=2s, z=2t.

After swapping the two left summands if necessary, take A even and B,C odd. Then

    (A^r)^2 + (B^s)^2 = (C^t)^2

is a primitive Pythagorean triple. Hence there are coprime integers m>n>0 of opposite parity with

    A^r=2mn,
    B^s=m^2-n^2,
    C^t=m^2+n^2.

Since

    B^s=(m-n)(m+n)

and m-n,m+n are coprime odd integers, there are coprime odd u<v with

    m-n=u^s,
    m+n=v^s.

Therefore

    m=(v^s+u^s)/2,
    n=(v^s-u^s)/2.

Also 2mn=A^r with gcd(m,n)=1. The odd member of {m,n} is an r-th power; the even member is 2^(r-1) times an r-th power after absorbing any extra power 2^r into its base. Thus for coprime positive a,b,

    {m,n}={a^r, 2^(r-1)b^r}.

Consequently

    {v^s+u^s, v^s-u^s}={2a^r, 2^r b^r}

and, independently of the orientation,

    C^t = a^(2r) + 2^(2r-2)b^(2r).          (1)

There is a second useful identity from the u,v parametrization:

    2 C^t = u^(2s)+v^(2s).                   (2)

These identities are direct and restore the core of the missing earlier all-even derivation.

## 2. Published generalized-Fermat input

Anni-Siksek, `Modular elliptic curves over real abelian fields and the generalized Fermat equation x^{2l}+y^{2m}=z^p`, Algebra & Number Theory 10 (2016), Theorem 1:

for primes l,m>=5 and p in {3,5,7,11,13}, with the original p=13 exception l,m !=7, the only primitive solutions are trivial. The remaining p=13 exception was later closed by Billerey-Chen-Dembele-Dieulefait-Freitas; their 2023 paper states that for l,m>=5 the only solutions to x^(2l)+y^(2m)=z^13 are trivial.

Michaud-Jacobs, `On some generalized Fermat equations of the form x^2+y^{2n}=z^p`, Mathematika 68 (2022), Theorem 3:

for primes l,m !=5, the equation

    X^(2l)+Y^(2m)=Z^17

has no solutions in nonzero coprime integers.

## 3. Conditional recovery of the "one side is a 5-power" step

Assume 17|t and assume every prime divisor of r and s is >=5.

If neither r nor s is a power of 5, choose prime divisors

    l|r, m|s, l!=5, m!=5.

Then the original all-even equation can be rewritten

    (A^(r/l))^(2l) + (B^(s/m))^(2m)
      = (C^(2t/17))^17.

The transformed bases remain nonzero and coprime. Michaud-Jacobs Theorem 3 gives a contradiction.

Therefore, under the stated prerequisite on the prime divisors of r and s,

    17|t  =>  r is a power of 5 OR s is a power of 5.       (3)

This is now reconstructed from the published theorem rather than inherited from an AI summary.

## 4. The two orientations are exact

### If s=5^b

From (2),

    u^(2s)+v^(2s)=2C^t.

For b>=1 and 17|t set

    X=u^(s/5),
    Y=v^(s/5),
    Z=C^(t/17).

Then

    X^10+Y^10=2 Z^17.                         (4)

The transformation preserves gcd(X,Y)=1 and X,Y are odd.

### If r=5^a

From (1),

    C^t=a0^(2r)+2^(2r-2)b0^(2r)

(rename the Pythagorean bases a0,b0 to avoid confusion with the exponent index).

For a>=1 and 17|t define

    X=a0^(r/5),
    Y=2^((r-5)/5) b0^(r/5),
    Z=C^(t/17).

Since r=5^a, r-5 is divisible by 5 and

    2^(2r-2)=2^8 * (2^((r-5)/5))^10.

Thus exactly

    X^10+256Y^10=Z^17.                         (5)

This proves the coefficient 256 and restores the logical link from the r=5^a orientation to U15-U41.

## 5. What remains missing

The all-even chain is not yet complete. Two prerequisites still need proof from preserved evidence/primary sources:

1. show that the relevant r and s have no prime divisors 2 or 3 (equivalently, every prime divisor is >=5);
2. eliminate the alternate orientation (4), X^10+Y^10=2Z^17, or verify a published theorem that does so.

The available 2011 Q-curve theorem for x^5+y^5=2z^p does not automatically cover p=17: its displayed density result requires congruence conditions not satisfied by 17. Therefore the earlier project summary's assertion that (4) has only the trivial primitive positive solution is NOT accepted here without a stronger source.

U41's weighted equation (5) is also still a candidate elimination pending the independent level-lowering/newspace audit recorded there.

## 6. Coverage consequence

What is now rigorously connected is:

    all-even primitive Beal solution
      -> Pythagorean system (1),(2)
      -> [if 17|t, all prime divisors of r,s >=5]
      -> one of r,s is a 5-power
      -> either (4) or (5).

This is a substantial reconstruction, but the bracketed prerequisite and the coefficient-2 branch remain open obligations. No complete all-even elimination is claimed.
