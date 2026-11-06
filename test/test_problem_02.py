import pytest

from problem_02 import my_strip, my_words


@pytest.mark.parametrize(
    "s, expected",
    [
        ("  hello  ", "hello"),
        ("hello", "hello"),
        ("   ", ""),
        ("", ""),
        ("a  b", "a  b"),
        ("  a  b  ", "a  b"),
        (" x", "x"),
        ("x ", "x"),
    ],
)
def test_my_strip_default(s, expected):
    assert my_strip(s) == expected


@pytest.mark.parametrize(
    "s, chars, expected",
    [
        ("...hi!!", ".!", "hi"),
        ("xxhixx", "x", "hi"),
        ("  hi  ", "x", "  hi  "),
        ("xyxhixyx", "xy", "hi"),
        ("xxxx", "x", ""),
        ("hi", "", "hi"),
        ("--a-b--", "-", "a-b"),
    ],
)
def test_my_strip_chars(s, chars, expected):
    assert my_strip(s, chars) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("a b c", ["a", "b", "c"]),
        ("  a   b  ", ["a", "b"]),
        ("a\tb\nc", ["a", "b", "c"]),
        ("", []),
        ("   ", []),
        ("hello", ["hello"]),
        (" hello ", ["hello"]),
        ("one  two\t\tthree\n", ["one", "two", "three"]),
    ],
)
def test_my_words(s, expected):
    assert my_words(s) == expected
