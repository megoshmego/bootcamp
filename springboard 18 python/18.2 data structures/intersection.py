def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    set2 = set(l2)

    return [val for val in l1 if val in set2]

"""THE ABOVE CONVERTS TO A SET... OR"""

#other solutions

def merge(l1, l2):
    return [val for val in l1 if val in l2]

print(merge([1, 2, 6], [6, 4]))


def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)










