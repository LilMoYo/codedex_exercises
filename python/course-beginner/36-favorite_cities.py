
class City:
    def __init__(self, 
                 name: str, 
                 country: str, 
                 population: int, 
                 landmarks: list, 
                 nickname: str, 
                 foundingyear: int, 
                 mayor: str):
        
        # Strings
        self.name = name
        self.country = country
        self.nickname = nickname
        self.mayor = mayor
        
        # Integers
        self.population = round(population, -3)
        self.foundingyear = foundingyear
        
        # Lists
        self.landmarks = landmarks
        
newyork = City("New York", "USA", 8478000, ["Empire State Building"], "The Big Apple", 1624, "Eric Adams")

london = City("London", "UK", 8945310, ["Big Ben", "Tower of London"], "The Big Smoke", 43, "Sadiq Khan")

frankfurt = City("Frankfurt am Main", "Germany", 773068, ["Main Tower"], "Mainhattan", 749, "Mike Josef")

print(vars(newyork))
print(vars(london))
print(vars(frankfurt))
