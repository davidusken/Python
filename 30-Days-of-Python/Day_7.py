# Day 7: split, join, and Slices

# Exercises

# Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, and then assign each name to a different variable. 
# For this exercise, you can assume that the user has a single given name and a single surname.

fullname = input("Enter your name and surname: ")
fullname = fullname.title()
firstname = fullname.split()[0]
surname = fullname.split()[1]

print(f"Your first name is {firstname} and your surname is {surname}")

# Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.

numbers = [1, 2, 3, 4, 5]
strnumbers = []

for number in numbers:
	strnumbers.append(str(number))

print(" | ".join(strnumbers))

# Below you’ll find a short list of quotes. Each quote is a string, but each string actually contains quote characters at the start and end. 
# Using slicing, extract the text from each string, without these extra quote marks, and print each quote.

quotes = [
 	"'What a waste my life would be without all the beautiful mistakes I've made.'",
 	"'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
 	"'The very essence of romance is uncertainty.'",
 	"'We are not here to do what has already been done.'"
 ]

for quote in quotes:
	print(f"{quote[1:-1]}")

# You may also want to try a solution using strip.

for quote in quotes:
	print(quote.strip("'"))


# Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace in the user’s input, 
# so you’re going to have to process the string before you find its length.

word = input("Enter a word: ").strip()
wordlength = len(word)

print(f"You entered the word '{word}' this word has a length of '{wordlength}'")

# If you want to take this a little bit further, you an ask the user for a long piece of text. 
# You can then tell them how many how many characters are in the text overall, and you can also provide them a word count.

longtext = input("Enter a long piece of text: ")
characters = len(longtext)

convtolist = longtext.split()
wordcount = len(convtolist)

print(f"The text you entered has a total of {characters} characters, and a word count of {wordcount}.")