# =============================================================================
# import time
# start_time = time.time()
# 
# =============================================================================
# the outstanding balance on the credit card
balance = 3329
# annual interest rate as a decimal
annualInterestRate = 0.2


def dept():
    avgMonthPayment = 0

    while True:
        avgMonthPayment +=10
#        print(avgMonthPayment)
        monthBalanceTest = balance
    
        for _ in range(12):
            monthUnpaidBal = monthBalanceTest - avgMonthPayment
            monthBalanceTest = monthUnpaidBal + (annualInterestRate/12 * monthUnpaidBal)
#            print('For: Month', _+1, monthBalanceTest)
        if monthBalanceTest<0:
            return avgMonthPayment

print('Lowest Payment:', dept())

# =============================================================================
# for _ in range(10000):
#     dept()
# 
# print("Iterative test: --- %s seconds ---" % (time.time() - start_time))
# =============================================================================
