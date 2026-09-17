allocatemem(512*10^6);
{
print("==========================================================================================================");
print("Arithmetic Classification of Generalized Fermat Exponents p in [19, 100] for Signature (2l, 2m, p)");
print("Evaluating Sahoo (2025) Class P_1 Criteria: 2 inert in Q(zeta_p)^+, p != 1 mod 8, 2 does not divide h_p^+");
print("==========================================================================================================");
print(printf("%-4s | %-5s | %-4s | %-7s | %-8s | %-6s | %-4s | %-8s | %-12s | %-15s", 
             "p", "mod 8", "d", "ord_p(2)", "primes_2", "f(2)", "h", "h^+", "Inert in K?", "Classification"));
print("----------------------------------------------------------------------------------------------------------");

plist = [19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
p1_list = [];
non_p1_list = [];

for(i=1, #plist,
  p = plist[i];
  pmod8 = p % 8;
  d = (p-1)/2;
  ord2 = znorder(Mod(2, p));
  
  P = polsubcyclo(p, d);
  nf = nfinit(P);
  dec = idealprimedec(nf, 2);
  num2 = #dec;
  f2 = dec[1].f;
  isinert = (num2 == 1 && f2 == d);
  
  /* Class number computation */
  bnf = bnfinit(P, 1);
  h = bnf.no;
  hplus = bnfnarrow(bnf)[1];
  
  class_str = "";
  if (isinert && (pmod8 != 1) && (hplus % 2 != 0),
    class_str = "Class P_1 (ELIM)";
    p1_list = concat(p1_list, [p]);
  ,
    if (pmod8 == 1,
      class_str = "Class P_2 (p=1 mod 8)";
    ,
      if (!isinert,
        class_str = "Class P_3 (Split-2)";
      ,
        if (hplus % 2 == 0,
          class_str = "Even h^+ (2 | h^+)";
        );
      );
    );
    non_p1_list = concat(non_p1_list, [p]);
  );
  
  print(printf("%-4d | %-5d | %-4d | %-7d | %-8d | %-6d | %-4d | %-8d | %-12s | %-15s",
               p, pmod8, d, ord2, num2, f2, h, hplus, if(isinert, "YES", "NO"), class_str));
);

print("==========================================================================================================");
print("Summary of Classification for p in [19, 100]:");
print("Total primes checked: ", #plist);
print("Class P_1 (Asymptotically Eliminated by Sahoo 2025): ", p1_list);
print("Count in Class P_1: ", #p1_list, " / ", #plist, " (", floor(100*#p1_list/#plist), "%)");
print("Non-Class P_1 primes: ", non_p1_list);
print("==========================================================================================================");
}
\q
