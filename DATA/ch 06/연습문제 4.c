#include <stdio.h>

// swap 함수 정의
void swap(int *px, int *py) {
    int temp = *px;  // *px의 값을 temp에 저장
    *px = *py;       // *py의 값을 *px에 저장
    *py = temp;      // temp의 값을 *py에 저장
}

int main() {
    int x = 3;  // x 변수 초기화
    int y = 5;  // y 변수 초기화

    // swap 호출 전 출력
    printf("x:%d\n", x);
    printf("y:%d\n", y);

    // swap 함수 호출
    swap(&x, &y);

    // swap 호출 후 출력
    printf("swap() 호출 후\n");
    printf("x:%d\n", x);
    printf("y:%d\n", y);

    return 0;
}
