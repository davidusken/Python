# Day 17: Flexible Functions with *args and **kwargs

# Exercises

# Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. Remember that we can use the sum function to add the values in an iterable.

def myfunct(*numbers):
    numbers = sum(numbers)
    print(numbers)

myfunct(32, 32, 64, 128, 512)

# Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.

def kwargfunct(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

kwargfunct(1,  "blue",  [1,  23,  3], height=184,)

# Print the following dictionary using the format method and ** unpacking.

country = {
 	"name": "Germany",
 	"population": "83 million",
 	"capital": "Berlin",
 	"currency": "Euro"
 }

country_template = "{name}, {population}, {capital}, {currency}"

print(country_template.format(**country))

# Using * unpacking and range, print the numbers 1 to 20, separated by commas. You will have to provide an argument for print function's sep parameter for this exercise.

print(*range(0, 21), sep=",")

# Modify your code from exercise 4 so that each number prints on a different line. You can only use a single print call.

print(*range(0, 21), sep="\n")