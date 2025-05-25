import testing_data_tc
def add_time(start: str, duration: str, day: str = '') -> str:
    output_list = []
    symbols = ['AM', 'PM']

    start_hour, start_minute = map(int, start.split(' ')[0].split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))
    symbol = symbols.index(start.split(' ')[1])

    end_minute = (start_minute + duration_minute) % 60

    end_hour = start_hour + duration_hour
    end_hour += (start_minute + duration_minute) // 60
    end_hour += symbol * 12
    formatted_hour = end_hour % 12
    if formatted_hour == 0:
        formatted_hour = 12

    symbol = 11 < end_hour % 24 < 24

    output_list.append(f'{formatted_hour}:{end_minute:02d} {symbols[symbol]}')

    days = end_hour // 24
    if days == 1:
        output_list.append(' (next day)')
    elif days > 1:
        output_list.append(f' ({days} days later)')
    return ''.join(output_list)


if __name__ == "__main__":
    print('Running tests...')
    for test in testing_data_tc.tests:
        args, expected = test
        result = add_time(*args)
        # print(f'Testing with args: {args}')
        # print(f'Result:   {result!a}')
        # print(f'Expected: {expected!a}')
        matched = result == expected
        if not matched:
            print(f'Test failed for args: {args}')
            print(f'Expected: {expected!a}')
            print(f'Got:      {result!a}')

