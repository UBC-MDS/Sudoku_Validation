
def combined_validation(board: list[list[int]]) -> bool:
    """
    Validate an entire Sudoku board.

    This function checks whether a Sudoku board is valid according to
    standard rules: each row, each column and each 3x3 square must
    contain unique digits from 1 to 9, ignoring placeholder values
    (e.g., 0 or None) for incomplete cells. It combines the checks
    from row_validation, column_validation and square_validation.

    Parameters
    ----------
    board : list of list of int
        A 9x9 grid representing a Sudoku board. Each cell should contain
        an integer from 1-9.

    Returns
    -------
    bool
        True if the board is valid (all rows, columns and squares contain
        unique digits according to Sudoku rules), False otherwise.

    Raises
    ------
    ValueError
        If the board is not a 9x9 grid or contains invalid cell values
        outside the range 0-9.


    Examples
    --------
    >>> board = [
    ...     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    ...     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    ...     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    ...     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    ...     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    ...     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    ...     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    ...     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    ...     [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ... ]
    >>> combined_validation(board)
    False

    >>> solved_board = [
    ...     [5, 3, 4, 6, 7, 8, 9, 1, 2],
    ...     [6, 7, 2, 1, 9, 5, 3, 4, 8],
    ...     [1, 9, 8, 3, 4, 2, 5, 6, 7],
    ...     [8, 5, 9, 7, 6, 1, 4, 2, 3],
    ...     [4, 2, 6, 8, 5, 3, 7, 9, 1],
    ...     [7, 1, 3, 9, 2, 4, 8, 5, 6],
    ...     [9, 6, 1, 5, 3, 7, 2, 8, 4],
    ...     [2, 8, 7, 4, 1, 9, 6, 3, 5],
    ...     [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ... ]
    >>> combined_validation(solved_board)
    True
    """
    