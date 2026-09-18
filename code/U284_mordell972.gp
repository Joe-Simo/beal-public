/* U284 — the quotient curve is the Mordell curve y^2 = x^3 - 972 (conductor 972, rank 1,
   generator [13,35]). Find ALL its integral points, then pull back. */
default(parisize,"2G");
{
E = ellinit([0,0,0,0,-972]);
print("E : y^2 = x^3 - 972");
print("  conductor  = ", ellglobalred(E)[1]);
print("  rank       = ", ellrank(E));
print("  torsion    = ", elltors(E));
print("  generators = ", ellrank(E)[4]);
print("");
print("integral points via ellratpoints at increasing height:");
for(h = 3, 7, print("  height 10^", h, " : ", ellratpoints(E, 10^h)));
print("");
print("multiples of the generator P = [13,35] and whether they are integral:");
P = [13,35];
for(n = 1, 14,
   Q = ellmul(E, P, n);
   if(Q == [0], print("  ", n, "P = O"),
      print("  ", n, "P = ", Q, "   integral: ", denominator(Q[1]) == 1 && denominator(Q[2]) == 1)));
quit;
}
