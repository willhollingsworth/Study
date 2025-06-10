"""Advent of Code 2024 - Day 8."""  # noqa: INP001

import numpy as np
from aoc2024_utils import Coords, parse_str_to_grid, print_grid
from numpy.typing import NDArray


def main(input_string: str) -> int:
    grid: NDArray[np.str_] = parse_str_to_grid(input_string)
    antennas_coords: dict[str, list[Coords]] = get_antenna_coordinates(
        grid,
    )
    print_grid(grid)
    print(antennas_coords)
    return 0


def get_antenna_coordinates(
    grid: NDArray[np.str_],
) -> dict[str, list[Coords]]:
    antennas_coords: dict[str, list[Coords]] = {}
    antenna_types: list[str] = np.unique(grid).tolist()
    antenna_types.remove('.')
    for antenna_type in antenna_types:
        coords = np.array(np.where(grid == antenna_type)).transpose()
        for coord in coords:
            antennas_coords.setdefault(antenna_type, []).append(
                Coords(*coord),
                )
    return antennas_coords



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
