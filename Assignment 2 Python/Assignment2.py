#Description: Creating a receipt for St. John’s Marina&Yacht Club program. - To better help them keep track of what's going on. 
#Author: Kyle "Table Flipper" Hollett
#Date 2024-01-25

#Constants
TOTAL_SITES = 100 #redundant (edit - Could use for loop if TOTAL_SITES > 100 then repeat statement? 
HST_RATE = 0.15
EVEN_NUM_SITE_RATE = 80.00
ODD_NUM_SITE_RATE = 120.00
ADD_MEM_RATE = 5
WEEKLY_CLEAN_RATE = 50
SURVEILLANCE_RATE = 35
STD_MEM_RATE = 75
EXEC_MEM_RATE = 150
CANCELATION_RATE = .6
PROCESS_FEE_RATE = 59.99

# Start the main program
#User Inputs

NewOrE =               input("Is this a new or Existing member?(N for New E for existing):      ").upper()
if NewOrE == "N":
    MemberName =       input("Enter New Members Name:                                           ").title()
else: 
    MemberName =       input("Enter Existing Members Name:                                      ").title()
         
CurrentDate =          input("Enter the current date (YYYY-MM-DD):                              ")
SitePosition =         input("Enter Boats Site Position (1-100):                                ")
SitePosition = int(SitePosition)          
StAd =                 input("Enter Members Street Address:                                     ").title()
City =                 input("Enter Members City:                                               ") #Want use .title to capatialize but it would captialize the S after ' in St John's
Province =             input("Enter Members Provience Name  (LL):                               ").upper()
PostalCode =           input("Enter Members Postal Code - (L9L9L9):                             ").upper()
HomeNum =              input("Enter Members Home Number (9999999999):                           ")
CellNum =              input("Enter Members Cell Number (9999999999):                           ")
MemType =              input("Enter Membership type (S for standard, E for Executive):          ").upper()
AltMemb =              input("Enter the number of alternate members:                            ")
AltMemb = int(AltMemb)
WeeklyClean =          input("Does The Member Want Weekly Site Cleaning? (Y for yes, N for no): ").upper()
VideoSurveillance =    input("Does The Member Want Video Surveillance?   (Y for yes, N for no): ").upper()

#Calculations

if SitePosition % 2 == 0:
    SiteCharge = EVEN_NUM_SITE_RATE
else: 
    SiteCharge = ODD_NUM_SITE_RATE

if WeeklyClean == "Y":
    WeeklyClean = WEEKLY_CLEAN_RATE
    CleanMsg = "Yes"
else: 
    WeeklyClean = 0
    CleanMsg = "No"
if VideoSurveillance == "Y":
    VideoSurveillance = SURVEILLANCE_RATE
    SurvMsg = "Yes"
else:
    VideoSurveillance = 0
    SurvMsg = "No"


AltMemCharge = AltMemb * ADD_MEM_RATE #possibly needs fix: FIXED

SiteAltSubTotal = SiteCharge + AltMemCharge

ExtraCharges = SURVEILLANCE_RATE + WEEKLY_CLEAN_RATE

SAESubTotal = SiteAltSubTotal + ExtraCharges

HST = SAESubTotal * HST_RATE

MonthlySAEWithHst = SAESubTotal + HST

if MemType == "S":
    MonthlyMemFee = STD_MEM_RATE * AltMemb
    FullMemType = "Standard"
else:
    MonthlyMemFee = EXEC_MEM_RATE * AltMemb
    FullMemType = "Executive"


SAEAndMMFee = MonthlySAEWithHst + MonthlyMemFee

#Finally monthly  dues  are  calculated  at $75.00  for standard members  and $150.00  for executive  #members.The total monthly   charge   andthe   monthly   duesare added together #to givethe Total Monthly Fees

#The total monthly   charge   andthe   monthly   duesare added together to givethe Total Monthly Fees
TotYearCost = SAEAndMMFee * 12
#Also  determine  the  total  Yearly  Fees  by  multiplying the  total  #monthly  fees  by  12.
TotMonthPayment = (TotYearCost + 59.99) / 12
#The  monthly  payment is  the  Total  yearly  fees,  plus  a  processing  fee  of $59.99  divided  by  12.
YearlySiteCharge = SiteAltSubTotal * 12

CancelFee = YearlySiteCharge * .6 

#Outputs

print()
print( "     St. John's Marina & Yacht Club     ")
print( "         Yearly Member Receipt          ")
print()
print()
print( "-----------------------------------------")
print()
print( "Client Name and Address:")
print()
print(f"{MemberName:<24s}                           ") 
print(f"{StAd:<24s}                                 ")
print(f"{City:<15s}, {Province:<2s} {PostalCode:>6s}")
print(f"Phone: {HomeNum:<10s}(H)")
print(f"       {CellNum:<10s}(C)")
print()
SitePositionDsp = "{:}".format(SitePosition)
print(f"Site #: {SitePositionDsp:<3s}        Member type:{FullMemType:>9s}")
print()
AltMembDsp = "{:}".format(AltMemb)
print(f"Alternate members:                    {AltMembDsp:>2s}")
print(f"Weekly site cleaning:                {CleanMsg:>3s}")
print(f"Video surveillance:                  {SurvMsg:>3s}")
print()
SiteAltSubTotalDsp = "{:,.2f}".format(SiteAltSubTotal)
print(f"Site charges:                  ${SiteAltSubTotalDsp:>8s}")
ExtraChargesDsp = "{:,.2f}".format(ExtraCharges)
print(f"Extra charges:                 $ {ExtraChargesDsp:>7s}")
print("                               ----------")
SAESubTotalDsp = "{:,.2f}".format(SAESubTotal)
print(f"Subtotal:                      ${SAESubTotalDsp:>8s}")
SalesTaxDsp = "{:,.2f}".format(HST)
print(f"Sales Tax (HST):               $ {SalesTaxDsp:>7s}")
print("                               ----------")
MonthlySAEWithHstDsp = "{:,.2f}".format(MonthlySAEWithHst)
print(f"Total monthly charges:         ${MonthlySAEWithHstDsp:>8s}") 
MonthlyMemFeeDsp = "{:,.2f}".format(MonthlyMemFee)
print(f"Monthly dues:                  ${MonthlyMemFeeDsp:>8s}")
print("                               ----------")
SAEAndMMFeeDsp = "{:,.2f}".format(SAEAndMMFee)
print(f"Total monthly fees:            ${SAEAndMMFeeDsp:>8s}")
TotYearCostDsp = "{:,.2f}".format(TotYearCost)
print(f"Total yearly fees:            ${TotYearCostDsp:>9s}")
print()
TotMonthPaymentDsp = "{:,.2f}".format(TotMonthPayment)
print(f"Monthly Payment:               ${TotMonthPaymentDsp:>8s}")
print()
print( "-----------------------------------------")
print()
print(f"Issued: {CurrentDate:<10s}                              ")
print( "HST RegNo: 549-33-5849-4720-9885                        ")
CancelFeeDsp = "{:,.2f}".format(CancelFee)
print(f"Cancelation Fee:               ${CancelFeeDsp:>8s}")
print()


#Copy Reference - increases efficiency 
#Dsp = "{:,.2f}".format()

#Reminders 
#- Dsp
#% 2 == 0:
#.upper .title .lower
#Love yourself

#Feedback from Last Assignemnt: 

#Lose the IE in the prompts - just the pattern is fine.

#Total cost before taxes is high - you added extra things.

#Put the % signs at the end of the rate.
