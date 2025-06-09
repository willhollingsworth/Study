"""Advent of Code 2024 - Day 6."""  # noqa: INP001
from dataclasses import dataclass
from itertools import starmap

import day6_data
import numpy as np
from numpy.typing import NDArray


@dataclass
class WalkGridResult:
    grid: NDArray[np.str_]
    loop_detected: bool


class Coords(tuple[int, int]):
    """Tuple for holding and better adding of coordinates."""

    def __new__(cls, row: int, col: int) -> 'Coords':
        return super().__new__(cls, (int(row), int(col)))

    def __add__(self, other: 'Coords') -> 'Coords':
        """ Add two coordinates together."""
        return Coords(*(s + o for s, o in zip(self, other)))


def main(input_string: str, status: bool = False) -> int:
    """Implement Main day6 logic."""
    grid: NDArray[np.str_] = parse_input(input_string)
    walked_grid: WalkGridResult = walk_grid(grid)
    walked_coords: list[Coords] = get_walked_coordinates(walked_grid.grid)
    walked_count: int = len(walked_coords)
    loop_count: int = 0
    print('checking for loops')
    for i, (r, c) in enumerate(walked_coords):
        if i % (walked_count // 20) == 0 and status:
            percentage_completed = (i) / walked_count * 100
            print(
                f'{round(percentage_completed)}% completed,',
                f'Loops found: {loop_count}',
            )
        temp_grid = grid.copy()
        temp_grid[r, c] = '#'
        walked_grid = walk_grid(temp_grid)
        if walked_grid.loop_detected:
            loop_count += 1
    return loop_count


def parse_input(input_string: str) -> NDArray[np.str_]:
    """Parse the input string into a 2d Numpy array."""
    lines: list[str] = input_string.strip().splitlines()
    return np.array([list(line) for line in lines])


def walk_grid(grid: NDArray[np.str_]) -> WalkGridResult:
    """Walk the grid and update the visited cells."""
    coords_array = np.array(np.where(grid == '^')).transpose()
    current_coords: Coords = Coords(*coords_array[0])
    start_point: Coords = current_coords
    direction: Coords = Coords(-1, 0)  # row, col
    new_grid: NDArray[np.str_] = grid.copy()
    loop_detected: bool = False
    visited_states: set[tuple[Coords, Coords]] = set()
    while True:
        visted_state: tuple[Coords, Coords] = (current_coords, direction)
        if visted_state in visited_states:
            loop_detected = True
            break
        new_grid[current_coords] = 'x'
        visited_states.add(visted_state)
        new_coords = current_coords + direction
        if not is_valid_coordinate(new_coords, new_grid):
            break
        if new_grid[new_coords] == '#':
            direction = change_direction(direction)
            new_coords = current_coords + direction
            if not is_valid_coordinate(new_coords, new_grid):
                break
        current_coords = new_coords
    new_grid[start_point] = '^'
    # print(visited_states)
    # print_grid(new_grid)
    return WalkGridResult(grid=new_grid, loop_detected=loop_detected)


def get_walked_coordinates(grid: NDArray[np.str_]) -> list[Coords]:
    """Get the coordinates of the walked path."""
    walked_coords = np.where(grid == 'x')
    return list(starmap(Coords, zip(*walked_coords)))


def print_grid(grid: NDArray[np.str_]) -> None:
    """Print the grid for debugging."""
    for row in grid:
        print(''.join(row))
    print()


def change_direction(direction: Coords) -> Coords:
    """Cycle through the directions."""
    directions: list[Coords] = list(starmap(Coords, [(-1, 0), (0, 1), (1, 0), (0, -1)]))
    index: int = directions.index(direction)
    next_index: int = (index + 1) % 4
    return directions[next_index]


def is_valid_coordinate(coords: Coords, grid: NDArray[np.str_]) -> bool:
    """Check if the given coordinates are valid."""
    rows, cols = grid.shape
    return 0 <= coords[0] < rows and 0 <= coords[1] < cols


test_data1: str = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

if __name__ == "__main__":
    print('running tests')
    results1 = main(test_data1, status=False)
    print(results1)
    results2 = main(day6_data.test_data2, status=True)
    print(results2)
