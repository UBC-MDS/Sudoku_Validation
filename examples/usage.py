"""Runnable usage examples for the sudoku_validation package.

Run this script to see demonstration outputs for all exported functions.
"""
from sudoku_validation.array_validation import array_validation
from sudoku_validation.row_validation import row_validation
from sudoku_validation.column_validation import column_validation
from sudoku_validation.square_validation import square_validation
from sudoku_validation.combined_validation import combined_validation


complete = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

incomplete = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


def main():
    print('--- array_validation ---')
    print('valid unit ->', array_validation([5,3,4,6,7,8,9,1,2]))
    print('invalid unit ->', array_validation([5,3,4,6,7,8,9,1,5]))

    print('\n--- row_validation ---')
    print('complete board ->', row_validation(complete))

    print('\n--- column_validation ---')
    print('complete board ->', column_validation(complete))

    print('\n--- square_validation ---')
    print('complete board ->', square_validation(complete))

    print('\n--- combined_validation ---')
    print('complete board ->', combined_validation(complete))
    print('incomplete (valid) board ->', combined_validation(incomplete))


if __name__ == '__main__':
    main()
