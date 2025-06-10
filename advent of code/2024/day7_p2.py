"""Advent of Code 2024 - Day 7 Part 2."""  # noqa: INP001

from itertools import product, zip_longest
import day7_data


def main(input_string: str, feedback: bool = False) -> int:
    """Implement Main day7 logic."""
    equations = parse_input(input_string)
    total: int = 0
    for equation in equations:
        total += determine_combo_results(*equation, feedback=feedback)
    return total


def determine_combo_results(total: int, elements: list[int], feedback: bool = False) -> int:
    op_signs: list[str] = ['+', '*', '||']
    op_count: int = len(elements) - 1
    op_combos = product(op_signs, repeat=op_count)
    for op_combo in op_combos:
        total_result: int = elements[0]
        for i, e1 in enumerate(elements[1:]):
            string_eval: str = f'{total_result}{op_combo[i]}{e1}'
            total_result = eval_expression(total_result, e1, op_combo[i])
        if total_result == total:
            if feedback:
                correct_combo: str = ' '.join(
                    f'{e} {op_combo[i]}' for i, e in enumerate(elements[:-1])
                ) + ' ' + str(elements[-1])
                print('Found a match:', correct_combo, '=', total_result)
            return total_result
    return 0

def eval_expression(element1: int, element2: int, operator: str) -> int:
    """Evaluate a simple expression with two elements and an operator."""
    if operator == '+':
        return element1 + element2
    elif operator == '*':
        return element1 * element2
    return int(str(element1) + str(element2))



def parse_input(input_string: str) -> list[tuple[int, list[int]]]:
    """Parse the input string into a list of tuples."""
    lines: list[str] = input_string.strip().splitlines()
    line_data: tuple[int, list[int]] = (0, [0])
    parsed_data: list[tuple[int, list[int]]] = []
    for line in lines:
        total: int = int(line.split(':')[0])
        elements: list[int] = list(map(int, line.split(':')[1].strip().split()))
        line_data = (total, elements)
        parsed_data.append(line_data)

    return parsed_data


test_data1: str = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

if __name__ == '__main__':
    # Example usage
    result = main(test_data1, feedback=True)
    print(f'Result: {result}')
    result2 = main(day7_data.test_data2)
    print(f'Result: {result2}')
