"""
Test the combined_validation function using two predefined boards.
"""

import pytest
from copy import deepcopy
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from sudoku_validation.combined_validation import combined_validation


# Fully solved valid board
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
    board[0] = "not a list"
    with pytest.raises(TypeError):
        combined_validation(board)


def test_cell_not_int():
    """Raise TypeError if any cell is not an integer."""
    board = deepcopy(VALID_COMPLETE_BOARD)
    board[0][0] = "5"
    with pytest.raises(TypeError):
        combined_validation(board)


