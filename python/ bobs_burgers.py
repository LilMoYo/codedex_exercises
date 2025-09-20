class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = False
    
bobs_burgers = Restaurant()
bobs_burgers.name = "Bob's Burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.rating = 4.5
bobs_burgers.delivery = False

krusty_krab = Restaurant()
krusty_krab.name = "Krusty Krab"
krusty_krab.category = "Seafood Restaurant"
krusty_krab.rating = 4.0
krusty_krab.delivery = False

mocyonalds = Restaurant()
mocyonalds.name = "MocYonalds"
mocyonalds.category = "Fast Food"
mocyonalds.rating = 4.5
mocyonalds.delivery = True

print(vars(bobs_burgers))
print(vars(krusty_krab))
print(vars(mocyonalds))