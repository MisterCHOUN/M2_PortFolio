/*
Ouais les boucles dans des boucles de boucles
ce n'est pas très joli mais faire 2 programmes en c et python
c'est assez long.

le mot de passe est "azerty"
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include "application.h"

#define max_jeux 50

union user{
    int menu_choice;
    int user_choice;
    int selection;
    char mdp[6];
}u;

int main(){

    srand ( time( NULL ) );

    //{"", "", "", "", "", rand()%50, rand()%11}
    int current_nb = 4;
    JEU J[max_jeux]= {
        {"SSBU", "Jeu de Combat all-star", "Combat", "Switch", "Nintendo", rand()%50, rand()%11},
        {"Starcraft 2", "Strategie dans un univers parallel", "Strategie", "PC", "Blizzard", rand()%50, rand()%11},
        {"League of Legends", "Jeu d'equipe 5v5", "Combat", "PC", "Riot", rand()%50, rand()%11},
        {"Zelda BOTW", "Aventure mystique", "Aventure", "Switch", "Nintendo", rand()%50, rand()%11}
    };

    u.menu_choice = 0;

    while(1){
        printf("Bienvenue dans l'application [Game Reviewer]\n");
        if(u.menu_choice == 0){
            while(2){
                printf("Que voulez-vous faire ?\n");
                printf("1) Entree (Utilisateur)\n");
                printf("2) Entree (Administrateur)\n");
                printf("3) Quitter\n");
                printf("Input -> ");
                scanf("%d", &u.menu_choice);
                if (u.menu_choice >= 1 && u.menu_choice <= 3){
                    break;
                }
                else{
                    printf("Input incorrect, veuillez choisir un nombre entre 1 et 3\n");
                }
            }
        }
        else if(u.menu_choice == 1){
            while(3){
                printf("Que voudrez-vous faire ?\n");
                printf("1) Voir la description entiere d'un jeu\n");
                printf("2) revenir au menu principal\n");
                printf("Input -> ");
                scanf("%d", &u.user_choice);
                if (u.user_choice == 1){
                    printf("Voici les noms des jeux de l'application : max = %d\n", current_nb);
                    for (int num = 0; num < current_nb; num++){
                        printf("Jeu numero %d : %s\n", num+1, J[num].name);
                    }
                    while(4){
                        printf("Quel jeu voudriez-vous voir ?\n appuyer sur 0 pour revenir a l'accueil principal\n");
                        printf("Input -> ");
                        scanf("%d", &u.selection);
                        if (u.selection >= 1 && u.selection <= current_nb){
                            print_game(J[u.selection-1]);
                            u.menu_choice = 0;
                            break;
                        }
                        else if(u.selection == 0){
                            printf("retour au menu principal\n");
                            u.menu_choice = 0;
                            break;
                        }
                        else{
                            printf("Input incorrect, veuillez choisir un nombre entre 0 et %d\n", current_nb);
                        }
                    }
                    break;
                }
                else if (u.user_choice == 2){
                    u.menu_choice = retour_menu_principal();
                    break;
                }
                else{
                    printf("Input incorrect, veuillez choisir un nombre entre 1 et 2\n");
                }
            
            }
        }
        else if (u.menu_choice == 2){
            int confirmation =  confirmation_mdp();
            printf("confirmation = %d\n", confirmation);
            switch(confirmation){
                case 0:
                    u.menu_choice = 0;
                    break;
                case 1:
                    while(3){
                        printf("Bienvenue administrateur !\n");
                        printf("Que voudriez-vous faire ?\n");
                        printf("1) ajouter un nouveau jeu dans la liste\n");
                        printf("2) revenir au menu principal\n");
                        printf("Input -> ");
                        scanf("%d", &u.user_choice);
                        if (u.user_choice == 1){
                            int new = add_game(&J[current_nb]);
                            print_game(J[current_nb]);
                            if (new == 1){
                                current_nb += 1;
                            }
                        }
                        else if (u.user_choice == 2){
                            u.menu_choice = retour_menu_principal();
                            break;
                        }
                        else{
                            printf("Input incorrect, veuillez choisir un nombre entre 1 et 2\n");
                        }

                    }
                    break;
            }
            u.menu_choice == 0;
        }
        else if (u.menu_choice == 3){
            printf("Extinction de l'application\n");
            printf("Au revoir\n");
            break;
        }
        
    }

    return 0;
}