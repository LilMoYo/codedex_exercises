
ph = int(input("What is the pH level of your liquid? "))

if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")