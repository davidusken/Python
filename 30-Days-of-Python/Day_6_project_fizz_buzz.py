# Day 6 Project: Fizz Buzz

# For our version, we're only going to have a single player, the computer, and it's going to play the first 100 rounds of Fizz Buzz all by itself.
# In order to complete this exercise, you're going to need to use loops, and you can generate your list of numbers using range. 
# You're also going to need conditionals, and you're going to need be able to check if something is divisible by 3 or 5.
# For this last part, you can use an operator called modulo, which uses the percent symbol (%). Modulo will give you the remainder of a division, 
# so if a number is divisible by 3, the value of number % 3 will be 0.

print("Welcome to the Fizz Buzz game!")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0: 
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)