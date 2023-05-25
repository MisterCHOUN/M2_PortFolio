#include "application.h"

void print_game(JEU J){
    printf("Nom du jeu : %s\n", J.name);
    printf("Description : %s\n",J.description);
    printf("Genre : %s\n", J.genre);
    printf("Plateforme Jouable : %s\n", J.plateforme);
    printf("Createur du jeu : %s\n", J.creator);
    printf("Stock disponible : %d copie(s)\n",J.stock);
    printf("Note moyenne : %d/10\n\n",J.moyenne);
}

int confirmation_mdp(){
    int confirmation, key;
    char mdp[5];
    printf("Entrer un mot de passe : ");
    scanf("%s", &mdp);
    confirmation = strcmp(mdp,"azerty");
    if (confirmation == 0)
    {
        printf("\tAccepted\n");
        key = 1;
    }
    else
    {
        printf("\tWrong password\n");
        key = 0;
    }

    return key;
}

int retour_menu_principal(){
    printf("retour au menu principal\n");
    return 0;
}

int add_game(JEU *J){
    char tmp1[20], tmp2[40], tmp3[15], tmp4[15], tmp5[15];
    int tmp6;
    printf("\nVeuillez ajouter le nom du nouveau jeu :\n");
    printf("-> ");
    scanf("%s", &tmp1);
    printf("\nVeuillez ajouter une description au nouveau jeu :\n");
    printf("-> ");
    scanf("%s", &tmp2);
    printf("\nVeuillez ajouter un genre au nouveau jeu :\n");
    printf("-> ");
    scanf("%s", &tmp3);
    printf("\nVeuillez ajouter la plateforme du nouveau jeu :\n");
    printf("-> ");
    scanf("%s", &tmp4);
    printf("\nVeuillez ajouter le createur du nouveau jeu :\n");
    printf("-> ");
    scanf("%s", &tmp5);
    printf("\nVeuillez ajouter le stock du nouveau jeu :\n");
    printf("-> ");
    scanf("%d", &tmp6);
    printf("\nLa note sera ajoutee plus tard :\n");
    strcpy(J->name,tmp1);
    strcpy(J->description,tmp2);
    strcpy(J->genre,tmp3);
    strcpy(J->plateforme,tmp4);
    strcpy(J->creator,tmp5);
    J->stock=tmp6;
    J->moyenne=5;
    //add_all_info(&J, tmp1, tmp2, tmp3, tmp4, tmp5, tmp6);
    //print_game(J);
    return 1;
}

void add_all_info(JEU* J, char name[20], char description[40], char genre[15], char plateforme[15], char creator[15], int stock){
    // strcpy(J.name, name);
    // strcpy(J.description, description);
    // strcpy(J.genre, genre);
    // strcpy(J.plateforme, plateforme);
    // strcpy(J.creator, creator);
    // strcpy(J->name,name);
    // strcpy(J->description,description);
    // strcpy(J->genre,genre);
    // strcpy(J->plateforme,plateforme);
    // strcpy(J->creator,creator);
    // J->stock=stock;
    // J->moyenne=5;
}