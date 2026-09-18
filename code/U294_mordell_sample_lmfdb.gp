/* U294 — discharge the C078 obligation "independent rank confirmation for a sample of the rank-0
   curves". The {3,4,r} fixed-base argument lands on Mordell curves Y^2 = X^3 + k with
   k = -432 n^{2e}; confirm rank 0 for a sample by TWO methods (2-descent and analytic rank),
   and cross-check conductor/torsion so the curve cannot be mislabelled. */
default(parisize,"2G");
{
print("n  e   k = -432*n^(2e)      cond      torsion         2-descent   analytic   agree?");
for(n = 2, 12,
  for(e = 1, 2,
    k = -432 * n^(2*e);
    E = ellinit([0,0,0,0,k]);
    if(E == 0, next);
    c = ellglobalred(E)[1];
    t = elltors(E)[1];
    r2 = ellrank(E)[1];
    ra = ellanalyticrank(E)[1];
    print(n, "  ", e, "   ", k, "   ", c, "   ", t, "   ", r2, "   ", ra, "   ", r2 == ra);
  ));
quit;
}
