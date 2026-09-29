# Changelog

## V3.0.0

### Added

- Reusable number and menu option input handling, with messages for invalid inputs.
- Support for either a period or comma as the decimal separator, without thousands separators.
- Operation cancellation with `m` while entering operands.
- Clean exit with `Ctrl+C` or the end of terminal input.
- UTF-8 output to preserve mathematical symbols, including when redirected on Windows.
- Validation of finite real numbers in inputs and calculations.
- Automated tests using `unittest`, without external dependencies.
- Documentation covering startup, usage, the mathematical domain, precision, and completion criteria.

### Changed

- Separated mathematical functions, the terminal interface, and the entry point.
- Protected startup with `if __name__ == "__main__":`, allowing functions to be imported without starting the menu.
- Standardized the interface and messages in English.
- Square root and percentage operations now accept decimals.
- Percentage prompts distinguish the percentage from the base value; trigonometric prompts explicitly request degrees.
- Displayed the expression alongside its result.
- Results now use up to 12 significant digits, with automatic scientific notation when appropriate, replacing the fixed two decimal places.
- Automatic return to the menu after operations, mathematical errors, or cancellation.

### Fixed

- Unexpected exits caused by letters, empty inputs, and invalid numbers.
- Failures involving negative square roots, zero raised to a negative exponent, and operations that exceed the numeric representation.
- Complex results from powers outside the chosen domain.
- A misleading large value for the tangent of `90°` and equivalent angles with a period of `180°`.
- Acceptance of non-finite values such as `nan` and `inf`.
- Repeated error messages when selecting an invalid menu option.

### Preserved

- The ten original operations.
- Menu numbering, including `0` for history and `11` to exit.
- The launch command `python Scientific-Calculator.py`.
- The history of the five most recent calculations, stored only in session memory.
- History records only successful calculations.
- The terminal interface and exclusive use of the Python standard library.

This version was prepared as a local deliverable. Publishing a release or tag in the repository is a separate step.
