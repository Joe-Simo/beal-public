# U57: coefficient-2 orientation is eliminated by the strengthened Freitas theorem

Status: verified primary-source theorem application to one Beal subbranch. This does not resolve Beal's conjecture.

Date: 2026-09-16.

## 1. Branch to eliminate

U43 proves that in the all-even `17 | t` branch, if the `s`-orientation is the 5-power orientation, then there are coprime odd positive integers `X<Y` and a positive integer `Z` satisfying

    X^10 + Y^10 = 2 Z^17.                              (1)

The strict inequality follows directly from U43's Pythagorean parametrization: `m-n=u^s`, `m+n=v^s` with `0<u<v`, and in this orientation

    X=u^(s/5),
    Y=v^(s/5).

Thus `X<Y`.

Set

    x=X^2,
    y=Y^2,
    z=Z.

Then (1) becomes

    x^5 + y^5 = 2 z^17,                                (2)

with `gcd(x,y)=1`.

## 2. Correction to the literature record

The project previously relied on arXiv:1103.5388v1 (March 2011) by Luis Dieulefait and Nuno Freitas. In that early preprint, Theorem 1.1 used the narrower condition

    p ≡ 1 (mod 4) AND p ≡ ±1 (mod 5),

which does not include `p=17` because `17 ≡ 2 (mod 5)`.

That preprint is not the strongest later source and is superseded for this application.

Nuno Freitas' doctoral thesis,

    Some Generalized Fermat-type Equations via Q-Curves and Modularity,
    Universitat de Barcelona, 2012,

states and proves the strengthened result as Theorem 2.0.3:

Let `beta` be an integer divisible only by primes `l` with `l != 1 (mod 5)`. Suppose

    p ≡ 1 (mod 4) OR p ≡ ±1 (mod 5).

Then

    x^5+y^5=C z^p

has no non-trivial primitive solutions if

    C=2 beta and p>13,

with a parallel coefficient-3 statement under its own bound.

The same thesis later completes the proof by eliminating the surviving CM pairs whenever

    p ≡ 1 (mod 4) OR p ≡ ±1 (mod 5).

Primary source item:

    https://diposit.ub.edu/items/c2f22042-c62e-4c2c-8912-1205d382ed2d

Direct thesis text:

    https://diposit.ub.edu/bitstreams/c7eff111-9cde-45e5-8dae-85b503ecaafd/download

The later joint article is

    Luis Dieulefait and Nuno Freitas,
    `The Fermat-type equations x^5+y^5=2z^p or 3z^p solved through Q-curves`,
    Mathematics of Computation 83 (2014), 917–933,
    DOI 10.1090/S0025-5718-2013-02731-7.

Its final publication metadata/abstract reports a solved prime set of density `3/4`, consistent with the union (`OR`) of the two congruence conditions, whereas the old arXiv v1 abstract reported density `1/4` for the coefficient-2 case. This independently confirms that the old preprint statement is stale for the later result.

## 3. Application to p=17

Apply Theorem 2.0.3 with

    beta=1,
    C=2,
    p=17.

The condition on prime divisors of `beta` is vacuous. Also

    17>13,
    17 ≡ 1 (mod 4).

Hence the theorem applies and (2) has no non-trivial primitive solution.

Our `(x,y,z)` is primitive because `gcd(X,Y)=1` implies `gcd(X^2,Y^2)=1`.

## 4. The trivial solution cannot arise from U43

The thesis calls a primitive solution trivial when `|xyz|<=1`. For positive integers in (2), this forces

    x=y=z=1.

But U43 gives `X<Y`, hence

    x=X^2<Y^2=y.

Therefore the trivial solution cannot be the image of a Beal-derived solution.

Consequently U43's coefficient-2 orientation is impossible.

## 5. Coverage consequence

The orientation

    X^10+Y^10=2Z^17

is CLOSED by the primary-source theorem plus the elementary U43 pullback.

The exploratory arithmetic descent U46 and U48–U56 remains preserved because it contains valid independent structure and may be reusable elsewhere, but it is no longer needed to eliminate this orientation.

This does NOT close the full all-even `17 | t` branch: the second orientation

    X^10+256Y^10=Z^17

still depends on U41's candidate modular elimination, whose complete Hilbert-newspace enumeration and level-lowering bridge require independent certification.

This also does NOT address the all-even `17 ∤ t` branch (all right prime divisors at least 19), or the much larger mixed-signature part of the original Beal conjecture.
