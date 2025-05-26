import pytest
from pc import Rectangle, Square


def test_get_area() -> None:
    """Test the get_area method of Rectangle."""
    rect = Rectangle(10, 5)
    expected = 50
    results = rect.get_area()
    assert results == expected, f'Expected :{expected!a} but got :{results!a}'


def test_get_perimeter() -> None:
    """Test the perimeter of a rectangle."""
    rect = Rectangle(10, 5)
    rect.set_height(3)
    expected = 26
    results = rect.get_perimeter()
    assert results == expected, f'Expected :{expected!a} but got :{results!a}'


def test_string() -> None:
    """Test the string representation of a rectangle."""
    rect = Rectangle(10, 3)
    expected = "Rectangle(width=10, height=3)"
    results = str(rect)
    assert results == expected, f'Expected :{expected!a} but got :{results!a}'


def test_get_picture() -> None:
    """Test the get_picture method of Rectangle."""
    rect = Rectangle(10, 3)
    expected = "**********\n" * 3
    results = rect.get_picture()
    assert results == expected, f'Expected :{expected!a} but got :{results!a}'
