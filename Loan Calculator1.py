#Version 2.0.0 


from time import sleep


#Declaring the fucntion for the loan calculate prompt

def loanCalculate():
#L = Loan amount as a whole number
#R = Interest rate as a whole number
#n = Lenghth of loan term in years as a whole number
#i = Interest calculation
#M = Monthly payment as floating number
    
    L = input('How much would you like to borrow? \n')
    R = input('What is the desired interest rate on your loan? \n')
    n = input('How many years will the loan term be? \n')
    
    L = float(L)
    R = float(R)
    n = float(n)


    i = R / 100

    print(R)
    print(i)

    numberofPayments = n*12

    M = L * i * (1 + i) * n / ((1 + i) * n - 1)

    print('So, You would like to borrow $' + str(L) + ' ' + 'And pay us back over ' + str(n)  + ' ' + 'years at an interest rate of ' + str(i) + '%?')
    print('Okay! If approved Your monthly payment will be $' + str(M))

#Calling The loan calculate Prompt

loanCalculate()


#Declaring Functions to be used in the continuation prompt

def perfectScore():
    print('Wow! You have a perfect credit score congratulations!')

def needsWork():
    print('Your credit needs a little work but its not too bad')
    
def prettyGood():
    print('Your credit is pretty good.')

def wantTips():
    wantTips = input('Would you like some tips on how to improve your credit? y/n')
    if wantTips == 'y':
        print('Ok here are some helpful tips on ways to increase your credit score.') #add a list of tips
    elif wantTips == 'n':
        print('Well there are alot of resources out there. ')
    else:
        print('Please enter a valid answer')
        sleep(3)
        runCreditPrompt()

def runCreditPrompt():
    creditScoreAnswer = input('Ok please tell me your credit score')
    creditScoreAnswer = float(creditScoreAnswer)

    if creditScoreAnswer <= 600:
        needsWork()
        wantTips()
        
    elif creditScoreAnswer >= 600:
        prettyGood()
        wantTips()

    elif creditScoreAnswer ==850:
        perfectScore()

    else:
        print('please enter a valid answer')
        sleep(3)
        runCreditPrompt()

def initialContinue():
    continueAnswer = input('Would you like to continue with with the loan? y/n')
    if continueAnswer == 'y':
        knowScore = input('Great! Would you happen to know what your credit score is? y/n')
        if knowScore == 'y':
            runCreditPrompt()
        elif knowScore == 'n':
            dontKnowScore = input('Ok, well once you know it please come back and tell me so we can continue')
        else: 
            print('Please enter a valid answer.')
            sleep(3)
            initialContinue()

    elif continueAnswer == 'n':
        noAnswer = input('Ok well I think we`re done here.')
    else:
        print('Please enter a valid answer.')
        sleep(3)
        initialContinue()


#Calling the continuation prompt
initialContinue()