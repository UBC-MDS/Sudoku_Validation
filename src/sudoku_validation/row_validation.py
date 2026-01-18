"""
Row-level validation utilities for Sudoku boards.

This module provides functionality for validating individual rows of a
Sudoku board. Row validation is performed by extracting a single row from
the board and delegating Sudoku rule checks to the generic array validation
functions.
"""

from sudoku_validation.array_validation import array_validation

def row_validation(board):
    """
    Validate all rows of a Sudoku board.

    This function iterates through every row in the provided board and
    validates it according to Sudoku rules by delegating to the 
    validate_array_unit function.

    Parameters
    ----------
    board : list of lists
        A two-dimensional list representing a 9x9 Sudoku board.
        Must contain integers from 1 to 9.

    Returns
    -------
    bool
        True if ALL rows are valid Sudoku units (no duplicates).
        False if ANY row contains duplicate values.

    Raises
    ------
    ValueError
        If the board is not a list, is not of length 9, contains
        rows of invalid length, or contains non-integer values/placeholders.
    """
    # Basic board validation
    if not isinstance(board, list) or len(board) != 9:
        raise ValueError("Board must be a 9x9 list of lists.")

    # 2. Iterate and Validate
    for i, row in enumerate(board):
        # Passing the rest of the validation to array_validation.
        # It raises ValueError if the row has bad types/lengths/ranges.
        # It returns False if the row has duplicates.
        try:
            is_valid = array_validation(row)
        except ValueError as e:
            raise ValueError(f"Invalid row at index {i}: {str(e)}") from e
        if not is_valid:
            return False

    return True