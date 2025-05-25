from datetime import datetime, timedelta
import testing_data

def add_time(start: str, duration: str):
    start_time = datetime.strptime(start, '%I:%M %p')
    duration_time = datetime.strptime(duration, '%H:%M')
    duration_delta = timedelta(hours=duration_time.hour, minutes=duration_time.minute)
    end_time = start_time + duration_delta
    result: str = end_time.strftime('%I:%M %p').lstrip("0")
    return result


if __name__ == "__main__":
    for test in testing_data.tests[:2]:
        args, expected = test
        result = add_time(*args)
        print(f'Testing with args: {args}')
        print(f'Result:   {result!a}')
        print(f'Expected: {expected!a}')
        # matched = results == expected
        # if not matched:
        #     print(f'Test failed for args: {args}')
        #     print('Expected:')
        #     print(ascii(expected))
        #     print('Got:')
        #     print(ascii(results))
