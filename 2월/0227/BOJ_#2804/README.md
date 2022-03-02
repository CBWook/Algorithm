## 문제

창영이는 크로스워드 퍼즐을 만들려고 한다.

두 단어 A와 B가 주어진다. A는 가로로 놓여야 하고, B는 세로로 놓여야 한다. 또, 두 단어는 서로 교차해야 한다. (정확히 한 글자를 공유해야 한다) 공유하는 글자는 A와 B에 동시에 포함되어 있는 글자여야 하고, 그런 글자가 여럿인 경우 A에서 제일 먼저 등장하는 글자를 선택한다. 마찬가지로 이 글자가 B에서도 여러 번 등장하면 B에서 제일 처음 나오는 것을 선택한다. 예를 들어, A = "ABBA"이고, B = "CCBB"라면, 아래와 같이 만들 수 있다.

```
.C..
.C..
ABBA
.B..
```

## 입력

첫째 줄에 두 단어 A와 B가 주어진다. 두 단어는 30글자 이내이고, 공백으로 구분되어져 있다. 또, 대문자로만 이루어져 있고, 적어도 한 글자는 두 단어에 포함되어 있다.

## 출력

A의 길이를 N, B의 길이를 M이라고 했을 때, 출력은 총 M줄이고, 각 줄에는 N개 문자가 있어야 한다. 문제 설명에 나온 것 같이 두 단어가 교차된 형태로 출력되어야 한다. 나머지 글자는 '.'로 출력한다.

## 예제 입력 1 복사

```
BANANA PIDZAMA
```

## 예제 출력 1 복사

```
.P....
.I....
.D....
.Z....
BANANA
.M....
.A....
```

## 예제 입력 2 복사

```
MAMA TATA
```

## 예제 출력 2 복사

```
.T..
MAMA
.T..
.A..
```

## 예제 입력 3 복사

```
REPUBLIKA HRVATSKA
```

## 예제 출력 3 복사

```
H........
REPUBLIKA
V........
A........
T........
S........
K........
A........
```

## 출처

[Contest](https://www.acmicpc.net/category/45) > [Croatian Open Competition in Informatics](https://www.acmicpc.net/category/17) > [COCI 2011/2012](https://www.acmicpc.net/category/19) > [Contest #5](https://www.acmicpc.net/category/detail/72) 1번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 문제의 오타를 찾은 사람: [cth0629](https://www.acmicpc.net/user/cth0629), [jang3661](https://www.acmicpc.net/user/jang3661), [silvercube](https://www.acmicpc.net/user/silvercube)
- 빠진 조건을 찾은 사람: [jung2381187](https://www.acmicpc.net/user/jung2381187)

