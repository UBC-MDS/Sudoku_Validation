# Welcome to Sudoku_Validation
[Sudoku_Validation](https://github.com/UBC-MDS/Sudoku_Validation) is a Python package designed to validate standard 9x9 Sudoku boards. It provides robust, defensive functions to check the validity of rows, columns, 3x3 squares, and the entire board, ensuring that each unit contains unique integers from 1 to 9. The package is suitable for both end-users and developers who need reliable Sudoku validation in their applications or data pipelines.


## Package Contents {#package-contents}

- **combined_validation(board)**: Validates whether a 9x9 Sudoku board is a complete and correct solution, checking all rows, columns, and 3x3 squares.
- **array_validation(arr)**: Checks if a one-dimensional array represents a valid Sudoku unit (9 unique integers between 1 and 9). Used as a helper in other functions.
- **column_validation(board)**: Validates that each column in a 9x9 Sudoku board contains all digits from 1 to 9 exactly once.
- **row_validation(board)**: Validates that each row in a 9x9 Sudoku board contains all digits from 1 to 9 exactly once.
- **square_validation(board)**: Validates that each 3x3 square in a 9x9 Sudoku board contains all digits from 1 to 9 exactly once.

## Position in the Python Ecosystem {#position-in-the-python-ecosystem}

Sudoku_Validation fits into the Python ecosystem as a specialized utility for Sudoku board validation. While there are other Python packages with similar functionality, such as [sudoku_py](https://github.com/aurbano/sudoku_py) and [CodeWars-Python's Validate_Sudoku_with_size_NxN](https://github.com/Peter-Liang/CodeWars-Python/blob/master/solutions/Validate_Sudoku_with_size_NxN.py), this package emphasizes defensive programming and informative error handling. If you need a focused, well-documented, and reliable Sudoku validation tool, Sudoku_Validation is a strong choice among available Python solutions.

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/sudoku_validation.svg)](https://pypi.org/project/sudoku_validation/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/sudoku_validation.svg)](https://pypi.org/project/sudoku_validation/)  [![codecov](https://codecov.io/github/UBC-MDS/Sudoku_Validation/graph/badge.svg?token=Hk51HZyYd4)](https://codecov.io/github/UBC-MDS/Sudoku_Validation)|
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

[Sudoku_Validation](https://github.com/UBC-MDS/Sudoku_Validation) is a project that validates a standard 9 x 9 Sudoku board. It has the ability to validate rows only, columns only, 3x3 squares only, or the entire 9 x 9 board. 

This package contains five methods:

- `combined_validation()`: validates a 9 x 9 Sudoku board is a valid solution

- `array_validation()`: validates whether a one-dimensional array represents a valid Sudoku unit (contains 9 integers and each integer is unique and between 1 and 9). Returns True if valid, False otherwise. Other functions in this package use this function as a helper function.

- `column_validation()`: validates whether the columns of a 9 x 9 Sudoku board is a valid solution

- `row_validation()`: validates whether the rows of a 9 x 9 Sudoku board is a valid solution

- `square_validation()`: validates whether the nine 3 x 3 squares of a 9 x 9 Sudoku board is a valid solution

**Input Requirements**
All validation functions expect a 9 x 9 Sudoku board represented as a list of lists containing integers from 1 to 9. For example:

```python
sudoku_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6,  1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
```
> Note: Invalid shapes or values will raise an exception.
> 
> Note: All functions are written defensively and will raise informative exceptions
when invalid input is detected.

There are other Python packages that provide similar functionality. Here are some examples: 
- `sudoku_py`: [https://github.com/aurbano/sudoku_py](https://github.com/aurbano/sudoku_py)
- `CodeWars-Python`: [https://github.com/Peter-Liang/CodeWars-Python/blob/master/solutions/Validate_Sudoku_with_size_NxN.py](https://github.com/Peter-Liang/CodeWars-Python/blob/master/solutions/Validate_Sudoku_with_size_NxN.py)

> Note: this package is a work in progress and might contain example code that is not used in the final product. 

## Get started {#get-started}

You can install this package into your preferred Python environment using pip:

```bash
$ pip install sudoku_validation
```

To use sudoku_validation in your code:

```python
import sudoku_validation

sudoku_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6,  1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

sudoku_validation.combined_validation(sudoku_board)
```

## Usage (runnable examples)

The following examples demonstrate all exported functions. You can copy these snippets into a script or run the `examples/usage.py` script included with this repository.

```python
from sudoku_validation.array_validation import array_validation
from sudoku_validation.row_validation import row_validation
from sudoku_validation.column_validation import column_validation
from sudoku_validation.square_validation import square_validation
from sudoku_validation.combined_validation import combined_validation

# Example boards
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

# array_validation
print('array_validation (valid unit):', array_validation([5,3,4,6,7,8,9,1,2]))
print('array_validation (invalid unit):', array_validation([5,3,4,6,7,8,9,1,5]))

# row_validation
print('row_validation (complete board):', row_validation(complete))

# column_validation
print('column_validation (complete board):', column_validation(complete))

# square_validation
print('square_validation (complete board):', square_validation(complete))

# combined_validation
print('combined_validation (complete board):', combined_validation(complete))
print('combined_validation (incomplete but valid):', combined_validation(incomplete))
```

## Documentation {#documentation}

The full documentation for this package is built using **Quarto** and **Quartodoc** and
is automatically deployed to **GitHub Pages** via GitHub Actions.

Live documentation:
[https://ubc-mds.github.io/Sudoku_Validation/](https://ubc-mds.github.io/Sudoku_Validation/)

The documentation includes:
- A full API reference generated with Quartodoc
- Usage examples for all validation functions
- Developer instructions for building and previewing documentation



## For Developers {#for-developers}

This section provides instructions for contributors and developers working on
the Sudoku Validation package.

### Setting Up the Development Environment

#### 1. Clone the repository

```bash
git clone https://github.com/UBC-MDS/Sudoku_Validation.git
cd Sudoku_Validation
```

#### 2. Create an Environment Using Conda

```bash
conda env create -f environment.yml
conda activate sudoku_validation
```

#### 3. Install the package in Development Mode

```bash
pip install -e ".[dev]"
```

#### Running Tests

Execute the full test suite:
```bash
pytest 
``` 

#### Building Documentation

Build documentation locally:
```bash
cd docs
quarto render
```
To preview documentation in a browser:
```bash
quarto preview
```

## Continuous Integration and Deployment

All tests, formatting checks and documentation builds are automatically built and deployed using GitHub Actions.
On every push to the main branch, Quarto renders the documentation and publishes
it to GitHub Pages.
No manual deployment steps are required.


## Contributing {#contributing}

Please check contributing for guidelines on:
Reporting bugs
Suggesting features
Submitting pull requests

## Contributors {#contributors}

Justin Mak: justinmak08@gmail.com

Eric Yang: eric99yang@gmail.com

Kin Chung Choy: kcchoyaa@connect.ust.hk

Omowunmi Obadero: obaderoomowunmi@gmail.com

## Copyright {#copyright}

- Copyright © 2026 Justin Mak, Eric Yang, Kin Chung Choy, Omowunmi Obadero.
- Free software distributed under the [MIT License](./LICENSE).
