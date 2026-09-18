/* U298b — REDONE WITH EXACT RATIONAL ARITHMETIC. The first version used sqrt() which returned
   floating point, violating the exactness discipline; issquare(x,&r) sets r exactly for rationals. */
default(parisize,"2G");
{
M = ellinit([0, 6912, 0, 15925248, -4076863488]);
P = [1024, 143360];
print("P on M: ", ellisoncurve(M,P), "   rank ", ellrank(M)[1], "   torsion ", elltors(M)[1]);
print("");
print(" n   disc a square?   Y roots (exact)                      admissible (Y a positive rational square)?");
hits = 0;
for(n = 1, 40,
  Q = ellmul(M, P, n);
  if(Q == [0], next);
  t = Q[1]/36864;
  if(t == 0, next);
  s = 1/t;
  a = 3*s - 108; b = 3*s^2 + 1152; c = s^3 - 3072;
  if(a == 0,
     Y = -c/b;
     ok = (Y > 0) && issquare(Y);
     if(n <= 8, print(n, "   (degenerate a=0)   Y = ", Y, "   ", ok));
     if(ok, hits++)
  ,
     D = b^2 - 4*a*c;
     r = 0;
     if(issquare(D, &r),
        Y1 = (-b + r)/(2*a); Y2 = (-b - r)/(2*a);
        ok1 = (Y1 > 0) && issquare(Y1); ok2 = (Y2 > 0) && issquare(Y2);
        if(n <= 8, print(n, "   yes   Y1 = ", Y1, "  Y2 = ", Y2, "   ", ok1 || ok2));
        if(ok1 || ok2, hits++; print("  *** ADMISSIBLE HIT at n = ", n))
     ,
        if(n <= 8, print(n, "   no  -> no rational Y for this point")))));
print("");
print("n = 1..40 : admissible hits = ", hits);
quit;
}
