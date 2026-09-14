# U41: corrected weighted level-2000 route and q=11 elimination

Status: verified partial theorem within the stated literature and LMFDB computational dependencies. This does not resolve Beal's conjecture.

Date: 2026-09-14.

## 1. Scope

Continue with the genuine Beal-derived weighted equation

    X^10 + 256 Y^10 = Z^17,

and put

    U=X^2,
    V=2Y^2.

Then

    U^5 + 8V^5 = Z^17,

with gcd(U,V)=1, U and Z odd, and V even.

This checkpoint corrects two errors in U40 and then specializes the weighted Frey method of Azon, `Effective Darmon's program for the generalised Fermat equation` (arXiv:2504.01967), to this exact equation.

## 2. Corrections to U40

U40 is superseded on the following points.

### 2.1 Correct Frey polynomial

The authors' executable `Frey_cvs.m` defines, for signature `(r,r,p)`,

    (ABab)^((r-1)/2) x h(2 + x^2/(ABab))
      +(AB)^((r-1)/2)(B b^r-A a^r),

where h is the minimal polynomial of zeta_r+zeta_r^(-1).

For r=5,

    h(T)=T^2+T-1.

For A=1, B=8, a=U, b=V, exact expansion gives

    f(x)=x^5 + 40UV x^3 + 320U^2V^2 x + 64(8V^5-U^5).

The sign of the cubic term is **positive**. U40's `-40UVx^3` was wrong.

The code's twist parameter is 1 in the present branch:

- at 2, `SQ(64(8V^5-U^5))` holds because the 2-adic valuation is even and the normalized unit condition is satisfied;
- at 5, neither c=Z nor C=1 is divisible by 5 in the manner triggering a twist.

Therefore this is the actual Frey curve used below.

### 2.2 Correct local parameter

U40 also used the `(p,p,r)` parameter `s0=U^5/Z^17`. For our `(r,r,p)` equation this is not the relevant local parameter.

The source gives, for signature `(r,r,p)`, the valuation identity

    nu_q = v_q(s0(s0-1))
         = 2p v_q(Cc) - v_q(16 A a^r B b^r).

Thus here

    nu_q = 34 v_q(Z) - v_q(128 U^5 V^5).

All local conductor calculations below use this formula.

## 3. Residual irreducibility from q=2

Since U,Z are odd and V=2Y^2,

    v2(V)=1+2v2(Y),

so

    nu_2 = -(7+5v2(V))
         = -(12+10v2(Y)).

Hence

    nu_2 <= -12,
    nu_2 == 3 (mod 5),

whereas `-8 == 2 (mod 5)`.

Azon Proposition 5.20 applies with r=5 and residual characteristic p=17 because ord_5(2)=4 is even, p does not divide 2r, `nu_2<=-8`, and `nu_2 != -8 (mod 5)`.

Therefore the mod-17 residual representation is absolutely irreducible. Its local representation at the prime above 2 is the irreducible induction from the unramified quadratic extension, with inertia image of order 5.

Table 2 gives the local Artin conductor exponent

    n_2^- = 2.

## 4. Exact 5-adic case

From the Gaussian-descent branch, U37 proves 5 divides the Gaussian parameter B. Since U15-U16 give

    b=16*17^4 B^5,
    H=17D^5,
    bH=16Y^5,

we obtain exactly

    Y=17BD

in the positive branch. In particular 5|Y, hence 5|V, while gcd(U,V)=1 gives 5∤U.

Also 5∤Z. One direct check is that for 5-adic units X,Y the tenth powers modulo 25 are ±1; whenever 5 divides

    X^10+256Y^10,

the valuation is exactly 1, which cannot equal 17v5(Z). Thus Z is a 5-adic unit.

Therefore

    nu_5 = -5 v5(V) < 0,
    nu_5 == 0 (mod 5).

To decide the corresponding Table-2 row one must know whether the source polynomial `g_5^-` is reducible over Q_5. Proposition 4.39 of the source implies, in this setting, that reducibility would force a Q_5-root.

An exact Wolfram residue calculation was performed on the **correct** `+40UVx^3` model modulo 125:

