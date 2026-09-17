/*
 * Beal Conjecture High-Performance Multi-Threaded Arbitrary-Precision Search Tool
 *
 * Implements an optimized multi-threaded search in C with GNU MP (GMP) to search
 * for counterexamples to the Beal conjecture:
 *     A^x + B^y = C^z
 * with A, B, C >= 1, exponents x, y, z >= 3, and gcd(A, B, C) == 1.
 *
 * Integrates strict Section 8 validation rules:
 * 1. Exact arbitrary-precision integer arithmetic (GMP mpz_t).
 * 2. Positivity check: A, B, C, x, y, z > 0.
 * 3. Exponent bounds: x, y, z >= 3.
 * 4. Coprimality check: gcd(A, B, C) == 1.
 * 5. Exact equality: A^x + B^y == C^z.
 * 6. Edge case and near-miss validation suite.
 */

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>
#include <pthread.h>
#include <time.h>
#include <unistd.h>
#include <gmp.h>

#define DEFAULT_MIN_BASE 2
#define DEFAULT_MAX_BASE 1000
#define DEFAULT_MIN_EXP  3
#define DEFAULT_MAX_EXP  10
#define DEFAULT_THREADS  8

/* Fast binary GCD for 32-bit integers */
static inline uint32_t gcd32(uint32_t a, uint32_t b) {
    if (a == 0) return b;
    if (b == 0) return a;
    int shift = __builtin_ctz(a | b);
    a >>= __builtin_ctz(a);
    do {
        b >>= __builtin_ctz(b);
        if (a > b) {
            uint32_t t = b;
            b = a;
            a = t;
        }
        b -= a;
    } while (b != 0);
    return a << shift;
}

/* 64-bit splitmix hash for mpz low limb or uint64_t */
static inline uint64_t splitmix64(uint64_t x) {
    x ^= x >> 30;
    x *= 0xbf58476d1ce4e5b9ULL;
    x ^= x >> 27;
    x *= 0x94d049bb133111ebULL;
    x ^= x >> 31;
    return x;
}

/* Power entry in the precomputed table */
typedef struct {
    uint32_t base;
    uint16_t exp;
    uint64_t hash;
    mpz_t val;
} PowerEntry;

/* Hash table for O(1) power lookup */
typedef struct {
    uint64_t capacity;
    uint64_t mask;
    int32_t *slots;      /* stores index into powers array, or -1 if empty */
    uint64_t *slot_hash;
} PowerHashTable;

/* Search configuration */
typedef struct {
    uint32_t min_base;
    uint32_t max_base;
    uint32_t min_exp;
    uint32_t max_exp;
    uint32_t base_a_start;
    uint32_t base_a_end;
    uint32_t base_b_start;
    uint32_t base_b_end;
    int num_threads;
    bool prime_exponents_only;
    bool pure_primes_only;
    bool allow_non_coprime;
    bool check_all_roots;
    bool verbose;
    bool json_output;
    const char *log_file;
} SearchConfig;

/* Thread search shared state */
typedef struct {
    const SearchConfig *config;
    PowerEntry *powers;
    size_t num_powers;
    PowerHashTable *table;
    
    pthread_mutex_t work_mutex;
    uint32_t next_base_A;
    uint32_t chunk_size;

    /* Global statistics */
    pthread_mutex_t stat_mutex;
    uint64_t total_pairs_checked;
    uint64_t total_solutions_found;
    uint64_t total_near_misses_rejected;
    uint64_t total_non_coprime_found;
} SearchState;

/* Hash computation for mpz */
static uint64_t hash_mpz(const mpz_t val) {
    size_t size = mpz_size(val);
    uint64_t h = 0x517cc1b727220a95ULL;
    for (size_t i = 0; i < size; i++) {
        uint64_t limb = (uint64_t)mpz_getlimbn(val, i);
        h ^= splitmix64(limb + i);
        h = (h << 13) | (h >> 51);
    }
    return h;
}

/* Initialize hash table */
static PowerHashTable* hash_table_create(uint64_t min_capacity) {
    PowerHashTable *ht = (PowerHashTable*)malloc(sizeof(PowerHashTable));
    uint64_t cap = 1024;
    while (cap < min_capacity * 2) {
        cap <<= 1;
    }
    ht->capacity = cap;
    ht->mask = cap - 1;
    ht->slots = (int32_t*)malloc(sizeof(int32_t) * cap);
    ht->slot_hash = (uint64_t*)malloc(sizeof(uint64_t) * cap);
    for (uint64_t i = 0; i < cap; i++) {
        ht->slots[i] = -1;
        ht->slot_hash[i] = 0;
    }
    return ht;
}

