"""Advent of Code 2024 - Day 4 Part 2."""  # noqa: INP001
import numpy as np  # noqa: I001
from numpy.typing import NDArray

from day4_data import test_data


def parse_input(input_string: str) -> NDArray[np.str_]:
    """Parse the input string into a grid."""
    lines = input_string.strip().split('\n')
    length: int = len(lines[0])
    parsed_input: str = ''.join(lines)
    grid: NDArray[np.str_] = np.array(
        list(parsed_input),
    ).reshape(-1, length)
    return grid


def x_finder(input_grid: NDArray[np.str_]) -> int:
    """Find the number of crossed XMAS in the grid."""
    count: int = 0
    target = {np.str_(c) for c in 'MS'}
    for r, c in np.ndindex(input_grid[:-1, :-1].shape):
        if not (c and r):
            continue
        if input_grid[r, c] != 'A':
            continue
        pairs: list[set[np.str_]] = [
            {input_grid[r - 1, c + 1], input_grid[r + 1, c - 1]},
            {input_grid[r - 1, c - 1], input_grid[r + 1, c + 1]},
        ]
        matches: list[bool] = [
            pair == target for pair in pairs
        ]
        if all(matches):
            count += 1
    return count


test1_data: str = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

if __name__ == "__main__":
    print('running tests')
    test1 = parse_input(test1_data)
    results1 = x_finder(test1)
    print(results1)

    test2 = parse_input(test_data)
    results2 = x_finder(test2)
    print(results2)
