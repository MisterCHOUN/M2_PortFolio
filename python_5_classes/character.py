# J'ai eu des problèmes avec match pour je ne sais quelle raison
# donc je continue avec elif

class character:
    def __init__(self, name, Speed, Acceleration, Weight, Handling, Traction):
        self.name = name
        self.Speed = Speed
        self.Acceleration = Acceleration
        self.Weight = Weight
        self.Handling = Handling
        self.Traction = Traction

    def character_select(self):
        choice = 0
        print("Choose your character :")
        while (1):
            print("1) Mario\t2) Luigi\t3) Peach\t4) Bowser")
            print("c) [Create your own]")
            print("q) [Return to Menu]\n")
            choice = input("input -> ")
            if choice == '1':
                return("Mario", 7, 2, 6, 4, 2)
            elif choice =='2':
                return("Luigi", 2, 7, 5, 5, 1)
            elif choice =='3':
                return("Peach", 6, 3, 4, 5, 3)
            elif choice =='4':
                return("Bowser", 10, 1, 10, 1, 1)
            elif choice == 'c':
                break
            elif choice == 'q':
                print("back to main menu")
                break
            else:
                print("Mamamia, wrong input !\n")
            # match choice:
            #     case 1:
            #         return("Mario", 7, 2, 6, 4, 2)
            #     case 2:
            #         return("Luigi", 2, 7, 5, 5, 1)
            #     case 3:
            #         return("Peach", 6, 3, 4, 5, 3)
            #     case 4:
            #         return("Bowser", 10, 1, 10, 1, 1)

    def custom_character():
        print("You have 20 points to spare,")
        print("You are allowed to spend 1 to 9 points in a stat")
        print("Weight Stat is it's own case, \tyou will be allowed to choose a number between 1 and 10")
        print("How much point will you spend to the speed stat ?")
        print("Point(s) spend -> ")

        print("How much point will you spend to the Acceleration stat ?")
        print("Point(s) spend -> ")

        print("How much point will you choose to the speed stat ?")
        print("Weight from 1 to 10 -> ")

        print("How much point will you spend to the Handling stat ?")
        print("Point(s) spend -> ")

        print("How much point will you spend to the Traction stat ?")
        print("Point(s) spend -> ")

        print("Custom Character complete !")