"""Advent of Code 2024 - Day 2."""
from collections.abc import Iterator
from day2_data import test_data


def check_reactors(reactors: list[list[int]]) -> int:
    """Count the number of safe reactors."""
    safe_reactors: list[bool] = []
    for reactor in reactors:
        minimum_change: int = 1
        maximum_change: int = 3
        if reactor not in (sorted(reactor), sorted(reactor, reverse=True)):  # noqa: PLR6201
            safe_reactors.append(False)  # reactor is not sorted, so not safe
            continue
        pairs: Iterator[tuple[int, int]] = zip(reactor, reactor[1:])
        differences: list[int] = [
            abs(pair[0] - pair[1]) for pair in pairs
        ]
        within_range: list[bool] = [
            minimum_change <= difference <= maximum_change for difference in differences
        ]
        passed: bool = all(within_range)
        # print(f'{passed=}, {reactor=}, {differences=}')  # noqa: ERA001
        safe_reactors.append(passed)
    return safe_reactors.count(True)  


def parse_input(input_string: str) -> list[list[int]]:
    """Parse a string input into a list of lists of integers."""
    output: list[list[int]] = [
        [int(number) for number in line.split()]
        for line in input_string.splitlines()
        ]
    return output


test_1: str = \
"""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

if __name__ == "__main__":
    print('running tests')
    numbers_1 = parse_input(test_1)
    print('final checks:', check_reactors(numbers_1))
    numbers_day2 = parse_input(test_data)
    print('final checks:', check_reactors(numbers_day2))