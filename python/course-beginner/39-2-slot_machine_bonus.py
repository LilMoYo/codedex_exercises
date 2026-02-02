
import random

symbols = [
    '🍒',
    ' 🍇', 
    '🍉', 
    '7️⃣'
    ]

def play():
    play_in = input("Would you like to play? (y/n) ")
    if play_in == "y":
        results = random.choices(symbols, k=3)
        win = results[0] == "7️⃣" and results[1] == "7️⃣" and results[2] == "7️⃣"
        
        if win:
            print(f"{results[0]} | {results[1]} | {results[2]}")
            print("--------")
            print("YOU WIN!")
            print("--------")
        else:
            print(f"{results[0]} | {results[1]} | {results[2]}")
            print("You lose!")
            
            while win != True:
                play_again()
    else:
        print("Have a great day!")

def play_again():
    play_in2 = input("Would you like to play, again? (y/n) ")
    if play_in2 == "y":
        results = random.choices(symbols, k=3)
        print(f"{results[0]} | {results[1]} | {results[2]}")
        if results[0] == "7️⃣" and results[1] == "7️⃣" and results[2] == "7️⃣":
            print("--------")
            print("YOU WIN!")
            print("--------")
        else:
            print("You lose!")
    else:
        print("Have a great day!")
        exit()
play()
