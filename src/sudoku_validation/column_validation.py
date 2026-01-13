def column_validation(board: list[list[int]]) -> bool:
    """
    Validate the columns of a Sudoku board.

    This function checks that each column in the Sudoku board contains
    the digits 1-9 exactly once, with no duplicates. 

    Parameters
    ----------
    board : list of list of int
        A 9x9 grid representing a Sudoku board. Each cell should contain
        an integer from 1-9.

    Returns
    -------
    bool
        True if all columns are valid (no duplicate digits 1-9), False otherwise.

    Raises
    ------
    ValueError
        If the board is not a 9x9 grid or if any of the cells contain a value outside the range 1-9.

    Examples
    --------
    >>> board = [
    ...     [4, 3, 0, 0, 7, 0, 0, 0, 0],
    ...     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    ...     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    ...     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    ...     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    ...     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    ...     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    ...     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    ...     [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ... ]
    >>> column_validation(board)
    False

    >>> board = [
    ...     [3, 2, 6, 9, 7, 4, 8, 1, 5],
    ...     [8, 1, 9, 3, 5, 6, 4, 7, 2],
    ...     [5, 4, 7, 2, 1, 8, 9, 6, 3],
    ...     [9, 5, 2, 7, 3, 1, 6, 4, 8],
    ...     [1, 3, 4, 6, 8, 9, 5, 2, 7],
    ...     [6, 7, 8, 4, 2, 5, 1, 3, 9],
    ...     [7, 6, 1, 8, 9, 3, 2, 5, 4],
    ...     [2, 9, 5, 1, 4, 7, 3, 8, 6],
    ...     [4, 8, 3, 5, 6, 2, 7, 9, 1]
    ... ]
    >>> column_validation(board)
    True

    """
    from sudoku_validation.array_validation import array_validation
    
    # validate the board is a 9x9 grid
    if len(board) != 9:
        raise ValueError("Board must be a 9x9 grid")
    
    for row in board:
        if len(row) != 9:
            raise ValueError("Board must be a 9x9 grid")
    
    # validate the board contains only integers from 1 to 9
    for row in board:
        for cell in row:
            if not isinstance(cell, int) or cell < 1 or cell > 9:
                raise ValueError("Board must contain only integers from 1 to 9")

    # get arrays of the columns
    columns = [[] for _ in range(9)]
    for row in board:
        for i in range(9):
            columns[i].append(row[i])

    # validate the columns contain only unique integers from 1 to 9
    for column in columns:
        if len(set(column)) != 9:
            return False

    # validate the columns are a valid sudoku solution
    for column in columns:
        if not array_validation(column):
            return False

    # return True if all tests pass
    return True