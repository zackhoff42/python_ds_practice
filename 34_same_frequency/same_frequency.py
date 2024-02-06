def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num_list_one = [int(num) for num in str(num1)]
    num_list_two = [int(num) for num in str(num2)]

    return sorted(num_list_one) == sorted(num_list_two)