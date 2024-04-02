#include <stdio.h>

typedef struct {
    double real;
    double imag;
} Complex;

Complex add_complex(Complex a, Complex b){
    Complex result;
    result.real = a.real + b.real;
    result.imag = a.imag + b.imag;
    return result;
}

int main(){
    Complex a = {1.6, 2.0};//3.6
    Complex b = {3.2, 4.5};//7.7
    Complex sum = add_complex(a, b);
    printf("Sum: %.lf + %.lf\n", sum.real, sum.imag);
    printf("result: %lf",);
    return 0;
}