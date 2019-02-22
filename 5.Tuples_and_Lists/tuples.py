# TUPLES
def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)


(quot, rem) = quotient_and_remainder(4, 5)


def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)


(small, large, words) = get_data(
    ((1, 'mine'), (3, 'yours'), (5, 'ours'), (7, 'mine')))


aTup = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    return aTup[0::2]
