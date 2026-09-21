/*
 * High-Performance Native C / OpenMP Kraus Modular Sieve Engine
 * Target: Signature (3, 3, p) against newforms 72a1 and 144a1.
 *
 * Computes exact Frobenius traces over F_q with O(q) array-lookup Legendre tables
 * and OpenMP multi-threaded parallelization.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>
#include <math.h>
#include <omp.h>
#include <gmp.h>

typedef struct {
    uint32_t p;
    uint64_t q;
    uint32_t k;
    int32_t aq_72;
    int32_t aq_144;
    size_t size_adm;
    bool eliminated;
} PrimeCert;

/* Fast modular inverse mod q via extended Euclidean algorithm */
static inline int64_t mod_inv64(int64_t a, int64_t m) {
    int64_t m0 = m, t, q;
    int64_t x0 = 0, x1 = 1;
    if (m == 1) return 0;
    a = (a % m + m) % m;
    while (a > 1) {
        q = a / m;
        t = m;
        m = a % m, a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }
    if (x1 < 0) x1 += m0;
    return x1;
}

/* Fast modular exponentiation (base^exp % mod) */
static inline uint64_t pow_mod64(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (unsigned __int128)res * base % mod;
        base = (unsigned __int128)base * base % mod;
        exp >>= 1;
    }
    return res;
}

/* Fast prime test for q using Miller-Rabin */
static inline bool is_prime64(uint64_t n) {
    if (n < 2) return false;
    if (n == 2 || n == 3 || n == 5 || n == 7) return true;
    if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0) return false;

    uint64_t d = n - 1;
    int s = 0;
    while ((d & 1) == 0) {
        d >>= 1;
        s++;
    }

    static const uint64_t bases[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (size_t b = 0; b < 12; b++) {
        uint64_t a = bases[b];
        if (n <= a) break;
        uint64_t x = pow_mod64(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool composite = true;
        for (int r = 1; r < s; r++) {
            x = (unsigned __int128)x * x % n;
            if (x == n - 1) {
                composite = false;
                break;
            }
        }
        if (composite) return false;
    }
    return true;
}

/* Find primitive root mod prime q */
static uint64_t find_primitive_root(uint64_t q) {
    uint64_t phi = q - 1;
    uint64_t n = phi;
    uint64_t factors[32];
    size_t num_factors = 0;

    for (uint64_t i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            factors[num_factors++] = i;
            while (n % i == 0) n /= i;
        }
    }
    if (n > 1) factors[num_factors++] = n;

    for (uint64_t res = 2; res < q; res++) {
        bool ok = true;
        for (size_t i = 0; i < num_factors; i++) {
            if (pow_mod64(res, phi / factors[i], q) == 1) {
                ok = false;
                break;
            }
        }
        if (ok) return res;
    }
    return 2;
}

/* Fast trace computation for y^2 = x^3 + a4*x + a6 mod q using precomputed Legendre table */
static inline int32_t trace_weierstrass_c(int64_t a4, int64_t a6, uint64_t q, const int8_t *leg) {
    int32_t sum = 0;
    uint64_t u_a4 = (uint64_t)((a4 % (int64_t)q + q) % q);
    uint64_t u_a6 = (uint64_t)((a6 % (int64_t)q + q) % q);

    for (uint64_t x = 0; x < q; x++) {
        uint64_t x2 = (x * x) % q;
        uint64_t x3 = (x2 * x) % q;
        uint64_t rhs = (x3 + u_a4 * x + u_a6) % q;
        sum += leg[rhs];
    }
    return -sum;
}

static __thread int8_t *t_leg = NULL;
static __thread size_t t_leg_cap = 0;

