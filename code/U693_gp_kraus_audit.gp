/*
  PARI/GP Independent Verification of Kraus Modular Sieve for Signature (3,3,p)
  Exponents p in [14401, 14500]: 14401, 14407, 14419, 14431, 14437, 14449, 14461, 14479 - 14500 Centennial Milestone
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

audit_prime(14401, 259219, 9);
audit_prime(14407, 345769, 12);
audit_prime(14419, 605599, 21);
audit_prime(14431, 86587, 3);
audit_prime(14437, 259867, 9);
audit_prime(14449, 433471, 15);
audit_prime(14461, 86767, 3);
audit_prime(14479, 781867, 27);

print("ALL 8 AUDITS COMPLETED SUCCESSFULLY WITH 0 SURVIVORS.");
quit;
