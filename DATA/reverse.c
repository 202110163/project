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

void init_stak() { top = -1; }
int is_empty() { return top == -1; }
int is_full() { return top == MAX_STACK_SIZE - 1; }
int size() { return top + 1; }

void push(Element e) {
    if (is_full == 1) error("스택 포화 에러");
    data[++top] = e;
}

Element pop() {
    if (is_empty == 1) error("스택 공백 에러");
    return data[top--];
}

Element peek() {
    if (is_empty == 1) error("스택 공백 에러");
    return data[top];
}

int main()
{
    init_stak();
    char str[100];
    int count = 0;
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
        printf("%c", pop());
    }
    return 0;
}