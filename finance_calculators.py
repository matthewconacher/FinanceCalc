#This program performs financial calculations
#
#There is a investment calculator which can calculate simple and compound interest
#
#There is also a loan calculator which can calculate monthly repayments

import math

#print the menu showing the two options to choose
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("investment    - to calculate the amount of interest you'll earn on interest")
print("bond          - to calculate the amount you'll have to pay on a home loan\n")

#get the input and convert to all upper case
choice = input().upper()

#based on the input perform the investment OR the bond calc

if (choice == "INVESTMENT"):
    #ask the user for the details of their investment
    invest_amount = float(input("Please enter the amount you would like to invest: "))          
    interest_rate = float(input("Please enter the interest rate in %: "))                       
    invest_years = int(input("Please enter the number of years you will invest for: "))         
    interest = input("Please enter if you would like a 'simple' or 'compound' calculation: ").upper()   
    
    if (interest == "SIMPLE"): #for simple interest

        A = invest_amount * ((1 + (interest_rate/100)) * invest_years)
        
        print("Your investment will be worth £" + str(round(A,2)))
        
    elif (interest == "COMPOUND"): #for compound interest

        A = invest_amount * math.pow((1 + (interest_rate/100)), invest_years)

        print("Your investment will be worth £" + str(round(A,2)))
        
elif (choice == "BOND"):
    #ask user for the details of their loan
    present_value = float(input("What is the present value of your house?: "))                  
    annual_interest = float(input("What is the annual interest rate of the loan?: ")) / 100   
    months_to_repay = int(input("How many months do you plan to repay over?: "))                

    #calcuate monthly interest based on input annual interest
    monthly_interest = annual_interest / 12                                                                             
    
    x = (monthly_interest * present_value) / (1 - (math.pow((1 + monthly_interest), -months_to_repay)))
    
    print("Your monthly repayment will be £" + str(round(x,2)))
else:
    print("Please enter a valid choice")

    
