#VERSION 2.1.0 
#AUTHOR: Marshall Burns a.k.a Schooly B

import continuations 

###DECLARING LOANCLACULATE() FUNCTION###
def loanCalculate():

###DECLARING VARIABLES TO BE USED IN THE LOANCALCULATE() FUNCTION###

#L = Loan amount as a whole number
#R = Interest rate as a whole number
#n = Lenghth of loan term in years as a whole number
#i = Interest calculation
#M = Monthly payment as floating number

    
    L = input('How much would you like to borrow? \n' '$' )
    R = input('What is the desired interest rate on your loan? \n')
    n = input('How many years will the loan term be? \n' 'length in years:')
    
    L = float(L)
    R = float(R)
    n = float(n)


    i = R / 100

    numberofPayments = n*12

###DECLARING THE FORMULA TO CALCULATE A MONTHLY PAYMENT WITH VARIABLES GIVEM###
    M = L * i * (1 + i) * n / ((1 + i) * n - 1)

    print('So, You would like to borrow $' + str(L) + ' ' + 'And pay that back over ' + str(n)  + ' ' + 'years at an interest rate of ' + str(i) + '%?')
    ###CALLING THE CORRECTINFO() FUNCTION####
    correctInfo()
    print('Okay! Your monthly payment will be $' + str(M))



###CALLING THE LAONCALCULATE() FUNCTION###
loanCalculate()

runAgain()