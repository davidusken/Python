# Author: David Usken
# Program: Salary calculator v2
# Dependencies: tabulate - https://pypi.org/project/tabulate/

import math
import time
from tabulate import tabulate

def main():
    mainMenu()
    validOpt()
  #  if saltype hourly is True # Run only if salType is hourly
       # hourlyInput()
   # if saltype yearly is True
       # yearlyInput()
    print(salType)

# Options menu
def mainMenu():
    print("\nSelect input type for calculation:\n")
    print("1. Hourly wage\n2. Yearly salary\n")
    global salType
    salType = input("Enter: ")
    salType = salType.lower()
    salType = salType.replace(".", "")
    return salType

# Validate option 
def validOpt(salType):
    if (salType =="1") or (salType == "hourly") or (salType == "hourly wage"):
        salType = hourlyWage
        return hourlyWage
    elif (salType =="2") or (salType == "yearly") or (salType == "yearly salary"):
        salType = yearlySal
        return yearlySal
    else:
        print("User input not recognized, try again.")

# Called when option 1. Hourly wage
def hourlyInput():
    print ("What is your hourly wage?")
    hourlyWage = input("Enter: ")
    while hourlyWage.isnumeric() is False:
        print("User input not recognized, try again.")
        print ("What is your hourly wage?")
        hourlyWage = input("Enter: ")

# Called when option 2. Yearly salary
def yearlyInput():
    print ("What is your yearly salary?")
    yearlySal = input("Enter: ")
    while yearlySal.isnumeric() is False:
        print("User input not recognized, try again.")
        print ("What is your hourly wage?")
        hourlyWage = input("Enter: ")

# Called when above conditions are met
def miscInput():

    timeOrFixed()

    taxPerc = input("Enter how much you pay in taxes [Default 33%]: ")
    if len (taxPerc) == 0 :
        taxPerc = float(33)

    hoursPerWeek = input("Enter amount of hours per week [Default 37.5]: ")
    if len (hoursPerWeek) == 0 :
        hoursPerWeek = float(37.5)

    vacWeeks = input("Enter how many weeks of vacation [Default 5]: ")
    if len (vacWeeks) == 0 :
        vacWeeks = int(5)

    holPay = input("Enter percentage [Default 12%]: ")
    if len (holPay) == 0 :
        holPay = float(0.12)

    decTax = input("Do you pay half of the normal monthly tax in December? [Y/N]")
    decTax = decTax.lower()

    if decTax == ("y"):
        decTax is True
    elif decTax == ("n"):
        decTax is False
    else:
        print("User input not recognized, try again.")

def confirmInput():
    print("""You entered the following information:\n
    You want to base your calculations on a {} basis\n
    Your wage\salary {} is per hour\year\n
    You work a total of {} hours per week.\n 
    You have a total of {vacWeeks}weeks of vacation\n 
    Your holiday pay is {} % of your yearly income\n 
    You pay 50% less tax in December (if true) \n")
    input("Press ENTER to continue or ESC to restart""" .format)

def salaryCalc():

# Info collected so far: calc choice, time or fixed, tax, hours per week, vacation weeks, holiday pay, december tax
# Weekly salary is needed for accurate sum to deduct from amount of vacation weeks taken

# Yearly sal formula 1762 * timelønn * 0.12 - 5 uker ferie (25 * 5 * 7.5) * timelønn. # yearly - sum fra feriepengtrekk = Yearly
# Worked hours per year with 5 weeks of holiday = 1950 - 5 ferie uker 1762 (kalkuler, 5 dager per ferieuke mindre. )

# Calculate yearly salary using hourly wages
if hourlySal is True
    yearlySal = float(hourlySal) * 1762
else:
    quit()

# Calculate hourly wages using yearly salary
if yearlySal is True:
    hourlySal = float(yearlySal) / 1762
else:
    quit()

# Calculate holiday pay
holPaySum = int(yearlySal) * float(holPay)

# Calculate monthly salary
monthlySal = float(hourlySal) * float(162.5)

# Calculate weekly salary
weeklySal = float(hourlySal) * float(37.5)

# Calculate daily salary
dailySal = float(hourlySal) * float(7.5)

# Wages per minute
wageMinute = float(hourlySal) / int(60)

# Wages per second
wageSecond = float(hourlySal) / int(3600)

# Calculate December tax
if decTax is True:
    decTax = (float(decSal)) * 0.33) * 0.50
    decSal = (float(decSal)) - (float(decTax))
else:
    quit()
    
def timeOrFixed():
    typeSalary = input ("Time based or fixed salary?\nEnter: ")
    typeSalary = typeSalary.lower()

    if (typeSalary == "time based") or (typeSalary == "time"):
        typeSalary = time
        return typeSalary

    elif (typeSalary == "fixed salary") or (typeSalary == "fixed"):
        typeSalary = fixed
        return typeSalary

# Tabulate library for table print

grossSalJan = None
netSalJan = None
taxJan = None

def output(): 

    grossSalJan = int(15000)
    netSalJan = int(10000)
    taxJan = int(5000)
    
    table = [["January",grossSalJan,netSalJan,taxJan],["February",0,0,0],["March",0,0,0]]
    headers = ["Gross salary", "Net salary", "Tax"]

    print(tabulate(table, headers, tablefmt="pretty"))


tabledict = {
    'Month': []
    'Net salary': []
    'Gross salary': []
    'Tax' : []
}

def addMonthData(datalist,tabledict):
    i = 0
    for list in tabledict:
        list.append(datalist[i])
        i += 1
    return tabledict

# Print new table with yearlysal\feriepeng\total tax

# Condition if time based output sal\holpay june, if fixed output only holpay june

#def moreOutput():
    #input("Do you want more details? [Y/N]")
    #print("Very well, generating some more details...")
    #time.sleep(1)

### Improvements 
# Lønnsoppgjør beregning fra %
# Add moreOutput as an option after confirming details and before printing output. Should include weekly pay, daily pay, hourly pay, minute pay and pay per second.
# If time based, check how it will vary from month to month

main()