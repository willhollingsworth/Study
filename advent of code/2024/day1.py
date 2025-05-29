"""For Advent of Code 2024, Day 1: Find the distance between two lists of numbers."""  # noqa: INP001

from day1_data import day1_data


def find_distance_of_list(numbers: list[list[int]]) -> int:
    """Find the distances between two lists of numbers."""
    distance: int = 0
    numbers = [sorted(number_list) for number_list in numbers]  # sort list
    for i in range(len(numbers[0])):
        distance += abs(numbers[0][i] - numbers[1][i])
    return distance


def parse_input(input_string: str) -> list[list[int]]:
    """Parse the input string into a list of lists of integers."""
    lines: list[list[int]] = []
    lines = [
                [int(number) for number in line.split()]  # split each line into numbers
                for line in input_string.splitlines()  # split the input into lines
            ]
    return [list(group) for group in zip(*lines)]  # rotate the list


test_1: str = \
"""3   4
4   3
2   5
1   3
3   9
3   3
"""

if __name__ == "__main__":
    numbers_1 = parse_input(test_1)
    print('test1:', find_distance_of_list(numbers_1))
    numbers_day1 = parse_input(day1_data)
    print('test2:', find_distance_of_list(numbers_day1))
