class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(f"{self.name} {self.name}")
        
    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Types: {self.types}")
        print(f"Description: {self.description}")
        if self.is_caught == True:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught yet!")  
        
squirtle = Pokemon(7, "Squirtle", "Water", "After birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth.", True)

totodile = Pokemon(158, "Totodile", "Water", "ts powerful, well-developed jaws are capable of crushing anything. Even its Trainer must be careful.", True)

torchic = Pokemon(255, "Torchic", "Fire", "Torchic feels toasty warm if you hug it. It has a flame sac inside its belly, and the flames burn continuously as long as Torchic has life in it.", False)

squirtle.speak()
squirtle.display_details()
print("")
totodile.speak()
totodile.display_details()
print("")
torchic.speak()
torchic.display_details()
print("")