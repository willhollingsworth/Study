"""Probability Calculator.

made for FreeCodeCamp's Scientific Computing with Python course.
"""
import random


class Hat:
    """Hat class to represent a collection of coloured balls."""

    def __init__(self, **kwargs: int) -> None:
        """Initialize the Hat with a variable number of coloured balls."""
        self.contents: list[str] = []
        for color, count in kwargs.items():
            for _ in range(count):
                self.contents.append(color)

    def draw(self, num_balls: int) -> list[str]:
        """Draw a specified number of balls from the hat."""
        returned_balls: list[str] = []
        draw_count: int = min(num_balls, len(self.contents))
        for _ in range(draw_count):
            chosen_ball: str = random.choice(self.contents)
            self.contents.remove(chosen_ball)
            returned_balls.append(chosen_ball)
        return returned_balls

# def experiment(hat: 'Hat', expected_balls, num_balls_drawn, num_experiments):
#     pass


if __name__ == "__main__":
    hat1 = Hat(yellow=3, blue=2, green=6)
    print(hat1.draw(12))
    # hat2 = Hat(red=5, orange=4)
    # hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)