import time
from random import randrange

diceAmount = None
diceRoll = None

# Start of program for easy reuse
def welcomeScreen():
    print("##########################\n####### Dice roller ######\n##########################\n\nHow many dices do you want to roll? (1-10)")
    #Fix hashtag spam
    return input("Enter: ")

diceAmount = int(welcomeScreen())

def rollConditions():
    # Condition to ensure input is valid
    if diceAmount > 1 and diceAmount < 11:
        print ("Your input is valid, proceeding...")
    else:
        print ("User input not recognized, please try again.")
    # Determine grammar 
    if diceAmount > 0 and diceAmount < 2:
        print ("Getting {0} die" .format(diceAmount))
    elif diceAmount > 1 and diceAmount < 11:
        print ("Getting {0} dice" .format(diceAmount))

rollConditions()

# Roll dice
def diceRollfunction():
    print("Rolling your dice... ")
    time.sleep(0.5)
    print("Your die rolls ", end="")
    print(randrange(6))
    return input

diceRoll = (diceRollfunction())

#End screen / rerun
rollAgain = input("Do you want to roll again? (y/n) ")
if (rollAgain == "y") or (rollAgain == "yes"):
    welcomeScreen()
    rollConditions()
    diceRollfunction()
else:
    print("Bye!")

#for i in range (diceAmount):
#    print
#else: