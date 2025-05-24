
from testing_data import tests

def arithmetic_arranger(problems: list[str], show_answers: bool = False) -> str:
    lines = [[] for _ in range(3)]
    finished_lines = []
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        items = parse_string(problem)
        if isinstance(items, str):
            # On error return error string
            return items
        val1, val2, operator = items
        longest_number = max(len(str(val1)),len(str(val2)))
        if longest_number > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        char_count = longest_number + 2
        dashes = '-' * (char_count) 
        lines[0].append(f'{val1:>{char_count}}')
        lines[1].append(f'{operator} {val2:>{char_count-2}}')
        lines[2].append(f'{dashes:>{char_count}}')

        if show_answers:
            lines.append([])
            if operator == '+':
                total = val1 + val2
            elif operator == '-':
                total = val1 - val2
            lines[3].append(f'{total:>{char_count}}')

    for i in range(len(lines)):
        finished_lines.append('    '.join(lines[i]))
    return '\n'.join(finished_lines)


def parse_string(input: str) -> list | str:   # -> Any:
    ''' parse the raw string into a list of two numbers and the operator, return a string msg on error'''
    items = input.split(' ')
    output = []
    try:
        output.append(int(items[0]))
    except ValueError:
        return 'Error: Numbers must only contain digits.'
    
    try:
        output.append(int(items[2]))
    except ValueError:
        return 'Error: Numbers must only contain digits.'
    
    operator = items[1]
    if operator not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."
    
    output.append(operator)
    return output

if __name__ == "__main__":
    for test in tests:
        args,expected = test
        results = arithmetic_arranger(*args)
        matched = results == expected
        if not matched:
            print(f'Test failed for args: {args}')
            print('Expected:')
            print(ascii(expected))
            print('Got:')
            print(ascii(results))
