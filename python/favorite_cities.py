# Write code below 💖

class City:
  def __init__(self, name, country, population, landmarks, nickname, foundingyear, mayor):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.nickname = nickname
    self.foundingyear = foundingyear
    self.mayor = mayor
        
newyork = City("New York", "United States of America", 8478000, "Empire State Building", "The Big Apple", 1624 ,"Eric Adams")

london = City("London", "United Kingdom", 8945310, "Big Ben", "The Big Smoke", 43, "Sadiq Khan")

frankfurt = City("Frankfurt am Main", "Germany", 773068, "Main Tower", "Mainhattan", 749, "Mike Josef")

print(vars(newyork))
print(vars(london))
print(vars(frankfurt))