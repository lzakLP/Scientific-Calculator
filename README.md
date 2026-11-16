# Scientific Calculator — V3.0.0

A Python scientific calculator for the terminal. It provides ten mathematical operations, input validation, error handling, and a session history of the five most recent successful calculations.

Version 3.0.0 separates mathematical operations from the terminal interface and provides reusable functions through `calculator.py`.

## Requirements

- Python 3.10 or later.
- No external dependencies.

The application was developed and manually verified with Python 3.12 on Windows.

## Installation and startup

Clone the repository:

```bash
git clone https://github.com/lzakLP/Scientific-Calculator.git
cd Scientific-Calculator
```

Run the application:

```bash
python Scientific-Calculator.py
```

On Windows, you can also use:

```powershell
py Scientific-Calculator.py
```

## Available operations

| Option | Operation |
| --- | --- |
| `1` | Addition |
| `2` | Subtraction |
| `3` | Multiplication |
| `4` | Division |
| `5` | Power |
| `6` | Square root |
| `7` | Percentage |
| `8` | Sine |
| `9` | Cosine |
| `10` | Tangent |
| `0` | View calculation history |
| `11` | Exit |

Choose an operation and enter the requested values. Trigonometric operations use angles in degrees. For percentages, enter the percentage first and the base value second.

## Input and interaction

- A period or comma can be used as the decimal separator: `2.25` and `2,25` represent the same value.
- Thousands separators are not supported. Enter one thousand as `1000`.
- Enter `m` at a numeric prompt to cancel the current operation and return to the menu.
- Invalid inputs and menu options produce explanatory messages.
- The menu remains available after a calculation, cancellation, or mathematical error.
- `Ctrl+C` or end-of-input closes the session without an error traceback.
- Output uses UTF-8 to preserve mathematical symbols, including when redirected to a file.

## Examples

| Operation and input | Expected result |
| --- | --- |
| Square root; `2.25` | `1.5` |
| Percentage; `12.5` and `200` | `25` |
| Division; `1` and `1000` | `0.001` |
| Sine; `30` degrees | Approximately `0.5` |
| Tangent; `90` degrees | Undefined-operation message |
| Square root; `-1` | Real-number restriction message |

Results are displayed with up to 12 significant digits. Scientific notation is used when appropriate. Calculation operands retain their internal floating-point values; display formatting does not change the values used in subsequent calculations.

## Mathematical rules and limitations

The calculator operates on finite real numbers using Python's `float` type.

- Division by zero and square roots of negative numbers are rejected.
- Negative bases in exponentiation require integer exponents.
- Zero raised to a negative exponent is rejected. `0 ** 0` follows Python's convention and returns `1`.
- Tangent is undefined at `90° + 180° × k`, where `k` is an integer.
- `nan`, `inf`, and `-inf` are rejected.
- Non-finite results and values outside the supported numeric range are handled as errors.
- Floating-point arithmetic is approximate. Some decimal values cannot be represented exactly, and extreme values may lose precision or underflow.

The history stores only the five most recent successful calculations during the current session. Cancelled or rejected operations are not recorded. History is cleared when the program exits.

## Code structure

```text
Scientific-Calculator/
├── Scientific-Calculator.py   Application entry point
├── calculator.py              Mathematical functions and validation
├── cli.py                     Terminal menu, input, output, and history
├── CHANGELOG.md               Version history
├── .gitignore
└── README.md
```

The mathematical functions can be imported and used without launching the terminal interface:

```python
from calculator import add, percentage, square_root

print(add(2, 3))              # 5.0
print(square_root(2.25))      # 1.5
print(percentage(12.5, 200))  # 25.0
```

The command-line interface starts only when its entry point is executed directly.

## Current scope

The current version focuses on common scientific and arithmetic operations using real numbers.

The following features are outside the current scope:

- Persistent calculation history.
- Complex-number arithmetic.
- Graphical user interface.
- External dependencies or a separate installation process.

## License

No license file is currently included in this repository. Check the repository for licensing updates before redistributing the project.
