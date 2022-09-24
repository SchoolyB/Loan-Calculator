#Variables:

#L = Loan amount as a whole number
#R = Interest rate as a whole number
#n = Lenghth of loan term in years as a whole number
#i = Interest calculation
#M = Monthly payment as floating number
#CS = input('Lastly, What is your credit score?')

L = input('How much would you like to borrow? \n')
R = input('What is the desired interest rate on your loan? \n')
n = input('How many years will the loan term be? \n')
CS = input('Lastly, What is your credit score? \n')

L = float(L)
R = float(R)
n = float(n)
CS = float(CS)

i = R / 100

print(R)
print(i)

numberofPayments = n*12

#Monthly Payment Loan Formula: M = L[i(1+i)n] / [(1+i)n-1]

M = L * i * (1 + i) * n / ((1 + i) * n - 1)

print('So, You would like to borrow $' + str(L) + ' ' + 'And pay us back over ' + str(n)  + ' ' + 'years at an interest rate of ' + str(i) + '%?')
print('Great! Your monthly payment will be $' + str(M))

#DECLARING FUNTIONS

def runCredit():

    if CS >= 850:
        perfectScore()

    elif CS <= 550:
        needsWork()
        score = questionContinue()
        if score == 'y':
            yesAnswer()
        elif score == 'n':
            noAnswer()
        else:
            questionContinue()

    elif CS >= 550:
        print('Your credit score is good')
        score = questionContinue()
        if score == 'y':
            yesAnswer()
        elif score =='n':
            noAnswer()
        else: 
            questionContinue()
    else:
        runCredit()

def questionContinue():
    foo = input('Would you like to continue? y/n') #CHANGE VARIABLE NAME
    if foo == 'n':
        noAnswer()
    elif foo == 'y':
        yesAnswer()
    else:
        questionContinue()

def yesAnswer():
    print('Ok Great! Lets move foward!')

def noAnswer():
    print('Ok I think we are done here.')

def needsWork():
    print('Your credit score needs some work.')
    wantResource = input('Would you like some resources on how to improve your credit score? y/n')
    if wantResource == 'y':
        print('Here is a link containing some useful information on how to improve your credit score.') #ADD LINK
    elif wantResource == 'n':
        print('Ok well there are many ways to increase your credit score. Goodluck.')
    else:
        needsWork()

def goodCredit():
    print('Your credit is good.')

def perfectScore():
    print('You have a perfect credit score!')

#CALLING FUNCTION

runCredit()

#NEED TO FIGURE OUT WHY the questionContinue FUNCTION KEEPS RUNNING