//RA 7th Varibles
#include <stdio.h>
int main(void){
    int grade; //4 bytes
    float pi = 3.14; //4 bytes
    double long_pi = 3.14159265368; //8 bytes
    char letter; //1 byte
    char name[] = "Ryan";

    printf("what is your grade as a whole number? \n");
    scanf("%d", &grade);



    printf("what is your grade as a letter \n");
    scanf(" %c", &letter);

    printf("%s did it!\n", name);
    printf("You have a %d in the class that is a %c \n", grade, letter);
    return 0;




}