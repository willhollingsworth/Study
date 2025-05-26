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


def test_get_diagonal() -> None:
    """Test the diagonal of a rectangle."""
    rect = Rectangle(4, 4)
    expected = 5.656854249492381
    results = rect.get_diagonal()
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


def test_get_picture_too_big() -> None:
    """Test the get_picture method of Rectangle with a too big rectangle."""
    rect = Rectangle(60, 3)
    expected = "Too big for picture."
    results = rect.get_picture()
    assert results == expected, f'Expected :{expected!a} but got :{results!a}'


def test_get_amount_inside() -> None:
    """Test the get_amount_inside method of Rectangle."""
    rect = Rectangle(10, 2)
    small_rect = Rectangle(3, 1)
    expected = 6
    results = rect.get_amount_inside(small_rect)
    assert results == expected, f'Expected :{expected!a} but got :{results!a}'
