# Author: David Usken
# Program: Salary calculator based on hourly wage

import math
import time

# Assumptions
# 37.5 hours per week
# 0.12% feriepenger
# 5 weeks holiday
# Årsverk 1695 timer
# No 50% dec tax
# 4 weeks of holiday in july

# Main function
def mainCalculator():
    userInput()

# User input
def userInput():
    hourlyWage = input("Enter your hourly wage: ")
    # Verify that input is int format
    while hourlyWage(int) is True
    
    typeSalary = input ("Time based or fixed salary?\n Enter:")
    typeSalary = typeSalary.lower()

    if (typeSalary == time based) or (typeSalary == time)
        print("Confirming your hourly wage is {0} and you are on a time based salary" .format(hourlywage))
        print("Calculating salary...")
        salaryCalc()
        time.sleep(1)
        timebasedSalOut()

    elif (typeSalary == fixed salary) or (typeSalary == fixed)
        print("Confirming your hourly wage is {0} and you are on a fixed salary" .format(hourlywage))
        print("Calculating salary...")
        salaryCalc()
        time.sleep(1)
        fixedSalOut()
    else: 
        print("User input not recognized, please try again.")

# Calculations
def salaryCalc():
    # Find monthly salary
    monthlySal = sum() = int (hourlyWage) * int (37.5)

    # Find yearly salary
    yearlySal = sum() = int (hourlyWage) * int (1695)

    # Find feriepenger
    feriePeng = sum() = int (yearlySal) * int (0.12)

# Months with feriepenger july, 0 june
def timebasedSalOut(timebasedSalOut):
        print("Your yearly salary is {0}\n Your monthly salary is {1}\n Estimated feriepenger {2}\n" .format (yearlySal, monthlySal, feriePeng))
        print("January: {0]" .format(monthlySal))
        print("February: {0]" .format(monthlySal))
        print("March: {0]" .format(monthlySal))
        print("April: {0]" .format(monthlySal))
        print("May: {0]" .format(monthlySal))
        print("June: {0]" .format(monthlySal))
        print("July: {0]" .format(feriePeng))
        print("August: {0]" .format(monthlySal))
        print("September: {0]" .format(monthlySal))
        print("October: {0]" .format(monthlySal))
        print("November: {0]" .format(monthlySal))
        print("December: {0]" .format(monthlySal))

# Months with feriepenger june, normal july
def fixedSalOut(fixedsalOut):
        print("Your yearly salary is {0}\n Your monthly salary is {1}\n Estimated feriepenger {2}\n" .format (yearlySal, monthlySal, feriePeng))
        print("January: {0]" .format(monthlySal))
        print("February: {0]" .format(monthlySal))
        print("March: {0]" .format(monthlySal))
        print("April: {0]" .format(monthlySal))
        print("May: {0]" .format(monthlySal))
        juneSal = sum(monthlySal + Feriepeng)
        print("June: {0]" .format(juneSal))
        print("July: 0" .format(monthlySal))
        print("August: {0]" .format(monthlySal))
        print("September: {0]" .format(monthlySal))
        print("October: {0]" .format(monthlySal))
        print("November: {0]" .format(monthlySal))
        print("December: {0]" .format(monthlySal))