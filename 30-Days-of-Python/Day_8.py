# Day 8: While Loops

# Exercises

# Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell them whether their guess was too 
# high or too low after each guess. The loop should keeping running until the user guesses the number correctly.

import random
thenumber = random.randint(0, 101)

while True: 
    guessnumber = int(input("Guess a number between 1-100: "))
    if guessnumber == thenumber:
        print("You are right, congratulations!")
        break
    elif guessnumber > thenumber:
        print("The number is too damn high!")
    elif guessnumber < thenumber:
        print("Too low!")

# Use a loop and the continue keyword to print out every character in the string "Python", except the "o". # Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one character at a time.


pythonstring = "Python"

for character in "Python":
    if character == "o":
        continue
    print(character)


# Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.
