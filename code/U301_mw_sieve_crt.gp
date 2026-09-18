/* U301 — intersect the Mordell-Weil sieve conditions of U300 by CRT.
   n = 0 is the identity (the point at infinity), which is NOT an admissible affine point, so if
   the only surviving class is n = 0 the branch is closed by the sieve. */
default(parisize,"4G");
{
M = ellinit([0, 6912, 0, 15925248, -4076863488]);
P = [1024, 143360];
LCM = 1; SURV = [0];   /* surviving residues modulo LCM */
forprime(p = 5, 300,
  if(Mod(36864,p) == 0, next);
  Ep = ellinit(M, p);
  if(Ep == 0 || ellisoncurve(Ep,P) == 0, next);
  m = ellorder(Ep, P);
  if(m == 0 || m > 200, next);
  surv = [];
  for(n = 0, m-1,
    Q = ellmul(Ep, P, n);
    if(Q == [0], surv = concat(surv,[n]); next);
    t = Mod(lift(Q[1]),p)/Mod(36864,p);
    if(t == 0, surv = concat(surv,[n]); next);
    s = 1/t; a = 3*s-108; b = 3*s^2+1152; c = s^3-3072; ok = 0;
    if(a == 0, if(b != 0 && issquare(-c/b), ok = 1),
       D = b^2-4*a*c; r = 0;
       if(issquare(D,&r), if(issquare((-b+r)/(2*a)) || issquare((-b-r)/(2*a)), ok = 1)));
    if(ok, surv = concat(surv,[n])));
  if(#surv == m, next);
  /* CRT-merge {SURV mod LCM} with {surv mod m} */
  L = lcm(LCM, m); new = [];
  for(i = 1, #SURV, for(j = 1, #surv,
    x = SURV[i]; y = surv[j];
    if((x - y) % gcd(LCM,m) == 0,
       z = lift(chinese(Mod(x,LCM), Mod(y,m)));
       new = concat(new, [z]))));
  SURV = Set(new); LCM = L;
  print("after p = ", p, " : modulus ", LCM, ", surviving classes ", #SURV,
        if(#SURV <= 6, concat([" = "], SURV), ""));
  );
print("");
print("final: modulus ", LCM, ", ", #SURV, " surviving classes");
if(#SURV <= 20, print("  classes: ", SURV));
quit;
}