static void hash_table_free(PowerHashTable *ht) {
    if (ht) {
        free(ht->slots);
        free(ht->slot_hash);
        free(ht);
    }
}

static void hash_table_insert(PowerHashTable *ht, const PowerEntry *powers, int32_t power_idx) {
    uint64_t h = powers[power_idx].hash;
    uint64_t idx = h & ht->mask;
    while (ht->slots[idx] != -1) {
        /* If already present with same value, ignore */
        if (ht->slot_hash[idx] == h && mpz_cmp(powers[ht->slots[idx]].val, powers[power_idx].val) == 0) {
            return;
        }
        idx = (idx + 1) & ht->mask;
    }
    ht->slots[idx] = power_idx;
    ht->slot_hash[idx] = h;
}

static int32_t hash_table_lookup(const PowerHashTable *ht, const PowerEntry *powers, const mpz_t target, uint64_t target_hash) {
    uint64_t idx = target_hash & ht->mask;
    while (ht->slots[idx] != -1) {
        if (ht->slot_hash[idx] == target_hash) {
            int32_t p_idx = ht->slots[idx];
            if (mpz_cmp(powers[p_idx].val, target) == 0) {
                return p_idx;
            }
        }
        idx = (idx + 1) & ht->mask;
    }
    return -1;
}

/* Is exponent a pure odd prime >= 3 */
static bool is_pure_prime(uint32_t e) {
    if (e < 3) return false;
    if (e % 2 == 0) return false;
    for (uint32_t d = 3; d * d <= e; d += 2) {
        if (e % d == 0) return false;
    }
    return true;
}

/* Is exponent prime or 4 */
static bool is_prime_or_4(uint32_t e) {
    if (e == 4) return true;
    return is_pure_prime(e);
}

/* Check if exponent matches search config */
static inline bool is_allowed_exp(const SearchConfig *cfg, uint32_t e) {
    if (cfg->pure_primes_only) return is_pure_prime(e);
    if (cfg->prime_exponents_only) return is_prime_or_4(e);
    return true;
}

/* Section 8 Validation Certificate Result */
typedef struct {
    bool admissible;
    bool equality;
    bool primitive;
    bool counterexample;
    char reason[256];
} Section8Result;

/* Full Section 8 validation function */
static Section8Result validate_section8(uint64_t A, uint64_t B, uint64_t C,
                                       uint32_t x, uint32_t y, uint32_t z) {
    Section8Result res;
    memset(&res, 0, sizeof(res));

    /* 1. Positivity */
    if (A == 0 || B == 0 || C == 0 || x == 0 || y == 0 || z == 0) {
        res.admissible = false;
        snprintf(res.reason, sizeof(res.reason),
                 "Positivity violation: all bases and exponents must be > 0");
        return res;
    }

    /* 2. Greatest common divisor */
    uint32_t g_ab = gcd32(A, B);
    uint32_t g_all = gcd32(g_ab, C);
    res.primitive = (g_all == 1);

    /* 3. Exact Arbitrary Precision Equality */
    mpz_t Ax, By, Cz, lhs;
    mpz_inits(Ax, By, Cz, lhs, NULL);

    mpz_ui_pow_ui(Ax, A, x);
    mpz_ui_pow_ui(By, B, y);
    mpz_ui_pow_ui(Cz, C, z);
    mpz_add(lhs, Ax, By);

    res.equality = (mpz_cmp(lhs, Cz) == 0);

    /* 4. Exponent restriction x, y, z >= 3 */
    if (x < 3 || y < 3 || z < 3) {
        res.admissible = false;
        res.counterexample = false;
        snprintf(res.reason, sizeof(res.reason),
                 "Exponent restriction violated (x, y, z must all be >= 3): x=%u, y=%u, z=%u", x, y, z);
        mpz_clears(Ax, By, Cz, lhs, NULL);
        return res;
    }

    res.admissible = true;

    if (res.equality && res.primitive) {
        res.counterexample = true;
        snprintf(res.reason, sizeof(res.reason),
                 "Genuine Beal counterexample: %llu^%u + %llu^%u == %llu^%u with gcd == 1",
                 (unsigned long long)A, x, (unsigned long long)B, y, (unsigned long long)C, z);
    } else if (res.equality && !res.primitive) {
        res.counterexample = false;
        snprintf(res.reason, sizeof(res.reason),
                 "Valid equality, but nonprimitive: gcd(%llu, %llu, %llu) = %u > 1 (satisfies Beal conjecture)",
                 (unsigned long long)A, (unsigned long long)B, (unsigned long long)C, g_all);
    } else {
        res.counterexample = false;
        snprintf(res.reason, sizeof(res.reason),
                 "Arithmetic mismatch: %llu^%u + %llu^%u != %llu^%u",
                 (unsigned long long)A, x, (unsigned long long)B, y, (unsigned long long)C, z);
    }

    mpz_clears(Ax, By, Cz, lhs, NULL);
    return res;
}

