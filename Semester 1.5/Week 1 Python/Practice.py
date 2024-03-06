#For each of the following, write a function that can be used for the required calculations. 
#Test each function by setting up a calling statement with possible values. 

#6. Write a function that will accept a Purchase date as a parameter and return payment 
#date as the first day of the next month. If the day of the month is 25 or greater, add 
#an extra month. For example, is the date is 2022-02-14 then return 2022-03-01. 
#However, if the date is 2022-02-26 then return 2022-04-01.

#7. Write a function that will calculate the gross pay based on a base salary plus 
#commission based on a draw against commission. NOTE – a draw against commission 
#is when an employee does not meet their sales quota and the base salary is deducted 
#based on a percentage under the quota. 
#All employees earn a base salary of $350.00 and have a sales quota of $5,000.00. If 
#their sales are below the quota, calculate 10% of the amount they are under and 
#subtract it from the base salary. If they have exceeded their quota calculate the 
#commission at 4% of sales and add it to their base salary. In addition, if the employee 
#has sales more than $10,000.00 add an extra $200.00 to the gross pay. If the 
#employee has sales more than $20,000.00, add an extra $500.00 to the gross pay. 

#8. Write a function that will determine the customer status. The status will be “OK” if 
#the customer is under their credit limit, “CHECK” if they are not over but within 
#$200.00 of the credit limit, and “OVER” if they are over their credit limit. If the number 
#of days since the last purchase is more than 60 days concatenate the word – PURCH 
#(including the -) to the status. If the number of days since the last payment is more 
#than 30 days add the text – PAY to the status. For a bad customer the status may 
#read OVER – PURCH – PAY. Return the Status and determine required parameters.

#9. This might look familiar from the Midterm Sprint. The bonus is calculated based on 
#the following: If the number of days is more than 3 add $100.00 to the bonus. If the 
#kilometers are over 1000 and the salesperson used their own car, add an extra 4 cents 
#per kilometer to the bonus. If the claim type is Executive add an extra $45.00 per day 
#to the bonus. Finally, if the start date is between Dec 15 and Dec 22 add an extra 
#$50.00 per day to the bonus.

#10. Think of another function that could be useful to you in your code. As with the others, 
#code the function, then in the main program call and test the function.


#6. Write a function that will accept a Purchase date as a parameter and return payment 
#date as the first day of the next month. If the day of the month is 25 or greater, add 
#an extra month. For example, is the date is 2022-02-14 then return 2022-03-01. 
#However, if the date is 2022-02-26 then return 2022-04-01.


# Define Libraries

import datetime

# Define Constants


# Define Program Functions
def get_payment_date(PurchaseDateStr):
    PurchaseDate = datetime.datetime.strptime(PurchaseDateStr, "%Y-%m-%d")
    day = PurchaseDate.day
    month = PurchaseDate.month
    year = PurchaseDate.year
    if day >= 25:
        month += 2
    else:
        month += 1

    if month > 12:
        month -= 12
        year += 1

    return datetime.datetime(PurchaseDateStr).strftime("%Y-%m-%d")

PurchaseDateStr = 2020-10-10

# Main Program 
PurchaseDateDsp = get_payment_date(PurchaseDateStr)
    #Inputs

    #Calculations


    #Display results
print(f" PurchaseDate: {PurchaseDateStr}")




# HouseKeeping duties


#Write a function that will calculate the gross pay based on a base salary plus 
#commission based on a draw against commission. NOTE – a draw against commission 
#is when an employee does not meet their sales quota and the base salary is deducted 
#based on a percentage under the quota. 
#All employees earn a base salary of $350.00 and have a sales quota of $5,000.00. If 
#their sales are below the quota, calculate 10% of the amount they are under and 
#subtract it from the base salary. If they have exceeded their quota calculate the 
#commission at 4% of sales and add it to their base salary. In addition, if the employee 
#has sales more than $10,000.00 add an extra $200.00 to the gross pay. If the 
#employee has sales more than $20,000.00, add an extra $500.00 to the gross pay. 

#BASE_SALARY = 350
#SALES_QUOTA = 5000
#
#def GrossPay(Sales):
#
#    if Sales < SALES_QUOTA
#        AmountDeduct = (SALES_QUOTA - Sales) * .10 
#        AmountPaid = BASE_SALARY - AmountDeduct
#    elif
#        Sales >= SALES_QUOTA
#        Bonus = Sales + 
#
#Sales = input("Enter sales: ")

