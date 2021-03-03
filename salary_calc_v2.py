# Author: David Usken
# Program: Salary calculator v2

import math

def main():
    mainmenu()
    validOpt()
    if saltype hourly is True # Run only if salType is hourly
        hourlyInput()
    if saltype yearly is True
        yearlyInput()

# Options menu
def mainMenu():
    print("\nSelect input type for calculation:\n")
    print("1. Hourly wage\n2. Yearly salary\n")
    salType = input("Enter: ")
    salType = salType.lower()
    salType = salType.replace(".", "")

# Validate input
def validOpt():
    if (salType =="1") or (salType == "hourly") or (salType == hourly wage)
        salType = hourlyWage
        return hourlyWage
    elif (salType == "2") or (salType == "yearly") or (salType == yearly salary)
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

    #tax

    hoursPerWeek = input("Enter amount of hours per week [Default 37.5]: ")
    if len (hoursPerWeek) == 0 :
        hoursPerWeek = float(37.5)

    holidayWeeks = input("Enter how many weeks of holiday [Default 5]: ")
    if len (holidayWeeks) == 0 :
        holidayWeeks = int(5)

    holPay = input("Enter percentage [Default 12%]: ")
    if len (holPay) == 0 :
        holPay = float(0.12)

    decTax = input("Do you pay half of the normal monthly tax in December? [Y/N]")
    decTax = decTax.lower()

    if decTax = "y"
        decTax is True
    elif decTax = "n"
        decTax is False
    else:
        print("User input not recognized, try again.")

def confirmInput():

def salaryCalc():

# holpay = yearlysal * float(0.12)
# Yearly sal formula 1762 * timelønn * 0.12 - 5 uker ferie (25 * 5 * 7.5) * timelønn. # yearly - sum fra feriepengtrekk = Yearly
# worked hours per year with 5 weeks of holiday = 1950 - 5 ferie uker 1762 (kalkuler, 5 dager per ferieuke mindre. )

def timeOrFixed():
    typeSalary = input ("Time based or fixed salary?\nEnter: ")
    typeSalary = typeSalary.lower()

    if (typeSalary == "time based") or (typeSalary == "time"):
        typeSalary = time
        return typeSalary

    elif (typeSalary == "fixed salary") or (typeSalary == "fixed"):
        typeSalary = fixed
        return typeSalary

def output(): 
    #table brutto/netto/feriepenger/skatt/netto per mnd (halv dec)

### Improvements 
# Lønnsoppgjør beregning fra %

main()