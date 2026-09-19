/*
  PARI/GP Independent Verification of Kraus Modular Sieve for Signature (3,3,p)
  Exponents p in [12701, 12800]: 12703, 12721, 12739, 12757, 12763, 12781, 12799
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

audit_prime(12703, 685963, 27);
audit_prime(12721, 381631, 15);
audit_prime(12739, 382171, 15);
audit_prime(12757, 76543, 3);
audit_prime(12763, 76579, 3);
audit_prime(12781, 230059, 9);
audit_prime(12799, 153589, 6);

print("ALL 7 AUDITS COMPLETED SUCCESSFULLY WITH 0 SURVIVORS.");
quit;
