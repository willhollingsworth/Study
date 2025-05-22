def arithmetic_arranger(problems, show_answers=False):
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


tests =[
        ["32 + 698","3801 - 2","45 + 43","123 + 49",],
        ["3801 - 2", "123 + 49"], 
        ["1 + 2", "1 - 9380"], 
        ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], 
        ["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"], 
        ["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"],
        ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"],
        (["3 + 855", "988 + 40"], True),
        (["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"],True)
]       

for test in tests:
    if isinstance(test, tuple): 
        results = arithmetic_arranger(*test)
    else:
        results = arithmetic_arranger(test)
    print(results)

