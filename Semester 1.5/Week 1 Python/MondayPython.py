#Description:
#Author: 
#Date:

#Define Libraries

#Define Constants

#Define Program Functions

def DetLetterGrade(NumGrade):
    #Determine and return letter grade

    if NumGrade >= 80:
        LetterGrade = "A"
    elif NumGrade >= 70 and NumGrade <= 79:
        LetterGrade = "B"
    elif NumGrade >= 60 and NumGrade <= 69:
        LetterGrade = "C"
    elif NumGrade >= 50 and NumGrade <= 59:
        LetterGrade = "D"
    else:
        LetterGrade = "F"
    
    return LetterGrade


def CalcWeekGrossPay(Hours, PayRate):
    #Determine and return the weekly gross pay
    #Based on hours worked and hourly pay rate

    if Hours <= 40:
        GrossPay = Hours * PayRate
    else: 
        RegPay = PayRate * 40 
        OTPay = (Hours - 40) * (PayRate * 1.5)
        GrossPay = RegPay + OTPay
    
    return GrossPay


# Main Program 
while True:

    #Inputs
    NumGrade = input("Enter the numeric grade (0 - 100): ")
    NumGrade = int(NumGrade)
    
    HoursWorked = 35
    HourlyPayRate = 15.00

    #Calculations
    LetterGrade = DetLetterGrade(NumGrade)
    WeeklyGrossPay = CalcWeekGrossPay(HoursWorked, HourlyPayRate)

    #Display results
    print(LetterGrade)
    print(WeeklyGrossPay)





#HouseKeeping duties