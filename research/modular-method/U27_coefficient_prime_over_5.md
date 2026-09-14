# U27: exact coefficient-field prime over 5

Status: verified partial result only. This does not resolve Beal's conjecture.

This checkpoint clarifies the coefficient-field prime used in U26 for the two residual-pairing problems.

## r/s pair

The LMFDB Hecke polynomial for both `4.4.4913.1-272.1-r` and `4.4.4913.1-272.1-s` is

    f_rs(x) = x^2 + 2 x - 4.

Exact factorization modulo 5 gives

    f_rs(x) = (x+1)^2  (mod 5).

Hence the only residue-degree-one prime above 5 in this coefficient field is the ramified prime

    lambda_rs = (5, e+1),

and reduction at lambda_rs is obtained by sending

    e -> -1  (mod 5).

## v/w pair

The LMFDB Hecke polynomial for both `4.4.4913.1-272.1-v` and `4.4.4913.1-272.1-w` is

    f_vw(x) = x^6 + 3 x^5 - 42 x^4 - 104 x^3 + 364 x^2 + 428 x + 104.

Exact factorization modulo 5 gives

    f_vw(x) = (x+1)^2 (x^4 + x^3 - 1)  (mod 5),

and the quartic factor `x^4+x^3-1` is irreducible over F_5. Therefore there is again a unique residue-degree-one prime above 5,

    lambda_vw = (5, e+1),

with ramification index 2; the remaining prime above 5 has residue degree 4. Thus the mod-5 comparison relevant to the U26 Galois-descent route is unambiguously the reduction

    e -> -1  (mod 5)

for both pairs.

This removes a possible ambiguity in the residual-congruence problem but does not prove either congruence `r ~= s (mod lambda)` or `v ~= w (mod lambda)`.

## Verification

Wolfram Language exact modular factorization returned

    {(1+x)^2, (1+x)^2 (4+x^3+x^4), 4+x^3+x^4}

for `f_rs`, `f_vw`, and the quartic factor respectively, confirming irreducibility of the quartic over F_5.

The LMFDB records used are the current API records for the four level-272 Hilbert newforms.

## Next obligation

With the coefficient prime fixed exactly, the preferred next computation is the finite mod-5 Hecke-module test from U26: certify or refute the paired congruences `r ~= s` and `v ~= w` at `(5,e+1)`. A finite prefix comparison of listed LMFDB Hecke eigenvalues is evidence only and is not a substitute for the full Hecke-algebra/multiplicity-one certificate.