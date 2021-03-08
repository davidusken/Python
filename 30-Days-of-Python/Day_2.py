# Day 2: Strings, Variables, and Getting Input from Users

# Exercises
# Now that we’ve covered how to use strings, variables, and the input function, it’s time to practice with some exercises.

# Ask the user for their name and age, assign theses values to two variables, and then print them.

age = input("Enter your age: ")
name = input("Enter your name: ")

print("Hi, {0} just confirming we got your name right, and that your age is {1}.".format (name, age))

# Investigate what happens when you try to assign a value to a variable that you’ve already defined. Try printing the variable before and after you reuse the name.

boxes = 5
print(boxes)

boxes = 100
print(boxes)

# Below you’ll find some code with a number of errors. Try to go through the program line by line and fix the issues in the code. I’d encourage you to try running the program while you’re working on it, as reading the error messages is great practice for debugging your own programs.

hourly_wage = input("Please enter your hourly wage: ")
print("Hourly wage: ")
print(hourly_wage)

hours_worked = input("How many hours did you work this week? ")
print("Hours worked: ")
print(hours_worked)