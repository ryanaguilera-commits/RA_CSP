//RA 7th Silly Sentances
#include <stdio.h>
#include <string.h>

int main(void){
    char adjective[25];
    char animal[25];
    char verb[25];

    printf("please give me an adjective:");
    scanf("%s", adjective);
    printf("please give me an active verb:");
    scanf("%s", verb);
    printf("please give me an animal:");
    scanf("%s", animal);
    printf("The %s %s was %s down the hill, through the barn and into the house.",adjective, animal, verb);



}







