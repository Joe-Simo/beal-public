/* U276 — attack the C144 branch with PARI's Thue solver, which works on this form.
   The sextic F(u,v) (homogenised p) satisfies W(a,b) = F(a^2, b^2). The branch needs
   F(u,v) = w^3 with u = a^2, v = b^2 both squares and gcd(a,b)=1.
   thue() is COMPLETE for each fixed right-hand side, so this enumerates every solution
   for every cube up to the bound. */
default(parisize,"1G");
{
T = thueinit(x^6 + 114*x^5 - 705*x^4 + 1436*x^3 - 705*x^2 + 114*x + 1, 1);
print("w   F(u,v)=w^3 solutions              any with u,v BOTH nonzero squares, gcd=1 ?");
tot = 0; hits = 0;
for(w = 1, 60,
  k = w^3;
  S = thue(T, k);
  tot += #S;
  good = [];
  for(i = 1, #S,
    u = S[i][1]; v = S[i][2];
    if(u != 0 && v != 0,
      a = sqrtint(abs(u)); b = sqrtint(abs(v));
      if(u > 0 && v > 0 && a^2 == u && b^2 == v && gcd(a,b) == 1,
         good = concat(good, [[a,b,w]]))));
  if(#S > 0,
    print(w, "   ", S, "   ", if(#good, good, "none")));
  hits += #good;
);
print("");
print("cubes w^3 for w = 1..60 : ", tot, " Thue solutions in total, ", hits, " with u,v both nonzero coprime squares");
quit;
}
