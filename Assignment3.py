#Project 3–PythonHonest  Harry  owns  a  used  car  lot  and  would  like  a  program  to  keep  track  of  his  sales.    Follow  good programming practise  using Comments,  Constants, and Spacing. The program will repeat until the user enters the word “END” for the Customer First Name. The invoice date is the current system date.Input  for  the  program  will  be  the customer  first  name(must  be  entered –adjust  to  title  case), the customer last name (must be entered –adjust to title case), the phone number (must be entered -must be 10 digits), the plate number (must be entered –must be 6 characters -convert to all caps –BONUS: entered in the format XXX999), the car make(ie: Toyota), the car model (ie: Corolla), the year(ie: 2018), the selling price  (does  not exceed $50,000.00), the amount of the trade  in (does not exceed the selling price), and the salespersons name.NOTE:Validation is only required on the fields as specified.The program should calculate the price after trade, the licence fee, the transfer fee, the HST, Subtotal, and the total sales price. The price after trade is the selling price less the trade in amount.  The licence fee is standard rate in NL of $75.00 on cars up to and including $5,000.00 and $165.00 on cars over $5,000.00.  The transfer fee 1% of the selling price -if the selling price is more than $20,000.00, an additional 1.6% luxury tax is calculated on the selling price and added to the transferfee. The Subtotal is the Price after trade plus the License Fee plus the Transfer Fee.  Taxes (HST) are calculated at 15% on the Subtotal.   The total sales price is the subtotal plus the HST.   Display results based on the following guidelines: Customer name is the first initial and the last name, the second line is the street address, and the third line is the City, Province and Postal Code.  Car Details are the Year, Make and Model –ie: 2014 Toyota Corolla. The program should create a Receipt ID for the sale in the form XX-XXX-XXXX where the first two characters are the customer initials, the middle 3 characters are the last 3 digits in the license plate number, and the final 4 characters are the last 4 digits of the phone number.  The payment schedule uses a loop based on the number of years the customer will use to pay off the car.  For each of 4 years, calculate the number of monthly payments (Years * 12), the financing fee at 39.99 per year, the total price as the total sales price plus the financing fee, and the monthly payment (The Total Price divided by the number of months).  The first payment date is 30 days from the purchase date.  NOTE :This will allow the user to decide on payment options.

#Description: Creating a receipt for Honest Harry and his used car lot.
#Author: Kyle Hollett
#Date 2024-02-08
#Imports

import datetime

#Constants

FINANCING_FEE = 39.99 
YEAR_ONE = 1
YEAR_TWO = 2 
YEAR_THREE = 3
YEAR_FOUR = 4
LICENCE_FEE_UPTO_5000_RATE = 75.00
LICENCE_FEE_OVER_5000_RATE = 165.00
OVER_UNDER_5000 = 5000.00
HST_RATE = 0.15
TRANSFER_FEE = 0.01
OVER_UNDER_20000 = 20000
LUXURY_TAX = 0.016
SELL_PRICE_MAX = 50000
END = "End"

#Main Program
#Inputs and Valadations
#include Current System Date 

