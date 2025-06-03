"""Advent of Code 2024 - Day 3."""  # noqa: INP001
import re

from day3_data import test_data


def proccess_pairs(pair_list: list[tuple[int, int]]) -> int:
    """Process pairs of integers, Multiplying then add them to a running total."""
    total: int = 0
    for a, b in pair_list:
        total += a * b
    return total


def parse_input(input_string: str) -> list[tuple[int, int]]:
    """Parse a string input into a list of lists of integers."""
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, input_string)
    return [
        (int(a), int(b)) for a, b in matches
    ]


if __name__ == "__main__":
    print('running tests')
    test1: str = (
        'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]'
        'then(mul(11,8)mul(8,5))'
    )
    input_test1: list[tuple[int, int]] = parse_input(test1)
    result_test1: int = proccess_pairs(input_test1)
    print(f'Test 1 result: {result_test1}')
    input_test2: list[tuple[int, int]] = parse_input(test_data)
    result_test2: int = proccess_pairs(input_test2)
    print(f'Test 2 result: {result_test2}')
