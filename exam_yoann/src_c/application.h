#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

//char name[20], char description[40], char genre[15], char plateforme[15], char creator[15], int stock

typedef struct jeu {
    char name[20];
    char description[40];
    char genre[15];
    char plateforme[15];
    char creator[15];
    int stock;
    int moyenne;
} JEU;

void print_game(JEU J);

int retour_menu_principal();

int add_game(JEU *J);

int confirmation_mdp();

void add_all_info(JEU* J, char name[20], char description[40], char genre[15], char plateforme[15], char creator[15], int stock);