while True:
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
    while True:
        FirstName = input("Enter customers first name(Or END to end the program): ").title()
        if FirstName == "":
            print("Data Entry Error - Customers first name cannot be blank.")
            print("Try again")
        elif set(FirstName).issubset(allowed_char) == False:
            print("Data Entry Error - Customers first name contains invalid characters.")
            print("Try again")
        else:
            break
    if FirstName == END:
        print("Exiting the program")
        break
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
    while True:
        LastName = input("Enter customers last name: ").title()
        if LastName == "":
            print("Data Entry Error - Customers last name cannot be blank.")
            print("Try again")
        elif set(LastName).issubset(allowed_char) == False:
            print("Data Entry Error - Customers last name contains invalid characters.")
            print("Try again")
        else:
            break
    allowed_char = set("1234567890")
    while True:
        PhoNum = input("Enter the customers 10 digit phone number: ")
        if len(PhoNum) != 10:
            print("Data Entry Error - The number has to contain 10 digits")
            print("Try again")
        elif set(PhoNum).issubset(allowed_char) == False:
            print("Data Entry Error - Your number contains invalid characters")
            print("Try again")
        else: 
            break
    StreetName = input("Enter customers Street address: ").title()
    Province = input("Enter province initials (ie: NL): ").upper()
    City = input("Enter the city name: ").title()
    PostalCode = input("Enter customers postal code: (IE A1B-3G6)").upper()

    allowed_char = ("ABCDEFGHIJKLMNOPQRSTUVWXZ")
    allowed_num = ("1234567890")
    while True:
        PlateNum = input("Enter the customers license plate number (LLL999): ").upper()        
        if len(PlateNum) != 6:
            print("Data Entry Error - Customers license plate number must be 6 digits.")
            print("Try again")
        elif PlateNum == "":
            print("Data Entry Error")
        elif set(PlateNum[0:3]).issubset(allowed_char) == False:
            print("Data Entry Error - First 3 characters must be letters.")
            print("Try again")
        elif set(PlateNum[3:6]).issubset(allowed_num) == False:
            print("Data Entry Error - Last 3 characters must be numbers.")
            print("Try again")
        else:
            PlateNum = PlateNum[0:3] + "" + PlateNum[3:6]
            break
        
    CarMake = input("Enter the make of the car (ie: Toyota): ").title()
    CarModel = input("Enter the car model (ie: Corolla): ").title()
    CarYear = input("Enter the year the car was made (ie: 2018): ")
    SalesPersonName = ("Enter the sales persons name: ").title()
    

    allowed_num = ("1234567890,.")

    while True: 
        SellPrice = input("Input sell price: (ie:8000): ")
        try:
            SellPrice = float(SellPrice)
        except: 
            SellPrice > SELL_PRICE_MAX
            print("Data Entry Error: You cannot exceed 50,000 in sell price.")
            print("Try again")
        else:
            break
    allowed_num = ("1234567890,.")    
    while True: 
        TradeInValue = input("Enter trade in value: (ie:8000$): ")
        try:
            TradeInValue = float(TradeInValue)
        except: 
            TradeInValue > SellPrice
            print("Data Entry Error: Trade in value cannot exceed the selling price.")
        else:
            break

    PriceAfterTrade = SellPrice - TradeInValue
    if  SellPrice <= OVER_UNDER_5000:
        LicenseFee = LICENCE_FEE_UPTO_5000_RATE #possible error
    else:
        LicenseFee = LICENCE_FEE_OVER_5000_RATE #possible error

    if  SellPrice > OVER_UNDER_20000:
        LuxuaryTax = SellPrice * LUXURY_TAX
    else:
        LuxuaryTax = 0
        
    TransferFee = (SellPrice * TRANSFER_FEE) + LuxuaryTax

    HST = (PriceAfterTrade + LicenseFee + TransferFee) * HST_RATE
    SubTotal = PriceAfterTrade + LicenseFee + TransferFee
    TotalSalesPrice = SubTotal + HST

    for Year in range(1, 5):
        NumMonth = Year * 12 
        FFee = FINANCING_FEE * Year
        TotPrice = TotalSalesPrice + FFee
        Monthly = TotPrice / 12

CurrentYear = datetime.date.today()
CurrentDate = datetime.date.today()

#DSP conversion
CurrentYearDsp = CurrentYear.strftime("%y")
InvoiceDateDsp = CurrentDate.strftime("%d-%m-%y")
FirstPayment = CurrentDate + datetime.timedelta(days=30)
FirstPaymentDsp = FirstPayment.strftime("%d-%m-%y")
CustName = FirstName + " " + LastName
FirstInitial = FirstName[0]
LastInitial = LastName[0]
ReceiptID = FirstInitial + LastInitial + "-" + PlateNum[3:6] + "-" + PhoNum[-4:]
CustomerName = FirstInitial + "." + " " + LastName
CurrentDateDsp = CurrentDate.strftime("%B %d, %Y")
SellPriceDsp = "{:,.2f}".format(SellPrice)
TradeInValueDsp = "{:,.2f}".format(TradeInValue)
PriceAfterTradeDsp = "{:,.2f}".format(PriceAfterTrade)
LicenseFeeDsp = "{:,.2f}".format(LicenseFee)
TransferFeeDsp = "{:,.2f}".format(TransferFee)
LuxuaryTaxDsp = "{:,.2f}".format(LuxuaryTax)
HSTDsp = "{:,.2f}".format(HST)
SubtotalDsp = "{:,.2f}".format(SubTotal)
TotalSalesPriceDsp = "{:,.2f}".format(TotalSalesPrice)

