# U46: elimination of the all-even t=2 boundary

Status: verified partial theorem for the all-even branch. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## 1. Target

Let a primitive all-even Beal candidate satisfy

    A^(2r) + B^(2s) = C^(2t),

with r,s,t>=2 and pairwise coprime positive bases A,B,C.

U45 proves that if t>=3 then neither 2 nor 3 divides r*s. The only boundary not covered there was t=2. This checkpoint eliminates t=2 completely.

Assume for contradiction

    A^(2r) + B^(2s) = C^4.                    (1)

After interchanging the left terms if necessary, take A even and B,C odd. Then

    (A^r)^2 + (B^s)^2 = (C^2)^2

is a primitive Pythagorean triple whose even leg is A^r.

## 2. If r is even, Fermat descent gives an immediate contradiction

If 2|r, put X=A^(r/2) and Y=B^s. Equation (1) becomes

    X^4 + Y^2 = C^4,

hence

    C^4 - X^4 = Y^2.                           (2)

Fermat's classical infinite-descent theorem says that

    x^4-y^4=z^2

has no solution in positive integers with xyz nonzero. Equation (2) is exactly such a solution, contradiction.

Therefore any hypothetical t=2 solution would have r odd. Since r>=2,

    r>=3 and r is odd.                          (3)

## 3. Nested Pythagorean parametrization for odd r

Parameterize the outer primitive Pythagorean triple:

    A^r = 2mn,
    B^s = m^2-n^2,
    C^2 = m^2+n^2,

where gcd(m,n)=1 and m,n have opposite parity.

Because m^2+n^2=C^2, the pair (m,n) is itself the pair of legs of a primitive Pythagorean triple. Thus there are coprime positive P,Q of opposite parity with

    {m,n} = { |P^2-Q^2|, 2PQ }.

Therefore

    A^r = 2mn
        = 4 P Q |P-Q| (P+Q).                   (4)

The four positive integers

    P, Q, |P-Q|, P+Q

are pairwise coprime except for the fact that exactly one of P,Q is even; the other three factors are odd and pairwise coprime. Since the product (4) is an r-th power and r is odd, every odd factor in (4) is itself an r-th power.

Let the odd member of {P,Q} be a^r, and write

    |P-Q|=b^r,
    P+Q=c^r

for positive coprime a,b,c.

There are two cases.

### Case A: the odd parameter is larger

Then

    |P-Q| + (P+Q) = 2*(odd parameter),

so

    b^r + c^r = 2 a^r.                         (5)

### Case B: the odd parameter is smaller

Then

    (P+Q) - |P-Q| = 2*(odd parameter),

so

    c^r - b^r = 2 a^r.

Because r is odd, (-b)^r=-b^r, hence this is

    c^r + (-b)^r = 2 a^r.                      (6)

Thus in either case we obtain a nontrivial primitive integer solution of

    x^r + y^r = 2 z^r.                         (7)

## 4. Darmon-Merel contradiction

Henri Darmon and Loic Merel, `Winding quotients and some variants of Fermat's Last Theorem`, J. reine angew. Math. 490 (1997), 81-100, prove that for every integer n>=3, the primitive solutions of

    x^n+y^n=2z^n

are only the trivial ones. In particular, no solution with nonzero unequal x,y,z exists.

Equations (5) and (6) are nontrivial because P,Q>0 and |P-Q|>0, and the factors above are coprime. This contradicts Darmon-Merel for n=r>=3.

Hence the odd-r case is impossible as well.

## 5. Conclusion

There is no primitive positive solution of

    A^(2r)+B^(2s)=C^4

with r,s>=2. Equivalently, the all-even Beal branch has no survivor with t=2.

Combining this with U45 gives the unconditional statement for every surviving all-even candidate:

    t>=3,
    2 does not divide r*s,
    3 does not divide r*s.

Therefore every prime divisor of r and s is at least 5. This restores the prerequisite used in U43 without any remaining t=2 exception.

## 6. Coverage consequence

For the all-even branch we now have a rigorously restored chain:

    primitive all-even Beal candidate
      -> t>=3
      -> every prime divisor of r,s is >=5.

If additionally 17|t, U43 and Michaud-Jacobs imply that one of r,s is a positive power of 5, reducing the problem to either

    X^10+Y^10=2Z^17

or

    X^10+256Y^10=Z^17.

The next unresolved coverage question is not r or s; it is t. The repository still lacks a proof that an arbitrary surviving all-even candidate must have 17|t, or a complete treatment of the cases 17 does not divide t.
