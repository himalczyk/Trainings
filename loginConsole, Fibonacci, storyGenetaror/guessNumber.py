import random
print("Welcome to the number guessing game!\n")
number = random.randint(0, 100)
guessNumber = input("I am thinking of a number from 0 to 100, try guessing the right one :)\n")

def tryAgain():
    guess = input("Try again!\n")
    return guess


while True:
    if(int(guessNumber) > int(number)):
        print("Unlucky, that is not the correct one, try lower :)\n")
        guessNumber = tryAgain()
    elif(int(guessNumber) < int(number)):
        print("Unlucky, that is not the correct one, try higher :)\n")
        guessNumber = tryAgain()
    if(int(guessNumber) == int(number)):
        print("Congrats! Number: " +str(guessNumber) + "\n" + "That is the correct one!\n")
        break