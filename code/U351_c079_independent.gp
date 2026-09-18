\\ INDEPENDENT re-implementation of U194's criterion, written from the stated mathematics
\\ rather than copied: rank 0 (UPPER bound, so sound), then map each torsion point back and
\\ reject only if it gives a POSITIVE pair with a non-integral coordinate.
NMAX=150;
ok1=0; ok2=0; flagged=List();
{
for(n=2, NMAX,
  for(e=1, 2,
    my(k=n^e, E=ellinit([0,0,0,0,-432*k^2]), rhi=ellrank(E)[2]);
    if(rhi==0,
      my(T=elltors(E), gens=T[3], ords=T[2], clean=1);
      forvec(v=vector(#gens,i,[0,ords[i]-1]),
        my(P=[0]);
        for(i=1,#gens, P=elladd(E,P,ellmul(E,gens[i],v[i])));
        if(P!=[0] && P[1]!=0,
          my(x=(36*k+P[2])/(6*P[1]), y=(36*k-P[2])/(6*P[1]));
          if(x>0 && y>0 && denominator(x)>1, clean=0; listput(flagged,[n,e,x,y]))));
      if(clean, if(e==1, ok1++, ok2++)))));
print("independent re-run, bases 2..", NMAX, ":");
print("  rank-0 and clean, e=1: ", ok1, "    e=2: ", ok2);
print("  flagged (positive non-integral torsion point): ", Vec(flagged));
}
print("curves examined: ", 2*(NMAX-1));
quit
