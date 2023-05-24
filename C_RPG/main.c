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
#include "rpg.h"

#define nb_fighter 2

int main(void){

    //Roster[2];
    FIGHTER f[nb_fighter] = {
        {"Maxime", 30, 8, 2, 6, 4, {1, 2}, {'P', 'M'}, {5, 5} },
        {"Walid", 30, 3, 4, 7, 6, {1, 2}, {'P', 'M'}, {4, 6}}
    };
    //Roster[]
    //FIGHTER f3 = {"Adrian", 10, 10, 0, 0};

    //print_class(f1);
    print_fighter(f[0]);
    print_fighter(f[1]);

    int choice;
    while(1){
        printf("\tWelcome to Smash in the house !\n");
            printf("\tChoose your character :\n");
            for (int i = 0; i < nb_fighter; i++){
                printf("Fighter number %d : %s\n", i, f[i].name);
            }
            printf("Input the number you want -> ");
            scanf("%d", &choice);
        if (choice >= 0 && choice < nb_fighter){
            print_user_choice(f[choice], choice);
            
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
        if (cpu_choice != choice){
            break;
        }
    }
    printf("The CPU has chosen : %s\n\n", f[cpu_choice].name);

    printf("Let's smash in the house !!!\n");
    printf("Player : [%s] VS CPU : [%s]\n", f[choice].name, f[cpu_choice].name);
    
    int turn = rock_paper_scissors();

    fight(f[choice], f[cpu_choice], turn);

    return 0;
}

