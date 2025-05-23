import time

from testing_data import tests



def arithmetic_arranger(problems: str, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    output = ''

    for problem in problems:
        items = problem.split(' ')

        try:
            num_1 = int(items[0])
        except:
            return 'Error: Numbers must only contain digits.'
        line1 += f'{num_1: >6}  '

        try:
            num_2 = int(items[2])
        except:
            return 'Error: Numbers must only contain digits.'
        operator = items[1]
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        line2 += f'{operator + " "+ str(num_2): >6}  '

        longest_number = max(len(items[0]),len(items[2]))
        if longest_number > 4:
            return 'Error: Numbers cannot be more than four digits.'
        line = '-' * (longest_number + 2) 
        line3 += f'{line:>6}  '

        if show_answers:
            if operator == '+':
                total = num_1 + num_2
            elif operator == '-':
                total = num_1 - num_2
            line4 += f'{total:>6}  '

    output += line1 + '\n'
    output += line2 + '\n' 
    output += line3 + '\n' 
    if show_answers:
        output += line4 + '\n' 
    return output

if __name__ == "__main__":
    for test in tests[:2]:
        inputs = test[0]
        # print(test[0])
        if isinstance(inputs[0], str): 
            results = arithmetic_arranger(inputs)
        else:
            results = arithmetic_arranger(*inputs)
        print(results)
        print(test[1])


