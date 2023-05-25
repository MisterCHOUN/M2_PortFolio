/*
1) Documentation
2) Preprocessors /Libraries
3) Definition / Variable Globale #define
4) Déclaration Globale : 
par ex, remettre la fonction au départ, si elle a été codé plus bas
int PlayerAmmo (int ammo);
5) Main Function
int main(void)
6) Subprograms (user-defined functions)
*/


/*
SUR VSC
utiliser pour les scanf
# define _CRT_SECURE_NO_WARNINGS
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include "rpg.h"

#define nb_fighter 4

union user{
    int choice;
}u;



int main(void){

    srand ( time(NULL) );

    //Roster[2];
    FIGHTER f[nb_fighter] = {
        {"Maxime", 30, 8, 2, 6, 4, {"Bite the Dust", "Burlp"}, {'P', 'M'}, {5, 5}, {80, 80} },
        {"Walid", 30, 3, 4, 7, 6, {"Throw a Bag", "Hack ur Switch !"}, {'P', 'M'}, {8, 7}, {80, 75}},
        {"Raphael", 30, 8, 5, 3, 4, {"Stiking Pose", "High Jump kick"}, {'P', 'P'}, {3, 7}, {90, 60}},
        {"Adrian", 30, 10, 4, 3, 3, {"Swearing", "RUN OVER YOU"}, {'M', 'P'}, {7, 15}, {100, 50}}
        //{"GOD Adrian", 30, 10, 10, 10, 10, {"S#!7 0n u", "GAS GAS GAS"}, {'M', 'P'}, {5, 5}, {100, 100}}
    };
    //Roster[]
    //FIGHTER f3 = {"Adrian", 10, 10, 0, 0};

    //print_class(f1);
    print_fighter(f[0]);
    print_fighter(f[1]);

    //int choice;
    while(1){
        printf("\tWelcome to Smash in the house !\n");
            printf("\tChoose your character :\n");
            for (int i = 0; i < nb_fighter; i++){
                printf("Fighter number %d : %s\n", i, f[i].name);
            }
            printf("Input the number you want -> ");
            scanf("%d", &u.choice);
        if (u.choice >= 0 && u.choice < nb_fighter){
            print_user_choice(f[u.choice], u.choice);
            break;
        }
        else{
            printf("Wrong input try again\n");
        }
    }
    int cpu_choice;
    printf("the CPU will choose at random...");
    while(1){
        cpu_choice = rand()%nb_fighter;
        if (cpu_choice != u.choice){
            break;
        }
    }
    printf("The CPU has chosen : %s\n\n", f[cpu_choice].name);

    printf("Let's smash in the house !!!\n");
    printf("Player : [%s] VS CPU : [%s]\n", f[u.choice].name, f[cpu_choice].name);
    
    int turn = rock_paper_scissors();

    fight(f[u.choice], f[cpu_choice], turn);

    return 0;
}

