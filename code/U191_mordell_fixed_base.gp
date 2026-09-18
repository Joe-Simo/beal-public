\\ U191: fixed-base closure of the {3,4,r} signatures for ALL primes r>=7 at once.
\\ A^3 + B^4 = n^r  =>  (B^2)^2 = (-A)^3 + n^r  => rational point on y^2 = x^3 + n^(r mod 6)   [scale by n^(6j)]
\\ A^4 + n^r = C^3  =>  (A^2)^2 = C^3 - n^r     => point on y^2 = x^3 - n^(r mod 6)
\\ A^3 + n^r = C^4  =>  (C^2)^2 = A^3 + n^r     => point on y^2 = x^3 + n^(r mod 6)
\\ r prime >= 7  => r mod 6 in {1,5}.  rank 0 (PARI 2-descent upper bound 0) => only torsion, which is integral => no solution.
N = 120;
{
for(n=2,N,
  my(v=[]);
  foreach([[1,1],[1,5],[-1,1],[-1,5]], t,
     my(E=ellinit([0,0,0,0,t[1]*n^t[2]]), r=ellrank(E));
     v=concat(v, r[2]));           \\ unconditional upper bound on the rank
  print(n," ",v));
}
quit;
