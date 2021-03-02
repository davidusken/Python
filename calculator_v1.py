import time

operationChoice = None 

def choice_function():
    print("What do you wish to do?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("Enter: ", end="")
    return input()

operationChoice = choice_function() 
operationChoice = operationChoice.lower()
operationChoice = operationChoice.replace(".", "")

if (operationChoice == "1") or (operationChoice == "add"):
    addNumberA = input("Enter the first number you want to add: ")
    addNumberB = input("Ok, and the second one: ")
    sum = int (addNumberA) + int (addNumberB)
    print ("Performing extreme calculations...")
    time.sleep(1)
    print ("The sum of {0} + {1} is {2}" .format(addNumberA, addNumberB, sum))
elif (operationChoice == "2") or (operationChoice == "subtract"):
    subNumberA = input("Enter the first number you want to subtract: ")
    subNumberB = input("Ok, and the second one: ")
    sum = int (subNumberA) - int (subNumberB)
    print ("Performing extreme calculations...")
    time.sleep(1)
    print ("The sum of {0} - {1} is {2}" .format(subNumberA, subNumberB, sum))
elif (operationChoice == "3") or (operationChoice == ("multiply")):
    mulNumberA = input("Enter the first number you want to multiply: ")
    mulNumberB = input("Ok, and the second one: ")
    sum = int (mulNumberA) * int (mulNumberB)
    print ("Performing extreme calculations...")
    time.sleep(1)
    print ("The sum of {0} * {1} is {2}" .format(mulNumberA, mulNumberB, sum))
elif (operationChoice == "4") or (operationChoice == "divide"):
    divNumberA = input("Enter the first number you want to divide: ")
    divNumberB = input("Ok, and the second one: ")
    sum = int (divNumberA) / int (divNumberB)
    print ("Performing extreme calculations...")
    time.sleep(1)
    print ("The sum of {0} divided by {1} is {2}" .format(divNumberA, divNumberB, sum))      
else:
    print("User input not recognized, please try again.")
    operationChoice = choice_function()