#Display 78 long
print()
print(f"Honest Harry Car Sales                           Invoice Date: {CurrentDateDsp}")
print(f"Used Car Sale and Receipt                        Receipt No:         {ReceiptID:>11s}")
print()
print(f"                                              Sales price:            ${SellPriceDsp:>9s}")
print(f"Sold to:                                      Trade Allowance:        ${TradeInValueDsp:>9s}")
print("                                              ----------------------------------")
print(f"     {CustomerName:<18s}                       Price after Trade:      ${PriceAfterTradeDsp:>9s} ")
print(f"     {StreetName:<18s}                       License Fee:            ${LicenseFeeDsp:>9s}")
print(f"     {City:<18s}, {Province:<2s}  {PostalCode:<6s}           Transfer Fee:           ${TransferFeeDsp:>9s}")
print("                                              ----------------------------------")
print(f"Car Details:                                  Subtotal:               ${SubtotalDsp:>9s}")
print(f"                                              HST:                    ${HSTDsp:>9s}")
print(f"     {CarYear:<4s} {CarMake:<18s} {CarModel:<10s}       ----------------------------------")
print(f"                                              Total sales price:      ${TotalSalesPriceDsp:>9s}")
print("--------------------------------------------------------------------------------")
print()
print("                                   Financing     Total     Monthly")
print("         # Years     # Payments       Fee        Price     Payment")
print("         ------------------------------------------------------------        ")
for Year in range(1, 5):
    NumMonth = Year * 12 
    FFee = FINANCING_FEE * Year
    TotPrice = TotalSalesPrice + FFee
    Monthly = TotPrice / 12
    NumMonthDsp = "{:<6}".format(NumMonth)
    FFeeDsp = "{:<10.2f}".format(FFee)
    TotPriceDsp = "{:<10.2f}".format(TotPrice)
    MonthlyDsp = "{:<10.2f}".format(Monthly)
    print(f"             {Year}           {NumMonthDsp}      {FFeeDsp} {TotPriceDsp} {MonthlyDsp}")
print("         ------------------------------------------------------------        ")
print(f"         Invoice date: {InvoiceDateDsp:<9s}         First Payment Date: {FirstPaymentDsp:<9s} ")
print() 
print("--------------------------------------------------------------------------------")
print("                   Best used cars at the best prices!")
    
    # Display results based on the following guidelines: Customer name is the first initial and the last name, the second line is the street address, and the third line is the City, Province and Postal Code.  Car Details are the Year, Make and Model –ie: 2014 Toyota Corolla. The program should create a Receipt ID for the sale in the form XX-XXX-XXXX where the first two characters are the customer initials, the middle 3 characters are the last 3 digits in the license plate number, and the final 4 characters are the last 4 digits of the phone number.  The payment schedule uses a loop based on the number of years the customer will use to pay off the car.  For each of 4 years, calculate the number of monthly payments (Years * 12), the financing fee at 39.99 per year, the total price as the total sales price plus the financing fee, and the monthly payment (The Total Price divided by the number of months).  The first payment date is 30 days from the purchase date.  NOTE :This will allow the user to decide on payment options.       

#The licence fee is standard rate in NL of $75.00 on cars up to and including $5,000.00 and $165.00 on cars over $5,000.00.  The transfer fee 1% of the selling price -if the selling price is more than $20,000.00, an additional 1.6% luxury tax is calculated on the selling price and added to the transferfee. The Subtotal is the Price after trade plus the License Fee plus the Transfer Fee.  Taxes (HST) are calculated at 15% on the Subtotal.   The total sales price is the subtotal plus the HST. 

 #Project 3–PythonHonest  Harry  owns  a  used  car  lot  and  would  like  a  program  to  keep  track  of  his  sales.    Follow  good programming practise  using Comments,  Constants, and Spacing. The program will repeat until the user enters the word “END” for the Customer First Name. The invoice date is the current system date.Input  for  the  program  will  be  the customer  first  name(must  be  entered –adjust  to  title  case), the customer last name (must be entered –adjust to title case), the phone number (must be entered -must be 10 digits), the plate number (must be entered –must be 6 characters -convert to all caps –BONUS: entered in the format XXX999), the car make(ie: Toyota), the car model (ie: Corolla), the year(ie: 2018), the selling price  (does  not exceed $50,000.00), the amount of the trade  in (does not exceed the selling price), and the salespersons name.NOTE:Validation is only required on the fields as specified.The program should calculate the price after trade, the licence fee, the transfer fee, the HST, Subtotal, and the total sales price. The price after trade is the selling price less the trade in amount.   

#LastName = input("Enter customers last name: ").title
#PhoNum = input("Enter customers phone number: ").isdigit

#if PhoNum != 10 
##Outputs
#
#Copy Paste stuff: invoice_date_dsp = datetime.datetime.strftime(invoice_date, "%B %d, %Y")
# Invoice Date: {invoice_date_dsp:>}

