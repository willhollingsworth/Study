"""Advent of Code 2024 Utilities."""  # noqa: INP001

import numpy as np
from numpy.typing import NDArray

class Coords(tuple[int, int]):
    """Tuple for holding and better adding of coordinates."""

    def __new__(cls, row: int, col: int) -> 'Coords':
        return super().__new__(cls, (int(row), int(col)))

    def __add__(self, other: 'Coords') -> 'Coords':
        """ Add two coordinates together."""
        return Coords(*(s + o for s, o in zip(self, other)))


def parse_str_to_grid(input_string: str) -> NDArray[np.str_]:
    """Parse the input string into a 2d Numpy array."""
    lines = input_string.strip().splitlines()
    return np.array([list(line) for line in lines])


def print_grid(grid: NDArray[np.str_]) -> None:
    """Print the grid for debugging."""
    for row in grid:
        print(''.join(row))
    print()


def is_valid_coordinate(coords: Coords, grid: NDArray[np.str_]) -> bool:
    """Check if the given coordinates are valid."""
    rows, cols = grid.shape
    return 0 <= coords[0] < rows and 0 <= coords[1] < cols


test_data1: str = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

if __name__ == '__main__':
    result = main(test_data1)
    print(f'Result: {result}')
