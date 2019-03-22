# selection sort

'''
selSort implements this without explicitly creating a new list, 
by maintaining sorted (from position 0 to i-1) and unsorted 
(from position i to the end) parts of the list. All elements in 
positions before the iterating variable i are sorted, and unsorted 
for those positions at i or below. In each iteration, it selects 
the smallest element in the unsorted part of the list, and swaps 
it with the element at the ith position. That essentially adds 
the next smallest element from the old list and appends it to the new. 
It keeps doing that until the old list is empty 
(i.e., i reaches the end of the list).

selSort only does one "swap" each iteration of i
'''
L = [1, 0, 4, 3]


def selSort(L):
    for i in range(len(L) - 1):
        print(L)
        # get min index
        minIndx = i  # 0 index
        # get min values corresponding that index
        minVal = L[i]  # 1 values
        # get index of the following value
        j = i+1  # 1 index
        # check all the element of L to find the smallest
        while j < len(L):
            # consecutive checking
            # check if min value > than following value
            if minVal > L[j]:  # 1 > 0
                # change current min Index to to the following
                minIndx = j  # 1
                # assign min value to the following value
                minVal = L[j]  # 0
            # go down through the list
            j += 1  # 2
        # Swap
        if minIndx != i:  # 1 != 0
            temp = L[i]  # 1
            L[i] = L[minIndx]  # 0
            L[minIndx] = temp  # 1


selSort(L)

'''
newSort is basically a slight variant of Selection Sort. In each iteration, 
newSort also tries to find the smallest element in the unsorted part of the 
list and appends it to the sorted part of the list. The only difference here 
is that instead of finding the smallest value in the unsorted part of the 
list with minVal and minIndx, newSort maintains that the element at the 
ith position is the smallest element between the ith and jth positions. 
So, when j reaches the end of the list, the ith position must have been the 
smallest element in the unsorted portion (from position i to the end) of the list.

newSort may use up to (n-i) "swaps" for each iteration of i
'''
L = [1, 0, 4, 3]


def newSort(L):
    # range(0,2)
    for i in range(len(L) - 1):
        print(L)
        # 1
        j = i+1
        # every time it goes through all the element of the list
        # and compare them to the first one (index i)
        while j < len(L):
            if L[i] > L[j]:
                # swap
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1


newSort(L)

# BUBBLE SORT
# in each iteration, if an element e is bigger than the one after it,
# e moves down one location. Then, e is checked against the next element,
# and so on,
'''
the biggest element drops to the bottom of the list. Then, in the second pass, 
the second biggest drops to the second to last position in the list, and so 
on for the remaining iterations. In each pass through the list, the next biggest 
element drops to its proper location, so that after n iterations, the list is sorted. 
'''


def mySort(L):
    """ L, list with unique elements """
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp


# goes on in making comparison for all elments of L until reaching the end
# it keeps tracks of the values already ordered
'''
maintains that the element at the ith position is the smallest element 
between the ith and jth positions
'''


def newSort(L):
    """ L, list with unique elements """
    for i in range(len(L) - 1):
        j = i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1


'''
For L = [1, 2, 3] mySort performs 2 comparisons and newSort performs 3 comparisons. 
For L = [3, 2, 1] mySort performs 6 comparisons and newSort performs 3 comparisons. 
'''

# Increasing


def swapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)

# Decreasing


def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)
