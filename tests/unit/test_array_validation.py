import pytest
from sudoku_validation.array_validation import array_validation

def test_valid_array():
    valid_unit = [5, 3, 4, 6, 7, 8, 9, 1, 2]
    assert array_validation(valid_unit)

def test_invalid_array_duplicates():
    # Array with duplicate '5' at column 8
    invalid_unit = [5, 3, 4, 6, 7, 8, 9, 1, 5]
    assert not array_validation(invalid_unit)

def test_invalid_array_length():
    # Array with only 8 elements
    invalid_unit = [5, 3, 4, 6, 7, 8, 9, 1]
    with pytest.raises(ValueError):
        array_validation(invalid_unit)

def test_invalid_array_non_integer():
    # Array with a string element at column 2
    invalid_unit = [5, 3, '4', 6, 7, 8, 9, 1, 2]
    with pytest.raises(ValueError):
        array_validation(invalid_unit)

def test_invalid_array_out_of_range():
    # Array with an out-of-range value '10' at column 3
    invalid_unit = [5, 3, 10, 6, 7, 8, 9, 1, 2]
    with pytest.raises(ValueError):
        array_validation(invalid_unit)

def test_invalid_array_type():
    # Input is a string instead of a list
    invalid_unit = "5,3,4,6,7,8,9,1,2"
    with pytest.raises(TypeError):
        array_validation(invalid_unit)
