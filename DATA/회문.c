#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define MAX_STACK_SIZE 100
typedef char Element;

Element data[MAX_STACK_SIZE];
int top;

void error(const char str[]) {
    printf("%s\n", str);
    exit(1);
}

void init_stak() { top = -1; } /*스택 초기화 top변수를 -1로 설정하여 스택이 비어있음*/
int is_empty() { return top == -1; } /*스택이 비어있는지 여부 판단 top변수가 -1이면 1로 아니면 0을 반환*/
int is_full() { return top == MAX_STACK_SIZE - 1; }/*스택이 가득 차 있는지 여부 판단 top변수가 MAX_STACK_SIZE -1 과 같으면 스택이 가득 찼으므로 1을 반환 아니면 0을 반환 */
int size() { return top + 1; }

void push(Element e)/* 스택에 데이터를 추가 스택이 가득 차 있는지 확인 후 데이터를 추가*/ {
    if (is_full()== 1) error("스택 포화 에러");
    data[++top] = e;
}

Element pop()/* 스택에 데이터를 제거 후 반환 스택이 비어있는지 확인 후 데이터를 제거하고 반환*/ {
    if (is_empty() == 1) error("스택 공백 에러");
    return data[top--];
}

Element peek()/* 스택의 맨 위에 있는 데이터를 반환하지만 제거하지 않음 스택이 비어있는지 확인 후 맨 위의 데이터를 반환*/ {
    if (is_empty() == 1) error("스택 공백 에러");
    return data[top];
}

int main()
{
    init_stak();/*함수 호출 후 스택 초기화*/
    char str[100];/*0 ~ 99 까지의 문자열을 입력*/
    int count = 0;/* 문자열의 길이를 계산 후 count 변수에 저장*/
    char tmp[100];
    printf("문자열을 입력해보세요 : ");
    scanf("%s", str);

    for (int i = 0; i < sizeof(str) / sizeof(char); i++) {
        if (str[i] == '\0')
            break;
        else 
            count++;
    }

    for (int i = 0; i < count; i++) {
        push(str[i]);
    }

    for (int i = 0; i < count; i++) {
        tmp[i] = pop();
    }

    for (int i = 0; i < count; i++){
        if (str[i]!=tmp[i]){
            printf("회문이 아닙니다.");
            exit(1);
        }
    }
    printf("회문입니다.");
    return 0;
}