class MK_menu:
    def __init__ (self):
        self.input_choice = 0

    def opening(self, menu):
        print("\nOpening Mario Kart Menu :\n")
        path = 1
        
        while(1):
            print("Select your choice :")
            print("1) Play")
            print("2) Quit\n")
            
            menu.input_choice = input("input -> ")
            #print("menu.input_choice =", menu.input_choice)
            if (menu.input_choice == '1'):
                print("User chooses [PLAY]")
                break
            elif(menu.input_choice == '2'):
                menu.quit_game()
            else:
                print("Mamamia, wrong input !\n")
        
    def main_menu(self):


    def quit_game(self):
        print("Okidoki, Goodbye !\n")
        exit()