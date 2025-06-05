"""Advent of Code 2024 - Day 4."""  # noqa: INP001
import numpy as np  # noqa: I001
from numpy.typing import NDArray

from day4_data import test_data


def find_matches(input_strings: list[NDArray[np.str_]]) -> int:
    """Find the number of occurrences of target string in a list of strings."""
    count: int = 0
    target: str = 'XMAS'
    for input_string in input_strings:
        for string in input_string:
            count += string.count(target)
            count += string[::-1].count(target)
    return count


def parse_input(input_string: str) -> list[NDArray[np.str_]]:
    """Parse the input string into a list of strings."""
    lines = input_string.strip().split('\n')
    length: int = len(lines[0])
    parsed_input: str = ''.join(lines)
    grid: NDArray[np.str_] = np.array(
        list(parsed_input),
    ).reshape(-1, length)
    completed_strings: list[NDArray[np.str_]] = []
    completed_strings.extend([
        horizontal_parse(grid),
        vertical_parse(grid),
        diagonal_parse_tl(grid),
        diagonal_parse_tr(grid),
    ])
    return completed_strings


def horizontal_parse(
    grid: NDArray[np.str_],
) -> NDArray[np.str_]:
    """Parse the input string horizontally."""
    return np.apply_along_axis(''.join, axis=1, arr=grid)


def vertical_parse(
    grid: NDArray[np.str_],
) -> NDArray[np.str_]:
    """Parse the input string vertically."""
    rot_grid = np.rot90(grid)
    return horizontal_parse(rot_grid)


def diagonal_parse_tl(
    grid: NDArray[np.str_],
) -> NDArray[np.str_]:
    """Parse the input string diagonally from top-left to bottom-right."""
    diagonals: list[str] = []
    height, width = grid.shape
    diagonals = [
        ''.join(np.diag(grid, k=offset))
        for offset in range(-height, width)
    ]
    return np.array(diagonals)


def diagonal_parse_tr(
    grid: NDArray[np.str_],
) -> NDArray[np.str_]:
    """Parse the input string diagonally from top-right to bottom-left."""
    grid_flipped = np.rot90(grid)
    return diagonal_parse_tl(grid_flipped)


test1_data: str = \
"""MMMSXXMASM
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
    results1 = find_matches(test1)
    print(results1)

    test2 = parse_input(test_data)
    results2 = find_matches(test2)
    print(results2)
