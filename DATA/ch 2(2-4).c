/*
프로그램 : 이름을 입력해 주소길이 출력
실습일: 2024.3.31
실습자 : 202110163 김민성
*/

#include<stdio.h>
#include<string.h>
int main(){
	char name[20];
	char addr[20]; 
	char st_cat[40]="";


	printf("please, enter your name");
	scanf("%d",name);
	printf("your name is %s \n",name);
	getchar();

	printf("please, enter your addrss >> ");
	gets(addr);
	printf("your addrss is \n",addr);

	strcat(st_cat,name);
	strcat(st_cat," 's address is");
	strcat(st_cat,addr);

	printf("%s",st_cat);
	printf("string length is %d \n",strlen(st_cat));
return 0;
}

