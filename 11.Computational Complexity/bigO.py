# Asymptotic complexity: upper bound on asymptotic growth
# describe running time in terms of number of basic steps.

# Program 1 (o: outter, i: inner -> both to n (big number))


def program1(L):
    multiples = []  # 1 op: assignment
    for x in L:  # 1*o: assignment
        for y in L:  # (1*i)*(1*o): assignment
            multiples.append(x*y)  # (2*i)*(1*o): assignment, math operation
    return multiples  # 1 op: access memory


'''
BEST CASE: L is empty >>> 2
WORST CASE: L -> inf >>> 
o + oi + 2io + 2 =
o(1+i+2i)+2 -> n(3n+1)+2 =
3n²+n+2
Big O: O(n²)
'''

# Program 2 (o: outter, i: inner -> both to n (big number))


def program2(L):
    squares = []  # 1 op: assignment
    for x in L:  # 1*o op: assignment
        for y in L:  # (1*i)*(1*o) op: assignment
            if x == y:  # (1*i)*(1*o) op: comparisons
                # (2*i)*(1*o) op: assignment, math operation
                squares.append(x*y)
    return squares  # 1 op: access memory


'''
BEST CASE: L is empty >>> 2
WORST CASE: L -> inf of all the same numbers >>> (4n + 1)*n + 2 = 4*n² + n + 2 
o + i*o + i*o + 2i*o + 2 =
o(1+i+i+2i) + 2 -> n(4n+1) + 2 =
4n²+n+2
Big O: O(n²)
'''

# Program 3 (o: outter, i: inner -> both to n (big number))


def program3(L1, L2):
    intersection = []  # 1 op: assignment
    for elt in L1:  # 1*o op: assignment
        if elt in L2:  # (1*i)*1*o op: assignment
            intersection.append(elt)  # 1*o op: assignment
    return intersection  # 1 op: accessing memory


'''
BEST CASE: L1 and L2 are empty >>> 2
WORST CASE: L1 and L2 -> inf and common values at the end L2 >>> 
1*o+(1*i)*1*o+1*o + 2 =
o(1+i+1)+2 = 
n(1+n+1)+2 =
n²+2n+2 
Big O: O(n²)
'''
