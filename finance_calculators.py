import math
#Defining the mode of desired calculation mode
#".lower()" is used to force the input into lower case for compatibility
print("'investment' mode to calculate interest earned on investments.")
print("'bond' mode to calculate interest generated from home loan.")
user_mode = input("Enter mode: ")
mode = user_mode.lower()

#Block for defining variables in investment calculations
if mode == "investment":
    deposit = float(input("How much ar you investing? "))
    interest_rate_input = float(input("What is the interest rate % (whole number)?"))
    interest_rate = float(interest_rate_input / 100)
    length = float(input("How long are you planning to invest for (in years)?"))
    interest_input = str(input("Simple or Compound Interest?"))
    interest_type = interest_input.lower()
#Seperate calculations for types of investment interests
    if interest_type == "simple":
        simple_interest = deposit*(1 + (interest_rate) * length)
        print("Simple Interest gained: ", simple_interest)
    elif interest_type == "compound":
        compound_interest = deposit * math.pow((1 + interest_rate), length)
        print("Compound interest gained: ", compound_interest)

#Block for defining variables in bonds calculation
if mode == "bond":
    house_value = int(input("Enter present value of house: "))
    interest_rate = int(input("What is the interest rate % (whole number)?"))
    repay_months = int(input("How many months do you plan to repay the bond over?"))
    monthly_rate = float((interest_rate / 100) / 12)
#Bonds interest calculation 
    repayment_calculation = float(monthly_rate * house_value) / (1 - (monthly_rate / 100)**(repay_months))
    repayment = round(repayment_calculation, 2)
    print("You will have to pay ", repayment, " each month.")
#Prints anything that's neither "investments" or "bonds".
else:
    print("Invalid input. Please try again.")
