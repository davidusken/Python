# Day 19: Exception Handling

# Exercises

# Create a short program that prompts the user for a list of grades separated by commas. Split the string into individual grades and use a list comprehension to convert each string to an integer. You should use a try statement to inform the user when the values they entered cannot be converted.

grades = input("Enter a list of grades separated by commas: ").split(",")

try:
    grades = [int(grade) for grade in grades]
    print(grades)
except ValueError:
    print("Invalid input format!")

# Investigate what happens when there is a return statement in both the try clause and finally clause of a try statement.

def func():
    try:
        resulttry = 2 + 2
        print("Correct")
        return resulttry
    finally:
        result = 3 + 3
        print("Finally correct")
        return result

print(func()) # 6

# Imagine you have a file named data.txt with this content: "There is some data here!""
# Open it for reading using Python, but make sure to use a try block to catch an exception that arises if the file doesn't exist. Once you've verified your solution works with an actual file, delete the file and see if your try block is able to handle it.

try:
    with open("data.txt", "r") as file:
        data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found!")