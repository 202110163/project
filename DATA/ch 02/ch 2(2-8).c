/*
프로그램 : 전체 다항식 프로그램
실습일: 2024.3.31
실습자 : 202110163 김민성
*/

#include <stdio.h>
#define MAX_DEGREE 101 // 다항식의 최고 차수 + 1
typedef struct {
	int degree;
	float coef[MAX_DEGREE];
} Polynomial;

void print_poly(Polynomial p, char str[]);
void print_poly2(Polynomial p, char str[]);
Polynomial read_poly();
Polynomial add_poly(Polynomial a, Polynomial b);

int main() {
	Polynomial a, b, c;
	a = read_poly();
	b = read_poly();
	c = add_poly(a, b);
	print_poly(a, " A = ");
	print_poly(b, " B = ");
	print_poly(c, "A+B= ");
	print_poly(c, "A-B= ");

	return 0;
}

void print_poly(Polynomial p, char str[])
{
	int i;
	printf("\t%s", str);
	for (i = 0; i < p.degree; i++)
		printf("%5.1f x^%d + ", p.coef[i], p.degree - i);
	printf("%4.1f\n", p.coef[p.degree]);
}
Polynomial read_poly() {
	int i;
	Polynomial p;
	printf("다항식의 최고 차수를 입력하시오: ");
	scanf("%d", &p.degree);
	printf("각 항의 계수를 입력하시오 (총 %d개): ", p.degree + 1);
	for (i = 0; i <= p.degree; i++)
		scanf("%f", p.coef + i);
	return p;
}
Polynomial add_poly(Polynomial a, Polynomial b)
{
	int i;
	Polynomial p;
	if (a.degree > b.degree) {
		p = a;
		for (i = 0; i <= b.degree; i++)
			p.coef[i + (p.degree - b.degree)] += b.coef[i];
	}
	else {
		p = b;
		for (i = 0; i <= a.degree; i++)
			p.coef[i + (p.degree - a.degree)] += a.coef[i];
	}
	return p;
}


void print_poly2(Polynomial p, char str[]) {
	int i;
	printf("\t%s", str);
	for (i = 0; i < p.degree; i++) {
		if (i == 0)
			printf("%5.1f x^%d", p.coef[i], p.degree - i);
		else if (p.coef[i] >= 0)
			printf("+ %5.1f x^%d", p.coef[i], p.degree - i);
		else
			printf("- %5.1f x^%d", -p.coef[i], p.degree - i);

	}

	if (p.coef[p.degree] >= 0)
		printf("+ %4.1\n", p.coef[p.degree]);
	else
		printf("- %4.1\n", -p.coef[p.degree]);
}

