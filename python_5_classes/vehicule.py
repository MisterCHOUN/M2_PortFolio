class vehicule:
    def __init__(self):
        self.core = ""
        self.tires = ""
        self.glider = ""

    def select_vehicule(self):
        print("Select your vehicule:\n")
        
        while(1):
            print("Select your core part:")
            choice = int(input("1) Kart\t2) Bike\t3) Quad/ATV\n-> "))
            if choice == 1 :
                self.core = "Kart"
                break
            elif choice == 2 :
                self.core = "Bike"
                break
            elif choice == 3 :
                self.core = "Quad/ATV"
                break
            else:
                print("Mamamia, wrong input !\n") 

        tmp = ["Standart", "Monster", "Rollers"]
        while(2):
            print("Select your tires:")
            choice = int(input("1) Standart\t2) Monster\t3) Rollers\n-> "))
            if choice >= 1 or choice <= 3:
                self.tires = tmp[choice - 1]
                break
            else:
                print("Mamamia, wrong input !\n") 

        tmp = ["Classic Glider", "Cloud Glider", "Parachute"]
        while(3):
            print("Select your glider:")
            choice = int(input("1) Classic Glider\t2) Cloud Glider\t3) Parachute\n-> "))
            if choice >= 1 or choice <= 3:
                self.glider = tmp[choice - 1]
                break
            else:
                print("Mamamia, wrong input !\n") 

        print("Your vehicule is ready !")

    def print_vehicule_stat(self):
        print("Vehicule chosen:")
        print("\tcore =", self.core)
        print("\ttires =", self.tires)
        print("\tglider =", self.glider)
        print

