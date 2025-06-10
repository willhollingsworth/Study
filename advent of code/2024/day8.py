"""Advent of Code 2024 - Day 8."""  # noqa: INP001

import numpy as np
from numpy.typing import NDArray


def main(input_string: str) -> int:
    grid: NDArray[np.str_] = parse_input(input_string)
    print_grid(grid)  # Debugging output
    coords = np.array(np.where(grid == 'A')).transpose()
    print(coords)
    return 0


def parse_input(input_string: str) -> NDArray[np.str_]:
    """Parse the input string into a 2d Numpy array."""
    lines = input_string.strip().splitlines()
    return np.array([list(line) for line in lines])


def print_grid(grid: NDArray[np.str_]) -> None:
    """Print the grid for debugging."""
    for row in grid:
        print(''.join(row))
    print()


def is_valid_coordinate(coords: NDArray[np.int_], grid: NDArray[np.str_]) -> bool:
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
