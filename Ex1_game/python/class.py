class Bird:
    def __init__(self, species):
        self.species = species


b1 = Bird("Corbeau")

print("\n", str(b1), "species is :")
print(b1.species)