#import time
#start_time = time.time()

# the outstanding balance on the credit card
balance = 484
# annual interest rate as a decimal
annualInterestRate = 0.2
# minimum monthly payment rate as a decimal
monthlyPaymentRate = 0.04

def dept(x,y,z):
    monthBalance = balance
    #Monthly interest rate= (Annual interest rate) / 12.0
    monthRate = annualInterestRate / 12
    for month in range(12):
        #Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
        minMonthPayment = monthlyPaymentRate * monthBalance
        #Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
        monthUnpaidBal = monthBalance - minMonthPayment
        #Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
        monthBalance = monthUnpaidBal + (monthRate * monthUnpaidBal)
#        print('Month', month, 'Remaining balance:', round(monthBalance,2))
    return(round(monthBalance,2))

print('Remaining balance:', dept(balance, annualInterestRate, monthlyPaymentRate))
#for _ in range(10000):
#    dept(balance, annualInterestRate, monthlyPaymentRate)
#
#print("--- %s seconds ---" % (time.time() - start_time))