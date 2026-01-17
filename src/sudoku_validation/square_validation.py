"""
Square-level validation utilities for Sudoku boards.

This module provides functionality for validating individual rows of a Sudoku board. Square validation is performed by extracting a valid square from the board and delegating Sudoku rule checks to the generic array validation functions.
"""

from array_validation import array_validation

def square_validation(board: list[list[int]]) -> bool:
    """
    Validate the squares of a Sudoku board.
    This function checks that each of the 9 square in the Sudoku board contains the digits 1-9 exactly once, with no duplicates. 
    
    Parameters
    ----------
    board : list of list of int
        A 9x9 grid representing a Sudoku board. Each cell should contain an integer from 1-9.
    
    Returns
    -------
    bool
        True if all 9 of the squares are valid (no duplicate digits 1-9), False otherwise.
    
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
    >>> square_validation(board)
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
    >>> square_validation(board)
    True
    """

    # Iterate and Validate 3×3 Squares
    for square_index in range(9):
        # Determine the top-left corner of this 3×3 square
        row_offset = (square_index // 3) * 3
        col_offset = (square_index % 3) * 3
    
        # Extract the 3×3 square as a flat list of 9 elements
        square = [
            board[r][c]
            for r in range(row_offset, row_offset + 3)
            for c in range(col_offset, col_offset + 3)
        ]
    
        # Validate the square
        try:
            is_valid = array_validation(square)
        except ValueError as e:
            raise ValueError(
                f"Invalid 3×3 square at index {square_index}: {str(e)}"
            ) from e
    
        if not is_valid:
            return False
    
    return True

# board = [
#          [3, 2, 6, 9, 7, 4, 8, 1, 5],
#          [8, 1, 9, 3, 5, 6, 4, 7, 2],
#          [5, 4, 7, 2, 1, 8, 9, 6, 3],
#          [9, 5, 2, 7, 3, 1, 6, 4, 8],
#          [1, 3, 4, 6, 8, 9, 5, 2, 7],
#          [6, 7, 8, 4, 2, 5, 1, 3, 9],
#          [7, 6, 1, 8, 9, 3, 2, 5, 4],
#          [2, 9, 5, 1, 4, 7, 3, 8, 6],
#          [4, 8, 3, 5, 6, 2, 7, 9, 1]
#     ]
# square_validation(board)