# U22: exact 17-adic split of the fixed gamma and delta equations

Status: verified partial result only. This does not resolve Beal's conjecture.

Continue from U20/U21. In the only surviving Case III branch,

a=A^5,
b=16*17^4*B^5,
gcd(a,b)=1,

and with w=(1+sqrt(17))/2 we have

gamma=u+v w,
delta=r+s w,

for coprime integer coordinate pairs (u,v) and (r,s).

The first fixed equation is

(P_g/sqrt(17))/eta = gamma^5,

and U20 gives the exact w-coordinate identity

v Q(u,v) = 8 b^2 (a-b)(a+b)(3a^2-b^2)(a^2+b^2),

where

Q(x,y)=5x^4+10x^3y+50x^2y^2+45xy^3+29y^4.

## Exact structure of Q at 17

Exact Wolfram factorization modulo 17 gives

Q(u,v) == 5 (u+9v)^4 (mod 17).

More precisely, after setting t=u+9v,

Q = 5 t^4 -170 t^3 v +2210 t^2 v^2 -13005 t v^3 +29189 v^4

  = 5 t^4 -10*17 t^3 v +130*17 t^2 v^2 -45*17^2 t v^3 +101*17^2 v^4.

Hence, under gcd(u,v)=1:

- if 17|v, then 17 does not divide u and therefore v_17(Q)=0;
- if 17 does not divide v and 17 does not divide (u+9v), then v_17(Q)=0;
- if 17 does not divide v and 17|(u+9v), then v_17(Q)=2 exactly, because the constant term is 101*17^2*v^4 and every other term is divisible by at least 17^3.

Thus v_17(Q) is always 0 or 2 for primitive (u,v).

## Consequence for the gamma coordinate v

Write k=v_17(B). Then

v_17(b)=4+5k.

Because 17 does not divide a, each of

a-b, a+b, 3a^2-b^2, a^2+b^2

is a 17-adic unit. Therefore the right side of the U20 identity has exact valuation

2 v_17(b)=8+10k.

If 17 did not divide v, then the left side would have valuation 0 or 2, impossible. Therefore 17|v. In that case v_17(Q)=0, and so

v_17(v)=8+10k=2 v_17(b).

Equivalently,

17^(8+10 v_17(B)) | v,

with exact exponent 8+10 v_17(B).

This is an exact strengthening of the finite forcing-prime divisibility from U20.

## The second fixed delta equation

The second fixed equation is

(P_h/sqrt(17))/eta^4 = delta^5.

Exact rationalization and coefficient extraction gives its sqrt(17)-coefficient

B_h = (-72913 a^8 +255748 a^6 b^2 -186150 a^4 b^4 +40324 a^2 b^6 -2177 b^8)/17.

Therefore its w-coordinate satisfies

s Q(r,s) = 2 B_h

= -2(72913 a^8 -255748 a^6 b^2 +186150 a^4 b^4 -40324 a^2 b^6 +2177 b^8)/17.

Since 72913=17*4289 and 17^4|b, reducing this identity modulo 17 gives

s Q(r,s) == -2*4289*a^8 == -10 a^8 (mod 17),

which is nonzero because 17 does not divide a. Hence

17 does not divide s,

and also 17 does not divide Q(r,s). Using Q(r,s)==5(r+9s)^4 mod 17 further gives

17 does not divide (r+9s).

Thus the two fifth-power coordinates have sharply opposite 17-adic behavior:

- gamma=u+v w has v_17(v)=8+10 v_17(B);
- delta=r+s w has v_17(s)=0 and 17 does not divide r+9s.

This is a new exact compatibility constraint tying both fixed equations together.

## Additional local note at forcing primes

For any known forcing prime q|B with q not dividing 2*17*4289, the same delta identity reduces modulo q to a nonzero multiple of a^8, so q does not divide s Q(r,s). In particular q does not divide s. Thus the primes forced to high powers into the gamma coordinate v are simultaneously excluded from the delta coordinate s.

This does not yet contradict the surviving branch. The next obligation is to exploit the simultaneous conditions on gamma and delta, most naturally through a relation between their fixed fifth-power equations or a Thue/Thue-Mahler elimination that uses the exact 17-adic asymmetry.