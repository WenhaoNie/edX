balance = 320000
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#Problem1
monthlyInterestRate = annualInterestRate/12.0

def MonthlyPayment(remainingBalance, interest):
    newBalance = remainingBalance+interest
    payment = newBalance*monthlyPaymentRate
    unpaidBalance = newBalance-payment
    newInterest = unpaidBalance*monthlyInterestRate
    return unpaidBalance, newInterest

currentBalance = balance
currentInterest = 0
for i in range(12):
    currentBalance, currentInterest = MonthlyPayment(currentBalance,currentInterest)
    #print('Month {} Remaining balance: {}'.format(i+1,round(currentBalance+currentInterest,2)))

print('Remaining balance: {}'.format(round(currentBalance+currentInterest,2)))

#Problem2
monthlyInterestRate = annualInterestRate/12.0
def FixedPayment(remainingBalance, interest, payment):
    newBalance = remainingBalance+interest
    unpaidBalance = newBalance-payment
    newInterest = unpaidBalance*monthlyInterestRate
    return unpaidBalance, newInterest

currentBalance = balance
currentInterest = 0
payment = 0

def FullyPaid(startBalance, payment, months):
    unpaidBalance = startBalance
    interest = 0
    for i in range(months):
        unpaidBalance,interest=FixedPayment(unpaidBalance,interest,payment)
        if unpaidBalance < 0: break
    if unpaidBalance <= 0: return True
    else: return False

while not FullyPaid(currentBalance,payment,12):
    payment += 10

print('Lowest Payment: {}'.format(payment))

#Problem3

monthlyInterestRate = annualInterestRate/12.0
lowerbound = balance/12
upperbound = balance*(1+monthlyInterestRate)**12/12
guess = (lowerbound+upperbound)/2
epsilon = 0.01

def FixedPayment(remainingBalance, interest, payment):
    newBalance = remainingBalance+interest
    unpaidBalance = newBalance-payment
    newInterest = unpaidBalance*monthlyInterestRate
    return unpaidBalance, newInterest

def FullyPaid(startBalance, payment, months):
    unpaidBalance = startBalance
    interest = 0
    for i in range(months):
        unpaidBalance,interest=FixedPayment(unpaidBalance,interest,payment)
        if unpaidBalance < 0: break
    if unpaidBalance <= 0: return True
    else: return False

while True:
    oldguess = guess
    if FullyPaid(balance,guess,12):
        upperbound = guess
        guess = (lowerbound+upperbound)/2
        if abs(oldguess-guess)<epsilon: break
    else:
        lowerbound = guess
        guess = (lowerbound+upperbound)/2

print('Lowest Payment: {}'.format(round(guess,4)))

