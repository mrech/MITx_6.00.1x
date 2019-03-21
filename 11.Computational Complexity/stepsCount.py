# developing the intuition to gauge efficient coding 
# counting the number of steps

# Program 1:
def program1(x):
    total = 0 # 1 op: assignments
    for i in range(1000): # 1*1000 op: assignments
        total += i # 2*1000 op: assignments, mathematical operations

    while x > 0: # 1*n + 1 at the zero condition op: comparison
        x -= 1 # 2*n op: assignment, mathematical operations
        total += x # 2*n op: assignment, mathematical operations

    return total # 1 op: accessing objects in memory
'''
BEST CASE: x < 0 >>> 1 + 3*1000 + 1 + 1 = 3003
WORST CASE: x -> inf >>> 1 + 3*1000 + 5*n + 1 + 1 = 5*n + 3003
'''

# Program 2: 
def program2(x):
    total = 0 # 1 op: assignemnt
    for i in range(1000): # 1*1000 op: assignment
        total = i # 1*1000 op: assignment

    while x > 0: # 1*log2(n) +1 +1 at the zero condition op: comparison
        x = x//2 # 2*log2(n) + 1 op: assignment, mathematical operations
        total += x # 2*log2(n) + 1  op: assignment, mathematical operations

    return total # 1 op: accessing objects in memory

'''
BEST CASE: x = 0 >>> 1 + 2*1000 + 1 + 1 = 2003
Because we divide x by 2 every time through the loop, 
we only execute this loop a logarithmic number of times. 
log2(n) divisions of x by 2 will get us to x = 1; 
we'll need one more division to get x <= 0 
WORST CASE: x -> inf >>> 1 + 2*1000 + 5*(log2(n) + 1) + 1 + 1 = 5*log2(n)) + 2008
'''

# Program 3:
def program3(L):
    totalSum = 0 # 1 op: assignment
    highestFound = None # 1 op: assignment
    for x in L: # 1*n op: assignment
        totalSum += x # 2*n op: assignment, mathematical operations

    for x in L: # 1*n op: assignement
        if highestFound == None: # 1*n op: comparishon
            highestFound = x # 1 op: assignment
        elif x > highestFound: # 1*n-1 op: comparison
            highestFound = x # 1*n-1(x+1 > x) op: assignment

    return (totalSum, highestFound) # 1 op: accessing objects in memory

'''
BEST CASE: L is empty >>> 1 + 1 + 2 = 4
WORST CASE: L -> inf and x+1 > x >>> 
1 + 1 + 3*n + 2*n + 1 + 2*n-1 + 1 = 
4 + 5*n + 2*(n-1) = 
7*n + 2
'''