L = input("How much are you looking to borrow")
i = input("what is an interest rate you can afford?")
n = input('how many payments can you make?')

L = float(L)
i = float(i)
n = float(n)

M = L * i * (1+i) * n / (1+i) * n - 1

print('Your monthly payment is' + M)
