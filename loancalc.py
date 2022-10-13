#VERSION:3.0.0
#AUTHOR: Marshall Burns a.k.a Schooly B

from time import sleep

###DECLARING _RUN() FUNCTION###
def _Run():

###DECLARING VARIABLES TO BE USED IN THE _RUN() FUNCTION###

#L = Loan amount as a whole number
#R = Interest rate as a whole number
#n = Lenghth of loan term in years as a whole number
#i = Interest calculation
#M = Monthly payment as floating number

    L = input('How much would you like to borrow? \n' '$' )
    R = input('What is the desired interest rate on your loan? \n')
    n = input('How many years will the loan term be? \n' 'Length in years:')

    ###CONVERTING 'STRING' INPUTS TO INTERGERES TO BE ABLE TO USE THEM IN MATH###   
    L = float(L)
    R = float(R)
    n = float(n)

    i = R / 100

    ###THE FORMULA TO CALCULATE A MONTHLY PAYMENT WITH GIVEN VARIABLES ###
    M = L * i * (1 + i) * n / ((1 + i) * n - 1)

    print('So, You would like to borrow $' + str(L) + ' ' + 'And pay that back over ' + str(n)  + ' ' + 'years at an interest rate of ' + str(i) + '%? ')
    sleep(3)
    print('Okay! Your monthly payment will be $' + str(M))
    sleep(2)
    Run_Again()

###DECLARING THE RUN_AGAIN() FUNCTION###
def Run_Again():
    runAgain = input('Would you like to run the program again? ')
    if runAgain == 'yes':
        print('Ok lets run it again')
        sleep(2)
        _Run()
    elif runAgain =='no':
        print('OK..goodbye')
    else:
        print('please enter a valid respons. ' 'yes/no ')
        sleep(2)
        Run_Again()

###CALLING THE _RUN() FUNCTION###
_Run()
