#include <immintrin.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

static inline uint64_t rdtsc() {
    unsigned int lo, hi;
    __asm__ __volatile__ ("rdtsc" : "=a"(lo), "=d"(hi));
    return ((uint64_t)hi << 32) | lo;
}

#define N 10000000  // 10M — fits in L3 but not L2

int main() {
    printf("=== CYCLE-ACCURATE AVX-512 THROUGHPUT ===\n");
    printf("%d constraints, cycle-accurate timing\n\n", N);
    
    int8_t*  v8  = aligned_alloc(64, N);
    int8_t*  lo8 = aligned_alloc(64, N);
    int8_t*  hi8 = aligned_alloc(64, N);
    int16_t* v16 = aligned_alloc(64, N*2);
    int16_t* lo16= aligned_alloc(64, N*2);
    int16_t* hi16= aligned_alloc(64, N*2);
    int32_t* v32 = aligned_alloc(64, N*4);
    int32_t* lo32= aligned_alloc(64, N*4);
    int32_t* hi32= aligned_alloc(64, N*4);
    
    srand(42);
    for (int i = 0; i < N; i++) {
        int lo = rand()%200 - 100;
        int hi = lo + rand()%50 + 1;
        int v = lo + rand()%(hi-lo+1);
        v8[i]=(int8_t)v; lo8[i]=(int8_t)lo; hi8[i]=(int8_t)hi;
        v16[i]=(int16_t)v; lo16[i]=(int16_t)lo; hi16[i]=(int16_t)hi;
        v32[i]=v; lo32[i]=lo; hi32[i]=hi;
    }
    
    volatile int sink = 0;
    
    // INT32: 16 per register
    uint64_t t0 = rdtsc();
    for (int i = 0; i <= N-16; i += 16) {
        __m512i vv = _mm512_loadu_si512((void*)(v32+i));
        __m512i ll = _mm512_loadu_si512((void*)(lo32+i));
        __m512i hh = _mm512_loadu_si512((void*)(hi32+i));
        __mmask16 kge = _mm512_cmpge_epi32_mask(vv, ll);
        __mmask16 kle = _mm512_cmple_epi32_mask(vv, hh);
        sink += __builtin_popcount(kge & kle);
    }
    uint64_t t32 = rdtsc() - t0;
    
    // INT8: 64 per register
    t0 = rdtsc();
    for (int i = 0; i <= N-64; i += 64) {
        __m512i vv = _mm512_loadu_si512((void*)(v8+i));
        __m512i ll = _mm512_loadu_si512((void*)(lo8+i));
        __m512i hh = _mm512_loadu_si512((void*)(hi8+i));
        __mmask64 kge = _mm512_cmpge_epi8_mask(vv, ll);
        __mmask64 kle = _mm512_cmple_epi8_mask(vv, hh);
        sink += __builtin_popcountll(kge & kle);
    }
    uint64_t t8 = rdtsc() - t0;
    
    // INT16: 32 per register
    t0 = rdtsc();
    for (int i = 0; i <= N-32; i += 32) {
        __m512i vv = _mm512_loadu_si512((void*)(v16+i));
        __m512i ll = _mm512_loadu_si512((void*)(lo16+i));
        __m512i hh = _mm512_loadu_si512((void*)(hi16+i));
        __mmask32 kge = _mm512_cmpge_epi16_mask(vv, ll);
        __mmask32 kle = _mm512_cmple_epi16_mask(vv, hh);
        sink += __builtin_popcount(kge & kle);
    }
    uint64_t t16 = rdtsc() - t0;
    
    // DUAL: INT32 run twice
    t0 = rdtsc();
    for (int i = 0; i <= N-16; i += 16) {
        __m512i vv = _mm512_loadu_si512((void*)(v32+i));
        __m512i ll = _mm512_loadu_si512((void*)(lo32+i));
        __m512i hh = _mm512_loadu_si512((void*)(hi32+i));
        __mmask16 kge = _mm512_cmpge_epi32_mask(vv, ll);
        __mmask16 kle = _mm512_cmple_epi32_mask(vv, hh);
        __mmask16 pass_a = kge & kle;
        __m512i above = _mm512_sub_epi32(vv, ll);
        __m512i below = _mm512_sub_epi32(hh, vv);
        __mmask16 neg1 = _mm512_cmplt_epi32_mask(above, _mm512_set1_epi32(0));
        __mmask16 neg2 = _mm512_cmplt_epi32_mask(below, _mm512_set1_epi32(0));
        __mmask16 pass_b = ~(neg1|neg2) & 0xFFFF;
        sink += __builtin_popcount(pass_a & pass_b);
    }
    uint64_t td = rdtsc() - t0;
    
    printf("%-10s %12s %12s %12s %10s\n", "Precision", "Cycles", "Cycles/constr", "Constr/cycle", "Speedup");
    printf("-----------------------------------------------------------------------\n");
    
    int n32 = (N/16)*16, n8 = (N/64)*64, n16 = (N/32)*32;
    
    printf("%-10s %12lu %12.2f %12.1f %10s\n", 
        "INT32", t32, (double)t32/n32, (double)n32/t32, "1.00x");
    printf("%-10s %12lu %12.2f %12.1f %10.2fx\n", 
        "INT8",  t8,  (double)t8/n8,   (double)n8/t8,  (double)t32/t8);
    printf("%-10s %12lu %12.2f %12.1f %10.2fx\n", 
        "INT16", t16, (double)t16/n16, (double)n16/t16, (double)t32/t16);
    printf("%-10s %12lu %12.2f %12.1f %10.2fx\n", 
        "DUAL",  td,  (double)td/n32,  (double)n32/td,  (double)t32/td);
    
    // Mixed precision: weighted by time
    double mix_cycles = 0.75*(double)t8 + 0.15*(double)t16 + 0.08*(double)t32 + 0.02*(double)td;
    double mix_speedup = (double)t32 / mix_cycles;
    
    printf("\n=== MIXED PRECISION (AV mix) ===\n");
    printf("Weighted cycles: %.0f (vs %lu INT32 baseline)\n", mix_cycles, t32);
    printf("MEASURED SPEEDUP: %.2fx\n", mix_speedup);
    printf("(void)sink=%d\n", sink);
    
    free(v8); free(lo8); free(hi8);
    free(v16); free(lo16); free(hi16);
    free(v32); free(lo32); free(hi32);
    return 0;
}
