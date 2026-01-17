import pytest
from sudoku_validation.square_validation import square_validation

def test_square_validation_valid_board_a():
    """A fully solved Sudoku should pass all 3×3 block checks."""
    board = [
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
    assert square_validation(board) is True


def test_square_validation_valid_board_b():
    """Another correct Sudoku arrangement should validate successfully."""
    board = [
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
    assert square_validation(board) is True


def test_square_validation_valid_board_c():
    """A patterned valid Sudoku should also pass square checks."""
    board = [
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
    assert square_validation(board) is True


def test_square_validation_invalid_shape_too_few_rows():
    """Boards missing rows should raise an error."""
    board = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
    ]
    with pytest.raises(ValueError):
        square_validation(board)


def test_square_validation_invalid_shape_too_few_columns():
    """Boards with rows of incorrect length should trigger ValueError."""
    board = [
        [1, 2, 3, 4, 5, 6, 7, 8],
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
        square_validation(board)


def test_square_validation_invalid_value_outside_range():
    """Values outside 0–9 should cause a ValueError."""
    board = [
        [10, 2, 3, 4, 5, 6, 7, 8, 9],
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
        square_validation(board)


def test_square_validation_negative_values():
    """Negative entries should not be accepted."""
    board = [
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
        square_validation(board)


def test_square_validation_duplicate_in_square():
    """A repeated number inside a 3×3 block should cause failure."""
    board = [
        [1, 1, 3, 4, 5, 6, 7, 8, 9],  # duplicate '1' in top-left block
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
    assert square_validation(board) is False
