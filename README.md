# Scientific Calculator — V3.0.0

A Python scientific calculator for the terminal, with ten operations, input validation, and a history of the five most recent calculations in the session.

V3.0.0 completes the previous version's scope with error handling, reusable calculation functions, and an English interface.

## Requirements and startup

- Python 3.10 or later.
- No external dependencies.
- Implementation and tests verified with Python 3.12.14 on Windows.

Open a terminal in this folder and run:

```console
python Scientific-Calculator.py
```

On Windows installations that use the `py` launcher, the equivalent command is:

```console
py Scientific-Calculator.py
```

## How to use

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
| `0` | History |
| `11` | Exit |

Choose an option and enter the requested values. Trigonometric operations take angles in **degrees**. For percentages, enter the percentage first, followed by the base value.

- Use a period **or** comma as the decimal separator: `2.25` and `2,25` represent the same number.
- Do not use thousands separators. For example, enter one thousand as `1000`; `1,000` means one, and `1.000,00` is rejected.
- Enter `m` at any numeric prompt to cancel the operation and return to the menu.
- The program returns to the menu after a calculation, a mathematical error, or cancellation.
- Letters, empty inputs, and invalid menu options receive helpful messages.
- `Ctrl+C` or the end of terminal input closes the session without displaying an error traceback.
- Output uses UTF-8, including when redirected to a file, to preserve mathematical symbols.

### Examples

| Selection and inputs | Expected result |
| --- | --- |
| Square root; `2.25` | `1.5` |
| Percentage; `12.5` and `200` | `25` |
| Division; `1` and `1000` | `0.001` |
| Sine; `30` degrees | Approximately `0.5` |
| Tangent; `90` degrees | Message explaining that the operation is undefined |
| Square root; `-1` | Message explaining the restriction to real numbers |

Results are displayed with up to **12 significant digits**. Scientific notation is selected automatically when appropriate. This prevents small numbers from always being displayed as `0.00`.

Operands in expressions and history preserve the `float` value used in the calculation. For example, `89.99999999999°` is not displayed as `90°` when calculating a tangent near an undefined angle.

## Mathematical rules and limitations

This calculator works with finite real numbers, using Python's `float` type.

- Division by zero and the square root of a negative number are rejected.
- A negative base in a power requires an integer exponent. Odd roots of negative bases, expressed as fractional exponents, are outside the scope of this version.
- Zero raised to a negative exponent is rejected. `0 ** 0` returns `1`, following Python's convention.
- The tangent is undefined at `90° + 180° × k`, where `k` is an integer. Angles close to those values are allowed and may produce very large results.
- Inputs such as `nan`, `inf`, and `-inf` are rejected. Infinite results and values that exceed the numeric representation are handled as errors.
- Calculations use the available internal value without first rounding it for display. However, `float` is an approximate representation: some decimals cannot be represented exactly, extreme values may lose precision, and very small results may underflow to zero.
- Extremely large angles are also subject to the limited precision of `float`.

History stores only the **five most recent successful calculations**, as text, during the session. Cancelled or rejected operations are not recorded. History is discarded when the program exits.

## Code structure

```text
Scientific-Calculator.py   Entry point that preserves the original launch command
calculator.py              Mathematical functions and validation
cli.py                     Menu, input, display, and history
tests/                     Automated tests
README.md                  Usage, rules, and limitations
CHANGELOG.md               Version changes
```

This separation allows calculations to be tested or reused without opening the menu. For example, from this folder:

```python
from calculator import add, percentage, square_root

print(add(2, 3))             # 5.0
print(square_root(2.25))     # 1.5
print(percentage(12.5, 200)) # 25.0
```

A future graphical interface or web application can call these functions and replace only the interaction layer. The `if __name__ == "__main__":` block starts the interface only when the program is executed directly.

## Tests

From the root of this folder, run:

```console
python -m unittest discover -s tests -v
```

The suite checks operations, mathematical restrictions, and interface behavior. Approximate results are compared using a numerical tolerance where necessary.

Validation for this deliverable: **27 tests passed** with Python 3.12.14 on Windows.

After changing the program, also try a manual session: perform a calculation, enter invalid input, cancel another calculation, view history, and exit. This helps check whether the messages remain clear.

## V3.0 completion criteria

The deliverable can be considered complete when a user can:

1. Run the calculator by following this README.
2. Use all ten operations, including decimal values.
3. Correct invalid inputs and continue after mathematical errors.
4. Cancel operations and navigate history.
5. Understand the rules and limitations without reading the code.
6. Run the test suite successfully.

Persistent history, complex numbers, and a graphical interface are outside the scope of this version.
