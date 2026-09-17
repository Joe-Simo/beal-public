# Makefile for Beal Conjecture High-Performance Search & Section 8 Checker
CC ?= clang
CFLAGS ?= -O3 -Wall -Wextra -pthread
INCLUDES ?= -I/opt/homebrew/include -I/opt/homebrew/opt/gmp/include -I/usr/local/include
LDFLAGS ?= -L/opt/homebrew/lib -L/opt/homebrew/opt/gmp/lib -L/usr/local/lib -lgmp -lpthread
PYTHON ?= python3

TARGET = beal_search_gmp
SRC = beal_search_gmp.c

CHECKER_TARGET = check_counterexample_gmp
CHECKER_SRC = check_counterexample_gmp.c

.PHONY: all clean test bench run_all $(CHECKER_TARGET) code/check_counterexample_gmp

all: $(TARGET) $(CHECKER_TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) $(INCLUDES) $(LDFLAGS) -o $@ $<

$(CHECKER_TARGET): $(CHECKER_SRC)
	$(CC) $(CFLAGS) $(INCLUDES) $(LDFLAGS) -o $@ $<

code/check_counterexample_gmp: $(CHECKER_TARGET)

test: $(TARGET) $(CHECKER_TARGET)
	@echo "=== Running C+GMP Section 8 Counterexample Checker Suite ==="
	$(PYTHON) test_check_counterexample_gmp.py
	@echo "=== Running C+GMP Section 8 Near-Miss & Edge-Case Suite ==="
	./$(TARGET) --test-near-misses --verbose
	@echo "=== Running Python Section 8 Test Suite ==="
	$(PYTHON) test_section8_counterexample_checker.py
	@echo "=== Running Comprehensive Search & Integration Test Suite ==="
	$(PYTHON) test_beal_search.py

bench: $(TARGET)
	@echo "=== Running Multi-Threaded Benchmark Suite ==="
	./$(TARGET) --benchmark --threads 8

run_python_search:
	$(PYTHON) beal_search.py --max-base 1000 --max-exp 10 --threads 8

run_gmp_search: $(TARGET)
	./$(TARGET) --max-base 5000 --max-exp 10 --threads 8

clean:
	rm -f $(TARGET) $(CHECKER_TARGET)
	rm -f search_log_*.json
	rm -rf __pycache__
