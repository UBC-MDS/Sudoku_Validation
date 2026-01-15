"""
Test the column_validation function.
"""

import pytest
from sudoku_validation.column_validation import column_validation


def test_column_validation_valid_board_example():
    """
    Test column_validation with a valid board (example 1).
    """
    board_example = [
        [3, 2, 6, 9, 7, 4, 8, 1, 5],
        [8, 1, 9, 3, 5, 6, 4, 7, 2],
        [5, 4, 7, 2, 1, 8, 9, 6, 3],
        [9, 5, 2, 7, 3, 1, 6, 4, 8],
        [1, 3, 4, 6, 8, 9, 5, 2, 7],
        [6, 7, 8, 4, 2, 5, 1, 3, 9],
        [7, 6, 1, 8, 9, 3, 2, 5, 4],
        [2, 9, 5, 1, 4, 7, 3, 8, 6],
        [4, 8, 3, 5, 6, 2, 7, 9, 1]
    ]
    assert column_validation(board_example) == True


def test_column_validation_valid_board_example_1():
    """
    Test column_validation with a valid board (example 2).
    """
    board_example_1 = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    assert column_validation(board_example_1) == True


def test_column_validation_valid_board_example_2():
    """
    Test column_validation with a valid board (example 3).
    """
    board_example_2 = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
    assert column_validation(board_example_2) == True


def test_column_validation_valid_board_example_3():
    """
    Test column_validation with a valid board (example 4).
    """
    board_example_3 = [
        [8, 1, 2, 7, 5, 3, 6, 4, 9],
        [9, 4, 3, 6, 8, 2, 1, 7, 5],
        [6, 7, 5, 4, 9, 1, 2, 8, 3],
        [1, 5, 4, 2, 3, 7, 8, 9, 6],
        [3, 6, 9, 8, 4, 5, 7, 2, 1],
        [2, 8, 7, 1, 6, 9, 5, 3, 4],
        [5, 2, 1, 9, 7, 4, 3, 6, 8],
        [4, 3, 8, 5, 2, 6, 9, 1, 7],
        [7, 9, 6, 3, 1, 8, 4, 5, 2]
    ]
    assert column_validation(board_example_3) == True


def test_column_validation_valid_board_example_4():
    """
    Test column_validation with a valid board (example 5).
    """
    board_example_4 = [
        [2, 4, 6, 8, 1, 3, 5, 7, 9],
        [1, 3, 5, 7, 9, 2, 4, 6, 8],
        [7, 9, 2, 4, 6, 8, 1, 3, 5],
        [4, 6, 8, 1, 3, 5, 7, 9, 2],
        [3, 5, 7, 9, 2, 4, 6, 8, 1],
        [9, 2, 4, 6, 8, 1, 3, 5, 7],
        [6, 8, 1, 3, 5, 7, 9, 2, 4],
        [5, 7, 9, 2, 4, 6, 8, 1, 3],
        [8, 1, 3, 5, 7, 9, 2, 4, 6]
    ]
    assert column_validation(board_example_4) == True


def test_column_validation_valid_board_example_5():
    """
    Test column_validation with a valid board (example 6).
    """
    board_example_5 = [
        [9, 6, 3, 1, 7, 4, 2, 5, 8],
        [1, 7, 8, 3, 2, 5, 6, 4, 9],
        [2, 5, 4, 6, 8, 9, 7, 3, 1],
        [8, 2, 1, 4, 3, 7, 5, 9, 6],
        [4, 9, 6, 8, 5, 2, 3, 1, 7],
        [7, 3, 5, 9, 6, 1, 4, 8, 2],
        [5, 8, 9, 7, 1, 3, 6, 2, 4],
        [3, 1, 7, 2, 4, 6, 8, 9, 5],
        [6, 4, 2, 5, 9, 8, 1, 7, 3]
    ]
    assert column_validation(board_example_5) == True


def test_column_validation_valid_board_example_6():
    """
    Test column_validation with a valid board (example 7).
    """
    board_example_6 = [
        [3, 2, 6, 9, 7, 4, 8, 1, 5],
        [8, 1, 9, 3, 5, 6, 4, 7, 2],
        [5, 4, 7, 2, 1, 8, 9, 6, 3],
        [9, 5, 2, 7, 3, 1, 6, 4, 8],
        [1, 3, 4, 6, 8, 9, 5, 2, 7],
        [6, 7, 8, 4, 2, 5, 1, 3, 9],
        [7, 6, 1, 8, 9, 3, 2, 5, 4],
        [2, 9, 5, 1, 4, 7, 3, 8, 6],
        [4, 8, 3, 5, 6, 2, 7, 9, 1]
    ]
    assert column_validation(board_example_6) == True


def test_column_validation_invalid_board_wrong_rows():
    """
    Test column_validation with board that has wrong number of rows (only 7 rows).
    """
    invalid_board_wrong_rows = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2]
    ]
    with pytest.raises(ValueError):
        column_validation(invalid_board_wrong_rows)


def test_column_validation_invalid_board_wrong_columns():
    """
    Test column_validation with board that has wrong number of columns (only 8 columns).
    """
    invalid_board_wrong_columns = [
        [0, 2, 3, 4, 5, 6, 7, 8],
        [4, 5, 6, 7, 8, 9, 1, 2],
        [7, 8, 9, 1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [5, 6, 7, 8, 9, 1, 2, 3],
        [8, 9, 1, 2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7, 8, 9, 1],
        [6, 7, 8, 9, 1, 2, 3, 4],
        [9, 1, 2, 3, 4, 5, 6, 7]
    ]
    with pytest.raises(ValueError):
        column_validation(invalid_board_wrong_columns)

def test_column_validation_invalid_board_invalid_value_zero():
    """
    Test column_validation with board containing invalid value (0 is outside 1-9 range).
    """
    invalid_board_invalid_value = [
        [0, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
    with pytest.raises(ValueError):
        column_validation(invalid_board_invalid_value)


def test_column_validation_invalid_board_invalid_value_ten():
    """
    Test column_validation with board containing invalid value (10 is outside 1-9 range).
    """
    invalid_board_invalid_value_2 = [
        [1, 2, 3, 4, 5, 6, 7, 8, 10],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
    with pytest.raises(ValueError):
        column_validation(invalid_board_invalid_value_2)


def test_column_validation_invalid_board_negative_values():
    """
    Test column_validation with board containing negative values.
    """
    invalid_board_negative_values = [
        [-1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
    with pytest.raises(ValueError):
        column_validation(invalid_board_negative_values)


def test_column_validation_invalid_board_duplicate_values():
    """
    Test column_validation with board containing duplicate values.
    """
    invalid_board_duplicate_values = [
        [1, 2, 3, 4, 4, 6, 7, 8, 9],
        [1, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
    assert column_validation(invalid_board_duplicate_values) == False
