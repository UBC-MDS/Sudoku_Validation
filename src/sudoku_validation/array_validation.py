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
    unique integers from 1 to 9, ignoring placeholder values used for
    incomplete boards.

    This function serves as the core validation logic for all Sudoku unit
    checks. Higher-level validation functions (e.g., row, column, square)
    are expected to transform their respective inputs into a one-dimensional
    array and delegate validation to this function.

    Parameters
    ----------
    unit : array-like of shape (9,)
        A one-dimensional array representing a Sudoku unit. The array
        must contain numeric values. Placeholder values such as 0 or None
        may be used to represent empty cells.

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
    - Placeholder values (e.g., 0 or None) are ignored when checking
      for duplicates.
    - This function does not modify the input array.

    Examples
    --------
    >>> validate_array_unit([5, 3, 4, 6, 7, 8, 9, 1, 2])
    True

    >>> validate_array_unit([5, 3, 0, 6, 7, 8, 9, 1, 5])
    False
    """