- enumerate every U mod 125 that is a square;
- enumerate every V mod 125 that is twice a square;
- retain primitive pairs compatible with 5∤Z;
- there are 793 such residue pairs;
- for every one, test every x mod 125 in

      x^5 + 40UVx^3 + 320U^2V^2x + 64(8V^5-U^5).

No pair admits a root modulo 125.

Because the polynomial is monic, a Q_5-root would be 5-integral and would reduce to a root modulo 125. Therefore it has no Q_5-root and the relevant `g_5^-` is irreducible.

Table 2 then gives

    n_5^- = 3.

## 5. The residual prime 17

The same identity `Y=17BD` gives 17|V. Primitivity implies 17∤U and the original equation then gives 17∤Z.

Hence

    nu_17 = -5 v17(V) < 0,
    nu_17 == 0 (mod 5).

The twist is trivial at 17. Table 2 places this in the good-reduction row, so the conductor exponent at the prime above 17 is zero. The residual representation is finite flat at 17.

## 6. Solution-dependent primes

For q|Z with q not in {2,5,17},

    nu_q = 34 v_q(Z)>0.

Azon Theorem 5.21 shows that the mod-17 residual representation is unramified at such q because the relevant toric valuation is divisible by 17.

For q|UV away 2 and 5, `nu_q` is a negative multiple of r=5, and Table 2 gives conductor exponent zero.

Thus after lowering, the only level support is at 2 and the ramified prime over 5.

## 7. Correct lowered level

Let K=Q(sqrt(5)), and let r5 denote the unique prime of K above 5.

The local exponents are

    n_2=2,
    n_5=3.

Therefore the target Hilbert level is

    N = (2)^2 * r5^3.

Since 2 is inert in K,

    Norm((2))=4,

and Norm(r5)=5. Hence

    Norm(N)=4^2*5^3=2000.

The LMFDB ideal at this level is

    2000.1 = [2000,100,-40*w+20].

## 8. Level-lowering theorem-chain adaptation

Azon's packaged Theorem 5.23 assumes Hypothesis 5 and a convenient local condition at the residual prime. Our branch does **not** satisfy Hypothesis 5: every negative `nu_q` away 2 and 5 arising from q|UV is automatically a multiple of 5.

Therefore Theorem 5.23 is not quoted verbatim here.

Instead, the proof ingredients are supplied directly:

1. The minus compatible system is modular by Azon Theorem 5.5.
2. Absolute irreducibility is supplied by Proposition 5.20 at q=2.
3. Breuil-Diamond Theorem 3.2.2 requires irreducibility after restriction to the quadratic 17-cyclotomic subfield K(sqrt(17)). This follows from the same local q=2 representation:
   - if the restriction to G_{K(sqrt17)} were reducible while the representation over G_K were irreducible, Clifford theory would make it induced from the quadratic field K(sqrt17);
   - 17 == 1 (mod 8), so sqrt17 is already in Q_2;
   - consequently the prime of K above 2 splits in K(sqrt17)/K;
   - a representation induced from that quadratic extension restricts to the local decomposition group at 2 as a sum of characters, hence is reducible;
   - Proposition 5.20 gives an irreducible local representation at 2. Contradiction.
4. At 17 the original Jacobian has good reduction, supplying the required finite-flat/Barsotti-Tate local lift of Hodge-Tate weights {0,1}.
5. At primes removed from the level, Theorem 5.21 and Table 2 supply unramified residual local conditions; retain the original local types at 2 and 5.

Thus Breuil-Diamond's modular lifting theorem applies with the desired local types and yields a parallel-weight-2 Hilbert newform over K at level N above.

This is a theorem-chain adaptation of Azon's proof, not a literal application of his Theorem 5.23. It remains an important point for independent expert/formal audit.

## 9. Complete LMFDB level-2000 inventory

The LMFDB API query for field `2.2.5.1` and level norm 2000 returns exactly eight newform orbits at the single level ideal `2000.1`. Querying the next offset returns zero further records.

The eight orbits are

    a,b,c,d,e,f,g,h,

with dimensions

    2,2,2,2,2,2,2,4.

Their total dimension is 18.

This is currently a database-completeness dependency; an independent Magma reconstruction of the full newspace has not yet been executed in our environment.

## 10. Exact q=11 Frey trace inventory

Take q=11. It splits into two norm-11 primes in K.

