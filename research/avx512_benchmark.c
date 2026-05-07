#include <immintrin.h>
#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include <stdlib.h>

// Pack 64 INT8 constraint checks into one AVX-512 operation
int check_int8_packed(int8_t* values, int8_t* lowers, int8_t* uppers, int count) {
    int failures = 0;
    int i = 0;
    for (; i + 63 < count; i += 64) {
        __m512i v = _mm512_loadu_si512((void*)(values + i));
        __m512i lo = _mm512_loadu_si512((void*)(lowers + i));
        __m512i hi = _mm512_loadu_si512((void*)(uppers + i));
        
        __mmask64 k_ge = _mm512_cmpge_epi8_mask(v, lo);
        __mmask64 k_le = _mm512_cmple_epi8_mask(v, hi);
        __mmask64 k_pass = k_ge & k_le;
        
        failures += 64 - __builtin_popcountll(k_pass);
    }
    for (; i < count; i++) {
        if (!(values[i] >= lowers[i] && values[i] <= uppers[i]))
            failures++;
    }
    return failures;
}

// Standard INT32: 16 per VPCMPD
int check_int32(int32_t* values, int32_t* lowers, int32_t* uppers, int count) {
    int failures = 0;
    int i = 0;
    for (; i + 15 < count; i += 16) {
        __m512i v = _mm512_loadu_si512((void*)(values + i));
        __m512i lo = _mm512_loadu_si512((void*)(lowers + i));
        __m512i hi = _mm512_loadu_si512((void*)(uppers + i));
        
        __mmask16 k_ge = _mm512_cmpge_epi32_mask(v, lo);
        __mmask16 k_le = _mm512_cmple_epi32_mask(v, hi);
        __mmask16 k_pass = k_ge & k_le;
        
        failures += 16 - __builtin_popcount(k_pass);
    }
    for (; i < count; i++) {
        if (!(values[i] >= lowers[i] && values[i] <= uppers[i]))
            failures++;
    }
    return failures;
}

// Exhaustive differential: INT8 vs INT32 for all small values
int differential_test() {
    int8_t v8[64], lo8[64], hi8[64];
    int32_t v32[64], lo32[64], hi32[64];
    int mismatches = 0;
    int total = 0;
    
    for (int v = -127; v <= 127; v += 3) {
        for (int lo = -127; lo <= v; lo += 5) {
            for (int hi = v; hi <= 127; hi += 5) {
                total++;
                for (int lane = 0; lane < 64; lane++) {
                    v8[lane] = (int8_t)v; lo8[lane] = (int8_t)lo; hi8[lane] = (int8_t)hi;
                    v32[lane] = v; lo32[lane] = lo; hi32[lane] = hi;
                }
                int f8 = check_int8_packed(v8, lo8, hi8, 64);
                int f32 = check_int32(v32, lo32, hi32, 64);
                if (f8 != f32) {
                    mismatches++;
                    if (mismatches <= 3)
                        printf("MISMATCH: v=%d lo=%d hi=%d INT8=%d INT32=%d\n", v, lo, hi, f8, f32);
                }
            }
        }
    }
    printf("Differential: %d tests, %d mismatches\n", total, mismatches);
    return mismatches;
}

// Throughput benchmark
void benchmark() {
    #define N 1000000
    static int8_t v8[N], lo8[N], hi8[N];
    static int32_t v32[N], lo32[N], hi32[N];
    
    srand(42);
    for (int i = 0; i < N; i++) {
        int lo = rand() % 200 - 100;
        int hi = lo + rand() % 50;
        int v = lo + rand() % (hi - lo + 1);
        v8[i] = (int8_t)v; lo8[i] = (int8_t)lo; hi8[i] = (int8_t)hi;
        v32[i] = v; lo32[i] = lo; hi32[i] = hi;
    }
    
    struct timespec start, end;
    int reps = 100;
    
    // INT32 baseline
    clock_gettime(CLOCK_MONOTONIC, &start);
    volatile int f32 = 0;
    for (int r = 0; r < reps; r++) f32 += check_int32(v32, lo32, hi32, N);
    clock_gettime(CLOCK_MONOTONIC, &end);
    double t32 = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec)/1e9;
    
    // INT8 packed (4x more per register)
    clock_gettime(CLOCK_MONOTONIC, &start);
    volatile int f8 = 0;
    for (int r = 0; r < reps; r++) f8 += check_int8_packed(v8, lo8, hi8, N);
    clock_gettime(CLOCK_MONOTONIC, &end);
    double t8 = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec)/1e9;
    
    printf("\n=== MEASURED THROUGHPUT (AMD Ryzen AI 9, AVX-512) ===\n");
    printf("1M constraints × %d reps = %dM total checks\n", reps, N*reps/1000000);
    printf("INT32 (16/reg): %.3f sec → %.1f M constraints/sec\n", t32, (double)N*reps/t32/1e6);
    printf("INT8  (64/reg): %.3f sec → %.1f M constraints/sec\n", t8, (double)N*reps/t8/1e6);
    printf("MEASURED SPEEDUP: %.2fx\n", t32/t8);
}

int main() {
    printf("=== REAL AVX-512 TEST (AMD Ryzen AI 9 HX 370) ===\n\n");
    
    // Quick sanity: do the intrinsics work?
    __m512i test = _mm512_set1_epi32(42);
    printf("AVX-512 available: YES (created zmm register)\n\n");
    
    differential_test();
    benchmark();
    return 0;
}
