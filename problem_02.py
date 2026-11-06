"""
문제 2. 공백 다루기 (함수 2개)

str.strip() 과 인자 없는 str.split() 을 직접 만드세요. str.strip(), str.lstrip(),
str.rstrip(), str.split() 은 쓸 수 없습니다.

my_strip(s, chars=" ")
- s 의 양 끝에서 chars 에 들어 있는 글자를 모두 떼어 낸 문자열을 돌려줍니다.
- chars 는 "떼어 낼 글자들의 모음"입니다. chars 가 ".,!" 이면 ".", ",", "!" 중
  무엇이든 떼어 냅니다.
- chars 를 주지 않으면 공백 " " 만 떼어 냅니다. (기본값 인자)
- s 가 전부 떼어 낼 글자로만 되어 있으면 "" 입니다.
- 가운데에 있는 글자는 건드리지 않습니다.

my_words(s)
- s 를 공백으로 나눈 단어들의 리스트를 돌려줍니다. 공백은 " ", "\\t", "\\n" 세 가지입니다.
- 수업 문제 1(my_split)과 달리 공백이 연달아 있어도 빈 조각 "" 은 만들지 않습니다.
- 양 끝의 공백도 무시합니다. s 가 비어 있거나 공백만 있으면 [] 입니다.

예시
    my_strip("  hello  ")          -> "hello"
    my_strip("hello")              -> "hello"
    my_strip("   ")                -> ""
    my_strip("a  b")               -> "a  b"
    my_strip("...hi!!", ".!")      -> "hi"
    my_strip("xxhixx", "x")        -> "hi"
    my_strip("  hi  ", "x")        -> "  hi  "

    my_words("a b c")              -> ["a", "b", "c"]
    my_words("  a   b  ")          -> ["a", "b"]
    my_words("a\\tb\\nc")            -> ["a", "b", "c"]
    my_words("")                   -> []
    my_words("   ")                -> []

힌트
    - my_strip: 왼쪽 끝 i 는 0 에서 시작해 s[i] in chars 인 동안 1 씩 늘리고, 오른쪽
      끝 j 는 len(s) 에서 시작해 s[j - 1] in chars 인 동안 1 씩 줄입니다. 답은
      s[i:j] 입니다. 두 while 모두 "i < len(s)", "j > i" 같은 범위 조건을 and 로
      먼저 걸어야 전부 공백인 문자열에서 인덱스 오류가 나지 않습니다.
    - my_words: 수업 문제 1 처럼 piece 를 모으되, 공백을 만났을 때 piece 가 "" 이면
      결과에 넣지 않고 넘어가면 빈 조각이 생기지 않습니다. 반복이 끝난 뒤
      마지막 piece 도 "" 이 아닐 때만 넣으세요.
    - "공백인가"는 ch in " \\t\\n" 으로 확인합니다.
"""

from typing import List


def my_strip(s: str, chars: str = " ") -> str:
    raise NotImplementedError


def my_words(s: str) -> List[str]:
    raise NotImplementedError
