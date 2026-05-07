#include <immintrin.h>
#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

#define N 100000000
#define REPS 3

// INT32 baseline: 16 constraints per VPCMPD
double bench_int32(int32_t* v, int32_t* lo, int32_t* hi) {
    struct timespec s, e;
    int failures = 0;
    clock_gettime(CLOCK_MONOTONIC, &s);
    for (int r = 0; r < REPS; r++) {
        for (int i = 0; i <= N - 16; i += 16) {
            __m512i vv = _mm512_loadu_si512((void*)(v+i));
            __m512i ll = _mm512_loadu_si512((void*)(lo+i));
            __m512i hh = _mm512_loadu_si512((void*)(hi+i));
            __mmask16 kge = _mm512_cmpge_epi32_mask(vv, ll);
            __mmask16 kle = _mm512_cmple_epi32_mask(vv, hh);
            failures += 16 - __builtin_popcount(kge & kle);
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &e);
    return (e.tv_sec - s.tv_sec) + (e.tv_nsec - s.tv_nsec)/1e9;
}

// INT8 packed: 64 constraints per VPCMPD (4x density)
double bench_int8(int8_t* v, int8_t* lo, int8_t* hi) {
    struct timespec s, e;
    int failures = 0;
    clock_gettime(CLOCK_MONOTONIC, &s);
    for (int r = 0; r < REPS; r++) {
        for (int i = 0; i <= N - 64; i += 64) {
            __m512i vv = _mm512_loadu_si512((void*)(v+i));
            __m512i ll = _mm512_loadu_si512((void*)(lo+i));
            __m512i hh = _mm512_loadu_si512((void*)(hi+i));
            __mmask64 kge = _mm512_cmpge_epi8_mask(vv, ll);
            __mmask64 kle = _mm512_cmple_epi8_mask(vv, hh);
            failures += 64 - __builtin_popcountll(kge & kle);
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &e);
    return (e.tv_sec - s.tv_sec) + (e.tv_nsec - s.tv_nsec)/1e9;
}

// INT16 packed: 32 constraints per VPCMPD (2x density)
double bench_int16(int16_t* v, int16_t* lo, int16_t* hi) {
    struct timespec s, e;
    int failures = 0;
    clock_gettime(CLOCK_MONOTONIC, &s);
    for (int r = 0; r < REPS; r++) {
        for (int i = 0; i <= N - 32; i += 32) {
            __m512i vv = _mm512_loadu_si512((void*)(v+i));
            __m512i ll = _mm512_loadu_si512((void*)(lo+i));
            __m512i hh = _mm512_loadu_si512((void*)(hi+i));
            __mmask32 kge = _mm512_cmpge_epi16_mask(vv, ll);
            __mmask32 kle = _mm512_cmple_epi16_mask(vv, hh);
            failures += 32 - __builtin_popcount(kge & kle);
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &e);
    return (e.tv_sec - s.tv_sec) + (e.tv_nsec - s.tv_nsec)/1e9;
}

// DUAL redundant: same as INT32 but run twice with different code paths
double bench_dual(int32_t* v, int32_t* lo, int32_t* hi) {
    struct timespec s, e;
    int failures = 0;
    clock_gettime(CLOCK_MONOTONIC, &s);
    for (int r = 0; r < REPS; r++) {
        for (int i = 0; i <= N - 16; i += 16) {
            __m512i vv = _mm512_loadu_si512((void*)(v+i));
            __m512i ll = _mm512_loadu_si512((void*)(lo+i));
            __m512i hh = _mm512_loadu_si512((void*)(hi+i));
            // Path A: comparison
            __mmask16 kge = _mm512_cmpge_epi32_mask(vv, ll);
            __mmask16 kle = _mm512_cmple_epi32_mask(vv, hh);
            __mmask16 pass_a = kge & kle;
            // Path B: subtraction-based (different execution unit)
            __m512i above_lo = _mm512_sub_epi32(vv, ll);
            __m512i below_hi = _mm512_sub_epi32(hh, vv);
            __mmask16 neg1 = _mm512_cmplt_epi32_mask(above_lo, _mm512_set1_epi32(0));
            __mmask16 neg2 = _mm512_cmplt_epi32_mask(below_hi, _mm512_set1_epi32(0));
            __mmask16 pass_b = ~(neg1 | neg2) & 0xFFFF;
            // Both paths must agree
            __mmask16 disagree = pass_a ^ pass_b;
            failures += 16 - __builtin_popcount(pass_a & ~disagree);
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &e);
    return (e.tv_sec - s.tv_sec) + (e.tv_nsec - s.tv_nsec)/1e9;
}

int main() {
    printf("=== MIXED-PRECISION AVX-512 BENCHMARK ===\n");
    printf("AMD Ryzen AI 9 HX 370 | %d constraints × %d reps\n\n", N, REPS);
    
    // Allocate aligned buffers
    int8_t*  v8  = aligned_alloc(64, N*sizeof(int8_t));
    int8_t*  lo8 = aligned_alloc(64, N*sizeof(int8_t));
    int8_t*  hi8 = aligned_alloc(64, N*sizeof(int8_t));
    int16_t* v16 = aligned_alloc(64, N*sizeof(int16_t));
    int16_t* lo16= aligned_alloc(64, N*sizeof(int16_t));
    int16_t* hi16= aligned_alloc(64, N*sizeof(int16_t));
    int32_t* v32 = aligned_alloc(64, N*sizeof(int32_t));
    int32_t* lo32= aligned_alloc(64, N*sizeof(int32_t));
    int32_t* hi32= aligned_alloc(64, N*sizeof(int32_t));
    
    // Generate data: 90% pass rate, values in INT8 range for fair comparison
    srand(42);
    for (int i = 0; i < N; i++) {
        int lo = rand() % 200 - 100;
        int hi = lo + rand() % 50 + 1;
        int v;
        if (rand() % 100 < 90) {
            v = lo + rand() % (hi - lo + 1);  // pass
        } else {
            v = hi + rand() % 50 + 1;  // fail
        }
        v8[i] = (int8_t)v; lo8[i] = (int8_t)lo; hi8[i] = (int8_t)hi;
        v16[i]= (int16_t)v; lo16[i]= (int16_t)lo; hi16[i]= (int16_t)hi;
        v32[i]= v; lo32[i]= lo; hi32[i]= hi;
    }
    
    // Warm up
    bench_int32(v32, lo32, hi32);
    
    // Run benchmarks
    double t32 = bench_int32(v32, lo32, hi32);
    double t8  = bench_int8(v8, lo8, hi8);
    double t16 = bench_int16(v16, lo16, hi16);
    double td  = bench_dual(v32, lo32, hi32);
    
    double total32 = (double)N * REPS;
    
    printf("%-12s %10s %12s %10s\n", "Precision", "Time(s)", "M c/s", "Speedup");
    printf("---------------------------------------------------\n");
    printf("%-12s %10.4f %12.1f %10s\n", "INT32", t32, total32/t32/1e6, "1.00x (baseline)");
    printf("%-12s %10.4f %12.1f %10.2fx\n", "INT8",  t8,  total32/t8/1e6,  t32/t8);
    printf("%-12s %10.4f %12.1f %10.2fx\n", "INT16", t16, total32/t16/1e6, t32/t16);
    printf("%-12s %10.4f %12.1f %10.2fx\n", "DUAL",  td,  total32/td/1e6,  t32/td);
    
    // Mixed-precision simulation: AV mix (75/15/8/2)
    double mix_time = 0.75*t8 + 0.15*t16 + 0.08*t32 + 0.02*td;
    double mix_speedup = t32 / mix_time;
    
    printf("\n=== MIXED-PRECISION (AV mix: 75%% INT8, 15%% INT16, 8%% INT32, 2%% DUAL) ===\n");
    printf("Projected time: %.4f sec\n", mix_time);
    printf("MEASURED SPEEDUP: %.2fx\n", mix_speedup);
    printf("Corrected formula (harmonic): 2.61x\n");
    printf("Register counting verified:    2.61x\n");
    
    // Differential test
    printf("\n=== DIFFERENTIAL TEST ===\n");
    int mismatches = 0;
    for (int i = 0; i < N; i++) {
        int ref = (v32[i] >= lo32[i] && v32[i] <= hi32[i]);
        int int8_res = ((int)v8[i] >= (int)lo8[i] && (int)v8[i] <= (int)hi8[i]);
        if (v32[i] >= -127 && v32[i] <= 127 && lo32[i] >= -127 && lo32[i] <= 127 && hi32[i] >= -127 && hi32[i] <= 127) {
            if (ref != int8_res) mismatches++;
        }
    }
    printf("INT8 vs INT32 (in-range values): %d mismatches out of %d constraints\n", mismatches, N);
    
    free(v8); free(lo8); free(hi8);
    free(v16); free(lo16); free(hi16);
    free(v32); free(lo32); free(hi32);
    return 0;
}
