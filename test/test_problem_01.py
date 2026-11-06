import pytest

from problem_01 import my_count, my_endswith, my_startswith


@pytest.mark.parametrize(
    "s, prefix, expected",
    [
        ("hello", "he", True),
        ("hello", "hello", True),
        ("hello", "hell!", False),
        ("he", "hello", False),
        ("hello", "", True),
        ("", "", True),
        ("", "a", False),
        ("hello", "ello", False),
    ],
)
def test_my_startswith(s, prefix, expected):
    assert my_startswith(s, prefix) is expected


@pytest.mark.parametrize(
    "s, suffix, expected",
    [
        ("hello", "lo", True),
        ("hello", "hello", True),
        ("hello", "l", False),
        ("", "a", False),
        ("hello", "", True),
        ("", "", True),
        ("lo", "hello", False),
        ("hello", "hell", False),
    ],
)
def test_my_endswith(s, suffix, expected):
    assert my_endswith(s, suffix) is expected


@pytest.mark.parametrize(
    "s, sub, expected",
    [
        ("banana", "a", 3),
        ("banana", "an", 2),
        ("banana", "ana", 1),
        ("aaaa", "aa", 2),
        ("aaaaa", "aa", 2),
        ("hello", "z", 0),
        ("", "a", 0),
        ("abcabcabc", "abc", 3),
        ("abc", "abcd", 0),
    ],
)
def test_my_count(s, sub, expected):
    assert my_count(s, sub) == expected
