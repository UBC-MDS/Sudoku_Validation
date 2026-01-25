import pytest
from sudoku_validation.row_validation import row_validation

@pytest.fixture
def valid_board():
    """Valid 9x9 Sudoku board."""
    return [
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

def test_row_validation_valid(valid_board):
    """
    Rubric: Test the 'True' branch.
    Verifies that a fully valid board returns True.
    """
    assert row_validation(valid_board)

def test_row_validation_duplicates(valid_board):
    """
    Rubric: Test the 'False' branch.
    Verifies that a row with duplicates returns False.
    """
    # Create a board with a duplicate '5' in the first row
    invalid_board = [row[:] for row in valid_board]
    invalid_board[0] = [5, 5, 4, 6, 7, 8, 9, 1, 2]
    
    assert not row_validation(invalid_board)

@pytest.mark.parametrize("invalid_input", [
    "not_a_list", # Edge Case 1: String input
    12345, # Edge Case 2: Integer input
    None, # Edge Case 3: None input
])
def test_row_validation_invalid_type(invalid_input):
    """
    Rubric: Check for defensive coding against wrong types.
    """
    with pytest.raises(ValueError, match="9x9"):
        row_validation(invalid_input)

def test_row_validation_invalid_dimensions(valid_board):
    """
    Rubric: Check for structural edge cases (wrong size).
    """
    # Edge Case 4: Board with only 8 rows
    short_board = valid_board[:-1]
    with pytest.raises(ValueError, match="9x9"):
        row_validation(short_board)

@pytest.mark.parametrize("bad_row", [
    [5, 3, 4, 6, 7, 8, 9, 1, 0], # Edge Case 5: Contains 0
    [5, 3, 4, 6, 7, 8, 9, 1, 10], # Edge Case 6: Out of range
    [5, 3, 4, 6, 7, 8, 9, 1, None], # Edge Case 7: Contains None
    [5, 3, 4, 6, 7, 8, 9, 1, "X"], # Edge Case 8: Contains String
])
def test_row_validation_invalid_content(valid_board, bad_row):
    """
    Rubric: Exception handling with useful error messages.
    Ensures that invalid content inside a row raises ValueError.
    """
    invalid_board = [row[:] for row in valid_board]
    invalid_board[0] = bad_row
    
    # Expect a ValueError that specifically mentions the row index logic: f"Invalid row at index 0..."
    with pytest.raises(ValueError, match="Invalid row at index 0"):
        row_validation(invalid_board)