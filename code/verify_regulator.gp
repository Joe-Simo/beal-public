default(parisize, "512M");
default(realprecision, 38);
{
f = x^34 + 2*x^17 - 4;
bnf = bnfinit(f, 1);
r = polroots(f);
print("Polroots count: ", #r);

r_real = [];
r_cplx = [];
for(i=1, #r,
  if(abs(imag(r[i])) < 1e-25,
    r_real = concat(r_real, [r[i]]),
    if(imag(r[i]) > 1e-25,
      r_cplx = concat(r_cplx, [r[i]])
    )
  )
);
print("Real roots count: ", #r_real);
print("Complex roots count: ", #r_cplx);

M = matrix(17, 17);
for(j=1, 17,
  u_pol = lift(bnf.fu[j]);
  val = subst(u_pol, x, r_real[1]);
  M[1, j] = log(abs(val));
  for(i=1, 16,
    val = subst(u_pol, x, r_cplx[i]);
    M[i+1, j] = 2 * log(abs(val));
  );
);
det_M = abs(matdet(M));
print("Dirichlet regulator computed directly from roots: ", det_M);
print("bnf.reg:                                          ", bnf.reg);
print("Ratio: ", det_M / bnf.reg);
print("Difference: ", abs(det_M - bnf.reg));
}
quit;
