"""
문제 5. 중첩 리스트 (함수 2개)

수업 문제 5(flatten)와 같은 중첩 리스트를 받아, 이번에는 리스트가 아니라 **숫자
하나**를 돌려주는 함수 두 개를 작성하세요. 원소는 정수이거나 리스트이고, 리스트는
몇 겹이든 중첩될 수 있습니다. 원래 리스트는 바꾸면 안 됩니다.

nested_sum(items)
- 안에 들어 있는 모든 정수의 합을 돌려줍니다. 빈 리스트는 0 입니다.

max_depth(items)
- 가장 깊이 중첩된 곳의 깊이를 돌려줍니다. 리스트 안에 리스트가 하나도 없으면
  깊이는 1 입니다. 빈 리스트도 1 입니다.

예시
    nested_sum([1, 2, 3])            -> 6
    nested_sum([1, [2, 3], 4])       -> 10
    nested_sum([1, [2, [3, [4]]]])   -> 10
    nested_sum([])                   -> 0
    nested_sum([[], [[]], []])       -> 0

    max_depth([1, 2, 3])             -> 1
    max_depth([])                    -> 1
    max_depth([1, [2, 3], 4])        -> 2
    max_depth([1, [2, [3, [4]]]])    -> 4
    max_depth([[], [[]], []])        -> 3
    max_depth([[1], [2], [3]])       -> 2

재귀로 생각하는 법
    flatten 과 똑같이 원소를 하나씩 보고 두 종류로 나눕니다. 다른 점은 "결과를
    어떻게 합치는가" 하나입니다.

        nested_sum: 정수면 더하고, 리스트면 nested_sum(그 리스트) 를 더합니다.
        max_depth:  정수는 깊이에 영향이 없습니다. 리스트면 1 + max_depth(그 리스트)
                    가 "그 안쪽까지 내려간 깊이"이고, 그중 가장 큰 값이 답입니다.

힌트
    - 어떤 값이 리스트인지 확인: isinstance(x, list)
    - max_depth 는 best = 1 로 시작해, 리스트 원소마다 best = max(best, 1 + max_depth(x))
      로 갱신하세요. 리스트 원소가 하나도 없으면 best 가 1 그대로 남아 종료 조건이
      저절로 됩니다. [[], [[]], []] 가 왜 3 인지 손으로 따라가 보세요.
    - 수업 문제 5 를 아직 못 풀었으면 그것부터 푸세요. 이 문제는 그 코드에서
      "결과에 넣는다"를 "더한다 / 최댓값을 고른다"로 바꾼 것입니다.
"""


def nested_sum(items: list) -> int:
    raise NotImplementedError


def max_depth(items: list) -> int:
    raise NotImplementedError
