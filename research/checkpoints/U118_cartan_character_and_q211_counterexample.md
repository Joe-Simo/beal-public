# Checkpoint U118: Cartan-Character Match and Exact q=211 Counterexample to Uniform Orbit-b Forcing

**Date:** 2026-09-17  
**Status:** PARTIAL_RESULT / ROUTE REFUTATION. Orbit b is still not eliminated. Two proposed shortcuts have now been discriminated: the local quadratic-character comparison agrees with the CM obstruction rather than contradicting it, and the proposed infinite auxiliary-prime forcing statement is false by an exact counterexample at q=211.  
**Parents:** C117-03, U63, U64, U71, U97, U102, U113, U117.

Nothing in this checkpoint proves or disproves the weighted equation
[
X^{10}+256Y^{10}=Z^{17}
]
or the full Beal conjecture.

## 1. CM quadratic character of orbit b

The surviving Hilbert newform orbit b is the boundary CM constituent associated with
[
L=mathbb Q(zeta_5),qquad K=mathbb Q(sqrt5),
]
where (L/K) is quadratic.

Write
[
phi=rac{1+sqrt5}{2},qquad pi=phi+2=rac{5+sqrt5}{2}.
]
Then
[
N_{K/mathbb Q}(pi)=5
]
and
[
(zeta_5-zeta_5^{-1})^2=-pi.
]
Hence
[
L=K(sqrt{-pi}).
]

### At the prime above 2

The exact factorizations
[
Phi_5(T)=T^4+T^3+T^2+T+1
]
and
[
T^2-T-1
]
remain irreducible modulo (2). Thus (2) is inert in (L/mathbb Q), inert in (K/mathbb Q), and the unique prime (mathfrak p_2) of (K) is inert in the relative quadratic extension (L/K).

Therefore the CM quadratic character (chi_b) is:
- unramified at (mathfrak p_2);
- nontrivial on Frobenius at (mathfrak p_2).

This matches the local negative-Frey representation from U63: its tame inertia is the order-5 rotation subgroup and Frobenius acts by inversion, so the quotient by the Cartan is also unramified and nontrivial at (mathfrak p_2).

### At the prime above 5

Because
[
L=K(sqrt{-pi})
]
with (v_{mathfrak p_5}(pi)=1), the extension (L/K) is ramified at the unique prime (mathfrak p_5mid5).

This again matches the local D5 structure recorded for the negative Frey curve: the order-5 rotation lies in the Cartan and the order-2 reflection maps nontrivially to the Cartan-normalizer quotient.

### Consequence

The first character-comparison discriminator does **not** eliminate orbit b.

At both fixed bad primes (2) and (5), the Frey dihedral quotient behaves exactly like the CM quadratic character of (K(zeta_5)/K).

This is an informative failure, not evidence for a solution.

## 2. Residual-characteristic prime 17: why a naive niveau-2 shortcut is unsafe

Since (17) is inert in (K=mathbb Q(sqrt5)), the completion (K_{mathfrak p_{17}}) is the unramified quadratic extension of (mathbb Q_{17}), and the residual coefficient field for the RM component is (mathbb F_{17^2}).

For weight-2 finite-flat/supersingular representations over an unramified degree-(f) local field, Raynaud/Serre-weight theory permits fundamental-character levels reflecting the residue degree. In this setting, a niveau-4 local type is a genuine possibility.

This matters because:
- a niveau-2 projective inertia order (17+1=18) would contain a factor 3;
- a nonsplit Cartan normalizer in (mathrm{PGL}_2(mathbb F_{17^2})) has Cartan order (17^2+1=290), with no factor 3;
- but a niveau-4 projective inertia order (17^2+1=290) fits that nonsplit Cartan exactly.

Therefore the repository's earlier casual use of “niveau 2 at 17” cannot be promoted into a Cartan contradiction without a source-level computation of the exact finite-flat local type of this RM component.

The local geometry also gives a reason to expect compatibility rather than contradiction: U71 gives (17^2mid Y), so
[
V=2Y^2
]
is divisible by (17^4). The actual Frey model is therefore highly 17-adically close to its boundary (V=0) CM specialization.

The p=17 Cartan-quotient ramification question remains a verification obligation rather than an elimination theorem.

## 3. Refuted proposed route: “every split prime forces q|Y”

A tempting escape from orbit b was:

> For every good rational prime (qequiv1pmod5), congruence of the Frey residual representation with orbit b forces (Vequiv0pmod q), hence (qmid Y).

If true uniformly for infinitely many primes, a fixed nonzero (Y) would be impossible.

U102 only checked this at (q=11,31,41). It did not prove the universal statement.

An exact counterexample now refutes that extrapolation.

## 4. Exact q=211 local counterexample

Take
[
q=211.
]

This is a good split prime:
[
211equiv1pmod5,qquad 211
otin{2,5,17}.
]

Use the square-structured residues
[
Xequiv1,qquad Yequiv31,qquad Zequiv4pmod{211}.
]

Then
[
U=X^2equiv1,
]
and
[
V=2Y^2equiv 2cdot31^2equiv23
otequiv0pmod{211}.
]

The generalized-Fermat relation holds locally:
[
U^5+8V^5equiv Z^{17}pmod{211}.
]

More explicitly,
[
23^5equiv-1pmod{211},
]
so
[
1+8cdot23^5equiv-7equiv204pmod{211},
]
and
[
4^{17}equiv204pmod{211}.
]

Thus this is an admissible **non-boundary** local parameter.

## 5. Exact Frobenius calculation

