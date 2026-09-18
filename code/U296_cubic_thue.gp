/* U296 — the (3,4,4) survivor, attacked with a COMPLETE method on the right form.
   The branch curve is W^3 = Q(Y) with Q(Y) = Y^3+108Y^2-1152Y+3072 and Y = y^2 required a square.
   Writing Y = m/n in lowest terms, W^3 = Q(m/n) means the CUBIC BINARY FORM
       R(m,n) = m^3 + 108 m^2 n - 1152 m n^2 + 3072 n^3
   is a perfect cube. thue() is COMPLETE for each fixed right-hand side, so this enumerates every
   solution for every cube up to the bound. The branch additionally needs m/n to be a square. */
default(parisize,"2G");
{
R = x^3 + 108*x^2 - 1152*x + 3072;
print("form R(m,n) = m^3 + 108 m^2 n - 1152 m n^2 + 3072 n^3");
print("  irreducible over Q ? ", polisirreducible(R));
print("  discriminant       = ", factor(poldisc(R)));
T = thueinit(R, 1);
print("");
print("w    R(m,n) = w^3 solutions                         any with m/n a positive square, gcd=1 ?");
tot = 0; good = 0;
for(w = 1, 80,
  S = thue(T, w^3);
  tot += #S;
  hit = [];
  for(i = 1, #S,
    m = S[i][1]; n = S[i][2];
    if(n != 0 && m > 0 && n > 0 && gcd(m,n) == 1,
      if(issquare(m) && issquare(n), hit = concat(hit, [[m,n,w]]))));
  if(#S > 0, print(w, "    ", S, "     ", if(#hit, hit, "none")));
  good += #hit;
);
print("");
print("cubes w = 1..80 : ", tot, " Thue solutions total, ", good, " with m and n both positive coprime squares");
quit;
}
