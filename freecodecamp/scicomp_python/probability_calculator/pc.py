"""Probability Calculator.

made for FreeCodeCamp's Scientific Computing with Python course.
"""
import copy
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


def experiment(
        hat: 'Hat',
        expected_balls: dict[str, int],
        num_balls_drawn: int,
        num_experiments: int,
        ) -> float:
    """Determine ball probabilities.

    Draw a given number of times to work out the chance
    of getting the expected ball combination.
    """
    successful_experiments: int = 0
    for _ in range(num_experiments):
        hat_copy: Hat = copy.deepcopy(hat)
        drawn_balls: list[str] = hat_copy.draw(num_balls_drawn)
        failed_experiment: bool = False
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                failed_experiment = True
        if not failed_experiment:
            successful_experiments += 1
    return successful_experiments / num_experiments


if __name__ == "__main__":
    hat = Hat(black=6, red=4, green=3)
    probability: float = experiment(
        hat=hat,
        expected_balls={'red': 2, 'green': 1},
        num_balls_drawn=5,
        num_experiments=20,
    )
    print(f"Probability: {probability}")
