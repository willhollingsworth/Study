"""Code wars.

Third attempt, cleaner than previous versions but still fails due to speed.

"""
from __future__ import annotations

from itertools import combinations


def sum_pairs(pairs: list[int], target: int) -> list[int] | None:
    """Return first pair of integers that sum to target."""
    combos = combinations(pairs, 2)
    valid_pairs: list[tuple[int, int]] = []
    valid_pairs = [pair for pair in combos if sum(pair) == target]
    if not valid_pairs:
        return None
    duplicates = any(pair for pair in valid_pairs if pair.count(pair[0]) > 1)
    if not duplicates:
        valid_pairs.sort(key=lambda x: pairs.index(x[1]))
    else:
        valid_pairs.sort(key=lambda pair: second_index((pair[1], pairs)))
    return list(valid_pairs[0])


def second_index(args: tuple[int, list[int]]) -> int:
    """Return second index if there are duplicates else return first index."""
    target, pairs = args
    first: int = pairs.index(target)
    duplicates = pairs.count(target) - 1
    if not duplicates:
        return first
    second: int = pairs.index(target, first + 1)
    return second


if __name__ == '__main__':
    """Main function."""
    # Test cases
    l1 = [1, 4, 8, 7, 3, 15]
    l2 = [1, -2, 3, 0, -6, 1]
    l3 = [20, -13, 40]
    l4 = [1, 2, 3, 4, 1, 0]
    l5 = [10, 5, 2, 3, 7, 5]
    l6 = [4, -2, 3, 3, 4]
    l7 = [0, 2, 0]
    l8 = [5, 9, 13, -3]

    print(sum_pairs(l1, 8), 'Expected: [1, 7]')
    print(sum_pairs(l2, -6), 'Expected: [0, -6]')
    print(sum_pairs(l3, -7), 'Expected: None')
    print(sum_pairs(l4, 2), 'Expected: [1, 1]')
    print(sum_pairs(l5, 10), 'Expected: [3, 7]')
    print(sum_pairs(l6, 8), 'Expected: [4, 4]')
    print(sum_pairs(l7, 0), 'Expected: [0, 0]')
    print(sum_pairs(l8, 10), 'Expected: [13, -3]')