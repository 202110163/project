/*
프로그램 : 구조체를 포함하는 구조체와 배열 프로그램
실습일: 2024.3.31
실습자 : 202110163 김민성
*/

typedef struct {
	int month;
	int date;
} Birthday;
typedef struct{
	char name[20];
	Birthday birthday;
} Friend;

int main(void){
	Friend a;
	Friend list[100];
	a.birthday.month = 7; 
	a.birthday.date = 17;
	list[0].birthday = a.birthday;
	strcpy(list[3].name,"mintoung");
return 0;
}
#include<stdio.h>

typedef struct {
	int month;
	int date;
} Birthday;
typedef struct{
	char name[20];
	Birthday birthday;
} Friend;

int main(void){
	Friend list[100];
	list[0].birthday.month = 7; 
	list[0].birthday.date = 17;
	strcpy(list[0].name,"mintoung");
	return 0;
}

