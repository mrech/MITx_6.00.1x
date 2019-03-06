# Test and tune code before implementing to ps4a.py
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
