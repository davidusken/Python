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
    print("Enter the first number you want to add: ", end="")
    addNumberA = input()
    print ("Ok, and the second one: ", end="")
    addNumberB = input()
    sum = int (addNumberA) + int (addNumberB)
    print ("Performing extreme calculations...")
    time.sleep(1)
    print ("The sum of {0} + {1} is {2}" .format(addNumberA, addNumberB, sum))

elif (operationChoice == "2") or (operationChoice == "subtract"):
    print("Enter the first number you want to subtract: ", end="")
    subNumberA = input()
    print ("Ok, and the second one: ", end="")
    subNumberB = input()
    sum = int (subNumberA) - int (subNumberB)
    print ("Performing extreme calculations...")
    time.sleep(1)
    print ("The sum of {0} - {1} is {2}" .format(subNumberA, subNumberB, sum))

elif (operationChoice == "3") or (operationChoice == ("multiply")):
    print("Enter the first number you want to multiply: ", end="")
    mulNumberA = input()
    print ("Ok, and the second one: " , end="")
    mulNumberB = input()
    sum = int (mulNumberA) * int (mulNumberB)
    print ("Performing extreme calculations...")
    time.sleep(1)
    print ("The sum of {0} * {1} is {2}" .format(mulNumberA, mulNumberB, sum))

elif (operationChoice == "4") or (operationChoice == "divide"):
    print("Enter the first number you want to divide: ", end="")
    divNumberA = input()
    print ("Ok, and the second one: ", end="")
    divNumberB = input()
    sum = int (divNumberA) / int (divNumberB)
    print ("Performing extreme calculations...")
    time.sleep(1)
    print ("The sum of {0} divided by {1} is {2}" .format(divNumberA, divNumberB, sum))      

else:
    print("User input not recognized, please try again.")
    operationChoice = choice_function()