import pytest

from problem_05 import max_depth, nested_sum


@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 3], 6),
        ([1, [2, 3], 4], 10),
        ([1, [2, [3, [4]]]], 10),
        ([], 0),
        ([[], [[]], []], 0),
        ([[1, 2], [3, [4, 5]]], 15),
        ([[-1], [1]], 0),
    ],
)
def test_nested_sum(items, expected):
    assert nested_sum(items) == expected


@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 3], 1),
        ([], 1),
        ([1, [2, 3], 4], 2),
        ([1, [2, [3, [4]]]], 4),
        ([[], [[]], []], 3),
        ([[1], [2], [3]], 2),
        ([[[1]], 2], 3),
        ([1, [2], [[3]], [[[4]]]], 4),
    ],
)
def test_max_depth(items, expected):
    assert max_depth(items) == expected


def test_original_is_not_changed():
    items = [1, [2, [3]], 4]
    nested_sum(items)
    max_depth(items)
    assert items == [1, [2, [3]], 4]
