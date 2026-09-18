\\ INDEPENDENT CROSS-CHECK of the rank-0 determinations, by a different mechanism:
\\ on a rank-0 curve every rational point is torsion, so a direct search for INTEGRAL points
\\ must find nothing outside the torsion set. Positive rank would usually show up as an extra point.
NMAX = 60; XB = 20000;
extra = 0; curves = 0; tors_seen = 0;
{
for(n = 2, NMAX,
  for(e = 1, 2,
    my(k = n^e, E = ellinit([0,0,0,0,-432*k^2]));
    if(ellrank(E)[2] == 0,
      curves++;
      my(T = elltors(E), tp = List());
      my(gens = T[3], ords = T[2]);
      forvec(v = vector(#gens, i, [0, ords[i]-1]),
        my(P = [0]);
        for(i = 1, #gens, P = elladd(E, P, ellmul(E, gens[i], v[i])));
        if(P != [0], listput(tp, P[1])));
      tors_seen += #tp;
      for(X = -200, XB,
        my(R = X^3 - 432*k^2);
        if(R >= 0 && issquare(R),
          if(!setsearch(Set(Vec(tp)), X), extra++;
             print("EXTRA integral point n=", n, " e=", e, " X=", X))))
    )));
print("rank-0 curves cross-checked: ", curves);
print("torsion x-coordinates seen:  ", tors_seen);
print("integral points OUTSIDE torsion, |X| <= ", XB, ": ", extra);
}
quit

\\ CALIBRATION (U353): the positive control for this searcher, run separately, found an integral
\\ point on only 42 of the 53 positive-rank curves in the same family (|X| <= 20000). So the
\\ searcher's sensitivity to positive rank is about 42/53 -- it MISSES roughly one in five.
\\ WITHDRAWN AS EVIDENCE (U354). The misses were diagnosed, not just counted: in every one
\\ examined the curve has rank exactly 1 and its GENERATOR IS NON-INTEGRAL -- e.g. n=50, e=1 has
\\ x = 2716/9, and n=58, e=2 has x = 14580300595449/1479556225. Widening the search range would
\\ never find them, because there is nothing integral to find. So an integral-point search is
\\ STRUCTURALLY unable to detect positive rank in this family, and "no extra integral point"
\\ carries NO information about rank. This script is kept as a record of a check that does not
\\ work, not as evidence. C079's rank-0 determinations rest on PARI's ellrank upper bound alone.
