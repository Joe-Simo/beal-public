# Checkpoint U116: Repaired Breuil–Diamond Bridge for the Weighted (5,5,17) Equation

**Date:** 2026-09-17  
**Status:** PARTIAL_RESULT. The Breuil–Diamond level-lowering bridge can be reconstructed coherently for the genus-2 negative Frey representation, subject to the explicitly retained upstream arithmetic/local claims below. This checkpoint does **not** prove (X^{10}+256Y^{10}=Z^{17}) has no primitive solutions and does **not** solve Beal's conjecture.  
**Parent candidate:** `C115-02`  
**Supersedes:** the false Allen–Khare–Thorne citation and the mixed genus-8/genus-2 synthesis in U101/U105.

## 1. Fixed object

Assume a primitive positive solution
[
X^{10}+256Y^{10}=Z^{17},qquad gcd(X,Y)=1.
]
As in U63, (X,Z) are odd. Put
[
U=X^2,qquad V=2Y^2,
]
so
[
U^5+8V^5=Z^{17}.
]

For (r=5), (A=1), (B=8), (a=U), (b=V), Azon's/Kraus's signature-((r,r,p)) hyperelliptic model is exactly
[
C^+:quad y^2=f_{U,V}(x)
]
with
[
f_{U,V}(x)
=x^5+40UVx^3+320U^2V^2x+64(8V^5-U^5).
]

The curve used in the repaired repository route is the quadratic twist
[
C^-:quad y^2=-f_{U,V}(x).
]

This is a **genus-2** curve. Its Jacobian (J^-) is an abelian surface carrying real multiplication by
[
K=mathbf Q(sqrt5).
]

No genus-8 auxiliary Jacobian is used anywhere in this checkpoint.

### Source match

Azon, *Effective Darmon's program for the generalised Fermat equation*, arXiv:2504.01967v2:
- Proposition 3.22 / the signature-((r,r,p)) specialization gives the coefficient-dependent Frey curve;
- §5.1 proves modularity of the negative compatible system;
- the paper explicitly notes that quadratic twists preserve the modularity input.

Thus the object mismatch identified in U115 is repaired.

## 2. Exact Breuil–Diamond theorem used

Breuil–Diamond, *Formes modulaires de Hilbert modulo p et valeurs d'extensions entre caractères galoisiens*, Théorème 3.2.2 (printed pp. 36–37), requires:

1. (p>2);
2. a modular residual representation (arho);
3. (arho|_{G_{F(zeta_p)}}) irreducible;
4. a determinant lift (psi) with (psiarepsilon^{-1}) finite order;
5. a finite set (S) containing all (p)-adic places and all places where (arho) or (psi) ramifies;
6. for each (vin S), an **actual characteristic-zero local lift** (ho_v) satisfying the listed Hodge–Tate, ordinarity, Weil–Deligne, subrepresentation, and determinant-on-inertia conditions.

The conclusion is a global modular lift of parallel weight 2, unramified outside (S), with the prescribed local types.

Crucially, Théorème 3.2.2 does **not** require us to prove
[
R_v^{	au,psi}congmathcal O
]
or to derive local-lift uniqueness from Maschke's theorem.

Therefore the deformation-ring assertions in U98/U101 are unnecessary for this application and are not used here.

Primary source inspected directly:
https://www.imo.universite-paris-saclay.fr/~breuil/PUBLICATIONS/extensions.pdf

## 3. Residual modularity: repaired source

U101 incorrectly cited Allen–Khare–Thorne (2021), Theorem 1.2, as a general residual modularity theorem for arbitrary mod-17 representations. U115 refuted that citation.

A valid source exists.

Azon's Theorem 5.5 proves that the compatible system attached to the negative Frey Jacobian is modular. Hence every residual specialization of that system, including the prime over (17), is modular.

The quadratic twist (C^-) differs from the untwisted coefficient-dependent Frey curve by the character of (K(i)/K); modularity is preserved by character twist.

Thus Breuil–Diamond's residual modularity hypothesis is supplied by Azon's actual compatible-system theorem, not by Allen–Khare–Thorne.

## 4. Residual irreducibility over (K(zeta_{17}))

### 4.1 Local irreducibility at the prime over 2

U63 supplies a direct local model for the negative twist over
[
F=K_{mathfrak p_2}=mathbf Q_2(sqrt5).
]

