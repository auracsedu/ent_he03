"""
문제 8. 고르고 되돌리기 (함수 2개)

양의 정수 리스트 nums 에서 몇 개를 골라(각 수는 한 번만) 합이 target 이 되게
만드는 문제입니다. 문제 6 처럼 부분집합을 전부 만들어 놓고 고르는 대신, 재귀가
내려가는 **도중에** 지금까지 고른 수를 리스트에 넣고 되돌아올 때 빼는 방식으로
쓰세요. 수업 extra 2(백트래킹)에서 set 에 넣고 빼던 것과 같은 모양입니다.

can_make(nums, target)
- 합이 target 인 고르기가 하나라도 있으면 True, 없으면 False 를 돌려줍니다.
- target 이 0 이면 아무것도 안 고르면 되므로 True 입니다.

make_one(nums, target)
- 합이 target 이 되게 고른 수들의 리스트를 **하나만** 돌려줍니다. 없으면 None 을
  돌려줍니다.
- 여러 가지가 있으면 "앞쪽 수를 쓰는 쪽을 먼저 시도"해서 가장 먼저 찾아지는 것을
  돌려줍니다. 돌려주는 리스트 안의 순서는 nums 에 나온 순서입니다.
- target 이 0 이면 [] 입니다.

예시
    can_make([3, 5, 2, 8], 10)    -> True     # 3 + 5 + 2 또는 2 + 8
    can_make([3, 5, 2, 8], 7)     -> True     # 5 + 2
    can_make([3, 5, 2, 8], 4)     -> False
    can_make([3, 5], 0)           -> True
    can_make([], 1)               -> False

    make_one([3, 5, 2, 8], 10)    -> [3, 5, 2]   # [2, 8] 보다 먼저 찾아짐
    make_one([3, 5, 2, 8], 7)     -> [5, 2]
    make_one([3, 5, 2, 8], 4)     -> None
    make_one([3, 5], 0)           -> []
    make_one([1, 2, 3, 4], 10)    -> [1, 2, 3, 4]

재귀로 생각하는 법
    수업 문제 9 처럼 재귀 함수를 하나 더 만듭니다.

        go(i, remaining) = "nums[i] 부터 보기 시작해서 remaining 을 만들 수 있는가?"

        1) remaining 이 0 이면 True (다 만들었습니다)
        2) i 가 nums 의 끝이거나 remaining 이 0 보다 작으면 False
        3) nums[i] 를 쓰는 경우 go(i + 1, remaining - nums[i]) 와
           안 쓰는 경우 go(i + 1, remaining) 중 하나라도 True 면 True

    make_one 은 여기에 "지금까지 고른 수" 리스트 chosen 을 하나 두고,
    쓰는 경우로 들어가기 **전에** chosen.append(nums[i]) 하고, 그 경우가 실패해서
    돌아오면 chosen.pop() 으로 되돌립니다. 성공해서 돌아오면 chosen 이 그대로 답입니다.

힌트
    - go 는 파일 맨 위에 따로 함수로 만들어도 되고, can_make 안에 def 로 만들어도
      됩니다. 안에 만들면 nums 를 인자로 넘기지 않아도 보입니다.
    - make_one 에서 chosen 은 리스트(가변 객체)라서 go 안에서 append / pop 해도 밖의
      chosen 이 함께 바뀝니다. 그래서 go 가 True 를 돌려주면 make_one 은 chosen 을
      그대로 돌려주면 됩니다. (리스트를 복사해서 돌려주고 싶으면 chosen[:] 또는
      list(chosen))
    - pop 을 빼먹으면 실패한 경로의 수가 남아 [3, 5, 2, 8], 7 에서 [3, 5, 2] 같은 틀린
      답이 나옵니다. append 와 pop 이 한 쌍이라는 것이 이 문제의 핵심이고, 수업 extra 2 에서
      본 백트래킹의 뼈대입니다.
"""

from typing import List, Optional


def can_make(nums: List[int], target: int) -> bool:
    raise NotImplementedError


def make_one(nums: List[int], target: int) -> Optional[List[int]]:
    raise NotImplementedError
