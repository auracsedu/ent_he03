"""
문제 4. 재귀 워밍업 (함수 3개)

for / while 없이, 함수가 자기 자신을 부르는 재귀만으로 세 함수를 작성하세요.
수업 문제 5(flatten)에서 본 "함수가 자기 자신을 부른다"를 가장 작은 문제에서
손에 익히는 단계입니다.

digit_sum(n)
- 0 이상의 정수 n 의 각 자릿수의 합을 돌려줍니다.

to_binary(n)
- 0 이상의 정수 n 을 2진법 문자열로 돌려줍니다. bin() 은 쓸 수 없습니다.
- to_binary(0) 은 "0" 입니다. 그 밖에는 맨 앞에 0 이 오지 않습니다.

my_reverse(s)
- 문자열 s 를 거꾸로 뒤집은 문자열을 돌려줍니다. 슬라이스 s[::-1] 과 reversed() 는
  쓸 수 없습니다.

예시
    digit_sum(0)      -> 0
    digit_sum(7)      -> 7
    digit_sum(1234)   -> 10
    digit_sum(99999)  -> 45

    to_binary(0)      -> "0"
    to_binary(1)      -> "1"
    to_binary(2)      -> "10"
    to_binary(10)     -> "1010"
    to_binary(255)    -> "11111111"

    my_reverse("")      -> ""
    my_reverse("a")     -> "a"
    my_reverse("abc")   -> "cba"
    my_reverse("hello") -> "olleh"

재귀로 생각하는 법
    세 문제 모두 "한 조각을 떼어 내고, 나머지는 같은 함수에 맡긴다" 입니다.

        digit_sum(1234)  = 4 + digit_sum(123)           마지막 자리 하나를 뗀다
        to_binary(10)    = to_binary(5) + "0"           마지막 비트 하나를 뗀다
        my_reverse("abc") = my_reverse("bc") + "a"      첫 글자 하나를 뗀다

    그리고 더 뗄 것이 없는 가장 작은 경우(종료 조건)에서 답을 바로 돌려줍니다.
    종료 조건을 빼먹으면 함수가 끝없이 자기를 불러 RecursionError 가 납니다.

힌트
    - digit_sum: n 이 10 보다 작으면 n 그대로입니다. 아니면 n % 10 + digit_sum(n // 10).
    - to_binary: n 이 0 또는 1 이면 "0" 또는 "1" 입니다. 아니면 to_binary(n // 2) 뒤에
      n % 2 를 글자로 붙입니다. 2 를 "10" 으로 만드는 과정을 손으로 따라가 보세요.
    - my_reverse: s 가 "" 이면 "" 입니다. 아니면 my_reverse(s[1:]) + s[0].
"""


def digit_sum(n: int) -> int:
    raise NotImplementedError


def to_binary(n: int) -> str:
    raise NotImplementedError


def my_reverse(s: str) -> str:
    raise NotImplementedError
