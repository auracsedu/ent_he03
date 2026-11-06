"""
문제 1. find 의 사촌들 (함수 3개)

수업 문제 2(my_find)처럼 "슬라이스로 잘라서 비교하기"만으로 문자열 메서드 세 개를
직접 만드세요. str.startswith(), str.endswith(), str.count(), str.find(), in 은
쓸 수 없습니다.

my_startswith(s, prefix)
- s 가 prefix 로 시작하면 True, 아니면 False 를 돌려줍니다.
- prefix 가 빈 문자열이면 True 입니다.

my_endswith(s, suffix)
- s 가 suffix 로 끝나면 True, 아니면 False 를 돌려줍니다.
- suffix 가 빈 문자열이면 True 입니다.

my_count(s, sub)
- s 안에 sub 가 몇 번 나오는지 돌려줍니다. 한 번 센 부분은 다시 세지 않습니다.
  ("aaaa" 에서 "aa" 는 2번입니다. 겹치는 1번째 자리는 세지 않습니다.)
- sub 는 빈 문자열이 아닙니다.

예시
    my_startswith("hello", "he")   -> True
    my_startswith("hello", "hello") -> True
    my_startswith("hello", "hell!") -> False
    my_startswith("he", "hello")   -> False
    my_startswith("hello", "")     -> True

    my_endswith("hello", "lo")     -> True
    my_endswith("hello", "l")      -> False
    my_endswith("", "a")           -> False
    my_endswith("hello", "")       -> True

    my_count("banana", "a")        -> 3
    my_count("banana", "an")       -> 2
    my_count("aaaa", "aa")         -> 2
    my_count("hello", "z")         -> 0

힌트
    - my_startswith 는 s[:len(prefix)] == prefix 한 줄입니다. s 가 prefix 보다
      짧으면 슬라이스가 짧게 잘려서 저절로 False 가 됩니다.
    - my_endswith 는 s[len(s) - len(suffix):] 과 비교하세요. s[-len(suffix):] 라고
      쓰면 suffix 가 빈 문자열일 때 s[-0:] == s[0:] 이 되어 s 전체가 나오니
      조심하세요. (-0 은 0 입니다)
    - my_count 는 수업 문제 3(my_replace)의 while 반복과 같습니다. 위치 i 를 0 부터
      움직이면서 s[i:i + len(sub)] == sub 이면 1 을 세고 i 를 len(sub) 만큼
      건너뛰고, 아니면 i 를 1 늘립니다. 건너뛰기 때문에 겹치는 것은 세지 않게
      됩니다.
"""


def my_startswith(s: str, prefix: str) -> bool:
    raise NotImplementedError


def my_endswith(s: str, suffix: str) -> bool:
    raise NotImplementedError


def my_count(s: str, sub: str) -> int:
    raise NotImplementedError
