
low = 0
high = 100
ans = int((high-low)/2)
user = ''

print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(ans) + "?")
print("Enter 'h' to indicate the guess is too high.", end=' ')
print("Enter 'l' to indicate the guess is too low.", end=' ')
print("Enter 'c' to indicate I guessed correctly.", end=' ')

user = input()

while user != 'c':

    if user == 'h':
        high = ans
        ans = int((high-low)/2) + low
        print("Is your secret number " + str(ans) + "?")
        print("Enter 'h' to indicate the guess is too high.", end=' ')
        print("Enter 'l' to indicate the guess is too low.", end=' ')
        print("Enter 'c' to indicate I guessed correctly.", end=' ')
        user = input()

    elif user == 'l':
        low = ans
        ans = int((high-low)/2) + low
        print("Is your secret number " + str(ans) + "?")
        print("Enter 'h' to indicate the guess is too high.", end=' ')
        print("Enter 'l' to indicate the guess is too low.", end=' ')
        print("Enter 'c' to indicate I guessed correctly.", end=' ')
        user = input()

    else:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(ans) + "?")
        print("Enter 'h' to indicate the guess is too high.", end='')
        print("Enter 'l' to indicate the guess is too low.", end='')
        print("Enter 'c' to indicate I guessed correctly.", end='')
        user = input()

print("Game over. Your secret number was: " + str(ans))


# Bisection search: with caracters

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False

    ans = aStr[len(aStr)//2]

    if char == ans:
        return True
    elif len(aStr) == 1:
        return char == ans
    elif char < ans:
        return isIn(char, aStr[:aStr.index(ans)])
    else:
        return isIn(char, aStr[aStr.index(ans)+1:])
