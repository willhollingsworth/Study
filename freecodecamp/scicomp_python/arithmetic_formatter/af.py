from typing import Union

from testing_data import tests



def arithmetic_arranger(problems: str, show_answers=False) -> str:
    if len(problems) > 5:
        return 'Error: Too many problems.'
    lines = [''] * 4    

    for problem in problems:
        items = parse_string(problem)
        if isinstance(items, str):
            return items
        val1, val2, operator = items
        longest_number = max(len(str(val1)),len(str(val2)))
        if longest_number > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        dashes = '-' * (longest_number + 2) 
        lines[0] += f'{val1: >6}  '
        lines[1] += f'{operator + " "+ str(val2): >6}  '
        lines[2] += f'{dashes:>6}  '

        if show_answers:
            if operator == '+':
                total = val1 + val2
            elif operator == '-':
                total = val1 - val2
            lines[3] += f'{total:>6}  '

    output = '\n'.join(lines)
    return output

def parse_string(input: str) -> list | str:   # -> Any:
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
    for test in tests[1:2]:
        args,expected = test
        results = arithmetic_arranger(*args)
        print('result')
        print(results)
        print('expected')
        print(test[1])