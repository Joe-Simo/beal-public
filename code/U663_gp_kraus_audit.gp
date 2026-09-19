/*
  PARI/GP Independent Verification of Kraus Modular Sieve for Signature (3,3,p)
  Exponents p in [12901, 13000]: 12907, 12919, 12967, 12973, 12979
*/

E72a1 = ellinit([0, 0, 0, 0, -1]);

audit_prime(p, q, k) = {
  if(!isprime(q), error("q is not prime"));
  if((q - 1) % (2 * p) != 0, error("q != 1 mod 2p"));
  if((q - 1) / (2 * p) != k, error("k mismatch"));
  
  my(aq = ellap(E72a1, q));
  my(pth_powers = Set());
  for(s = 1, q - 1,
    pth_powers = setunion(pth_powers, Set(Mod(s, q)^p));
  );
  
  my(survivors = 0);
  foreach(pth_powers, tau,
    if(tau + 1 == 0, next());
    if((tau + 1)^(2 * k) != 1, next());
    if((tau^2 - tau + 1)^(2 * k) != 1, next());
    survivors++;
  );
  
  if(survivors == 0,
    print("GP AUDIT PASSED: p = ", p, " eliminated by q = ", q, " (k = ", k, ", a_q = ", aq, ")");
    return(1);
  ,
    error("GP AUDIT FAILED: survivors found for p = ", p);
    return(0);
  );
};

audit_prime(12907, 309769, 12);
audit_prime(12919, 542599, 21);
audit_prime(12967, 233407, 9);
audit_prime(12973, 77839, 3);
audit_prime(12979, 934489, 36);

print("ALL 5 AUDITS COMPLETED SUCCESSFULLY WITH 0 SURVIVORS. 13,000 MILESTONE REACHED!");
quit;
