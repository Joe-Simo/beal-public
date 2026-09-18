\\ U194: fixed-base closure of (3,3,r) for ALL r at once:  A^3 + B^3 = n^r, r = 3j+e, e in {1,2}
\\ => (A/n^j)^3 + (B/n^j)^3 = n^e : rational point on x^3+y^3 = k, k=n^e  <->  Y^2 = X^3 - 432 k^2
\\ rank 0 => only torsion; list torsion points mapped back to (x,y) and test whether x = A/n^j with gcd(A,n)=1, j>=1, A,B>0.
N=150; cnt=[0,0]; badlist=[];
{
for(n=2,N, for(e=1,2,
  my(k=n^e, E=ellinit([0,0,0,0,-432*k^2]), r=ellrank(E)[2]);
  if(r==0,
    my(T=elltors(E), ok=1, pts=List());
    \\ enumerate torsion points
    my(gens=T[3], ords=T[2]);
    forvec(v=vector(#gens,i,[0,ords[i]-1]),
       my(P=[0]); for(i=1,#gens, P=elladd(E,P,ellmul(E,gens[i],v[i])));
       if(P!=[0] && P[1]!=0,
          my(x=(36*k+P[2])/(6*P[1]), y=(36*k-P[2])/(6*P[1]));
          if(x*y<0 && denominator(x)>1, ok=0; listput(pts,[x,y]))));
    if(ok, cnt[e]++; print("OK ",n," ",e), badlist=concat(badlist,[[n,e,Vec(pts)]]))
  )));
print("bases 2..",N,": DIFFERENCE arrangement C^3-A^3=n^r: rank-0 AND no mixed-sign non-integral torsion point:  e=1 (r=1 mod 3): ",cnt[1],"   e=2 (r=2 mod 3): ",cnt[2]);
print("rank-0 cases with a positive non-integral torsion point (need inspection): ",badlist);
}
quit;
