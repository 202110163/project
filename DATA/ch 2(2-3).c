/*
프로그램 : 랜덤으로 A,B를 포인터와 배열을 사용하여 출력하는 프로그램
실습일: 2024.3.31
실습자 : 202110163 김민성
*/

#include<stdio.h>
#include <stdlib.h>
int find_max_score(int *score[],int n);

int main(void){
	int A[5],B[5];
	int i, maxA, maxB;

	srand(time(NULL));


	for(i=0;i<5;i++){
		*(A+i) = rand();
		*(B+i) = rand();
	}
	maxA = find_max_score(A,5);
	maxB = find_max_score(B,5);

	if(maxA > maxB)
		printf("Array A");
	else if(maxA < maxB)
		printf("Array B");
	else 
		printf("Array A and Array B have same maximum number");	
	return 0;
}
int find_max_score(int *score[],int n){
	int i, tmp = *score[0];
	for(i=1;i<n;i++)
		if(*(score+i)>tmp)
			tmp = *(score+i);
	return tmp;
}

