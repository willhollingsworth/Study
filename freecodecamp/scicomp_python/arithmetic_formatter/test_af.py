import pytest

from af import arithmetic_arranger
import testing_data

@pytest.mark.parametrize("input, expected",testing_data.tests)
def test_string_match(input, expected):
        results = arithmetic_arranger(*input)
        assert results == expected, f'Expected :{ascii(expected)} but got :{ascii(results)}'

if __name__ == "__main__":
    for input, expected in testing_data.tests:
        results = arithmetic_arranger(*input)
        print(f'{ascii(results)}\n{ascii(expected)}')
