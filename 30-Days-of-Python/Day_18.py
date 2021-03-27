# Day 18: Imports

# Exercises

# Import the fractions module and create a Fraction from the float 2.25. You can find information on how to create fractions in the documentation.

from fractions import Fraction

print(Fraction(2.25))

# Import only the fsum function from the math module and use it to find the sum of the following series of floats:

numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]

from math import fsum

print(fsum(numbers))

# Import the random module using an alias, and find a random number between 1 and 100 using the randint function. You can find documentation for this function here.

import random as rand

print(rand.randint(0, 101))

# Use the randint function from the exercise above to create a new version of the guessing game we made in day 8. This time the program should generate a random number, and you should tell the user whether their guess was too high, or too low, until they get the right number.

randomnum = rand.randint(0, 101)
print(randomnum)

while True:
    guessed_num = int(input("Guess a number between 0 - 100: "))
    if guessed_num > randomnum:
        print("Too high!")
    elif guessed_num < randomnum:
        print("Too low!")
    elif guessed_num == randomnum:
        print("Congratulations, you guessed it!")
    else:
        print("Something went wrong.")