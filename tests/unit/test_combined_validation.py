"""
Test the combined_validation function using two predefined boards.
"""

import pytest
from copy import deepcopy
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from sudoku_validation.combined_validation import combined_validation


# Fully solved valid board (no blanks)
VALID_COMPLETE_BOARD = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9],
]

# Valid but incomplete board
# Zeros indicate blanks. Example blank locations (1-based):
# - row 1, col 3 = 0 (index [0][2])
# - row 1, col 4 = 0 (index [0][3])
# - row 3, col 1 = 0 (index [2][0])
# - row 9, col 1 = 0 (index [8][0])
VALID_INCOMPLETE_BOARD = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def test_input_not_list():
    """Raise TypeError if input is not a list."""
    with pytest.raises(TypeError):
        combined_validation("not a list")


def test_row_not_list():
    """Raise TypeError if any row is not a list."""
    board = deepcopy(VALID_COMPLETE_BOARD)
    # Replace row 1 (index [0]) with a non-list to test type checking
    board[0] = "not a list"
    with pytest.raises(TypeError):
        combined_validation(board)


def test_cell_not_int():
    """Raise TypeError if any cell is not an integer."""
    board = deepcopy(VALID_COMPLETE_BOARD)
    # Make cell non-int at row 1, col 1 (1-based); index [0][0]
    board[0][0] = "5"
    with pytest.raises(TypeError):
        combined_validation(board)


def test_invalid_number_of_rows():
    """Raise ValueError if board does not have 9 rows."""
    # Remove last row (row 9) to create an 8-row board
    board = deepcopy(VALID_COMPLETE_BOARD[:8])
    with pytest.raises(ValueError):
        combined_validation(board)


def test_invalid_number_of_columns():
    """Raise ValueError if any row does not have 9 columns."""
    # Truncate each row to 8 columns (removed column 9) to test column count
    board = [row[:8] for row in deepcopy(VALID_COMPLETE_BOARD)]
    with pytest.raises(ValueError):
        combined_validation(board)


def test_row_duplicate_returns_false():
    """Return False if a row contains duplicates."""
    board = deepcopy(VALID_COMPLETE_BOARD)
    # Introduce duplicate 5 in row 1 at columns 1 and 2 (1-based); indices [0][0] and [0][1]
    board[0][0] = 5
    board[0][1] = 5  
    assert not combined_validation(board)


def test_column_duplicate_returns_false():
    """Return False if a column contains duplicates."""
    board = deepcopy(VALID_COMPLETE_BOARD)
    # Introduce duplicate 7 in column 1 at row 1 and row 2 (1-based); indices [0][0] and [1][0]
    board[0][0] = 7
    board[1][0] = 7  
    assert not combined_validation(board)


def test_block_duplicate_returns_false():
    """Return False if a 3x3 block contains duplicates."""
    board = deepcopy(VALID_COMPLETE_BOARD)
    # Introduce duplicate 9 inside the top-left 3x3 block at
    # row 1 col 1 and row 2 col 2 (1-based); indices [0][0] and [1][1]
    board[0][0] = 9
    board[1][1] = 9  
    assert not combined_validation(board)


def test_valid_complete_board_returns_true():
    """Return True for a valid, complete Sudoku board."""
    assert combined_validation(VALID_COMPLETE_BOARD)


def test_valid_incomplete_board_returns_true():
    """Return True for a valid, incomplete board."""
    assert combined_validation(VALID_INCOMPLETE_BOARD)
