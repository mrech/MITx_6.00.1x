# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def YearBalance(balance, annualInterestRate, monthlyPaymentRate):

    # for a period of 12 months
    for i in range(12):

        # calculate monthly unpaid balance
        balance = (balance - (balance*monthlyPaymentRate))
        # monthly interest due on the upaid balance
        balance = balance + (balance * (annualInterestRate/12))

        i += 1

    # Remaining balance at the end of the year
    print("Remaining balance: " + str(round(balance, 2)))


# Paying Debt Off in a Year
balance = 3329
annualInterestRate = 0.2

# Define the lowest payment
fixedMonthlyPayment = 0
UnpaidBalance = balance

while UnpaidBalance > 0:

    UnpaidBalance = balance
    # Increment fix monthly payment
    fixedMonthlyPayment += 10

    for i in range(12):

        # monthly unpaid balance
        UnpaidBalance = UnpaidBalance - fixedMonthlyPayment
        # monthly interest due on the updaid balance
        UnpaidBalance = UnpaidBalance + \
            (UnpaidBalance * (annualInterestRate/12))
        i += 1

print("Lowest Payment: " + str(fixedMonthlyPayment))


# Using Bisection Search
balance = 320000
annualInterestRate = 0.2

# Define Lower bound
lower = balance/12
# Define Upper bound
upper = (balance * (1 + (annualInterestRate/12))**12)/12

# Calculate the initial fixed monthly payment
fixedMonthlyPayment = lower + (upper - lower)/2
UnpaidBalance = balance
epsilon = 0.0001

while UnpaidBalance <= -epsilon or UnpaidBalance >= epsilon:
    # Re-initiate
    UnpaidBalance = balance

    for i in range(12):
        # monthly unpaid balance
        UnpaidBalance = UnpaidBalance - fixedMonthlyPayment
        # monthly interest due on the updaid balance
        UnpaidBalance = UnpaidBalance + \
            (UnpaidBalance * (annualInterestRate/12))
        i += 1

    if UnpaidBalance < 0:
        upper = fixedMonthlyPayment
        fixedMonthlyPayment = lower + (upper - lower)/2
    else:
        lower = fixedMonthlyPayment
        fixedMonthlyPayment = lower + (upper - lower)/2

print("Lowest Payment: " + str(round(fixedMonthlyPayment, 2)))
