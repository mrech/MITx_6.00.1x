# Handling specific exceptions
try:
    a = int(input('Tell me one number: '))
    b = int(input('Tell me another number: '))
    print('a/b = ', a/b)
    print('a+b = ', a+b)
except ValueError:
    print('Could not convert to a number.')
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print('Something went very wrong.')

# While Exception
while True:
    try:
        n = input('Please enter an integer: ')
        n = int(n)
        break
    except ValueError:
        print('Input not an integer; try again.')
print('Correct input of an integer!')
