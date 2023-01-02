
"""Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """



def frequency(lst, search_term):
    return lst.count(search_term)

#my example which returns a dict, containing the terms and the number of times it appears

import collections

def frequency_terms(random_list):
    frequency = collections.Counter(random_list)
    print(dict(frequency))