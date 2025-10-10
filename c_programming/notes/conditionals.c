//RA 7th Conditionals notes
#include <stdio.h>
#include <string.h>

/*logical operators
&& amd
|| or
! not


*/


int main(void){
    int grade;
    char name[50];
    printf("what is your grade percent:\n");
    scanf("%d", &grade);
    printf("what is your name:\n");
    scanf("%d", &name);

    //printf("%d", strcmp(name, "Ms.Larose"));






    if(name == "Ms.LaRose"){
        printf("you dont get a grade");
    }else if(grade >= 90){
        printf("You have an A\n");
    }   
        
    else if(grade>= 80){
        printf("You have an B");
    }
    else if(grade>= 70){
        printf("You have an C");
    }
    else if(grade>= 60){
        printf("You have an D");
}
    else{
        printf("you have an F");
    }
    return 0;






}