#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define nb_attacks 2

typedef struct Fighter {
  char name[20];
  int PV;
  int ATT;
  int DEF;
  int MAG;
  int RES;
  int skill_num[nb_attacks];
  char skill_name[nb_attacks][20];
  char skill_type[nb_attacks];
  int skill_dmg[nb_attacks];
} FIGHTER;

void print_fighter(FIGHTER f);

void print_user_choice(FIGHTER f, int choice);

int damage_formula(FIGHTER A, FIGHTER D, int choice);

int rock_paper_scissors();

void fight(FIGHTER user, FIGHTER cpu, int turn);

//void menu_1(FIGHTER )