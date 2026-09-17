#!/usr/bin/env bash
# Section 8 C+GMP Counterexample Checker Bash Test Runner
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN="${SCRIPT_DIR}/check_counterexample_gmp"

if [[ ! -x "$BIN" ]]; then
    echo "Building ${BIN}..."
    make -C "$SCRIPT_DIR" check_counterexample_gmp
fi

echo "=== Running C+GMP Section 8 Counterexample Checker Bash Tests ==="

total=0
passed=0

assert_exit_code() {
    local expected="$1"
    local desc="$2"
    shift 2
    total=$((total + 1))

    set +e
    "$BIN" "$@" > /dev/null 2>&1
    local code=$?
    set -e

    if [[ "$code" -eq "$expected" ]]; then
        passed=$((passed + 1))
        echo "  ✔ [Exit $expected] $desc"
    else
        echo "  ✖ [FAILED] $desc (Expected exit $expected, got $code)"
        exit 1
    fi
}

# 1. Common Factor Violations (Exit 1)
assert_exit_code 1 "3^3 + 6^3 = 3^5 (COMMON_FACTOR_VIOLATION)" 3 3 6 3 3 5
assert_exit_code 1 "7^3 + 7^4 = 14^3 (COMMON_FACTOR_VIOLATION)" 7 3 7 4 14 3
assert_exit_code 1 "2^3 + 2^3 = 2^4 (COMMON_FACTOR_VIOLATION)" 2 3 2 3 2 4

# 2. Exponent Restrictions (Exit 2)
assert_exit_code 2 "3^5 + 10^2 = 7^3 (EXPONENT_TOO_SMALL, y=2)" 3 5 10 2 7 3
assert_exit_code 2 "2^5 + 7^2 = 3^4 (EXPONENT_TOO_SMALL, y=2)" 2 5 7 2 3 4
assert_exit_code 2 "13^2 + 7^3 = 2^9 (EXPONENT_TOO_SMALL, x=2)" 13 2 7 3 2 9
assert_exit_code 2 "1^3 + 2^3 = 3^2 (EXPONENT_TOO_SMALL, z=2)" 1 3 2 3 3 2

# 3. Arithmetic Mismatches (Exit 3)
assert_exit_code 3 "2^3 + 3^3 != 4^3 (ARITHMETIC_MISMATCH)" 2 3 3 3 4 3
assert_exit_code 3 "3^3 + 4^3 != 5^3 (ARITHMETIC_MISMATCH)" 3 3 4 3 5 3
assert_exit_code 3 "1^3 + 2^3 != 3^3 (ARITHMETIC_MISMATCH, base 1)" 1 3 2 3 3 3

# 4. Non-Positive Inputs (Exit 4)
assert_exit_code 4 "Zero base A (NON_POSITIVE_INPUT)" 0 3 3 3 4 3
assert_exit_code 4 "Zero exponent x (NON_POSITIVE_INPUT)" 3 0 3 3 4 3
assert_exit_code 4 "Negative base B (NON_POSITIVE_INPUT)" 3 3 -1 3 4 3
assert_exit_code 4 "Negative exponent z (NON_POSITIVE_INPUT)" 3 3 3 3 4 -1

# 5. Invalid Inputs (Exit 5)
assert_exit_code 5 "Decimal string '1.5' (INVALID_INPUT)" 1.5 3 3 3 4 3
assert_exit_code 5 "Alphabetic string 'abc' (INVALID_INPUT)" abc 3 3 3 4 3
assert_exit_code 5 "Too few arguments (INVALID_INPUT)" 3 3 3
assert_exit_code 5 "Too many arguments (INVALID_INPUT)" 3 3 3 3 3 3 3

# 6. Beyond Safe-Integer Limits
BASE60="1152921504606846976" # 2^60
assert_exit_code 1 "(2^60)^3 + (2^60)^3 = 2^181 (COMMON_FACTOR_VIOLATION)" "$BASE60" 3 "$BASE60" 3 2 181
assert_exit_code 3 "Large integer mismatch (ARITHMETIC_MISMATCH)" "$BASE60" 3 "$BASE60" 3 3 181

echo "================================================================="
echo "Bash Test Suite Completed: ${passed}/${total} tests passed."
echo "================================================================="
