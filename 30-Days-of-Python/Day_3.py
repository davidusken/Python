# Day 3: Formatting Strings and Processing User Input

# Exercises

# Using the variable below, print "Hello, world!". You can add the missing exclamation mark using string concatenation, format, or f-strings. The choice is yours.
greeting = "Hello, world"

# String concatenation 
print(greeting + "!")

# Format
excmark = "!"
print("{0}{1}".format(greeting, excmark))

# f-string
fstringex = f"{greeting}!"
print(fstringex)

# Ask the user for their name, and then greet the user, using their name as part of the greeting. The name should be in title case, and shouldn't be surrounded by any excess white space.
# For example, if the user enters "lewis ", your output should be something like this:
# Hello, Lewis!

name = input("Enter your name: ")
print("Hello, " + name.capitalize().strip() + "!")

# Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".
# Remember that we can only concatenate strings to other strings, so you will have to convert the integer to a string before you can perform the concatenation.

print("I am " + str(29))

# Format and print the information below using string interpolation. The output should look like this:
# Joker (2019), directed by Todd Phillips

title = "Joker"
director = "Todd Phillips"
release_year = 2019

print(title + "(" + str(release_year) + "), " + "directed by " + director)