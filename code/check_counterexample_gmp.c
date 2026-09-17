/*
 * Section 8: Standalone C+GMP Beal Counterexample Checker
 *
 * REQUIRE EXACT, REPRODUCIBLE COMPUTATION.
 * Validates candidate inputs against all Section 8 requirements:
 * 1. Accepts 6 command-line arguments: A x B y C z as arbitrary-precision integer strings.
 * 2. Positivity: A, B, C > 0 and x, y, z > 0
 * 3. Exponent restrictions: x, y, z >= 3
 * 4. Exact equality: A^x + B^y == C^z
 * 5. Greatest common divisor: gcd(A, gcd(B, C)) == 1
 *
 * Exit codes and statuses:
 *   0: VALID_COUNTEREXAMPLE
 *   1: COMMON_FACTOR_VIOLATION (e.g. 3^3 + 6^3 = 3^5)
 *   2: EXPONENT_TOO_SMALL      (e.g. 3^5 + 10^2 = 7^3)
 *   3: ARITHMETIC_MISMATCH     (e.g. 2^3 + 3^3 != 4^3)
 *   4: NON_POSITIVE_INPUT      (e.g. A <= 0 or x <= 0)
 *   5: INVALID_INPUT           (non-integer string or wrong argument count)
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <gmp.h>

typedef enum {
    STATUS_VALID_COUNTEREXAMPLE   = 0,
    STATUS_COMMON_FACTOR_VIOLATION = 1,
    STATUS_EXPONENT_TOO_SMALL     = 2,
    STATUS_ARITHMETIC_MISMATCH    = 3,
    STATUS_NON_POSITIVE_INPUT     = 4,
    STATUS_INVALID_INPUT          = 5
} StatusCode;

static const char *status_to_string(StatusCode code) {
    switch (code) {
        case STATUS_VALID_COUNTEREXAMPLE:    return "VALID_COUNTEREXAMPLE";
        case STATUS_COMMON_FACTOR_VIOLATION: return "COMMON_FACTOR_VIOLATION";
        case STATUS_EXPONENT_TOO_SMALL:      return "EXPONENT_TOO_SMALL";
        case STATUS_ARITHMETIC_MISMATCH:     return "ARITHMETIC_MISMATCH";
        case STATUS_NON_POSITIVE_INPUT:      return "NON_POSITIVE_INPUT";
        case STATUS_INVALID_INPUT:           return "INVALID_INPUT";
        default:                             return "UNKNOWN_ERROR";
    }
}

/* Validates that a string is a well-formed signed decimal integer */
static bool is_valid_integer_string(const char *s) {
    if (!s || *s == '\0') return false;
    if (*s == '+' || *s == '-') s++;
    if (*s == '\0') return false;
    while (*s) {
        if (*s < '0' || *s > '9') return false;
        s++;
    }
    return true;
}

static void print_usage(const char *prog_name) {
    fprintf(stderr, "Usage: %s [--json|--text] <A> <x> <B> <y> <C> <z>\n", prog_name);
    fprintf(stderr, "Checks Section 8 Beal conjecture counterexample conditions for A^x + B^y = C^z.\n");
    fprintf(stderr, "Arguments:\n");
    fprintf(stderr, "  A, B, C : Bases (arbitrary-precision integer strings)\n");
    fprintf(stderr, "  x, y, z : Exponents (arbitrary-precision integer strings)\n");
    fprintf(stderr, "\nExit codes / Statuses:\n");
    fprintf(stderr, "  0: VALID_COUNTEREXAMPLE\n");
    fprintf(stderr, "  1: COMMON_FACTOR_VIOLATION\n");
    fprintf(stderr, "  2: EXPONENT_TOO_SMALL\n");
    fprintf(stderr, "  3: ARITHMETIC_MISMATCH\n");
    fprintf(stderr, "  4: NON_POSITIVE_INPUT\n");
    fprintf(stderr, "  5: INVALID_INPUT\n");
}

