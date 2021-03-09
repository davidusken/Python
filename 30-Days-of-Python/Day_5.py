# Day 5: Conditionals and Booleans

# Exercises

# Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.
a = 5

print(a == 5)
print(id(a))

print(a is 5)
print(id(a))

# Try to use the is operator or the id function to investigate the difference between this:
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

print("\nTask 2")
print(numbers == new_numbers)
print(id(numbers))
print(id(new_numbers))
print(numbers is new_numbers)

# And this:
# Are new_numbers and numbers the same thing? What about numbers before and after we append 5?
numbers = [1, 2, 3, 4]

print(id(numbers))
print(numbers)
numbers.append(5)
print(id(numbers))
print(numbers)

# Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
number = int(input("Enter a number: "))

if number > 0:
    print("Your number is positive.")
elif number < 0:
    print("Your number is negative.")
elif number == 0:
    print("Your number is zero.")
else:
    print("Something went wrong, try again.")

# Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
# If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. 
# The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. In effect, the employees get paid 110% of their hourly wage for any overtime.
hoursworked = int(input("Enter amount of hours worked this week: "))
hourlywage = int(input("Enter your hourly wage: "))

if hoursworked > 40:
    print("You have worked more than 40 hours this week and will get some additional pay.")
    overtimewage = hourlywage * float(0.10) + hourlywage
    dueamount = hoursworked * overtimewage
    overtime = (hoursworked - 40) * overtimewage
    print("The amount due is " + str(dueamount))
    print("Your hourly wage on overtime is " + str(overtimewage))
    print("Of this sum the overtime makes up a total of: " + str(overtime))
elif hoursworked < 40:
    print("You have worked less than 40 hours this week, so you will get paid a normal salary.")
else:
    print("Something went wrong, try again.")