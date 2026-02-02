earth_weight = float(input('What is your weight on Earth? '))

print("Which planet would you like to travel to?")
print("1 - Mercury")
print("2 - Venus")
print("3 - Mars")
print("4 - Jupiter")
print("5 - Saturn")
print("6 - Uranus")
print("7 - Neptune")

planet = int(input("Enter the number of the planet: "))

if planet == 1:
  destination_weight = earth_weight * 0.38
elif planet == 2:
  destination_weight = earth_weight * 0.91
elif planet == 3:
  destination_weight = earth_weight * 0.38
elif planet == 4:
  destination_weight = earth_weight * 2.53
elif planet == 5:
  destination_weight = earth_weight * 1.07
elif planet == 6:
  destination_weight = earth_weight * 0.89
elif planet == 7:
  destination_weight = earth_weight * 1.14
else:
  destination_weight = None
  print('Invalid planet number')

if destination_weight:
  print("Your weight on this planet is:", round(destination_weight, 2))