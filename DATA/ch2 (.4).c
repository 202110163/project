/*
for 루프는 사용하여 배열의 값을 출력하는 프로그램
*/

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