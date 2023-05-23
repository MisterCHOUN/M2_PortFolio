class track:
    def __init__(self):
        self.track_name = ""
        self.nb_laps = 3

    def select_track(self):
        print("\nSelect your rules :\n")
        tmp = ["Luigi's Circuit", "Peach's Gardens", "Bowser's Castle", "Rainbow Road"]
        while(1):
            print("Choose the track :")
            choice = int(input("1) Luigi's Circuit\t2) Peach's Gardens\t 3) Bowser's Castle\t4) Rainbow Road\n-> "))
            if choice >= 1 and choice <= 4:
                self.track_name = tmp[choice -1]
                break
            else:
                print("Mamamia, wrong input !\n")

        while(2):
            print("Choose the number of laps :")
            choice = int(input("2 to 6 laps -> "))
            if choice >= 2 and choice <= 6:
                self.track_name = choice
                break
            else:
                print("Mamamia, wrong input !\n")

    def print_track_rules(self):
        print("Current Rules:")
        print("\tTrack Name =", self.track_name)
        print("\tNumber of Laps =", self.nb_laps)
        print