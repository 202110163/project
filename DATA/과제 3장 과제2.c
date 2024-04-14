#include<stdio.h>
#include<stdlib.h>
#define MAX_STACK_SIZE 100
typedef int Element;

Element data[MAX_STACK_SIZE];
int top;

void error(char str[])
{
    printf("%s\n", str);
    exit(1);
}

void init_stack() {top = -1;}
int is_empty() {return top == -1;}
int is_full() {return top == MAX_STACK_SIZE-1;}
int size() {return top+1;}

void push(Element e)
{
    if(is_full())
    error("스택 포화 에러");
    data[++top] = e;
}
Element pop()
{
    if(is_empty())
    error("스태 공백 에러");
    return data[top];
}
Element peek()
{
    if(if_empty())
    error("스택 공백 에러");
    return data[top];
}
int cheek_matching(char expr[])
{
    int i = 0, prev;
    char ch;

    init_stack();
    while(expr[i] !='\0'){
        ch = expr[i++];
        if(ch == '[' || ch == '(' || ch == '{')
        push(ch);
    else if( ch == ']' || ch == ')' || ch == '}'){
        if(is_empty())
        return 2;
        prev = pop();
        if((ch == ']' && prev != '[')
        || (ch == ')' && prev != '(')
        || (ch == '}' && prev != '{')){
            return 3;
        }
    }
    }
    if(is_epmty()==0) return 1;
    return 0;
}

void main()
{
    char expr[4][80] = {"{A[(i+1)]=0;}", "if((i==0) && (j==0)",
                        "A[(i+1])=0;", "A[i] = f)(;"};
    int errCode, i;

    for(i=0 ; i<4; i++){
        errCode = check_matching(expr[i]);
        if( errCode == 0)
        printf("정싱: %s\n", expr[i]);
        elseprintf("오류:%s (조건%d 위반)\n", expr[i], errCode);
    }
}

double calc_postfix(char expr[])
{
    char c;
    int i = 0;
    double val,val1,val2;

    init_stack();
    while(expr[i]!='\n'){
        c = expr[i++];
        if(c>='0' && c<='9'){
            val = c - '0';
            push(val);
        }
        else if(c=='+' || c=='-' || c=='*' || c=='/'){
            val2 = pop();
            val1 = pop();
            switch(c){
                case '+': push(val1 + val2); break;
                case '-': push(val1 - val2); break;
                case '*': push(val1 * val2); break;
                case '/': push(val1 / val2); break;
            }
        }
    }
    return pop();
}
void main()
    {
        char expr[2][80] = {"8 2 / 3- 3 2 * +", "1 2 / 4 * 1 4 / *"};

        printf("수식:%s = %lf\n", expr[0], calc_postfix(expr[0]));
        printf("수식: %s = %lf\n"), expr[1], calc_postfix(expr[1]);
    }

    int precedence(char op)
    {
        switch(op){
            case'(' : case ')' : return 0;
            case'+' : case '-' : return 1;
            case'*' : case '/' : return 2;
        }
        return -1;
    }

    void infiw_to_postfix(char expr[])
    {
        int i = 0;
        char C, op;

        init_stack();
        while(expr[i]!= '\0'){
            c = expr[i++];
            if((c>='0' && c<='9')){
                printf("%c", c);
            }
        }
    }