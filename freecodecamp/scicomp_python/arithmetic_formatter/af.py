
from testing_data import tests

def arithmetic_arranger(problems: list[str], show_answers: bool = False) -> str:
    lines = [''] * 3    

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
        lines[0] += f'{val1:>{char_count}}'
        lines[1] += f'{operator} {val2:>{char_count-2}}'
        lines[2] += f'{dashes:>{char_count}}'

        if show_answers:
            lines[3] = ''
            if operator == '+':
                total = val1 + val2
            elif operator == '-':
                total = val1 - val2
            lines[3] += f'{total:>{char_count}}'
        
        # add spaces between the lines
        for i in range(len(lines)):
            lines[i] += ' ' * 4
    output = '\n'.join(lines)
    return output

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
    for test in tests[1:2]:
        args,expected = test
        results = arithmetic_arranger(*args)
        print('result')
        print(results)
        print('expected')
        print(test[1])