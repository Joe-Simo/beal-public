default(parisize, "512M");
{
f = x^34 + 2*x^17 - 4;
bnf = bnfinit(f, 1);
rel_pol = x^17 - (2*y - 2);
k_pol = y^2 - y - 1;

for(i=1, 17,
  u = lift(bnf.fu[i]);
  res = polresultant(rel_pol, u, x);
  res_mod = Mod(res, k_pol);
  found = 0;
  for(m=-40, 40,
    for(s_idx=1, 2,
      sgn = if(s_idx==1, 1, -1);
      phi_m = sgn * (Mod(y, k_pol)^m);
      if(phi_m == res_mod,
        print("u", i, " rel norm = ", if(sgn==1, "+", "-"), " phi^(", m, ")");
        found = 1;
        break(2);
      );
    );
  );
  if(!found, print("u", i, " not recognized: ", res_mod));
);
}
quit;
