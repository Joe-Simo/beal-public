# Beal Conjecture Research

Private research workspace. **Beal's conjecture is not solved.**

## Latest checkpoint: U77 missing quadratic-twist component

[U77](research/checkpoints/U77_anti_invariant_twist_reduction.md) proves that a positive primitive weighted solution would give an infinite-order class on the Jacobian of

    (3-phi)w^2=phi^2-4u^17, phi^2-phi-1=0,

now over the real quadratic field Q(sqrt(5)). This is the opposite quadratic twist to the earlier U73 model, not an interchangeable sign. The new Jacobian has trivial rational torsion. A weighted solution would therefore require positive rank of this one explicit genus-eight Jacobian.

The construction proves that the required degree-five orbit class is outside the entire smaller-field subgroup J_F(Q(zeta_5)), even after saturation and addition of torsion. In particular the fifteen known U75 generators and U76's index-17 enlargement, all defined over that smaller field, cannot alone capture a weighted solution. This does not invalidate their rank lower bound or index calculation; it identifies the missing extension component.

**No rank-zero result is established.** The attempted unconditional Magma calculation returned a browser-tool timeout with no calculation output. A bounded affine search is retained only as exploration. The new nonvanishing proof, torsion calculation, and subgroup exclusion are written/self-reviewed partial theorems, not a proof that the weighted equation has no solutions.

Python and TypeScript agree on their entire exact output, including three twist-specific reduction orders and both complete finite cyclic-orbit examples. Wolfram corroborates the key identities and all three orders. Independent expert or proof-assistant verification remains outstanding. The remaining task is a certified rank upper bound, or another global exclusion for the relevant infinite-order class; no effective upper height bound or full point classification is supplied.

## Continuity and retained work

U76's unchanged local proof and archive are retained in the delivered U77 evidence package. Its full Python output was replayed exactly. The historical remote index is preserved in [README before U77](references/U77/README_before_remote_U75.md); the prior local index is also retained. Files not explicitly present in a remote commit are not silently represented as pushed.

[U75](research/checkpoints/U75_jacobian_decomposition_and_infinite_order_classes.md) supplies the genus-eight factor decomposition, exact factor torsion and fifteen independent classes. [U71](research/checkpoints/U71_common_decic_seventeenth_root.md) supplies the common-root theorem used for the weighted application. These remain inherited written/self-reviewed results, not independent certifications. U77's rank condition does not imply that rank zero has been proved.

U68-U72 contain necessary height and support bounds, not upper bounds or impossibility statements. U61/U62 retain their separate coefficient-two scope and outstanding verification requirements. **U41 remains invalidated by U63.** No unproved boundary congruence or global modular prerequisite is reinstated, and no new complete Beal signature is marked solved.

## Original target

For positive integers A,B,C,x,y,z with A^x+B^y=C^z and x,y,z>=3, prove gcd(A,B,C)>1 or produce an independently verified counterexample. All bases and exponents remain unbounded. The weighted equation X^10+256Y^10=Z^17 and the full Beal conjecture remain unresolved.
