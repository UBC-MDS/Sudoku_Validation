'''
Add 4 unit test to trigger checks
'''
import pytest
from sudoku_validation.row_validation import row_validation

def test_validate_rows_valid():
    board = [
        [1,2,3,4,5,6,7,8,9],
        [4,5,6,7,8,9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [2,3,4,5,6,7,8,9,1],
        [5,6,7,8,9,1,2,3,4],
        [8,9,1,2,3,4,5,6,7],
        [3,4,5,6,7,8,9,1,2],
        [6,7,8,9,1,2,3,4,5],
        [9,1,2,3,4,5,6,7,8],
    ]
    assert row_validation(board)

def test_validate_rows_duplicate():
    board = [
        [1,1,3,4,5,6,7,8,9],  # duplicate 1
    ] + [[0]*9 for _ in range(8)]
    assert not row_validation(board)

def test_validate_rows_non_numeric():
    board = [
        ["a",2,3,4,5,6,7,8,9],
    ] + [[0]*9 for _ in range(8)]
    with pytest.raises(ValueError):
        row_validation(board)

def test_validate_rows_short_row():
    board = [
        [1,2,3],  # too short
    ] + [[0]*9 for _ in range(8)]
    with pytest.raises(ValueError):
        row_validation(board)
