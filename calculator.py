"""Calculator V3.0 operations: finite real numbers and angles in degrees."""

import math


class CalculationError(ValueError):
    """A calculation error that the interface can explain to the user."""


def _number(value: float) -> float:
    """Validate direct function calls as well as values entered through the menu."""
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise CalculationError("Enter a finite real number.") from error
    if not math.isfinite(number):
        raise CalculationError("Enter a finite real number; nan and inf are not accepted.")
    return number


def _result(value: float) -> float:
    if not math.isfinite(value):
        raise CalculationError("The result exceeds the calculator's numeric range.")
    return value


def add(a: float, b: float) -> float:
    return _result(_number(a) + _number(b))


def subtract(a: float, b: float) -> float:
    return _result(_number(a) - _number(b))


def multiply(a: float, b: float) -> float:
    return _result(_number(a) * _number(b))


def divide(a: float, b: float) -> float:
    a, b = _number(a), _number(b)
    if b == 0:
        raise CalculationError("Division by zero is not allowed.")
    return _result(a / b)


def power(a: float, b: float) -> float:
    a, b = _number(a), _number(b)
    if a == 0 and b < 0:
        raise CalculationError("Zero cannot be raised to a negative exponent.")
    if a < 0 and not b.is_integer():
        raise CalculationError("In this version, negative bases require integer exponents.")
    try:
        return _result(a ** b)
    except OverflowError as error:
        raise CalculationError("The result exceeds the calculator's numeric range.") from error


def square_root(a: float) -> float:
    a = _number(a)
    if a < 0:
        raise CalculationError("The square root of a negative number is not real.")
    return math.sqrt(a)


def percentage(a: float, b: float) -> float:
    """Calculate a percent of the base value b, including decimal values."""
    a, b = _number(a), _number(b)
    # Dividing the larger factor first avoids unnecessary intermediate overflow.
    result = (a / 100) * b if abs(a) >= abs(b) else a * (b / 100)
    return _result(result)


def sine(a: float) -> float:
    angle = math.remainder(_number(a), 360.0)
    # Exact values on the axes avoid residuals such as sin(180°) = 1.22e-16.
    axis_values = {0.0: 0.0, 90.0: 1.0, -90.0: -1.0, 180.0: 0.0, -180.0: 0.0}
    if angle in axis_values:
        return axis_values[angle]
    return math.sin(math.radians(angle))


def cosine(a: float) -> float:
    angle = math.remainder(_number(a), 360.0)
    axis_values = {0.0: 1.0, 90.0: 0.0, -90.0: 0.0, 180.0: -1.0, -180.0: -1.0}
    if angle in axis_values:
        return axis_values[angle]
    return math.cos(math.radians(angle))


def tangent(a: float) -> float:
    angle = math.remainder(_number(a), 180.0)
    if abs(angle) == 90.0:
        raise CalculationError("Tangent is undefined at 90° + 180° × k, where k is an integer.")
    # Exact comparison preserves angles close to, but different from, 90°.
    return _result(math.tan(math.radians(angle)))
