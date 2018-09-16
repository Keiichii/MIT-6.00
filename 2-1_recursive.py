#import time
#start_time = time.time()

# the outstanding balance on the credit card
balance = 484
# annual interest rate as a decimal
annualInterestRate = 0.2
# minimum monthly payment rate as a decimal
monthlyPaymentRate = 0.04

monthes =12
def dept(monthBalance,annualInterestRate,monthlyPaymentRate,month):
    if month == 0:
        return monthBalance
    else:
        minMonthPayment = monthlyPaymentRate * monthBalance
        monthUnpaidBal = monthBalance - minMonthPayment
        monthBalance = monthUnpaidBal + (annualInterestRate/12 * monthUnpaidBal)
#        print('Month', monthes-month+1, 'Remaining balance:', round(monthBalance,2))
        return round(dept(monthBalance,annualInterestRate,monthlyPaymentRate,month-1),2)
        
print('Remaining balance:', dept(balance, annualInterestRate, monthlyPaymentRate, monthes))
#for _ in range(10000):
#    dept(balance, annualInterestRate, monthlyPaymentRate, monthes)
#
#print("--- %s seconds ---" % (time.time() - start_time))