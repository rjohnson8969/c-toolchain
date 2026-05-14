#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    printf("C Test 1\n");

    if (argc < 3) {
        printf("Usage: %s <a> <b>\n", argv[0]);
        return 1;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int sum = a + b;

    printf("%d + %d = %d\n", a, b, sum);

    return 0;
}