Let (pi^5=2). With
[
x=pi^8t,qquad y=16w+8kappa,qquad
kappa^2=X^{10}-256Y^{10},
]
the curve becomes an integral model reducing to
[
w^2+w=t^5
]
over (mathbf F_4).

The special fiber is smooth, so the curve acquires good reduction over the tame degree-5 extension. Tame inertia acts with characteristic polynomial
[
Phi_5(T)=T^4+T^3+T^2+T+1
]
on (H^1). On each two-dimensional RM component the two characters are a nontrivial inverse pair of fifth-order characters.

The residue-field Frobenius has cardinality (4), hence sends
[
zeta_5mapstozeta_5^4=zeta_5^{-1},
]
so it swaps the two inertia eigenspaces. Modulo (17) they remain distinct. Therefore the local residual two-dimensional component is absolutely irreducible.

This argument also gives conductor exponent
[
n_{mathfrak p_2}=2
]
per RM component for the negative twist.

### 4.2 Clifford-theory argument after adjoining (zeta_{17})

Since (K=mathbf Q(sqrt5)) and (mathbf Q(zeta_{17})) have disjoint ramification,
[
[K(zeta_{17}):K]=16
]
and the extension is cyclic.

Suppose (arho|_{G_{K(zeta_{17})}}) were reducible. Clifford theory for a two-dimensional irreducible representation with cyclic quotient forces (arho) to be induced from the unique quadratic intermediate extension
[
K(sqrt{17})/K.
]

But
[
17equiv1pmod8,
]
so (sqrt{17}inmathbf Q_2). Hence the prime (mathfrak p_2) splits in (K(sqrt{17})/K). Restricting an induced representation to the split local decomposition group would make it reducible, contradicting §4.1.

Therefore
[
arho|_{G_{K(zeta_{17})}}
]
is absolutely irreducible.

This provides the exact Breuil–Diamond cyclotomic-restriction hypothesis without Azon's Hypothesis 5.

## 5. Why Azon's Hypothesis 5 remains unavailable

For the signature-((5,5,17)) specialization, the negative valuations of the common parameter away from fixed coefficient primes are multiples of (r=5). Thus the project does **not** obtain a prime
[
q'
mid10
]
with negative valuation nonzero modulo (5), as demanded by Azon's Hypothesis 5.

Consequently Azon's packaged Theorem 5.22 cannot simply be invoked as a black box for this specialization.

The repaired route instead uses:
- Azon for modularity and local conductor information;
- the independent §4 cyclotomic irreducibility argument;
- Breuil–Diamond Théorème 3.2.2 directly.

## 6. The local lifts required by Breuil–Diamond

The key simplification is to use the **geometric 17-adic representation of (J^-) itself** as the characteristic-zero lift at the fixed places. Its reduction is (arho) by construction, and its local Weil–Deligne type is the geometric type already computed from the curve.

### 6.1 Prime (mathfrak p_2)

From §4.1:
- potential good reduction over a tame degree-5 extension;
- (N=0);
- inertia type with fifth-order characters;
- conductor exponent (2);
- an actual characteristic-zero local lift is
  [
  ho_{J^-,17}|_{G_{K_{mathfrak p_2}}}.
  ]

Because (v
mid17) and (N=0), Breuil–Diamond conditions (i), (ii), and (iv) do not impose additional requirements there.

### 6.2 Prime (mathfrak p_5=(sqrt5))

The exact translated quintic is Eisenstein at 5 whenever (5
mid Z), and the direct local analysis in U98 gives potential good reduction with conductor exponent (3) on the relevant two-dimensional RM component.

The actual geometric local representation
[
ho_{J^-,17}|_{G_{K_{mathfrak p_5}}}
]
is the required characteristic-zero lift.

This checkpoint does **not** use U98's stronger assertion that Maschke semisimplicity implies a unique deformation ring (mathcal O).

### 6.3 Prime (mathfrak p_{17})

To keep the lowered level prime to 17 we need (17
mid Z).

U71 proves the stronger necessary condition
[
17^2mid Y,
]
hence primitivity gives (17
mid Z).

One finite discriminator in that proof was independently replayed in Wolfram during this audit. For the three Gaussian factorization cases modulo 11, the fifth-power image is
[
{0,1,-1},
]
and the surviving pair counts are exactly
[
	ext{I}:0,qquad 	ext{II}:0,qquad 	ext{III}:10,
]
with all ten survivors in III satisfying (Bequiv0pmod{11}), matching U71's recorded calculation.

This replay independently checks that finite step; it is **not** an independent proof of every class-number/unit argument in U71.

Given (17
mid Z), the Frey discriminant has zero 17-adic valuation, so (J^-) has good reduction at (mathfrak p_{17}). The 17-adic representation is crystalline with Hodge–Tate weights ({0,1}). The geometric representation itself supplies the required local lift.

The repository's additional supersingularity calculation is not needed merely to establish local-lift existence. If an ordinarity choice is required for the exact local type, it must be matched to the actual geometric representation, not inferred from a generic deformation ring.

## 7. Determinant choice

Rather than postulating a new determinant character, use the determinant character of the already modular characteristic-zero compatible system supplied by Azon.

Because this is a parallel-weight-2 modular system, its determinant has the required form
[
psi=arepsiloncdoteta
]
with (eta) finite order. It reduces to (detarho) and, since the local lifts in §6 are restrictions of the same geometric system, their determinants agree with (psi) on inertia automatically.

This is exactly the compatibility Breuil–Diamond asks for; no assertion that every local deformation ring is one-dimensional is needed.

## 8. Ramification set and the solution-dependent primes

Take
[
S={mathfrak p_2,mathfrak p_5,mathfrak p_{17}}.
]

This is valid only if both (arho) and (psi) are unramified away from these places.

For a prime (qmid Z), (q
otin{2,5,17}), the relevant toric valuation is a multiple of (17). Azon's residual-unramifiedness theorem therefore removes (q) from the residual conductor. The determinant on such toric local representations is cyclotomic up to an unramified finite-order character, so (psi) is unramified there as well.

At primes dividing (UV) away from (2,5), the specialized discriminant is a unit under primitivity, so the geometric representation is unramified.

Thus the solution-variable primes do not have to be inserted into (S).

Breuil–Diamond Théorème 3.2.2 then produces a parallel-weight-2 modular lift unramified outside (S), with the chosen local types.

## 9. Resulting fixed level

The conductor exponents of the selected local types are
[
n_{mathfrak p_2}=2,qquad n_{mathfrak p_5}=3,qquad n_{mathfrak p_{17}}=0.
]

Hence the predicted fixed Hilbert level is
[
mathfrak N=mathfrak p_2^2mathfrak p_5^3.
]

In (K=mathbf Q(sqrt5)):
- (2) is inert, so (operatorname N(mathfrak p_2)=4);
- (5) is ramified, so (operatorname N(mathfrak p_5)=5).

Therefore
[
operatorname N(mathfrak N)=4^2cdot5^3=2000.
]

This is the coherent mathematical origin of the repository's “level 2000” target.

## 10. What this checkpoint does and does not establish

### Established at the current written/source-audited level

- The correct coefficient-dependent Frey object is genus 2 and matches Azon's ((5,5,p)) framework.
- The negative twist has the required (2)-adic conductor-2 local model and local residual irreducibility.
- The restriction to (G_{K(zeta_{17})}) is irreducible by an independent Clifford/local-splitting argument.
- Azon's compatible-system modularity replaces the false Allen–Khare–Thorne citation.
- Breuil–Diamond requires actual local lifts, not the deformation-ring isomorphisms claimed in U98/U101.
- Using geometric local lifts yields the fixed norm-2000 level, provided the retained upstream U71 (17
mid Z) conclusion and the prime-5 conductor computation are valid.

### Not established

- No Hilbert-newform orbit at level 2000 is eliminated by this checkpoint.
- The repository's previous “all seven non-CM orbits + CM orbit eliminated” claim has not been re-authenticated here.
- The U97/U102 deformation/CM arguments remain suspect because several were downstream of the now-refuted U105 synthesis.
- No claim that the weighted equation is solved is made.
- No statement about the full Beal conjecture follows yet.

## 11. Next discriminating action

Audit the **level-2000 newform inventory and elimination from scratch** while keeping only the genus-2 representation fixed above.

The first questions are:
1. Does the computed Hilbert newspace over (K=mathbf Q(sqrt5)) at (mathfrak p_2^2mathfrak p_5^3) really have exactly the recorded Hecke constituents?
2. Can each non-CM constituent be eliminated by authenticated prime-ideal-labelled Hecke data rather than array offsets?
3. Does a CM constituent remain, and if so can it be eliminated by a representation-theoretic argument that does not use the invalid genus-8 Chabauty route or unsupported deformation-ring uniqueness?

A negative answer at any one of these stages blocks the claimed weighted-equation closure and must be preserved rather than patched by assertion.
