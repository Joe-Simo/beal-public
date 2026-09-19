/*
  PARI/GP Independent Verification of Kraus Modular Sieve for Signature (3,3,p)
  Exponents p in [15601, 15700]: 15601, 15607, 15619, 15643, 15649, 15661, 15667, 15679
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

audit_prime(15601, 93607, 3);
audit_prime(15607, 280927, 9);
audit_prime(15619, 2155423, 69);
audit_prime(15643, 563149, 18);
audit_prime(15649, 281683, 9);
audit_prime(15661, 93967, 3);
audit_prime(15667, 376009, 12);
audit_prime(15679, 376297, 12);

print("ALL 8 AUDITS COMPLETED SUCCESSFULLY WITH 0 SURVIVORS.");
quit;
