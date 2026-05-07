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

// XOR sign bit to convert signed to unsigned range
static inline __m512i xor_sign(__m512i v) {
    return _mm512_xor_si512(v, _mm512_set1_epi32(0x80000000));
}

int main() {
    printf("=== DUAL-PATH OVERFLOW FIX BENCHMARK ===\n\n");
    
    int32_t* v = aligned_alloc(64, N*4);
    int32_t* lo = aligned_alloc(64, N*4);
    int32_t* hi = aligned_alloc(64, N*4);
    
    // Include extreme values that trigger overflow
    srand(42);
    for (int i = 0; i < N; i++) {
        int r = rand() % 100;
        if (r < 5) {
            // 5% extreme values near INT_MIN/INT_MAX
            lo[i] = -2147483647 + rand()%100;
            hi[i] = 2147483647 - rand()%100;
        } else if (r < 20) {
            // 15% negative ranges
            lo[i] = -(rand()%10000);
            hi[i] = lo[i] + rand()%5000 + 1;
        } else {
            // 80% normal ranges
            lo[i] = rand()%2000 - 1000;
            hi[i] = lo[i] + rand()%500 + 1;
        }
        v[i] = lo[i] + rand()%(hi[i]-lo[i]+1);
    }
    
    volatile int sink = 0;
    
    // ORIGINAL dual-path (broken at extreme values)
    uint64_t t0 = rdtsc();
    // count disagreements
    for (int i = 0; i <= N-16; i += 16) {
        __m512i vv = _mm512_loadu_si512((void*)(v+i));
        __m512i ll = _mm512_loadu_si512((void*)(lo+i));
        __m512i hh = _mm512_loadu_si512((void*)(hi+i));
        __mmask16 ka = _mm512_cmpge_epi32_mask(vv, ll) & _mm512_cmple_epi32_mask(vv, hh);
        __m512i above = _mm512_sub_epi32(vv, ll);
        __m512i below = _mm512_sub_epi32(hh, vv);
        __mmask16 kb = ~(_mm512_cmplt_epi32_mask(above, _mm512_set1_epi32(0)) |
                         _mm512_cmplt_epi32_mask(below, _mm512_set1_epi32(0)));
        sink += __builtin_popcount(ka & kb);
    }
    uint64_t t_broken = rdtsc() - t0;
    
    // FIXED dual-path (XOR-based, overflow-safe)
    t0 = rdtsc();
    for (int i = 0; i <= N-16; i += 16) {
        __m512i vv = _mm512_loadu_si512((void*)(v+i));
        __m512i ll = _mm512_loadu_si512((void*)(lo+i));
        __m512i hh = _mm512_loadu_si512((void*)(hi+i));
        // Path A: comparison
        __mmask16 ka = _mm512_cmpge_epi32_mask(vv, ll) & _mm512_cmple_epi32_mask(vv, hh);
        // Path B: XOR sign bit, then unsigned comparison
        __m512i vu = xor_sign(vv);
        __m512i lu = xor_sign(ll);
        __m512i hu = xor_sign(hh);
        __mmask16 kb = _mm512_cmpge_epu32_mask(vu, lu) & _mm512_cmple_epu32_mask(vu, hu);
        sink += __builtin_popcount(ka & kb);
    }
    uint64_t t_fixed = rdtsc() - t0;
    
    // Verify: both paths should always agree with the fixed version
    int mismatches = 0;
    for (int i = 0; i < N; i++) {
        int pa = (v[i] >= lo[i] && v[i] <= hi[i]);
        uint32_t vu = (uint32_t)v[i] ^ 0x80000000;
        uint32_t lu = (uint32_t)lo[i] ^ 0x80000000;
        uint32_t hu = (uint32_t)hi[i] ^ 0x80000000;
        int pb = (vu >= lu && vu <= hu);
        if (pa != pb) mismatches++;
    }
    
    printf("%-25s %12s %12s\n", "Method", "Cycles", "cyc/constr");
    printf("===============================================\n");
    printf("%-25s %12lu %12.4f\n", "Subtraction dual (broken)", t_broken, (double)t_broken/N);
    printf("%-25s %12lu %12.4f\n", "XOR dual (fixed)", t_fixed, (double)t_fixed/N);
    printf("\nCost of fix: %.2fx\n", (double)t_fixed/t_broken);
    printf("Differential: %d mismatches / %d (XOR vs comparison)\n", mismatches, N);
    printf("(void)sink=%d\n", sink);
    
    free(v); free(lo); free(hi);
    return 0;
}
