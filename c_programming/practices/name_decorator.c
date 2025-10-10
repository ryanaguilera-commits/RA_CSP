//RA 7th Name Decorator
#include <stdio.h>
#include <string.h>
int main(void){
    char user_name[25];
    char decor[] = "Xx";
    char decor_two[] = "xX";
    printf("tell me your desired username: \n");
    scanf("%s", user_name);
    strcat(decor, user_name);
    printf("%s%s%s", decor, user_name, decor_two);











}





