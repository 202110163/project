/*
프로그램 : 랜덤값을 입력받아 오른쪽 정렬 프로그램
실습일: 2024.3.31
실습자 : 202110163 김민성
*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
	int score[5][100];
	int i, j;
	srand(time(NULL));
	
	for(i=0;i<5;i++){
		for(j=0;j<100;j++){		
			score[i][j] = rand()%101;
		}
	}
	for(i=0;i<5;i++){
		for(j=0;j<5;j++){		
			printf("%5d	",score[i][j]);
		printf("\n");
		}
	}
return 0;
}

