"""Advent of Code 2024 - Day 8."""  # noqa: INP001

from itertools import combinations

import day8_data
import numpy as np
from aoc2024_utils import Coords, is_valid_coordinate, parse_str_to_grid, print_grid
from numpy.typing import NDArray


def main(input_string: str) -> int:
    grid: NDArray[np.str_] = parse_str_to_grid(input_string)
    antennas_coords: dict[str, list[Coords]] = get_antenna_coordinates(
        grid,
    )
    antinodes_coords = calculate_antinodes_coords(antennas_coords, grid)
    print_grid(grid)
    for anti in antinodes_coords:
        grid[anti] = 'X'
    print_grid(grid)
    return len(antinodes_coords)


def calculate_antinodes_coords(
    antennas_coords: dict[str, list[Coords]],
    grid: NDArray[np.str_],
    ) -> set[Coords]:
    """Calculate the coordinates of antinodes for each antenna type."""
    antinode_coords: set[Coords] = set()
    for coords_list in antennas_coords.values():
        for p1, p2 in combinations(coords_list, 2):
            delta = p2 - p1
            a1 = p1 - delta
            a2 = p2 + delta
            if is_valid_coordinate(a1, grid):
                antinode_coords.add(a1)
            if is_valid_coordinate(a2, grid):
                antinode_coords.add(a2)
    return antinode_coords


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
    result2 = main(day8_data.test_data2)
    print(f'Result: {result2}')
