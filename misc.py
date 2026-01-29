print ("Welcom to the DundunDugneon\n"
       "You need to explore and solve few puzzles to escpape")
Name = input("What is your name?: ")
print (f"Lets begin your journey {Name} ! ")

print ("You are in a dark room, you can only see a glimer of light thru the door, what will you do?\n"
       "1) Go thourds the door\n"
       "2) Check out the room you are in")
answer = int(input("Enter answer 1 or 2: "))
if answer == 1:
    print("You are going thourds the door")
    #libary()
else:
    print("There is nothing intresting in this room")

print("What will you do now?\n"
      "1) Go thourds the door\n"
      "2) Look around the room")
answer = int(input("Enter answer 1 or 2: "))
if answer == 1:
    print("You are going thours the door")
else:
    print("Yup there is nothing")

print("Soo what now?\n"
      "1) Go thru that door that i told you about twice\n"
      "2) Look around the room even more")
answer = int(input("Please pick 1: "))
if answer == 1:
    print("You are going thours the door")
else:
    print("IT'S A ROOM AND IT'S EMPTY: ")

print("...OK that room i cool and whatever but you need to make progress to escape\n"
      "1) You are going thru that nice and tempting lookin door\n"
      "2) You are looking at the empty room like a lunatic")
answer = 2
if answer == 1:
    print("You are finaly going thours the door")
else:
    print("I Had enough, you have been forced *by magical power* thourd the door")