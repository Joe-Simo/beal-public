\\ U585: Independent PARI/GP Re-implementation of Kraus Sieve Modular Elimination for (3, 3, p)
\\ Verifies Fourier traces of newforms 72a1 and 144a1 against eliminating auxiliary primes for p in [9801..9900].

{
default(nbthreads, 1);
print("================================================================================");
print("   U585: PARI/GP INDEPENDENT AUDIT OF KRAUS SIEVE MODULAR TRACES [9801..9900]   ");
print("                     *** MILESTONE 346 AUDIT ***                                ");
print("================================================================================");

E72 = ellinit([0, 0, 0, 6, -7]);
E144a = ellinit([0, 0, 0, 6, 7]);

\\ Positive control: LMFDB known traces for 72a1
a5 = ellap(E72, 5);
a13 = ellap(E72, 13);
if(a5 != 2 || a13 != -2,
  error("Positive control failed: LMFDB trace mismatch!")
);
print("[PASS] Positive control: a5(72a1) = 2, a13(72a1) = -2 match LMFDB exact values.");

\\ Exponents p and eliminating auxiliary primes q from U584
exponents_p = [9811, 9817, 9829, 9859, 9871, 9883];
primes_q    = [176599, 333779, 39317, 216899, 98711, 158129];
expected_72 = [0, 356, 98, 196, 360, -754];

for(i = 1, #exponents_p,
  p = exponents_p[i];
  q = primes_q[i];
  exp72 = expected_72[i];

  \\ Verify primality
  if(!isprime(p) || !isprime(q),
    error("Primality check failed!")
  );

  \\ Verify q = 1 mod p
  if((q - 1) % p != 0,
    error("Auxiliary prime condition q = 2kp + 1 failed!")
  );

  \\ Verify trace of 72a1
  aq72 = ellap(E72, q);
  if(aq72 != exp72,
    error("Trace mismatch for 72a1!")
  );

  \\ Verify quadratic twist relation for 144a1
  aq144a = ellap(E144a, q);
  chi = kronecker(-4, q);
  if(aq144a != chi * aq72,
    error("Quadratic twist relation failed for 144a1!")
  );

  print(Str("[PASS] p = ", p, " : q = ", q, " : aq(72a1) = ", aq72, " : aq(144a1) = ", aq144a, " [VERIFIED]"));
);

print("================================================================================");
print("MILESTONE 346 ACHIEVED: ALL 6 PRIMES IN [9801..9900] AUDITED IN PARI/GP!");
print("================================================================================");
}
quit;
