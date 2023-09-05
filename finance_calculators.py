import math
#Explain the difference between the investment and bond calculations and request one to be input, save input as upper
#Use if, elif and else options to indicate option chosen and give user a chance to re-enter if they did not input correct options
#If investment has been chosen, request input of the amount of deposit, interest%, simple or compound interest.
#Output the amount they will have 
#If the user selects bond, request input of present value, interest rate, number of months.
#Determine the amount that has to be paid every month and print for the user to see.

print("Good day and thank you for choosing Midas Investment Funds.")
print("")

print("There are two options of calculations to choose from, please see below:")
print("")

print("Investment - To calculate the amount of interest you will build from your investment.")
print("Bond - To calculate the amunt you will have to pay monthly on a home loan.")
print ("")

calculation = input("Please type in one of the two options as mentioned above.  Investment or Bond: ").upper()
print("")

if calculation == "INVESTMENT":
    print("You have chosen investment.")

elif calculation == "BOND":
    print("You have chosen bond")

else:
    calculation = input("Sorry!  We don't recognise your entry.  Please try again and use either the words investment or bond: ").upper()
    if calculation == "INVESTMENT":
        print("You have chosen investment.")
    elif calculation == "BOND":
        print("You have chosen bond.")

if calculation == "INVESTMENT":
    deposit = float(input("Please enter the amount of money you would like to deposit with us in Rand: R"))
    interest = float(input("Please enter the number of the percentage of interest: "))
    years = float(input("Please enter the number of years you would like to invest with us: "))
    type_interest = input("Please type in one of the options for the type of interest you would like to use, Simple or Compound: ").upper()
    if type_interest == "SIMPLE":
        amount = round(deposit * (1 + interest / 100 * years), 2)
        print("")
        print(f"After {years} years, you will have made R{amount} with simple interest.")
    elif type_interest == "COMPOUND":
        amount = round(deposit * math.pow((1 + interest/100), years), 2)
        print("")
        print(f"After {years} years, you will have made R{amount} with compound interest.")

elif calculation == "BOND":
    value = float(input("Please enter the current value of the asset in Rand: R"))
    interest = float(input("Please enter the number of percentage of the interest rate: "))
    months = int(input("Please enter the number of months in which you would like to pay off the bond: "))
    monthly_interest = (interest/100)/12
    repay = round(((monthly_interest * value) / (1 -(1 + monthly_interest) ** (-months))), 2)
    print("")
    print(f"You will need to repay R{repay} over {months} months.")

print("Thank you for your time and have a nice day.")

#1.Hyperiondev,2021.
#1.Hyperiondev.2021. The String Data Type. Reviewed on 5 March 2023. https://www.dropbox.com/s/8jw4mngir51rwns/DS%20L1T05%20-%20The%20String%20Data%20Type.pdf?dl=0
#2.Hyperiondev, 2021.
#2.Hyperiondev. 2021. Capstone Project 1- Variables and Control Structures. Reviewed on 5 March 2023. https://www.dropbox.com/s/6ox0x43sm04ujse/DS%20L1T11%20-%20Capstone%20Project%20I%20-%20Variables%20and%20Control%20Structures.pdf?dl=0