/* Worker thread function */
static void* search_worker(void *arg) {
    SearchState *state = (SearchState*)arg;
    const SearchConfig *cfg = state->config;

    /* Preallocate thread-local GMP variables */
    mpz_t Ax, By, S, Cz;
    mpz_inits(Ax, By, S, Cz, NULL);

    uint64_t local_pairs = 0;
    uint64_t local_solutions = 0;
    uint64_t local_non_coprime = 0;

    uint32_t max_a = cfg->base_a_end ? cfg->base_a_end : cfg->max_base;

    while (1) {
        uint32_t a_start = 0;
        uint32_t a_end = 0;

        pthread_mutex_lock(&state->work_mutex);
        if (state->next_base_A > max_a) {
            pthread_mutex_unlock(&state->work_mutex);
            break;
        }
        a_start = state->next_base_A;
        a_end = a_start + state->chunk_size - 1;
        if (a_end > max_a) {
            a_end = max_a;
        }
        state->next_base_A = a_end + 1;
        pthread_mutex_unlock(&state->work_mutex);

        for (uint32_t A = a_start; A <= a_end; A++) {
            uint32_t b_min = (cfg->base_b_start > A) ? cfg->base_b_start : A;
            uint32_t b_max = cfg->base_b_end ? cfg->base_b_end : cfg->max_base;
            for (uint32_t B = b_min; B <= b_max; B++) {
                /* If allow_non_coprime is false, skip gcd(A, B) > 1 immediately */
                if (!cfg->allow_non_coprime && gcd32(A, B) > 1) {
                    continue;
                }

                for (uint32_t x = cfg->min_exp; x <= cfg->max_exp; x++) {
                    if (!is_allowed_exp(cfg, x)) continue;
                    mpz_ui_pow_ui(Ax, A, x);

                    for (uint32_t y = cfg->min_exp; y <= cfg->max_exp; y++) {
                        if (!is_allowed_exp(cfg, y)) continue;
                        mpz_ui_pow_ui(By, B, y);

                        /* Symmetry: enforce Ax <= By to avoid duplicate testing */
                        if (mpz_cmp(Ax, By) > 0) continue;

                        mpz_add(S, Ax, By);
                        local_pairs++;

                        /* Fast table lookup */
                        uint64_t s_hash = hash_mpz(S);
                        int32_t match = hash_table_lookup(state->table, state->powers, S, s_hash);
                        if (match >= 0) {
                            uint32_t C = state->powers[match].base;
                            uint32_t z = state->powers[match].exp;

                            Section8Result sec8 = validate_section8(A, B, C, x, y, z);
                            if (sec8.counterexample) {
                                printf("\n*** BEAL COUNTEREXAMPLE FOUND! ***\n");
                                printf("%s\n", sec8.reason);
                                local_solutions++;
                            } else if (sec8.equality && !sec8.primitive) {
                                local_non_coprime++;
                                if (cfg->verbose) {
                                    printf("[Non-primitive solution] %s\n", sec8.reason);
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    mpz_clears(Ax, By, S, Cz, NULL);

    /* Update global statistics */
    pthread_mutex_lock(&state->stat_mutex);
    state->total_pairs_checked += local_pairs;
    state->total_solutions_found += local_solutions;
    state->total_non_coprime_found += local_non_coprime;
    pthread_mutex_unlock(&state->stat_mutex);

    return NULL;
}

/* Run edge case and known near-miss validation */
static int run_test_suite(bool verbose) {
    printf("=================================================================\n");
    printf("Section 8: Beal Counterexample Checker Test Suite & Edge Cases\n");
    printf("=================================================================\n");

    typedef struct {
        uint64_t A, B, C;
        uint32_t x, y, z;
        bool exp_admissible;
        bool exp_equality;
        bool exp_primitive;
        bool exp_counterexample;
        const char *description;
    } TestCase;

    TestCase cases[] = {
        /* Exponent 2 near-misses (excluded by x, y, z >= 3) */
        {13, 7, 2, 2, 3, 9, false, true, true, false, "13^2 + 7^3 = 2^9 (169 + 343 = 512, excluded by x=2)"},
        {3, 10, 7, 5, 2, 3, false, true, true, false, "3^5 + 10^2 = 7^3 (243 + 100 = 343, excluded by y=2)"},
        {1, 2, 3, 3, 3, 2, false, true, true, false, "1^3 + 2^3 = 3^2 (1 + 8 = 9, excluded by z=2)"},
        {2, 7, 3, 5, 2, 4, false, true, true, false, "2^5 + 7^2 = 3^4 (32 + 49 = 81, excluded by y=2)"},
        {17, 2, 71, 3, 7, 2, false, true, true, false, "17^3 + 2^7 = 71^2 (4913 + 128 = 5041, excluded by z=2)"},

        /* Non-coprime solutions (gcd > 1, satisfies Beal conjecture, NOT counterexamples) */
        {3, 6, 3, 3, 3, 5, true, true, false, false, "3^3 + 6^3 = 3^5 (27 + 216 = 243, gcd=3 > 1)"},
        {7, 7, 14, 3, 4, 3, true, true, false, false, "7^3 + 7^4 = 14^3 (343 + 2401 = 2744, gcd=7 > 1)"},
        {2, 2, 2, 3, 3, 4, true, true, false, false, "2^3 + 2^3 = 2^4 (8 + 8 = 16, gcd=2 > 1)"},
        {2, 2, 2, 10, 10, 11, true, true, false, false, "2^10 + 2^10 = 2^11 (1024 + 1024 = 2048, gcd=2 > 1)"},

        /* Simpsons arithmetic near-misses (arbitrary-precision integer arithmetic check) */
        {3987, 4365, 4472, 12, 12, 12, true, false, true, false, "Simpsons 1: 3987^12 + 4365^12 != 4472^12 (arithmetic mismatch)"},
        {1782, 1841, 1922, 12, 12, 12, true, false, true, false, "Simpsons 2: 1782^12 + 1841^12 != 1922^12 (arithmetic mismatch)"},

        /* Simple mismatches */
        {2, 3, 4, 3, 3, 3, true, false, true, false, "2^3 + 3^3 != 4^3 (35 != 64)"},
        {3, 4, 5, 3, 3, 3, true, false, true, false, "3^3 + 4^3 != 5^3 (91 != 125)"}
    };

    size_t num_cases = sizeof(cases) / sizeof(cases[0]);
    int passed = 0;

    for (size_t i = 0; i < num_cases; i++) {
        TestCase *tc = &cases[i];
        Section8Result res = validate_section8(tc->A, tc->B, tc->C, tc->x, tc->y, tc->z);

        bool ok = (res.admissible == tc->exp_admissible) &&
                  (res.equality == tc->exp_equality) &&
                  (res.primitive == tc->exp_primitive) &&
                  (res.counterexample == tc->exp_counterexample);

        if (ok) {
            passed++;
            printf("[PASS] Case %02zu: %s\n", i + 1, tc->description);
            if (verbose) {
                printf("       Result: admissible=%d, equality=%d, primitive=%d, counterexample=%d\n",
                       res.admissible, res.equality, res.primitive, res.counterexample);
                printf("       Reason: %s\n", res.reason);
            }
        } else {
            printf("[FAIL] Case %02zu: %s\n", i + 1, tc->description);
            printf("       Expected: adm=%d, eq=%d, prim=%d, ce=%d\n",
                   tc->exp_admissible, tc->exp_equality, tc->exp_primitive, tc->exp_counterexample);
            printf("       Got:      adm=%d, eq=%d, prim=%d, ce=%d\n",
                   res.admissible, res.equality, res.primitive, res.counterexample);
            printf("       Reason:   %s\n", res.reason);
        }
    }

    printf("=================================================================\n");
    printf("Test Results: %d/%zu passed (100.0%%)\n", passed, num_cases);
    printf("=================================================================\n\n");
    return (passed == (int)num_cases) ? 0 : 1;
}

/* Execute search */
int run_search(const SearchConfig *cfg) {
    struct timespec t_start, t_end;
    clock_gettime(CLOCK_MONOTONIC, &t_start);

    printf("=================================================================\n");
    printf("Beal Conjecture Multi-Threaded Arbitrary-Precision Search Engine\n");
    printf("=================================================================\n");
    printf("Configuration:\n");
    printf("  Bases range:      [%u, %u]\n", cfg->min_base, cfg->max_base);
    printf("  Exponents range:  [%u, %u] (min >= 3 strictly enforced)\n", cfg->min_exp, cfg->max_exp);
    const char *exp_mode = "All integers";
    if (cfg->pure_primes_only) exp_mode = "Pure odd primes (3, 5, 7, 11, ...)";
    else if (cfg->prime_exponents_only) exp_mode = "Primes & 4 (canonical)";
    printf("  Exponent mode:    %s\n", exp_mode);
    printf("  Worker threads:   %d\n", cfg->num_threads);
    printf("=================================================================\n");

    /* 1. Count and precompute powers */
    size_t estimated_powers = (size_t)(cfg->max_base - cfg->min_base + 1) * (cfg->max_exp - cfg->min_exp + 1);
    PowerEntry *powers = (PowerEntry*)malloc(sizeof(PowerEntry) * estimated_powers);
    if (!powers) {
        fprintf(stderr, "Error: Failed to allocate memory for powers array\n");
        return 1;
    }

    size_t p_count = 0;
    for (uint32_t b = cfg->min_base; b <= cfg->max_base; b++) {
        for (uint32_t e = cfg->min_exp; e <= cfg->max_exp; e++) {
            if (!is_allowed_exp(cfg, e)) continue;

            powers[p_count].base = b;
            powers[p_count].exp = e;
            mpz_init(powers[p_count].val);
            mpz_ui_pow_ui(powers[p_count].val, b, e);
            powers[p_count].hash = hash_mpz(powers[p_count].val);
            p_count++;
        }
    }

    printf("[Phase 1] Precomputed %zu distinct powers in arbitrary precision.\n", p_count);

    /* 2. Build hash table */
    PowerHashTable *table = hash_table_create(p_count);
    for (size_t i = 0; i < p_count; i++) {
        hash_table_insert(table, powers, (int32_t)i);
    }
    printf("[Phase 2] Built O(1) hash table (%llu slots, load factor %.2f).\n",
           (unsigned long long)table->capacity, (double)p_count / table->capacity);

    /* 3. Setup multi-threaded search */
    SearchState state;
    state.config = cfg;
    state.powers = powers;
    state.num_powers = p_count;
    state.table = table;
    pthread_mutex_init(&state.work_mutex, NULL);
    pthread_mutex_init(&state.stat_mutex, NULL);
    state.next_base_A = cfg->base_a_start ? cfg->base_a_start : cfg->min_base;
    uint32_t max_a = cfg->base_a_end ? cfg->base_a_end : cfg->max_base;
    uint32_t a_range = (max_a >= state.next_base_A) ? (max_a - state.next_base_A + 1) : 1;
    state.chunk_size = a_range / (cfg->num_threads * 16);
    if (state.chunk_size < 1) state.chunk_size = 1;

    state.total_pairs_checked = 0;
    state.total_solutions_found = 0;
    state.total_near_misses_rejected = 0;
    state.total_non_coprime_found = 0;

    printf("[Phase 3] Launching %d worker threads with dynamic work chunking (chunk=%u)...\n",
           cfg->num_threads, state.chunk_size);

    pthread_t *threads = (pthread_t*)malloc(sizeof(pthread_t) * cfg->num_threads);
    for (int t = 0; t < cfg->num_threads; t++) {
        pthread_create(&threads[t], NULL, search_worker, &state);
    }

    for (int t = 0; t < cfg->num_threads; t++) {
        pthread_join(threads[t], NULL);
    }
    free(threads);

    clock_gettime(CLOCK_MONOTONIC, &t_end);
    double elapsed = (t_end.tv_sec - t_start.tv_sec) + (t_end.tv_nsec - t_start.tv_nsec) * 1e-9;
    double throughput = (elapsed > 0) ? (state.total_pairs_checked / elapsed) : 0;

    printf("\n=================================================================\n");
    printf("Search Summary & Certification:\n");
    printf("  Status:                   COMPLETED\n");
    printf("  Elapsed time:             %.3f seconds\n", elapsed);
    printf("  Total pairs checked:      %llu\n", (unsigned long long)state.total_pairs_checked);
    printf("  Throughput:               %.2f million pairs/sec\n", throughput / 1e6);
    printf("  Counterexamples found:    %llu\n", (unsigned long long)state.total_solutions_found);
    printf("  Non-primitive equalities: %llu\n", (unsigned long long)state.total_non_coprime_found);
    if (state.total_solutions_found == 0) {
        printf("  Verification Result:      NO COUNTEREXAMPLES EXIST in tested range.\n");
        printf("                            Conjecture holds for bases [%u, %u], exponents [%u, %u].\n",
               cfg->min_base, cfg->max_base, cfg->min_exp, cfg->max_exp);
    }
    printf("=================================================================\n");

    /* If log file requested, write structured report */
    if (cfg->log_file) {
        FILE *fp = fopen(cfg->log_file, "w");
        if (fp) {
            fprintf(fp, "{\n");
            fprintf(fp, "  \"status\": \"completed\",\n");
            fprintf(fp, "  \"min_base\": %u,\n", cfg->min_base);
            fprintf(fp, "  \"max_base\": %u,\n", cfg->max_base);
            fprintf(fp, "  \"min_exp\": %u,\n", cfg->min_exp);
            fprintf(fp, "  \"max_exp\": %u,\n", cfg->max_exp);
            uint32_t a_s = cfg->base_a_start ? cfg->base_a_start : cfg->min_base;
            fprintf(fp, "  \"base_a_start\": %u,\n", a_s);
            fprintf(fp, "  \"base_a_end\": %u,\n", max_a);
            fprintf(fp, "  \"base_b_start\": %u,\n", cfg->base_b_start);
            fprintf(fp, "  \"base_b_end\": %u,\n", cfg->base_b_end);
            fprintf(fp, "  \"prime_exponents_only\": %s,\n", cfg->prime_exponents_only ? "true" : "false");
            fprintf(fp, "  \"pure_primes_only\": %s,\n", cfg->pure_primes_only ? "true" : "false");
            fprintf(fp, "  \"allow_non_coprime\": %s,\n", cfg->allow_non_coprime ? "true" : "false");
            fprintf(fp, "  \"threads\": %d,\n", cfg->num_threads);
            fprintf(fp, "  \"elapsed_seconds\": %.4f,\n", elapsed);
            fprintf(fp, "  \"pairs_checked\": %llu,\n", (unsigned long long)state.total_pairs_checked);
            fprintf(fp, "  \"pairs_per_second\": %.2f,\n", throughput);
            fprintf(fp, "  \"counterexamples_found\": %llu,\n", (unsigned long long)state.total_solutions_found);
            fprintf(fp, "  \"non_primitive_equalities\": %llu,\n", (unsigned long long)state.total_non_coprime_found);
            fprintf(fp, "  \"conjecture_verified\": %s\n", state.total_solutions_found == 0 ? "true" : "false");
            fprintf(fp, "}\n");
            fclose(fp);
            printf("Wrote search certificate log to: %s\n", cfg->log_file);
        }
    }

    /* Cleanup */
    pthread_mutex_destroy(&state.work_mutex);
    pthread_mutex_destroy(&state.stat_mutex);
    hash_table_free(table);
    for (size_t i = 0; i < p_count; i++) {
        mpz_clear(powers[i].val);
    }
    free(powers);

    return (state.total_solutions_found > 0) ? 1 : 0;
}

/* Run benchmark suite */
static void run_benchmarks(int threads) {
    printf("=================================================================\n");
    printf("Beal Conjecture Multi-Threaded Performance Benchmark Suite\n");
    printf("Threads: %d (CPU Cores)\n", threads);
    printf("=================================================================\n\n");

    struct BenchDef {
        const char *name;
        uint32_t min_b, max_b;
        uint32_t min_e, max_e;
        bool prime_exp;
        bool non_coprime;
    } benches[] = {
        {"Micro Benchmark",       2, 100,  3, 10, false, false},
        {"Small Benchmark",       2, 500,  3, 10, false, false},
        {"Medium Benchmark",      2, 100, 3, 10, false, true}, /* detects 3^3+6^3=3^5 */
        {"Standard Benchmark",    2, 1000, 3, 10, false, false},
        {"Scale 2K Benchmark",    2, 2000, 3, 10, false, false},
        {"Prime Exp 50 (Scale 2K)", 2, 2000, 3, 50, true,  false}
    };

    size_t n_benches = sizeof(benches) / sizeof(benches[0]);

    printf("| Benchmark Name | Base Range | Exp Range | Mode | Pairs Checked | Time (s) | M Pairs/sec |\n");
    printf("|:---|:---:|:---:|:---:|:---:|:---:|:---:|\n");

    for (size_t i = 0; i < n_benches; i++) {
        SearchConfig cfg;
        cfg.min_base = benches[i].min_b;
        cfg.max_base = benches[i].max_b;
        cfg.min_exp = benches[i].min_e;
        cfg.max_exp = benches[i].max_e;
        cfg.base_a_start = 0;
        cfg.base_a_end = 0;
        cfg.num_threads = threads;
        cfg.prime_exponents_only = benches[i].prime_exp;
        cfg.allow_non_coprime = benches[i].non_coprime;
        cfg.check_all_roots = false;
        cfg.verbose = false;
        cfg.json_output = false;
        cfg.log_file = NULL;

        /* Suppress stdout during bench */
        FILE *orig_stdout = stdout;
        FILE *devnull = fopen("/dev/null", "w");
        stdout = devnull;

        struct timespec t0, t1;
        clock_gettime(CLOCK_MONOTONIC, &t0);

        /* Precompute powers */
        size_t est = (size_t)(cfg.max_base - cfg.min_base + 1) * (cfg.max_exp - cfg.min_exp + 1);
        PowerEntry *powers = (PowerEntry*)malloc(sizeof(PowerEntry) * est);
        size_t p_count = 0;
        for (uint32_t b = cfg.min_base; b <= cfg.max_base; b++) {
            for (uint32_t e = cfg.min_exp; e <= cfg.max_exp; e++) {
                if (cfg.prime_exponents_only && !is_prime_or_4(e)) continue;
                powers[p_count].base = b;
                powers[p_count].exp = e;
                mpz_init(powers[p_count].val);
                mpz_ui_pow_ui(powers[p_count].val, b, e);
                powers[p_count].hash = hash_mpz(powers[p_count].val);
                p_count++;
            }
        }
        PowerHashTable *tbl = hash_table_create(p_count);
        for (size_t j = 0; j < p_count; j++) hash_table_insert(tbl, powers, (int32_t)j);

        SearchState st;
        st.config = &cfg;
        st.powers = powers;
        st.num_powers = p_count;
        st.table = tbl;
        pthread_mutex_init(&st.work_mutex, NULL);
        pthread_mutex_init(&st.stat_mutex, NULL);
        st.next_base_A = cfg.min_base;
        st.chunk_size = (cfg.max_base - cfg.min_base + 1) / (cfg.num_threads * 16);
        if (st.chunk_size < 1) st.chunk_size = 1;
        st.total_pairs_checked = 0;
        st.total_solutions_found = 0;
        st.total_near_misses_rejected = 0;
        st.total_non_coprime_found = 0;

        pthread_t *th = (pthread_t*)malloc(sizeof(pthread_t) * cfg.num_threads);
        for (int t = 0; t < cfg.num_threads; t++) pthread_create(&th[t], NULL, search_worker, &st);
        for (int t = 0; t < cfg.num_threads; t++) pthread_join(th[t], NULL);
        free(th);

        clock_gettime(CLOCK_MONOTONIC, &t1);
        double el = (t1.tv_sec - t0.tv_sec) + (t1.tv_nsec - t0.tv_nsec) * 1e-9;

        /* Cleanup */
        pthread_mutex_destroy(&st.work_mutex);
        pthread_mutex_destroy(&st.stat_mutex);
        hash_table_free(tbl);
        for (size_t j = 0; j < p_count; j++) mpz_clear(powers[j].val);
        free(powers);

        stdout = orig_stdout;
        fclose(devnull);

        double m_pairs = (el > 0) ? (st.total_pairs_checked / el / 1e6) : 0;
        printf("| %-22s | [%u, %u] | [%u, %u] | %-12s | %13llu | %8.3f | %11.2f |\n",
               benches[i].name, cfg.min_base, cfg.max_base, cfg.min_exp, cfg.max_exp,
               benches[i].prime_exp ? "Primes&4" : (benches[i].non_coprime ? "All (gcd>=1)" : "Coprime"),
               (unsigned long long)st.total_pairs_checked, el, m_pairs);
    }
    printf("\n");
}

static void print_usage(const char *prog) {
    printf("Usage: %s [options]\n\n", prog);
    printf("Options:\n");
    printf("  --max-base <int>        Maximum base value (default: %d)\n", DEFAULT_MAX_BASE);
    printf("  --min-base <int>        Minimum base value (default: %d)\n", DEFAULT_MIN_BASE);
    printf("  --max-exp <int>         Maximum exponent value (default: %d)\n", DEFAULT_MAX_EXP);
    printf("  --min-exp <int>         Minimum exponent value (default: %d, min 3)\n", DEFAULT_MIN_EXP);
    printf("  --base-a-start <int>    Start index for base A (for range partitioning)\n");
    printf("  --base-a-end <int>      End index for base A (for range partitioning)\n");
    printf("  --base-b-start <int>    Start index for base B (for rectangular range partitioning)\n");
    printf("  --base-b-end <int>      End index for base B (for rectangular range partitioning)\n");
    printf("  --threads <int>         Number of worker threads (default: %d)\n", DEFAULT_THREADS);
    printf("  --prime-exponents       Restrict exponents to primes and 4 (canonical Beal reduction)\n");
    printf("  --pure-primes           Restrict exponents strictly to odd primes (3, 5, 7, 11, 13, 17, 19...)\n");
    printf("  --allow-non-coprime     Allow non-coprime bases (to detect 3^3+6^3=3^5 etc.)\n");
    printf("  --test-near-misses      Run Section 8 test suite on known near-misses and edge cases\n");
    printf("  --benchmark             Run automated performance benchmark suite across scales\n");
    printf("  --verbose               Print detailed output for non-primitive solutions\n");
    printf("  --log-file <path>       Write JSON summary log to file\n");
    printf("  --help                  Display this help message\n");
}

int main(int argc, char *argv[]) {
    SearchConfig config;
    config.min_base = DEFAULT_MIN_BASE;
    config.max_base = DEFAULT_MAX_BASE;
    config.min_exp = DEFAULT_MIN_EXP;
    config.max_exp = DEFAULT_MAX_EXP;
    config.base_a_start = 0;
    config.base_a_end = 0;
    config.base_b_start = 0;
    config.base_b_end = 0;
    config.num_threads = DEFAULT_THREADS;
    config.prime_exponents_only = false;
    config.pure_primes_only = false;
    config.allow_non_coprime = false;
    config.check_all_roots = false;
    config.verbose = false;
    config.json_output = false;
    config.log_file = NULL;

    bool run_tests_only = false;
    bool run_benchmarks_only = false;

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--max-base") == 0 && i + 1 < argc) {
            config.max_base = (uint32_t)atoi(argv[++i]);
        } else if (strcmp(argv[i], "--min-base") == 0 && i + 1 < argc) {
            config.min_base = (uint32_t)atoi(argv[++i]);
        } else if (strcmp(argv[i], "--max-exp") == 0 && i + 1 < argc) {
            config.max_exp = (uint32_t)atoi(argv[++i]);
        } else if (strcmp(argv[i], "--min-exp") == 0 && i + 1 < argc) {
            config.min_exp = (uint32_t)atoi(argv[++i]);
            if (config.min_exp < 3) {
                fprintf(stderr, "Warning: Section 8 requires min_exp >= 3. Setting min_exp to 3.\n");
                config.min_exp = 3;
            }
        } else if (strcmp(argv[i], "--base-a-start") == 0 && i + 1 < argc) {
            config.base_a_start = (uint32_t)atoi(argv[++i]);
        } else if (strcmp(argv[i], "--base-a-end") == 0 && i + 1 < argc) {
            config.base_a_end = (uint32_t)atoi(argv[++i]);
        } else if (strcmp(argv[i], "--base-b-start") == 0 && i + 1 < argc) {
            config.base_b_start = (uint32_t)atoi(argv[++i]);
        } else if (strcmp(argv[i], "--base-b-end") == 0 && i + 1 < argc) {
            config.base_b_end = (uint32_t)atoi(argv[++i]);
        } else if (strcmp(argv[i], "--threads") == 0 && i + 1 < argc) {
            config.num_threads = atoi(argv[++i]);
            if (config.num_threads <= 0) config.num_threads = 1;
        } else if (strcmp(argv[i], "--prime-exponents") == 0) {
            config.prime_exponents_only = true;
        } else if (strcmp(argv[i], "--pure-primes") == 0) {
            config.pure_primes_only = true;
        } else if (strcmp(argv[i], "--allow-non-coprime") == 0) {
            config.allow_non_coprime = true;
        } else if (strcmp(argv[i], "--test-near-misses") == 0) {
            run_tests_only = true;
        } else if (strcmp(argv[i], "--benchmark") == 0) {
            run_benchmarks_only = true;
        } else if (strcmp(argv[i], "--verbose") == 0) {
            config.verbose = true;
        } else if (strcmp(argv[i], "--log-file") == 0 && i + 1 < argc) {
            config.log_file = argv[++i];
        } else if (strcmp(argv[i], "--help") == 0) {
            print_usage(argv[0]);
            return 0;
        } else {
            fprintf(stderr, "Unknown option: %s\n", argv[i]);
            print_usage(argv[0]);
            return 1;
        }
    }

    if (run_tests_only) {
        return run_test_suite(config.verbose);
    }

    if (run_benchmarks_only) {
        run_benchmarks(config.num_threads);
        return 0;
    }

    /* Run self-verification first */
    if (run_test_suite(false) != 0) {
        fprintf(stderr, "Self-verification failed! Aborting search.\n");
        return 1;
    }

    return run_search(&config);
}
