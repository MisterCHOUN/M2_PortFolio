from character import *
from vehicule import *
from rules import *
from track import *

class MK_menu:
    def __init__ (self):
        self.input_choice = 0

    def opening(self, menu):
        
        user_character = character("", "", "", "", "", "")
        user_vehicule = vehicule("", "", "")
        user_rules = rules("", "", "", "", "", "")
        user_track = track("", "")

        menu.input_choice = '1'
        while(1):
            if menu.input_choice == '1':
                menu.main_menu(menu)
            elif menu.input_choice == '2':
                menu.character_menu(menu, user_character)
            #elif menu.input_choice == '3':
                #menu.vehicule_menu(user_vehicule)
            #elif menu.input_choice == '4':
                #menu.vehicule_menu(menu, user_vehicule)
            #elif menu.input_choice == '5':
                #menu.vehicule_menu(menu, user_vehicule)
            elif menu.input_choice == '-1':
                break
        
        print("Okidoki, Goodbye !\n")
        exit()
        
    def main_menu(self, menu):
        print("\nOpening Mario Kart Menu :\n")
        while(1):
            print("Select your choice :")
            print("1) Play")
            print("2) Quit\n")
            
            input_choice = input("input -> ")
            #print("input_choice =", input_choice)
            if (input_choice == '1'):
                print("User chooses [PLAY]")
                menu.input_choice = '2'
                break
            elif(input_choice == '2'):
                menu.quit_game()
            else:
                print("Mamamia, wrong input !\n")

    def character_menu(self, menu, user_character):
        print("name ", user_character.name)
        user_character.print_character_stat()
        user_character.character_select(menu, user_character)
        if user_character.name != "":
            menu.input_choice = '3'
            print(user_character.name)
            user_character.print_character_stat()
        else:
            menu.input_choice = '1'

        print("menu = ", menu.input_choice)
        
    def vehicule_menu(self, menu, user_vehicule):
        pass
        

    def quit_game(self):
        print("Okidoki, Goodbye !\n")
        exit()