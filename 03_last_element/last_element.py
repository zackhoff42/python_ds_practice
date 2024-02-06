def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    list_length = len(lst)

    if(list_length == 0):
        return None
    
    return lst[list_length - 1]
