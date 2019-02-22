animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'
animals['a'] = 'anteater'
animals.keys()
del animals['b']
animals.values()

# How many

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    TotalCount = 0
    for letter in aDict:
        count = len(aDict[letter])
        TotalCount += count
    return TotalCount


# Biggest
animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest = 0
    letter = None
    for key in aDict:
        count = len(aDict[key])
        if count > biggest:
            biggest = count
            letter = key
    return letter

# Application og Google Dynamic Programming
# Fibonacci Efficient


numFibCalls = 0


def fib_efficient(n, d):
    # Traking Efficiency
    global numFibCalls
    numFibCalls += 1
    # base cases
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans


# base case
d = {1: 1, 2: 2}
n = 30

print(fib_efficient(n, d))
print('Function calls', numFibCalls)