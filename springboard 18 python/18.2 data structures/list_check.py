def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

for item in lst:
        if not isinstance(item, list):
            return False

    return True



# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
