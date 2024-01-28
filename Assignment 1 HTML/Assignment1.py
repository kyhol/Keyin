# Description: Creating an invoice for rented car
# Author: Kyle Hollett
# Date:  Jan 11, 2024


# Constants
RATE_PER_DAY = 55.00
RATE_PER_MILE = 0.24
DISCOUNT_DAY = .10 
DISCOUNT_MILE = .25 
HST_RATE = .15 
RATE_INSUR= 14


# Start the main Program
# Gather user inputs
#Personal Data
print()
CustName = input("Enter customer name: ")
CustPhone = input("Enter 10 digit customer phone number: IE(9999999999): ")
print()
NumDaysRented = input("Enter number of days rented: ")
NumDaysRented = int(NumDaysRented)
OdomStart = input("Enter odometer start amount - IE(99900): ")
OdomStart = int(OdomStart)
OdomFin = input("Enter odometer finish amount - IE(99999): ")
OdomFin = int(OdomFin)

#Calculations

TotalTravel = (OdomFin - OdomStart)
DayCost = NumDaysRented * RATE_PER_DAY
MileCost = TotalTravel * RATE_PER_MILE
InsurCost = NumDaysRented * RATE_INSUR
RentCost = DayCost + MileCost
TotalDiscountMile = MileCost * DISCOUNT_MILE
TotalDiscountDay = DayCost * DISCOUNT_DAY
TotalCost = RentCost + InsurCost + DayCost
DiscountAdd = TotalDiscountDay + TotalDiscountMile 
TotalCostPlD = TotalCost - DiscountAdd
HST = TotalCostPlD * HST_RATE
FinalInvoice = TotalCostPlD + HST

#Printed personal details + values
# Display results 

print()
print()
print("Customers name:               ", CustName)
print("Customers phone number        ", CustPhone)
print()
print("Number of days rented:        ",NumDaysRented)
print("Odometer miles start:         ",OdomStart)
print("Odometer miles finish:        ",OdomFin)
print("Total travel distance:    (mi)",TotalTravel)
print()
print("Price per day:               $",RATE_PER_DAY)
print("Price per mile:              $",RATE_PER_MILE)
print("Price of insurance per day:  $",RATE_INSUR)
print()
print("Discount per day(s):         %",DISCOUNT_DAY)
print("Discount per mile(s):        %",DISCOUNT_MILE)
print()
print("Total day cost:              $",DayCost)
print("Total mile cost:             $",MileCost)
print("Total insurance cost:        $",InsurCost)
print("Total rent cost:             $",RentCost)
print()
print("Amount saved from miles:     $",TotalDiscountMile)
print("Amount saved from days:      $",TotalDiscountDay)
print("Total amount Amount saved:   $",DiscountAdd)
print()
print("Total cost before tax        $",TotalCost)
print("Total cost with discount:    $",TotalCostPlD)
print()
print("HST Rate:                    %",HST_RATE)
print("HST amount:                  $",HST)
print()
print("Final amount to be paid      $",FinalInvoice)
print()
print()
print()

