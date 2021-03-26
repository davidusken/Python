# Day 15: Comprehensions

# Exercises

# Convert the following for loop into a comprehension:

numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
	squares.append(number ** 2)

# Python operator ** = Exponentiation

numbers = [number ** 2 for number in numbers]

# Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the values is title case.
# Remember that iterating over a dictionary only gives us the keys by default. You can use the items method to get the keys and the values. 

movie = {
	"title": "thor: ragnarok",
	"director": "taika waititi",
	"producer": "kevin feige",
	"production_company": "marvel studios"
}

# Creating the normal loop first

movietitled = {}

for key, value in movie.items():
    movietitled.update({key: value.title()})

# Comprehension

movie = {key: value.title() for key, value in movie.items()}