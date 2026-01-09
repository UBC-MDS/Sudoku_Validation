# Welcome to Sudoku_Validation

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/sudoku_validation.svg)](https://pypi.org/project/sudoku_validation/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/sudoku_validation.svg)](https://pypi.org/project/sudoku_validation/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

Sudoku_Validation is a project that validates a standard 9 x 9 Sudoku board. It has the ability to validate rows only, columns only, 3x3 squares only, or the entire 9 x 9 board. 

This package contains four methods:
- `sudoku_validation()`: validates a 9 x 9 Sudoku board is a valid solution
- `array_validation()`: validates whether any array is a valid 9-integer Sudoku solution with unique integers from 1-9
- `column_validation()`: validates whether the columns of a 9 x 9 Sudoku board is a valid solution
- `row_validation()`: validates whether the rows of a 9 x 9 Sudoku board is a valid solution
- `combined_validation()`: validates whether the nine 3 x 3 squares of a 9 x 9 Sudoku board is a valid solution

There are other Python packages that provide similar functionality. Here are some examples: 
- `sudoku_py`: https://github.com/aurbano/sudoku_py
- `CodeWars-Python`: https://github.com/Peter-Liang/CodeWars-Python/blob/master/solutions/Validate_Sudoku_with_size_NxN.py

## Contributors

Justin Mak: justinmak08@gmail.com
Eric Yang: eric99yang@gmail.com
Kin Chung Choy: kcchoyaa@connect.ust.hk
Omowunmi Obadero: obaderoomowunmi@gmail.com

## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install sudoku_validation
```

To use sudoku_validation in your code:

```python
>>> import sudoku_validation
>>> sudoku_validation.combined_validation()
```

## Copyright

- Copyright © 2026 Justin Mak, Eric Yang, Kin Chung Choy, Omowunmi Obadero.
- Free software distributed under the [MIT License](./LICENSE).
