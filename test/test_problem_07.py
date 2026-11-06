import pytest

import problem_07 as memo


@pytest.mark.parametrize(
    "n, expected",
    [(0, 0), (1, 1), (2, 1), (10, 55), (20, 6765), (50, 12586269025), (90, 2880067194370816120)],
)
def test_fib(n, expected):
    assert memo.fib(n) == expected


def test_fib_fills_memo():
    memo.fib(30)
    assert memo.fib_memo[30] == 832040
    assert memo.fib_memo[29] == 514229
    assert memo.fib_memo[2] == 1


def test_fib_big_is_fast():
    # 메모가 없으면 이 줄은 끝나지 않습니다.
    assert memo.fib(300) == 222232244629420445529739893461909967206666939096499764990979600


@pytest.mark.parametrize(
    "n, expected",
    [(1, 0), (2, 1), (4, 2), (6, 8), (7, 16), (27, 111), (97, 118), (871, 178)],
)
def test_collatz_steps(n, expected):
    assert memo.collatz_steps(n) == expected


def test_collatz_fills_memo_along_the_way():
    memo.collatz_steps(6)
    for n, steps in [(6, 8), (3, 7), (10, 6), (5, 5), (16, 4), (8, 3), (4, 2), (2, 1), (1, 0)]:
        assert memo.collatz_memo[n] == steps


def test_collatz_many():
    longest = max(range(1, 10001), key=memo.collatz_steps)
    assert longest == 6171
    assert memo.collatz_steps(6171) == 261
