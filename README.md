# Welcome to Sudoku_Validation

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/sudoku_validation.svg)](https://pypi.org/project/sudoku_validation/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/sudoku_validation.svg)](https://pypi.org/project/sudoku_validation/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

Sudoku_Validation is a project that validates a standard 9 x 9 Sudoku board. It has the ability to validate rows only, columns only, 3x3 squares only, or the entire 9 x 9 board. 

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
- `sudoku_py`: https://github.com/aurbano/sudoku_py
- `CodeWars-Python`: https://github.com/Peter-Liang/CodeWars-Python/blob/master/solutions/Validate_Sudoku_with_size_NxN.py

> Note: this package is a work in progress and might contain example code that is not used in the final product. 

## Get started

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

## 📚 Documentation

The full documentation for this package is built using **Quarto** and **Quartodoc** and
is automatically deployed to **GitHub Pages** via GitHub Actions.

Live documentation:
[https://ubc-mds.github.io/Sudoku_Validation/](https://ubc-mds.github.io/Sudoku_Validation/)

The documentation includes:
- A full API reference generated with Quartodoc
- Usage examples for all validation functions
- Developer instructions for building and previewing documentation



## 👥 For Developers

This section provides instructions for contributors and developers working on
the Sudoku Validation package.

### Setting Up the Development Environment

#### 1. Clone the repository

```bash
git clone https://github.com/UBC-MDS/Sudoku_Validation.git
cd sudoku_validation
```

#### 2. Create an Environment Using Conda

```bash
conda env create -f environment.yml
conda activate sudoku-validation
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


## Contributing

Please check contributing for guidelines on:
Reporting bugs
Suggesting features
Submitting pull requests

## Contributors

Justin Mak: justinmak08@gmail.com
Eric Yang: eric99yang@gmail.com
Kin Chung Choy: kcchoyaa@connect.ust.hk
Omowunmi Obadero: obaderoomowunmi@gmail.com

## Copyright

- Copyright © 2026 Justin Mak, Eric Yang, Kin Chung Choy, Omowunmi Obadero.
- Free software distributed under the [MIT License](./LICENSE).
