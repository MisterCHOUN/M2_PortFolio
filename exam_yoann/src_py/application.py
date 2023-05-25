from random import randrange
from game import *
from utilisateur import *

class Application:
    def __init__ (self):
        self.menu_num = ""
        pass

    def application_launch(self):

        #["", "", "", "", "", randrange(50), randrange(11)]
        liste = [
            ["SSBU", "Jeu de Combat all-star", "Combat", "Switch", "Nintendo", randrange(50), randrange(11)],
            ["Starcraft 2", "Stratégie dans un univers parallel", "Stratégie", "PC", "Blizzard", randrange(50), randrange(11)],
            ["League of Legends", "Jeu d'équipe 5v5", "Combat", "PC", "Riot", randrange(50), randrange(11)],
            ["Zelda BOTW", "Aventure mystique", "Aventure", "Switch", "Nintendo", randrange(50), randrange(11)]
        ]

        user = utilisateur()

        self.menu_num = 1

        while(1):
            if self.menu_num == 1:
                self.menu_accueil(user)
            elif self.menu_num == 2:
                self.menu_utilisateur(user, liste)
            elif self.menu_num == 3:
                self.menu_administrateur(liste)
            elif self.menu_num == 0:
                print("L'application va s'éteindre\n\n Au revoir !")
                break

    
    def menu_accueil(self, user):
        print("Bienvenue dans l'application [Game Reviewer]")
        while(1):
            print("Que voulez-vous faire ?")
            print("1) Entrée (Utilisateur)")
            print("2) Entrée (Administrateur)")
            print("3) Quitter")
            user.input = int( input("input -> ") )

            if user.input == 1:
                print("Entrée Utilisateur,\nVous pouvez consulter la base de donnée de l'application")
                self.menu_num = 2
                break
            elif user.input == 2:
                print("Entrez le mot de passe :")
                password = input("-> ")
                if password == 'password':
                    print("Entrée Administrateur,\nVous pouvez modifier la base de donnée de l'application")
                    self.menu_num = 3
                    break
                else:
                    print("Mot de passe incorrect\n retour à l'accueil\n")
            elif user.input == 3:
                print("Extinction de l'application")
                self.menu_num = 0
                break
            else:
                print("Input incorrect, veuillez choisir un nombre entre 1 et 3")

    def menu_utilisateur(self, user, liste):
        
        while(1):
            print("Que voudrez-vous faire ?")
            print("1) Voir la description entière d'un jeu")
            print("2) revenir au menu principal")
            user.input = int(input("-> "))
            if user.input == 1:
                print("Voici la liste des jeux en stock :")
                nb_jeux = len(liste)
                for numero in range(0, nb_jeux):
                    print("Jeu n°", numero+1, " -> ", liste[numero][0]) 
                while(2):
                    print("Quel jeu voudriez-vous voir ?\n appuyer sur 0 pour revenir à l'accueil principal")
                    sec_input = int( input("-> ") )
                    if sec_input >= 1 and sec_input <= 4:
                        user.game = game()
                        user.game.add_game(liste[sec_input])
                        user.game.print_game_desc()
                        break
                    elif sec_input == 0:
                        user.input = 2
                    else:
                        print("Input incorrect, veuillez choisir un nombre entre 0 et 3")
            elif user.input == 2:
                print("retour au menu principal")
                self.menu_num = 1
                break
            else:
                print("Input incorrect, veuillez choisir un nombre entre 1 et 2")


    def menu_administrateur(self, liste):
        # ICI Pouvoir mettre des jeux en plus dans la liste
        pass

        