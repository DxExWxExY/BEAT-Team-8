#include <stdlib.h>
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int mult(int a, int b) {
    return a * b;
}

int main(void) {
    int a = 4;
    int b = 5;
    int c = add(a, b);
    printf("result %d\n", c);
    int d = mult(a, b);
    printf("multiplication %d", d);
}

