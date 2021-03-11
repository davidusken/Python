# Day 9: Unpacking, Enumeration, and the zip Function

# Exercises

# Below is some simple data about characters from BoJack Horseman. The data contains the character name, the voice actor or actress who plays them, and the species of the character.
# Write a for loop that uses destructuring so that you can print each tuple in the following format: BoJack Horseman is a horse voiced by Will Arnet.
# Note that you're going to have to change the species information to lowercase when you print it. If you need a reminder on how to do this, we covered it in day 3 of the first week.

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for character, act, species in main_characters:
    print(f"{character} is a {species.lower()} voiced by {act}")

# Unpack the following tuple into 4 variables. The data represents a student's name, their student id number, and their major and minor disciplines in that order.

("John Smith", 11743, ("Computer Science", "Mathematics"))

name, studid, (major, minor) = ("John Smith", 11743, ("Computer Science", "Mathematics"))
print(f"\nName: {name}\nStudent ID{str(studid)}\nMajor discipline: {major}\nMinor discipline: {minor}\n")

# Investigate what happens when you try to zip two iterables of different lengths. For example, try to zip a list containing three items, and a tuples containing four items.

food = ["bread", "fish", "lamb"]
drinks = ["coca cola", "redbull", "litago", "lettmelk"]

food_and_drinks = zip(food, drinks)

# Convert to list because it's lazy and only calculates next value when requested. 
print(list(food_and_drinks)) # [('bread', 'coca cola'), ('fish', 'redbull'), ('lamb', 'litago')]

# Results = it ignores the 4th (lettmelk) item because nothing can be paired with it