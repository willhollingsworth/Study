import pytest
import testing_data
from af import arithmetic_arranger


@pytest.mark.parametrize(("problem", "expected"), testing_data.tests)
def test_string_match(problem: list[list], expected: str) -> None:
    """Test that the arithmetic_arranger function returns the expected string."""
    results = arithmetic_arranger(*problem)
    assert results == expected, f'Expected :{expected!a} but got :{results!a}'


if __name__ == "__main__":
    for args, expected in testing_data.tests:
        results = arithmetic_arranger(*args)
        print(f'{results!a}\n{expected!a}')
