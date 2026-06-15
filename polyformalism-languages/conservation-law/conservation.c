/* C: What hardware truth reveals about conservation
   Forces you to think about: Hardware. int is 32 bits. double is IEEE 754.
     sqrt() calls a hardware instruction. Mathematics is EXECUTED ON PHYSICAL HARDWARE.
   Broken assumption: That abstraction is free. C has no generics, no closures.
   Novel insight: The conservation law is a PHYSICAL PROCESS. When the CPU computes
     δ(n), electrons move through silicon. The computation has a COST — joules,
     nanoseconds. Every δ(n) costs energy, and the conservation law is about energy.

   Build: cc conservation.c -lm -o conservation && ./conservation
*/

#include <stdio.h>
#include <math.h>

double delta(int n) {
    return (1.0 / sqrt((double)n)) * (1.0 - 3.0 / (2.0 * n));
}

int main(void) {
    printf("%5s  %10s  %8s\n", "n", "δ(n)", "CCR%");
    printf("%.28s\n", "----------------------------");
    for (int n = 1; n <= 100; n++) {
        printf("%5d  %10.6f  %7.2f%%\n", n, delta(n), delta(n) * 100.0);
    }
    return 0;
}
