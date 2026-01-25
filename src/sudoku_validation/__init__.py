# MIT License
#
# Copyright (c) 2026 Justin Mak, Eric Yang, Kin Chung Choy, Omowunmi Obadero
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Sudoku Validation Package.

A comprehensive package for validating Sudoku puzzles according to standard rules.
This package provides functions to validate individual rows, columns, 3x3 squares,
or entire 9x9 Sudoku boards.

Functions
---------
array_validation : Validate a single 1D array as a Sudoku unit
row_validation : Validate all rows of a Sudoku board
column_validation : Validate all columns of a Sudoku board
square_validation : Validate all 3x3 squares of a Sudoku board
combined_validation : Validate entire Sudoku board

Examples
--------
>>> from sudoku_validation import combined_validation
>>> board = [
...     [5, 3, 4, 6, 7, 8, 9, 1, 2],
...     [6, 7, 2, 1, 9, 5, 3, 4, 8],
...     [1, 9, 8, 3, 4, 2, 5, 6, 7],
...     [8, 5, 9, 7, 6, 1, 4, 2, 3],
...     [4, 2, 6, 8, 5, 3, 7, 9, 1],
...     [7, 1, 3, 9, 2, 4, 8, 5, 6],
...     [9, 6, 1, 5, 3, 7, 2, 8, 4],
...     [2, 8, 7, 4, 1, 9, 6, 3, 5],
...     [3, 4, 5, 2, 8, 6, 1, 7, 9]
... ]
>>> combined_validation(board)
True
"""

from sudoku_validation.array_validation import array_validation
from sudoku_validation.row_validation import row_validation
from sudoku_validation.column_validation import column_validation
from sudoku_validation.square_validation import square_validation
from sudoku_validation.combined_validation import combined_validation

__all__ = [
    "array_validation",
    "row_validation", 
    "column_validation",
    "square_validation",
    "combined_validation",
]
