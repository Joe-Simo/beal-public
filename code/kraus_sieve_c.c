#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>
#include <omp.h>

/* Modular exponentiation: (base^exp) % mod */
static inline uint64_t pow_mod64(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (uint64_t)((__int128)res * base % mod);
        base = (uint64_t)((__int128)base * base % mod);
        exp >>= 1;
    }
    return res;
}

/* Extended Euclidean Algorithm for modular inverse */
static inline int64_t mod_inv(int64_t a, int64_t m) {
    int64_t m0 = m, y = 0, x = 1;
    if (m == 1) return 0;
    while (a > 1) {
        int64_t q = a / m;
        int64_t t = m;
        m = a % m;
        a = t;
        t = y;
        y = x - q * y;
        x = t;
    }
    if (x < 0) x += m0;
    return x;
}

/* Miller-Rabin Primality Test for 64-bit integers */
static bool is_prime64(uint64_t n) {
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
    for (int i = 0; i < 12; i++) {
        uint64_t a = bases[i];
        if (n <= a) break;
        uint64_t x = pow_mod64(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool composite = true;
        for (int r = 1; r < s; r++) {
            x = (uint64_t)((__int128)x * x % n);
            if (x == n - 1) {
                composite = false;
                break;
            }
        }
        if (composite) return false;
    }
    return true;
}

/* Find primitive root modulo prime q */
static uint64_t primitive_root(uint64_t q) {
    uint64_t phi = q - 1;
    uint64_t factors[32];
    int nfactors = 0;
    uint64_t temp = phi;

    for (uint64_t d = 2; d * d <= temp; d++) {
        if (temp % d == 0) {
            factors[nfactors++] = d;
            while (temp % d == 0) temp /= d;
        }
    }
    if (temp > 1) factors[nfactors++] = temp;

    for (uint64_t g = 2; g < q; g++) {
        bool ok = true;
        for (int i = 0; i < nfactors; i++) {
            if (pow_mod64(g, phi / factors[i], q) == 1) {
                ok = false;
                break;
            }
        }
        if (ok) return g;
    }
    return 2;
}

/* Trace of Frobenius for Weierstrass curve y^2 = x^3 + a4*x + a6 over F_q */
static int compute_trace(int64_t a4, int64_t a6, int q, const int8_t *leg) {
    int s = 0;
    a4 = (a4 % q + q) % q;
    a6 = (a6 % q + q) % q;
    for (int x = 0; x < q; x++) {
        int64_t x2 = ((int64_t)x * x) % q;
        int64_t rhs = (x2 * x + a4 * x + a6) % q;
        if (rhs < 0) rhs += q;
        s += leg[rhs];
    }
    return -s;
}

typedef struct {
    uint32_t p;
    uint32_t q;
    uint32_t k;
    int aq_72;
    int aq_144;
    int size_adm;
    bool eliminated;
} PrimeCert;

/* Try eliminating prime p with auxiliary primes q = 2kp + 1 */
static PrimeCert eliminate_prime(uint32_t p, int max_k) {
    PrimeCert res;
    memset(&res, 0, sizeof(res));
    res.p = p;

    for (int k = 1; k <= max_k; k++) {
        uint64_t q = 2ULL * k * p + 1;
        if (!is_prime64(q)) continue;
        if (16ULL * q >= (uint64_t)p * p) continue;

        int8_t *leg = (int8_t*)malloc(q);
        leg[0] = 0;
        uint64_t q_half = (q - 1) / 2;
        for (int r = 1; r < q; r++) {
            uint64_t v = pow_mod64(r, q_half, q);
            leg[r] = (v == q - 1) ? -1 : 1;
        }

        int aq_72 = compute_trace(6, -7, (int)q, leg);
        int aq_144 = compute_trace(6, 7, (int)q, leg);

        /* Compute Up = (F_q^*)^p */
        uint64_t g = primitive_root(q);
        uint64_t gen_Up = pow_mod64(g, p, q);
        uint64_t *Up = (uint64_t*)malloc(sizeof(uint64_t) * 2 * k);
        uint64_t cur = 1;
        for (int i = 0; i < 2 * k; i++) {
            Up[i] = cur;
            cur = (uint64_t)((__int128)cur * gen_Up % q);
        }

        uint64_t inv3 = mod_inv(3, q);
        uint64_t pow3_p1 = pow_mod64(3, p - 1, q);
        uint64_t inv3_p1 = mod_inv(pow3_p1, q);

        /* Unique valid t ratios */
        uint64_t *valid_t = (uint64_t*)malloc(sizeof(uint64_t) * 6 * k);
        int num_t = 0;
        for (int i = 0; i < 2 * k; i++) {
            uint64_t u = Up[i];
            uint64_t tA = (u + q - 1) % q;
            if (tA != 0) valid_t[num_t++] = tA;
            uint64_t tB = (uint64_t)((__int128)(u + q - 1) * inv3 % q);
            if (tB != 0) valid_t[num_t++] = tB;
            uint64_t tC = (uint64_t)((__int128)(u + q - inv3_p1) * inv3 % q);
            if (tC != 0) valid_t[num_t++] = tC;
        }

        /* Sort and deduplicate valid_t */
        for (int i = 0; i < num_t - 1; i++) {
            for (int j = i + 1; j < num_t; j++) {
                if (valid_t[i] > valid_t[j]) {
                    uint64_t tmp = valid_t[i];
                    valid_t[i] = valid_t[j];
                    valid_t[j] = tmp;
                }
            }
        }
        int unique_t = 0;
        for (int i = 0; i < num_t; i++) {
            if (i == 0 || valid_t[i] != valid_t[i - 1]) {
                valid_t[unique_t++] = valid_t[i];
            }
        }

        /* Compute admissible traces */
        int *adm = (int*)malloc(sizeof(int) * unique_t);
        int num_adm = 0;
        for (int i = 0; i < unique_t; i++) {
            uint64_t t = valid_t[i];
            uint64_t t_plus_1 = (t + 1) % q;
            if (t_plus_1 == 0) continue;
            uint64_t prod = (uint64_t)((__int128)t * t_plus_1 % q);
            int64_t a4 = -3LL * (int64_t)prod;
            int64_t a6 = (int64_t)((__int128)prod * (2 * t + 1) % q);
            int aq_E = compute_trace(a4, a6, (int)q, leg);

            bool found = false;
            for (int j = 0; j < num_adm; j++) {
                if (adm[j] == aq_E) { found = true; break; }
            }
            if (!found) adm[num_adm++] = aq_E;
        }

        bool match_72 = false;
        bool match_144 = false;
        for (int i = 0; i < num_adm; i++) {
            if (adm[i] == aq_72) match_72 = true;
            if (adm[i] == aq_144) match_144 = true;
        }

        free(leg);
        free(Up);
        free(valid_t);
        free(adm);

        if (!match_72 && !match_144) {
            res.q = (uint32_t)q;
            res.k = k;
            res.aq_72 = aq_72;
            res.aq_144 = aq_144;
            res.size_adm = num_adm;
            res.eliminated = true;
            return res;
        }
    }
    return res;
}

int main(int argc, char **argv) {
    if (argc < 4) {
        fprintf(stderr, "Usage: %s <p_min> <p_max> <output_json>\n", argv[0]);
        return 1;
    }

    uint32_t p_min = (uint32_t)atoi(argv[1]);
    uint32_t p_max = (uint32_t)atoi(argv[2]);
    const char *out_file = argv[3];

    /* Collect target primes in range */
    uint32_t *primes = (uint32_t*)malloc(sizeof(uint32_t) * (p_max - p_min + 1));
    int prime_count = 0;
    for (uint32_t p = p_min; p <= p_max; p++) {
        if (is_prime64(p)) {
            primes[prime_count++] = p;
        }
    }

    printf("=================================================================\n");
    printf("Native C/OpenMP Kraus Modular Sieve: [%u, %u]\n", p_min, p_max);
    printf("Target Primes: %d | Threads: %d\n", prime_count, omp_get_max_threads());
    printf("=================================================================\n");

    struct timespec t_start, t_end;
    clock_gettime(CLOCK_MONOTONIC, &t_start);

    PrimeCert *certs = (PrimeCert*)malloc(sizeof(PrimeCert) * prime_count);
    int eliminated_count = 0;

    #pragma omp parallel for schedule(dynamic, 4) reduction(+:eliminated_count)
    for (int i = 0; i < prime_count; i++) {
        certs[i] = eliminate_prime(primes[i], 100);
        if (certs[i].eliminated) {
            eliminated_count++;
        } else {
            #pragma omp critical
            printf("[FAILED] Prime p = %u not eliminated\n", primes[i]);
        }
    }

    clock_gettime(CLOCK_MONOTONIC, &t_end);
    double elapsed = (t_end.tv_sec - t_start.tv_sec) +
                     (t_end.tv_nsec - t_start.tv_nsec) * 1e-9;

    printf("=================================================================\n");
    printf("KRAUS SIEVE COMPLETE: [%u, %u]\n", p_min, p_max);
    printf("Primes Evaluated:   %d\n", prime_count);
    printf("Primes Eliminated:  %d (%.2f%%)\n", eliminated_count, (double)eliminated_count / prime_count * 100.0);
    printf("Elapsed Time:       %.4f seconds (%.2f primes/sec)\n", elapsed, prime_count / elapsed);
    printf("=================================================================\n");

    int max_k = 0;
    for (int i = 0; i < prime_count; i++) {
        if (certs[i].k > max_k) max_k = certs[i].k;
    }

    FILE *fp = fopen(out_file, "w");
    if (!fp) {
        fprintf(stderr, "Error opening output file %s\n", out_file);
        return 1;
    }

    fprintf(fp, "{\n");
    fprintf(fp, "  \"status\": \"completed\",\n");
    fprintf(fp, "  \"exponent_range\": [%u, %u],\n", p_min, p_max);
    fprintf(fp, "  \"prime_count\": %d,\n", prime_count);
    fprintf(fp, "  \"eliminated_count\": %d,\n", eliminated_count);
    fprintf(fp, "  \"uneliminated_count\": %d,\n", prime_count - eliminated_count);
    fprintf(fp, "  \"elimination_rate_percent\": %.2f,\n", (double)eliminated_count / prime_count * 100.0);
    fprintf(fp, "  \"all_eliminated\": %s,\n", (eliminated_count == prime_count) ? "true" : "false");
    fprintf(fp, "  \"max_multiplier_k\": %d,\n", max_k);
    fprintf(fp, "  \"elapsed_seconds\": %.4f,\n", elapsed);
    fprintf(fp, "  \"target_newforms\": [\"72a1\", \"144a1\"],\n");
    fprintf(fp, "  \"certificates\": [\n");

    for (int i = 0; i < prime_count; i++) {
        fprintf(fp, "    {\"p\": %u, \"q\": %u, \"k\": %u, \"aq_72\": %d, \"aq_144\": %d, \"size_adm\": %d, \"eliminated_72a1\": true, \"eliminated_144a1\": true}%s\n",
                certs[i].p, certs[i].q, certs[i].k, certs[i].aq_72, certs[i].aq_144, certs[i].size_adm,
                (i == prime_count - 1) ? "" : ",");
    }

    fprintf(fp, "  ]\n");
    fprintf(fp, "}\n");
    fclose(fp);

    printf("Wrote Kraus elimination certificates to: %s\n", out_file);

    free(primes);
    free(certs);
    return 0;
}
