#*****************************************************************************
# Author:       	Gayathri Iyer
# Lab:          	Sample A02
# Date:         	Jan 31, 2025
# Description:  	This program will read principal, rate, and time and
#                       calculate the simple interest for that amount.
# Input:        	option as string, the rest as integers and floats
# Output:       	Interest, totalAmount                                               
# Sources:      	Assignment 02 sample, document and lecture videos
#*****************************************************************************

#constants - None here

def main():
    #print welcome message
    print("Welcome to my Multi-Option Calculator!!")
    print()

    #declare all variables here
    option = ""
    principal = 0.0
    rate = 0.0
    period = 0
    interest = 0.0
    numMonths = 0
    monthlyPayment = 0

    #display prompts or menu and read input
    print("Please pick an option from below: ")
    print("(S) Simple Inyterest")
    print("(A) Auto Loan")
    print("(Q) Quit")
    option = input('>>')
    option = option.upper() #convert to upper case before checking
    
    if option == 'Q':
        return
    
    # input name and echo input name
    name = input("\nWhat is your name? ")
    print(f"Hello {name}! It is so nice to meet you!\n")
    
    #conditional statements for the different options
    #if option is S - since we converted to uppercase
    if option == 'S':
        #user input
        principal = float(input("\nEnter the principal amount: $"))
        rate = float(input("Enter the rate in percentage: "))
        period = int(input("Enter the period in years: "))

        #calculations for simple interest
        interest = principal * (1 +((rate / 100) * period)) - principal
        totalAmount = principal + interest

        #output to user
        print("\nYour interest accrued is $", (format(interest, '.2f')))
        print("Your total amuont with interest is $", format(totalAmount, '.2f'))
        print("Thank you for using my interest calculator!")

    #else if option is A - since we converted to uppercase
    elif option == 'A':
        #user input
        principal = float(input("\nEnter the price of the car: $"))
        rate = float(input("Enter the rate in percentage: "))
        numMonths = int(input("Enter the number of monthly payments: "))

        #monthly payment calculated
        rate = rate / 100
        monthlyPayment = (principal * (rate / 12)) / (1 - pow((1 + rate / 12), (-1 * numMonths)))

        #output to user
        print("\nYour total monthly payment is $", (format(monthlyPayment, '.2f')))
        print("Thank you for using my Auto Loan calculator!!")

    #else if neither S nor A, invalid option
    else:
        print("Invalid option!! Please try again later!!")
        

# Run the program
main()
