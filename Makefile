# Root Makefile forwarding to code/Makefile
.PHONY: all test clean check_counterexample_gmp code/check_counterexample_gmp

all:
	$(MAKE) -C code all

check_counterexample_gmp:
	$(MAKE) -C code check_counterexample_gmp

code/check_counterexample_gmp:
	$(MAKE) -C code check_counterexample_gmp

test:
	$(MAKE) -C code test

clean:
	$(MAKE) -C code clean
