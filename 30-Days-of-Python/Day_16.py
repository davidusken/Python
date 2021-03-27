# First Class Functions and Lambda Expressions

# Exercises

# Use the sort method to put the following list in alphabetical order with regards to the students' names:
# You're going to need to pass in a function as a key here, and it's up to you whether you use a lambda expression, or whether you define a function with def.

students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]

def sortstudents(students):
    return students["name"]

stupidsort = sorted(students, key=sortstudents)
print(f"{stupidsort}")

# Convert the following function to a lambda expression and assign it to a variable called exp.

def exponentiate(base, exponent):
	return base ** exponent
print(exponentiate(3, 5))

exp = lambda base, exponent: base ** exponent
print(exp(3, 5)) 

# Print the function you created using a lambda expression in previous exercise. What is the name of the function that was created?

print(exp) # <function <lambda> at 0x0000014F1F8280D0>