default(parisize, "1024M");
default(realprecision, 19);

poly_plus(p) = {
  my(x='x, y='y, P=polcyclo(p, x));
  my(R = polresultant(P, x^2 - y*x + 1, x));
  my(F = factor(R));
  return(subst(F[1, 1], y, x));
};

{
print("======================================================================================================");
print("  SAHOO (2025) CLASS P_1 AUDIT: REAL CYCLOTOMIC FIELDS Q(zeta_p)^+ (19 <= p < 100)");
print("======================================================================================================");

t_global_start = gettime();

P_list = [19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

printf("%-4s | %-6s | %-10s | %-10s | %-6s | %-6s | %-6s | %-6s | %-6s | %-10s\n", 
      "p", "[K+:Q]", "ord_p(2)", "-1 in <2>?", "f+", "g+", "Inert?", "h_p+", "2|h+?", "Class P_1?");
print("------------------------------------------------------------------------------------------------------");

p1_primes = [];
non_p1_primes = [];

for(i=1, #P_list,
  p = P_list[i];
  deg_plus = (p - 1) / 2;
  ord = znorder(Mod(2, p));
  has_neg1 = (ord % 2 == 0 && Mod(2, p)^(ord/2) == Mod(-1, p));
  f_plus = if(has_neg1, ord / 2, ord);
  g_plus = deg_plus / f_plus;
  inert = (g_plus == 1);

  \\ Compute class number h_p^+
  t0 = gettime();
  pol = poly_plus(p);
  bnf = bnfinit(pol, 1);
  t_comp = gettime() - t0;
  h_plus = bnf.no;
  two_divides = (h_plus % 2 == 0);
  in_p1 = (inert && !two_divides);

  if(in_p1,
    p1_primes = concat(p1_primes, [p]),
    non_p1_primes = concat(non_p1_primes, [p])
  );

  has_neg1_str = if(has_neg1, "YES", "NO");
  inert_str = if(inert, "YES", "NO");
  two_div_str = if(two_divides, "YES", "NO");
  in_p1_str = if(in_p1, "IN P_1", "NOT P_1");

  printf("%-4d | %-6d | %-10d | %-10s | %-6d | %-6d | %-6s | %-6d | %-6s | %-10s\n", 
        p, deg_plus, ord, has_neg1_str, f_plus, g_plus, inert_str, h_plus, two_div_str, in_p1_str);
);

print("------------------------------------------------------------------------------------------------------");
print("\n[+] Total Primes Analyzed: ", #P_list);
print("[+] Class P_1 Primes (", #p1_primes, "): ", p1_primes);
print("[+] Non-P_1 Primes   (", #non_p1_primes, "): ", non_p1_primes);
print("[+] Total Execution Time: ", gettime() - t_global_start, " ms");
print("======================================================================================================");
}
quit;
