#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct student{
    int id;
    char name[20];
    char dept[32];
} Student;

void tset1(Student s);
void test2(Student *s);
Student test3(Student s);

int main(void)
{
    Student s1,s2;
    Student *ps = &s2;

    s1.id = 10;
    strcpy(s1.name,"park");
    strcpy(s1.dept,"Coputer Eng")
}