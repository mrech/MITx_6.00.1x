
# Exponential complexity: 2^x


def genSubsets(L):  # L = [1,2,3]
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])  # [[],[1],[1,2]]
    extra = L[-1:]  # [3]
    new = []
    for small in smaller:
        new.append(small+extra)
        # 1. []+[3] = [3]
        # 2. [1]+[3] = [1,3]
        # 3. [1,2]+[3] = [1,2,3]
        # new = [[3], [1,3], [1,2,3]]
    return smaller+new  # [[],[1],[1,2]] + [[3], [1,3], [1,2,3]]


L = [1, 2, 3]

genSubsets(L)
# [[], [1], [1, 2], [3], [1, 3], [1, 2, 3]]
