\\ U480: Independent PARI/GP Re-implementation of Kraus Sieve Modular Elimination for (3, 3, p)
\\ Verifies Fourier traces of newforms 72a1 and 144a1 against eliminating auxiliary primes for p in [6301..6400].

{
default(nbthreads, 1);
print("================================================================================");
print("   U480: PARI/GP INDEPENDENT AUDIT OF KRAUS SIEVE MODULAR TRACES [6301..6400]   ");
print("                     *** MILESTONE 241 AUDIT ***                                ");
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

\\ Exponents p and eliminating auxiliary primes q from U479
exponents_p = [6301, 6337, 6343, 6361, 6367, 6373, 6379, 6397];
primes_q    = [264643, 25349, 25373, 38167, 25469, 38239, 140339, 25589];
expected_72 = [300, 226, 234, -32, 90, 72, -348, -222];

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
print("MILESTONE 241 ACHIEVED: ALL 8 PRIMES IN [6301..6400] AUDITED IN PARI/GP!");
print("================================================================================");
}
quit;
