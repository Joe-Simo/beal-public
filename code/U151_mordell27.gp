E = ellinit([0,0,0,0,27]);
print("conductor: ", ellglobalred(E)[1]);
print("torsion: ", elltors(E));
print("analytic rank: ", ellanalyticrank(E)[1]);
print("2-descent bound (ell2cover/ellrank): ", ellrank(E)[2]);
quit;
