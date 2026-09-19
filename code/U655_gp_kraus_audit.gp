/*
  PARI/GP Independent Verification of Kraus Modular Sieve for Signature (3,3,p)
  Exponents p in [12501, 12600]: 12511, 12517, 12541, 12547, 12553, 12577, 12583, 12589
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

audit_prime(12511, 600529, 24);
audit_prime(12517, 225307, 9);
audit_prime(12541, 376231, 15);
audit_prime(12547, 602257, 24);
audit_prime(12553, 451909, 18);
audit_prime(12577, 452773, 18);
audit_prime(12583, 301993, 12);
audit_prime(12589, 679807, 27);

print("ALL 8 AUDITS COMPLETED SUCCESSFULLY WITH 0 SURVIVORS.");
quit;
