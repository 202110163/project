/*
다항식에 x값을 대입 계산하여 결과값 반환하는 함수
*/

#include <stdio.h>
#include <math.h>

#define MAX_DEGREE 101 // 다항식의 최고 차수 + 1

typedef struct {
    int degree;
    double coef[MAX_DEGREE];
} Polynomial;

void print_poly(Polynomial p, char str[]);
Polynomial read_poly();
Polynomial add_poly(Polynomial a, Polynomial b);
double Cal_poly(Polynomial p, double x);

int main() {
    Polynomial a, b, c;
    printf("다항식 A를 입력하세요:\n");
    a = read_poly();
    printf("다항식 B를 입력하세요:\n");
    b = read_poly();
    c = add_poly(a, b);
    print_poly(a, " 다항식 A = ");
    print_poly(b, " 다항식 B = ");
    print_poly(c, "A + B = ");
    
    double x;
    printf("다항식을 계산할 변수 x의 값을 입력하세요: ");
    scanf("%lf", &x);
    printf("다항식을 x = %.2f 에 대해 계산한 결과: %.2f\n", x, Cal_poly(c, x));
    
    return 0;
}

void print_poly(Polynomial p, char str[]) {
    printf("%s", str);
    int flag = 0;
    for (int i = p.degree; i >= 0; i--) {
        if (p.coef[i] != 0) {
            if (flag) {
                if (p.coef[i] > 0) {
                    printf(" + ");
                } else {
                    printf(" - ");
                }
            }
            flag = 1;
            printf("%.2fx^%d", p.coef[i], i);
        }
    }
    printf("\n");
}

Polynomial read_poly() {
    Polynomial p;
    printf("다항식의 최고 차수를 입력하세요: ");
    scanf("%d", &p.degree);
    printf("각 항의 계수를 입력하세요 (최고 차수부터 차수가 내림차순으로): ");
    for (int i = p.degree; i >= 0; i--) {
        scanf("%lf", &p.coef[i]);
    }
    return p;
}

Polynomial add_poly(Polynomial a, Polynomial b) {
    Polynomial c;
    c.degree = (a.degree > b.degree) ? a.degree : b.degree;
    for (int i = 0; i <= c.degree; i++) {
        c.coef[i] = ((i <= a.degree) ? a.coef[i] : 0) + ((i <= b.degree) ? b.coef[i] : 0);
    }
    return c;
}

double Cal_poly(Polynomial p, double x) {
    double result = 0;
    for (int i = p.degree; i >= 0; i--) {
        result += p.coef[i] * pow(x, i);
    }
    return result;
}
