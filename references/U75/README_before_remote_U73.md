# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest checkpoint: U73 fixed curve and verified limitations

[U73](research/checkpoints/U73_genus_eight_reduction.md) maps the common seventeenth root to the fixed genus-eight curve

    (3-phi)V^2=4U^17-phi^2, phi=(1+sqrt(5))/2.

The resulting point has coordinate field exactly `Q(2^(1/5),i,sqrt(5))`, degree twenty over Q and degree ten over `Q(sqrt(5))`. Searching only points rational over the latter field cannot cover positive weighted solutions. A source-checked CM argument proves the Jacobian absolutely simple, so this curve has no elliptic quotient or quotient of genus two through seven, even over an algebraic closure in characteristic zero.

The extra condition `V=R^17`, with R in the degree-ten common field and relative norm one, is retained explicitly. It gives a genus-256 cover; arbitrary points on either curve are not automatically weighted solutions. Local common-root examples continue to satisfy the new identities.

**No new integer range, prime class, or complete Beal signature is eliminated in U73.** This is a written/self-reviewed global reduction and a rigorous rejection of two shortcuts, not an impossibility theorem. The required global points, ranks, and upper bounds remain unclassified. Independent expert or proof-assistant verification is outstanding.

The proof, both exact verifiers, reproduction commands, source mapping and core certificates are preserved. Python and TypeScript agree on every tested local vector; Wolfram corroborates the algebra and corrected subgroup inventory. The evidence package retains full outputs and logs, including a rejected preliminary Wolfram expression and the unchanged local constants-U72 archive.

## Two distinct continuations numbered U72

The remote [full-support U72](research/checkpoints/U72_root_closed_order_and_full_support.md) is distinct from the locally delivered `U72_common_root_constant_obstructions.md`. Neither was silently replaced or treated as an alternate filename. Their exact identifiers are in [U73 sources](references/U73/sources.json). The constants-U72 archive is preserved in the delivered U73 package; its old relative source paths are not claimed as newly uploaded to this repository.

The remote full-support U72 retains its written/self-reviewed coefficient profiles and weighted lower bound `max(X,Y)>10^4810`. U73 neither increases that bound nor relies on it. The new reduction uses [U71](research/checkpoints/U71_common_decic_seventeenth_root.md), whose arithmetic was replayed, as the explicit source of the common root and `289|Y`.

## Retained work and original target

U68–U70 contain earlier necessary height and support restrictions, not impossibility theorems. U61/U62 concern the separate coefficient-two equation and retain their prior limited status. **U41 remains invalidated by U63.** The unproved boundary congruence and global modular prerequisites are not reinstated.

The preceding remote index is preserved unchanged in [README before U73](references/U73/README_before.md). No earlier mathematical checkpoint was overwritten.

For positive integers A,B,C,x,y,z with `A^x+B^y=C^z` and `x,y,z>=3`, the original goal is to prove `gcd(A,B,C)>1` or exhibit an independently verified counterexample. All bases and exponents remain unbounded. The weighted equation and full conjecture remain unresolved.
