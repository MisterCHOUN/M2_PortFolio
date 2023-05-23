class rules:
    def __init__(self):
        self.speed = ""
        self.teams = ""
        self.items = ""
        self.CPU = ""
        self.courses = ""
        self.race_count = ""

    def select_rules(self):
        print("\nSelect your rules :\n")
        tmp = ["50cc", "100cc", "150cc"]
        while(1):
            print("Choose the Speed setting:")
            choice = int(input("1) 50cc\t2) 100cc\t3) 150cc\n-> "))
            if choice >= 1 and choice <= 3:
                self.speed = tmp[choice -1]
                break
            else:
                print("Mamamia, wrong input !\n") 

        tmp = ["Yes", "No"]
        while(2):
            print("Will you allow teams ?")
            choice = int(input("1) Yes\t2) No\n-> "))
            if choice == 1 or choice == 2:
                self.teams = tmp[choice - 1]
                break
            else:
                print("Mamamia, wrong input !\n")

        tmp = ["Classic", "Explosive", "No Items"]
        while(3):
            print("Select the items parameters:")
            choice = int(input("1) Classic\t2) Explosive\t3) No Items\n-> "))
            if choice >= 1 and choice <= 3:
                self.items = tmp[choice - 1]
                break
            else:
                print("Mamamia, wrong input !\n") 

        tmp = ["Easy", "Normal", "Hard"]
        while(4):
            print("Select the difficulty of CPU:")
            choice = int(input("1) Easy\t2) Normal\t3) Hard\n-> "))
            if choice >= 1 and choice <= 3:
                self.CPU = tmp[choice - 1]
                break
            else:
                print("Mamamia, wrong input !\n")

        tmp = ["Choose", "Random"]
        while(5):
            print("Select the course choice:")
            choice = int(input("1) Choose\t2) Random\n-> "))
            if choice == 1 or choice == 2:
                self.courses = tmp[choice - 1]
                break
            else:
                print("Mamamia, wrong input !\n")

        while(6):
            print("Select the number of races for this game:")
            choice = int(input("Enter a number (max 48) -> "))
            if choice >= 1 and choice <= 48:
                self.race_count = choice
                break
            else:
                print("Mamamia, wrong input !\n")

    def print_rules_stats(self):
        print("Current Rules:")
        print("\tSpeed =", self.speed)
        print("\tTeams =", self.teams)
        print("\tItems =", self.items)
        print("\tCPU =", self.CPU)
        print("\tcourses =", self.courses)
        print("\tNumber of races =", self.race_count)
        print
