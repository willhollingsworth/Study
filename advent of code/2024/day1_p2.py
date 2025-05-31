"""Advent of Code 2024 - Day 1, Part 2."""  # noqa: INP001
from day1 import parse_input, test_1
from day1_data import day1_data


def similarity_score(numbers: list[list[int]]) -> int:
    """Calculate the similarity between two lists of numbers."""
    similarity: int = 0
    for number in numbers[0]:
        similarity += number * numbers[1].count(number)
    return similarity


if __name__ == "__main__":
    numbers_1 = parse_input(test_1)
    print(similarity_score(numbers_1))
    numbers_2 = parse_input(day1_data)
    print(similarity_score(numbers_2))
