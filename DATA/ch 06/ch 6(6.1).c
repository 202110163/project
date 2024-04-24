#include<stdio.h>
#include<stdlib.h>

typedef int Element;
tyoedef struct DLinkedNode {
    Element data;
    struct DLinkedNode* prev;
    struct DLinkedNode* next;
} Node;
Node org;

void init_list