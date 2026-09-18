/* U300 — MORDELL-WEIL SIEVE on the (3,4,4) survivor. No p-adic integration needed.
   E has rank 1 and trivial torsion with generator P, so every rational point is nP.
   For each good prime p: compute the order m of P in E(F_p); for each residue class n mod m,
   reduce nP, follow the map to Y, and test whether Y is a square mod p. A class with NO square
   Y is EXCLUDED. Intersecting the surviving classes over many primes constrains n. */
default(parisize,"3G");
{
M = ellinit([0, 6912, 0, 15925248, -4076863488]);
P = [1024, 143360];
print("M : Y^2 = X^3 + 6912X^2 + 15925248X - 4076863488,  P = ", P, ",  rank 1, torsion trivial");
print("");
print("  p    ord(P)   surviving n-classes mod ord(P)              fraction");
allinfo = [];
forprime(p = 5, 400,
  if(Mod(36864, p) == 0, next);
  Ep = ellinit(M, p);
  if(Ep == 0, next);
  if(ellisoncurve(Ep, P) == 0, next);
  m = ellorder(Ep, P);
  if(m == 0 || m > 4000, next);
  surv = [];
  for(n = 0, m-1,
    Q = ellmul(Ep, P, n);
    if(Q == [0], surv = concat(surv, [n]); next);
    X = lift(Q[1]);
    t = Mod(X,p) / Mod(36864,p);
    if(t == 0, surv = concat(surv, [n]); next);
    s = 1/t;
    a = 3*s - 108; b = 3*s^2 + 1152; c = s^3 - 3072;
    ok = 0;
    if(a == 0,
       if(b != 0, Y = -c/b; if(issquare(Y), ok = 1)),
       D = b^2 - 4*a*c;
       if(issquare(D, &r),
          Y1 = (-b + r)/(2*a); Y2 = (-b - r)/(2*a);
          if(issquare(Y1) || issquare(Y2), ok = 1)));
    if(ok, surv = concat(surv, [n])));
  if(#surv < m,
     allinfo = concat(allinfo, [[p, m, surv]]);
     print("  ", p, "    ", m, "     ", if(#surv <= 12, surv, concat(surv[1..10], ["..."])), "     ", #surv, "/", m)));
print("");
print("primes giving a nontrivial condition: ", #allinfo);
quit;
}
