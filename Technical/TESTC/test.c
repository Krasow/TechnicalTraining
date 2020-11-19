#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//purpose: this program will teach trainees how to properly comment.


//function to generate name random time based on the rand
//inputs: random: random number generated
//        name: name of the user entered
//outputs: count: the amount of printed names
int nameCall(int random, char name[12]){
    int i, count=0;
    for(i=0; i < random; i++){
        printf("%s\t", name);
        count++;
    }
    printf("\n");
    return count;
}

//function to generate name random time based on the rand
//inputs: count: a variable returns by the nameCall function. It is the count of the amount of names printed.
//outputs: none, prints a sqaure based off the input
void square(int count){
    int i, j; 

    for(int i=0; i < count/3; i++) {
        for(int j=0; j < count/3; j++) {
            if (i == 0 || i == count/3 - 1) {
                printf("*");
            }
            else if(j == 0 || j == count/3 -1) {
                printf("*");
            }
            else {
                printf(" ");
            }
            printf(" ");
        }
        printf("\n");
    }

}


int main() {
    char name[12]; // char array that stores the name of the user
    int favNum; // users favorite number
    int rand; // random generated number
    int count;


    //asks users to enter name and displays name
    printf("Enter your name: ");
    scanf("%s", name);
    printf("Hello, %s!\n", name);
    printf("Welcome to CPE Technical Training Camp Hosted on technicalcomptraining.xyz\n");
    //This asks user their favorite number and displays it
    printf("Enter your favorite number: ");
    scanf("%d", &favNum);

    //creates a randomly generated number by using the favNum as a seed
    srand48(favNum);
    rand = 100*drand48();

    count = (int)nameCall(rand, name);
    square(count);
    return 0;
}