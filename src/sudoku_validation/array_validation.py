"""
Core validation utilities for Sudoku array units.

This module provides generic validation functionality for checking
whether one-dimensional array-like objects represent valid Sudoku
units. Higher-level validation functions for rows, columns, and
subgrids rely on the functions defined here.
"""

def array_validation(unit):
    """
    Validate whether an array represents a valid Sudoku unit.

    This function checks whether the provided array corresponds to a valid
    Sudoku unit (row, column, or 3x3 square). A valid unit must contain
    unique integers from 1 to 9.

    This function serves as the core validation logic for all Sudoku unit
    checks. Higher-level validation functions (e.g., row, column, square)
    are expected to transform their respective inputs into a one-dimensional
    array and delegate validation to this function.

    Parameters
    ----------
    unit : array-like of shape (9,)
        A one-dimensional array representing a Sudoku unit. The array
        must contain numeric values.

    Returns
    -------
    bool
        True if the array represents a valid Sudoku unit according to
        Sudoku rules; False otherwise.

    Raises
    ------
    ValueError
        If the input cannot be interpreted as a one-dimensional array
        of length 9.

    Notes
    -----
    - A valid Sudoku unit contains no duplicate values among the digits
      1 through 9.
    - This function does not modify the input array.

    Examples
    --------
    >>> array_validation([5, 3, 4, 6, 7, 8, 9, 1, 2])
    True

    >>> array_validation([5, 3, 0, 6, 7, 8, 9, 1, 5])
    False
    """
    # Basic input validation
    if not isinstance(unit, list):
        raise TypeError("Input array must not be a list.")
    if len(unit) != 9:
        raise ValueError("Input array must be of length 9.")
    if not all(isinstance(x, int) for x in unit):
        raise ValueError("All elements must be integers.")
    if not all(1 <= x <= 9 for x in unit):
        raise ValueError("Elements must be in the range 1-9.")

    # Return False if sum exceeds expected sum
    seen = set()
    for number in unit:
        if number in seen:
            return False
        seen.add(number)
    return True