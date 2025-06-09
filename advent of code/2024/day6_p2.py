"""Advent of Code 2024 - Day 6."""  # noqa: INP001
from dataclasses import dataclass

import day6_data
import numpy as np
from numpy.typing import NDArray


@dataclass
class WalkGridResult:
    grid: NDArray[np.str_]
    loop_detected: bool


def main(input_string: str, status: bool = False) -> int:
    """Implement Main day6 logic."""
    grid = parse_input(input_string)
    walked_grid = walk_grid(grid)
    walked_coords = get_walked_coordinates(walked_grid.grid)
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
    lines = input_string.strip().splitlines()
    return np.array([list(line) for line in lines])


def walk_grid(grid: NDArray[np.str_]) -> WalkGridResult:
    """Walk the grid and update the visited cells."""
    coords = np.array(np.where(grid == '^')).flatten()
    start_point: NDArray[np.int_] = coords.reshape(1, 2)  # (row, col)
    direction: NDArray[np.int_] = np.array([-1, 0])  # row, col direction
    new_grid = grid.copy()
    retread_count: int = 0
    loop_detected: bool = False
    for _ in range(10000):
        if new_grid[tuple(coords)] == 'x':
            retread_count += 1
            if retread_count > 100:
                loop_detected = True
                break
        else:
            retread_count = 0
        new_grid[tuple(coords)] = 'x'
        new_coords = coords + direction
        if not is_valid_coordinate(new_coords, new_grid):
            break
        if new_grid[tuple(new_coords)] == '#':
            direction = change_direction(direction)
            new_coords = coords + direction
            if not is_valid_coordinate(new_coords, new_grid):
                break
        coords = new_coords
    new_grid[tuple(start_point)] = '^'
    return WalkGridResult(grid=new_grid, loop_detected=loop_detected)


def get_walked_coordinates(grid: NDArray[np.str_]) -> list[tuple[int, int]]:
    """Get the coordinates of the walked path."""
    walked_coords = np.where(grid == 'x')
    return [(r, c) for r, c in zip(*walked_coords)]


def print_grid(grid: NDArray[np.str_]) -> None:
    """Print the grid for debugging."""
    for row in grid:
        print(''.join(row))
    print()


def change_direction(direction: NDArray[np.int_]) -> NDArray[np.int_]:
    """Cycle through the directions."""
    directions: list[list[int]] = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    index: int = directions.index(direction.tolist())
    next_index: int = (index + 1) % 4
    return np.array(directions[next_index], dtype=np.int_)


def is_valid_coordinate(coords: NDArray[np.int_], grid: NDArray[np.str_]) -> bool:
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
