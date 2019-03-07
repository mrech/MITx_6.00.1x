# Test and tune code before implementing to ps4a.py
import random

# Problem #1: Scoring a word


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        # safe way to access a value if key not in dictionary return zero
        # insert elements in the dictionary
        freq[x] = freq.get(x, 0) + 1
    return freq


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

hand = 'oiac'
word = 'ciao'
n = 4
value = []
tot_value = []

if len(word) > 0:
    # check hand availability
    hand_availability = getFrequencyDict(hand)
    word_availability = getFrequencyDict(word)

    if all(item in hand_availability.items() for item in word_availability.items()):
        for i in word:
            value.append(SCRABBLE_LETTER_VALUES[i])
            # sum of the points for the letters in the word
            if n == len(word):
                score = sum(value)*len(word) + 50
            else:
                score = sum(value)*len(word)
    else:
        print('HAND do not contain all the necessary letters to make WORD')
else:
    score = 0

# Problem #2: Make sure you understand how this function works and what it does!

hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}


def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):  # with dupplicate later range > 0
            print(letter, end=" ")
    print()


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
n = 4


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        # safe way to access a value if key not in dictionary return zero
        # insert elements in the dictionary
        hand[x] = hand.get(x, 0) + 1

    # the same with the ramained letters. Picking from consonants
    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

# Problem #2: Update a hand by removing letters


hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
word = 'quail'


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """

    updateHand = hand.copy()

    for i in word:

        updateHand[i] = updateHand.get(i, 0) - 1

    return updateHand

#
# Problem #3: Test word validity


hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
word = 'honne'


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    if len(word) > 0:
        # check hand availability
        word_availability = getFrequencyDict(word)
        try:
            if all(word_availability[i] <= hand[i] for i in word_availability.keys()):
                if word in wordList:
                    print('Word in list')
                    return True
                else:
                    print('Word not in list')
                    return False
            else:
                print('Not enough letters')
                print(word_availability.items())
                print(hand.items())
                return False
        except KeyError:
            return False
    else:
        print('word is empty')
        return False

# Problem #5: Playing a game

# Tests
#playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
#playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)


# Computer chooses a word
# Test cases to Understand the code
'''
compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6) 
appels 
compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5) 
acta 
compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12) 
immanent 
compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12) 
None
'''


# Computer plays a hand
# Test cases to Understand the code
''''
compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
'''
