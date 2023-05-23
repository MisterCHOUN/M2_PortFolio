from character import *
from vehicule import *
from rules import *
from track import *

class MK_menu:
    def __init__ (self):
        self.input_choice = 0

    def opening(self, menu):
        
        user_character = character()
        user_vehicule = vehicule()
        user_rules = rules()
        user_track = track()

        menu.input_choice = '1'
        while(1):
            if menu.input_choice == '1':
                menu.main_menu()
            elif menu.input_choice == '2':
                menu.character_menu(user_character)
            elif menu.input_choice == '3':
                menu.vehicule_menu(user_vehicule)
            elif menu.input_choice == '4':
                menu.rules_menu(user_rules)
            elif menu.input_choice == '5':
                menu.track_menu(user_track)
            elif menu.input_choice == '6':
                user_character.print_character_stat()
                user_vehicule.print_vehicule_stat()
                user_rules.print_rules_stats()
                user_rules.print_rules_stats()
                user_track.print_track_rules()
                print("LET'S START THE RACE !")
                exit()
            elif menu.input_choice == '-1':
                break
        
        print("Okidoki, Goodbye !\n")
        exit()
        
    def main_menu(self):
        print("\nOpening Mario Kart Menu :\n")
        while(1):
            print("Select your choice :")
            print("1) Play")
            print("2) Quit\n")
            
            input_choice = input("input -> ")
            #print("input_choice =", input_choice)
            if (input_choice == '1'):
                print("User chooses [PLAY]")
                self.input_choice = '2'
                break
            elif(input_choice == '2'):
                self.quit_game()
            else:
                print("Mamamia, wrong input !\n")

    def character_menu(self, user_character):
        #print("name ", user_character.name)
        #user_character.print_character_stat()
        user_character.character_select(self, user_character)
        if user_character.name != "":
            self.input_choice = '3'
            #print(user_character.name)
            user_character.print_character_stat()
        else:
            self.input_choice = '1'

        print("menu = ", self.input_choice)
        
    def vehicule_menu(self, user_vehicule):
        #user_vehicule.print_vehicule_stat()
        user_vehicule.select_vehicule()
        if user_vehicule.core != "":
            self.input_choice = '4'
            #user_vehicule.print_vehicule_stat()
        else:
            self.input_choice = '2'
        print("menu = ", self.input_choice)

    def rules_menu(self, user_rules):
        #user_rules.print_rules_stats()
        user_rules.select_rules()
        if user_rules.speed != "":
            self.input_choice = '5'
            #user_rules.print_rules_stats()
        else:
            self.input_choice = '3'
        print("menu = ", self.input_choice)

    def track_menu(self, user_track):
        #user_track.print_track_rules()
        user_track.select_track()
        if user_track.track_name != "":
            self.input_choice = '6'
            #user_track.print_track_rules()
        else:
            self.input_choice = '4'

    def quit_game(self):
        print("Okidoki, Goodbye !\n")
        exit()