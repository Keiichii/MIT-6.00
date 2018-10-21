balance = 320000
# annual interest rate as a decimal
annualInterestRate = 0.2

def dept():
    avgMonthPayment = 0
    low =0
    top = balance
    
    while True:
        avgMonthPayment = (top-low)/2+low
        #print(avgMonthPayment)
        monthBalanceTest = balance
    
        for _ in range(12):
            monthUnpaidBal = monthBalanceTest - avgMonthPayment
            monthBalanceTest = monthUnpaidBal + (annualInterestRate/12 * monthUnpaidBal)
            print('For: Month', _+1, monthBalanceTest)
        if -0.1<monthBalanceTest<0:
            return avgMonthPayment
        elif monthBalanceTest<0:
            top = avgMonthPayment 
        elif monthBalanceTest>0:
            low = avgMonthPayment
         

print('Lowest Payment:', round(dept(),2))
