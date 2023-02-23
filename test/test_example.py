import pytest

from src.example import add

case = [(1, 1, 2), (-1, 1, 0), (-1, -1, -2)]


@pytest.mark.parametrize("a, b, expected", case)
def test_add(a, b, expected) -> None:
    assert add(a, b) == expected
