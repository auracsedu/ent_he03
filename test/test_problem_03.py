import pytest

from problem_03 import my_int, my_str


@pytest.mark.parametrize(
    "s, expected",
    [
        ("0", 0),
        ("7", 7),
        ("42", 42),
        ("007", 7),
        ("-15", -15),
        ("-0", 0),
        ("1234567", 1234567),
        ("-1000", -1000),
    ],
)
def test_my_int(s, expected):
    assert my_int(s) == expected
    assert type(my_int(s)) is int


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "0"),
        (7, "7"),
        (42, "42"),
        (-15, "-15"),
        (1000, "1000"),
        (1234567, "1234567"),
        (-1000, "-1000"),
        (10, "10"),
    ],
)
def test_my_str(n, expected):
    assert my_str(n) == expected


@pytest.mark.parametrize("n", [0, 5, 99, -7, 123456, -1000000])
def test_round_trip(n):
    assert my_int(my_str(n)) == n
