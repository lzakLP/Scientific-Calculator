"""Calculator terminal interface. Run this file or the launcher."""

import math
import sys
from typing import Callable

from calculator import (
    CalculationError,
    add,
    cosine,
    divide,
    multiply,
    percentage,
    power,
    sine,
    square_root,
    subtract,
    tangent,
)

VERSION = "3.0.0"
HISTORY_LIMIT = 5

# Each operation groups its name, function, prompts, and expression template.
Operation = tuple[str, Callable[..., float], tuple[str, ...], str]
OPERATIONS: dict[str, Operation] = {
    "1": ("Add", add, ("First number", "Second number"), "{0} + {1}"),
    "2": ("Subtract", subtract, ("First number", "Second number"), "{0} − {1}"),
    "3": ("Multiply", multiply, ("First number", "Second number"), "{0} × {1}"),
    "4": ("Divide", divide, ("Dividend", "Divisor"), "{0} ÷ {1}"),
    "5": ("Power", power, ("Base", "Exponent"), "({0}) ^ ({1})"),
    "6": ("Square root", square_root, ("Number",), "√({0})"),
    "7": ("Percentage", percentage, ("Percentage", "Base value"), "{0}% of {1}"),
    "8": ("Sine", sine, ("Angle in degrees",), "sin({0}°)"),
    "9": ("Cosine", cosine, ("Angle in degrees",), "cos({0}°)"),
    "10": ("Tangent", tangent, ("Angle in degrees",), "tan({0}°)"),
}


def format_number(value: float) -> str:
    """Round only the display, preserving small and large numbers."""
    if value == 0:
        return "0"
    return f"{value:.12g}"


def _format_operand(value: float) -> str:
    """Preserve the operand in the expression without rounding it to 12 digits."""
    if value == 0:
        return "0"
    text = str(value)
    return text[:-2] if text.endswith(".0") else text


def read_number(prompt: str) -> float | None:
    """Keep prompting until a valid number is entered, or m is used to cancel."""
    while True:
        text = input(f"{prompt} (m = menu): ").strip()
        if text.lower() == "m":
            return None

        # A comma is a decimal separator; thousands separators are not supported.
        if not text or "_" in text or ("," in text and "." in text):
            print("Error: enter a number using a decimal point or comma, without thousands separators.")
            continue
        try:
            number = float(text.replace(",", "."))
        except ValueError:
            print("Error: enter a valid number or m to return to the menu.")
            continue
        if not math.isfinite(number):
            print("Error: enter a finite number; nan and inf are not accepted.")
            continue
        return number


def read_option() -> str:
    while True:
        option = input("Choose an option: ").strip()
        if option in OPERATIONS or option in {"0", "11"}:
            return option
        print("Error: invalid option. Choose a number from 0 to 11.")


def add_to_history(history: list[str], operation: str) -> None:
    history.append(operation)
    del history[:-HISTORY_LIMIT]


def show_history(history: list[str]) -> None:
    print("\n========== History ==========")
    if not history:
        print("No operations performed in this session.")
    else:
        for number, operation in enumerate(history, start=1):
            print(f"{number}. {operation}")


def show_menu() -> None:
    print(f"\n======= Scientific Calculator v{VERSION} =======")
    for option, (name, _, _, _) in OPERATIONS.items():
        print(f"{option:>2}. {name}")
    print(" 0. History")
    print("11. Exit")
    print("Trigonometry in degrees | m cancels a calculation")


def execute_operation(operation: Operation, history: list[str]) -> None:
    _, calculate, prompts, expression_template = operation
    values = []
    for prompt in prompts:
        value = read_number(prompt)
        if value is None:
            print("Operation canceled.")
            return
        values.append(value)

    try:
        result = calculate(*values)
    except CalculationError as error:
        print(f"Error: {error}")
        return

    expression = expression_template.format(*(_format_operand(value) for value in values))
    operation_text = f"{expression} = {format_number(result)}"
    print(f"Result: {operation_text}")
    add_to_history(history, operation_text)


def main() -> None:
    # Preserve mathematical symbols when redirecting output on Windows.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    # History belongs to this session, with no mutable global state.
    history: list[str] = []
    try:
        while True:
            show_menu()
            option = read_option()
            if option == "11":
                break
            if option == "0":
                show_history(history)
            else:
                execute_operation(OPERATIONS[option], history)
    except (KeyboardInterrupt, EOFError):
        print("\nSession interrupted.")
    print("Goodbye!")


if __name__ == "__main__":
    main()
