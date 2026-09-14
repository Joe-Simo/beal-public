# Certified lemma: sigma^2 acts through coefficient conjugation on r,s,v,w

Date: 2026-09-14

## Scope

This lemma concerns only the four Case-2 Hilbert newform constituents left by the l=5 sieve in Michaud-Jacobs' treatment of x^(2l)+y^(2m)=z^17. It does not resolve that generalized-Fermat equation by itself, and it does not resolve Beal.

## Statement

Let F be the cyclic quartic field with LMFDB label 4.4.4913.1, represented as

F = Q(w),  w^4-w^3-6w^2+w+1=0.

Let sigma generate Gal(F/Q), with

sigma(w) = -w^3/2 + 3w + 3/2,

so

sigma^2(w) = w^3-w^2-6w+1.

Let r,s,v,w denote the Hilbert newform constituents with LMFDB labels

4.4.4913.1-272.1-r,
4.4.4913.1-272.1-s,
4.4.4913.1-272.1-v,
4.4.4913.1-272.1-w.

For r,s let K2=Q(e), e^2+2e-4=0, and let

tau2(e)=-e-2.

For v,w let K6=Q(e),

P6(e)=e^6+3e^5-42e^4-104e^3+364e^2+428e+104=0,

and let

tau6(e)=e^5/4-e^4/4-17e^3/2+5e^2+41e+17.

Then, for each of the four constituents f,

f^(sigma^2) = f^tau,

where tau is tau2 for r,s and tau6 for v,w. Equivalently, for every prime ideal Q away from the level,

a_{sigma^2(Q)}(f) = tau(a_Q(f))

(up to the harmless inverse convention for the base-field action; sigma^2 is its own inverse).

## Exhaustive newform-space input

The LMFDB API for field 4.4.4913.1 and level 272.1 lists exactly 24 newform constituents with dimensions

1 repeated 17 times,
2,2,
4,4,
6,6,
8.

In particular, the only dimension-2 constituents are r and s, and the only dimension-6 constituents are v and w.

This agrees with the author's Magma output: constituents 18 and 19 have Hecke-field degree 2 and are the only two such constituents; constituents 22 and 23 have degree 6 and are the only two such constituents.

Because the level is 2*P17, with 2O_F and the unique prime P17 above 17 both Gal(F/Q)-stable, base conjugation by sigma^2 preserves the level, parallel weight 2, newness, and constituent dimension. Therefore sigma^2 permutes {r,s} and separately permutes {v,w}.

## The q=13 prime permutation

The polynomial for F factors modulo 13 with roots

2,6,9,10.

In the LMFDB ordering of the four primes above 13, the corresponding roots are

Q1: 10,
Q2: 9,
Q3: 6,
Q4: 2.

Exact evaluation of sigma^2 on these roots gives

10 <-> 9,
6 <-> 2.

Thus sigma^2 acts on the ordered q=13 prime block as

(Q1 Q2)(Q3 Q4).

The root identification was checked directly from the third generator in each LMFDB prime tuple, and the permutation was independently checked in exact arithmetic modulo 13.

## Dimension-2 constituents

The q=13 Hecke blocks from LMFDB are

r: [e, -e-2, -e-2, e],
s: [e, -e-2, e, -e-2].

Writing t=tau2(e)=-e-2, these are

r: [e,t,t,e],
s: [e,t,e,t].

Applying sigma^2, i.e. swapping positions 1<->2 and 3<->4, gives

r^(sigma^2): [t,e,e,t] = tau2([e,t,t,e]),
s^(sigma^2): [t,e,t,e] = tau2([e,t,e,t]).

The two coefficient-conjugacy orbits of these blocks are disjoint:

r orbit: [e,t,t,e], [t,e,e,t];
s orbit: [e,t,e,t], [t,e,t,e].

Since r and s are the only dimension-2 constituents at this level, sigma^2 fixes each constituent rather than swapping them. Inside K2 the only two automorphisms are id and tau2, and the q=13 block is changed, so the induced coefficient automorphism is tau2. Hence globally

r^(sigma^2)=r^tau2,
s^(sigma^2)=s^tau2.

## Dimension-6 constituents

Define

t = tau6(e)

and

A = -e^5/4 + e^4/2 + 31e^3/4 - 25e^2/2 - 45e/2 - 4.

The q=13 blocks from LMFDB are

v: [A,A,e,t],
w: [e,t,A,A].

Exact reduction modulo P6 verifies

tau6(A)=A,
tau6(t)=e.

Wolfram also factors P6(Y) over K6 as two linear factors and one irreducible quartic factor. Therefore K6 has exactly two Q-automorphisms, id and tau6.

Applying sigma^2 to the q=13 block gives

v^(sigma^2): [A,A,t,e] = tau6([A,A,e,t]),
w^(sigma^2): [t,e,A,A] = tau6([e,t,A,A]).

The id/tau6 coefficient-conjugacy orbit of v's block is

[A,A,e,t], [A,A,t,e],

while that of w is

[e,t,A,A], [t,e,A,A].

These orbits are disjoint. Since v and w are the only dimension-6 constituents at the level, sigma^2 fixes each constituent, and since the block is not fixed pointwise, the induced coefficient automorphism is tau6. Hence globally

v^(sigma^2)=v^tau6,
w^(sigma^2)=w^tau6.

## Why one q=13 block is enough here

This is not an inference that agreement at finitely many Hecke primes generally proves equality of newforms. The finite q=13 data are used only to identify the image of an already-known automorphism action inside an exhaustive finite list of same-dimension constituents.

Base conjugation must land in one of exactly two constituents of the relevant dimension. The complete q=13 coefficient-conjugacy blocks distinguish those two constituents. Once the constituent is fixed, the exact automorphism group of its coefficient field identifies whether the internal action is id or tau. Equality of newforms then follows from the automorphism action itself, not from a finite Sturm-like test.

## Computational certificates used

Wolfram exact checks for K6:

1. P6(tau6(X)) has zero remainder modulo P6(X).
2. tau6(tau6(X))-X has zero remainder modulo P6(X).
3. tau6(A)-A has zero remainder modulo P6(X).
4. P6(Y) over Q(e) factors into exactly two linear factors and one quartic factor, so Aut_Q(K6)={id,tau6}.

Wolfram exact check for the base field at p=13:

- roots of X^4-X^3-6X^2+X+1 mod 13 are {2,6,9,10};
- sigma^2 maps 2<->6 and 9<->10;
- matching the LMFDB prime-generator tuples gives the ordered permutation (1 2)(3 4).

## Consequence for reduction modulo the ramified lambda|5

For r,s, the unique prime above 5 in K2 is ramified and tau2 is the identity on its residue field F5.

For v,w, previous exact work established a unique ramified residue-degree-1 prime lambda above 5 in K6 and tau6 fixes lambda and induces the identity on O_K6/lambda = F5.

Therefore the certified characteristic-zero identities imply

bar(rho)^(sigma^2) ~= bar(rho)

for the residual representation attached to each of r,s,v,w at the relevant ramified lambda|5 (at least at the semisimple representation level determined by Hecke traces; under irreducibility this is an actual isomorphism by Brauer-Nesbitt/Chebotarev).

This closes open obligation #1 in the main checkpoint. The next obstruction is to exploit or strengthen this invariance enough to prove the residual representation reducible.