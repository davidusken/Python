# Day 13: Scope and Returning Values from Functions

# Exercises

# Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise the base to. 
# The function should return the result of this operation. Remember we can perform exponentiation using the ** operator.

numA = 0
numB = 0

def exponentiate(numA, numB):
    numA = int(input("Enter first number: "))
    numB = int(input("Enter second number: "))
    return numA ** numB

print(exponentiate(numA, numB))

# Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, and has had any excess whitespace removed.

string = None

def process_string(string):
    string = input("Enter a string: ")
    return string.lower().strip()

print(process_string(string))


# Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. The data should be in the following format: 
# ("Tom Hardy", "English", 42) name, nationality, age. You can choose whatever key names you like for the dictionary.

def actor_register():
    name = input("Enter name: ").strip().title()
    nationality = input("Enter nationality: ").strip().title()
    age = input("Enter age: ").strip()

    add_author = {
        "name": name,
        "nationality": nationality,
        "age": age
    }
    return add_author

print(actor_register())

# Write a function that takes in a single number and returns True or False depending on whether or not the number is prime. 
# If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series.

def primechecker():
    num = int(input("Enter a number: "))
    for i in range(2, num//2):
        if (num % i) == 0:
            return False
    return True 

print(primechecker())