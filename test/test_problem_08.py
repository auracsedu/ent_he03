import pytest

from problem_08 import can_make, make_one


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([3, 5, 2, 8], 10, True),
        ([3, 5, 2, 8], 7, True),
        ([3, 5, 2, 8], 4, False),
        ([3, 5, 2, 8], 18, True),
        ([3, 5, 2, 8], 19, False),
        ([3, 5], 0, True),
        ([], 0, True),
        ([], 1, False),
        ([1, 1, 1], 3, True),
        ([1, 1, 1], 4, False),
    ],
)
def test_can_make(nums, target, expected):
    assert can_make(nums, target) is expected


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([3, 5, 2, 8], 10, [3, 5, 2]),
        ([3, 5, 2, 8], 7, [5, 2]),
        ([3, 5, 2, 8], 4, None),
        ([3, 5, 2, 8], 8, [3, 5]),
        ([3, 5, 2, 8], 13, [3, 2, 8]),
        ([3, 5], 0, []),
        ([], 1, None),
        ([1, 2, 3, 4], 10, [1, 2, 3, 4]),
        ([1, 2, 3, 4], 5, [1, 4]),
        ([5, 5, 5], 10, [5, 5]),
    ],
)
def test_make_one(nums, target, expected):
    assert make_one(nums, target) == expected


def test_make_one_does_not_change_nums():
    nums = [3, 5, 2, 8]
    make_one(nums, 7)
    assert nums == [3, 5, 2, 8]
