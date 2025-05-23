import pytest

from af import arithmetic_arranger
from testing_data import tests

tests = [tests[0]]

@pytest.mark.parametrize("input, expected",tests)
def test_string_match(input, expected):
        input = [input] if isinstance(input[1],str) else input
        results = arithmetic_arranger(*input)
        expected = expected
        assert results == expected, f'Expected :{ascii(expected)} but got :{ascii(results)}'

if __name__ == "__main__":
    pytest.main([__file__])