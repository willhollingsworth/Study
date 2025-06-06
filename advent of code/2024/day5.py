"""Advent of Code 2024 - Day 5."""  # noqa: INP001
import day5_data


def main(input_string: str) -> int:
    """Implement the main logic for day 5."""
    ordering_list, manuals = parse_input(input_string)
    ordering_rules = build_ordering_rules(ordering_list)
    correct_count: int = 0
    for manual in manuals:
        if check_manual(manual, ordering_rules):
            correct_count += manual[len(manual) // 2]
    return correct_count


def parse_input(input_string: str) -> list[list[list[int]]]:
    """Parse the input string into two lists of ordering info and manuals."""
    ordering_list: list[list[int]] = []
    manuals: list[list[int]] = []
    for line in input_string.splitlines():
        if '|' in line:
            ordering_list.append(list(map(int, line.split('|'))))
        elif ',' in line:
            manuals.append(list(map(int, line.split(','))))
    return [ordering_list, manuals]


def build_ordering_rules(ordering_list: list[list[int]]) -> dict[int, list[int]]:
    """Build a dictionary of ordering rules from the ordering list."""
    ordering_rules: dict[int, list[int]] = {}
    for i, j in ordering_list:
        ordering_rules.setdefault(i, []).append(j)
    return ordering_rules


def check_manual(manual: list[int], ordering_rules: dict[int, list[int]]) -> bool:
    """Check the manual against the ordering rules."""
    for index, current in enumerate(manual):
        if current not in ordering_rules:
            continue
        for rule in ordering_rules[current]:
            if rule not in manual:
                continue
            if manual.index(rule) < index:
                return False
    return True


if __name__ == "__main__":
    print('running tests')
    results1 = main(day5_data.test_data1)
    print(results1)
    results2 = main(day5_data.test_data2)
    print(results2)
