class vehicule:
    def __init__(self, speed, teams, items, CPU, courses, race_count):
        self.speed = speed
        self.teams = teams
        self.items = items
        self.CPU = CPU
        self.courses = courses
        self.race_count = race_count

    def select_rules():
        print("Choose the Speed setting:")
        print("1) 50cc\t2) 100cc\t3) 150cc")

        print("Will you allow team race ?")
        print("1) Yes\t2) No")

        print("Select the items parameters:")
        print("1) Classic\t2) Explosive\t3) No Items")

        print("Select the difficulty of CPU:")
        print("1) Easy\t2) Normal\t3) Hard")

        print("Select the course choice:")
        print("1) Choose\t2) random")

        print("Select the number of races for this game:")
        print("Enter a number -> ")