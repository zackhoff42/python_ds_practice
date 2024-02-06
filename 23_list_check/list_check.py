def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for val in lst:
        if isinstance(val, list) == False:
            return False
        
    return True