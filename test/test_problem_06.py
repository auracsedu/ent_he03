import pytest

from problem_06 import subsets, subsets_with_sum


@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 3], [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]),
        ([1, 2], [[1, 2], [1], [2], []]),
        ([1], [[1], []]),
        ([], [[]]),
        (["a", "b"], [["a", "b"], ["a"], ["b"], []]),
    ],
)
def test_subsets(items, expected):
    assert subsets(items) == expected


def test_subsets_count_is_power_of_two():
    assert len(subsets([1, 2, 3, 4, 5])) == 32
    assert len(subsets(list(range(10)))) == 1024


@pytest.mark.parametrize(
    "items, target, expected",
    [
        ([1, 2, 3], 3, [[1, 2], [3]]),
        ([1, 2, 3], 6, [[1, 2, 3]]),
        ([1, 2, 3], 0, [[]]),
        ([1, 2, 3], 7, []),
        ([3, 5, 2, 8], 10, [[3, 5, 2], [2, 8]]),
        ([2, 4, 6], 6, [[2, 4], [6]]),
        ([], 0, [[]]),
        ([], 1, []),
    ],
)
def test_subsets_with_sum(items, target, expected):
    assert subsets_with_sum(items, target) == expected
