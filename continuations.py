from loancalc import loanCalculate

###DECLARING A RUNAGAIN() FUNCTION###
def runAgain():
    Run_Again = input('Would you like to run the program again? ' 'yes/no')
    if Run_Again == 'yes':
        loanCalculate()
    elif Run_Again == 'no':
        print('OK...goodbye')    


###DECLARING A CORRECTINFO() FUNCTION###
def correctInfo():

    Correct_Info = input('Is th information above correct? ' 'yes/no ')

    if Correct_Info == 'yes':
        print('Okay! Your monthly payment will be $' + str(M))

    elif Correct_Info == 'no':
        print('Ok I think we`re done here...')
    else:
        print('Please enter a valid response...' ' yes/no ')
        correctInfo()
