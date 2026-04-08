import pytest

import maths


def test_basic_arithmetic_operations():
    assert maths.add(2, 3) == 5
    assert maths.subtract(10, 4) == 6
    assert maths.multiply(6, 7) == 42
    assert maths.divide(9, 2) == 4.5


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match='division by zero'):
        maths.divide(10, 0)


@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        (0, 1),
        (1, 1),
        (5, 120),
    ],
)
def test_factorial(value, expected):
    assert maths.factorial(value) == expected


def test_factorial_rejects_negative_values():
    with pytest.raises(ValueError, match='non-negative'):
        maths.factorial(-1)


def test_factorial_rejects_non_integers():
    with pytest.raises(TypeError, match='integers'):
        maths.factorial(3.5)


def test_mean():
    assert maths.mean([1, 2, 3, 4]) == 2.5
    assert maths.mean((2, 4)) == 3


def test_mean_rejects_empty_iterables():
    with pytest.raises(ValueError, match='at least one'):
        maths.mean([])


@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        (-5, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (29, True),
    ],
)
def test_is_prime(value, expected):
    assert maths.is_prime(value) is expected


def test_gcd():
    assert maths.gcd(54, 24) == 6
    assert maths.gcd(-54, 24) == 6
