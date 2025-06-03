"""Advent of Code 2024 - Day 2."""  # noqa: INP001
import re

from day3_data import test_data


def proccess_pairs(pair_list: list[tuple[int, int]]) -> int:
    """Process pairs of integers, Multiplying then add them to a running total."""
    total: int = 0
    for a, b in pair_list:
        total += a * b
    return total


def parse_input(input_string: str) -> list[tuple[int, int]]:
    """Parse a string input into a list of tuple of integers."""
    pattern: str = r'mul\((\d{1,3}),(\d{1,3})\)|(don\'t\(\))|(do\(\))'
    matches: list[tuple[str, str, str, str]] = re.findall(pattern, input_string)
    filtered_matches: list[tuple[int, int]] = []
    active: bool = True
    for match in matches:
        if 'do()' in match:
            active = True
        elif 'don\'t()' in match:
            active = False
        elif active:
            filtered_matches.append((int(match[0]), int(match[1])))
    return filtered_matches


if __name__ == "__main__":
    print('running tests')
    test1: str = (
       "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    input_test1: list[tuple[int, int]] = []
    input_test1 = parse_input(test1)
    result_test1: int = proccess_pairs(input_test1)
    print(f'Test 1 result: {result_test1}')

    input_test2: list[tuple[int, int]] = parse_input(test_data)
    result_test2: int = proccess_pairs(input_test2)
    print(f'Test 2 result: {result_test2}')