int main(int argc, char *argv[]) {
    bool json_output = true;
    const char *inputs[6];
    int input_count = 0;

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--json") == 0) {
            json_output = true;
        } else if (strcmp(argv[i], "--text") == 0) {
            json_output = false;
        } else if (strcmp(argv[i], "--help") == 0 || strcmp(argv[i], "-h") == 0) {
            print_usage(argv[0]);
            return STATUS_VALID_COUNTEREXAMPLE;
        } else {
            if (input_count < 6) {
                inputs[input_count++] = argv[i];
            } else {
                input_count++; /* Excess arguments */
            }
        }
    }

    if (input_count != 6) {
        if (json_output) {
            printf("{\n");
            printf("  \"status\": \"%s\",\n", status_to_string(STATUS_INVALID_INPUT));
            printf("  \"code\": %d,\n", STATUS_INVALID_INPUT);
            printf("  \"admissible\": false,\n");
            printf("  \"equality\": false,\n");
            printf("  \"primitive\": false,\n");
            printf("  \"counterexample\": false,\n");
            printf("  \"reason\": \"Expected exactly 6 integer arguments (A x B y C z), received %d\"\n", input_count);
            printf("}\n");
        } else {
            printf("STATUS: %s\n", status_to_string(STATUS_INVALID_INPUT));
            printf("CODE: %d\n", STATUS_INVALID_INPUT);
            printf("REASON: Expected exactly 6 integer arguments (A x B y C z), received %d\n", input_count);
        }
        return STATUS_INVALID_INPUT;
    }

    /* Validate that all 6 strings are well-formed decimal integers */
    const char *names[6] = {"A", "x", "B", "y", "C", "z"};
    for (int i = 0; i < 6; i++) {
        if (!is_valid_integer_string(inputs[i])) {
            if (json_output) {
                printf("{\n");
                printf("  \"status\": \"%s\",\n", status_to_string(STATUS_INVALID_INPUT));
                printf("  \"code\": %d,\n", STATUS_INVALID_INPUT);
                printf("  \"admissible\": false,\n");
                printf("  \"equality\": false,\n");
                printf("  \"primitive\": false,\n");
                printf("  \"counterexample\": false,\n");
                printf("  \"reason\": \"Invalid non-integer argument for %s: '%s'\"\n", names[i], inputs[i]);
                printf("}\n");
            } else {
                printf("STATUS: %s\n", status_to_string(STATUS_INVALID_INPUT));
                printf("CODE: %d\n", STATUS_INVALID_INPUT);
                printf("REASON: Invalid non-integer argument for %s: '%s'\n", names[i], inputs[i]);
            }
            return STATUS_INVALID_INPUT;
        }
    }

    mpz_t A, x, B, y, C, z;
    mpz_inits(A, x, B, y, C, z, NULL);

    if (mpz_set_str(A, inputs[0], 10) != 0 ||
        mpz_set_str(x, inputs[1], 10) != 0 ||
        mpz_set_str(B, inputs[2], 10) != 0 ||
        mpz_set_str(y, inputs[3], 10) != 0 ||
        mpz_set_str(C, inputs[4], 10) != 0 ||
        mpz_set_str(z, inputs[5], 10) != 0) {
        mpz_clears(A, x, B, y, C, z, NULL);
        if (json_output) {
            printf("{\n");
            printf("  \"status\": \"%s\",\n", status_to_string(STATUS_INVALID_INPUT));
            printf("  \"code\": %d,\n", STATUS_INVALID_INPUT);
            printf("  \"reason\": \"Failed to parse arbitrary-precision integer input\"\n");
            printf("}\n");
        } else {
            printf("STATUS: %s\n", status_to_string(STATUS_INVALID_INPUT));
            printf("CODE: %d\n", STATUS_INVALID_INPUT);
            printf("REASON: Failed to parse arbitrary-precision integer input\n");
        }
        return STATUS_INVALID_INPUT;
    }

    /* Check Positivity: A, B, C > 0 and x, y, z > 0 */
    if (mpz_sgn(A) <= 0 || mpz_sgn(B) <= 0 || mpz_sgn(C) <= 0 ||
        mpz_sgn(x) <= 0 || mpz_sgn(y) <= 0 || mpz_sgn(z) <= 0) {
        char reason_buf[256];
        snprintf(reason_buf, sizeof(reason_buf),
                 "Positivity violation: all bases (A, B, C) and exponents (x, y, z) must be strictly positive integers (> 0)");
        if (json_output) {
            printf("{\n");
            printf("  \"status\": \"%s\",\n", status_to_string(STATUS_NON_POSITIVE_INPUT));
            printf("  \"code\": %d,\n", STATUS_NON_POSITIVE_INPUT);
            printf("  \"admissible\": false,\n");
            printf("  \"equality\": false,\n");
            printf("  \"primitive\": false,\n");
            printf("  \"counterexample\": false,\n");
            printf("  \"reason\": \"%s\"\n", reason_buf);
            printf("}\n");
        } else {
            printf("STATUS: %s\n", status_to_string(STATUS_NON_POSITIVE_INPUT));
            printf("CODE: %d\n", STATUS_NON_POSITIVE_INPUT);
            printf("REASON: %s\n", reason_buf);
        }
        mpz_clears(A, x, B, y, C, z, NULL);
        return STATUS_NON_POSITIVE_INPUT;
    }

    /* Compute Greatest Common Divisor: gcd(A, gcd(B, C)) */
    mpz_t g_bc, g_all;
    mpz_inits(g_bc, g_all, NULL);
    mpz_gcd(g_bc, B, C);
    mpz_gcd(g_all, A, g_bc);
    bool primitive = (mpz_cmp_ui(g_all, 1) == 0);
    char *g_str = mpz_get_str(NULL, 10, g_all);

    /* Check Exponent Restrictions: x, y, z >= 3 */
    bool exp_admissible = (mpz_cmp_ui(x, 3) >= 0 &&
                           mpz_cmp_ui(y, 3) >= 0 &&
                           mpz_cmp_ui(z, 3) >= 0);

    /* Check Exact Equality: A^x + B^y == C^z */
    bool equality = false;
    bool can_compute_power = true;

    /* Check if exponents fit in unsigned long for mpz_pow_ui */
    if (!mpz_fits_ulong_p(x) || !mpz_fits_ulong_p(y) || !mpz_fits_ulong_p(z)) {
        can_compute_power = false;
    }

    /* Exponent upper limit check to avoid memory exhaustion (e.g. exp <= 10,000,000) */
    if (can_compute_power) {
        if (mpz_cmp_ui(x, 10000000UL) > 0 ||
            mpz_cmp_ui(y, 10000000UL) > 0 ||
            mpz_cmp_ui(z, 10000000UL) > 0) {
            can_compute_power = false;
        }
    }

    mpz_t Ax, By, Cz, lhs;
    mpz_inits(Ax, By, Cz, lhs, NULL);

    if (can_compute_power) {
        unsigned long ux = mpz_get_ui(x);
        unsigned long uy = mpz_get_ui(y);
        unsigned long uz = mpz_get_ui(z);

        mpz_pow_ui(Ax, A, ux);
        mpz_pow_ui(By, B, uy);
        mpz_pow_ui(Cz, C, uz);

        mpz_add(lhs, Ax, By);
        equality = (mpz_cmp(lhs, Cz) == 0);
    }

    StatusCode final_status;
    char reason[512];

    if (!exp_admissible) {
        final_status = STATUS_EXPONENT_TOO_SMALL;
        char x_str[32], y_str[32], z_str[32];
        gmp_snprintf(x_str, sizeof(x_str), "%Zd", x);
        gmp_snprintf(y_str, sizeof(y_str), "%Zd", y);
        gmp_snprintf(z_str, sizeof(z_str), "%Zd", z);
        if (equality) {
            snprintf(reason, sizeof(reason),
                     "Valid equality (%s^%s + %s^%s == %s^%s), but excluded because exponent is < 3 (x=%s, y=%s, z=%s)",
                     inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5],
                     x_str, y_str, z_str);
        } else {
            snprintf(reason, sizeof(reason),
                     "Exponent restriction violated (x, y, z must all be >= 3): x=%s, y=%s, z=%s",
                     x_str, y_str, z_str);
        }
    } else if (!equality) {
        final_status = STATUS_ARITHMETIC_MISMATCH;
        snprintf(reason, sizeof(reason),
                 "Arithmetic mismatch: %s^%s + %s^%s != %s^%s",
                 inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5]);
    } else if (!primitive) {
        final_status = STATUS_COMMON_FACTOR_VIOLATION;
        snprintf(reason, sizeof(reason),
                 "Valid equality (%s^%s + %s^%s == %s^%s), but bases share common factor gcd(A, B, C) = %s > 1 (satisfies Beal conjecture)",
                 inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], g_str);
    } else {
        final_status = STATUS_VALID_COUNTEREXAMPLE;
        snprintf(reason, sizeof(reason),
                 "Genuine Beal counterexample verified: %s^%s + %s^%s == %s^%s with gcd(%s, %s, %s) == 1",
                 inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5],
                 inputs[0], inputs[2], inputs[4]);
    }

    bool admissible = exp_admissible;
    bool counterexample = (final_status == STATUS_VALID_COUNTEREXAMPLE);

    if (json_output) {
        printf("{\n");
        printf("  \"status\": \"%s\",\n", status_to_string(final_status));
        printf("  \"code\": %d,\n", final_status);
        printf("  \"admissible\": %s,\n", admissible ? "true" : "false");
        printf("  \"equality\": %s,\n", equality ? "true" : "false");
        printf("  \"primitive\": %s,\n", primitive ? "true" : "false");
        printf("  \"counterexample\": %s,\n", counterexample ? "true" : "false");
        printf("  \"A\": \"%s\",\n", inputs[0]);
        printf("  \"x\": \"%s\",\n", inputs[1]);
        printf("  \"B\": \"%s\",\n", inputs[2]);
        printf("  \"y\": \"%s\",\n", inputs[3]);
        printf("  \"C\": \"%s\",\n", inputs[4]);
        printf("  \"z\": \"%s\",\n", inputs[5]);
        printf("  \"gcd\": \"%s\",\n", g_str);
        printf("  \"reason\": \"%s\"\n", reason);
        printf("}\n");
    } else {
        printf("STATUS: %s\n", status_to_string(final_status));
        printf("CODE: %d\n", final_status);
        printf("ADMISSIBLE: %s\n", admissible ? "true" : "false");
        printf("EQUALITY: %s\n", equality ? "true" : "false");
        printf("PRIMITIVE: %s\n", primitive ? "true" : "false");
        printf("COUNTEREXAMPLE: %s\n", counterexample ? "true" : "false");
        printf("GCD: %s\n", g_str);
        printf("REASON: %s\n", reason);
    }

    free(g_str);
    mpz_clears(A, x, B, y, C, z, g_bc, g_all, Ax, By, Cz, lhs, NULL);
    return final_status;
}
