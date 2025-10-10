//RA 7th Strings Notes
#include <stdio.h>
#include <string.h>
int main(void){
    char name[] = "Ryan";
    char last_name[25];
    printf("tell me your last name: \n");
    scanf("%s", last_name);
    char full_name[50];
    printf("%s\n", full_name);
    strcat(full_name, name);
    strcat(full_name, " ");

    last_name[0] = 'R';

    printf("%c\n", last_name[0]);

    strcat(full_name, last_name);
    printf("%s\n", full_name);

    printf("%zu", strlen(name));
    printf("%zu", sizeof(name));

    printf("Your name is %s %s", name, last_name);
}




