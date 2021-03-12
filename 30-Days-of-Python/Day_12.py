# Day 12: Functions

# Exercises

# Define four functions: add, subtract, divide, and multiply. Each function should take two arguments, and they should print the result of the arithmetic operation indicated by the function name.
# When orders matters for an operation, the first argument should be treated as the left operand, and the second argument should be treated as the right operand. 
# For example, if the user passes in 6 and 2 to subtract, the result should be 4, not -4.
# You should also make sure that the user can’t pass in 0 as the second argument for divide. If the user provides 0, you should print a warning instead of calculating their division.

def add(firstvalue, secondvalue):
    print(firstvalue + secondvalue)


def subtract(firstvalue, secondvalue):
    print(firstvalue - secondvalue)


def divide(firstvalue, secondvalue):
    if secondvalue == 0:
            quit("You can't do that!")
    print(firstvalue / secondvalue)


def multiply(firstvalue, secondvalue):
    print(firstvalue * secondvalue)

# Main (input/menu)
firstvalue = int(input("Enter first value: "))
secondvalue = int(input("Enter second value: "))
userchoice = input("\nWhat operation do you wish to perform?\n1. Add\n2. Subtract\n3. Divide\n4. Multiply\nEnter choice: ")
if userchoice == "1":
    add(firstvalue, secondvalue)
elif userchoice == "2":
    subtract(firstvalue, secondvalue)
elif userchoice == "3":
    divide(firstvalue, secondvalue)
elif userchoice == "4":
    multiply(firstvalue, secondvalue)
else:
    print("Invalid input, try again.")

# Define a function called print_show_info that has a single parameter. The argument passed to it will be a dictionary with some information about a T.V. show. For example:
# The print_show_info function should print the information stored in the dictionary, in a nice way. For example:
# Breaking Bad (2008) - 5 seasons - Remember you must define your function before calling it!

tv_show = {
 	"title": "Breaking Bad",
 	"seasons": 5,
 	"initial_release": 2008
 }

def print_show_info(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} seasons")

print_show_info(tv_show)

# Below you’ll find a list containing details about multiple TV series.

series = [
 	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
 	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
 	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
 	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
 	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
 	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]

# Use your function, print_show_info, and a for loop, to iterate over the series list, and call your function once for each iteration, passing in each dictionary. 
# You should end up with each series printed in the appropriate format.

for show in series:
    print_show_info(show)

# Create a function to test if a word is a palindrome. A palindrome is a string of characters that are identical whether read forwards or backwards. For example, “was it a car or a cat I saw” is a palindrome.
# In the day 7 project, we saw a number of ways to reverse a sequence, and you can use this to verify whether a string is the same backwards as it is in its original order. You can also use a slicing approach. 
# Once you’ve found whether or not a word is a palindrome, you should print the result to the user. Make sure to clean up the argument provided to the function. We should be stripping whitespace from both 
# ends of the string, and we should convert it all to the same case, just in case we’re dealing with a name, like “Hannah”.

# Vars needed
userword = None
reverseword = None

def palindrome_check():
    userword = list(input("Enter the word you want to check: ").strip().lower())
    reverseword = userword[0:]
    reverseword.reverse()

    if reverseword == userword:
        print("That is indeed a palindrome.")
    elif reverseword is not userword:
        print("That is not a palindrome.")
    else:
        print("Something went terribly wrong, contact script author.")

palindrome_check()