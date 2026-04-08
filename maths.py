"""Basic maths utility functions.

This module provides a small, dependency-free set of arithmetic helpers
suitable as a foundation for future feature work in this repository.
"""

from __future__ import annotations

from math import gcd as _gcd
from typing import Iterable


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the result of subtracting ``b`` from ``a``."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return ``a / b``.

    Raises:
        ValueError: If ``b`` is zero.
    """
    if b == 0:
        raise ValueError('division by zero is not allowed')
    return a / b


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer.

    Raises:
        ValueError: If ``n`` is negative.
        TypeError: If ``n`` is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError('factorial is only defined for integers')
    if n < 0:
        raise ValueError('factorial is only defined for non-negative integers')
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def mean(values: Iterable[float]) -> float:
    """Return the arithmetic mean of a non-empty iterable of numbers.

    Raises:
        ValueError: If ``values`` is empty.
    """
    items = list(values)
    if not items:
        raise ValueError('mean requires at least one value')
    return sum(items) / len(items)


def is_prime(n: int) -> bool:
    """Return True when ``n`` is prime, otherwise False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    factor = 5
    while factor * factor <= n:
        if n % factor == 0 or n % (factor + 2) == 0:
            return False
        factor += 6
    return True


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers."""
    return _gcd(a, b)
