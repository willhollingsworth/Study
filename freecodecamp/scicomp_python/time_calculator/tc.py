import testing_data

def add_time(start, duration):
    return start + duration


if __name__ == "__main__":
    for test in testing_data.tests:
        args, expected = test
        print(f'Testing with args: {args}')
        print(f'Expected: {expected!a}')
        # results = add_time(*args)
        # matched = results == expected
        # if not matched:
        #     print(f'Test failed for args: {args}')
        #     print('Expected:')
        #     print(ascii(expected))
        #     print('Got:')
        #     print(ascii(results))
