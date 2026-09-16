# U80: the quadratic-norm shortcut is redundant, Hecke reciprocity is vacuous here, and the class-group bottleneck remains

**Status: written self-reviewed reduction/audit with exact finite corroboration. The class-group 2-rank, full global restriction matrix, numerical rank upper bound, weighted equation, and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. The private repository was resumed from U79. No existing mathematical checkpoint was overwritten. A bounded PARI/GP GitHub Actions attempt was also made and failed before any workflow step executed; this is an execution-environment failure, not class-group evidence.

## 1. What this checkpoint establishes

Keep U78/U79's genus-eight Jacobian over

    k=Q(phi), phi^2-phi-1=0,

and its odd-degree 2-descent root field

    F=k(s), s^17=2/phi=2phi-2,
    O_F=Z[phi,s],
    disc(F)=2^32*5^17*17^34.

Write `Sel_2(J/k)` for the Selmer group described in U78 and let

    d=dim_F2 Cl(O_F)[2].

U79 determined the complete dyadic Kummer image. The present checkpoint proves two negative-but-useful route eliminations.

**Theorem A (the extra quadratic-norm condition gives no new Selmer restriction).** The weighted divisor class constructed in U77 has Kummer squareclass represented by a norm from `F(i)/F`. However, **every** class in `Sel_2(J/k)` is already represented by a global norm from `F(i)/F`. Thus the special quadratic-norm shape of the weighted class cannot reduce the U78/U79 Selmer space any further.

**Theorem B (Hecke reciprocity supplies no class-group parity restriction for this field).** For the degree-seventeen extension `F/k`, the Hecke ideal of Shnidman--Siad has even valuation at every prime. Hence there are no Hecke primes in the sense of their Definition 3.7. Their Theorem 3.8 is therefore vacuous here and does not determine or bound `d`.

The exact class-group 2-rank remains uncomputed. The best current rank-zero certificate is still U78's

    d=0 and rank(Psi)=17.

U80 does not establish either assertion.

## 2. Exact norm shape of the weighted Kummer class

This section records a structural fact that initially looked like a possible shortcut, then shows why it is redundant.

Let `zeta` be a primitive fifth root with `phi=1+zeta+zeta^-1`. Keep U77's fields and automorphisms. In particular, let

    K0=k(c), c^10=-256,

and in a Galois closure let `sigma(c)=zeta*c`, while `eta` sends `i` and `c` to their negatives and fixes `zeta,k`. Let `kappa` send `zeta` to `zeta^-1` and fix `c,i,k`. U77's common-root orbit gives

    u_j=sigma^j(U), j mod 5,

for the `u`-coordinate `U` used in the genus-eight quotient. Let `r` be a branch root of the odd-degree model over `F`; the monic coordinate change in U78 multiplies every `u-r` factor by the same base-field constant, which cancels on degree-zero divisor differences.

For U77's effective divisor `D=sum_j P_j`, define

    q=product_(j=0)^4 (u_j-r).

The five factors are permuted by `kappa`, so `q` is `kappa`-fixed. Before taking `kappa` invariants it lies in the compositum with `Q(zeta,i)`; hence

    q in F(i).

For the anti-invariant class

    Z=[D-eta(D)],

the odd-degree hyperelliptic Kummer map gives

    delta(Z)=q/eta(q)  in F*/F*^2.

Modulo squares,

    q/eta(q) = q*eta(q),

because the quotient differs from the product by the square `eta(q)^2`. Therefore

    delta(Z)=[Norm_(F(i)/F)(q)].                    (2.1)

Equivalently, multiplying the five `sigma` factors and their five `eta` conjugates gives all ten `k`-embeddings of `K0`, so

    delta(Z)=[Norm_(K0/k)(U-r)].                    (2.2)

The quadratic-twist isomorphism from U77 leaves the hyperelliptic `u`-coordinate and branch locus unchanged, so the same 2-Kummer squareclass represents the descended class on `Jminus`.

There is also an immediate norm-kernel check. Since

    r^17=phi^2/4,
    U^17-r^17=(3-phi)V^2/4,

we have

    Norm_(F/k)(U-r)=(3-phi)V^2/4.

Taking `Norm_(K0/k)` and using `Norm_(K0/k)(V)=1` shows that the norm of (2.2) down to `k` is a square, as required by U78's global space `V`.

