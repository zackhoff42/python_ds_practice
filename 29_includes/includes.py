def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if start != None and type(collection) != set and type(collection) != dict:
        count = 0
        for val in collection[start:]:
            if val == sought:
                count += 1
        if count >= 1:
            return True
        else:
            return False
    elif isinstance(collection, dict):
        count = 0
        vals = list(collection.values())
        for val in vals:
            if val == sought:
                count += 1
        if count >= 1:
            return True
        else:
            return False

    return sought in collection