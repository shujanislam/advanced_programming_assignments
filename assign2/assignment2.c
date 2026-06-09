#include <stdio.h>

void constant_space() {
    int a = 1, b = 2, c = 3;
    (void)a; (void)b; (void)c;
}

void linear_space(int n) {
    int a[n];
    a[0] = 1;
}

void quadratic_space(int n) {
    int a[n][n];
    a[0][0] = 1;
}

int main() {
    int sizes[] = {10, 50, 100, 200, 300};
    int i;

    printf("n\tO(1) bytes\tO(n) bytes\tO(n^2) bytes\n");

    for (i = 0; i < 5; i++) {
        int n = sizes[i];

        constant_space();
        linear_space(n);
        quadratic_space(n);

        printf("%d\t%d\t\t%d\t\t%d\n",
               n,
               3 * (int)sizeof(int),
               n * (int)sizeof(int),
               n * n * (int)sizeof(int));
    }

    return 0;
}