For every pair `(a,b) mod 11` with `(a,b)!=(0,0)` and

    a^5+8b^5 != 0 (mod 11),

compute the genus-2 curve from the **correct** source model and count points over F_11 and F_121. From the first two point counts recover the genus-2 Euler polynomial and its RM trace quadratic.

An exact Wolfram finite-field computation over all 120 admissible residue pairs gives precisely the following eight possibilities `(S,P,Delta; multiplicity)`:

    (-9,19,5;5),
    (-7,11,5;25),
    (-3,-9,45;25),
    (-1,-1,5;5),
    ( 1,-1,5;5),
    ( 3,-9,45;25),
    ( 7,11,5;25),
    ( 9,19,5;5).

Thus the possible two-dimensional RM traces are

    (S ± d sqrt(5))/2,

with d=1 for S=±1,±7,±9 and d=3 for S=±3.

All have nonzero norm modulo 17 because P is one of

    19,11,-9,-1.

This computation independently reproduces the trace structure expected from the authors' `Bounding_ps` algorithm.

## 11. q=11 Hecke data for the eight forms

The ordered norm-11 primes in LMFDB are

    [11,11,-3*w+2],
    [11,11,-3*w+1].

The relevant Hecke data are:

- a: coefficient polynomial `e^2+e-1`, traces `(e,-5)`;
- b: `e^2-9e+19`, traces `(0,0)`;
- c: `e^2+5e-5`, traces `(-5,0)`;
- d: `e^2+e-1`, traces `(0,0)`;
- e: `e^2+11e+29`, traces `(0,0)`;
- f: `e^2+5e-5`, traces `(-e-5,e)`;
- g: `e^2+e-1`, traces `(e,5)`;
- h: quartic coefficient polynomial `e^4-10e^3-13e^2+190e+241`, traces `(0,0)`.

### Good reduction case q does not divide Z

Forms b,c,d,e,h are immediately impossible modulo 17 because one norm-11 Hecke trace is zero, while every admissible Frey RM trace has nonzero norm modulo 17.

For a,f,g an exact comparison in

    F_17[w]/(w^2+w-1)

was made against all 16 ordered Frey trace pairs, checking both embeddings of each quadratic coefficient field when relevant.

The result is

    no matches for a,
    no matches for f,
    no matches for g.

Hence all eight orbits are eliminated in the good-reduction q=11 branch.

### Toric case 11 divides Z

The authors' `M_toric` condition requires at each norm-11 prime

    a_q(g)^2 == (11+1)^2 = 144  (mod 17).

For the nontrivial quadratic coefficient fields, exact norms are

    Norm(144-e^2)=20305=5*31*131

for `e^2+e-1`, and

    Norm(144-e^2)=15721=79*199

for `e^2+5e-5`.

Neither is divisible by 17. A zero trace gives 144 == 8 mod 17, also impossible.

Therefore all eight forms are also eliminated in the toric q=11 branch.

## 12. Consequence

Subject to the theorem-chain adaptation in Section 8 and the completeness/correctness of the LMFDB level-2000 inventory, there is no primitive solution of the Beal-derived weighted equation

    U^5+8V^5=Z^17

with the square/parity structure

    U=X^2,
    V=2Y^2

coming from our all-even reduction.

Equivalently, the remaining weighted equation

    X^10+256Y^10=Z^17

is eliminated within these stated dependencies.

This closes the specific all-even `17|t`, `r=5^a` orientation that survived U14. It does **not** resolve Beal's conjecture or all remaining exponent signatures.

## 13. Verification obligations

Before promoting this subbranch from a research theorem to independently verified mathematics, retain the following obligations:

1. Independently reproduce the complete Hilbert newspace at level `(2)^2*r5^3` with Magma/Sage or another Hilbert modular-form implementation; current enumeration uses LMFDB.
2. Obtain an independent expert or formal audit of the Breuil-Diamond level-lowering adaptation in Section 8, since it replaces rather than literally invokes Azon's Hypothesis-5 package.
3. Reproduce the q=11 elimination with the authors' Magma package when an appropriate runtime is available; current Frey trace computation was independently performed in exact Wolfram finite fields and agrees structurally with the published algorithm.

No full Beal solution is claimed.
