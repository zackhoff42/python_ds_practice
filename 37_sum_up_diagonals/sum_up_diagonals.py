def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    diagonal_one = 0
    diagonal_two = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i == j:
                diagonal_one += matrix[i][j]
            if i + j == len(matrix) - 1:
                diagonal_two += matrix[i][j]

    return diagonal_one + diagonal_two