/* Sieve a single prime exponent p */
static PrimeCert sieve_prime(uint32_t p, uint32_t max_k) {
    PrimeCert cert;
    cert.p = p;
    cert.q = 0;
    cert.k = 0;
    cert.aq_72 = 0;
    cert.aq_144 = 0;
    cert.size_adm = 0;
    cert.eliminated = false;

    uint64_t p_sq = (uint64_t)p * p;

    for (uint32_t k = 1; k <= max_k; k++) {
        uint64_t q = 2ULL * k * p + 1ULL;
        if (!is_prime64(q)) continue;

        /* Integer rigidity condition */
        if (16ULL * q >= p_sq) continue;

        /* Ensure thread-local Legendre table buffer is large enough */
        if (q > t_leg_cap) {
            size_t new_cap = q + 65536;
            int8_t *new_ptr = (int8_t *)realloc(t_leg, new_cap * sizeof(int8_t));
            if (!new_ptr) continue;
            t_leg = new_ptr;
            t_leg_cap = new_cap;
        }
        int8_t *leg = t_leg;
        memset(leg, 0, q * sizeof(int8_t));

        leg[0] = 0;
        uint64_t half_q = (q - 1) / 2;
        for (uint64_t r = 1; r <= half_q; r++) {
            uint64_t sq = (unsigned __int128)r * r % q;
            leg[sq] = 1;
        }
        for (uint64_t r = 1; r < q; r++) {
            if (leg[r] == 0) leg[r] = -1;
        }

        /* Compute newform traces */
        int32_t aq_72 = trace_weierstrass_c(6, -7, q, leg);
        int32_t aq_144 = trace_weierstrass_c(6, 7, q, leg);

        /* Generate Up = (F_q^*)^p */
        uint64_t g = find_primitive_root(q);
        uint64_t gen_Up = pow_mod64(g, p, q);
        size_t size_up = 2 * k;

        uint64_t Up_stack[1024];
        uint64_t *Up = (size_up <= 1024) ? Up_stack : (uint64_t *)malloc(size_up * sizeof(uint64_t));
        uint64_t cur = 1;
        for (size_t i = 0; i < size_up; i++) {
            Up[i] = cur;
            cur = (unsigned __int128)cur * gen_Up % q;
        }

        /* Generate valid t ratios */
        int64_t inv3 = mod_inv64(3, q);
        uint64_t p_minus_1 = p - 1;
        uint64_t pow3_p1 = pow_mod64(3, p_minus_1, q);
        int64_t inv3_p1 = mod_inv64(pow3_p1, q);

        /* Hash set for valid t */
        size_t max_t = size_up * 3;
        uint64_t valid_t_stack[1024];
        uint64_t *valid_t = (max_t <= 1024) ? valid_t_stack : (uint64_t *)malloc(max_t * sizeof(uint64_t));
        size_t num_t = 0;

        for (size_t i = 0; i < size_up; i++) {
            uint64_t u = Up[i];
            // tA = (u - 1) % q
            uint64_t tA = (u + q - 1) % q;
            if (tA != 0) valid_t[num_t++] = tA;

            // tB = (u - 1) * inv3 % q
            uint64_t tB = (unsigned __int128)(u + q - 1) * inv3 % q;
            if (tB != 0) valid_t[num_t++] = tB;

            // tC = (u - inv3_p1) * inv3 % q
            uint64_t tC = (unsigned __int128)(u + q - (inv3_p1 % q)) * inv3 % q;
            if (tC != 0) valid_t[num_t++] = tC;
        }

        /* Sort and deduplicate valid_t */
        for (size_t i = 0; i < num_t; i++) {
            for (size_t j = i + 1; j < num_t; j++) {
                if (valid_t[i] > valid_t[j]) {
                    uint64_t tmp = valid_t[i];
                    valid_t[i] = valid_t[j];
                    valid_t[j] = tmp;
                }
            }
        }
        size_t unique_t = 0;
        for (size_t i = 0; i < num_t; i++) {
            if (i == 0 || valid_t[i] != valid_t[i - 1]) {
                valid_t[unique_t++] = valid_t[i];
            }
        }

        /* Compute admissible traces */
        int32_t adm_stack[1024];
        int32_t *adm = (unique_t <= 1024) ? adm_stack : (int32_t *)malloc(unique_t * sizeof(int32_t));
        size_t num_adm = 0;
        bool aq_72_matched = false;
        bool aq_144_matched = false;

        for (size_t i = 0; i < unique_t; i++) {
            uint64_t t = valid_t[i];
            if ((t + 1) % q == 0) continue;

            uint64_t prod = (unsigned __int128)t * (t + 1) % q;
            int64_t a4 = (-3 * (int64_t)prod) % (int64_t)q;
            int64_t a6 = ((unsigned __int128)prod * (2 * t + 1)) % q;

            int32_t aq = trace_weierstrass_c(a4, a6, q, leg);
            adm[num_adm++] = aq;

            if (aq == aq_72) {
                aq_72_matched = true;
                break;
            }
            if (aq == aq_144) {
                aq_144_matched = true;
                break;
            }
        }

        if (Up != Up_stack) free(Up);
        if (valid_t != valid_t_stack) free(valid_t);
        if (adm != adm_stack) free(adm);

        if (!aq_72_matched && !aq_144_matched) {
            cert.q = q;
            cert.k = k;
            cert.aq_72 = aq_72;
            cert.aq_144 = aq_144;
            cert.size_adm = num_adm;
            cert.eliminated = true;
            return cert;
        }
    }

    return cert;
}