For the negative genus-2 Frey curve
[
C^-_{U,V}:
y^2=
-Bigl(
x^5+40UVx^3+320U^2V^2x+64(8V^5-U^5)
Bigr),
]
define the rational-prime invariants
[
S=a_{mathfrak q_1}+a_{mathfrak q_2},
qquad
P=a_{mathfrak q_1}a_{mathfrak q_2},
]
from point counts over (mathbb F_q) and (mathbb F_{q^2}).

### Boundary (U=1,V=0)

Exact counts:
[
#C^-_{1,0}(mathbb F_{211})=193,
]
[
#C^-_{1,0}(mathbb F_{211^2})=44983.
]

Hence
[
(S,P)=(19,-11),
]
so modulo 17
[
(S,P)equiv(2,6).
]

### Non-boundary (U=1,V=23)

Exact counts are **identical**:
[
#C^-_{1,23}(mathbb F_{211})=193,
]
[
#C^-_{1,23}(mathbb F_{211^2})=44983.
]

Therefore
[
(S,P)=(19,-11)
]
exactly, not merely modulo 17.

So the nonzero square-structured parameter (V=23) matches orbit b's boundary Frobenius invariants perfectly at q=211.

## 6. Five nonzero matches

The complete fifth-root class gives five matching nonzero projective parameters:
[
V/Uin{23,104,140,156,210}.
]

For each,
[
(V/U)^5equiv-1pmod{211},
]
the required twice-square condition holds, and the exact Frobenius pair remains
[
(S,P)=(19,-11).
]

The reproducible checker is:
- `code/U118_q211_orbit_b_counterexample.py`.

It uses exact integer arithmetic and counts points directly in
[
mathbb F_{211}
]
and
[
mathbb F_{211^2}=mathbb F_{211}[s]/(s^2-2).
]

## 7. Independent Wolfram verification

A separate Wolfram calculation used the same field
[
mathbb F_{211^2}=mathbb F_{211}[s]/(s^2-2),
]
but independently recomputed the quadratic character via the norm.

It returned:

- (23^5mod211=210=-1);
- (1+8cdot23^5mod211=204);
- (23/2) is a quadratic residue modulo 211;
- boundary:
  [
  (N_1,N_2,S,P)=(193,44983,19,-11);
  ]
- non-boundary (V=23):
  [
  (N_1,N_2,S,P)=(193,44983,19,-11).
  ]

Thus the q=211 counterexample to the **uniform forcing lemma** has two exact implementations.

It is not a Beal counterexample and does not lift an integer solution.

## 8. Why this matters

The proposed route

> residual congruence to b + all (qequiv1pmod5) ⇒ (qmid Y)

is false.

Therefore no proof may extrapolate the successful q=11,31,41 local sieve to all split primes without a new theorem describing exactly which primes and which residue parameters are forcing.

This also invalidates one of U102's informal global extrapolations independently of the already-refuted Baker-bound argument.

## 9. Structural observation from the counterexample

For any parameter (t=V/U) with
[
t^5=-1,
]
the substitution
[
x=t^3 X
]
removes (t) from the quintic shape because
[
t^{15}=-1,qquad t^{10}=1,qquad t^5=-1.
]

The family specializes to a fixed non-boundary genus-2 curve. Hence the five q=211 matches are one geometric isomorphism class rather than five unrelated accidents.

At q=11 the same fixed non-boundary class has
[
(S,P)=(-3,-9),
]
which does not match the boundary pair ((9,19)). At q=211 the two classes happen to have the same Frobenius polynomial.

This points toward a Chebotarev-style interpretation: nonforcing primes should be expected whenever the two fixed residual representations have coincident Frobenius data on some conjugacy classes. Establishing an actual density is a separate problem and is not claimed here.

## 10. Research-population outcome

### C117-03 — BLOCKED
**Objective:** eliminate b by comparing its inducing quadratic character with the Frey Cartan quotient.

**Outcome:** the exact local behaviors at 2 and 5 agree. The 17-adic type requires a more careful inert-prime finite-flat analysis; no contradiction is established.

### C118-01 — REFUTED
**Objective:** prove that every good (qequiv1pmod5) forces (V=0) under orbit-b congruence.

**Failure:** exact admissible nonzero counterexample at (q=211), (U=1,V=23), with identical boundary Frobenius invariants.

### C118-02 — PARTIAL_RESULT
**Objective:** identify a reusable nonforcing mechanism.

**Result:** the locus (t^5=-1) collapses to a fixed non-boundary genus-2 isomorphism class after (x=t^3X); q=211 is a prime where this class and the boundary class have identical Frobenius data.

### C118-03 — ACTIVE / RESTART
**Objective:** attack orbit b through a genuinely global mechanism rather than another one-prime sieve.

**Recommended mechanisms:**
1. characterize the RM 17-isogeny/Cartan locus of the Frey one-parameter family over (K(zeta_5));
2. combine the modular congruence with the independent Gaussian/common-root descent, using a relation that cannot be satisfied by the boundary Cartan specialization;
3. if a second Frey representation exists for the same weighted solution, use a multi-Frey incompatibility so that the boundary CM form cannot serve both residual systems.

The next discriminating step is to search the existing descent tree for an invariant that distinguishes the nonzero parameter from the boundary **globally**, not merely modulo finitely many auxiliary primes.

## 11. Jev status

No callable Jev/Typesafe runtime is exposed in this session. No mathematical conclusion is attributed to Jev.

The persistent population continues to use the requested bounded routing fields as transparent research-management metadata only.

