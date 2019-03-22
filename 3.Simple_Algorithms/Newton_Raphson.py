
# g – p(g)/p’(g)
# whant to find g such that p(g)=0 > p(g) = g**2 - 24

epsilon = 0.00001
k = 24.0
guess = k/2
numGuess = 0

while abs(guess**2 - k) >= epsilon:
    numGuess =+ 1
    guess = guess - ((guess**2 - k)/(2*guess))

print('Number Guesses = ' + str(numGuess))
print('Square root of ' + str(k) + ' is about ' + str(guess))
