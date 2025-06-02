"""Advent of Code 2024 - Day 2 - Part 2."""  # noqa: INP001

from __future__ import annotations

from typing import TYPE_CHECKING

from day2_data import test_data

if TYPE_CHECKING:
    from collections.abc import Iterator

"""
Idea:
    - test a reactor,
        if it fails then attempt to rerun it with the failing number removed.
        Should be able to detect difference failures somewhat easily but
        out of order may be harder.
"""


def check_reactors(reactors: list[list[int]]) -> int:
    """Count the number of safe reactors.

    If a reactor fails, attempt to fix it by removing the first failing number.
    Then retest the reactor.
    """
    safe_reactors: list[bool] = []
    for reactor in reactors:
        if check_reactor(reactor):
            safe_reactors.append(True)
            continue
        fixed_reactor = fix_reactor(reactor)
        if check_reactor(fixed_reactor):
            safe_reactors.append(True)
        else:
            safe_reactors.append(False)
    return safe_reactors.count(True)


def check_reactor(reactor: list[int]) -> bool:
    """Check if a reactor is safe."""
    if not is_sorted(reactor):
        return False
    within_limits: list[bool] = check_reactor_ranges(reactor)
    passed: bool = all(within_limits)
    # print(f'{passed=}, {list(zip(reactor, ['', *within_limits]))}')  # noqa: ERA001
    return passed


def find_unordered_index(reactor: list[int]) -> int:
    """Check a list for the first unordered element."""
    pairs: Iterator[tuple[int, int]] = zip(reactor, reactor[1:])
    value_deltas: list[int] = [
        pair[1] - pair[0] for pair in pairs
    ]
    value_direction: list[str] = [asc_label(n) for n in value_deltas]
    possible_directions: list[str] = ['a', 'd']
    overall_inverse_direction: str = possible_directions[
        value_direction.count('a') > value_direction.count('d')
    ]
    unorder_index: int = value_direction.index(overall_inverse_direction)
    return unorder_index


def asc_label(n: int) -> str:
    """Labels a number as ascending, descending, or neutral."""
    if n > 0:
        return 'a'
    if n < 0:
        return 'd'
    return 'neutral'


def find_range_failing_index(reactor: list[int]) -> int:
    """Check a reactor and find the index of the first failing number.

    Check is done based on allowed differences.
    """
    within_limits: list[bool] = check_reactor_ranges(reactor)
    failing_index: int = within_limits.index(False) + 1
    return failing_index


def check_reactor_ranges(reactor: list[int]) -> list[bool]:
    """Check if all differences are within the allowed range."""
    minimum_change: int = 1
    maximum_change: int = 3
    pairs: Iterator[tuple[int, int]] = zip(reactor, reactor[1:])
    differences: list[int] = [
        abs(pair[0] - pair[1]) for pair in pairs
    ]
    within_range: list[bool] = [
        minimum_change <= difference <= maximum_change for difference in differences
    ]
    return within_range


def is_sorted(reactor: list[int]) -> bool:
    """Check if a reactor is sorted ascending or descending."""
    return reactor in (sorted(reactor), sorted(reactor, reverse=True))


def fix_reactor(reactor: list[int]) -> list[int]:
    """Attempt to fix a reactor by removing the first failing number."""
    failing_index: int = 0
    if not is_sorted(reactor):
        failing_index = find_unordered_index(reactor)
    else:
        failing_index = find_range_failing_index(reactor)
    reactor.pop(failing_index)
    return reactor


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
