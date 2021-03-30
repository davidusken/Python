# Day 20: map, filter, and Conditional Comprehensions

# Exercises

# Use map to call the strip method on each string in the following list:
# Print the lines of the nursery rhyme on different lines in the console.
# Remember that you can use the operator module and the methodcaller function instead of a lambda expression if you want to.

humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",  
	"    Couldn't put Humpty together again."
]

from operator import methodcaller

humpty_dumpty_strip = map(methodcaller("strip"), humpty_dumpty)
print(*humpty_dumpty_strip, sep="\n")


#Below you'll find a tuple containing several names:

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")

# Use a list comprehension with a filtering condition so that only names with fewer than 8 characters end up in the new list. Make sure that every name in the new list is in title case.

def namelength(names):
    return len(names)

for name in names:
    if namelength > 8 == 0

#shorternames = filter

print(namelength(names))
#names = filter[]
print(names)

# Use filter to remove all negative numbers from the following range: range(-5, 11). Print the remaining numbers to the console.