int main(int argc, char *argv[]) {
    uint32_t p_min = 30001;
    uint32_t p_max = 35000;
    uint32_t max_k = 100;
    const char *out_file = NULL;
    int pos_idx = 0;

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--p-min") == 0 && i + 1 < argc) {
            p_min = (uint32_t)atoi(argv[++i]);
        } else if (strcmp(argv[i], "--p-max") == 0 && i + 1 < argc) {
            p_max = (uint32_t)atoi(argv[++i]);
        } else if (strcmp(argv[i], "--max-k") == 0 && i + 1 < argc) {
            max_k = (uint32_t)atoi(argv[++i]);
        } else if (strcmp(argv[i], "--out") == 0 && i + 1 < argc) {
            out_file = argv[++i];
        } else if (argv[i][0] != '-') {
            if (pos_idx == 0) p_min = (uint32_t)atoi(argv[i]);
            else if (pos_idx == 1) p_max = (uint32_t)atoi(argv[i]);
            else if (pos_idx == 2) max_k = (uint32_t)atoi(argv[i]);
            pos_idx++;
        }
    }

    printf("=================================================================\n");
    printf("FAST NATIVE C KRAUS MODULAR SIEVE ENGINE\n");
    printf("Exponent Range: p in [%u, %u], Max Multiplier k: %u\n", p_min, p_max, max_k);
    printf("Threads: %d (OpenMP Parallelism)\n", omp_get_max_threads());
    printf("=================================================================\n");

    /* Collect primes in [p_min, p_max] */
    uint32_t *primes = (uint32_t *)malloc((p_max - p_min + 1) * sizeof(uint32_t));
    size_t num_primes = 0;
    for (uint32_t p = p_min; p <= p_max; p++) {
        if (is_prime64(p)) {
            primes[num_primes++] = p;
        }
    }
    printf("Target Primes: %zu\n", num_primes);

    PrimeCert *certs = (PrimeCert *)malloc(num_primes * sizeof(PrimeCert));
    size_t eliminated_count = 0;

    struct timespec t0, t1;
    clock_gettime(CLOCK_MONOTONIC, &t0);

    #pragma omp parallel for schedule(dynamic, 1) reduction(+:eliminated_count)
    for (size_t i = 0; i < num_primes; i++) {
        certs[i] = sieve_prime(primes[i], max_k);
        if (certs[i].eliminated) {
            eliminated_count++;
        }
    }

    clock_gettime(CLOCK_MONOTONIC, &t1);
    double elapsed = (t1.tv_sec - t0.tv_sec) + (t1.tv_nsec - t0.tv_nsec) * 1e-9;
    double rate = (double)eliminated_count / num_primes * 100.0;

    uint32_t max_k_used = 0;
    for (size_t i = 0; i < num_primes; i++) {
        if (certs[i].eliminated && certs[i].k > max_k_used) {
            max_k_used = certs[i].k;
        }
    }

    printf("=================================================================\n");
    printf("KRAUS MODULAR SIEVE COMPLETE\n");
    printf("  Target Primes:        %zu\n", num_primes);
    printf("  Eliminated:           %zu (%.2f%%)\n", eliminated_count, rate);
    printf("  Max Multiplier k:     %u\n", max_k_used);
    printf("  Elapsed Time:         %.4f seconds (%.2f primes/sec)\n", elapsed, num_primes / elapsed);
    printf("=================================================================\n");

    if (out_file) {
        FILE *fp = fopen(out_file, "w");
        if (fp) {
            fprintf(fp, "{\n");
            fprintf(fp, "  \"status\": \"completed\",\n");
            fprintf(fp, "  \"exponent_range\": [%u, %u],\n", p_min, p_max);
            fprintf(fp, "  \"prime_count\": %zu,\n", num_primes);
            fprintf(fp, "  \"eliminated_count\": %zu,\n", eliminated_count);
            fprintf(fp, "  \"uneliminated_count\": %zu,\n", num_primes - eliminated_count);
            fprintf(fp, "  \"elimination_rate_percent\": %.2f,\n", rate);
            fprintf(fp, "  \"all_eliminated\": %s,\n", eliminated_count == num_primes ? "true" : "false");
            fprintf(fp, "  \"max_multiplier_k\": %u,\n", max_k_used);
            fprintf(fp, "  \"elapsed_seconds\": %.4f,\n", elapsed);
            fprintf(fp, "  \"target_newforms\": [\"72a1\", \"144a1\"],\n");
            fprintf(fp, "  \"certificates\": [\n");
            for (size_t i = 0; i < num_primes; i++) {
                if (certs[i].eliminated) {
                    fprintf(fp, "    {\"p\": %u, \"q\": %llu, \"k\": %u, \"aq_72\": %d, \"aq_144\": %d, \"size_adm\": %zu, \"eliminated_72a1\": true, \"eliminated_144a1\": true}%s\n",
                            certs[i].p, (unsigned long long)certs[i].q, certs[i].k,
                            certs[i].aq_72, certs[i].aq_144, certs[i].size_adm,
                            i == num_primes - 1 ? "" : ",");
                }
            }
            fprintf(fp, "  ]\n");
            fprintf(fp, "}\n");
            fclose(fp);
            printf("Wrote certificates to: %s\n", out_file);
        }
    }

    free(primes);
    free(certs);
    return (eliminated_count == num_primes) ? 0 : 1;
}
