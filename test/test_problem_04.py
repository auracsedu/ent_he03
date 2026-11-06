import pytest

from problem_04 import digit_sum, my_reverse, to_binary


@pytest.mark.parametrize(
    "n, expected",
    [(0, 0), (7, 7), (10, 1), (1234, 10), (99999, 45), (1000000, 1)],
)
def test_digit_sum(n, expected):
    assert digit_sum(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (3, "11"),
        (8, "1000"),
        (10, "1010"),
        (255, "11111111"),
        (1024, "10000000000"),
    ],
)
def test_to_binary(n, expected):
    assert to_binary(n) == expected


@pytest.mark.parametrize(
    "s, expected",
    [("", ""), ("a", "a"), ("ab", "ba"), ("abc", "cba"), ("hello", "olleh"), ("racecar", "racecar")],
)
def test_my_reverse(s, expected):
    assert my_reverse(s) == expected
