# U91: mixed degree-four Padé space has maximum formal order 728, but the first exact enlargement weakens the height barrier

**Status: written route audit with exact rational/integer computation and a rigorous finite-field rank certificate. The weighted equation and Beal's conjecture remain unresolved. No independent expert or proof-assistant verification is claimed.**

Research date: 2026-09-16. This continues U90's Padé route for the surviving weighted equation

    X^10+256Y^10=Z^17.                               (W)

The goal is to determine whether the full degree-four mixed-weight coefficient space can materially improve U90's certified lower bound

    max(X,Y)>10^25993.

This checkpoint does **not** reconstruct the full 73-term degree-four relation. It proves the exact maximum possible local order in every residue class, reconstructs a substantial 58-term mixed-weight relation exactly, and measures its actual arithmetic-height cost.

## 1. Local series and degree-four monomials

Retain U90's notation at a strong prime `q|Y`:

    T=Y/X,
    S=T^10,
    theta=sum_(j=0)^9 a_j c^j,
    a_j=x*T^j*F_j(S),
    F_j(S)=sum_(m>=0) B_(j+10m)(-256)^m S^m,
    B_n=binomial(1/17,n),
    c^10=-256.                                       (1.1)

There are

    C(13,4)=715

degree-four monomials `a_i a_j a_k a_l` with `0<=i<=j<=k<=l<=9`. Group them by the residue of the total coefficient-index weight modulo ten.

The exact counts are

    residue 0,2,4,6,8: 73 monomials each,
    residue 1,3,5,7,9: 70 monomials each.            (1.2)

For a monomial of weight `r+10h`, factor

    x^4*T^r*S^h.

The remaining factor is a product of four `F_j(S)` series. Thus every residue class is one finite-dimensional Hermite--Padé problem.

## 2. A modular rank certificate gives the exact cancellation ceiling

`code/U91_degree4_mixed_audit.py` forms the series modulo the prime `5003` and, for every residue class, adds coefficient rows successively until full column rank is reached.

For every residue, the first full-rank row count equals the number of columns:

| residue | monomials | first full row count mod 5003 | largest possible local order |
|---:|---:|---:|---:|
| 0 | 73 | 73 | 720 |
| 1 | 70 | 70 | 691 |
| 2 | 73 | 73 | 722 |
| 3 | 70 | 70 | 693 |
| 4 | 73 | 73 | 724 |
| 5 | 70 | 70 | 695 |
| 6 | 73 | 73 | 726 |
| 7 | 70 | 70 | 697 |
| 8 | 73 | 73 | **728** |
| 9 | 70 | 70 | 699 |

A full-rank minor modulo `5003` is a nonzero integer minor. Hence these are rigorous upper bounds over `Q`, not heuristic modular estimates.

In particular, among **all** degree-four mixed residue spaces, the formal local order cannot exceed

    728,                                               (2.1)

and only residue `8` can attain that ceiling.

This improves the structural audit over U89: its fixed-weight extremum `438` was not the true degree-four cancellation ceiling.

## 3. Exact 58-term enlargement of the U89 extremal space

The residue-eight space splits by actual weights as

    weight 8:   15 monomials,
    weight 18:  43 monomials,
    weight 28:  15 monomials.                        (3.1)

U89 used only the 43 weight-18 monomials. As the first exact mixed test, take all monomials of weights `8` and `18`, giving 58 columns.

The exact rational coefficient matrix for `S^0,...,S^56` has rank 57. After primitive integer row scaling, SymPy's `DomainMatrix` over `ZZ` returns a one-dimensional nullspace. Let `lambda` be its primitive integer generator.

The corresponding degree-four integer invariant `K_8,18` cancels all powers through `S^56`, while the coefficient of `S^57` is nonzero. Therefore its exact local `Y`-order is

    8+10*57=578.                                     (3.2)

At the already forced prime `31`, its leading rational coefficient satisfies

    numerator = 10 mod 31,
    denominator = 25 mod 31.                         (3.3)

It is therefore a 31-adic unit. Since U72 forces `31|Y`, the invariant is nonzero and

    v_31(K_8,18)=578*v_31(Y).                        (3.4)

For the fourteen-prime product

    P=433992707035920672833426144791,

all of whose primes are strong and divide `Y`, this gives

    P^578 | K_8,18.                                  (3.5)

## 4. The coefficient-height cost is severe

The primitive 58-term relation has

    max coefficient digit length = 15884,
    L1 norm digit length = 15884.                    (4.1)

Let `L=sum |lambda_i|`, `kappa=2^(4/5)`, and

    H=X+kappa Y.

Every degree-four coefficient monomial is bounded by `H^(4/17)` after discarding a favorable power of `kappa>1`. Hence

    0<|K_8,18|<L*H^(4/17).                           (4.2)

Combining (3.5), `H<3M` with `M=max(X,Y)`, and raising to the seventeenth power gives

    P^(578*17) < 81*L^17*M^4.                        (4.3)

Exact integer comparison returns

    P^(9826) > 81*L^17*10^(4*5297),
    P^(9826) < 81*L^17*10^(4*5298).                  (4.4)

Thus this exact mixed degree-four invariant proves only

    max(X,Y)>10^5297.                                (4.5)

That is far weaker than U90's cubic bound `10^25993`, despite its much larger local order `578` versus `219`.

## 5. What is proved and what is not

The finite-field scan proves that the **entire** degree-four mixed Padé program has formal local order at most `728`; it does not determine the primitive coefficient height of the unique 73-term residue-eight extremal relation.

The 58-term exact reconstruction proves that a substantial enlargement of U89's space makes the order/height tradeoff dramatically worse. It does **not** prove that the full 73-term relation is also worse than U90. That would require either:

1. exact reconstruction of the 72-by-73 residue-eight null relation; or
2. a rigorous lower bound on its primitive coefficient height strong enough to compare with U90.

In the current execution environment, direct exact nullspace calculations for the full 72-by-73 integer matrix exceeded the bounded calculation window. A separate Wolfram attempt on the full exact nullspace returned an upstream service error. Neither execution failure is mathematical evidence.

## 6. Computation audit

The exact successful calculation used Python `3.13.5` and SymPy `1.14.0` with rational arithmetic and `DomainMatrix` over `ZZ`.

The executable certificate verifies:

- all 715 degree-four monomials;
- the residue counts in (1.2);
- full modular ranks at `5003` for all ten residue classes;
- the unique maximum formal order `728` at residue `8`;
- the residue-eight weight split `15,43,15`;
- exact 57-row cancellation for the 58-term weights-8-and-18 subspace;
- exact local order `578`;
- leading residues `(10,25)` modulo `31`;
- primitive relation `L1` and maximum coefficient lengths of 15884 digits;
- both exact threshold comparisons in (4.4).

The modular rank part and exact rational reconstruction serve different purposes: the former bounds the whole degree-four space; the latter measures one actual integer relation.

## 7. Research consequence

U91 prevents a misleading conclusion from U90's suggested next step. Moving from cubic degree to the full degree-four mixed space can at most raise the local order from `219` to `728`, but the first large exact subspace already shows coefficient growth large enough to erase the benefit.

The highest-value continuation is therefore **not** to infer progress merely from a larger vanishing order. Either the full residue-eight vector must be reconstructed with a height below roughly `10^15460` to beat U90, or this Padé direction should yield priority to a different global obstruction (especially the U80 Selmer/class-group route or the corrected modular route). No weighted-equation elimination and no complete Beal result is claimed.
