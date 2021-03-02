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

# User input
def userInput():
    hourlyWage = input("Enter your hourly wage: ")
    # Verify that input is int format
    while hourlyWage.isnumeric() is False:
        print("User input not recognized, please try again.")
        hourlyWage = input("Enter your hourly wage: ")

    typeSalary = input ("Time based or fixed salary?\nEnter:")
    typeSalary = typeSalary.lower()

    if (typeSalary == "time based") or (typeSalary == "time"):
        print("Confirming your hourly wage is {0} and you are on a time based salary" .format(hourlyWage))
        print("Calculating salary...")
        salaryCalc(hourlyWage)
        time.sleep(1)
        timebasedSalOut()

    elif (typeSalary == "fixed salary") or (typeSalary == "fixed"):
        print("Confirming your hourly wage is {0} and you are on a fixed salary" .format(hourlyWage))
        print("Calculating salary...")
        salaryCalc(hourlyWage)
        time.sleep(1)
        fixedSalOut()

# Calculations
def salaryCalc(hourlyWage):
    # Find monthly salary
    global monthlySal
    monthlySal = float (hourlyWage) * 37.5 * 4

    # Find yearly salary
    global yearlySal 
    yearlySal = int (hourlyWage) * 1695

    # Find feriepenger
    global feriePeng 
    feriePeng = float (yearlySal) * 0.12

# Months with feriepenger july, 0 june
def timebasedSalOut():
        print("Your yearly salary is {0}\nYour monthly salary is {1}\nEstimated feriepenger {2}\n" .format (yearlySal, monthlySal, feriePeng))
        print("January: {0}" .format(monthlySal))
        print("February: {0}" .format(monthlySal))
        print("March: {0}" .format(monthlySal))
        print("April: {0}" .format(monthlySal))
        print("May: {0}" .format(monthlySal))
        juneSal = (monthlySal + feriePeng)
        print("June: {0}" .format(juneSal + feriePeng))
        print("July: {0}" .format(monthlySal))
        print("August: {0}" .format(monthlySal))
        print("September: {0}" .format(monthlySal))
        print("October: {0}" .format(monthlySal))
        print("November: {0}" .format(monthlySal))
        print("December: {0}" .format(monthlySal))

# Months with feriepenger june, normal july
def fixedSalOut():
        print("Your yearly salary is {0}\nYour monthly salary is {1}\nEstimated feriepenger {2}\n" .format (yearlySal, monthlySal, feriePeng))
        print("January: {0}" .format(monthlySal))
        print("February: {0}" .format(monthlySal))
        print("March: {0}" .format(monthlySal))
        print("April: {0}" .format(monthlySal))
        print("May: {0}" .format(monthlySal))
        print("June: {0}" .format(feriePeng))
        print("July: {0}" .format(monthlySal))
        print("August: {0}" .format(monthlySal))
        print("September: {0}" .format(monthlySal))
        print("October: {0}" .format(monthlySal))
        print("November: {0}" .format(monthlySal))
        print("December: {0}" .format(monthlySal))

userInput()