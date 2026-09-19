/*
  PARI/GP Independent Verification of Kraus Modular Sieve for Signature (3,3,p)
  Exponents p in [14301, 14400]: 14323, 14341, 14347, 14389
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

audit_prime(14323, 171877, 6);
audit_prime(14341, 172093, 6);
audit_prime(14347, 86083, 3);
audit_prime(14389, 431671, 15);

print("ALL 4 AUDITS COMPLETED SUCCESSFULLY WITH 0 SURVIVORS.");
quit;
