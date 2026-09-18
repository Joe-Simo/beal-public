/* U299 — the elliptic-Chabauty rank condition, tested concretely.
   Bruin's elliptic Chabauty over K needs rank_E(K) < [K:Q]. For K = Q(sqrt d) quadratic,
   rank_E(K) = rank_E(Q) + rank_{E^d}(Q). Here rank_E(Q) = 1, so the condition rank_E(K) < 2
   holds exactly when the quadratic TWIST E^d has rank 0. Find such d. */
default(parisize,"2G");
{
print("E : y^2 = x^3 - 972,  rank_E(Q) = 1");
print("");
print("  d     twist E^d : y^2 = x^3 - 972 d^3     rank   rank_E(Q(sqrt d)) = 1 + rank   Chabauty usable (<2)?");
good = [];
for(d = -30, 30,
  if(d == 0 || d == 1, next);
  if(!issquarefree(abs(d)), next);
  E = ellinit([0,0,0,0,-972*d^3]);
  if(E == 0, next);
  r = ellrank(E);
  rl = r[1]; ru = r[2];
  tot = 1 + rl;
  usable = (ru == 0);
  if(rl == ru,
     print("  ", d, "     rank ", rl, "   rank over Q(sqrt d) = ", tot, "   ", if(usable, "YES", "no"));
     if(usable, good = concat(good, [d]))));
print("");
print("squarefree d with twist rank provably 0, so rank_E(Q(sqrt d)) = 1 < 2: ", good);
quit;
}
