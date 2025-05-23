import pytest

from af import arithmetic_arranger
from testing_data import tests

# tests = [tests[0:2]]

@pytest.mark.parametrize("input, expected",tests)
def test_string_match(input, expected):
        results = arithmetic_arranger(*input)
        assert results == expected, f'Expected :{ascii(expected)} but got :{ascii(results)}'

if __name__ == "__main__":
    pytest.main([__file__])