import time
import random

def mainRoller():
    print("##########################\n####### Dice roller ######\n##########################\n\n")
    diceAmount = int(getDiceAmount())
    while rollConditions(diceAmount) is False: 
        diceAmount = int(getDiceAmount())
    rollAmount(diceAmount)
    rollAgain = input("Do you want to roll again? (y/n) ")
    if (rollAgain == "y") or (rollAgain == "yes"):
        mainRoller()
    else:
        print("Bye!")

# Start of program for easy reuse
def getDiceAmount():
    print("How many dice do you want to roll? (1-10)")
    #Fix hashtag spam
    return input("Enter: ")

def rollConditions(diceAmount):
    # Condition to ensure input is valid
    if diceAmount > 1 and diceAmount < 11:
        print ("Your input is valid, proceeding...")
        # Determine grammar
        if diceAmount > 0 and diceAmount < 2:
            print ("Getting {0} die" .format(diceAmount))
        elif diceAmount > 1 and diceAmount < 11:
            print ("Getting {0} dice" .format(diceAmount))
        return True
    else:
        print ("User input not recognized, please try again.")
        return False

# Roll dice
def diceRollfunction():
    print("Rolling your dice... ")
    time.sleep(0.5)
    print("Your die rolls ", end="")
    print(random.randrange(6))

# Roll amount
def rollAmount(amount):
    for i in range (amount):
        diceRollfunction()

mainRoller()