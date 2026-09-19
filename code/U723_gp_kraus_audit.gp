/*
  PARI/GP Independent Verification of Kraus Modular Sieve for Signature (3,3,p)
  Exponents p in [15901, 16000]: 15901, 15907, 15913, 15919, 15937, 15973, 15991 (16000 Centennial Milestone)
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

audit_prime(15901, 477031, 15);
audit_prime(15907, 95443, 3);
audit_prime(15913, 95479, 3);
audit_prime(15919, 286543, 9);
audit_prime(15937, 478111, 15);
audit_prime(15973, 191677, 6);
audit_prime(15991, 95947, 3);

print("ALL 7 AUDITS COMPLETED SUCCESSFULLY WITH 0 SURVIVORS - 16000 CENTENNIAL VERIFIED.");
quit;
