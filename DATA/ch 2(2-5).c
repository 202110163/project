/*
프로그램 :  성을 입력하여 출력하는 프로그램
실습일: 2024.3.31
실습자 : 202110163 김민성
*/

#include <stdio.h>
#include <string.h>

int main() {
    char name1[5] = "park";
    char name2[5];
    char name3[4][20] = {"park", "lee", "kim", "han"}; // 문자열 초기화
    int i;

    strcpy(name2, name1);
    printf("name2 is %s\n", name2);
    if (strcmp(name1, name2) == 0)
        printf("name1 and name2 are equal.\n");

    strcpy(name2, "kim");
    if (strcmp(name1, name2) > 0)
        printf("name1 > name2\n");
    else if (strcmp(name1, name2) < 0)
        printf("name1 < name2\n");
    else
        printf("name1 == name2\n");

    for (i = 0; i < 4; i++) {
        printf("Please enter a name >> ");
        scanf("%s", name3[i]);
    }

    for (i = 0; i < 4; i++)
        printf("%s\t", name3[i]);

    return 0;
}