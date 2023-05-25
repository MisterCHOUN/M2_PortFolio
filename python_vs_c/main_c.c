#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int addition(int number1, int number2){
    int new_number = number1 + number2;
    return new_number;
}

int main(void){
    int number1, number2;
    number1 = 2;
    number2 = 3;

    int number3;

    number3 = addition(number1, number2);

    int array[10];

    printf("number3 = %d\n", number3);

    for (int i=0; i < 10; i ++){
        printf("i = %d\t", i);
        array[i]= i;
        if(i%2 == 0){
            printf("Nombre Pair\n");
        }
        else{
            printf("Nombre Impair\n");
        }
    }

    int y = 0;
    while (y < 10)
    {
        printf("array[%d] = %d\n", y, array[y]);
        y++;
    }
    

    return 0;
}