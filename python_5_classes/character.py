# J'ai eu des problèmes avec match pour je ne sais quelle raison
# donc je continue avec elif

class character:
    def __init__(self):
        self.name = ""
        self.Speed = ""
        self.Acceleration = ""
        self.Weight = ""
        self.Handling = ""
        self.Traction = ""

    def character_select(self, menu, user_character):
        choice = 0
        print("Choose your character :")
        list = [
            ["Mario", 7, 2, 6, 4, 2],
            ["Luigi", 2, 7, 5, 5, 1],
            ["Peach", 6, 3, 4, 5, 3],
            ["Bowser", 10, 1, 10, 1, 1]
        ]
        while (1):
            print("1) Mario\t2) Luigi\t3) Peach\t4) Bowser")
            print("c) [Create your own]")
            print("q) [Return to Menu]\n")
            choice = input("input -> ")
            print("choice = ", choice)
            if choice == '1':
                print("Waouh !")
                #user_character = list[1]
                #user_character.attribute_to_class("Mario", 7, 2, 6, 4, 2)
                user_character.attribute_to_class(list[0])
                #print("user_character_name =", user_character.name)
                #user_character.print_character_stat()
                break 
            elif choice =='2':
                print("Oh Yeah !")
                user_character.attribute_to_class(list[1])
                break
            elif choice =='3':
                print("Sweet !")
                user_character.attribute_to_class(list[2])
                break
            elif choice =='4':
                print("Showtime !")
                user_character.attribute_to_class(list[3])
                break
            elif choice == 'c':
                user_character.custom_character(user_character)
                break
            elif choice == 'q':
                menu.input_choice = '1'
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
        
    def custom_character(self, user_character):
        points_to_spare = 20
        name = input("Enter your name : ")
        print("-> ", end='')
        print("You have 20 points to spare,")
        print("You are allowed to spend 0 to 10 points in a stat")
        print("Weight Stat is it's own case, \tyou will be allowed to choose a number between 1 and 10")

        print("\nHow much point will you spend to the speed stat ?\t Points left :", points_to_spare)
        while(1):
            point_used = int(input("Point(s) to spend -> "))
            if point_used <= 10 and point_used >= 0 and points_to_spare >= 0:
                points_to_spare -= point_used
                speed = point_used
                break
            else:
                print("error, please input a number between 1 and 10")
        print("Points left :", points_to_spare)

        print("\nHow much point will you spend to the Acceleration stat ?\t Points left :", points_to_spare)
        while(2):
            point_used = int(input("Point(s) to spend -> "))
            if point_used <= 10 and point_used >= 0 and points_to_spare >= 0:
                points_to_spare -= point_used
                acceleration = point_used
                break
            else:
                print("error, please input a number between 1 and 10")
        print("Points left :", points_to_spare)

        print("\nHow much point will you choose to the Weight stat ?")
        while(3):
            point_used = int(input("Weight from 1 to 10 -> "))
            if point_used <= 10 and point_used >= 0:
                weight = point_used
                break
            else:
                print("error, please input a number between 1 and 10")

        print("\nHow much point will you spend to the Handling stat ?\t Points left :", points_to_spare)
        while(4):
            point_used = int(input("Point(s) to spend -> "))
            if point_used <= 10 and point_used >= 0 and points_to_spare >= 0:
                points_to_spare -= point_used
                handling = point_used
                break
            else:
                print("error, please input a number between 1 and 10")
                print("Points left :", points_to_spare)
        print("Points left :", points_to_spare)

        print("\nHow much point will you spend to the Traction stat ?\t Points left :", points_to_spare)
        while(5):
            point_used = int(input("Point(s) to spend -> "))
            if point_used <= 10 and point_used >= 0 and points_to_spare >= 0:
                points_to_spare -= point_used
                traction = point_used
                break
            else:
                print("error, please input a number between 1 and 10")
                print("Points left :", points_to_spare)

        print("Points left :", points_to_spare)

        print("RECAP :")
        print("name =", name)
        print("speed =", speed)
        print("acceleration =", acceleration)
        print("weight =", weight)
        print("handling =", handling)
        print("traction =", traction)
        
        print("Custom Character complete !")

        user_character.attribute_to_class(name, speed, acceleration, weight, handling, traction)
    
    def attribute_to_class(self, list):
        n = 0
        self.name = list[0]
        self.Speed = list[n+1]
        self.Acceleration = list[n+2]
        self.Weight = list[n+3]
        self.Handling = list[n+4]
        self.Traction = list[n+5]

    def print_character_stat(self):
        print("Character Chosen :")
        print("\tname =", self.name)
        print("\tspeed =", self.Speed)
        print("\tacceleration =", self.Acceleration)
        print("\tweight =", self.Weight)
        print("\thandling =", self.Handling)
        print("\ttraction =", self.Traction)
        print