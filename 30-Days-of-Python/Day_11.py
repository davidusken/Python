# Day 11: Sets

# Exercises

# Create an empty set and assign it to a variable.

bmw5series = {"E12", "E28", "E34", "E39"}
print(bmw5series)

# Add three items to your empty set using either several add calls, or a single call to update.

bmw5series.update(["E60", "F10", "G30"])
print(bmw5series)

# Create a second set which includes at least one common element with the first set.

bmwclassics = {"E28", "E39", "E9", "E46"}
print(bmwclassics)

# Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.

print(bmw5series.union(bmwclassics)) # {'E28', 'E60', 'E34', 'E9', 'E12', 'G30', 'E46', 'E39', 'F10'}
print(bmw5series.symmetric_difference(bmwclassics)) # {'E34', 'E12', 'F10', 'E46', 'E60', 'G30', 'E9'}
print(bmw5series.intersection(bmwclassics)) # {'E28', 'E39'}

# Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.
# If you want an extra challenge, also tell the user if their number was too high or too low.

seq = range(37-74)
guess = int(input("Enter guess: "))

if guess > 37 and guess < 74:
    print("Wow you rock!")
elif guess < 37:
    print("Too low!")
elif guess > 74:
    print("Too high!")