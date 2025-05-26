"""Polygon Calculator.

Provides classes to represent and manipulate shapes
"""


class Rectangle:
    """A class to represent a rectangle with width and height."""

    def __init__(self, width: float, height: float) -> None:
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height

    def __str__(self) -> str:
        """Return a string representation of the rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: float) -> None:
        """Set the width of the rectangle."""
        self.width = width

    def set_height(self, height: float) -> None:
        """Set the height of the rectangle."""
        self.height = height

    def get_width(self) -> float:
        """Return the width of the rectangle."""
        return self.width

    def get_height(self) -> float:
        """Return the height of the rectangle."""
        return self.height

    def get_area(self) -> float:
        """Return the area of the rectangle."""
        return self.width * self.height

    def get_perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        """Return the diagonal of the rectangle."""
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self) -> str:
        """Return a string representation of the rectangle as a picture."""
        if max(self.width, self.height) > 50:
            return "Too big for picture."
        output_string: str = ""
        for _ in range(int(self.height)):
            output_string += "*" * int(self.width) + "\n"
        return output_string

    def get_amount_inside(self, shape: 'Rectangle') -> int:
        """Return the number of times the given shape can fit inside this rectangle."""
        amount: int = 0
        amount += int(self.width // shape.get_width())
        amount *= int(self.height // shape.get_height())
        return amount


class Square(Rectangle):
    """A class to represent a square, which is a rectangle with equal width and height."""

    def __init__(self, side: float) -> None:
        """Initialize a square with side."""
        self.width = side
        self.height = side

    def __str__(self) -> str:
        """Return a string representation of the square."""
        return f"Square(side={self.width})"

    def set_side(self, side: float) -> None:
        """Set all sides of a square."""
        self.width = side
        self.height = side

    def set_width(self, width: float) -> None:
        """Set all sides of a square."""
        self.width = width
        self.height = width

    def set_height(self, height: float) -> None:
        """Set all sides of a square."""
        self.height = height
        self.width = height


if __name__ == "__main__":
    print("running polygon calculator")
    rect = Rectangle(10, 5)
    rect.set_height(4)
    print(rect)
    # print(rect.get_picture())

    reat2 = Rectangle(3, 2)
    # print(rect.get_amount_inside(reat2))

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())


    # print(rect.get_area())
    # print(rect.get_perimeter())
    # print(rect)
    # print(rect.get_picture())