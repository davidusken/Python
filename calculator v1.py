import time

print("What do you wish to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("Enter: ") 
operationChoice = input()

if (operationChoice == "1") or (operationChoice == "1.") or (operationChoice == "Add") or (operationChoice == "add"):
    print("Enter the first number you want to add")
    addNumberA = input()
    print ("Ok, and the second one?")
    addNumberB = input()
    sum = int (addNumberA) + int (addNumberB)
    print ("Performing extreme calculations...")
    time.sleep(1)
    print ("The sum of {0} + {1} is {2}" .format(addNumberA, addNumberB, sum))

elif (operationChoice == "2") or (operationChoice == "2.") or (operationChoice == "Subtract") or (operationChoice == "subtract"):
    print("Enter the first number you want to subtract")
    addNumberA = input()
    print ("Ok, and the second one?")
    addNumberB = input()
    sum = int (addNumberA) - int (addNumberB)
    print ("Performing extreme calculations...")
    time.sleep(1)
    print ("The sum of {0} - {1} is {2}" .format(addNumberA, addNumberB, sum))

elif (operationChoice == "3") or (operationChoice == "3.") or (operationChoice == "Multiply") or (operationChoice == ("multiply")):
    print("Enter the first number you want to multiply")
    addNumberA = input()
    print ("Ok, and the second one?")
    addNumberB = input()
    sum = int (addNumberA) - int (addNumberB)
    print ("Performing extreme calculations...")
    time.sleep(1)
    print ("The sum of {0} * {1} is {2}" .format(addNumberA, addNumberB, sum))

elif (operationChoice == "4") or (operationChoice == "4.") or (operationChoice == "Divide") or (operationChoice == "divide"):
    print("Enter the first number you want to divide")
    addNumberA = input()
    print ("Ok, and the second one?")
    addNumberB = input()
    sum = int (addNumberA) - int (addNumberB)
    print ("Performing extreme calculations...")
    time.sleep(1)
    print ("The sum of {0} divided by {1} is {2}" .format(addNumberA, addNumberB, sum))      
else:
    print("User input not recognized, please try again.")

### Future improvements:
# Add squaring as a operation
# Easter egg for special numbers
# Allow text input from user e.g (52 * 12) + 90 / 3