#include <stdio.h>
#include <math.h>

int main() {
    int two[10];

    for (int i = 0; i < 10; i++) {
        two[i] = (int)pow(2, i);
        printf("%d ", two[i]);
    }

    return 0;
}