This is an exact structural identity, not a point search and not a proof that a weighted solution exists.

## 3. The dyadic local norm group already contains W_2

Let `K2` be the completion of `k` at its unique prime above 2 and

    E=K2(s), s^17=2/phi.

U79 uses the normalization `v_s(s)=1`, so

    2=phi*s^17.                                    (3.1)

Adjoin `i` and put

    pi=i-1.

For every `b in E`, direct multiplication gives

    Norm_(E(i)/E)(1+b*pi)=1-2b+2b^2.               (3.2)

Suppose `v_s(b)=m>=1`. By (3.1), the first correction term in (3.2) has valuation `17+m`, while the quadratic correction has valuation `17+2m`. Thus the leading coefficient of the norm correction at depth `17+m` is

    -phi * bar(b) in F_4.

Multiplication by `-phi` is a bijection of `F_4`. Consequently an arbitrary leading coefficient at every depth `d>=18` can be produced by choosing `m=d-17` and the residue of `b` appropriately.

Starting with any target `u in 1+s^18 O_E`, recursively choose factors `1+b_j*pi` whose norms cancel the current leading error. Each step raises the error valuation strictly. The infinite product converges in the complete field `E(i)`, and continuity of the norm gives

    1+s^18 O_E  subset Norm_(E(i)/E)(E(i)^*).       (3.3)

U79 proved that `W_2` is generated by

    1+s^n, 1+phi*s^n, n=19,21,23,25,27,29,31,33.

Every generator belongs to `1+s^18 O_E`. Hence

    W_2 subset Norm_(E(i)/E)(E(i)^*)/E^*2.          (3.4)

This is stronger than checking only the sixteen generators.

### 3.1 Exact finite corroboration

`code/U80_quadratic_norm_redundancy.py` independently constructs explicit products of factors (3.2) for all sixteen U79 basis generators in

    (Z/8)[phi,s]/(phi^2-phi-1, s^17-2phi+2).

The residual valuations are respectively

    36,36,38,38,40,40,42,42,
    37,37,41,41,45,45,49,49,

all at least U79's certified `s^35` squareclass cutoff. The script was executed successfully and `py_compile` also succeeded in the working runtime.

Wolfram separately reduced the same sixteen product identities in the quotient ring and returned exactly the same residual-valuation list. This is distinct exact arithmetic corroboration of the finite certificate, not independent review of the written local argument.

## 4. Every Selmer class is already a global norm from F(i)

Take any class `alpha in Sel_2(J/k)` and choose a representative in `F^*`. Multiplying by a square never affects whether it is a local or global norm from `F(i)`, because every square in `F` is itself a norm.

We check every place of `F`.

### 4.1 Above 2

By the Selmer condition, the localization lies in `W_2`. Equation (3.4) makes it a local norm from `F(i)`.

### 4.2 Above 5

In `k_5`, `-1` is already a square: `2^2=-1 mod 5`, and the simple root lifts by Hensel. Therefore adjoining `i` splits locally. The norm map from the split quadratic algebra is surjective, so there is no restriction.

### 4.3 Above 17

U78 proves `H_17=W_17=0`. Thus every Selmer localization is a square, hence a norm.

### 4.4 Odd finite places outside 2,5,17

The quadratic extension `F(i)/F` is unramified or split at every such place. At a split place the norm is surjective. At an unramified quadratic place the unit norm is surjective and valuations of norms are even. U78's good-place Selmer condition is exactly the unramified/even-valuation condition, so every such localization is a norm.

### 4.5 Archimedean places

At a complex place there is no condition. At a real place of `F`, adjoining `i` gives `C/R`, whose nonzero norms are precisely the positive reals. U78 proves that at both real places of `k` the local norm-kernel space `H_v` is zero. In the root algebra this forces the real component of a global Selmer squareclass to be positive, hence a local norm.

Thus `alpha` is a local norm from `F(i)` at every place of `F`. The extension `F(i)/F` is cyclic of degree two, so the Hasse norm theorem (Milne, *Class Field Theory*, Chapter VIII, Section 3, Theorem 3.1) gives

    alpha in Norm_(F(i)/F)(F(i)^*).                 (4.1)

This proves Theorem A.

