#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "rpg.h"

#define nb_attacks 2

void print_fighter(FIGHTER f){
    printf("\tFighter Display :\n");
    printf("Name : %s\n", f.name);
    printf("ATT : %d\n", f.ATT);
    printf("DEF : %d\n", f.DEF);
    printf("MAG : %d\n", f.MAG);
    printf("RES : %d\n", f.RES);
    for (int i = 0; i < nb_attacks; i++ ){
        printf("Skill number : %d\tType : %c\tPower : %d\n", f.skill_num[i], f.skill_type[i], f.skill_dmg[i]);
    }
    printf("\n");
}

void print_user_choice(FIGHTER f, int choice){
    printf("You have chosen [%s]\n", f.name);
}

int damage_formula(FIGHTER A, FIGHTER D, int choice){
    int damage_dealt;
    switch(A.skill_type[choice]){
        case 'P':
            damage_dealt = (A.ATT + A.skill_dmg[choice]) - D.DEF;
            break;
        case 'M':
            damage_dealt = (A.MAG + A.skill_dmg[choice]) - D.RES;
            break;
    }
    return damage_dealt;
}

int rock_paper_scissors(){
    int sign;
    while(2){
        printf("Who will begin first ? Let's decide with a good old 1) rock / 2) paper / 3) scissor\n");
        printf("choose a sign -> ");
        scanf("%d", &sign);
        if (sign >=1 && sign <= 3){
            break;
        }
        else{
            printf("wrong input\n");
        }
    }

    printf("the CPU will choose a random sign...");
    int cpu_sign;
    cpu_sign = rand()%3 + 1;
    printf("CPU choose %d\n", cpu_sign );
    int turn;
    switch (sign){
        case 1:
            if(sign == 1 && (cpu_sign == 1 || cpu_sign == 3)){turn = 1;}
            else{turn = 2;}
            break;
        case 2:
            if(sign == 2 && (cpu_sign == 2 || cpu_sign == 1)){turn = 1;}
            else{turn = 2;}
            break;
        case 3:
            if(sign == 3 && (cpu_sign == 3 || cpu_sign == 2)){turn = 1;}
            else{turn = 2;}
            break;
    }
    if (turn == 1){
        printf("The Player begins first !\n");
    }
    else{
        printf("The CPU begins first !\n");
    }
    return turn;
}

void fight(FIGHTER user, FIGHTER cpu, int turn){
    int input;
    int ko = 0;
    int dmg_dealt;
    while(ko != 1){
        if (turn == 1){
            printf("\t[Player turn !]\n");
            printf("Choose your action :");
            for(int nb = 0; nb < nb_attacks; nb++){
                printf("%d) ", nb);
            }
            printf("\n-> ");
            scanf("%d", &input);
            if(input >=0 && input <= nb_attacks){
                printf("%s use skill %d !\n", user.name, user.skill_num[input]);
                dmg_dealt = damage_formula(user, cpu, input);
                printf("%s inflicts %d damage\n", user.name, dmg_dealt);
                cpu.PV -= dmg_dealt;
                if (cpu.PV > 0){
                    printf("%s has %d PV left\n", cpu.name, cpu.PV);
                    turn = 2;
                }
                else{
                    printf("%s is KO\n", cpu.name);
                    ko = 1;
                }
            }
            else{
                printf("Wrong input\n");
            }
        }
        if (turn == 2){
            printf("\t[CPU turn !]\n");
            input = rand()%nb_attacks;
            printf("%s use skill %d !\n", cpu.name, cpu.skill_num[input]);
            dmg_dealt = damage_formula(cpu, user, input);
            printf("%s inflicts %d damage\n", cpu.name, dmg_dealt);
            user.PV -= dmg_dealt;
            if (user.PV > 0){
                printf("%s has %d PV left\n", user.name, user.PV);
                turn = 1;
            }
            else{
                printf("%s is KO\n", user.name);
                ko = 2;
            }
        }
    }
    if (ko == 1){
        printf("Player wins !\n");
    }
    else if (ko == 2){
        printf("CPU wins !\n");
    }
}