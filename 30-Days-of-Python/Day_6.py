# Day 6: For Loops

# Exercises

# Below we've provided a list of tuples, where each tuple contains details about an employee of a shop: their name, the number of hours worked last week, and their hourly rate. 
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

# Print how much each employee is due to be paid at the end of the week in a nice, readable format.
for i in employees:
    print(f"{i[0]} is due to be paid {i[1] * i[2]} at the end of the week.")

# For the employees above, print out those who are earning an hourly wage above average.
# Hint: you can use a for loop and two variables to keep track of the total wage and the number of employees. Then, use the two variables to calculate the average. 
avgwage = (employees[0][2] + employees[1][2] + employees[2][2] + employees[3][2]) / 4
print("The average wage is: " + str(avgwage))

for employee in employees:
    if employee[2] > int(avgwage):
        print(f"{employee[0]} earns more than average.")