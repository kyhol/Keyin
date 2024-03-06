BASE_SALARY = 350.00
SALES_QUATA = 5000.00
COMMISSION_RATE = 0.04
COMISSION= 0

# Description:Write a function that will calculate the gross pay based on a base salary plus 
#commission based on a draw against commission. NOTE – a draw against commission 
#is when an employee does not meet their sales quota and the base salary is deducted 
#based on a percentage under the quota. 
#All employees earn a base salary of $350.00 and have a sales quota of $5,000.00. If 
#their sales are below the quota, calculate 10% of the amount they are under and 
#subtract it from the base salary. If they have exceeded their quota calculate the 
#commission at 4% of sales and add it to their base salary. In addition, if the employee 
#has sales more than $10,000.00 add an extra $200.00 to the gross pay. If the 
#employee has sales more than $20,000.00, add an extra $500.00 to the gross pay.
# Author: kyle hollett  
# Date:2024-03-04

# Define Libraries

# Define Constants
BASE_SALARY = 350.00
SALES_QUATA = 5000.00
COMMISSION_RATE = 0.04
COMISSION= 0
# Define Program Functions
GrossPay = 350
def calc_gross_pay(BaseSalary, Sales, GrossPay):
    GrossPay = BASE_SALARY
    if Sales < SALES_QUATA:
        Deduction = 0.10 * (SALES_QUATA - Sales)
        GrossPay -= Deduction
    else: 
        Comission = COMMISSION_RATE * Sales
        GrossPay += Comission
        if Sales > 20000.00:
            GrossPay += 500.00
        elif Sales > 10000.00:
            GrossPay += 200.00
    return GrossPay
# Main Program 
Sales = input("Enter amount of sales: ")
Sales = int(Sales)

    #Inputs


    #Calculations
GrossPay = calc_gross_pay(BASE_SALARY,Sales, GrossPay )
print(f"{GrossPay}")
    #Display results





# HouseKeeping duties