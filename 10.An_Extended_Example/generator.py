
def genPrimes():
    EarlyPrime = []
    x = 2
    while True:
        # using list comprehension
        if all(x % p != 0 for p in EarlyPrime):
            EarlyPrime.append(x)
            yield x
            x += 1
        else:
            x += 1


prime = genPrimes()
prime.__next__()

for x in genPrimes():
    print(x)

# Standard function is best:
'''
When the number of iterations is already known
- find the nth bounded number
- iterating over sequence of numbers in a random no repeated order
'''

# Generator is best:
'''
- print out an unbounded sequence
'''

# both are best:
'''
- bounded sequence
'''
