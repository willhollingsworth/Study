import pytest
import testing_data_tc
from tc import add_time


@pytest.mark.parametrize(("problem", "expected"), testing_data_tc.tests)
def test_add_time(problem: set, expected: str) -> None:
    """Test that the add_time function returns the expected string."""
    results = add_time(*problem)
    assert results == expected, f'Expected :{expected!a} but got :{results!a}'


if __name__ == "__main__":
    for args, expected in testing_data_tc.tests:
        results = add_time(*args)
        print(f'{results!a}')
        print(f'{expected!a}')
