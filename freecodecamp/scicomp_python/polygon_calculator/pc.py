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

    def get_picture(self) -> str:
        output_string: str = ""
        for line in range(int(self.height)):
            output_string += "*" * int(self.width) + "\n"
        return output_string


class Square:
    pass


if __name__ == "__main__":
    print("running polygon calculator")
    rect = Rectangle(10, 5)
    rect.set_height(3)
    print(rect.get_picture())

    # print(rect.get_area())
    # print(rect.get_perimeter())
    # print(rect)
    # print(rect.get_picture())