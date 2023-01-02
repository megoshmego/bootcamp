def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """


def multiple_letter_count(phrase):
    counter = {}
    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1
    return counter

    
#my solution

from collections import Counter

my_string = ""

def frequency(my_string):
        result = Counter(my_string)
        print("the count of the characters in your phrase is :\n" + str(result))
        