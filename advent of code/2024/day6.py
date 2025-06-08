"""Advent of Code 2024 - Day 6."""  # noqa: INP001
import day6_data
import numpy as np
from numpy.typing import NDArray


def main(input_string: str) -> int:
    """Implement Main day6 logic."""
    grid = parse_input(input_string)
    grid = walk_grid(grid)
    print(grid)
    return np.count_nonzero(grid == 'x')


def parse_input(input_string: str) -> NDArray[np.str_]:
    """Parse the input string into a 2d Numpy array."""
    lines = input_string.strip().splitlines()
    return np.array([list(line) for line in lines])


def walk_grid(grid: NDArray[np.str_]) -> NDArray[np.str_]:
    """Walk the grid and update the visited cells."""
    coords = np.array(np.where(grid == '^')).flatten()
    direction: NDArray[np.int_] = np.array([-1, 0])  # row, col direction
    new_coords = coords.copy()
    for _ in range(200):
        grid[tuple(coords)] = 'x'
        print(coords)
        new_coords = coords + direction
        if not is_valid_coordinate(new_coords, grid):
            break
        if grid[tuple(new_coords)] == '#':
            print('hit a wall')
            direction = change_direction(direction)
            new_coords = coords + direction
            if not is_valid_coordinate(new_coords, grid):
                break
        coords = new_coords
    return grid


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


if __name__ == "__main__":
    print('running tests')
    results1 = main(day6_data.test_data1)
    print(results1)
    # results2 = main(day5_data.test_data2)
    # print(results2)
