import random

ask = input("Do you want to roll the dice?\n")
if(ask):
    while True:
            diceNumbers = [1,2,3,4,5,6]
            if(ask=='yes'):
                diceNumber = random.choice(diceNumbers)
                print("You rolled: " + str(diceNumber))
                askWantToRoll = input("Do you want to roll the dice again?\n")
            elif(ask=="no"):
                break
else:
    print("Ok, you do not want to roll.")