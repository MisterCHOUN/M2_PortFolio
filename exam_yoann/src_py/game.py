class game:
    def __init__ (self):
        self.name = ""
        self.description = ""
        self.genre = ""
        self.plateforme = ""
        self.creator = ""
        self.stock = 0
        self.moyenne = 0 # sur 10

    def add_game(self, liste):
        n = 0
        self.name = liste[n]
        self.description = liste[n+1]
        self.genre = liste[n+2]
        self.plateforme = liste[n+3]
        self.creator = liste[n+4]
        self.stock = liste[n+5]
        self.moyenne = liste[n+6] # sur 10

    def print_game_desc(self):
        print("Nom du jeu : ", self.name)
        print("Description : ",self.description)
        print("Genre : ", self.genre)
        print("Plateforme Jouable : ", self.plateforme)
        print("Createur du jeu : ", self.creator)
        print("Stock disponible : ",self.stock, " copie(s)")
        print("Note moyenne : ",self.moyenne, "/10")