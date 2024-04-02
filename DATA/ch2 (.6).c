int items =10;

int main(){

    return 0;
}
 

void insert(int array[], int loc, int value){
    for (int i = items; i>=loc;i--)
    array[i + 1] = array[i];

    array[loc]=value;
}