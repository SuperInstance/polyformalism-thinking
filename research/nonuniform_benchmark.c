#include <immintrin.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

static inline uint64_t rdtsc() {
    unsigned int lo, hi;
    __asm__ __volatile__ ("rdtsc" : "=a"(lo), "=d"(hi));
    return ((uint64_t)hi << 32) | lo;
}

#define N 10000000

int main() {
    printf("=== NON-UNIFORM THRESHOLD BENCHMARK ===\n");
    printf("Each constraint has DIFFERENT lower/upper bounds (realistic)\n\n");
    
    // INT8: each constraint has different (lo, hi) pair
    int8_t* v8  = aligned_alloc(64, N);
    int8_t* lo8 = aligned_alloc(64, N);
    int8_t* hi8 = aligned_alloc(64, N);
    int32_t* v32 = aligned_alloc(64, N*4);
    int32_t* lo32= aligned_alloc(64, N*4);
    int32_t* hi32= aligned_alloc(64, N*4);
    
    srand(42);
    for (int i = 0; i < N; i++) {
        int lo = rand()%150 - 75;
        int hi = lo + rand()%30 + 1;
        int v = lo + rand()%(hi-lo+1);
        v8[i]=(int8_t)v; lo8[i]=(int8_t)lo; hi8[i]=(int8_t)hi;
        v32[i]=v; lo32[i]=lo; hi32[i]=hi;
    }
    
    volatile int sink = 0;
    
    // Baseline: INT32 with non-uniform bounds
    uint64_t t0 = rdtsc();
    for (int i = 0; i <= N-16; i += 16) {
        __m512i vv = _mm512_loadu_si512((void*)(v32+i));
        __m512i ll = _mm512_loadu_si512((void*)(lo32+i));
        __m512i hh = _mm512_loadu_si512((void*)(hi32+i));
        __mmask16 k = _mm512_cmpge_epi32_mask(vv, ll) & _mm512_cmple_epi32_mask(vv, hh);
        sink += __builtin_popcount(k);
    }
    uint64_t t32 = rdtsc() - t0;
    
    // INT8 with non-uniform bounds (THE KEY TEST)
    // Each lane has its own (lo, hi) — this IS the real-world case
    t0 = rdtsc();
    for (int i = 0; i <= N-64; i += 64) {
        __m512i vv = _mm512_loadu_si512((void*)(v8+i));
        __m512i ll = _mm512_loadu_si512((void*)(lo8+i));
        __m512i hh = _mm512_loadu_si512((void*)(hi8+i));
        __mmask64 k = _mm512_cmpge_epi8_mask(vv, ll) & _mm512_cmple_epi8_mask(vv, hh);
        sink += __builtin_popcountll(k);
    }
    uint64_t t8 = rdtsc() - t0;
    
    printf("%-15s %12s %12s %12s\n", "Mode", "Cycles", "cyc/constr", "Speedup");
    printf("===============================================\n");
    printf("%-15s %12lu %12.4f %12s\n", "INT32 non-uniform", t32, (double)t32/N, "1.00x");
    printf("%-15s %12lu %12.4f %12.2fx\n", "INT8 non-uniform", t8, (double)t8/N, (double)t32/t8);
    
    // Differential
    int mismatches = 0;
    for (int i = 0; i < N; i++) {
        int ref = (v32[i] >= lo32[i] && v32[i] <= hi32[i]);
        int i8r = (v8[i] >= lo8[i] && v8[i] <= hi8[i]);
        if (ref != i8r) mismatches++;
    }
    printf("\nNon-uniform threshold mismatches: %d / %d (%.4f%%)\n", 
        mismatches, N, 100.0*mismatches/N);
    printf("NOTE: All values in [-75, 80] range → INT8 safe\n");
    printf("(void)sink=%d\n", sink);
    
    free(v8); free(lo8); free(hi8); free(v32); free(lo32); free(hi32);
    return 0;
}
