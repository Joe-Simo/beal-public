# Makefile for Beal Conjecture High-Performance Search Tool
CC ?= clang
CFLAGS ?= -O3 -Wall -Wextra -pthread
INCLUDES ?= -I/opt/homebrew/include -I/usr/local/include
LDFLAGS ?= -L/opt/homebrew/lib -L/usr/local/lib -lgmp -lpthread
PYTHON ?= python3

TARGET = beal_search_gmp
SRC = beal_search_gmp.c

.PHONY: all clean test bench run_all

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) $(INCLUDES) $(LDFLAGS) -o $@ $<

test: $(TARGET)
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
	rm -f $(TARGET)
	rm -f search_log_*.json
	rm -rf __pycache__