**Consequence.** The fact that U77's weighted class has the norm shape (2.1) is not a hidden eighteenth Selmer condition. Any attempt to finish the weighted equation by imposing only this quadratic-norm property cannot work: it is already forced by membership in the existing 2-Selmer group.

## 5. Hecke reciprocity does not determine the missing 2-class group

A second possible shortcut was suggested by the recent preprint of Shnidman--Siad on 2-primary relative class groups of odd-degree extensions. Their Definition 3.7 calls a prime `w` of `F` a Hecke prime only when an **odd** power of `w` divides

    H_(F/k)=Disc_(F/k) O_F * Diff_(F/k)^(-1),

in addition to a local non-square condition. Their Theorem 3.8 says that the number of Hecke primes inert in an everywhere-unramified quadratic extension of square norm is even.

For our explicit extension `F/k`, only the primes above 2 and 17 ramify.

At 2, `s` is a uniformizer and the derivative of `T^17-c` has valuation 16, so

    v_(P2)(Diff)=16,
    v_(p2)(Disc)=16,
    p2 O_F=P2^17.

Therefore

    v_(P2)(H)=17*16-16=256.                         (5.1)

At 17, the shifted Eisenstein root is a uniformizer while `s` itself is a unit. The derivative has valuation 17, and U78's relative discriminant has base-prime exponent 17. Since

    p17 O_F=P17^17,

we get

    v_(P17)(H)=17*17-17=272.                        (5.2)

Both exponents are even, and every other exponent is zero. Hence there are **no Hecke primes** for `F/k`. Wolfram independently evaluated the two exponent calculations as `{256,272,True,True}` for the values and their parity.

Theorem 3.8 therefore imposes the empty parity condition `0=0` in this field. Corollary 3.10 and the pure-prime-degree example in that paper do not turn this into `Cl(O_F)[2]=0`; the hypotheses and Hecke-prime inventory must be retained. This proves Theorem B and closes this literature shortcut without making a class-group claim.

## 6. Exact field audit and the still-missing class-group computation

Wolfram was used on

    f(T)=T^34+2T^17-4.

It returned

    signature = (2,16),
    discriminant factorization = 2^32 * 5^17 * 17^34,
    integral-basis length = 34,

corroborating U78's field data. `NumberFieldClassNumber` did **not** return a class number; it reported that the class number for this field is not currently available. Requests for a regulator/fundamental-unit computation encountered an upstream error. None of these failures is evidence about `d`.

PARI/GP remains a suitable next exact engine. Its official documentation states that `bnfcertify(B,1)=1` certifies that the **true class group is a quotient of the computed class group**. For the present objective this weaker certificate is enough: if `B.clgp` has odd order and `bnfcertify(B,1)=1`, every quotient has odd order, so

    Cl(O_F)[2]=0 and d=0.                            (6.1)

A full unit/regulator certification is unnecessary merely to establish (6.1).

A bounded private GitHub Actions workflow `.github/workflows/u80-pari-classgroup.yml` was added at commit `7370f5854c3b9f8b151dc8c7bd2085664ca062eb`. Run `35118842305`, job `104871123523`, failed in roughly four seconds with **no workflow steps recorded**. No PARI installation or class-group command is known to have executed, and no calculation output exists. It must be recorded as a pre-execution runner failure, not a failed class-group computation and not a mathematical obstruction.

## 7. Current coverage and next obligation

U80 removes two tempting but ineffective shortcuts: the weighted quadratic-norm shape is automatic on the current Selmer group, and the available Hecke-reciprocity theorem is vacuous for this field's even Hecke-ideal exponents.

The arithmetic bottleneck is therefore unchanged but better isolated:

1. compute `d=dim_F2 Cl(O_F)[2]` unconditionally, preferably by an exact class-group engine plus a quotient certificate sufficient for parity;
2. if `d=0`, construct the seventeen-dimensional global candidate basis and compute the full restriction matrix `Psi` against U79's explicit dyadic quotient and U78's prime-5 bit;
3. certify `rank(Psi)=17` to obtain `Sel_2(J/k)=0`, which would exclude the active weighted equation through U77;
4. keep that conclusion separate from the remaining Beal exponent signatures.

No counterexample was found, no weighted-equation impossibility theorem was obtained, and no claim that Beal's conjecture is solved is made.
