"""
문제 6. 부분집합 (함수 2개)

subsets(items)
- 리스트 items 의 모든 부분집합을 리스트의 리스트로 돌려줍니다. itertools 는 쓸 수
  없습니다.
- 각 부분집합 안의 순서는 items 에 나온 순서를 따릅니다.
- 부분집합들의 순서는 "맨 앞 원소를 쓴 것"이 먼저입니다. (수업 문제 7 과 같은
  규칙입니다. 아래 예시를 보세요.)
- items 가 빈 리스트면 빈 부분집합 하나를 담은 [[]] 를 돌려줍니다.
- items 에 같은 값은 없습니다.

subsets_with_sum(items, target)
- items 의 부분집합 중 원소의 합이 target 인 것만, subsets 와 같은 순서로
  돌려줍니다. 없으면 [] 입니다.

예시
    subsets([1, 2, 3])
        -> [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    subsets([1])     -> [[1], []]
    subsets([])      -> [[]]

    subsets_with_sum([1, 2, 3], 3)        -> [[1, 2], [3]]
    subsets_with_sum([1, 2, 3], 6)        -> [[1, 2, 3]]
    subsets_with_sum([1, 2, 3], 0)        -> [[]]
    subsets_with_sum([1, 2, 3], 7)        -> []
    subsets_with_sum([3, 5, 2, 8], 10)    -> [[3, 5, 2], [2, 8]]

재귀로 생각하는 법
    수업 문제 7(combinations)에서 r 을 떼어 낸 문제입니다. 맨 앞 원소를 보고
    두 경우로 나눕니다.

        쓴다   -> 나머지의 부분집합 하나하나 앞에 items[0] 을 붙인다
        안 쓴다 -> 나머지의 부분집합을 그대로 쓴다

    "나머지의 부분집합"은 subsets(items[1:]) 가 알고 있습니다. r 이 없으므로
    종료 조건은 하나, items 가 비었을 때 [[]] 입니다.

힌트
    - 원소가 n 개면 부분집합은 2**n 개입니다. [1, 2, 3] 은 8 개입니다.
    - subsets 안에서 subsets(items[1:]) 는 **한 번만** 부르고 변수에 받아 두세요.
      "쓴다"와 "안 쓴다" 양쪽에서 같은 결과를 쓰기 때문입니다.
    - subsets_with_sum 은 subsets(items) 의 결과를 돌면서 sum(부분집합) == target
      인 것만 모으면 됩니다. 재귀를 새로 쓰지 않아도 됩니다.
"""

from typing import List


def subsets(items: list) -> List[list]:
    raise NotImplementedError


def subsets_with_sum(items: List[int], target: int) -> List[List[int]]:
    raise NotImplementedError
