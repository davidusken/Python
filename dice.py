from random import randrange

diceAmount = None

# Start of program for easy reuse
def welcomeScreen():
    print("##########################\n####### Dice roller ######\n##########################\n\nHow many dices do you want to roll? (1-10)")
    #hashtag spam should be replaced by for loops (26 characters)
    return input("Enter: ")

diceAmount = int(welcomeScreen())

# Condition to ensure input is valid
if diceAmount > 1 and diceAmount < 11:
    print ("Your input is valid, proceeding...")
else:
    print ("User input not recognized, please try again.")

# Determine grammar 
if diceAmount > 0 and diceAmount < 2:
    print ("Very well, getting {0} die" .format(diceAmount))
elif diceAmount > 1 and diceAmount < 11:
    print ("Very well, getting {0} dice" .format(diceAmount))

# Roll
print("Rolling your first dice ", end="")
print(randrange(6))