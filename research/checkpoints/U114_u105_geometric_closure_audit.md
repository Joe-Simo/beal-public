# Checkpoint U114: Adversarial Audit of the U105 Geometric Closure

**Date:** 2026-09-17  
**Status:** The claimed Chabauty/degree-obstruction closure of (X^{10}+256Y^{10}=Z^{17}) is not established. The weighted equation and Beal's conjecture remain unresolved by this route.  
**Parent candidate:** `C113-03`  
**Audit mode:** Mathbox-style proof audit: identify the earliest unsupported implication and attack it directly.

## 1. Claim under audit

U105 claims that the weighted equation
[
X^{10}+256Y^{10}=Z^{17}
]
has no primitive positive integer solutions, with one purported independent proof through a genus-eight curve
[
C^-: v^2=phi+2-4(3-phi)u^{17}
]
over (k=mathbb{Q}(sqrt5)).

The geometric chain asserted in U100-U105 is roughly:

1. a hypothetical integer solution produces algebraic points on (C^-);
2. (operatorname{rank}J^-(k)le2<8), so Chabauty-Coleman applies to (C^-(k));
3. local Coleman/Strassman computations classify (C^-(k)) as ({P_infty});
4. solution points have coordinate field of degree 10 over (k), so they are not (k)-rational;
5. therefore no integer solution exists.

Two independent gaps occur before the claimed conclusion.

## 2. Gap A: the computed differentials were never shown to annihilate (J^-(k))

The repository correctly observes only the dimension statement
[
dim operatorname{Ann}(J^-(k))ge 8-operatorname{rank}J^-(k)ge6.
]

From this it then **selects**
[
eta_r=omega_{r-1},qquad r=1,dots,6,
]
as “canonical annihilating differentials.”

That inference is invalid linear algebra.

Knowing that an unknown subspace (Wsubset H^0(C,Omega^1)) has dimension at least 6 does not imply that any prescribed six basis vectors belong to (W). For example, in an 8-dimensional vector space with basis (omega_0,dots,omega_7), the 6-dimensional subspace
[
W=operatorname{span}{omega_2,omega_3,omega_4,omega_5,omega_6,omega_7}
]
contains neither (omega_0) nor (omega_1).

The file `code/U102_coleman_integration_genus8.py` computes the dimension bound but never computes a Mordell-Weil basis, its (3)-adic logarithms, or a kernel giving the actual annihilator. The GP script `code/U110_coleman_strassman_genus8.gp` simply prints:

> “We consider the 6 independent canonical annihilating differentials: eta_r = omega_{r-1}.”

No preceding calculation proves that assertion.

### Consequence

All subsequent Strassman calculations on those chosen (eta_r) certify local power-series properties of ordinary holomorphic differentials, but they do **not** certify zeros of Coleman functions known to vanish on (C^-(k)).

In particular:

- the condition used at infinity, “choose (omegainoperatorname{Ann}(J^-(k))) with (c_7
otequiv0pmod3),” is not shown to be satisfiable;
- a 6-dimensional annihilator may lie entirely in the 7-dimensional hyperplane (c_7=0);
- on the ordinary discs, the scripts do not compute the global integration constants (int_{P_infty}^{Q_i}eta_r) for verified annihilating forms, yet those constants are essential to locating zeros of the actual Chabauty functions.

Therefore the claimed classification
[
C^-(k)={P_infty}
]
is not established by the recorded Coleman scripts.

## 3. Gap B: classifying (C^-(k)) would still not exclude the recorded Diophantine points

U100 and U102 explicitly state that a hypothetical positive integer solution does **not** yield a (k)-rational point on (C^-). Instead, the construction yields a Galois orbit over an extension of degree 10 over (k), and the orbit is said to define a (k)-rational divisor/divisor class.

Thus even a valid proof of
[
C^-(k)={P_infty}
]
would only classify degree-1 (k)-rational points.

It does not classify effective degree-(d) divisors or closed points of degree (d>1).

The standard geometric object for effective degree-(d) divisors is the symmetric power
[
C^{(d)}=operatorname{Sym}^d C,
]
whose (k)-points correspond to effective degree-(d) divisors. Literature on “symmetric Chabauty” exists precisely because ordinary Chabauty on (C(k)) is not the same problem as determining (C^{(d)}(k)) or degree-(d) points. See Jennifer Park, *Effective Chabauty for symmetric powers of curves*, arXiv:1606.05195.

The repository itself contains inconsistent degree language:

- U100 says a solution yields an effective degree-5 divisor whose points lie in a degree-10 extension;
- U102 describes a degree-10 Galois orbit;
- U105 reduces the issue to the fact that ([k(u,v):k]=10
e1).

Those statements require a precise divisor/orbit reconstruction before a Chabauty argument can address the Diophantine solution set.

### Consequence

“Solution point is not in (C^-(k))” is not an obstruction. It is a property already built into the auxiliary-field construction.

To exclude the solution through this geometric route one would need, for example, a valid argument on the relevant symmetric power, or a proof that the associated (k)-rational divisor class cannot exist in (J^-(k)). The rank bound
[
operatorname{rank}J^-(k)le2
]
does not by itself imply (J^-(k)=0), nor does it eliminate a specific nonzero divisor class.

## 4. What remains valid

This audit does **not** refute the following isolated facts merely by finding the two gaps above:

- the displayed algebraic identities for the curve model;
- the genus calculation;
- the finite-field point count (#C^-(mathbb F_9)=10);
- local Taylor expansions of the listed differentials;
- the assertion that positive solutions, under the recorded dictionary, are not expected to give (k)-rational points;
- any independent modular-method proof of the weighted equation, if that proof can be reconstructed without the failed geometric steps.

The audit only removes the claim that the recorded Chabauty/degree argument independently proves non-existence.

## 5. Research-population outcome

### Candidate `C114-01`
- **Objective:** use classical Chabauty on (C^-/k) to eliminate weighted-equation solutions.
- **Status:** **REFUTED as currently implemented**.
- **Failure mechanism 1:** annihilating forms were assumed from a dimension count instead of computed.
- **Failure mechanism 2:** (C^-(k)) is the wrong point set for degree-10 solution orbits.
- **Reusable component:** the curve model and local expansions may still be useful after the actual Mordell-Weil annihilator and the correct symmetric-power/divisor problem are specified.

### Evolved candidate `C114-02`
- **Status:** **ACTIVE**.
- **Objective:** reconstruct the exact solution divisor (D(X,Y,Z)), its degree, its Galois orbit, and its Abel-Jacobi class in (J^-(k)); then determine whether a symmetric-power Chabauty/Mordell-Weil-sieve argument is feasible.
- **First obligation:** resolve the U100/U102 degree-5 versus degree-10 discrepancy and prove the exact map into (C^{(d)}(k)).
- **Stop condition:** if the map or claimed (k)-rational divisor class is not well-defined, abandon this geometric route rather than repairing downstream Coleman computations.

## 6. Next route

The overall weighted-equation candidate `C113-03` remains **VERIFICATION_REQUIRED** because U105 also asserts a separate Hilbert modular/level-lowering pathway. The next discriminating audit should attack the earliest external theorem/application in that modular chain rather than treating the failed geometric route as proof that the equation has solutions.

