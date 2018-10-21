#import time
#start_time = time.time()

# the outstanding balance on the credit card
balance = 3329
# annual interest rate as a decimal
annualInterestRate = 0.2

avgMonthPayment = ((balance + annualInterestRate * balance)//12)//10*10

def dept(monthBalance, annualInterestRate, minMonthPayment):
#    print(minMonthPayment)
    monthBalanceTest = monthBalance
    for _ in range(12):
        monthUnpaidBal = monthBalanceTest - minMonthPayment
        monthBalanceTest = monthUnpaidBal + (annualInterestRate/12 * monthUnpaidBal)
        print('For: Month', _+1, monthBalanceTest)
    if monthBalanceTest>0:
        return minMonthPayment+10
    else:
        return dept(monthBalance, annualInterestRate, minMonthPayment-10)

print('Lowest Payment:', int(dept(balance, annualInterestRate, avgMonthPayment)))

#for _ in range(10000):
#    dept(balance, annualInterestRate, avgMonthPayment)
#
#print("Recursive test: --- %s seconds ---" % (time.time() - start_time))