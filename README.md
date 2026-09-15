# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest checkpoint: U72 full coefficient support

[U72](research/checkpoints/U72_root_closed_order_and_full_support.md) refines U71's common integral seventeenth root for the primitive positive weighted equation `X^10+256Y^10=Z^17`.

With `c=i*2^(4/5)`, it proves that this root belongs to the smaller order `Z[c]`, not only the full integer ring. All ten coefficients in the fixed basis `1,c,...,c^9` are nonzero. If `e=v17(Y)>=2`, their valuations are exactly `j(e-1)` for `j=0,...,9`. Exact profiles at the fourteen inherited forcing primes give additional divisibility of the same coefficients.

Using these divisibilities and all ten complex embeddings, a putative weighted solution must satisfy **`max(X,Y)>10^4810`**, so one left-hand base has at least 4811 decimal digits. This replaces the earlier necessary 515-digit threshold for this auxiliary equation; it does not apply to every possible Beal counterexample.

**This remains a necessary-condition theorem, not an impossibility proof.** The common-root local disk at 17 survives with all ten coefficients nonzero. There is no upper bound or global integral-point exclusion. The priority is to resolve the remaining global coefficient equations, not merely lengthen a finite forcing-prime list.

Verification is written self-review with distinct Python and TypeScript methods and separate Wolfram corroboration, not independent expert or proof-assistant certification. U71's complete Python output was replayed unchanged. The new proof, exact checkers, reproduction commands and compact certificates are preserved; the evidence archive additionally contains the full outputs, logs and unchanged U71 archive.

## Retained research and corrections

[U71](research/checkpoints/U71_common_decic_seventeenth_root.md) supplies the common root and `289|Y`. The weighted application of U72 inherits that self-reviewed proof; it does not invoke the earlier Q65 unit elimination or a boundary-curve congruence.

U68–U70 contain earlier height and prime-support restrictions. Their historical lower bounds are not impossibility statements. U61/U62 retain their separate, limited coefficient-two claims and outstanding independent-verification obligations.

**U41 remains invalidated by U63.** The boundary congruence and unresolved global modular prerequisites are not reinstated. No new complete Beal exponent family is marked solved.

The previous index is retained unchanged in [README before U72](references/U72/README_before.md). No prior mathematical checkpoint was overwritten.

## Original target

For positive integers A,B,C,x,y,z with `A^x+B^y=C^z` and `x,y,z>=3`, prove `gcd(A,B,C)>1` or exhibit an independently verified counterexample. All bases and exponents remain unbounded. None of the partial results here resolves that statement.
