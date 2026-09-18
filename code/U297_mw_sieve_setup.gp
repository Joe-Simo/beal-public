/* U297 — make the map EXPLICIT so a Mordell-Weil sieve becomes possible.
   The quartic y^2 = D(s) = -3s^4+432s^3+6912s^2+36864s has a rational ROOT at s=0, so s = 1/t,
   y = w/t^2 turns it into the CUBIC  w^2 = 36864 t^3 + 6912 t^2 + 432 t - 3.
   Get that curve, its rank and a generator, so points can be enumerated as n*P with t explicit. */
default(parisize,"2G");
{
print("cubic model: w^2 = 36864 t^3 + 6912 t^2 + 432 t - 3");
E = ellfromeqn(w^2 - (36864*t^3 + 6912*t^2 + 432*t - 3));
print("  ellfromeqn: ", E);
F = ellinit(E);
G = ellminimalmodel(F);
print("  minimal model : ", G[1..5]);
print("  conductor     : ", ellglobalred(G)[1]);
print("  rank          : ", ellrank(G));
print("  torsion       : ", elltors(G));
print("");
print("  small rational points on the minimal model: ", ellratpoints(G, 10000));
print("");
print("  direct search for rational t with 36864t^3+6912t^2+432t-3 a square:");
for(num = -200, 200,
  for(den = 1, 60,
    if(gcd(num,den) == 1,
      t = num/den;
      v = 36864*t^3 + 6912*t^2 + 432*t - 3;
      if(v >= 0 && issquare(v), print("    t = ", t, "   w^2 = ", v, "   w = ", sqrt(v))))));
quit;
}
