#include <stdio.h>
#include <time.h>

unsigned long long sink = 0;

void constant_time(int n) {
    sink += 1;
    sink += 2;
    sink += 3;
    sink += 4;
}

void linear_time(int n) {
    int i;
    for (i = 0; i < n; i++) {
        sink += i;
    }
}

void quadratic_time(int n) {
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            sink += i + j;
        }
    }
}

double measure(void (*func)(int), int n, int repeat) {
    clock_t start, end;
    int r;

    start = clock();
    for (r = 0; r < repeat; r++) {
        func(n);
    }
    end = clock();

    return (double)(end - start) / CLOCKS_PER_SEC;
}

int main() {
    int sizes[] = {100, 500, 1000, 2000, 4000};
    int i;
    int repeat = 100;

    printf("Input Size\tO(1)\t\tO(n)\t\tO(n^2)\n");

    for (i = 0; i < 5; i++) {
        int n = sizes[i];

        double t1 = measure(constant_time, n, repeat);
        double t2 = measure(linear_time, n, repeat);
        double t3 = measure(quadratic_time, n, repeat);

        printf("%d\t\t%f\t%f\t%f\n", n, t1, t2, t3);
    }

    return 0;
}
