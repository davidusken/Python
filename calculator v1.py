import time

print("What do you wish to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("Enter: ") 
operationChoice = input()

if operationChoice == "1":
    print("Enter the first number you want to add")
    addNumberA = input()
    print ("Ok, and the second one?")
    addNumberB = input()
    sum = int (addNumberA) + int (addNumberB)
    print ("Performing extreme calculations...")
    time.sleep(3)
    print ("The sum of {0} + {1} is {2}" .format(addNumberA, addNumberB, sum))
    ### OLD
    #print ("The answer is ", sum)
    #print ("The answer is " + (int(addNumberA)) + (int(addNumberB)))
else:
    print("Done")
### Future improvements:
# Allow user to write out choice instead of using number, non case sensitive.
# Add squaring as a operation
# Easter egg for special numbers